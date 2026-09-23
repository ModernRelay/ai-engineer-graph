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
from bench.arms import markdown_gate, omnigraph_gate
from bench.probe import evaluate, probe_prompt, probe_steps

REPO = Path("/repo")
HOME = Path("/home/me")
CHECKS = [
    "tools",
    "no_mcp_or_plugins",
    "model",
    "steps_attempted",
    "gate_enforced",
    "control_call_worked",
    "nothing_leaked",
    "finished",
]


def subject_input(tool: str, target: str) -> dict:
    field = {"Bash": "command", "Read": "file_path", "Grep": "path", "Glob": "pattern"}[tool]
    extra = {"Grep": {"pattern": "Anthropic"}}.get(tool, {})
    return {field: target, **extra}


BUILTIN_PLUGIN = {"name": "telemetry", "path": "builtin", "source": "telemetry@builtin"}


def session(arm, calls, tools=None, finished=True, plugins=None) -> list[dict]:
    """A serialized session: init, one tool call + result per entry, then the result."""
    tools = tools or {"markdown": ["Read", "Grep", "Glob"], "omnigraph": ["Bash", "Read"]}[arm]
    messages = [
        SystemMessage(
            subtype="init",
            data={
                "tools": tools,
                "mcp_servers": [],
                "plugins": [BUILTIN_PLUGIN] if plugins is None else plugins,
                # what CLI 2.1.280 reports with the 1M id (assistant messages carry the API id)
                "model": "anthropic/claude-sonnet-5[1m]",
            },
        )
    ]
    for n, (tool, tool_input, result, is_error) in enumerate(calls):
        messages.append(
            AssistantMessage(
                content=[
                    TextBlock(text="next step"),
                    ToolUseBlock(id=f"t{n}", name=tool, input=tool_input),
                ],
                model="anthropic/claude-sonnet-5",
            )
        )
        messages.append(
            UserMessage(
                content=[ToolResultBlock(tool_use_id=f"t{n}", content=result, is_error=is_error)]
            )
        )
    if finished:
        messages.append(
            ResultMessage(
                subtype="success",
                duration_ms=1000,
                duration_api_ms=900,
                is_error=False,
                num_turns=len(calls) + 1,
                session_id="s",
                usage={"input_tokens": 10, "output_tokens": 5},
            )
        )
    return [json.loads(json.dumps(serialize(m), default=str)) for m in messages]


def honest_calls(arm, gate, steps, results=None):
    """Every step attempted; denials carry the gate's reason, allowed calls return data."""
    results = results or {}
    calls = []
    for step in steps:
        tool_input = subject_input(step.tool, step.target)
        reason = gate(step.tool, tool_input)
        if step.id in results:
            calls.append((step.tool, tool_input, *results[step.id]))
        elif reason:
            calls.append((step.tool, tool_input, f"PreToolUse hook denied this: {reason}", True))
        else:
            ok = {
                "markdown": "ia-aie-alpha-talk.md\nia-aie-beta-talk.md",
                "omnigraph": "pat-verification-gap 375",
            }
            calls.append((step.tool, tool_input, ok[arm], False))
    return calls


def failing(checks):
    return {c["check"]: c["detail"] for c in checks if not c["ok"]}


@pytest.fixture
def markdown(tmp_path):
    workdir = tmp_path / "talks"
    workdir.mkdir()
    return markdown_gate(workdir), probe_steps("markdown", REPO, HOME)


@pytest.fixture
def omnigraph(tmp_path):
    workdir = tmp_path / "scratch"
    workdir.mkdir()
    return omnigraph_gate(workdir), probe_steps("omnigraph", REPO, HOME)


# ── the trace format ────────────────────────────────────────────────────────


def test_serialize_keeps_the_message_kind_and_its_blocks():
    message = AssistantMessage(
        content=[
            TextBlock(text="hi"),
            ToolUseBlock(id="t1", name="Read", input={"file_path": "/x"}),
        ],
        model="anthropic/claude-sonnet-5",
    )

    out = serialize(message)

    assert out["kind"] == "AssistantMessage"
    assert out["content"][1] == {"id": "t1", "name": "Read", "input": {"file_path": "/x"}}
    assert json.loads(json.dumps(out))["model"] == "anthropic/claude-sonnet-5"


# ── the probe itself ────────────────────────────────────────────────────────


