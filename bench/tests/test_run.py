import asyncio
import json
from pathlib import Path

import pytest
from claude_agent_sdk import (
    AssistantMessage,
    ResultMessage,
    SystemMessage,
    TextBlock,
    ToolResultBlock,
    ToolUseBlock,
    UserMessage,
)

from bench.agent import serialize
from bench.questions import Question
from bench.run import Planned, plan_runs, run_all, run_one

KEY = "test-openrouter-key-123"
PROVIDER = {
    "ANTHROPIC_BASE_URL": "https://openrouter.ai/api",
    "ANTHROPIC_AUTH_TOKEN": KEY,
    "ANTHROPIC_API_KEY": "",
}
META = {"graph_head": "01TESTHEAD", "corpus_sha": "abc123"}
ANSWER = (
    "Evals came up most.\n\n```json\n"
    '{"items": [{"label": "evals", "rank": 1, "talk_count": 2}], '
    '"claims": [{"item": "evals", "claim": "c", "talk": "ia-aie-a", "quote": "q"}]}\n```'
)
Q1 = Question("Q01", "aggregate", "ranked_list", "What was discussed most?")
Q2 = Question("Q02", "lookup", "prose", "How does Anthropic decide what to unship?")


@pytest.fixture
def bench(tmp_path):
    root = tmp_path / "bench"
    talks = root / "corpus" / "talks"
    talks.mkdir(parents=True)
    (talks / "ia-aie-a.md").write_text("# A\n- talk: ia-aie-a\n\nevals evals\n")
    (talks / "ia-aie-b.md").write_text("# B\n- talk: ia-aie-b\n\nmore evals\n")
    (root / "bin").mkdir()
    return root


def kwargs(bench, tmp_path, agent):
    return dict(
        bench_dir=bench,
        out_root=bench / "runs",
        work_root=tmp_path / "work",
        provider_env=PROVIDER,
        meta=META,
        agent=agent,
    )


def session(workdir: Path, subtype="success", answer=ANSWER, leak="") -> list[dict]:
    """Two tool calls (one the markdown gate denies), a final answer, the CLI's tallies."""
    messages = [
        SystemMessage(
            subtype="init",
            data={"model": "anthropic/claude-sonnet-5[1m]", "claude_code_version": "2.1.280"},
        ),
        AssistantMessage(
            content=[ToolUseBlock(id="t1", name="Grep", input={"pattern": "evals"})],
            model="anthropic/claude-sonnet-5",
        ),
        UserMessage(content=[ToolResultBlock(tool_use_id="t1", content=f"ia-aie-a.md:1{leak}")]),
        AssistantMessage(
            content=[ToolUseBlock(id="t2", name="Read", input={"file_path": "/etc/passwd"})],
            model="anthropic/claude-sonnet-5",
        ),
        UserMessage(content=[ToolResultBlock(tool_use_id="t2", content="denied", is_error=True)]),
        AssistantMessage(content=[TextBlock(text=answer)], model="anthropic/claude-sonnet-5"),
        ResultMessage(
            subtype=subtype,
            duration_ms=4200,
            duration_api_ms=3900,
            is_error=subtype != "success",
            num_turns=3,
            session_id="s",
            total_cost_usd=0.0306,
            result=answer,
            model_usage={
                "anthropic/claude-sonnet-5[1m]": {
                    "inputTokens": 1500,
                    "outputTokens": 600,
                    "cacheReadInputTokens": 44000,
                    "cacheCreationInputTokens": 5000,
                }
            },
        ),
    ]
    return [json.loads(json.dumps(serialize(m), default=str)) for m in messages]


class FakeAgent:
    """Stands in for run_agent: records what it was given, returns a canned session."""

    def __init__(self, **session_kw):
        self.calls = []
        self.session_kw = session_kw

    async def __call__(self, prompt, options):
        workdir = Path(options.cwd)
        self.calls.append(
            {
                "prompt": prompt,
                "cwd": workdir,
                "files": sorted(p.name for p in workdir.iterdir()),
                "system_prompt": options.system_prompt,
                "tools": options.tools,
                "claude_home": options.env["CLAUDE_CONFIG_DIR"],
            }
        )
        return session(workdir, **self.session_kw), 5.25


def result_of(bench, qid="Q01", arm="markdown", run=1) -> dict:
    return json.loads((bench / "runs" / qid / arm / str(run) / "result.json").read_text())


# ── planning ────────────────────────────────────────────────────────────────


def test_runs_interleave_arms_within_each_question_and_repeat_by_run():
    plan = plan_runs([Q1, Q2], ["markdown", "omnigraph"], runs=2)

    assert [(p.question.id, p.arm, p.run) for p in plan] == [
        ("Q01", "markdown", 1),
        ("Q01", "omnigraph", 1),
        ("Q02", "markdown", 1),
        ("Q02", "omnigraph", 1),
        ("Q01", "markdown", 2),
        ("Q01", "omnigraph", 2),
        ("Q02", "markdown", 2),
        ("Q02", "omnigraph", 2),
    ]


# ── one run ─────────────────────────────────────────────────────────────────


