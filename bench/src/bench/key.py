"""Answer keys from the curated graph, and scoring an answer against them.

The graph is the reference: what it holds is the answer as curated. `build` reads a
question's key through the reader login (keys/<qid>.gq):

- Q02: the challenge patterns, ranked by how many talks support them
- Q03: the top claims by direct contradictions, with pushback and supporting talks
- Q04: every talk with a signal forming pat-harness-over-model
- Q05: companies ranked by how many talks their speakers gave

`score_claims` (Q02, Q03, Q05) measures how much of a ranked key one answer recovers; the
only judgement call, which answer entry is which key entry and which side each cited talk
is on, comes from the judge (prompts/judge_key.md), cached like every other judge request.
`score_talk_set` (Q04) needs no judge: each answer entry resolves to the talks it cites.
The numbers are computed.
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


def top_claims(ranking: list[dict], count: int, by: str = "contradictions") -> list[dict]:
    """The first `count` entries by `by`, plus any tied with the last of them."""
    ranked = sorted(ranking, key=lambda r: (-r[by], r["pattern"]))
    if len(ranked) <= count:
        return ranked
    cutoff = ranked[count - 1][by]
    return [r for r in ranked if r[by] >= cutoff]


def _ranked_by_talks(rows: list[dict], slug: str, name: str, brief, count: int) -> list[dict]:
    """Key entries from (entry, talk, weight) rows: entries ranked by distinct talks, top
    `count` with ties, each with its talks (by weight) as the supporting side."""
    talks, names = defaultdict(dict), {}
    for r in rows:
        talks[r[slug]][r["talk"]] = talks[r[slug]].get(r["talk"], 0) + r["weight"]
        names[r[slug]] = (r[name], brief(r))
    ranking = [{"pattern": e, "talk_count": len(t)} for e, t in talks.items()]
    claims = []
    for n, r in enumerate(top_claims(ranking, count, by="talk_count"), start=1):
        e = r["pattern"]
        ordered = sorted(talks[e].items(), key=lambda kv: (-kv[1], kv[0]))
        claims.append(
            {
                "key": n,
                "pattern": e,
                "thesis": names[e][0],
                "brief": names[e][1],
                "talk_count": r["talk_count"],
                "support_talks": dict(ordered),
                "leading_support_talks": [talk for talk, _ in ordered[:TOP_SUPPORT]],
            }
        )
    return claims


def assemble_q02(rows: list[dict], count: int = 5) -> dict:
    rows = [{**r, "weight": r["signals"]} for r in rows]
    claims = _ranked_by_talks(rows, "pattern", "thesis", lambda r: r.get("brief", ""), count)
    return {"qid": "Q02", "shape": "ranked_list", "count": count, "claims": claims}


def assemble_q05(rows: list[dict], count: int = 5) -> dict:
    rows = [{**r, "weight": r["speakers"]} for r in rows]
    claims = _ranked_by_talks(rows, "company", "name", lambda r: "a company", count)
    return {"qid": "Q05", "shape": "ranked_list", "count": count, "claims": claims}


def assemble_q04(rows: list[dict]) -> dict:
    talks = {r["talk"]: r["signals"] for r in rows}
    ordered = dict(sorted(talks.items(), key=lambda kv: (-kv[1], kv[0])))
    core = [t for t, n in ordered.items() if n >= 2]
    return {"qid": "Q04", "shape": "talk_set", "talks": ordered, "core_talks": core}


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
    return {"qid": "Q03", "shape": "ranked_list", "count": count, "claims": claims}


KEY_QUERIES = {
    "Q02": ["challenge_support"],
    "Q03": ["ranking", "pushback_talks", "support_talks"],
    "Q04": ["harness_talks"],
    "Q05": ["company_talks"],
}


def build(qid: str, graph_head: str) -> dict:
    gq = KEYS_DIR / f"{qid}.gq"
    rows = [_graph_rows(gq, name) for name in KEY_QUERIES[qid]]
    key = {"Q02": assemble_q02, "Q03": assemble_q03, "Q04": assemble_q04, "Q05": assemble_q05}[qid](
        *rows
    )
    return {**key, "graph_head": graph_head}


def graph_answer_seconds(qid: str) -> float:
    """Wall time of the curated answer itself: the key's queries, through the reader login."""
    import time

    start = time.monotonic()
    for name in KEY_QUERIES[qid]:
        _graph_rows(KEYS_DIR / f"{qid}.gq", name)
    return round(time.monotonic() - start, 2)


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
        f"<question>{question}</question>\n\n<key_entries>\n{claims}\n</key_entries>\n\n"
        f"<answer>\n{answer_prose(run.get('answer_text') or '')}\n</answer>\n\n"
        f"<answer_entries>\n{items}\n</answer_entries>\n\n<answer_claims>\n{cited}\n</answer_claims>"
    )
    return _request("judge_key.md", content, KEY_MATCH_SCHEMA)


