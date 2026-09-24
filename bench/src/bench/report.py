"""The results page (Epic E): results/results.md, generated from results/scores.json, the runs'
result.json files and results/run-meta.json. Every number comes from here; nothing is typed in.
The page carries no generation timestamp, so rebuilding it from the same inputs is byte-identical.
"""

import math
import re
from pathlib import Path
from statistics import mean, median

from bench.parse import answer_prose
from bench.questions import Question

ARMS = ("omnigraph", "markdown")  # the page's column order
NAMES = {"omnigraph": "Agent + Omnigraph", "markdown": "Agent + Markdown files"}
DASH = "–"
# E1.3, picked on 2026-09-24: (question, run, what it shows).
SHOWCASES = [("Q03", 3, "Aggregate win"), ("Q09", 3, "Lookup"), ("Q01", 1, "Loss")]


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


def _call(name: str, inputs: dict) -> str:
    """One tool call as a short command line; temp paths are cut to file names."""
    if name == "Bash":
        return inputs.get("command", "")
    if name == "Read":
        path = inputs.get("file_path", "")
        if "/tool-results/" in path:
            return "read saved tool output"
        text = f"read {Path(path).name}"
        if "offset" in inputs or "limit" in inputs:
            start = inputs.get("offset", 1)
            end = start + inputs["limit"] - 1 if "limit" in inputs else "end"
            text += f" lines {start}–{end}"
        return text
    if name == "Grep":
        text = f'grep "{inputs.get("pattern", "")}"'
        if inputs.get("path"):
            text += f" {Path(inputs['path']).name}"
        for flag in ("-A", "-B", "-C"):
            if flag in inputs:
                text += f" {flag} {inputs[flag]}"
        return text + (" -i" if inputs.get("-i") else "")
    if name == "Glob":
        return f"glob {inputs.get('pattern', '')}"
    return f"{name.lower()} {inputs}"


def _text(content) -> str:
    if isinstance(content, list):
        return "\n".join(str(c.get("text", "")) for c in content if isinstance(c, dict))
    return str(content or "")


def _note(result: dict | None) -> str:
    """What came back, in a few words."""
    if result is None:
        return ""
    text = _text(result.get("content"))
    if result.get("is_error"):
        first = text.strip().splitlines()[0] if text.strip() else "error"
        first = first.split(". ")[0].rstrip(".") + "."  # the first sentence
        first = first.replace("`", "'")
        return "✗ " + (first if len(first) <= 80 else first[:79] + "…")
    if text.startswith("<persisted-output>"):
        return "output saved to a file"
    if m := re.match(r"(\d+) rows? from", text):
        return f"{m.group(1)} row{'' if m.group(1) == '1' else 's'}"
    if m := re.match(r"Found (\d+) files?", text):
        return f"{m.group(1)} file{'' if m.group(1) == '1' else 's'}"
    return ""


def tool_lines(trace: list[dict]) -> list[str]:
    """Every tool call of a run, in order, with a note on its result."""
    calls, results = [], {}
    for message in trace:
        for block in message.get("content") or []:
            if not isinstance(block, dict):
                continue
            if "name" in block and "input" in block:
                calls.append(block)
            elif "tool_use_id" in block:
                results[block["tool_use_id"]] = block
    lines = []
    for call in calls:
        text = _call(call["name"], call["input"]).replace("`", "'").replace("\n", " ↵ ")
        text = text if len(text) <= 140 else text[:139] + "…"
        note = _note(results.get(call["id"]))
        lines.append(f"`{text}`" + (f" → {note}" if note else ""))
    return lines


def excerpt(text: str, limit: int = 900) -> str:
    """The start of an answer, cut at the last paragraph break before `limit`."""
    text = text.strip()
    if len(text) <= limit:
        return text
    cut = text.rfind("\n\n", 0, limit)
    if cut > 0:
        return text[:cut] + "\n\n…"
    cut = text.rfind(". ", 0, limit)
    return (text[: cut + 1] if cut > 0 else text[:limit]) + " …"


def _quote(text: str) -> str:
    return "\n".join(f"> {line}" if line else ">" for line in text.splitlines())