def test_a_run_records_its_metrics(bench, tmp_path):
    asyncio.run(run_one(Planned(Q1, "markdown", 1), **kwargs(bench, tmp_path, FakeAgent())))

    r = result_of(bench)
    assert (r["qid"], r["arm"], r["run"], r["status"]) == ("Q01", "markdown", 1, "ok")
    assert (r["wall_s"], r["duration_ms"], r["duration_api_ms"], r["num_turns"]) == (
        5.25,
        4200,
        3900,
        3,
    )
    assert r["tool_calls"] == 2
    assert r["tool_calls_by_name"] == {"Grep": 1, "Read": 1}
    assert r["denied_tool_calls"] == 1
    assert (r["input_tokens"], r["output_tokens"]) == (1500, 600)
    assert (r["cache_read_input_tokens"], r["cache_creation_input_tokens"]) == (44000, 5000)
    # 1500×2 + 600×10 + 44000×0.20 + 5000×2.50 per Mtok
    assert r["cost_usd"] == pytest.approx(0.0303)
    assert r["sdk_cost_usd"] == 0.0306
    assert r["answer_json"]["items"][0]["label"] == "evals"
    assert (r["graph_head"], r["corpus_sha"], r["cli_version"]) == (
        "01TESTHEAD",
        "abc123",
        "2.1.280",
    )


def test_a_run_keeps_the_full_trace(bench, tmp_path):
    asyncio.run(run_one(Planned(Q1, "markdown", 1), **kwargs(bench, tmp_path, FakeAgent())))

    trace = (bench / "runs" / "Q01" / "markdown" / "1" / "trace.jsonl").read_text().splitlines()
    assert [json.loads(line)["kind"] for line in trace][0] == "SystemMessage"
    assert len(trace) == 7


def test_the_prompt_is_the_question_and_the_markdown_agent_gets_a_fresh_corpus(bench, tmp_path):
    agent = FakeAgent()

    asyncio.run(run_one(Planned(Q1, "markdown", 1), **kwargs(bench, tmp_path, agent)))

    call = agent.calls[0]
    assert call["prompt"] == Q1.text
    assert call["files"] == ["ia-aie-a.md", "ia-aie-b.md"]
    assert not call["cwd"].is_relative_to(bench)
    assert str(call["cwd"]) in call["system_prompt"]
    assert call["tools"] == ["Read", "Grep", "Glob"]


def test_the_omnigraph_agent_gets_an_empty_scratch_dir_and_its_own_home(bench, tmp_path):
    agent = FakeAgent()

    asyncio.run(run_one(Planned(Q1, "omnigraph", 1), **kwargs(bench, tmp_path, agent)))

    call = agent.calls[0]
    assert call["files"] == [] and call["tools"] == ["Bash", "Read"]
    assert Path(call["claude_home"]).is_relative_to(tmp_path / "work")


def test_hitting_the_turn_cap_is_recorded_as_capped(bench, tmp_path):
    agent = FakeAgent(subtype="error_max_turns")

    asyncio.run(run_one(Planned(Q1, "markdown", 1), **kwargs(bench, tmp_path, agent)))

    assert result_of(bench)["status"] == "capped"
    assert result_of(bench)["stop_reason"] == "error_max_turns"


def test_an_agent_failure_is_recorded_as_an_error(bench, tmp_path):
    async def broken(prompt, options):
        raise RuntimeError("connection reset by peer")

    asyncio.run(run_one(Planned(Q1, "markdown", 1), **kwargs(bench, tmp_path, broken)))

    r = result_of(bench)
    assert r["status"] == "error"
    assert "connection reset" in r["stop_reason"]


def test_the_key_never_reaches_disk(bench, tmp_path):
    agent = FakeAgent(leak=f" token={KEY}")

    asyncio.run(run_one(Planned(Q1, "markdown", 1), **kwargs(bench, tmp_path, agent)))

    run_dir = bench / "runs" / "Q01" / "markdown" / "1"
    written = "".join(p.read_text() for p in run_dir.iterdir())
    assert KEY not in written and "<redacted>" in written


# ── many runs ───────────────────────────────────────────────────────────────


def test_finished_runs_are_skipped_so_a_run_can_resume(bench, tmp_path):
    agent = FakeAgent()
    done = bench / "runs" / "Q01" / "markdown" / "1"
    done.mkdir(parents=True)
    (done / "result.json").write_text('{"status": "ok"}')

    plan = plan_runs([Q1], ["markdown", "omnigraph"], runs=1)
    results = asyncio.run(run_all(plan, concurrency=2, **kwargs(bench, tmp_path, agent)))

    assert [c["tools"] for c in agent.calls] == [["Bash", "Read"]]
    assert [r["arm"] for r in results] == ["omnigraph"]


# ── `bench run` ─────────────────────────────────────────────────────────────


def test_run_command_refuses_to_start_with_graph_credentials(monkeypatch, capsys):
    from bench.cli import main

    monkeypatch.setenv("OMNIGRAPH_BEARER_TOKEN", "x")

    with pytest.raises(SystemExit) as exit_:
        main(["run", "--pilot", "--arm", "markdown"])

    assert exit_.value.code != 0
    assert "OMNIGRAPH_BEARER_TOKEN" in capsys.readouterr().err


def test_run_command_refuses_an_unknown_question_id(capsys):
    from bench.cli import main

    with pytest.raises(SystemExit):
        main(["run", "--pilot", "--only", "Q01,Q99"])

    assert "Q99" in capsys.readouterr().err


def test_corpus_fingerprint_changes_when_a_talk_changes(tmp_path):
    from bench.cli import corpus_sha

    (tmp_path / "ia-aie-a.md").write_text("one")
    before = corpus_sha(tmp_path)
    (tmp_path / "ia-aie-a.md").write_text("two")

    assert corpus_sha(tmp_path) != before and len(before) == 64
