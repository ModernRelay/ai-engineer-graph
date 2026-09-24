"""Blinding for the pairwise judge (D2.2, #40): one fixed, phrase-level redaction applied to
both arms' text, so neither names its tools or sources. Ordinary words stay ("Signal" the
Arize product, "co-founder", "a graph of"); only self-references and tool vocabulary go."""

import re
from functools import cache

import yaml

from bench.prompts import ALIAS_PACK, QUERIES_DIR, QUERY

_METHODS = (
    "element signal chunk hybrid vector semantic transcript text keyword full-text bm25 pattern"
)
_METHOD = "(?:" + "|".join(_METHODS.split()) + ")"  # a search method word

# (pattern, replacement), applied in order, case-insensitively; a capitalised match keeps a
# capital. Specific phrases come before the words they contain.
RULES = [
    (r"\b(?:this|the|our) (?:knowledge )?graph's", "the sources'"),
    (r"\b(?:this|the|our) (?:knowledge )?graph\b", "the sources"),
    (r"\bomnigraph\b", "the sources"),
    (rf"\b{_METHOD}(?:/{_METHOD})*(?: {_METHOD})? (search(?:es)?)\b", r"\1"),
    (r"\bcontradicting signals?\b", "counter-evidence"),
    (r"\b(?:supporting-)?signal (count)(s?)\b", r"evidence \1\2"),
    (r"\b(\d+)-signal pattern\b", r"\1-item theme"),
    (r"\b(hundreds|dozens|a handful) of signals\b", r"\1 of evidence items"),
    (r"\bsignal mentions\b", "mentions"),
    (r"\bsignals? \(dated observations\)", "evidence (dated observations)"),
    (r"\"signal\" evidence", "evidence"),
    (
        r"\b(?:signals|elements|knowhow entries)(?:, (?:signals|elements|knowhow entries))*,?"
        r" (?:or|and) (?:signals|elements|knowhow entries)\b",
        "records",
    ),
    (r"\b(?:the )?pattern layer\b", "the themes"),
    (r"\btracked patterns\b", "tracked themes"),
    (r"\bpatterns view\b", "themes view"),
    (r"\bextraction pipeline\b", "sources"),
    (r"\bleaderboard\b", "ranking"),
    (r"\bsupporting signals?\b", "supporting evidence"),
    (r"\bcounter-signals?\b", "counter-evidence"),
    (r"\bsignal volume\b", "evidence volume"),
    (r"\bthe signals\b", "the evidence"),
    (r"\b(\d+) signals\b", r"\1 pieces of evidence"),
    (r"\b(?:talk|transcript) files?\b", "transcripts"),
    (r"(?<=[\w-])\.md\b", ""),
    (r"\bgrep(?:ped|ping|s)?\b", "search"),
]
COMPILED = [(re.compile(pattern, re.I), replacement) for pattern, replacement in RULES]
BACKTICKED = re.compile(r"`([^`\n]+)`")


@cache
def tool_names() -> frozenset[str]:
    """Every stored query and alias name the Omnigraph arm could cite."""
    names = set(yaml.safe_load(ALIAS_PACK.read_text()).get("aliases") or {})
    for gq in QUERIES_DIR.glob("*.gq"):
        names |= {m.group(1) for m in QUERY.finditer(gq.read_text(encoding="utf-8"))}
    return frozenset(names)


def _keep_case(replacement: str):
    """A match that opens a sentence (or a line, after markdown marks) keeps its capital."""

    def sub(match: re.Match) -> str:
        text = match.expand(replacement)
        before = match.string[: match.start()].rstrip(" *_#>-\"'(")
        opens = not before or before[-1] in ".!?:\n"
        return text[:1].upper() + text[1:] if opens and match.group(0)[:1].isupper() else text

    return sub


def _backticked(match: re.Match) -> str:
    first = match.group(1).split()[0]
    return "a lookup" if first == "omnigraph" or first in tool_names() else match.group(0)


def redact(text: str, labels: dict[str, str]) -> str:
    """labels: chunk label -> talk id; a bare label becomes the talk id, as the other arm cites."""
    text = BACKTICKED.sub(_backticked, text)
    for pattern, replacement in COMPILED:
        text = pattern.sub(_keep_case(replacement), text)
    if labels:
        names = "|".join(re.escape(label) for label in sorted(labels, key=len, reverse=True))
        text = re.sub(rf"(?<![\w-])(?:{names})(?![\w-])", lambda m: labels[m.group(0)], text)
    return text