def showcase(
    key: tuple[str, int, str],
    scores: dict,
    results: list[dict],
    questions: dict[str, Question],
    traces: dict[tuple[str, str, int], list[dict] | None],
) -> str:
    qid, n, label = key
    lines = [f"### {label}: {qid}, run {n}", "", f"> {questions[qid].text}", ""]
    pairing = next((p for p in scores["pairwise"].get(qid) or [] if p["run"] == n), None)
    if pairing:
        outcome = pairing["result"]
        said = f"the {outcome} answer wins both orders." if outcome in ARMS else "a tie."
        reason = pairing["orders"][0]["reason"] if pairing.get("orders") else ""
        lines += [f'**Pairwise:** {said} The judge: "{reason}"', ""]
    runs = {r["arm"]: r for r in scores["runs"] if (r["qid"], r["run"]) == (qid, n)}
    done = {r["arm"]: r for r in results if (r["qid"], r["run"]) == (qid, n)}

    def buckets(arm: str) -> str:
        claims = runs[arm]["claims"] if arm in runs else []
        return " / ".join(
            str(sum(c["grounding"] == b for c in claims))
            for b in ("grounded", "partial", "hallucinated")
        )

    rows = [
        ("Time / cost", lambda a: f"{done[a]['wall_s']:.0f} s / ${done[a]['cost_usd']:.2f}"),
        ("Turns / tool calls", lambda a: f"{done[a]['num_turns']} / {done[a]['tool_calls']}"),
        ("Claims: grounded / partial / hallucinated", buckets),
        ("Uncited statements", lambda a: str(len(runs[a]["uncited"] or []))),
    ]
    lines += [f"| | {NAMES['omnigraph']} | {NAMES['markdown']} |", "|---|---|---|"]
    lines += [f"| {name} | {cell('omnigraph')} | {cell('markdown')} |" for name, cell in rows]
    lines.append("")
    for arm in ARMS:
        trace = traces.get((qid, arm, n))
        if trace is None:
            lines += [f"{NAMES[arm]}: trace not available", ""]
            continue
        calls = tool_lines(trace)
        plural = "" if len(calls) == 1 else "s"
        lines += [f"<details><summary>{NAMES[arm]}: {len(calls)} tool call{plural}</summary>", ""]
        lines += [f"{i}. {call}" for i, call in enumerate(calls, 1)]
        lines += ["", "</details>", ""]
    for arm in ARMS:
        text = excerpt(answer_prose(done[arm].get("answer_text", "")))
        lines += [f"**{NAMES[arm]}**, start of the answer:", "", _quote(text), ""]
    return "\n".join(lines)


def render(
    scores: dict,
    results: list[dict],
    questions: dict[str, Question],
    meta: dict,
    traces: dict[tuple[str, str, int], list[dict] | None] | None = None,
) -> str:
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
    if traces is not None:
        shown = [
            key
            for key in SHOWCASES
            if key[0] in questions
            and sum((r["qid"], r["run"]) == key[:2] for r in results) == len(ARMS)
        ]
        if shown:
            lines += ["", "## Showcases", ""]
            for key in shown:
                lines.append(showcase(key, scores, results, questions, traces))
    lines += ["", "## Method notes", "", *method_notes(scores, results, meta), ""]
    return "\n".join(lines)


def method_notes(scores: dict, results: list[dict], meta: dict) -> list[str]:
    """E1.4: the setup and the caveats, with every number taken from the data or the code."""
    from bench.arms import EFFORT, MAX_BUDGET_USD, MAX_TURNS
    from bench.provider import PRICES_AS_OF
    from bench.run import WALL_TIMEOUT_S

    questions = len({r["qid"] for r in results})
    runs = max((r["run"] for r in results), default=0)
    pairings = [row for rows in scores["pairwise"].values() for row in rows or []]
    agree = sum(bool(row.get("agree")) for row in pairings)
    judge = scores.get("judge", {})
    absence = [
        f"{sum(row['result'] == 'tie' for row in scores['pairwise'].get(qid) or [])} of "
        f"{len(scores['pairwise'].get(qid) or [])} {qid} pairings are ties"
        for qid in sorted(scores.get("absence", {}))
    ]
    return [
        f"1. **Setup.** {questions} questions × 2 arms × {runs} run{'' if runs == 1 else 's'} "
        f"({len(results)} agent runs), run on {str(meta.get('started_first', DASH))[:10]}. Both "
        f"arms use `{meta.get('model', DASH)}` at effort `{EFFORT}`, no subagents, capped at "
        f"{MAX_TURNS} turns, ${MAX_BUDGET_USD:.0f} and {WALL_TIMEOUT_S // 60} min per run (Claude "
        f"Code {meta.get('cli_version', DASH)}, Agent SDK {meta.get('sdk_version', DASH)}). The "
        f"Omnigraph arm reads a local copy of the graph (commit `{meta.get('graph_head', DASH)}`) "
        "through stored read queries only. The markdown arm reads the talk transcripts as files "
        f"(corpus `{str(meta.get('corpus_sha', DASH))[:12]}`).",
        "2. **Correctness is relative.** There is no gold answer set. A claim is grounded when its "
        "quote is in the cited transcript and a judge finds that it supports the claim. Recall is "
        "measured against the pool of everything either arm found and grounded, so entries neither "
        "arm found don't count. On fixed-length lists every run's recall is N ÷ pool, so those "
        "show the arms' agreement instead.",
        f"3. **The judge** is `{judge.get('model', DASH)}` and never told which arm wrote what. "
        "Before the pairwise comparison, both answers go through the same redaction of tool and "
        "source mentions, though differences of style remain. Each pairing is judged in both "
        f"orders, and an arm wins only if it wins both; the two orders agreed in {agree} of "
        f"{len(pairings)} pairings. Its support verdicts vary by a few percent between passes, so "
        "small differences between the arms are within noise. Judge cost for these results: "
        f"${judge.get('cost_usd', 0):.2f}, kept apart from the arms' costs.",
        f"4. **Costs** are token usage × OpenRouter prices as of {PRICES_AS_OF} (the Agent SDK's "
        "own figure matched). They cover answering the questions; building the graph (extraction, "
        "embeddings) is excluded.",
        "5. **The absence question** has no talk to find, and both arms can be right by finding "
        "nothing. A pairwise win there reflects extra context, not accuracy"
        + (f" ({'; '.join(absence)})." if absence else "."),
    ]