def valid_key_match(output: dict) -> bool:
    return isinstance(output.get("items"), list) and isinstance(output.get("claims"), list)


def _ratio(hit: int, total: int) -> float | None:
    return round(hit / total, 3) if total else None


def score_claims(key: dict, run: dict, match: dict, labels: dict[str, str]) -> dict:
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
        against = set(c.get("against_talks", []))
        accepted = against | set(c.get("boundary_talks", []))
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
                "count_error": _count_error(c, answer, entry_key, k),
            }
        )
    top_n = min(key["count"], len(by_key))
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
                len(set(p["against_named"]) & set(by_key[p["key"]].get("against_talks", [])))
                for p in per_claim
            ),
            sum(len(c.get("against_talks", [])) for c in key["claims"]),
        ),
        "for_precision": _ratio(
            sum(
                len(set(p["for_named"]) & set(by_key[p["key"]]["support_talks"])) for p in per_claim
            ),
            sum(len(p["for_named"]) for p in per_claim),
        ),
        "count_error": _mean([p["count_error"] for p in per_claim if p["count_error"] is not None]),
        "per_claim": per_claim,
        "outside_key": outside,
        "wall_s": run.get("wall_s"),
        "cost_usd": run.get("cost_usd"),
        "tool_calls": run.get("tool_calls"),
    }


def _mean(values: list[float]) -> float | None:
    return round(sum(values) / len(values), 1) if values else None


def _count_error(claim: dict, answer, entry_key: dict[int, int], k: int) -> float | None:
    """How far the answer's talk_count for a key entry is from the key's, when both exist."""
    if "talk_count" not in claim:
        return None
    counts = [i.talk_count for i in answer.items if entry_key.get(i.position) == k]
    counts = [c for c in counts if c is not None]
    return abs(counts[0] - claim["talk_count"]) if counts else None


def score_talk_set(key: dict, run: dict, labels: dict[str, str]) -> dict:
    """Q04: each answer entry is the talks it cites (or the talk id it names); recall against
    every key talk and against the core (2+ supporting signals), precision of what it named."""
    answer = normalise(run.get("answer_json"))
    cited = defaultdict(set)
    for c in answer.claims:
        cited[c.item].add(labels.get(c.talk, c.talk))
    named, unresolved = set(), []
    for item in answer.items:
        talks = cited.get(item.label) or (
            {item.label} if item.label.startswith("ia-aie-") else set()
        )
        if talks:
            named |= talks
        else:
            unresolved.append(item.label)
    keyed, core = set(key["talks"]), set(key["core_talks"])
    return {
        "qid": key["qid"],
        "arm": run["arm"],
        "run": run["run"],
        "talks_named": len(named),
        "recall": _ratio(len(named & keyed), len(keyed)),
        "core_recall": _ratio(len(named & core), len(core)),
        "precision": _ratio(len(named & keyed), len(named)),
        "outside_key": sorted(named - keyed),
        "unresolved_entries": unresolved,
        "wall_s": run.get("wall_s"),
        "cost_usd": run.get("cost_usd"),
        "tool_calls": run.get("tool_calls"),
    }
