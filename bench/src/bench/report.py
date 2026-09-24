"""The results page (Epic E): results/results.md, generated from results/scores.json, the runs'
result.json files and results/run-meta.json. Every number comes from here; nothing is typed in.
The page carries no generation timestamp, so rebuilding it from the same inputs is byte-identical.
"""

import math
from statistics import mean, median

from bench.questions import Question

ARMS = ("omnigraph", "markdown")  # the page's column order
NAMES = {"omnigraph": "Agent + Omnigraph", "markdown": "Agent + Markdown files"}
DASH = "–"


def p90(values: list[float]) -> float:
    """Nearest-rank 90th percentile."""
    ordered = sorted(values)
    return ordered[math.ceil(0.9 * len(ordered)) - 1]


def _open_sections(scores: dict) -> dict[str, dict]:
    """List questions reported by recall (#39): those without a fixed `count`."""
    return {qid: s for qid, s in scores["recall"].items() if s and "count" not in s}


def arm_metrics(scores: dict, results: list[dict], arm: str) -> dict:
    runs = [run for run in scores["runs"] if run["arm"] == arm]
    mine = [r for r in results if r["arm"] == arm]
    other = next(a for a in ARMS if a != arm)
    outcomes = [row["result"] for rows in scores["pairwise"].values() for row in rows or []]
    claims = [claim for run in runs for claim in run["claims"]]
    buckets = {
        b: sum(c["grounding"] == b for c in claims) for b in ("grounded", "partial", "hallucinated")
    }
    recalls = [
        r["recall"]
        for section in _open_sections(scores).values()
        for r in section["runs"]
        if r["arm"] == arm and r["recall"] is not None
    ]
    consistency = [
        s["consistency"][arm]
        for s in scores["recall"].values()
        if s and s.get("consistency", {}).get(arm) is not None
    ]
    absence = [row for rows in scores["absence"].values() for row in rows if row["arm"] == arm]
    times = [r["wall_s"] for r in mine]
    costs = [r["cost_usd"] or 0 for r in mine]
    return {
        "pairwise": (outcomes.count(arm), outcomes.count("tie"), outcomes.count(other)),
        "recall": mean(recalls) if recalls else None,
        "consistency": mean(consistency) if consistency else None,
        "claims": (len(claims), len(claims) / len(runs) if runs else 0),
        **buckets,
        "uncited": sum(len(run["uncited"] or []) for run in runs) / len(runs) if runs else 0,
        "absence": (sum(row["correct"] for row in absence), len(absence)),
        "time_median": median(times) if times else None,
        "time_p90": p90(times) if times else None,
        "cost_mean": mean(costs) if costs else None,
        "cost_total": sum(costs),
        "tokens_in": mean(
            (r.get("input_tokens") or 0)
            + (r.get("cache_read_input_tokens") or 0)
            + (r.get("cache_creation_input_tokens") or 0)
            for r in mine
        )
        if mine
        else None,
        "tokens_out": mean(r.get("output_tokens") or 0 for r in mine) if mine else None,
        "turns": mean(r.get("num_turns") or 0 for r in mine) if mine else None,
        "tool_calls": mean(r.get("tool_calls") or 0 for r in mine) if mine else None,
        "not_ok": sum(r.get("status") != "ok" for r in mine),
    }


def _share(claims: list[dict], bucket: str) -> float | None:
    return sum(c["grounding"] == bucket for c in claims) / len(claims) if claims else None


def per_question(scores: dict, results: list[dict], questions: dict[str, Question]) -> list[dict]:
    rows = []
    for qid in sorted(questions):
        runs = [run for run in scores["runs"] if run["qid"] == qid]
        if not runs:
            continue
        outcomes = [row["result"] for row in scores["pairwise"].get(qid) or []]
        section = scores["recall"].get(qid)
        listed = None
        if section and "count" in section:
            listed = ("agree", section["agreement"]["mean"])
        elif section:
            by_arm = {}
            for arm in ARMS:
                values = [
                    r["recall"]
                    for r in section["runs"]
                    if r["arm"] == arm and r["recall"] is not None
                ]
                by_arm[arm] = mean(values) if values else None
            listed = ("recall", by_arm)
        claims = {
            arm: [c for run in runs if run["arm"] == arm for c in run["claims"]] for arm in ARMS
        }
        mine = {arm: [r for r in results if r["qid"] == qid and r["arm"] == arm] for arm in ARMS}
        rows.append(
            {
                "qid": qid,
                "shape": questions[qid].shape,
                "pairwise": (
                    outcomes.count("omnigraph"),
                    outcomes.count("markdown"),
                    outcomes.count("tie"),
                ),
                "list": listed,
                "grounded": {arm: _share(claims[arm], "grounded") for arm in ARMS},
                "hallucinated": {arm: _share(claims[arm], "hallucinated") for arm in ARMS},
                "time_median": {
                    arm: median([r["wall_s"] for r in mine[arm]]) if mine[arm] else None
                    for arm in ARMS
                },
                "cost_mean": {
                    arm: mean([r["cost_usd"] or 0 for r in mine[arm]]) if mine[arm] else None
                    for arm in ARMS
                },
            }
        )
    return rows


