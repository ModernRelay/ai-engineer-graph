"""The question shortlist (questions.yaml)."""

import re
from dataclasses import dataclass
from pathlib import Path

import yaml

CATEGORIES = {"aggregate", "multi-hop", "lookup", "absence"}
SHAPES = {"ranked_list", "talk_set", "company_set", "prose", "absence"}
QUESTION_ID = re.compile(r"^Q\d{2}$")
# Words that only make sense to someone who has seen the graph: id slugs and "signal(s)".
GRAPH_VOCABULARY = re.compile(
    r"\b(?:pat|sig|el|ins|how|co|exp|ia|source)-[a-z0-9]|\bsignals?\b", re.IGNORECASE
)


@dataclass(frozen=True)
class Question:
    id: str
    category: str
    shape: str
    text: str


def load_questions(path: Path) -> list[Question]:
    rows = (yaml.safe_load(path.read_text(encoding="utf-8")) or {}).get("questions") or []
    questions, seen = [], set()
    for row in rows:
        q = Question(
            **{f: str(row.get(f) or "").strip() for f in ("id", "category", "shape", "text")}
        )
        if not QUESTION_ID.match(q.id):
            raise ValueError(f"{q.id or '?'}: id must look like Q01")
        if q.id in seen:
            raise ValueError(f"{q.id}: duplicate id")
        if q.category not in CATEGORIES:
            raise ValueError(f"{q.id}: unknown category {q.category!r}")
        if q.shape not in SHAPES:
            raise ValueError(f"{q.id}: unknown shape {q.shape!r}")
        if not q.text:
            raise ValueError(f"{q.id}: empty text")
        if m := GRAPH_VOCABULARY.search(q.text):
            raise ValueError(f"{q.id}: graph vocabulary {m.group(0)!r} in the question text")
        seen.add(q.id)
        questions.append(q)
    return questions
