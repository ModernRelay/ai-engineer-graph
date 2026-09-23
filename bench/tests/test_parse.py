from bench.parse import answer_block, normalise

BLOCK = '```json\n{"items": [{"label": "evals", "rank": 1}], "claims": []}\n```'


def test_the_block_after_the_prose_is_parsed():
    reply = f"Evals came up most.\n\n{BLOCK}\n"

    assert answer_block(reply) == {"items": [{"label": "evals", "rank": 1}], "claims": []}


def test_the_last_json_block_wins():
    draft = '```json\n{"items": [], "claims": [{"claim": "draft"}]}\n```'

    assert answer_block(f"{draft}\nOn reflection:\n{BLOCK}")["items"][0]["label"] == "evals"


def test_a_reply_without_a_block_has_no_answer():
    assert answer_block("Nothing in the talks covers this.") is None


def test_a_block_that_is_not_valid_json_has_no_answer():
    assert answer_block('```json\n{"items": [,]}\n```') is None


def test_a_block_that_is_not_an_object_has_no_answer():
    assert answer_block("```json\n[1, 2]\n```") is None


# normalise (D1.1): fixed-shape items and claims from a run's answer_json.

QUOTE = "we moved every eval into the pipeline so nothing ships without one"  # 12 words


def claim(**fields):
    return {
        "item": "",
        "claim": "Evals gate releases.",
        "talk": "ia-aie-x",
        "quote": QUOTE,
    } | fields


def test_no_answer_block_is_unparseable():
    answer = normalise(None)

    assert answer.unparseable
    assert answer.items == () and answer.claims == ()


def test_items_keep_list_order_and_tied_ranks():
    answer = normalise(
        {
            "items": [
                {"label": "evals", "rank": 1, "talk_count": 12},
                {"label": "memory", "rank": 1},
                {"label": "voice", "rank": 3, "talk_count": 2},
            ],
            "claims": [],
        }
    )

    assert not answer.unparseable
    assert [(i.position, i.label, i.rank, i.talk_count) for i in answer.items] == [
        (1, "evals", 1, 12),
        (2, "memory", 1, None),
        (3, "voice", 3, 2),
    ]


def test_a_rank_that_is_not_an_integer_is_none():
    answer = normalise({"items": [{"label": "a", "rank": "2"}, {"label": "b", "rank": True}]})

    assert [i.rank for i in answer.items] == [None, None]


def test_missing_or_non_list_fields_count_as_empty_and_flag_the_answer():
    answer = normalise({"items": "evals, memory"})

    assert answer.items == () and answer.claims == ()
    assert answer.flags == ("bad_items", "bad_claims")
    assert not answer.unparseable


def test_entries_that_are_not_objects_are_dropped_and_counted():
    answer = normalise({"items": ["evals", {"label": "memory"}], "claims": [7, claim()]})

    assert [i.label for i in answer.items] == ["memory"]
    assert answer.items[0].position == 1
    assert (answer.dropped_items, answer.dropped_claims) == (1, 1)
    assert [c.index for c in answer.claims] == [1]


def test_text_fields_are_trimmed_and_numbers_become_strings():
    answer = normalise(
        {"items": [{"label": 2026}], "claims": [claim(claim="  Evals gate releases. ", talk=None)]}
    )

    assert answer.items[0].label == "2026"
    assert answer.claims[0].claim == "Evals gate releases."
    assert answer.claims[0].talk == ""
    assert "missing_talk" in answer.claims[0].flags


def test_brackets_around_a_chunk_label_are_stripped():
    answer = normalise(
        {
            "items": [],
            "claims": [
                claim(talk=" [klein-browserbase-agents-www] "),
                claim(talk="klein-browserbase-agents-www"),
                claim(talk="ia-aie-klein-agents-www"),
            ],
        }
    )

    assert [c.talk for c in answer.claims] == [
        "klein-browserbase-agents-www",
        "klein-browserbase-agents-www",
        "ia-aie-klein-agents-www",
    ]
    assert answer.claims[0].talk_raw == " [klein-browserbase-agents-www] "
    assert all(c.flags == () for c in answer.claims)


def test_a_missing_claim_falls_back_to_its_item_label():
    no_claim = {"item": "Evals", "talk": "ia-aie-x", "quote": QUOTE}
    answer = normalise(
        {"items": [{"label": "Evals"}], "claims": [no_claim, claim(item="Evals", claim=" ")]}
    )

    assert [c.claim for c in answer.claims] == ["Evals", "Evals"]
    assert all(c.flags == ("claim_from_item",) for c in answer.claims)


def test_a_claim_without_text_or_item_is_flagged():
    answer = normalise({"items": [], "claims": [{"talk": "ia-aie-x", "quote": QUOTE}]})

    assert answer.claims[0].claim == ""
    assert answer.claims[0].flags == ("missing_claim",)


def test_claims_link_to_the_first_item_with_the_exact_label():
    answer = normalise(
        {
            "items": [
                {"label": "AWS (Amazon Web Services)"},
                {"label": "Evals"},
                {"label": "Evals"},
            ],
            "claims": [claim(item=" Evals "), claim(item="AWS"), claim(item="")],
        }
    )

    linked, unknown, none = answer.claims
    assert (linked.item, linked.item_position, linked.flags) == ("Evals", 2, ())
    assert (unknown.item, unknown.item_position, unknown.flags) == ("AWS", None, ("unknown_item",))
    assert (none.item, none.item_position, none.flags) == ("", None, ())


def test_quotes_outside_8_to_40_words_are_flagged_but_kept():
    words = lambda n: " ".join(["word"] * n)  # noqa: E731
    answer = normalise({"items": [], "claims": [claim(quote=words(n)) for n in (7, 8, 40, 41)]})

    assert [(c.quote_words, c.flags) for c in answer.claims] == [
        (7, ("short_quote",)),
        (8, ()),
        (40, ()),
        (41, ("long_quote",)),
    ]


def test_an_empty_quote_is_flagged():
    answer = normalise({"items": [], "claims": [claim(quote="  ")]})

    assert answer.claims[0].quote == ""
    assert answer.claims[0].flags == ("missing_quote",)


def test_repeated_claims_are_all_kept():
    answer = normalise({"items": [], "claims": [claim(), claim()]})

    assert [c.index for c in answer.claims] == [0, 1]
