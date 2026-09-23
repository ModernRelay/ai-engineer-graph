import json

import pytest

from bench import judge
from bench.cli import main
from bench.judge import cached, valid_support
from bench.score import grounding, load_runs, score_runs, spread, support_requests
from bench.verify import Corpus

TALK = (
    "Every eval now runs inside the release pipeline before a change ships.\n\n"
    "The harness matters more than the model for what reaches customers."
)
REAL = "every eval now runs inside the release pipeline"
OTHER = "voice agents must handle interruptions gracefully or users hang up"


def claim(quote, talk="ia-aie-alpha-talk", text="Evals gate releases."):
    return {"item": "", "claim": text, "talk": talk, "quote": quote}


def result(qid, arm, run, claims):
    return {"qid": qid, "arm": arm, "run": run, "answer_json": {"items": [], "claims": claims}}


def write_run(runs_dir, record):
    path = runs_dir / record["qid"] / record["arm"] / str(record["run"]) / "result.json"
    path.parent.mkdir(parents=True)
    path.write_text(json.dumps(record))


@pytest.fixture
def corpus():
    return Corpus(texts={"ia-aie-alpha-talk": TALK, "ia-aie-beta-talk": OTHER}, labels={})


class FakeJudge:
    def __init__(self):
        self.requests = []

    def __call__(self, request):
        self.requests.append(request)
        return {
            "output": {"verdict": "supported", "reason": "It says so."},
            "usage": {"input_tokens": 1000, "output_tokens": 500},
            "model": "anthropic/claude-opus-5.5",
            "id": f"gen-{len(self.requests)}",
        }


def test_load_runs_reads_only_the_question_run_dirs_in_order(tmp_path):
    write_run(tmp_path, result("Q02", "markdown", 1, []))
    write_run(tmp_path, result("Q01", "omnigraph", 2, []))
    write_run(tmp_path / "_pilot", result("Q01", "markdown", 1, []))
    write_run(tmp_path, result("_old", "markdown", 1, []))  # an archive laid out like a run

    assert [(r["qid"], r["arm"], r["run"]) for r in load_runs(tmp_path)] == [
        ("Q01", "omnigraph", 2),
        ("Q02", "markdown", 1),
    ]


@pytest.mark.parametrize(
    "status, verdict, bucket",
    [
        ("exact", "supported", "grounded"),
        ("fuzzy", "supported", "grounded"),
        ("spliced", "supported", "grounded"),
        ("exact", "partial", "partial"),
        ("fuzzy", "unsupported", "hallucinated"),
        ("not_found", None, "hallucinated"),
        ("wrong_talk", None, "hallucinated"),
        ("exact", None, None),
    ],
)
def test_grounding_buckets(status, verdict, bucket):
    assert grounding(status, verdict) == bucket


def test_spread_picks_evenly_across_the_list():
    assert spread(list(range(10)), 3) == [0, 3, 6]
    assert spread([1, 2], 5) == [1, 2]


def test_only_claims_found_in_their_talk_are_sent_to_the_judge(corpus):
    runs = [
        result("Q01", "markdown", 1, [claim(REAL), claim(OTHER), claim("made up entirely here")])
    ]

    todo = support_requests(runs, corpus)

    assert [
        (label, request["messages"][0]["content"].lower().count(REAL)) for label, request in todo
    ] == [("Q01 markdown #1 c0", 2)]


def test_scores_carry_the_quote_check_the_cached_verdict_and_the_bucket(corpus, tmp_path):
    runs = [result("Q01", "omnigraph", 1, [claim(REAL), claim(OTHER), claim(REAL, text="Other.")])]
    [(_, first), _] = support_requests(runs, corpus)
    cached(first, FakeJudge(), tmp_path, valid_support)

    [scored] = score_runs(runs, corpus, tmp_path)

    judged, elsewhere, unjudged = scored["claims"]
    assert (judged["quote_check"]["status"], judged["support"]["verdict"]) == ("exact", "supported")
    assert judged["grounding"] == "grounded"
    assert (elsewhere["quote_check"]["status"], elsewhere["support"]) == ("wrong_talk", None)
    assert elsewhere["grounding"] == "hallucinated"
    assert (unjudged["support"], unjudged["grounding"]) == (None, None)


