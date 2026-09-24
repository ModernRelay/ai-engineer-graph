from bench.key import assemble_q03, key_match_request, score_q03, top_claims

RANKING = [
    {"pattern": "pat-a", "thesis": "A", "brief": "a", "contradictions": 5},
    {"pattern": "pat-b", "thesis": "B", "brief": "b", "contradictions": 3},
    {"pattern": "pat-c", "thesis": "C", "brief": "c", "contradictions": 2},
    {"pattern": "pat-d", "thesis": "D", "brief": "d", "contradictions": 1},
]
PUSHBACK = [
    {"pattern": "pat-a", "polarity": "contradiction", "talk": "ia-aie-x", "signals": 2},
    {"pattern": "pat-a", "polarity": "contradiction", "talk": "ia-aie-y", "signals": 1},
    {"pattern": "pat-a", "polarity": "boundary", "talk": "ia-aie-z", "signals": 1},
    {"pattern": "pat-b", "polarity": "contradiction", "talk": "ia-aie-x", "signals": 1},
]
SUPPORT = [
    {"pattern": "pat-a", "talk": "ia-aie-s1", "signals": 4},
    {"pattern": "pat-a", "talk": "ia-aie-s2", "signals": 1},
]


def test_top_claims_keeps_ties_at_the_cutoff():
    tied = RANKING[:2] + [{**RANKING[2], "contradictions": 3}]

    assert [c["pattern"] for c in top_claims(tied, 2)] == ["pat-a", "pat-b", "pat-c"]
    assert [c["pattern"] for c in top_claims(RANKING, 3)] == ["pat-a", "pat-b", "pat-c"]


def test_key_splits_contradiction_talks_from_boundary_talks():
    key = assemble_q03(RANKING, PUSHBACK, SUPPORT, count=3)
    a = key["claims"][0]

    assert a["against_talks"] == ["ia-aie-x", "ia-aie-y"]
    assert a["boundary_talks"] == ["ia-aie-z"]
    assert a["leading_support_talks"] == ["ia-aie-s1", "ia-aie-s2"]
    assert [c["key"] for c in key["claims"]] == [1, 2, 3]


def run_with(items, claims):
    return {
        "qid": "Q03",
        "arm": "markdown",
        "run": 1,
        "question": "q?",
        "answer_text": "prose",
        "answer_json": {"items": items, "claims": claims},
        "wall_s": 100,
        "cost_usd": 0.5,
        "tool_calls": 20,
    }


def claim(item, talk):
    return {
        "item": item,
        "claim": "c",
        "talk": talk,
        "quote": "one two three four five six seven eight",
    }


def test_score_counts_key_claims_and_pushback_talks_by_side():
    key = assemble_q03(RANKING, PUSHBACK, SUPPORT, count=3)
    run = run_with(
        [{"label": "A debate"}, {"label": "Something else"}],
        [
            claim("A debate", "ia-aie-x"),  # against, in the key
            claim("A debate", "ia-aie-z"),  # against, a boundary talk: accepted, not required
            claim("A debate", "x-label"),  # for, through a chunk label
            claim("Something else", "ia-aie-y"),
        ],
    )
    match = {
        "items": [{"position": 1, "key": 1}, {"position": 2, "key": 0}],
        "claims": [
            {"index": 0, "stance": "against"},
            {"index": 1, "stance": "against"},
            {"index": 2, "stance": "for"},
            {"index": 3, "stance": "against"},
        ],
    }

    s = score_q03(key, run, match, labels={"x-label": "ia-aie-s1"})
    a = s["per_claim"][0]

    assert s["claims_found"] == 1 and s["claims_recall"] == round(1 / 3, 3)
    assert a["against_recall"] == 0.5
    assert a["against_precision"] == 1.0
    assert a["for_named"] == ["ia-aie-s1"] and a["leading_for_hits"] == 1
    assert s["outside_key"] == ["Something else"]
    assert s["against_recall"] == round(1 / 3, 3)  # 1 of the key's 3 contradiction talks


def test_match_request_shows_the_key_and_the_answer_but_no_arm():
    key = assemble_q03(RANKING, PUSHBACK, SUPPORT, count=3)
    request = key_match_request("q?", key, run_with([{"label": "E"}], [claim("E", "ia-aie-x")]))
    content = request["messages"][0]["content"]

    assert "1. A: a" in content and "1. E" in content and "(talk ia-aie-x)" in content
    assert "markdown" not in content and "omnigraph" not in content
