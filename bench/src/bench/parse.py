"""The answer contract: the last fenced json block in an agent's reply, normalised into
fixed-shape items and claims (D1.1). Normalising fixes form only; the flags it sets are
contract deviations, and none of them changes a score by itself."""

import json
import re
from dataclasses import dataclass

JSON_BLOCK = re.compile(r"```json\s*\n(.*?)\n\s*```", re.DOTALL)
QUOTE_WORDS = (8, 40)  # the contract's quote length


@dataclass(frozen=True)
class Item:
    position: int  # 1-based list order; ranks may tie, positions don't
    label: str
    rank: int | None
    talk_count: int | None


@dataclass(frozen=True)
class Claim:
    index: int  # position in the agent's claims list: later steps refer to run + index
    item: str
    item_position: int | None
    claim: str
    talk: str  # an ia-aie-… id or a chunk label, brackets stripped
    talk_raw: str
    quote: str
    quote_words: int
    flags: tuple[str, ...] = ()


@dataclass(frozen=True)
class Answer:
    unparseable: bool
    items: tuple[Item, ...] = ()
    claims: tuple[Claim, ...] = ()
    flags: tuple[str, ...] = ()
    dropped_items: int = 0
    dropped_claims: int = 0


def answer_block(text: str) -> dict | None:
    blocks = JSON_BLOCK.findall(text or "")
    if not blocks:
        return None
    try:
        answer = json.loads(blocks[-1])
    except json.JSONDecodeError:
        return None
    return answer if isinstance(answer, dict) else None


def normalise(answer_json: dict | None) -> Answer:
    if answer_json is None:
        return Answer(unparseable=True)
    flags: list[str] = []
    raw_items = _entries(answer_json, "items", flags)
    raw_claims = _entries(answer_json, "claims", flags)
    items = tuple(
        Item(n, _text(row.get("label")), _int(row.get("rank")), _int(row.get("talk_count")))
        for n, row in enumerate((r for r in raw_items if isinstance(r, dict)), start=1)
    )
    positions: dict[str, int] = {}
    for item in items:
        positions.setdefault(item.label, item.position)
    claims = tuple(
        _claim(index, row, positions)
        for index, row in enumerate(raw_claims)
        if isinstance(row, dict)
    )
    return Answer(
        unparseable=False,
        items=items,
        claims=claims,
        flags=tuple(flags),
        dropped_items=len(raw_items) - len(items),
        dropped_claims=len(raw_claims) - len(claims),
    )


def _claim(index: int, row: dict, positions: dict[str, int]) -> Claim:
    flags = []
    item = _text(row.get("item"))
    item_position = positions.get(item) if item else None
    if item and item_position is None:
        flags.append("unknown_item")
    text = _text(row.get("claim"))
    if not text:
        text = item
        flags.append("claim_from_item" if item else "missing_claim")
    talk_raw = row.get("talk") if isinstance(row.get("talk"), str) else _text(row.get("talk"))
    talk = _text(talk_raw)
    if talk.startswith("[") and talk.endswith("]"):
        talk = talk[1:-1].strip()
    if not talk:
        flags.append("missing_talk")
    quote = _text(row.get("quote"))
    words = len(quote.split())
    if not quote:
        flags.append("missing_quote")
    elif words < QUOTE_WORDS[0]:
        flags.append("short_quote")
    elif words > QUOTE_WORDS[1]:
        flags.append("long_quote")
    return Claim(index, item, item_position, text, talk, talk_raw, quote, words, tuple(flags))


def _entries(answer: dict, key: str, flags: list[str]) -> list:
    value = answer.get(key)
    if isinstance(value, list):
        return value
    flags.append(f"bad_{key}")
    return []


def _text(value) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return str(value)
    return ""


def _int(value) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) else None
