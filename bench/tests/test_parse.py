from bench.parse import answer_block

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
