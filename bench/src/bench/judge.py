"""The Opus 5.5 judge, through OpenRouter (D1.3 on). Every request is cached on disk under a
hash of the whole request, prompt included, so rescoring never pays twice and every verdict
in the report traces back to a stored response. The judge is never told which arm wrote what.
"""

import hashlib
import json
from collections import Counter
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

UNCITED_SCHEMA = {
    "type": "object",
    "properties": {"uncited": {"type": "array", "items": {"type": "string"}}},
    "required": ["uncited"],
    "additionalProperties": False,
}

CLUSTER_SCHEMA = {
    "type": "object",
    "properties": {
        "groups": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "members": {"type": "array", "items": {"type": "integer"}},
                },
                "required": ["name", "members"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["groups"],
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


def _request(prompt: str, content: str, schema: dict) -> dict:
    return {
        "model": JUDGE_MODEL,
        "max_tokens": MAX_TOKENS,
        "system": (PROMPTS_DIR / prompt).read_text(encoding="utf-8"),
        "messages": [{"role": "user", "content": content}],
        "output_config": {"effort": EFFORT, "format": {"type": "json_schema", "schema": schema}},
    }


def support_request(title: str, claim: str, item: str, quote: str, context: str) -> dict:
    parts = [f"<talk>{title}</talk>", f"<claim>{claim}</claim>"]
    if item:
        parts.append(f"<list_entry>{item}</list_entry>")
    parts += [f"<quote>{quote}</quote>", f"<transcript>\n{context}\n</transcript>"]
    return _request("judge_support.md", "\n\n".join(parts), SUPPORT_SCHEMA)


def uncited_request(prose: str, claims: list[tuple[str, str]]) -> dict:
    """claims: (list entry or "", claim text) for every claim in the answer's contract block."""
    lines = [f"- [{item}] {claim}" if item else f"- {claim}" for item, claim in claims]
    listed = "\n".join(lines) or "(none)"
    content = f"<answer>\n{prose}\n</answer>\n\n<claims>\n{listed}\n</claims>"
    return _request("judge_uncited.md", content, UNCITED_SCHEMA)


def cluster_request(question: str, labels: list[str]) -> dict:
    """The distinct labels, numbered in sorted order so no arm or run order shows."""
    numbered = "\n".join(f"{n}. {label}" for n, label in enumerate(sorted(set(labels)), 1))
    content = f"<question>{question}</question>\n\n<labels>\n{numbered}\n</labels>"
    return _request("judge_cluster.md", content, CLUSTER_SCHEMA)


def valid_clusters(count: int) -> Callable[[dict], bool]:
    """Every label number 1..count in exactly one named group."""

    def valid(output: dict) -> bool:
        groups = output.get("groups")
        if not isinstance(groups, list) or not all(isinstance(g, dict) for g in groups):
            return False
        members = [m for g in groups for m in g.get("members") or []]
        names_ok = all(isinstance(g.get("name"), str) for g in groups)
        return names_ok and sorted(members) == list(range(1, count + 1))

    return valid


def label_groups(labels: list[str], groups: list[dict]) -> dict[str, str]:
    """label -> group name; a name the judge used twice gets a suffix so the groups stay apart."""
    distinct, seen, out = sorted(set(labels)), Counter(), {}
    for group in groups:
        seen[group["name"]] += 1
        name = (
            group["name"]
            if seen[group["name"]] == 1
            else f"{group['name']} ({seen[group['name']]})"
        )
        for member in group["members"]:
            out[distinct[member - 1]] = name
    return out


def clusters(
    question: str, labels: list[str], *, ask: Ask, cache_dir: Path = CACHE_DIR
) -> dict[str, str]:
    """Every distinct label mapped to its canonical group."""
    request = cluster_request(question, labels)
    record = cached(request, ask, cache_dir, valid_clusters(len(set(labels))))
    return label_groups(labels, record["output"]["groups"])


def valid_support(output: dict) -> bool:
    return output.get("verdict") in VERDICTS and isinstance(output.get("reason"), str)


def valid_uncited(output: dict) -> bool:
    listed = output.get("uncited")
    return isinstance(listed, list) and all(isinstance(s, str) for s in listed)


def uncited(
    prose: str, claims: list[tuple[str, str]], *, ask: Ask, cache_dir: Path = CACHE_DIR
) -> list[str]:
    """The factual statements in the prose that none of the answer's claims covers."""
    request = uncited_request(prose, claims)
    return cached(request, ask, cache_dir, valid_uncited)["output"]["uncited"]


def support(
    title: str,
    claim: str,
    item: str,
    quote: str,
    context: str,
    *,
    ask: Ask,
    cache_dir: Path = CACHE_DIR,
) -> Support:
    """Does the quote, read in its transcript context, support the claim?"""
    request = support_request(title, claim, item, quote, context)
    output = cached(request, ask, cache_dir, valid_support)["output"]
    return Support(output["verdict"], output["reason"])


def request_key(request: dict) -> str:
    """SHA-256 of the request's canonical JSON: the cache key, and the calibration fixture's."""
    return hashlib.sha256(json.dumps(request, sort_keys=True).encode("utf-8")).hexdigest()


def cache_path(request: dict, cache_dir: Path) -> Path:
    return cache_dir / f"{request_key(request)}.json"


def lookup(request: dict, cache_dir: Path) -> dict | None:
    """The saved record for this exact request, or None if it was never asked."""
    path = cache_path(request, cache_dir)
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def cached(
    request: dict, ask: Ask, cache_dir: Path, valid: Callable[[dict], bool] = lambda _: True
) -> dict:
    """The saved record for this exact request, asking the judge only the first time."""
    if (record := lookup(request, cache_dir)) is not None:
        return record
    answer = ask(request)
    if not valid(answer["output"]):
        raise JudgeError(f"judge output outside the schema: {answer['output']!r}")
    record = {"request": request, **answer}
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_path(request, cache_dir).write_text(
        json.dumps(record, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    return record


def anthropic_ask(client) -> Ask:
    """An Ask over an `anthropic` client: sends the request, returns the parsed JSON verdict."""

    def ask(request: dict) -> dict:
        response = client.messages.create(**request)
        if response.stop_reason != "end_turn":
            raise JudgeError(f"judge stopped with {response.stop_reason}")
        text = next((block.text for block in response.content if block.type == "text"), None)
        if text is None:
            raise JudgeError("judge returned no text block")
        try:
            output = json.loads(text)
        except json.JSONDecodeError as e:
            raise JudgeError(f"judge output is not JSON: {text[:200]!r}") from e
        return {
            "output": output,
            "usage": response.usage.to_dict(),
            "model": response.model,
            "id": response.id,
        }

    return ask


def openrouter_ask(env_file: Path) -> Ask:
    """The real judge: Opus 5.5 on OpenRouter, keyed by OPENROUTER_KEY in bench/.env."""
    token = openrouter_env(env_file)["ANTHROPIC_AUTH_TOKEN"]
    return anthropic_ask(anthropic.Anthropic(base_url=BASE_URL, auth_token=token, api_key=None))
