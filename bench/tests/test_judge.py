import json
from types import SimpleNamespace

import pytest
from anthropic.types import Usage

from bench.judge import (
    CLUSTER_SCHEMA,
    PAIRWISE_SCHEMA,
    SUPPORT_SCHEMA,
    UNCITED_SCHEMA,
    JudgeError,
    Support,
    anthropic_ask,
    cluster_request,
    clusters,
    pairwise_request,
    support,
    support_request,
    uncited,
    uncited_request,
    valid_pairwise,
)
from bench.provider import JUDGE_MODEL

CLAIM = dict(
    title="Harness Over Model (Ann Lee, Acme — AI Engineer World's Fair)",
    claim="Evals gate every release.",
    item="Evals",
    quote="every eval now runs inside the release pipeline",
    context="Chunk one says every eval now runs inside the release pipeline.",
)
USAGE = {"input_tokens": 900, "output_tokens": 300}


class FakeJudge:
    """Stands in for the API: records each request and answers with a fixed verdict."""

    def __init__(self, output=None):
        self.output = output or {"verdict": "supported", "reason": "The quote says so."}
        self.requests = []

    def __call__(self, request):
        self.requests.append(request)
        return {"output": self.output, "usage": USAGE, "model": JUDGE_MODEL, "id": "gen-1"}


def test_the_request_asks_opus_for_a_schema_bound_verdict_at_high_effort():
    request = support_request(**CLAIM)

    assert request["model"] == JUDGE_MODEL
    assert request["output_config"] == {
        "effort": "high",
        "format": {"type": "json_schema", "schema": SUPPORT_SCHEMA},
    }
    assert SUPPORT_SCHEMA["properties"]["verdict"]["enum"] == [
        "supported",
        "partial",
        "unsupported",
    ]
    assert "thinking" not in request


def test_the_request_carries_the_title_claim_item_quote_and_transcript():
    content = support_request(**CLAIM)["messages"][0]["content"]

    for value in CLAIM.values():
        assert value in content
    assert content.startswith(f"<talk>{CLAIM['title']}</talk>")


def test_the_request_is_blind_to_the_arms():
    text = json.dumps(support_request(**CLAIM)).lower()

    for word in ("omnigraph", "markdown", "graph", " arm", "benchmark"):
        assert word not in text


def test_a_claim_without_a_list_entry_leaves_the_entry_out():
    content = support_request(**(CLAIM | {"item": ""}))["messages"][0]["content"]

    assert "list_entry" not in content


def test_support_returns_the_judges_verdict(tmp_path):
    judge = FakeJudge({"verdict": "partial", "reason": "The number isn't in the quote."})

    verdict = support(**CLAIM, ask=judge, cache_dir=tmp_path)

    assert verdict == Support("partial", "The number isn't in the quote.")


def test_a_judged_claim_is_read_from_the_cache_not_asked_again(tmp_path):
    judge = FakeJudge()

    first = support(**CLAIM, ask=judge, cache_dir=tmp_path)
    second = support(**CLAIM, ask=judge, cache_dir=tmp_path)

    assert first == second
    assert len(judge.requests) == 1
    [saved] = tmp_path.glob("*.json")
    record = json.loads(saved.read_text())
    assert record["request"] == judge.requests[0]
    assert record["usage"] == USAGE


def test_different_inputs_are_asked_again(tmp_path):
    judge = FakeJudge()

    support(**CLAIM, ask=judge, cache_dir=tmp_path)
    support(**(CLAIM | {"claim": "Evals gate most releases."}), ask=judge, cache_dir=tmp_path)

    assert len(judge.requests) == 2


def test_a_verdict_outside_the_schema_raises_and_is_not_cached(tmp_path):
    judge = FakeJudge({"verdict": "probably", "reason": "?"})

    with pytest.raises(JudgeError):
        support(**CLAIM, ask=judge, cache_dir=tmp_path)

    assert list(tmp_path.iterdir()) == []


