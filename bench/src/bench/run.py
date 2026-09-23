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
from bench.provider import cost_usd, session_cost
from bench.questions import Question
from bench.trace import init_data, result_message, tool_uses

# result.json token fields ← the CLI's per-model tally (ResultMessage.model_usage)
TOKEN_FIELDS = {
    "input_tokens": "inputTokens",
    "output_tokens": "outputTokens",
    "cache_read_input_tokens": "cacheReadInputTokens",
    "cache_creation_input_tokens": "cacheCreationInputTokens",
}


WALL_TIMEOUT_S = 30 * 60
RETRY_DELAYS_S = (30, 60)  # waits before the 2nd and 3rd attempt
# API statuses worth another attempt: rate limits, server errors, "overloaded".
RETRYABLE_STATUS = {429, 500, 502, 503, 504, 529}


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
        "cost_complete": bool(result),
        "answer_text": answer,
        "answer_json": answer_block(answer),
        "model": init.get("model"),
        "cli_version": init.get("claude_code_version"),
    }


def partial_cost(trace: list[dict]) -> float:
    """Cost from per-message usage, for sessions that never reached a result. It undercounts."""
    total = 0.0
    for m in trace:
        if m["kind"] == "AssistantMessage" and m.get("usage"):
            try:
                total += cost_usd(m.get("model") or "", m["usage"])
            except KeyError:
                pass
    return round(total, 6)


def _retryable(trace: list[dict]) -> bool:
    result = result_message(trace)
    return bool(
        result and result.get("is_error") and result.get("api_error_status") in RETRYABLE_STATUS
    )


def _run_dir(out_root: Path, planned: Planned) -> Path:
    return out_root / planned.question.id / planned.arm / str(planned.run)


def _sandbox(planned: Planned, bench_dir: Path, work: Path, provider_env: dict[str, str]):
    """A fresh workdir and Claude home for one attempt: (options, gate)."""
    shutil.rmtree(work, ignore_errors=True)
    home = work / "claude-home"
    home.mkdir(parents=True)
    if planned.arm == "markdown":
        workdir = work / "talks"
        shutil.copytree(bench_dir / "corpus" / "talks", workdir)
        prompt = system_prompt("markdown", workdir)
        return markdown_options(workdir, prompt, provider_env, home), markdown_gate(workdir)
    workdir = work / "scratch"
    workdir.mkdir()
    prompt = system_prompt("omnigraph", workdir)
    options = omnigraph_options(workdir, prompt, bench_dir / "bin", provider_env, home)
    return options, omnigraph_gate(workdir)


async def run_one(
    planned: Planned,
    *,
    bench_dir: Path,
    out_root: Path,
    work_root: Path,
    provider_env: dict[str, str],
    meta: dict,
    agent=run_agent,
    wall_timeout: float = WALL_TIMEOUT_S,
    retry_delays: tuple[float, ...] = RETRY_DELAYS_S,
) -> dict:
    q = planned.question
    work = work_root / q.id / planned.arm / str(planned.run)
    started_at = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    retries: list[str] = []
    retry_cost = 0.0
    attempts = len(retry_delays) + 1

    for attempt in range(1, attempts + 1):
        options, gate = _sandbox(planned, bench_dir, work, provider_env)
        trace: list[dict] = []
        try:
            _, wall_s = await asyncio.wait_for(agent(q.text, options, trace), timeout=wall_timeout)
        except TimeoutError:  # a cap, not an infrastructure failure: never retried
            summary = summarize(trace, wall_timeout, gate)
            summary.update(status="capped", stop_reason="wall_timeout")
            summary.update(cost_usd=partial_cost(trace), cost_complete=False)
            break
        except Exception as e:  # an infrastructure failure, not an answer
            failure = f"{type(e).__name__}: {e}"
            summary = {"status": "error", "stop_reason": failure}
            summary.update(cost_usd=partial_cost(trace), cost_complete=False)
        else:
            summary = summarize(trace, wall_s, gate)
            if not _retryable(trace):
                break
            failure = f"api_error_status {result_message(trace).get('api_error_status')}"
        if attempt == attempts:
            break
        retries.append(failure)
        retry_cost += summary.get("cost_usd") or 0.0
        await asyncio.sleep(retry_delays[attempt - 1])

    record = {
        "qid": q.id,
        "arm": planned.arm,
        "run": planned.run,
        "question": q.text,
        "started_at": started_at,
        **summary,
        "attempts": attempt,
        "retries": retries,
        "retry_cost_usd": round(retry_cost, 6),
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
    max_spend: float | None = None,
    **kw,
) -> list[dict]:
    """Every planned run without a result.json. Once finished runs have spent `max_spend`,
    no new run starts (runs already going finish, so the total can overshoot a little)."""
    todo = [p for p in planned if not (_run_dir(kw["out_root"], p) / "result.json").exists()]
    slots = asyncio.Semaphore(concurrency)
    spent = 0.0

    async def one(p: Planned) -> dict | None:
        nonlocal spent
        async with slots:
            if max_spend is not None and spent >= max_spend:
                return None
            record = await run_one(p, **kw)
            spent += (record.get("cost_usd") or 0.0) + record.get("retry_cost_usd", 0.0)
        if on_done:
            on_done(record)
        return record

    return [r for r in await asyncio.gather(*(one(p) for p in todo)) if r is not None]