def _pct(x: float | None) -> str:
    return DASH if x is None else f"{x:.0%}" if x in (0, 1) else f"{x:.1%}".replace(".0%", "%")


def _tokens(n: float | None) -> str:
    if n is None:
        return DASH
    return f"{n / 1e6:.2f}M" if n >= 1e6 else f"{n / 1e3:.1f}k" if n >= 1e3 else f"{n:.0f}"


def _pair(values: dict, fmt) -> str:
    return " / ".join(fmt(values[arm]) for arm in ARMS)


def render(scores: dict, results: list[dict], questions: dict[str, Question], meta: dict) -> str:
    m = {arm: arm_metrics(scores, results, arm) for arm in ARMS}
    pairings = sum(len(rows or []) for rows in scores["pairwise"].values())
    open_ids = ", ".join(sorted(_open_sections(scores)))

    def counted(arm: str, bucket: str) -> str:
        total = m[arm]["claims"][0]
        return f"{m[arm][bucket]} ({_pct(m[arm][bucket] / total) if total else DASH})"

    def num(x, spec: str) -> str:
        return DASH if x is None else format(x, spec)

    headline = [
        (
            f"Answer quality: pairwise wins / ties / losses ({pairings} pairings)",
            lambda a: " / ".join(map(str, m[a]["pairwise"])),
        ),
        (f"Recall, open list questions ({open_ids}): mean", lambda a: _pct(m[a]["recall"])),
        (
            "Run-to-run consistency, list questions: mean item Jaccard",
            lambda a: num(m[a]["consistency"], ".2f"),
        ),
        (
            "Claims per answer: mean (total)",
            lambda a: f"{m[a]['claims'][1]:.1f} ({m[a]['claims'][0]})",
        ),
        ("Grounded claims (verbatim quote, supported)", lambda a: counted(a, "grounded")),
        ("Partially supported claims", lambda a: counted(a, "partial")),
        (
            "Hallucinated claims (quote not found, wrong talk, or unsupported)",
            lambda a: counted(a, "hallucinated"),
        ),
        ("Uncited factual statements per answer: mean", lambda a: f"{m[a]['uncited']:.1f}"),
        (
            "Absence question (Q10) answered correctly",
            lambda a: " / ".join(map(str, m[a]["absence"])),
        ),
        (
            "Time per question: median / p90",
            lambda a: f"{num(m[a]['time_median'], '.0f')} s / {num(m[a]['time_p90'], '.0f')} s",
        ),
        (
            "Cost per question: mean (total)",
            lambda a: f"${num(m[a]['cost_mean'], '.2f')} (${m[a]['cost_total']:.2f})",
        ),
        (
            "Tokens per question: input incl. cache / output",
            lambda a: f"{_tokens(m[a]['tokens_in'])} / {_tokens(m[a]['tokens_out'])}",
        ),
        (
            "Turns / tool calls per question: mean",
            lambda a: f"{num(m[a]['turns'], '.0f')} / {num(m[a]['tool_calls'], '.0f')}",
        ),
        ("Capped or failed runs", lambda a: str(m[a]["not_ok"])),
    ]
    lines = [
        "# Agent + Omnigraph vs Agent + Markdown files",
        "",
        f"{len({r['qid'] for r in results})} questions × 2 arms × "
        f"{max((r['run'] for r in results), default=0)} runs ({len(results)} agent runs).",
        "",
        "## Headline",
        "",
        f"| Metric | {NAMES['omnigraph']} | {NAMES['markdown']} |",
        "|---|---|---|",
        *[f"| {label} | {cell('omnigraph')} | {cell('markdown')} |" for label, cell in headline],
        "",
        "## Per question",
        "",
        "Each cell is omnigraph / markdown. Pairwise is omnigraph wins – markdown wins – ties.",
        "Fixed-length lists show how much the two arms agree instead of recall.",
        "",
        "| Question | Shape | Pairwise | Recall / agreement | Grounded | Hallucinated "
        "| Median time | Mean cost |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for row in per_question(scores, results, questions):
        kind, value = row["list"] or (None, None)
        listed = (
            DASH
            if kind is None
            else f"agree {_pct(value)}"
            if kind == "agree"
            else _pair(value, _pct)
        )
        lines.append(
            f"| {row['qid']} | {row['shape']} | {'–'.join(map(str, row['pairwise']))} | {listed} | "
            f"{_pair(row['grounded'], _pct)} | {_pair(row['hallucinated'], _pct)} | "
            f"{_pair(row['time_median'], lambda t: num(t, '.0f') + ' s')} | "
            f"{_pair(row['cost_mean'], lambda c: '$' + num(c, '.2f'))} |"
        )
    lines += [
        "",
        f"Graph `{meta.get('graph_head', DASH)}`, "
        f"corpus `{str(meta.get('corpus_sha', DASH))[:12]}`.",
        "",
    ]
    return "\n".join(lines)