# anthropic_ask: the one place the SDK's response is read, tested with a stub client.


class StubClient:
    def __init__(self, response):
        self.response = response
        self.calls = []
        self.messages = SimpleNamespace(create=self._create)

    def _create(self, **kwargs):
        self.calls.append(kwargs)
        return self.response


def response(stop_reason="end_turn", text='{"verdict": "supported", "reason": "ok"}'):
    return SimpleNamespace(
        stop_reason=stop_reason,
        content=[
            SimpleNamespace(type="thinking", thinking=""),
            SimpleNamespace(type="text", text=text),
        ],
        usage=Usage(input_tokens=900, output_tokens=300),
        model="anthropic/claude-opus-5.5",
        id="gen-1",
    )


def test_anthropic_ask_sends_the_request_and_reads_the_json_text():
    client = StubClient(response())
    request = support_request(**CLAIM)

    answer = anthropic_ask(client)(request)

    assert client.calls == [request]
    assert answer["output"] == {"verdict": "supported", "reason": "ok"}
    assert answer["usage"]["input_tokens"] == 900
    assert answer["id"] == "gen-1"


@pytest.mark.parametrize("stop_reason", ["refusal", "max_tokens"])
def test_anthropic_ask_raises_when_the_judge_did_not_finish(stop_reason):
    with pytest.raises(JudgeError, match=stop_reason):
        anthropic_ask(StubClient(response(stop_reason)))(support_request(**CLAIM))


def test_anthropic_ask_raises_when_there_is_no_json_text():
    no_text = response()
    no_text.content = [SimpleNamespace(type="thinking", thinking="")]

    with pytest.raises(JudgeError, match="no text"):
        anthropic_ask(StubClient(no_text))(support_request(**CLAIM))
    with pytest.raises(JudgeError, match="not JSON"):
        anthropic_ask(StubClient(response(text="Supported.")))(support_request(**CLAIM))


# uncited (D1.4): factual statements in the prose that no claim covers.

PROSE = "Lyft gates launches on offline evals. Etsy found the harness beats the model."
CLAIMS = [("Evals", "Lyft gates launches on offline evals."), ("", "Etsy says harness > model.")]


class FakeUncited(FakeJudge):
    def __init__(self, output=None):
        super().__init__(output or {"uncited": ["Etsy found the harness beats the model."]})


def test_the_uncited_request_carries_the_prose_and_every_claim():
    request = uncited_request(PROSE, CLAIMS)
    content = request["messages"][0]["content"]

    assert request["model"] == JUDGE_MODEL
    assert request["output_config"] == {
        "effort": "high",
        "format": {"type": "json_schema", "schema": UNCITED_SCHEMA},
    }
    assert f"<answer>\n{PROSE}\n</answer>" in content
    assert "- [Evals] Lyft gates launches on offline evals." in content
    assert "- Etsy says harness > model." in content


def test_an_answer_without_claims_says_so():
    content = uncited_request(PROSE, [])["messages"][0]["content"]

    assert "<claims>\n(none)\n</claims>" in content


def test_the_uncited_request_is_blind_to_the_arms():
    text = json.dumps(uncited_request(PROSE, CLAIMS)).lower()

    for word in ("omnigraph", "markdown", "graph", " arm", "benchmark"):
        assert word not in text


def test_uncited_returns_the_listed_statements_and_caches_them(tmp_path):
    judge = FakeUncited()

    first = uncited(PROSE, CLAIMS, ask=judge, cache_dir=tmp_path)
    second = uncited(PROSE, CLAIMS, ask=judge, cache_dir=tmp_path)

    assert first == second == ["Etsy found the harness beats the model."]
    assert len(judge.requests) == 1


def test_an_uncited_output_that_is_not_a_list_of_strings_raises(tmp_path):
    with pytest.raises(JudgeError):
        uncited(PROSE, CLAIMS, ask=FakeUncited({"uncited": [1, 2]}), cache_dir=tmp_path)

    assert list(tmp_path.iterdir()) == []


