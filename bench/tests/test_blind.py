"""blind.redact (D2.2, #40): the same phrase-level redaction for both arms' text."""

import pytest

from bench.blind import redact

LABELS = {"klein-browserbase-agents-www": "ia-aie-klein-agents-www"}


@pytest.mark.parametrize(
    "text, expected",
    [
        ("I searched this knowledge graph for FPGAs.", "I searched the sources for FPGAs."),
        ("The graph's single most cited thesis.", "The sources' single most cited thesis."),
        ("the graph doesn't expose a count", "the sources doesn't expose a count"),
        ("Omnigraph returned nothing.", "The sources returned nothing."),
        ("Found it. **Omnigraph** had it.", "Found it. **The sources** had it."),
        ("run `omnigraph alias talk-chunks ia-aie-x` to see it", "run a lookup to see it"),
        (
            "via element search, signal search, and hybrid searches",
            "via search, search, and searches",
        ),
        ("and semantic/hybrid chunk search", "and search"),
        ("ranked by supporting signals", "ranked by supporting evidence"),
        ("(22 counter-signals)", "(22 counter-evidence)"),
        ("extrapolated from signal volume", "extrapolated from evidence volume"),
        ("sampled the signals behind each one", "sampled the evidence behind each one"),
        ("backed by 14 signals", "backed by 14 pieces of evidence"),
        ("(via `signal-evidence`, which returns quotes)", "(via a lookup, which returns quotes)"),
        ("across all 337 talk files", "across all 337 transcripts"),
        ("the transcript files mention it", "the transcripts mention it"),
        ("see ia-aie-klein-agents-www.md for more", "see ia-aie-klein-agents-www for more"),
        ("a grep for FPGA found nothing", "a search for FPGA found nothing"),
        ("as klein-browserbase-agents-www says", "as ia-aie-klein-agents-www says"),
        ("(22 contradicting signals)", "(22 counter-evidence)"),
        ("by their supporting-signal count", "by their evidence count"),
        ("the sources' own signal counts", "the sources' own evidence counts"),
        ("a 375-signal pattern", "a 375-item theme"),
        ("hundreds of signals against the talks", "hundreds of evidence items against the talks"),
        ("not just signal mentions", "not just mentions"),
        ("built from Signals (dated observations)", "built from evidence (dated observations)"),
        ('each backed by dated "Signal" evidence', "each backed by dated evidence"),
        ("No signals, elements, or knowhow entries mention it", "No records mention it"),
        ("across elements and signals returned nothing", "across records returned nothing"),
        ("I used the Pattern layer", "I used the themes"),
        ("I ranked the 18 tracked patterns", "I ranked the 18 tracked themes"),
        ("the patterns view", "the themes view"),
        ("the extraction pipeline builds", "the sources builds"),
        ("(via the leaderboard)", "(via the ranking)"),
    ],
)
def test_tool_and_source_mentions_are_neutralised(text, expected):
    assert redact(text, LABELS) == expected


@pytest.mark.parametrize(
    "text",
    [
        "(`ia-aie-hall-signal-layer`) argues that taste resists training",
        "Arize's new Signal product turns traces into PRs",
        "turning production signals into fixes",
        "many small pockets collectively signal bloat",
        "the co-founder of Browserbase",
        "a graph of latency over time",
        "each user query goes to the agent",
        "see ia-aie-klein-browserbase-agents-www-extra",  # not the label on its own
        "the small, high-signal subset of PRs",
        "downstream customer signals (rollbacks, tickets)",
        "enough people to read the signal and act on it",
        "Other signals point to skills forming a supply chain",
        "a design pattern for agents",
    ],
)
def test_ordinary_words_and_talk_ids_survive(text):
    assert redact(text, LABELS) == text
