import pytest

from bench.verify import Corpus

ALPHA = (
    "So the thing we learned is that it's the harness, not the model, that decides what ships.\n"
    "\n"
    "Every eval now runs in the pipeline before a single change reaches a customer, and we "
    "measure the whole loop end to end rather than the model on its own."
)
BETA = "Voice agents have to handle interruptions gracefully or users hang up within seconds."
LONG = (
    "we measure the whole loop end to end rather than the model on its own and every eval now "
    "runs in the pipeline before a single change reaches a customer"
)


@pytest.fixture
def corpus():
    return Corpus(
        texts={"ia-aie-alpha-talk": ALPHA, "ia-aie-beta-talk": BETA + " " + LONG},
        labels={"alpha-talk": "ia-aie-alpha-talk", "beta-talk": "ia-aie-beta-talk"},
    )


def test_a_verbatim_quote_is_exact_despite_case_punctuation_and_apostrophes(corpus):
    check = corpus.check("ia-aie-alpha-talk", "Its the Harness — not the model — that decides")

    assert (check.status, check.talk, check.score) == ("exact", "ia-aie-alpha-talk", 100)


def test_a_quote_may_run_across_a_chunk_boundary(corpus):
    check = corpus.check("ia-aie-alpha-talk", "that decides what ships. Every eval now runs")

    assert check.status == "exact"


def test_a_chunk_label_resolves_to_its_talk(corpus):
    check = corpus.check("alpha-talk", "the harness, not the model, that decides what ships")

    assert (check.status, check.talk) == ("exact", "ia-aie-alpha-talk")


def test_a_lightly_garbled_quote_is_fuzzy(corpus):
    garbled = "Every eval now runs in the pipline before a single change reaches a customer and we"

    check = corpus.check("ia-aie-alpha-talk", garbled)

    assert check.status == "fuzzy"
    assert 90 <= check.score < 100


def test_real_passages_joined_by_an_ellipsis_are_spliced(corpus):
    quote = "it's the harness, not the model... every eval now runs in the pipeline"

    check = corpus.check("ia-aie-alpha-talk", quote)

    assert (check.status, check.score) == ("spliced", 100)


def test_a_unicode_ellipsis_splices_too(corpus):
    quote = "the harness, not the model … before a single change reaches a customer"

    assert corpus.check("ia-aie-alpha-talk", quote).status == "spliced"


def test_a_spliced_quote_scores_its_weakest_piece(corpus):
    quote = "it's the harness, not the model... every eval now runs in the pipline before a single"

    check = corpus.check("ia-aie-alpha-talk", quote)

    assert check.status == "spliced"
    assert 90 <= check.score < 100


def test_a_splice_with_an_invented_piece_is_not_found(corpus):
    quote = "it's the harness, not the model... customers love our pricing page a lot"

    assert corpus.check("ia-aie-alpha-talk", quote).status == "not_found"


def test_a_splice_of_only_short_pieces_is_not_found(corpus):
    assert (
        corpus.check("ia-aie-alpha-talk", "So the thing ... decides what ships").status
        == "not_found"
    )


def test_part_of_a_word_is_not_an_exact_match(corpus):
    check = corpus.check("ia-aie-alpha-talk", "arness, not the model, that decides what ships")

    assert check.status != "exact"


def test_an_invented_quote_is_not_found(corpus):
    check = corpus.check("ia-aie-alpha-talk", "we never run evals because customers test for us")

    assert check.status == "not_found"
    assert check.found_in is None


def test_a_quote_from_another_talk_is_wrong_talk(corpus):
    check = corpus.check(
        "ia-aie-alpha-talk", "voice agents have to handle interruptions gracefully"
    )

    assert (check.status, check.talk, check.found_in) == (
        "wrong_talk",
        "ia-aie-alpha-talk",
        "ia-aie-beta-talk",
    )


def test_a_garbled_quote_from_another_talk_is_wrong_talk(corpus):
    check = corpus.check(
        "ia-aie-alpha-talk", "Voice agents have to handel interruptions gracefully or users"
    )

    assert (check.status, check.found_in) == ("wrong_talk", "ia-aie-beta-talk")


def test_the_cited_talk_wins_when_the_quote_is_in_several(corpus):
    check = corpus.check(
        "ia-aie-beta-talk", "every eval now runs in the pipeline before a single change"
    )

    assert (check.status, check.talk) == ("exact", "ia-aie-beta-talk")


def test_an_unknown_talk_with_a_real_quote_is_wrong_talk(corpus):
    check = corpus.check("ia-aie-made-up", "voice agents have to handle interruptions gracefully")

    assert (check.status, check.talk, check.found_in, check.score) == (
        "wrong_talk",
        None,
        "ia-aie-beta-talk",
        0,
    )


def test_an_unknown_talk_with_an_invented_quote_is_not_found(corpus):
    check = corpus.check("", "we never run evals because customers test for us")

    assert (check.status, check.talk) == ("not_found", None)


def test_an_empty_quote_is_not_found(corpus):
    assert corpus.check("ia-aie-alpha-talk", "  ").status == "not_found"


def test_load_reads_only_the_transcript_not_the_header(tmp_path):
    talks = tmp_path / "talks"
    talks.mkdir()
    (talks / "ia-aie-alpha-talk.md").write_text(
        "# Harness Over Model (Ann Lee, Acme — AI Engineer World's Fair)\n"
        "- talk: ia-aie-alpha-talk\n"
        "- video: https://youtu.be/AAA\n"
        "- published: 2026-08-22\n"
        "\n" + ALPHA + "\n"
    )

    corpus = Corpus.load(talks, labels={})

    assert (
        corpus.check("ia-aie-alpha-talk", "Harness Over Model (Ann Lee, Acme").status == "not_found"
    )
    assert corpus.check("ia-aie-alpha-talk", "it's the harness, not the model").status == "exact"


# Corpus.context (D1.3): the transcript the support judge sees around a quote.

CHUNKS = [
    "Chunk zero opens the talk with a joke about the sleepy crowd.",
    "Chunk one says every eval now runs inside the release pipeline.",
    "Chunk two explains why the harness matters more than the model.",
    "Chunk three covers voice agents that must handle interruptions well.",
    "Chunk four closes with a call to hire more platform engineers.",
]


@pytest.fixture
def chunked():
    return Corpus(texts={"ia-aie-t": "\n\n".join(CHUNKS)}, labels={"t-label": "ia-aie-t"})


def test_context_is_the_matching_chunk_and_one_either_side(chunked):
    context = chunked.context("ia-aie-t", "why the harness matters more than the model")

    assert context == "\n\n".join(CHUNKS[1:4])


def test_context_finds_a_garbled_quote_through_a_chunk_label(chunked):
    context = chunked.context("t-label", "voice agents that must handel interruptions well")

    assert context == "\n\n".join(CHUNKS[2:5])


def test_context_stops_at_the_start_of_the_talk(chunked):
    context = chunked.context("ia-aie-t", "opens the talk with a joke about the sleepy crowd")

    assert context == "\n\n".join(CHUNKS[0:2])


def test_context_covers_each_piece_of_a_splice_with_a_gap_marker(chunked):
    quote = "opens the talk with a joke ... a call to hire more platform engineers"

    context = chunked.context("ia-aie-t", quote)

    assert context == "\n\n".join(CHUNKS[0:2]) + "\n\n[…]\n\n" + "\n\n".join(CHUNKS[3:5])


def test_context_merges_windows_that_touch(chunked):
    quote = "every eval now runs inside the release pipeline ... voice agents that must handle"

    assert chunked.context("ia-aie-t", quote) == "\n\n".join(CHUNKS)
