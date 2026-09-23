"""The question shortlist (questions.yaml)."""

import re
from dataclasses import dataclass, replace
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
    # Corpus terms for the answerability check (B1.2); never shown to the agents.
    check_terms: tuple[str, ...] = ()
    # How many entries a fixed-length list asks for (D2.1, #39); scorer-only, like check_terms.
    count: int | None = None


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
        terms = row.get("check_terms")
        if terms is not None:
            if not (
                isinstance(terms, list) and terms and all(isinstance(t, str) and t for t in terms)
            ):
                raise ValueError(f"{q.id}: check_terms must be a non-empty list of strings")
            q = replace(q, check_terms=tuple(terms))
        count = row.get("count")
        if count is not None:
            if not (isinstance(count, int) and not isinstance(count, bool) and count > 0):
                raise ValueError(f"{q.id}: count must be a positive integer")
            q = replace(q, count=count)
        seen.add(q.id)
        questions.append(q)
    return questions


def check_questions(questions: list[Question], talks_dir: Path) -> list[dict]:
    """Answerability from the markdown corpus alone: how many talks mention each check term.

    A question passes when every term hits at least one talk, or, for an absence
    question, when no term hits any talk.
    """
    texts = [p.read_text(encoding="utf-8").lower() for p in sorted(talks_dir.glob("*.md"))]
    results = []
    for q in questions:
        hits = {t: sum(t.lower() in text for text in texts) for t in q.check_terms}
        if not hits:
            ok, detail = False, "no check_terms"
        elif q.shape == "absence":
            ok, detail = not any(hits.values()), "expects no talk to match"
        else:
            ok, detail = all(hits.values()), "expects every term in at least one talk"
        results.append({"id": q.id, "shape": q.shape, "ok": ok, "hits": hits, "detail": detail})
    return results