def test_an_unparseable_answer_scores_no_claims(corpus, tmp_path):
    runs = [{"qid": "Q01", "arm": "markdown", "run": 1, "answer_json": None}]

    [scored] = score_runs(runs, corpus, tmp_path)

    assert scored["unparseable"] and scored["claims"] == []


# bench score: the CLI over a small runs dir, corpus and seed, with a fake judge.


@pytest.fixture
def workspace(tmp_path):
    runs, talks, seed = tmp_path / "runs", tmp_path / "talks", tmp_path / "seed"
    write_run(runs, result("Q01", "markdown", 1, [claim(REAL), claim("made up entirely here")]))
    write_run(runs, result("Q01", "omnigraph", 1, [claim(REAL, "alpha-talk", "Evals run first.")]))
    talks.mkdir()
    (talks / "ia-aie-alpha-talk.md").write_text("# Alpha\n- talk: ia-aie-alpha-talk\n\n" + TALK)
    (seed / "chunks").mkdir(parents=True)
    edge = {"edge": "PartOfArtifact", "from": "alpha-talk#0", "to": "ia-aie-alpha-talk"}
    (seed / "chunks" / "part-01.jsonl").write_text(json.dumps(edge) + "\n")
    paths = ["--runs-dir", runs, "--corpus", talks, "--seed", seed]
    paths += ["--cache", tmp_path / "cache", "--out", tmp_path / "scores.json"]
    return tmp_path, [str(p) for p in paths]


def test_score_dry_run_counts_without_asking(workspace, monkeypatch, capsys):
    tmp_path, paths = workspace
    monkeypatch.setattr(judge, "openrouter_ask", lambda env: pytest.fail("the judge was called"))

    assert main(["score", "--dry-run", *paths]) == 0

    out = capsys.readouterr().out
    assert "2 runs, 3 claims, 2 to judge: 0 cached, 2 to ask" in out
    assert not (tmp_path / "scores.json").exists()


def test_score_with_a_limit_judges_that_many_and_writes_no_partial_scores(workspace, monkeypatch):
    tmp_path, paths = workspace
    fake = FakeJudge()
    monkeypatch.setattr(judge, "openrouter_ask", lambda env: fake)

    assert main(["score", "--limit", "1", *paths]) == 0

    assert len(fake.requests) == 1
    assert not (tmp_path / "scores.json").exists()


def test_score_writes_scores_once_every_claim_is_judged(workspace, monkeypatch):
    tmp_path, paths = workspace
    fake = FakeJudge()
    monkeypatch.setattr(judge, "openrouter_ask", lambda env: fake)

    assert main(["score", "--limit", "1", *paths]) == 0
    assert main(["score", *paths]) == 0

    assert len(fake.requests) == 2
    scores = json.loads((tmp_path / "scores.json").read_text())
    buckets = [c["grounding"] for run in scores["runs"] for c in run["claims"]]
    assert buckets == ["grounded", "hallucinated", "grounded"]
    assert scores["judge"]["judgments"] == 2


def test_identical_claims_are_asked_once_and_costed_once(workspace, monkeypatch, capsys):
    tmp_path, paths = workspace
    same = [claim(REAL), claim(REAL)]
    write_run(tmp_path / "runs", result("Q02", "markdown", 1, same))
    fake = FakeJudge()
    monkeypatch.setattr(judge, "openrouter_ask", lambda env: fake)

    main(["score", "--dry-run", *paths])
    assert "4 to judge: 0 cached, 2 to ask" in capsys.readouterr().out

    assert main(["score", *paths]) == 0
    assert len(fake.requests) == 2
    scores = json.loads((tmp_path / "scores.json").read_text())
    assert scores["judge"]["judgments"] == 4
    assert scores["judge"]["cost_usd"] == 2 * 0.014  # 1000 in × $4 + 500 out × $20 per Mtok
