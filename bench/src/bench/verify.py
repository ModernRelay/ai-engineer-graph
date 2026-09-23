"""The mechanical quote check (D1.2): is a claim's quote in the transcript of the talk it
cites? No LLM: normalised substring match, then rapidfuzz, then the same across every talk."""

import re
from dataclasses import dataclass
from pathlib import Path

from rapidfuzz import fuzz, process

FUZZY_MIN = 90  # rapidfuzz partial_ratio
SPLICE_PIECE_MIN = 4  # words; shorter pieces between ellipses carry no evidence
ELLIPSIS = re.compile(r"\.{3,}|…")
APOSTROPHES = re.compile(r"['’‘ʼ]")
NON_WORD = re.compile(r"[^\w\s]")


def normalise_text(text: str) -> str:
    """Lowercase, apostrophes dropped (isn't = isnt), other punctuation as spaces, one space."""
    return " ".join(NON_WORD.sub(" ", APOSTROPHES.sub("", text.lower())).split())


@dataclass(frozen=True)
class QuoteCheck:
    status: str  # exact | fuzzy | spliced | wrong_talk | not_found
    talk: str | None  # the cited talk's id; None when the citation resolves to no talk
    found_in: str | None = None  # wrong_talk: the talk the quote is actually in
    score: float = 0  # best partial_ratio in the cited talk (100 for exact)


class Corpus:
    def __init__(self, texts: dict[str, str], labels: dict[str, str]):
        # Padded with spaces so an exact match can be required to start and end on a word.
        self.texts = {talk: f" {normalise_text(text)} " for talk, text in texts.items()}
        self.labels = labels

    @classmethod
    def load(cls, talks_dir: Path, labels: dict[str, str]) -> "Corpus":
        """The corpus transcripts without their headers, so the title can't be quoted."""
        texts = {
            path.stem: path.read_text(encoding="utf-8").split("\n\n", 1)[1]
            for path in sorted(talks_dir.glob("*.md"))
        }
        return cls(texts, labels)

    def resolve(self, talk: str) -> str | None:
        """A talk id or a chunk label -> the talk id, or None."""
        talk = self.labels.get(talk, talk)
        return talk if talk in self.texts else None

    def check(self, talk: str, quote: str) -> QuoteCheck:
        cited = self.resolve(talk.strip())
        needle = normalise_text(quote)
        if not needle:
            return QuoteCheck("not_found", cited)
        score = 0.0
        if cited:
            text = self.texts[cited]
            if f" {needle} " in text:
                return QuoteCheck("exact", cited, score=100)
            score = round(fuzz.partial_ratio(needle, text), 1)
            if score >= FUZZY_MIN:
                return QuoteCheck("fuzzy", cited, score=score)
            spliced = _splice_score(quote, text)
            if spliced is not None:
                return QuoteCheck("spliced", cited, score=spliced)
        return QuoteCheck(*self._elsewhere(needle, cited), score=score)

    def _elsewhere(self, needle: str, cited: str | None) -> tuple[str, str | None, str | None]:
        others = {talk: text for talk, text in self.texts.items() if talk != cited}
        found = next((t for t in sorted(others) if f" {needle} " in others[t]), None)
        if found is None:
            best = process.extractOne(
                needle, others, scorer=fuzz.partial_ratio, score_cutoff=FUZZY_MIN
            )
            found = best[2] if best else None
        return ("wrong_talk" if found else "not_found"), cited, found


def _splice_score(quote: str, text: str) -> float | None:
    """The weakest piece's score when every 4+ word piece between ellipses is in the text."""
    if not ELLIPSIS.search(quote):
        return None
    pieces = [normalise_text(piece) for piece in ELLIPSIS.split(quote)]
    pieces = [piece for piece in pieces if len(piece.split()) >= SPLICE_PIECE_MIN]
    if not pieces:
        return None
    scores = [
        100 if f" {piece} " in text else round(fuzz.partial_ratio(piece, text), 1)
        for piece in pieces
    ]
    return min(scores) if min(scores) >= FUZZY_MIN else None
