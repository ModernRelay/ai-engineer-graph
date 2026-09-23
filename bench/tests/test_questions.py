from collections import Counter
from pathlib import Path

import pytest

from bench.prompts import system_prompt
from bench.questions import load_questions

QUESTIONS = Path(__file__).resolve().parents[1] / "questions.yaml"


def write(tmp_path, body: str) -> Path:
    path = tmp_path / "questions.yaml"
    path.write_text(body)
    return path


def one(id="Q01", category="aggregate", shape="ranked_list", text="What was discussed most?"):
    return (
        f"questions:\n  - id: {id}\n    category: {category}\n"
        f"    shape: {shape}\n    text: {text}\n"
    )


# ── the shortlist itself ────────────────────────────────────────────────────


def test_the_shortlist_is_ten_questions_weighted_to_aggregation():
    questions = load_questions(QUESTIONS)

    assert [q.id for q in questions] == [f"Q{n:02}" for n in range(1, 11)]
    assert Counter(q.category for q in questions) == {
        "aggregate": 7,
        "multi-hop": 1,
        "lookup": 1,
        "absence": 1,
    }


def test_no_question_text_appears_in_either_system_prompt(tmp_path):
    prompts = system_prompt("markdown", tmp_path) + system_prompt("omnigraph", tmp_path)

    assert [q.id for q in load_questions(QUESTIONS) if q.text[:60] in prompts] == []


# ── what the loader refuses ─────────────────────────────────────────────────


def test_a_question_loads_with_its_fields(tmp_path):
    [q] = load_questions(write(tmp_path, one()))

    assert (q.id, q.category, q.shape, q.text) == (
        "Q01",
        "aggregate",
        "ranked_list",
        "What was discussed most?",
    )


@pytest.mark.parametrize(
    "body, complaint",
    [
        (one(shape="ranked"), "shape"),
        (one(category="trivia"), "category"),
        (one(text="''"), "text"),
        (one() + one().split("questions:\n")[1], "duplicate"),
        (one(id="question-1"), "id"),
    ],
)
def test_the_loader_refuses_a_malformed_question(tmp_path, body, complaint):
    with pytest.raises(ValueError, match=complaint):
        load_questions(write(tmp_path, body))


@pytest.mark.parametrize(
    "text",
    [
        "Which talks support pat-harness-over-model?",
        "What do the talks behind sig-foo-bar say?",
        "Which signals point to agent memory?",
        "What does co-anthropic ship?",
    ],
)
def test_the_loader_refuses_graph_vocabulary(tmp_path, text):
    with pytest.raises(ValueError, match="graph vocabulary"):
        load_questions(write(tmp_path, one(text=text)))
