import json

import pytest

from bench import judge
from bench.cli import main
from bench.judge import cached, valid_support
from bench.questions import Question
from bench.score import (
    absence,
    cluster_requests,
    grounding,
    load_runs,
    pairwise_requests,
    pairwise_sections,
    pooled_recall,
    render_answer,
    score_runs,
    spread,
    support_requests,
    uncited_requests,
)
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
    """Answers support requests with a verdict and uncited requests with one statement."""

    def __init__(self):
        self.requests = []

    def __call__(self, request):
        self.requests.append(request)
        schema = request["output_config"]["format"]["schema"]
        if "winner" in schema["properties"]:  # always prefers answer A
            output = {r: "A" for r in ("coverage", "specificity", "correctness", "winner")}
            output["reason"] = "A is better."
        elif "groups" in schema["properties"]:  # each label its own group
            listed = (
                request["messages"][0]["content"].split("<labels>\n")[1].split("\n</labels>")[0]
            )
            labels = [line.split(". ", 1)[1] for line in listed.splitlines()]
            output = {"groups": [{"name": lb, "members": [n]} for n, lb in enumerate(labels, 1)]}
        elif "uncited" in schema["properties"]:
            output = {"uncited": ["An uncited fact."]}
        else:
            output = {"verdict": "supported", "reason": "It says so."}
        return {
            "output": output,
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

    assert scored["uncited"] is None  # not asked yet
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
    assert "uncited check: 2 runs, 0 cached, 2 to ask" in out
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

    assert len(fake.requests) == 6  # 2 claims, 2 runs' uncited checks, 1 pairing in 2 orders
    scores = json.loads((tmp_path / "scores.json").read_text())
    buckets = [c["grounding"] for run in scores["runs"] for c in run["claims"]]
    assert buckets == ["grounded", "hallucinated", "grounded"]
    assert [run["uncited"] for run in scores["runs"]] == [["An uncited fact."]] * 2
    assert (scores["judge"]["claims_judged"], scores["judge"]["runs_checked"]) == (2, 2)


def test_identical_claims_are_asked_once_and_costed_once(workspace, monkeypatch, capsys):
    tmp_path, paths = workspace
    same = [claim(REAL), claim(REAL)]
    write_run(tmp_path / "runs", result("Q02", "markdown", 1, same))
    fake = FakeJudge()
    monkeypatch.setattr(judge, "openrouter_ask", lambda env: fake)

    main(["score", "--dry-run", *paths])
    assert "4 to judge: 0 cached, 2 to ask" in capsys.readouterr().out

    assert main(["score", *paths]) == 0
    # 2 distinct claims; 2 distinct uncited checks, since both markdown answers list the same
    # claim texts with the same (empty) prose; Q01's pairing in 2 orders (Q02 has no omnigraph run)
    assert len(fake.requests) == 2 + 2 + 2
    scores = json.loads((tmp_path / "scores.json").read_text())
    assert scores["judge"]["claims_judged"] == 4
    assert scores["judge"]["cost_usd"] == 6 * 0.014  # 1000 in × $4 + 500 out × $20 per Mtok


def test_the_judge_gets_the_title_of_the_talk_the_citation_resolves_to(workspace):
    tmp_path, _ = workspace
    corpus = Corpus.load(tmp_path / "talks", labels={"alpha-talk": "ia-aie-alpha-talk"})
    runs = [result("Q01", "omnigraph", 1, [claim(REAL, talk="alpha-talk")])]

    [(_, request)] = support_requests(runs, corpus)

    assert request["messages"][0]["content"].startswith("<talk>Alpha</talk>")


def test_every_run_gets_one_uncited_check_with_its_prose_and_claims(corpus):
    runs = [
        {**result("Q01", "markdown", 1, [claim(REAL)]), "answer_text": "Prose.\n```json\n{}\n```"},
        {
            "qid": "Q01",
            "arm": "omnigraph",
            "run": 1,
            "answer_json": None,
            "answer_text": "Only prose.",
        },
    ]

    [(label1, first), (label2, second)] = uncited_requests(runs)

    assert (label1, label2) == ("Q01 markdown #1", "Q01 omnigraph #1")
    assert "<answer>\nProse.\n</answer>" in first["messages"][0]["content"]
    assert "- Evals gate releases." in first["messages"][0]["content"]
    assert "<answer>\nOnly prose.\n</answer>" in second["messages"][0]["content"]
    assert "(none)" in second["messages"][0]["content"]


def test_scores_wait_for_every_uncited_check_too(workspace, monkeypatch, capsys):
    tmp_path, paths = workspace
    fake = FakeJudge()

    def support_only(request):
        if "uncited" in request["output_config"]["format"]["schema"]["properties"]:
            raise judge.JudgeError("judge stopped with refusal")
        return fake(request)

    monkeypatch.setattr(judge, "openrouter_ask", lambda env: support_only)

    assert main(["score", *paths]) == 1

    assert (
        "still unjudged: 0 claims, 2 runs, 0 cluster questions, 1 pairings"
        in capsys.readouterr().out
    )
    assert not (tmp_path / "scores.json").exists()


# pooled_recall (D2.1): groups found by any run, pooled when one of their claims is grounded.


def scored(arm, run, labels, claims):
    """A scored run: labels at positions 1..n; claims as (item position, grounding, talk)."""
    return {
        "qid": "Q05",
        "arm": arm,
        "run": run,
        "items": [{"position": n, "label": label} for n, label in enumerate(labels, 1)],
        "claims": [
            {"item_position": p, "grounding": g, "quote_check": {"talk": t}} for p, g, t in claims
        ],
    }


COMPANIES = [
    scored(
        "markdown",
        1,
        ["AWS", "Anthropic", "Google"],
        [(1, "grounded", "t1"), (2, "grounded", "t2"), (3, "hallucinated", "t3")],
    ),
    scored(
        "omnigraph",
        1,
        ["Anthropic", "Amazon Web Services", "Meta", "Meta Platforms"],
        [(1, "grounded", "t2"), (2, "partial", "t1"), (3, "grounded", "t4")],
    ),
]
GROUPS = {
    "AWS": "Amazon",
    "Amazon Web Services": "Amazon",
    "Anthropic": "Anthropic",
    "Google": "Google",
    "Meta": "Meta",
    "Meta Platforms": "Meta",
}


def test_a_group_is_pooled_when_any_run_grounds_one_of_its_claims():
    recall = pooled_recall("ranked_list", COMPANIES, GROUPS)

    assert {g["name"]: g["pooled"] for g in recall["groups"]} == {
        "Amazon": True,
        "Anthropic": True,
        "Google": False,  # its only claim is hallucinated
        "Meta": True,
    }
    assert next(g for g in recall["groups"] if g["name"] == "Meta")["members"] == [
        "Meta",
        "Meta Platforms",
    ]


def test_recall_counts_a_group_once_however_many_labels_a_run_has_in_it():
    runs = pooled_recall("ranked_list", COMPANIES, GROUPS)["runs"]

    assert [(r["arm"], r["found"], r["recall"]) for r in runs] == [
        ("markdown", ["Amazon", "Anthropic", "Google"], 2 / 3),
        ("omnigraph", ["Amazon", "Anthropic", "Meta"], 1.0),
    ]


def test_top_overlap_is_against_the_consensus_of_pooled_groups():
    recall = pooled_recall("ranked_list", COMPANIES, GROUPS)

    # k = the longest list (4); Amazon and Anthropic are in both runs' top 4 (mean position 1.5,
    # name breaks the tie), Meta in one
    assert (recall["k"], recall["consensus_top"]) == (4, ["Amazon", "Anthropic", "Meta"])
    assert [r["overlap"] for r in recall["runs"]] == [2 / 3, 1.0]


def test_a_company_set_has_no_ranking_to_overlap():
    recall = pooled_recall("company_set", COMPANIES, GROUPS)

    assert "consensus_top" not in recall
    assert [r["overlap"] for r in recall["runs"]] == [None, None]


def test_a_talk_set_groups_items_by_the_talks_their_claims_cite():
    runs = [
        scored(
            "markdown", 1, ["Talk A", "Talk B"], [(1, "grounded", "tA"), (2, "hallucinated", "tB")]
        ),
        scored("omnigraph", 1, ["B again"], [(1, "grounded", "tB")]),
    ]

    recall = pooled_recall("talk_set", runs)

    assert {g["name"]: (g["members"], g["pooled"]) for g in recall["groups"]} == {
        "tA": (["Talk A"], True),
        "tB": (["B again", "Talk B"], True),
    }
    # the markdown run found tB too, though its own claim for it isn't grounded
    assert [r["recall"] for r in recall["runs"]] == [1.0, 0.5]


def test_recall_is_none_when_nothing_is_pooled():
    runs = [scored("markdown", 1, ["X"], [(1, "hallucinated", "t1")])]

    assert pooled_recall("company_set", runs, {"X": "X"})["runs"][0]["recall"] is None


# bench score and D2.1: cluster requests for ranked lists and company sets.

QUESTIONS = {
    "Q05": Question("Q05", "aggregate", "ranked_list", "Which five companies gave the most talks?"),
    "Q08": Question("Q08", "multi-hop", "prose", "?"),
}


def with_items(qid, arm, run, labels, claims):
    record = result(qid, arm, run, claims)
    record["answer_json"]["items"] = [{"label": lb, "rank": n} for n, lb in enumerate(labels, 1)]
    return record


def test_only_clustered_questions_with_items_get_a_cluster_request():
    runs = [
        with_items("Q05", "markdown", 1, ["AWS", "Anthropic"], []),
        with_items("Q05", "omnigraph", 1, ["Anthropic"], []),
        with_items("Q08", "markdown", 1, ["Voice"], []),
    ]

    [(label, request, count)] = cluster_requests(runs, QUESTIONS)

    assert (label, count) == ("Q05 clusters", 2)
    assert "Which five companies gave the most talks?" in request["messages"][0]["content"]
    assert "1. AWS\n2. Anthropic" in request["messages"][0]["content"]


def test_score_asks_the_clusters_and_writes_recall(workspace, monkeypatch, capsys):
    tmp_path, paths = workspace
    real = claim(REAL) | {"item": "AWS"}
    write_run(tmp_path / "runs", with_items("Q05", "markdown", 1, ["AWS", "Anthropic"], [real]))
    fake = FakeJudge()
    monkeypatch.setattr(judge, "openrouter_ask", lambda env: fake)

    main(["score", "--dry-run", *paths])
    assert "clusters: 1 questions, 0 cached, 1 to ask" in capsys.readouterr().out

    assert main(["score", *paths]) == 0
    recall = json.loads((tmp_path / "scores.json").read_text())["recall"]
    # only AWS has a grounded claim, so the pool and the consensus top list are just AWS
    assert recall["Q05"]["consensus_top"] == ["AWS"]
    assert recall["Q05"]["runs"] == [
        {"arm": "markdown", "run": 1, "found": ["AWS", "Anthropic"], "recall": 1.0, "overlap": 1.0}
    ]


def test_the_consensus_breaks_ties_on_mean_position_before_name():
    runs = [
        scored("markdown", n, ["Zeta", "Alpha"], [(1, "grounded", "t1"), (2, "grounded", "t2")])
        for n in (1, 2)
    ]

    recall = pooled_recall("ranked_list", runs, {"Zeta": "Zeta", "Alpha": "Alpha"})

    assert recall["consensus_top"] == ["Zeta", "Alpha"]  # both in 2 top lists; Zeta ranks first


def test_scores_wait_for_the_clusters_too(workspace, monkeypatch, capsys):
    tmp_path, paths = workspace
    write_run(tmp_path / "runs", with_items("Q05", "markdown", 1, ["AWS"], [claim(REAL)]))
    fake = FakeJudge()

    def no_clusters(request):
        if "groups" in request["output_config"]["format"]["schema"]["properties"]:
            raise judge.JudgeError("judge stopped with max_tokens")
        return fake(request)

    monkeypatch.setattr(judge, "openrouter_ask", lambda env: no_clusters)

    assert main(["score", *paths]) == 1

    assert (
        "still unjudged: 0 claims, 0 runs, 1 cluster questions, 0 pairings"
        in capsys.readouterr().out
    )
    assert not (tmp_path / "scores.json").exists()


def test_a_fixed_length_list_reports_how_much_the_arms_agree_on_their_top_n():
    runs = [
        scored("markdown", 1, ["AWS", "Anthropic", "Meta"], [(1, "grounded", "t1")]),
        scored(
            "omnigraph", 1, ["Anthropic", "Amazon Web Services", "Meta"], [(1, "grounded", "t2")]
        ),
        scored("markdown", 2, ["Meta"], []),  # lists fewer than the 2 asked for
        scored("omnigraph", 2, ["Meta", "Google"], []),
    ]

    recall = pooled_recall("ranked_list", runs, GROUPS, count=2)

    # run 1: both top 2s are {Amazon, Anthropic}; the shared Meta at position 3 doesn't count.
    # run 2: {Meta} and {Meta, Google} share 1 of the 2 asked for.
    assert recall["count"] == 2
    assert recall["agreement"] == {
        "pairs": [
            {"run": 1, "shared": 2, "agreement": 1.0},
            {"run": 2, "shared": 1, "agreement": 0.5},
        ],
        "mean": 0.75,
    }


def test_an_open_list_has_no_agreement():
    assert "agreement" not in pooled_recall("ranked_list", COMPANIES, GROUPS)


# D2.3 consistency and D2.4 absence.

THREE_RUNS = [
    scored("markdown", 1, ["A", "B"], []),
    scored("markdown", 2, ["B", "A"], []),
    scored("markdown", 3, ["A", "C"], []),
    scored("omnigraph", 1, ["D"], []),
    scored("omnigraph", 2, ["D"], []),
    scored("omnigraph", 3, ["D"], []),
]
ALONE = {label: label for label in "ABCD"}


def test_consistency_is_the_mean_jaccard_over_each_arms_run_pairs():
    consistency = pooled_recall("company_set", THREE_RUNS, ALONE)["consistency"]

    # md: {A,B}~{A,B} 1, {A,B}~{A,C} 1/3, {A,B}~{A,C} 1/3; og: always {D}
    assert consistency == {"markdown": pytest.approx(5 / 9), "omnigraph": 1.0}


def test_a_fixed_length_lists_consistency_looks_at_the_top_n_only():
    consistency = pooled_recall("ranked_list", THREE_RUNS, ALONE, count=1)["consistency"]

    assert consistency["markdown"] == pytest.approx(1 / 3)  # top 1: A, B, A


def test_an_absence_answer_is_correct_only_with_no_items_and_no_claims():
    runs = [
        {"arm": "markdown", "run": 1, "items": [], "claims": []},
        {"arm": "omnigraph", "run": 1, "items": [], "claims": [{"grounding": "grounded"}]},
        {"arm": "omnigraph", "run": 2, "items": [{"label": "FPGA talk"}], "claims": []},
    ]

    assert absence(runs) == [
        {"arm": "markdown", "run": 1, "correct": True, "items": 0, "claims": 0},
        {"arm": "omnigraph", "run": 1, "correct": False, "items": 0, "claims": 1},
        {"arm": "omnigraph", "run": 2, "correct": False, "items": 1, "claims": 0},
    ]


def test_score_writes_the_absence_rows_for_the_absence_question(workspace, monkeypatch):
    tmp_path, paths = workspace
    write_run(tmp_path / "runs", result("Q10", "markdown", 1, []))
    write_run(tmp_path / "runs", result("Q10", "omnigraph", 1, [claim(REAL)]))
    monkeypatch.setattr(judge, "openrouter_ask", lambda env: FakeJudge())

    assert main(["score", *paths]) == 0

    rows = json.loads((tmp_path / "scores.json").read_text())["absence"]["Q10"]
    assert [(r["arm"], r["correct"]) for r in rows] == [("markdown", True), ("omnigraph", False)]


# D2.2 pairwise: redacted, annotated answers; both orders; an arm wins only if it wins both.

QUESTION_Q01 = {"Q01": Question("Q01", "aggregate", "ranked_list", "Most discussed topics?")}


def scored_claim(claim_text, status, verdict, bucket, talk="ia-aie-alpha-talk"):
    return {
        "claim": claim_text,
        "quote_check": {"status": status, "talk": talk},
        "support": {"verdict": verdict} if verdict else None,
        "grounding": bucket,
    }


def test_an_answer_is_rendered_redacted_with_its_claims_graded_and_its_uncited_statements():
    corpus = Corpus(
        texts={"ia-aie-alpha-talk": TALK}, labels={}, titles={"ia-aie-alpha-talk": "Alpha (Ann)"}
    )
    record = {"answer_text": "I searched this knowledge graph.\n```json\n{}\n```"}
    run = {
        "claims": [
            scored_claim("Evals gate releases.", "exact", "supported", "grounded"),
            scored_claim("Most teams skip evals.", "exact", "partial", "partial"),
            scored_claim("Invented.", "not_found", None, "hallucinated"),
            scored_claim("Misattributed.", "wrong_talk", None, "hallucinated", talk=None),
            scored_claim("Unsupported.", "exact", "unsupported", "hallucinated"),
        ],
        "uncited": ["Lyft gates launches."],
    }

    assert render_answer(record, run, corpus, {}) == (
        "I searched the sources.\n\n"
        "Claims:\n"
        "- grounded: Evals gate releases. (Alpha (Ann))\n"
        "- partial, the quote supports only part of it: Most teams skip evals. (Alpha (Ann))\n"
        "- hallucinated, the quote isn't in the cited talk: Invented. (Alpha (Ann))\n"
        "- hallucinated, the quote is from a different talk: Misattributed. (an unknown talk)\n"
        "- hallucinated, the quote doesn't support it: Unsupported. (Alpha (Ann))\n\n"
        "Statements with no cited quote:\n"
        "- Lyft gates launches."
    )


def test_an_answer_without_claims_or_uncited_statements_says_none():
    corpus = Corpus(texts={}, labels={})
    text = render_answer(
        {"answer_text": "Nothing covers it."}, {"claims": [], "uncited": []}, corpus, {}
    )

    assert text.endswith("Claims:\n(none)\n\nStatements with no cited quote:\n(none)")


def pairing_runs():
    records = [
        {"qid": "Q01", "arm": arm, "run": n, "answer_text": f"{arm[0].upper()} answer {n}."}
        for arm, n in (("markdown", 1), ("omnigraph", 1), ("markdown", 2))
    ]
    scored_runs = [{**r, "claims": [], "uncited": []} for r in records]
    return records, scored_runs


def test_each_run_pairing_is_asked_in_both_orders():
    records, scored_runs = pairing_runs()

    todo = pairwise_requests(records, scored_runs, Corpus({}, {}), {}, QUESTION_Q01)

    assert [(label, arm_a) for label, _, arm_a in todo] == [
        ("Q01 #1 markdown first", "markdown"),
        ("Q01 #1 omnigraph first", "omnigraph"),
    ]  # run 2 has no omnigraph answer to pair with
    first, second = (request["messages"][0]["content"] for _, request, _ in todo)
    assert first.index("M answer 1") < first.index("O answer 1")
    assert second.index("O answer 1") < second.index("M answer 1")


@pytest.mark.parametrize(
    "first, second, result, agree",
    [
        ("A", "A", "tie", False),  # each order prefers whichever answer came first
        ("A", "B", "markdown", True),
        ("B", "A", "omnigraph", True),
        ("tie", "tie", "tie", True),
        ("A", "tie", "tie", False),
    ],
)
def test_an_arm_wins_a_pairing_only_by_winning_both_orders(tmp_path, first, second, result, agree):
    records, scored_runs = pairing_runs()
    todo = pairwise_requests(records, scored_runs, Corpus({}, {}), {}, QUESTION_Q01)
    for (_, request, _), pick in zip(todo, (first, second), strict=True):
        ratings = {r: pick for r in ("coverage", "specificity", "correctness", "winner")}
        cached(request, lambda _, o=ratings: {"output": o | {"reason": "r"}, "usage": {}}, tmp_path)

    [pairing] = pairwise_sections(records, scored_runs, Corpus({}, {}), {}, QUESTION_Q01, tmp_path)[
        "Q01"
    ]

    assert (pairing["run"], pairing["result"], pairing["agree"]) == (1, result, agree)
    assert [o["a"] for o in pairing["orders"]] == ["markdown", "omnigraph"]


def test_pairwise_is_none_while_a_pairing_is_unjudged(tmp_path):
    records, scored_runs = pairing_runs()

    sections = pairwise_sections(records, scored_runs, Corpus({}, {}), {}, QUESTION_Q01, tmp_path)

    assert sections == {"Q01": None}


def test_score_asks_the_pairings_once_the_first_round_is_judged(workspace, monkeypatch, capsys):
    tmp_path, paths = workspace
    monkeypatch.setattr(judge, "openrouter_ask", lambda env: FakeJudge())

    main(["score", "--dry-run", *paths])
    assert "pairwise: waits for the claims and uncited checks" in capsys.readouterr().out

    assert main(["score", *paths]) == 0
    main(["score", "--dry-run", *paths])
    assert "pairwise: 1 pairings × 2 orders, 2 cached, 0 to ask" in capsys.readouterr().out
    [pairing] = json.loads((tmp_path / "scores.json").read_text())["pairwise"]["Q01"]
    assert (pairing["result"], pairing["agree"]) == ("tie", False)  # the fake always picks A
