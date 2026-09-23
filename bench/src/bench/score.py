"""Scoring the runs (Epic D): each claim's quote check, its support verdict and its grounding
bucket. Verdicts come only from the judge cache; asking the judge is the CLI's job."""

import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict
from pathlib import Path

from bench.judge import (
    cache_path,
    cluster_request,
    label_groups,
    lookup,
    support_request,
    uncited_request,
)
from bench.parse import answer_prose, normalise
from bench.questions import Question
from bench.verify import Corpus

RUN_DIR = re.compile(r"^Q\d{2}$")
JUDGED = {"exact", "fuzzy", "spliced"}  # a quote found in its talk; anything else is hallucinated
BUCKETS = {"supported": "grounded", "partial": "partial", "unsupported": "hallucinated"}
CLUSTERED = {"ranked_list", "company_set"}  # item labels grouped by the judge
RECALL_SHAPES = CLUSTERED | {"talk_set"}  # talk sets group items by the talk their claims cite
TOP_K = 5


def load_runs(runs_dir: Path) -> list[dict]:
    """Every result.json under runs/Qnn/<arm>/<n>/, in question, arm, run order."""
    paths = [
        path
        for question in runs_dir.iterdir()
        if RUN_DIR.match(question.name)
        for path in question.glob("*/*/result.json")
    ]
    runs = [json.loads(path.read_text(encoding="utf-8")) for path in paths]
    return sorted(runs, key=lambda r: (r["qid"], r["arm"], r["run"]))


def grounding(status: str, verdict: str | None) -> str | None:
    """grounded | partial | hallucinated, or None while a found quote awaits its verdict."""
    if status not in JUDGED:
        return "hallucinated"
    return BUCKETS.get(verdict)


