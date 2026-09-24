import json

import pytest

from bench.cli import main
from bench.questions import Question
from bench.report import arm_metrics, p90, per_question, render

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
        "| Q04 | talk_set | 1–0–0 | 75% / 25% | 100% / 100% | 0% / 0% | 300 s / 50 s | $0.60 / $0.20 |"
        in page
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
