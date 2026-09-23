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


# ── check_terms and the corpus check (B1.2) ─────────────────────────────────


def with_terms(terms: str, **kw) -> str:
    return one(**kw) + f"    check_terms: {terms}\n"


def test_check_terms_load_as_a_tuple(tmp_path):
    [q] = load_questions(write(tmp_path, with_terms("[memory, 'voice agent']")))

    assert q.check_terms == ("memory", "voice agent")


@pytest.mark.parametrize("terms", ["memory", "[memory, '']", "[]"])
def test_malformed_check_terms_are_refused(tmp_path, terms):
    with pytest.raises(ValueError, match="check_terms"):
        load_questions(write(tmp_path, with_terms(terms)))


@pytest.fixture
def corpus(tmp_path):
    talks = tmp_path / "talks"
    talks.mkdir()
    (talks / "ia-aie-a.md").write_text(
        "# A (Ann, Acme — AIE)\nWe built persistent Memory for agents.\n"
    )
    (talks / "ia-aie-b.md").write_text(
        "# B (Bo, Beta — AIE)\nOur voice agent handles memory too.\n"
    )
    (talks / "ia-aie-c.md").write_text("# C (Cy, Acme — AIE)\nCoding agents need review.\n")
    return talks


def question(shape="talk_set", terms=("memory",), category="aggregate"):
    from bench.questions import Question

    return Question("Q01", category, shape, "What?", tuple(terms))


def test_the_check_counts_talks_per_term_case_insensitively(corpus):
    from bench.questions import check_questions

    [result] = check_questions([question(terms=("memory", "voice agent"))], corpus)

    assert result["ok"] is True
    assert result["hits"] == {"memory": 2, "voice agent": 1}


def test_a_term_no_talk_mentions_fails_the_question(corpus):
    from bench.questions import check_questions

    [result] = check_questions([question(terms=("memory", "neuromorphic"))], corpus)

    assert result["ok"] is False
    assert result["hits"]["neuromorphic"] == 0


def test_an_absence_question_passes_only_when_nothing_matches(corpus):
    from bench.questions import check_questions

    absent = question(shape="absence", category="absence", terms=("fpga", "neuromorphic"))
    present = question(shape="absence", category="absence", terms=("fpga", "coding agents"))

    assert [r["ok"] for r in check_questions([absent, present], corpus)] == [True, False]


def test_a_question_without_check_terms_fails(corpus):
    from bench.questions import check_questions

    [result] = check_questions([question(terms=())], corpus)

    assert result["ok"] is False
    assert "no check_terms" in result["detail"]


def test_check_questions_command_exits_nonzero_on_a_failing_question(tmp_path, corpus, capsys):
    from bench.cli import main

    good = write(tmp_path, with_terms("[memory]"))
    assert main(["check-questions", "--questions", str(good), "--corpus", str(corpus)]) == 0

    bad = tmp_path / "bad.yaml"
    bad.write_text(with_terms("[neuromorphic]"))
    assert main(["check-questions", "--questions", str(bad), "--corpus", str(corpus)]) == 1
    assert "neuromorphic" in capsys.readouterr().out
