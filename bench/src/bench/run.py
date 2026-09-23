"""The benchmark runner: every (question, arm, run) in its own sandbox, with metrics.

Each run gets a fresh working directory outside the repo (a corpus copy for the
markdown arm, an empty scratch dir for the Omnigraph arm) and its own Claude
home. The full trace and a result.json land in runs/<qid>/<arm>/<n>/. A run that
already has a result.json is skipped, so `bench run` can be stopped and resumed.
"""

import asyncio
import json
import shutil
import time
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

import claude_agent_sdk

from bench.agent import run_agent
from bench.arms import markdown_gate, markdown_options, omnigraph_gate, omnigraph_options
from bench.parse import answer_block
from bench.prompts import system_prompt
from bench.provider import session_cost
from bench.questions import Question
from bench.trace import init_data, result_message, tool_uses

# result.json token fields ← the CLI's per-model tally (ResultMessage.model_usage)
TOKEN_FIELDS = {
    "input_tokens": "inputTokens",
    "output_tokens": "outputTokens",
    "cache_read_input_tokens": "cacheReadInputTokens",
    "cache_creation_input_tokens": "cacheCreationInputTokens",
}


@dataclass(frozen=True)
class Planned:
    question: Question
    arm: str
    run: int


def plan_runs(questions: list[Question], arms: list[str], runs: int) -> list[Planned]:
    """Run-major, then question, then arm: both arms see each question at about the same time."""
    return [Planned(q, arm, n) for n in range(1, runs + 1) for q in questions for arm in arms]


def _status(result: dict | None) -> tuple[str, str]:
    if result is None:
        return "error", "no result message"
    subtype = result.get("subtype") or ""
    if subtype == "success" and not result.get("is_error"):
        return "ok", subtype
    if subtype.startswith("error_max"):  # error_max_turns, error_max_budget_usd
        return "capped", subtype
    return "error", subtype or "error"


def summarize(trace: list[dict], wall_s: float, gate) -> dict:
    result = result_message(trace) or {}
    status, stop_reason = _status(result_message(trace))
    uses = tool_uses(trace)
    model_usage = result.get("model_usage") or {}
    answer = result.get("result") or ""
    init = init_data(trace)
    return {
        "status": status,
        "stop_reason": stop_reason,
        "wall_s": round(wall_s, 2),
        "duration_ms": result.get("duration_ms"),
        "duration_api_ms": result.get("duration_api_ms"),
        "num_turns": result.get("num_turns"),
        "cost_usd": round(session_cost(model_usage), 6),
        "sdk_cost_usd": result.get("total_cost_usd"),
        **{k: sum(t.get(v, 0) for t in model_usage.values()) for k, v in TOKEN_FIELDS.items()},
        "tool_calls": len(uses),
        "tool_calls_by_name": dict(Counter(u["name"] for u in uses)),
        "denied_tool_calls": sum(1 for u in uses if gate(u["name"], u["input"])),
        "answer_text": answer,
        "answer_json": answer_block(answer),
        "model": init.get("model"),
        "cli_version": init.get("claude_code_version"),
    }


def _run_dir(out_root: Path, planned: Planned) -> Path:
    return out_root / planned.question.id / planned.arm / str(planned.run)


async def run_one(
    planned: Planned,
    *,
    bench_dir: Path,
    out_root: Path,
    work_root: Path,
    provider_env: dict[str, str],
    meta: dict,
    agent=run_agent,
) -> dict:
    q, arm = planned.question, planned.arm
    work = work_root / q.id / arm / str(planned.run)
    shutil.rmtree(work, ignore_errors=True)
    home = work / "claude-home"
    home.mkdir(parents=True)
    if arm == "markdown":
        workdir = work / "talks"
        shutil.copytree(bench_dir / "corpus" / "talks", workdir)
        gate = markdown_gate(workdir)
        prompt = system_prompt("markdown", workdir)
        options = markdown_options(workdir, prompt, provider_env, home)
    else:
        workdir = work / "scratch"
        workdir.mkdir()
        gate = omnigraph_gate(workdir)
        prompt = system_prompt("omnigraph", workdir)
        options = omnigraph_options(workdir, prompt, bench_dir / "bin", provider_env, home)

    started_at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    trace: list[dict] = []
    try:
        trace, wall_s = await agent(q.text, options)
        summary = summarize(trace, wall_s, gate)
    except Exception as e:  # an infrastructure failure, not an answer
        summary = {"status": "error", "stop_reason": f"{type(e).__name__}: {e}"}

    record = {
        "qid": q.id,
        "arm": arm,
        "run": planned.run,
        "question": q.text,
        "started_at": started_at,
        **summary,
        **meta,
        "sdk_version": claude_agent_sdk.__version__,
    }
    out = _run_dir(out_root, planned)
    out.mkdir(parents=True, exist_ok=True)
    secret = provider_env["ANTHROPIC_AUTH_TOKEN"]

    def redact(text: str) -> str:
        return text.replace(secret, "<redacted>")

    lines = "".join(json.dumps(m, default=str) + "\n" for m in trace)
    (out / "trace.jsonl").write_text(redact(lines))
    (out / "result.json").write_text(redact(json.dumps(record, indent=2, default=str)))
    if record["status"] != "error":  # keep a failed run's workdir for debugging
        shutil.rmtree(work, ignore_errors=True)
    return record


async def run_all(
    planned: list[Planned],
    concurrency: int = 4,
    on_done: Callable[[dict], None] | None = None,
    **kw,
) -> list[dict]:
    todo = [p for p in planned if not (_run_dir(kw["out_root"], p) / "result.json").exists()]
    slots = asyncio.Semaphore(concurrency)

    async def one(p: Planned) -> dict:
        async with slots:
            record = await run_one(p, **kw)
        if on_done:
            on_done(record)
        return record

    return list(await asyncio.gather(*(one(p) for p in todo)))
