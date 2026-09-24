import json

import pytest

from bench.cli import main
from bench.questions import Question
from bench.report import (
    arm_metrics,
    excerpt,
    method_notes,
    p90,
    per_question,
    render,
    showcase,
    tool_lines,
)

QUESTIONS = {
    "Q01": Question("Q01", "aggregate", "ranked_list", "Top topics?", count=2),
    "Q04": Question("Q04", "aggregate", "talk_set", "Which talks?"),
    "Q10": Question("Q10", "absence", "absence", "FPGAs?"),
}


def claim(bucket):
    return {"grounding": bucket}


def run(qid, arm, n, buckets, uncited=0):
    return {
        "qid": qid,
        "arm": arm,
        "run": n,
        "claims": [claim(b) for b in buckets],
        "uncited": ["u"] * uncited,
    }


def result(qid, arm, n, wall, cost, status="ok"):
    return {
        "qid": qid,
        "arm": arm,
        "run": n,
        "status": status,
        "wall_s": wall,
        "cost_usd": cost,
        "input_tokens": 100,
        "cache_read_input_tokens": 1000,
        "cache_creation_input_tokens": 400,
        "output_tokens": 50,
        "num_turns": 10,
        "tool_calls": 9,
    }


SCORES = {
    "judge": {"cost_usd": 1.5},
    "runs": [
        run("Q01", "markdown", 1, ["grounded", "grounded", "partial"], uncited=2),
        run("Q01", "omnigraph", 1, ["grounded", "hallucinated"], uncited=1),
        run("Q04", "markdown", 1, ["grounded"]),
        run("Q04", "omnigraph", 1, ["grounded", "grounded"]),
        run("Q10", "markdown", 1, []),
        run("Q10", "omnigraph", 1, []),
    ],
    "recall": {
        "Q01": {
            "count": 2,
            "agreement": {"mean": 0.5},
            "consistency": {"markdown": 1.0, "omnigraph": 0.5},
            "runs": [
                {"arm": "markdown", "run": 1, "recall": 0.4},
                {"arm": "omnigraph", "run": 1, "recall": 0.4},
            ],
        },
        "Q04": {
            "consistency": {"markdown": 0.2, "omnigraph": 0.4},
            "runs": [
                {"arm": "markdown", "run": 1, "recall": 0.25},
                {"arm": "omnigraph", "run": 1, "recall": 0.75},
            ],
        },
    },
    "absence": {
        "Q10": [{"arm": "markdown", "correct": True}, {"arm": "omnigraph", "correct": False}]
    },
    "pairwise": {
        "Q01": [{"run": 1, "result": "markdown"}],
        "Q04": [{"run": 1, "result": "omnigraph"}],
        "Q10": [{"run": 1, "result": "tie"}],
    },
}
RESULTS = [
    result("Q01", "markdown", 1, 100, 0.5),
    result("Q01", "omnigraph", 1, 200, 1.0),
    result("Q04", "markdown", 1, 50, 0.2),
    result("Q04", "omnigraph", 1, 300, 0.6, status="capped"),
    result("Q10", "markdown", 1, 10, 0.1),
    result("Q10", "omnigraph", 1, 40, 0.2),
]