def spread(items: list, n: int) -> list:
    """n items evenly spaced through the list (all of them if n covers it)."""
    if n >= len(items):
        return list(items)
    return [items[i * len(items) // n] for i in range(n)]


def _claims(run: dict, corpus: Corpus):
    """(claim, quote check, support request or None) for each claim of one run."""
    for claim in normalise(run.get("answer_json")).claims:
        check = corpus.check(claim.talk, claim.quote)
        request = None
        if check.status in JUDGED:
            context = corpus.context(claim.talk, claim.quote)
            title = corpus.titles.get(check.talk, "")
            request = support_request(title, claim.claim, claim.item, claim.quote, context)
        yield claim, check, request


def support_requests(runs: list[dict], corpus: Corpus) -> list[tuple[str, dict]]:
    """(label, request) for every claim the support judge has to see."""
    return [
        (f"{run['qid']} {run['arm']} #{run['run']} c{claim.index}", request)
        for run in runs
        for claim, _, request in _claims(run, corpus)
        if request is not None
    ]


def _uncited_request(run: dict) -> dict:
    claims = [(claim.item, claim.claim) for claim in normalise(run.get("answer_json")).claims]
    return uncited_request(answer_prose(run.get("answer_text", "")), claims)


def uncited_requests(runs: list[dict]) -> list[tuple[str, dict]]:
    """(label, request) for every run: one uncited-statements check per answer."""
    return [(f"{run['qid']} {run['arm']} #{run['run']}", _uncited_request(run)) for run in runs]


def score_runs(runs: list[dict], corpus: Corpus, cache_dir: Path) -> list[dict]:
    scored = []
    for run in runs:
        answer = normalise(run.get("answer_json"))
        claims = []
        for claim, check, request in _claims(run, corpus):
            record = lookup(request, cache_dir) if request else None
            support = None
            if record:
                support = {**record["output"], "judgment": cache_path(request, cache_dir).stem}
            claims.append(
                {
                    **asdict(claim),
                    "quote_check": asdict(check),
                    "support": support,
                    "grounding": grounding(check.status, support and support["verdict"]),
                }
            )
        scored.append(
            {
                "qid": run["qid"],
                "arm": run["arm"],
                "run": run["run"],
                "unparseable": answer.unparseable,
                "flags": list(answer.flags),
                "dropped_items": answer.dropped_items,
                "dropped_claims": answer.dropped_claims,
                "items": [asdict(item) for item in answer.items],
                "claims": claims,
                "uncited": (lookup(_uncited_request(run), cache_dir) or {})
                .get("output", {})
                .get("uncited"),
            }
        )
    return scored


def _item_groups(run: dict, shape: str, label_group: dict[str, str] | None) -> dict[int, set[str]]:
    """Item position -> its groups: the talks its claims cite (talk sets) or its label's group."""
    if shape == "talk_set":
        groups: dict[int, set[str]] = {}
        for claim in run["claims"]:
            talk = claim["quote_check"]["talk"]
            if claim["item_position"] and talk:
                groups.setdefault(claim["item_position"], set()).add(talk)
        return groups
    return {item["position"]: {label_group[item["label"]]} for item in run["items"]}


def pooled_recall(
    shape: str,
    runs: list[dict],
    label_group: dict[str, str] | None = None,
    count: int | None = None,
) -> dict:
    """D2.1 for one question's scored runs: the groups, the pool, each run's recall and overlap."""
    per_run = [_item_groups(run, shape, label_group) for run in runs]
    members: dict[str, set[str]] = defaultdict(set)
    pooled: set[str] = set()
    for run, groups in zip(runs, per_run, strict=True):
        labels = {item["position"]: item["label"] for item in run["items"]}
        for position, names in groups.items():
            for name in names:
                members[name].add(labels[position])
        for claim in run["claims"]:
            if claim["grounding"] == "grounded":
                pooled |= groups.get(claim["item_position"], set())
    out: dict = {
        "shape": shape,
        "groups": [
            {"name": name, "members": sorted(members[name]), "pooled": name in pooled}
            for name in sorted(members)
        ],
    }
    consensus: list[str] | None = None
    tops: list[set[str]] = []
    if shape == "ranked_list":
        k = min(TOP_K, max((len(run["items"]) for run in runs), default=0))
        tops = [{n for p, names in groups.items() if p <= k for n in names} for groups in per_run]
        votes = Counter(name for top in tops for name in top if name in pooled)

        def mean_position(name: str) -> float:
            firsts = [
                min(p for p, names in groups.items() if name in names)
                for groups in per_run
                if any(name in names for names in groups.values())
            ]
            return sum(firsts) / len(firsts)

        consensus = sorted(votes, key=lambda n: (-votes[n], mean_position(n), n))[:k]
        out["k"], out["consensus_top"] = k, consensus
    out["runs"] = []
    for i, (run, groups) in enumerate(zip(runs, per_run, strict=True)):
        found = set().union(*groups.values())
        overlap = None
        if consensus:
            overlap = len(tops[i] & set(consensus)) / len(consensus)
        out["runs"].append(
            {
                "arm": run["arm"],
                "run": run["run"],
                "found": sorted(found),
                "recall": len(found & pooled) / len(pooled) if pooled else None,
                "overlap": overlap,
            }
        )
    if count:
        out["count"] = count
        out["agreement"] = _agreement(runs, per_run, count)
    out["consistency"] = _consistency(runs, per_run, count)
    return out


def _top(groups: dict[int, set[str]], count: int | None) -> set[str]:
    """The groups of a run's first `count` items, or of all of them."""
    return {n for p, names in groups.items() if count is None or p <= count for n in names}


def _consistency(
    runs: list[dict], per_run: list[dict[int, set[str]]], count: int | None
) -> dict[str, float | None]:
    """D2.3: per arm, the mean Jaccard of its runs' group sets over every pair of runs."""
    sets: dict[str, list[set[str]]] = defaultdict(list)
    for run, groups in zip(runs, per_run, strict=True):
        sets[run["arm"]].append(_top(groups, count))
    out: dict[str, float | None] = {}
    for arm, found in sorted(sets.items()):
        pairs = [(a, b) for i, a in enumerate(found) for b in found[i + 1 :]]
        scores = [len(a & b) / len(a | b) if a | b else 1.0 for a, b in pairs]
        out[arm] = sum(scores) / len(scores) if scores else None
    return out


def absence(runs: list[dict]) -> list[dict]:
    """D2.4: an absence answer is correct only with an empty contract block."""
    return [
        {
            "arm": run["arm"],
            "run": run["run"],
            "correct": not run["items"] and not run["claims"],
            "items": len(run["items"]),
            "claims": len(run["claims"]),
        }
        for run in runs
    ]


def _agreement(runs: list[dict], per_run: list[dict[int, set[str]]], count: int) -> dict:
    """Fixed-length lists (#39): for each run number, the share of the N asked for that the
    markdown and omnigraph runs both name in their top N."""
    tops = {
        (run["arm"], run["run"]): _top(groups, count)
        for run, groups in zip(runs, per_run, strict=True)
    }
    pairs = []
    for n in sorted({run["run"] for run in runs}):
        if ("markdown", n) in tops and ("omnigraph", n) in tops:
            shared = len(tops["markdown", n] & tops["omnigraph", n])
            pairs.append({"run": n, "shared": shared, "agreement": shared / count})
    mean = sum(p["agreement"] for p in pairs) / len(pairs) if pairs else None
    return {"pairs": pairs, "mean": mean}


def cluster_requests(
    runs: list[dict], questions: dict[str, Question]
) -> list[tuple[str, dict, int]]:
    """(label, request, distinct labels) for each clustered question with items to group."""
    out = []
    for qid, question in sorted(questions.items()):
        if question.shape not in CLUSTERED:
            continue
        labels = [
            item.label
            for run in runs
            if run["qid"] == qid
            for item in normalise(run.get("answer_json")).items
        ]
        if labels:
            request = cluster_request(question.text, labels)
            out.append((f"{qid} clusters", request, len(set(labels))))
    return out


def recall_sections(
    scored: list[dict], questions: dict[str, Question], cache_dir: Path
) -> dict[str, dict | None]:
    """D2.1 per question; None where the question's clusters haven't been judged yet."""
    out: dict[str, dict | None] = {}
    for qid, question in sorted(questions.items()):
        runs = [run for run in scored if run["qid"] == qid]
        if question.shape not in RECALL_SHAPES or not runs:
            continue
        label_group: dict[str, str] | None = None
        if question.shape in CLUSTERED:
            labels = [item["label"] for run in runs for item in run["items"]]
            label_group = {}
            if labels:
                record = lookup(cluster_request(question.text, labels), cache_dir)
                if record is None:
                    out[qid] = None
                    continue
                label_group = label_groups(labels, record["output"]["groups"])
        out[qid] = pooled_recall(question.shape, runs, label_group, question.count)
    return out
