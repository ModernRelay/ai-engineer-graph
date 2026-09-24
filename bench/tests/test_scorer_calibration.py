"""D1.5: the scorer (quote check + support judge) on 10 planted claims with known labels.

The judge's verdicts come from tests/fixtures/calibration_judgments.json, recorded from the real
judge by `bench calibrate`; nothing here calls the API."""

import json
from collections import Counter
from pathlib import Path

import pytest

from bench import judge
from bench.calibration import PLANTED, planted_run
from bench.cli import main
from bench.corpus import CHUNK_TALK_OVERRIDES, build_corpus, talk_labels
from bench.judge import request_key
from bench.score import score_runs, support_requests
from bench.verify import Corpus

SEED = Path(__file__).resolve().parents[2] / "seed"
TRANSCRIPTS = Path(__file__).resolve().parents[2] / "transcripts"
pytestmark = pytest.mark.skipif(
    not TRANSCRIPTS.is_dir(), reason="needs the local transcripts/ directory"
)
FIXTURE = Path(__file__).parent / "fixtures" / "calibration_judgments.json"


@pytest.fixture(scope="module")
def corpus(tmp_path_factory):
    talks = tmp_path_factory.mktemp("talks")
    build_corpus(SEED, TRANSCRIPTS, talks, CHUNK_TALK_OVERRIDES)
    return Corpus.load(talks, talk_labels(SEED, CHUNK_TALK_OVERRIDES))


@pytest.fixture
def recorded(tmp_path):
    """The recorded verdicts as a judge cache the scorer can read."""
    for key, output in json.loads(FIXTURE.read_text()).items():
        (tmp_path / f"{key}.json").write_text(json.dumps({"output": output}))
    return tmp_path


def test_the_plants_are_the_ten_the_spec_asks_for():
    kinds = Counter(plant.kind for plant in PLANTED)

    assert kinds == {"real": 5, "wrong_claim": 2, "invented": 2, "wrong_talk": 1}
    assert {p.expected for p in PLANTED if p.kind == "real"} == {"grounded"}
    assert {p.expected for p in PLANTED if p.kind != "real"} == {"hallucinated"}


def test_the_quote_check_labels_the_mechanical_plants(corpus):
    statuses = {p.kind: corpus.check(p.talk, p.quote).status for p in PLANTED}

    assert (statuses["real"], statuses["wrong_claim"]) == ("exact", "exact")
    assert (statuses["invented"], statuses["wrong_talk"]) == ("not_found", "wrong_talk")


def test_every_judged_plant_has_a_recorded_verdict(corpus):
    recorded = json.loads(FIXTURE.read_text())
    missing = [
        label
        for label, request in support_requests([planted_run()], corpus)
        if request_key(request) not in recorded
    ]

    assert not missing, f"no recorded verdict for {missing}: run `uv run bench calibrate`"


def test_the_scorer_gets_at_least_9_of_10_planted_claims_right(corpus, recorded):
    [scored] = score_runs([planted_run()], corpus, recorded)

    got = [claim["grounding"] for claim in scored["claims"]]
    wrong = [(p.kind, p.claim, g) for p, g in zip(PLANTED, got, strict=True) if g != p.expected]
    assert len(PLANTED) - len(wrong) >= 9, wrong


def test_calibrate_records_the_judges_verdicts_for_the_judged_plants(corpus, tmp_path, monkeypatch):
    verdicts = {p.claim: "supported" if p.kind == "real" else "unsupported" for p in PLANTED}

    def fake(request):
        claim = request["messages"][0]["content"].split("<claim>")[1].split("</claim>")[0]
        verdict = verdicts[claim]
        return {"output": {"verdict": verdict, "reason": "r"}, "usage": {}, "model": "m", "id": "x"}

    monkeypatch.setattr(judge, "openrouter_ask", lambda env: fake)
    talks = tmp_path / "talks"
    build_corpus(SEED, TRANSCRIPTS, talks, CHUNK_TALK_OVERRIDES)
    out = tmp_path / "fixture.json"

    code = main(
        [
            "calibrate",
            "--corpus",
            str(talks),
            "--seed",
            str(SEED),
            "--cache",
            str(tmp_path / "cache"),
            "--fixture",
            str(out),
        ]
    )

    assert code == 0
    saved = json.loads(out.read_text())
    assert len(saved) == 7
    assert sorted(o["verdict"] for o in saved.values()) == ["supported"] * 5 + ["unsupported"] * 2
