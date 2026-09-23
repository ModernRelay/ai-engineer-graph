import json
from types import SimpleNamespace

import pytest
from anthropic.types import Usage

from bench.judge import (
    SUPPORT_SCHEMA,
    JudgeError,
    Support,
    anthropic_ask,
    support,
    support_request,
)
from bench.provider import JUDGE_MODEL

CLAIM = dict(
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


def test_the_request_carries_the_claim_item_quote_and_transcript():
    content = support_request(**CLAIM)["messages"][0]["content"]

    for value in CLAIM.values():
        assert value in content


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
