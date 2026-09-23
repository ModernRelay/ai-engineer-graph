"""The Opus 5.5 judge, through OpenRouter (D1.3 on). Every request is cached on disk under a
hash of the whole request, prompt included, so rescoring never pays twice and every verdict
in the report traces back to a stored response. The judge is never told which arm wrote what.
"""

import hashlib
import json
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

import anthropic

from bench.prompts import PROMPTS_DIR
from bench.provider import BASE_URL, JUDGE_MODEL, openrouter_env

BENCH_DIR = Path(__file__).resolve().parents[2]
CACHE_DIR = BENCH_DIR / "runs" / "_judge"
MAX_TOKENS = 16000  # thinking counts against it; the verdict itself is short
EFFORT = "high"  # Opus 5.5 defaults to medium

VERDICTS = ["supported", "partial", "unsupported"]
SUPPORT_SCHEMA = {
    "type": "object",
    "properties": {
        "verdict": {"type": "string", "enum": VERDICTS},
        "reason": {"type": "string"},
    },
    "required": ["verdict", "reason"],
    "additionalProperties": False,
}

# request -> {"output": parsed JSON, "usage": {...}, "model": str, "id": str}
Ask = Callable[[dict], dict]


class JudgeError(Exception):
    pass


@dataclass(frozen=True)
class Support:
    verdict: str  # supported | partial | unsupported
    reason: str


def support_request(claim: str, item: str, quote: str, context: str) -> dict:
    parts = [f"<claim>{claim}</claim>"]
    if item:
        parts.append(f"<list_entry>{item}</list_entry>")
    parts += [f"<quote>{quote}</quote>", f"<transcript>\n{context}\n</transcript>"]
    return {
        "model": JUDGE_MODEL,
        "max_tokens": MAX_TOKENS,
        "system": (PROMPTS_DIR / "judge_support.md").read_text(encoding="utf-8"),
        "messages": [{"role": "user", "content": "\n\n".join(parts)}],
        "output_config": {
            "effort": EFFORT,
            "format": {"type": "json_schema", "schema": SUPPORT_SCHEMA},
        },
    }


def support(
    claim: str, item: str, quote: str, context: str, *, ask: Ask, cache_dir: Path = CACHE_DIR
) -> Support:
    """Does the quote, read in its transcript context, support the claim?"""

    def valid(output: dict) -> bool:
        return output.get("verdict") in VERDICTS and isinstance(output.get("reason"), str)

    output = cached(support_request(claim, item, quote, context), ask, cache_dir, valid)["output"]
    return Support(output["verdict"], output["reason"])


def cached(
    request: dict, ask: Ask, cache_dir: Path, valid: Callable[[dict], bool] = lambda _: True
) -> dict:
    """The saved record for this exact request, asking the judge only the first time."""
    key = hashlib.sha256(json.dumps(request, sort_keys=True).encode("utf-8")).hexdigest()
    path = cache_dir / f"{key}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    answer = ask(request)
    if not valid(answer["output"]):
        raise JudgeError(f"judge output outside the schema: {answer['output']!r}")
    record = {"request": request, **answer}
    cache_dir.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8")
    return record


def anthropic_ask(client) -> Ask:
    """An Ask over an `anthropic` client: sends the request, returns the parsed JSON verdict."""

    def ask(request: dict) -> dict:
        response = client.messages.create(**request)
        if response.stop_reason != "end_turn":
            raise JudgeError(f"judge stopped with {response.stop_reason}")
        text = next(block.text for block in response.content if block.type == "text")
        return {
            "output": json.loads(text),
            "usage": response.usage.to_dict(),
            "model": response.model,
            "id": response.id,
        }

    return ask


def openrouter_ask(env_file: Path) -> Ask:
    """The real judge: Opus 5.5 on OpenRouter, keyed by OPENROUTER_KEY in bench/.env."""
    token = openrouter_env(env_file)["ANTHROPIC_AUTH_TOKEN"]
    return anthropic_ask(anthropic.Anthropic(base_url=BASE_URL, auth_token=token, api_key=None))
