"""Answer keys from the curated graph, and scoring an answer against them.

The graph is the reference: what it holds is the answer as curated. `build_q03` reads the
key for Q03 through the reader login (keys/Q03.gq): the top claims by direct
contradictions, each with its pushback talks and its supporting talks. `score_q03` measures
how much of that key one answer recovers. The only judgement call, which answer entry is
which key claim and which side each cited talk is on, comes from the judge
(prompts/judge_key.md), cached like every other judge request; the numbers are computed.
"""

import json
import os
import subprocess
from collections import defaultdict
from pathlib import Path

from bench.judge import _request
from bench.parse import answer_prose, normalise

BENCH_DIR = Path(__file__).resolve().parents[2]
KEYS_DIR = BENCH_DIR / "keys"
TOP_SUPPORT = 10  # a key claim's "leading supporters": its talks with the most supporting signals

KEY_MATCH_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "position": {"type": "integer"},
                    "key": {"type": "integer"},
                },
                "required": ["position", "key"],
                "additionalProperties": False,
            },
        },
        "claims": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},
                    "stance": {"type": "string", "enum": ["for", "against", "neither"]},
                },
                "required": ["index", "stance"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["items", "claims"],
    "additionalProperties": False,
}


def _graph_rows(gq: Path, name: str) -> list[dict]:
    """A read query from a key file, run on the served graph through the reader login."""
    home = BENCH_DIR / ".omnigraph-home"
    binary = (home / "omnigraph-bin").read_text().strip()
    out = subprocess.run(
        [binary, "query", name, "--query", str(gq), "--server", "intel-local"]
        + ["--graph", "spike", "--format", "jsonl"],
        capture_output=True,
        text=True,
        check=True,
        env={
            "HOME": os.environ.get("HOME", ""),
            "PATH": "/usr/bin:/bin",
            "OMNIGRAPH_HOME": str(home),
        },
    )
    rows = [json.loads(line) for line in out.stdout.splitlines() if line.strip()]
    return [r for r in rows if r.get("kind") != "metadata"]


def top_claims(ranking: list[dict], count: int) -> list[dict]:
    """The first `count` claims by contradictions, plus any tied with the last of them."""
    ranked = sorted(ranking, key=lambda r: (-r["contradictions"], r["pattern"]))
    if len(ranked) <= count:
        return ranked
    cutoff = ranked[count - 1]["contradictions"]
    return [r for r in ranked if r["contradictions"] >= cutoff]


def assemble_q03(ranking, pushback, support, count: int = 3) -> dict:
    against, boundary = defaultdict(set), defaultdict(set)
    for r in pushback:
        (against if r["polarity"] == "contradiction" else boundary)[r["pattern"]].add(r["talk"])
    supporters = defaultdict(dict)
    for r in support:
        supporters[r["pattern"]][r["talk"]] = r["signals"]
    claims = []
    for n, r in enumerate(top_claims(ranking, count), start=1):
        slug = r["pattern"]
        ordered = sorted(supporters[slug].items(), key=lambda kv: (-kv[1], kv[0]))
        claims.append(
            {
                "key": n,
                "pattern": slug,
                "thesis": r["thesis"],
                "brief": r.get("brief", ""),
                "contradictions": r["contradictions"],
                "against_talks": sorted(against[slug]),
                "boundary_talks": sorted(boundary[slug] - against[slug]),
                "support_talks": dict(ordered),
                "leading_support_talks": [talk for talk, _ in ordered[:TOP_SUPPORT]],
            }
        )
    return {"qid": "Q03", "count": count, "claims": claims}


def build_q03(graph_head: str) -> dict:
    gq = KEYS_DIR / "Q03.gq"
    key = assemble_q03(
        _graph_rows(gq, "ranking"),
        _graph_rows(gq, "pushback_talks"),
        _graph_rows(gq, "support_talks"),
    )
    return {**key, "graph_head": graph_head}


def key_match_request(question: str, key: dict, run: dict) -> dict:
    """What the judge needs to map one answer onto the key: the key's claims, the answer's
    prose, its list entries and every cited claim with its talk."""
    answer = normalise(run.get("answer_json"))
    claims = "\n".join(f"{c['key']}. {c['thesis']}: {c['brief']}" for c in key["claims"])
    items = "\n".join(f"{i.position}. {i.label}" for i in answer.items) or "(none)"
    cited = (
        "\n".join(f"{c.index}. [{c.item}] {c.claim} (talk {c.talk})" for c in answer.claims)
        or "(none)"
    )
    content = (
        f"<question>{question}</question>\n\n<key_claims>\n{claims}\n</key_claims>\n\n"
        f"<answer>\n{answer_prose(run.get('answer_text') or '')}\n</answer>\n\n"
        f"<answer_entries>\n{items}\n</answer_entries>\n\n<answer_claims>\n{cited}\n</answer_claims>"
    )
    return _request("judge_key.md", content, KEY_MATCH_SCHEMA)


def valid_key_match(output: dict) -> bool:
    return isinstance(output.get("items"), list) and isinstance(output.get("claims"), list)


def _ratio(hit: int, total: int) -> float | None:
    return round(hit / total, 3) if total else None


def score_q03(key: dict, run: dict, match: dict, labels: dict[str, str]) -> dict:
    """How much of the key one answer recovers. `match` is the judge's output; `labels` maps
    chunk labels to talk ids so a cited talk resolves either way."""
    answer = normalise(run.get("answer_json"))
    by_key = {c["key"]: c for c in key["claims"]}
    entry_key = {m["position"]: m["key"] for m in match["items"] if m["key"] in by_key}
    stance = {m["index"]: m["stance"] for m in match["claims"]}
    positions = {i.label: i.position for i in answer.items}

    named: dict[int, dict[str, set[str]]] = defaultdict(lambda: {"for": set(), "against": set()})
    for c in answer.claims:
        k = entry_key.get(c.item_position or positions.get(c.item, 0))
        side = stance.get(c.index)
        if k and side in ("for", "against"):
            named[k][side].add(labels.get(c.talk, c.talk))

    per_claim = []
    for k, c in by_key.items():
        found = k in entry_key.values()
        against, accepted = (
            set(c["against_talks"]),
            set(c["against_talks"]) | set(c["boundary_talks"]),
        )
        supporters, leading = set(c["support_talks"]), set(c["leading_support_talks"])
        got_against, got_for = named[k]["against"], named[k]["for"]
        per_claim.append(
            {
                "key": k,
                "pattern": c["pattern"],
                "found": found,
                "against_recall": _ratio(len(got_against & against), len(against)),
                "against_precision": _ratio(len(got_against & accepted), len(got_against)),
                "for_precision": _ratio(len(got_for & supporters), len(got_for)),
                "leading_for_hits": len(got_for & leading),
                "against_named": sorted(got_against),
                "for_named": sorted(got_for),
            }
        )
    top_n = key["count"]
    found = sum(p["found"] for p in per_claim)
    outside = [i.label for i in answer.items if i.position not in entry_key]
    return {
        "qid": key["qid"],
        "arm": run["arm"],
        "run": run["run"],
        "claims_found": found,
        "claims_recall": round(min(found, top_n) / top_n, 3),
        "against_recall": _ratio(
            sum(
                len(set(p["against_named"]) & set(by_key[p["key"]]["against_talks"]))
                for p in per_claim
            ),
            sum(len(c["against_talks"]) for c in key["claims"]),
        ),
        "per_claim": per_claim,
        "outside_key": outside,
        "wall_s": run.get("wall_s"),
        "cost_usd": run.get("cost_usd"),
        "tool_calls": run.get("tool_calls"),
    }