# clusters (D2.1): item labels from every run of a question, grouped into canonical items.

QUESTION = "Which five companies gave the most talks at the conference?"
LABELS = ["Anthropic", "AWS", "Amazon Web Services", "AWS"]


class FakeClusters(FakeJudge):
    def __init__(self, groups):
        super().__init__({"groups": groups})


def test_the_cluster_request_numbers_the_distinct_labels_alphabetically():
    request = cluster_request(QUESTION, LABELS)
    content = request["messages"][0]["content"]

    assert request["output_config"]["format"]["schema"] == CLUSTER_SCHEMA
    assert f"<question>{QUESTION}</question>" in content
    assert "<labels>\n1. AWS\n2. Amazon Web Services\n3. Anthropic\n</labels>" in content


def test_the_cluster_request_is_blind_to_the_arms():
    text = json.dumps(cluster_request(QUESTION, LABELS)).lower()

    for word in ("omnigraph", "markdown", "graph", " arm", "benchmark"):
        assert word not in text


def test_clusters_map_every_label_to_its_group(tmp_path):
    judge = FakeClusters(
        [{"name": "Amazon", "members": [1, 2]}, {"name": "Anthropic", "members": [3]}]
    )

    groups = clusters(QUESTION, LABELS, ask=judge, cache_dir=tmp_path)

    assert groups == {"AWS": "Amazon", "Amazon Web Services": "Amazon", "Anthropic": "Anthropic"}


@pytest.mark.parametrize(
    "groups",
    [
        [{"name": "Amazon", "members": [1, 2]}],  # label 3 left out
        [{"name": "Amazon", "members": [1, 2]}, {"name": "All", "members": [2, 3]}],  # 2 twice
        [{"name": "Amazon", "members": [1, 2, 3, 4]}],  # no label 4
    ],
)
def test_clusters_that_miss_or_repeat_a_label_raise_and_are_not_cached(groups, tmp_path):
    with pytest.raises(JudgeError):
        clusters(QUESTION, LABELS, ask=FakeClusters(groups), cache_dir=tmp_path)

    assert list(tmp_path.iterdir()) == []


def test_clusters_keep_two_groups_with_the_same_name_apart(tmp_path):
    judge = FakeClusters([{"name": "Cloud", "members": [1]}, {"name": "Cloud", "members": [2, 3]}])

    groups = clusters(QUESTION, LABELS, ask=judge, cache_dir=tmp_path)

    assert groups["AWS"] != groups["Anthropic"]


# pairwise (D2.2): two answers to one question, A and B.


def test_the_pairwise_request_shows_the_question_and_both_answers():
    request = pairwise_request("Which talks argue X?", "Answer one.", "Answer two.")
    content = request["messages"][0]["content"]

    assert request["output_config"]["format"]["schema"] == PAIRWISE_SCHEMA
    assert content == (
        "<question>Which talks argue X?</question>\n\n"
        "<answer_a>\nAnswer one.\n</answer_a>\n\n<answer_b>\nAnswer two.\n</answer_b>"
    )


def test_the_pairwise_prompt_is_blind_to_the_arms():
    text = json.dumps(pairwise_request("Q?", "a", "b")).lower()

    for word in ("omnigraph", "markdown", "graph", " arm", "benchmark"):
        assert word not in text


@pytest.mark.parametrize(
    "output, ok",
    [
        (
            {
                "coverage": "A",
                "specificity": "tie",
                "correctness": "B",
                "winner": "A",
                "reason": "r",
            },
            True,
        ),
        (
            {
                "coverage": "A",
                "specificity": "tie",
                "correctness": "B",
                "winner": "C",
                "reason": "r",
            },
            False,
        ),
        ({"coverage": "A", "specificity": "tie", "winner": "A", "reason": "r"}, False),
    ],
)
def test_a_pairwise_verdict_needs_every_rating(output, ok):
    assert valid_pairwise(output) is ok
