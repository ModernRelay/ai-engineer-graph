"""Scoring the runs (Epic D): each claim's quote check, its support verdict and its grounding
bucket. Verdicts come only from the judge cache; asking the judge is the CLI's job."""

import json
import re
from dataclasses import asdict
from pathlib import Path

from bench.judge import cache_path, lookup, support_request, uncited_request
from bench.parse import answer_prose, normalise
from bench.verify import Corpus

RUN_DIR = re.compile(r"^Q\d{2}$")
JUDGED = {"exact", "fuzzy", "spliced"}  # a quote found in its talk; anything else is hallucinated
BUCKETS = {"supported": "grounded", "partial": "partial", "unsupported": "hallucinated"}


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