def test_p90_is_the_nearest_rank():
    assert p90([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
    assert p90([5]) == 5


def test_arm_metrics_are_computed_from_the_scores_and_the_run_results():
    og = arm_metrics(SCORES, RESULTS, "omnigraph")

    assert og["pairwise"] == (1, 1, 1)  # wins, ties, losses
    assert og["recall"] == 0.75  # open questions only: Q04; Q01 is fixed-length
    assert og["consistency"] == pytest.approx(0.45)
    assert og["claims"] == (4, 4 / 3)
    assert (og["grounded"], og["partial"], og["hallucinated"]) == (3, 0, 1)
    assert og["uncited"] == 1 / 3
    assert og["absence"] == (0, 1)
    assert (og["time_median"], og["time_p90"]) == (200, 300)
    assert (og["cost_mean"], og["cost_total"]) == (pytest.approx(0.6), pytest.approx(1.8))
    assert (og["tokens_in"], og["tokens_out"]) == (1500, 50)
    assert (og["turns"], og["tool_calls"]) == (10, 9)
    assert og["not_ok"] == 1


def test_the_per_question_rows_show_both_arms_and_the_right_list_metric():
    rows = {row["qid"]: row for row in per_question(SCORES, RESULTS, QUESTIONS)}

    assert rows["Q01"]["pairwise"] == (0, 1, 0)  # og wins, md wins, ties
    assert rows["Q01"]["list"] == ("agree", 0.5)
    assert rows["Q04"]["list"] == ("recall", {"omnigraph": 0.75, "markdown": 0.25})
    assert rows["Q10"]["list"] is None
    assert rows["Q01"]["grounded"] == {"omnigraph": 0.5, "markdown": 2 / 3}
    assert rows["Q01"]["hallucinated"] == {"omnigraph": 0.5, "markdown": 0.0}
    assert rows["Q04"]["time_median"] == {"omnigraph": 300, "markdown": 50}


def test_render_puts_omnigraph_first_and_formats_the_cells():
    page = render(SCORES, RESULTS, QUESTIONS, {"graph_head": "HEAD", "corpus_sha": "abc"})

    assert "| Metric | Agent + Omnigraph | Agent + Markdown files |" in page
    assert (
        "| Answer quality: pairwise wins / ties / losses (3 pairings) | 1 / 1 / 1 | 1 / 1 / 1 |"
        in page
    )
    assert "| Absence question (Q10) answered correctly | 0 / 1 | 1 / 1 |" in page
    assert "| Capped or failed runs | 1 | 0 |" in page
    assert "| Q01 | ranked_list | 0–1–0 | agree 50% |" in page
    # every per-question cell is omnigraph / markdown
    assert (
        "| Q04 | talk_set | 1–0–0 | 75% / 25% | 100% / 100% | 0% / 0% "
        "| 300 s / 50 s | $0.60 / $0.20 |" in page
    )


def test_bench_report_writes_results_md(tmp_path):
    results = tmp_path / "results"
    results.mkdir()
    (results / "scores.json").write_text(json.dumps(SCORES))
    (results / "run-meta.json").write_text(json.dumps({"graph_head": "HEAD", "corpus_sha": "abc"}))
    runs = tmp_path / "runs"
    for r in RESULTS:
        path = runs / r["qid"] / r["arm"] / str(r["run"]) / "result.json"
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps(r))
    questions = tmp_path / "questions.yaml"
    questions.write_text(
        "questions:\n"
        "  - {id: Q01, category: aggregate, shape: ranked_list, count: 2, text: 'Top topics?'}\n"
        "  - {id: Q04, category: aggregate, shape: talk_set, text: 'Which talks?'}\n"
        "  - {id: Q10, category: absence, shape: absence, text: 'FPGAs?'}\n"
    )

    code = main(
        [
            "report",
            "--results",
            str(results),
            "--runs-dir",
            str(runs),
            "--questions",
            str(questions),
        ]
    )

    assert code == 0
    page = (results / "results.md").read_text()
    assert page.startswith("# ")
    assert "| Q10 | absence | 0–0–1 | – |" in page


# E1.3 showcases: tool calls in order, an answer excerpt, the metrics, the judge's reason.

TMP = "/private/var/folders/xy/T/aie-bench/runs/Q09/markdown/3"


def use(id_, name, **inputs):
    return {"id": id_, "name": name, "input": inputs}


def res(id_, content, is_error=None):
    return {"tool_use_id": id_, "content": content, "is_error": is_error}


TRACE = [
    {
        "kind": "AssistantMessage",
        "content": [use("1", "Bash", command='omnigraph alias hybrid-search "unship"')],
    },
    {
        "kind": "UserMessage",
        "content": [res("1", "10 rows from branch main via hybrid_chunks\n...")],
    },
    {
        "kind": "AssistantMessage",
        "content": [
            use("2", "Grep", pattern="unship", path=f"{TMP}/talks/ia-aie-k.md", **{"-C": 6})
        ],
    },
    {"kind": "UserMessage", "content": [res("2", "Found 1 file ia-aie-k.md")]},
    {
        "kind": "AssistantMessage",
        "content": [use("3", "Read", file_path=f"{TMP}/talks/ia-aie-k.md", offset=1, limit=60)],
    },
    {"kind": "UserMessage", "content": [res("3", "1\t# Title")]},
    {
        "kind": "AssistantMessage",
        "content": [use("4", "Read", file_path=f"{TMP}/claude-home/p/tool-results/abc.txt")],
    },
    {"kind": "UserMessage", "content": [res("4", "...")]},
    {
        "kind": "AssistantMessage",
        "content": [use("5", "Bash", command="omnigraph alias talk-chunks x | head")],
    },
    {
        "kind": "UserMessage",
        "content": [res("5", "No shell operators, substitutions or redirects.", True)],
    },
    {"kind": "AssistantMessage", "content": [use("6", "Glob", pattern="*krieger*")]},
    {"kind": "UserMessage", "content": [res("6", "<persisted-output> Output too large")]},
]


def test_tool_calls_are_listed_in_order_with_a_note_on_each_result():
    assert tool_lines(TRACE) == [
        '`omnigraph alias hybrid-search "unship"` → 10 rows',
        '`grep "unship" ia-aie-k.md -C 6` → 1 file',
        "`read ia-aie-k.md lines 1–60`",
        "`read saved tool output`",
        "`omnigraph alias talk-chunks x | head` → ✗ "
        "No shell operators, substitutions or redirects.",
        "`glob *krieger*` → output saved to a file",
    ]


def test_an_excerpt_ends_at_a_paragraph_break():
    text = "First paragraph.\n\nSecond paragraph goes on.\n\nThird."

    assert excerpt(text, limit=45) == "First paragraph.\n\nSecond paragraph goes on.\n\n…"
    assert excerpt(text, limit=40) == "First paragraph.\n\n…"
    assert excerpt("Short.", limit=40) == "Short."


def test_a_showcase_shows_the_question_both_arms_and_the_judges_reason():
    scores = {
        "runs": [
            run("Q09", "omnigraph", 3, ["grounded", "grounded"], uncited=1),
            run("Q09", "markdown", 3, ["grounded", "partial"]),
        ],
        "pairwise": {
            "Q09": [
                {
                    "run": 3,
                    "result": "omnigraph",
                    "orders": [
                        {"a": "markdown", "winner": "omnigraph", "reason": "B is more specific."}
                    ],
                }
            ]
        },
    }
    results = [
        result("Q09", "omnigraph", 3, 35, 0.09)
        | {"answer_text": "They unship by usage.\n```json\n{}\n```"},
        result("Q09", "markdown", 3, 27, 0.05) | {"answer_text": "A project-unship channel."},
    ]
    questions = {"Q09": Question("Q09", "lookup", "prose", "How does Anthropic unship?")}
    traces = {("Q09", "omnigraph", 3): TRACE[:2], ("Q09", "markdown", 3): None}

    section = showcase(("Q09", 3, "Lookup"), scores, results, questions, traces)

    assert section.startswith("### Lookup: Q09, run 3\n\n> How does Anthropic unship?")
    assert (
        '**Pairwise:** the omnigraph answer wins both orders. The judge: "B is more specific."'
        in section
    )
    assert "| Claims: grounded / partial / hallucinated | 2 / 0 / 0 | 1 / 1 / 0 |" in section
    assert "<summary>Agent + Omnigraph: 1 tool call</summary>" in section
    assert '1. `omnigraph alias hybrid-search "unship"` → 10 rows' in section
    assert "Agent + Markdown files: trace not available" in section
    assert "> They unship by usage." in section and "```json" not in section


def test_a_multi_line_command_and_a_long_error_stay_on_one_line():
    trace = [
        {
            "kind": "AssistantMessage",
            "content": [use("1", "Bash", command="omnigraph a\necho ---\nomnigraph b")],
        },
        {
            "kind": "UserMessage",
            "content": [
                res("1", "No shell operators. Only `omnigraph alias <name>` is allowed", True)
            ],
        },
    ]

    assert tool_lines(trace) == ["`omnigraph a ↵ echo --- ↵ omnigraph b` → ✗ No shell operators."]


# E1.4: method notes, every number from the data or the code's constants.

META = {
    "graph_head": "01HEAD",
    "corpus_sha": "63c73703991e966e",
    "model": "anthropic/claude-sonnet-5[1m]",
    "cli_version": "2.1.280",
    "sdk_version": "0.2.158",
    "started_first": "2026-09-23T22:38:27+0200",
}


def test_method_notes_state_n_the_caveats_and_what_the_costs_leave_out():
    scores = SCORES | {
        "judge": {"model": "anthropic/claude-opus-5.5", "cost_usd": 10.29},
        "pairwise": {
            "Q01": [{"run": 1, "result": "markdown", "agree": True}],
            "Q04": [{"run": 1, "result": "tie", "agree": False}],
            "Q10": [{"run": 1, "result": "tie", "agree": True}],
        },
    }

    notes = "\n".join(method_notes(scores, RESULTS, META))

    assert "3 questions × 2 arms × 1 run (6 agent runs), run on 2026-09-23" in notes
    assert "`anthropic/claude-sonnet-5[1m]` at effort `high`, no subagents" in notes
    assert "300 turns, $10 and 30 min per run" in notes
    assert "commit `01HEAD`" in notes and "`63c73703991e`" in notes
    assert "There is no gold answer set" in notes
    assert "the two orders agreed in 2 of 3 pairings" in notes
    assert "Judge cost for these results: $10.29" in notes
    assert "OpenRouter prices as of 2026-09-23" in notes
    assert "building the graph" in notes and "excluded" in notes
    assert "1 of 1 Q10 pairings" in notes  # ties


def test_the_page_ends_with_the_method_notes():
    page = render(SCORES, RESULTS, QUESTIONS, META)

    assert "\n## Method notes\n" in page
