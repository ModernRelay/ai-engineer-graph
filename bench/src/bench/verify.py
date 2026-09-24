"""The mechanical quote check (D1.2): is a claim's quote in the transcript of the talk it
cites? No LLM: normalised substring match, then rapidfuzz, then the same across every talk."""

import re
from dataclasses import dataclass
from pathlib import Path

from rapidfuzz import fuzz, process

from bench.corpus import PASSAGE_WORDS, passages

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
    def __init__(
        self,
        texts: dict[str, str],
        labels: dict[str, str],
        titles: dict[str, str] | None = None,
        passage_words: int = PASSAGE_WORDS,
    ):
        # Padded with spaces so an exact match can be required to start and end on a word.
        self.texts = {talk: f" {normalise_text(text)} " for talk, text in texts.items()}
        self.labels = labels
        self.titles = titles or {}  # the header's title line: title (speakers, company — event)
        # Chunk-sized passages, cut the way the seed's chunks were; the judge's context uses them.
        self.chunks = {talk: passages(text, passage_words) for talk, text in texts.items()}
        self._chunk_texts = {
            talk: [f" {normalise_text(chunk)} " for chunk in chunks]
            for talk, chunks in self.chunks.items()
        }

    @classmethod
    def load(cls, talks_dir: Path, labels: dict[str, str]) -> "Corpus":
        """The corpus transcripts without their headers, so the title can't be quoted; the
        title line is kept apart, as context for the judge."""
        texts, titles = {}, {}
        for path in sorted(talks_dir.glob("*.md")):
            header, texts[path.stem] = path.read_text(encoding="utf-8").split("\n\n", 1)
            titles[path.stem] = header.splitlines()[0].removeprefix("# ").strip()
        return cls(texts, labels, titles)

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

    def context(self, talk: str, quote: str, around: int = 1) -> str:
        """For each quoted piece, its best-matching chunk and `around` chunks either side, in
        talk order; runs that don't touch are separated by [...]. The support judge reads this."""
        cited = self.resolve(talk.strip())
        if cited is None:
            raise ValueError(f"no talk for {talk!r}")
        chunks, texts = self.chunks[cited], self._chunk_texts[cited]
        keep: set[int] = set()
        for piece in _splice_pieces(quote) or [normalise_text(quote)]:
            best = max(
                range(len(texts)),
                key=lambda i: (
                    101 if f" {piece} " in texts[i] else fuzz.partial_ratio(piece, texts[i])
                ),
            )
            keep.update(range(max(0, best - around), min(len(chunks), best + around + 1)))
        runs: list[list[int]] = []
        for i in sorted(keep):
            if runs and i == runs[-1][-1] + 1:
                runs[-1].append(i)
            else:
                runs.append([i])
        return "\n\n[…]\n\n".join("\n\n".join(chunks[i] for i in run) for run in runs)

    def _elsewhere(self, needle: str, cited: str | None) -> tuple[str, str | None, str | None]:
        others = {talk: text for talk, text in self.texts.items() if talk != cited}
        found = next((t for t in sorted(others) if f" {needle} " in others[t]), None)
        if found is None:
            best = process.extractOne(
                needle, others, scorer=fuzz.partial_ratio, score_cutoff=FUZZY_MIN
            )
            found = best[2] if best else None
        return ("wrong_talk" if found else "not_found"), cited, found


def _splice_pieces(quote: str) -> list[str]:
    """The normalised 4+ word pieces of a quote joined by ellipses; [] if it isn't a splice."""
    if not ELLIPSIS.search(quote):
        return []
    pieces = [normalise_text(piece) for piece in ELLIPSIS.split(quote)]
    return [piece for piece in pieces if len(piece.split()) >= SPLICE_PIECE_MIN]


def _splice_score(quote: str, text: str) -> float | None:
    """The weakest piece's score when every 4+ word piece between ellipses is in the text."""
    pieces = _splice_pieces(quote)
    if not pieces:
        return None
    scores = [
        100 if f" {piece} " in text else round(fuzz.partial_ratio(piece, text), 1)
        for piece in pieces
    ]
    return min(scores) if min(scores) >= FUZZY_MIN else None