def test_every_escape_step_is_one_the_gate_denies(markdown, omnigraph):
    for gate, steps in (markdown, omnigraph):
        decisions = {
            s.id: "deny" if gate(s.tool, subject_input(s.tool, s.target)) else "allow"
            for s in steps
        }
        assert decisions == {s.id: s.expect for s in steps}
        assert list(decisions.values()).count("allow") == 1


def test_prompt_spells_out_every_step_target_exactly(markdown):
    _, steps = markdown

    prompt = probe_prompt(steps)

    assert all(s.id in prompt and s.target in prompt for s in steps)


def test_a_clean_markdown_session_passes_every_check(markdown):
    gate, steps = markdown

    checks = evaluate(
        session("markdown", honest_calls("markdown", gate, steps)), "markdown", gate, steps
    )

    assert [c["check"] for c in checks] == CHECKS
    assert failing(checks) == {}


def test_a_clean_omnigraph_session_passes_every_check(omnigraph):
    gate, steps = omnigraph

    checks = evaluate(
        session("omnigraph", honest_calls("omnigraph", gate, steps)), "omnigraph", gate, steps
    )

    assert failing(checks) == {}


def test_a_call_the_gate_should_have_denied_but_went_through_fails(markdown):
    gate, steps = markdown
    readme = {"M2": ("# AI Engineer Graph\n\nA knowledge graph of ...", False)}

    checks = evaluate(
        session("markdown", honest_calls("markdown", gate, steps, readme)), "markdown", gate, steps
    )

    assert set(failing(checks)) == {"gate_enforced", "nothing_leaked"}
    assert "README.md" in failing(checks)["gate_enforced"]


def test_a_denial_that_did_not_come_from_our_gate_fails(markdown):
    gate, steps = markdown
    other = {"M3": ("Permission to read this file was denied.", True)}

    checks = evaluate(
        session("markdown", honest_calls("markdown", gate, steps, other)), "markdown", gate, steps
    )

    assert set(failing(checks)) == {"gate_enforced"}


def test_a_skipped_step_is_reported(markdown):
    gate, steps = markdown
    calls = [
        c for c, s in zip(honest_calls("markdown", gate, steps), steps, strict=True) if s.id != "M5"
    ]

    checks = evaluate(session("markdown", calls), "markdown", gate, steps)

    assert set(failing(checks)) == {"steps_attempted"}
    assert "M5" in failing(checks)["steps_attempted"]


def test_an_extra_tool_in_the_session_fails_the_tool_check(markdown):
    gate, steps = markdown
    trace = session(
        "markdown", honest_calls("markdown", gate, steps), tools=["Read", "Grep", "Glob", "Bash"]
    )

    assert set(failing(evaluate(trace, "markdown", gate, steps))) == {"tools"}


def test_a_failed_control_call_is_reported(omnigraph):
    gate, steps = omnigraph
    down = {"O1": ("error: connection refused (127.0.0.1:8081)", True)}

    checks = evaluate(
        session("omnigraph", honest_calls("omnigraph", gate, steps, down)), "omnigraph", gate, steps
    )

    assert set(failing(checks)) == {"control_call_worked"}


def test_a_session_without_a_result_is_unfinished(omnigraph):
    gate, steps = omnigraph
    trace = session("omnigraph", honest_calls("omnigraph", gate, steps), finished=False)

    assert set(failing(evaluate(trace, "omnigraph", gate, steps))) == {"finished"}


# ── `bench probe` pre-flight ────────────────────────────────────────────────


def test_probe_command_refuses_to_start_with_graph_credentials_in_the_environment(
    monkeypatch, capsys
):
    from bench.cli import main

    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "x")
    monkeypatch.setenv("TOKEN_ACT_ANALYST", "y")

    with pytest.raises(SystemExit) as exit_:
        main(["probe", "--arm", "markdown"])

    assert exit_.value.code != 0
    err = capsys.readouterr().err
    assert "AWS_SECRET_ACCESS_KEY" in err and "TOKEN_ACT_ANALYST" in err


def test_a_user_plugin_in_the_session_fails_the_plugin_check(markdown):
    gate, steps = markdown
    user_plugin = {"name": "superpowers", "path": "/x", "source": "superpowers@claude-plugins"}
    trace = session(
        "markdown", honest_calls("markdown", gate, steps), plugins=[BUILTIN_PLUGIN, user_plugin]
    )

    failures = failing(evaluate(trace, "markdown", gate, steps))

    assert set(failures) == {"no_mcp_or_plugins"}
    assert "superpowers" in failures["no_mcp_or_plugins"]
