"""Integrity checks of the corpus built from the real seed (../seed) and the source
transcripts (../transcripts, local to the maintainer's machine; skipped without them)."""

import json
import re
from collections import defaultdict
from pathlib import Path

import pytest

from bench.corpus import CHUNK_TALK_OVERRIDES, build_corpus

SEED = Path(__file__).resolve().parents[2] / "seed"
TRANSCRIPTS = Path(__file__).resolve().parents[2] / "transcripts"
pytestmark = pytest.mark.skipif(
    not TRANSCRIPTS.is_dir(), reason="needs the local transcripts/ directory"
)
HEADER = re.compile(
    r"# [^\n]+\n"
    r"- talk: (?P<talk>ia-aie-[a-z0-9-]+)\n"
    r"- video: https://\S+\n"
    r"- published: \d{4}-\d{2}-\d{2}\n"
    r"\n"
)


def build(out: Path) -> dict[str, str]:
    build_corpus(SEED, TRANSCRIPTS, out, CHUNK_TALK_OVERRIDES)
    return {p.stem: p.read_text(encoding="utf-8") for p in out.glob("*.md")}


@pytest.fixture(scope="module")
def corpus(tmp_path_factory):
    return build(tmp_path_factory.mktemp("corpus"))


@pytest.fixture(scope="module")
def seed_chunks():
    """talk -> [(chunk_index, text)], read straight from the seed rows."""
    rows, talk_of = {}, {}
    for part in sorted((SEED / "chunks").glob("part-*.jsonl")):
        for line in part.open(encoding="utf-8"):
            row = json.loads(line)
            if row.get("type") == "Chunk":
                rows[row["id"]] = row["data"]
            elif row.get("edge") == "PartOfArtifact":
                talk_of[row["from"]] = row["to"]
    talks = defaultdict(list)
    for chunk_id, data in rows.items():
        prefix = chunk_id.rsplit("#", 1)[0]
        talk = CHUNK_TALK_OVERRIDES.get(prefix, talk_of[chunk_id])
        text = data["text"].removeprefix(f"[{prefix}] ")
        talks[talk].append((data["chunk_index"], text, prefix))
    return talks


def body(doc: str) -> str:
    return doc[HEADER.match(doc).end() :]


def test_one_file_per_transcript(corpus):
    assert len(corpus) == 337


def words(text: str) -> str:
    """Whitespace-separated words without the captions' `>>` turn markers, one space apart."""
    return " " + " ".join(w for w in text.split() if w != ">>") + " "


def test_every_chunk_appears_verbatim_in_its_talk_in_index_order(corpus, seed_chunks):
    checked, misplaced = 0, []
    for talk, chunks in seed_chunks.items():
        doc, pos = (
            words(
                body(
                    corpus.get(
                        talk,
                        "# \n- talk: ia-aie-x\n- video: https://x\n- published: 2000-01-01\n\n",
                    )
                )
            ),
            0,
        )
        for index, text, _ in sorted(chunks):
            found = doc.find(words(text), pos)
            if found < 0:
                misplaced.append(f"{talk}#{index}")
                continue
            pos = found + len(words(text)) - 1
            checked += 1

    # Shaw & Marten's chunks predate a cleanup of rolling-caption repeats in its transcript
    # (7 words across its 16 chunks); the transcript is the cleaner text.
    assert {m.split("#")[0] for m in misplaced} <= {"ia-aie-shaw-marten-rollout"}
    assert checked == 5339 - len(misplaced)


def test_chunk_labels_are_stripped(corpus, seed_chunks):
    labelled = [
        talk
        for talk, chunks in seed_chunks.items()
        if any(f"[{prefix}]" in corpus[talk] for prefix in {p for _, _, p in chunks})
    ]

    assert labelled == []


def test_sonar_talks_are_split_by_speaker(corpus):
    chatterjee = body(corpus["ia-aie-chatterjee-guide-verify-solve"])
    shaukat = body(corpus["ia-aie-shaukat-verifiers-king"])

    assert chatterjee.startswith("All right.\n\nThank you.\nThat's very helpful.\nMy name is")
    assert shaukat.startswith("[music] Please join me in welcoming the chief executive officer")
    assert "My name is Anirban Chatterjee" not in shaukat


def test_no_turn_markers_are_left(corpus):
    assert [talk for talk, doc in corpus.items() if ">>" in doc] == []


def test_headers_carry_only_title_video_and_date(corpus):
    bad = [
        talk
        for talk, doc in corpus.items()
        if not (m := HEADER.match(doc)) or m["talk"] != talk or doc[m.end()].isspace()
    ]

    assert bad == []


def test_transcript_word_count_matches_the_measured_corpus(corpus):
    words = sum(len(body(doc).split()) for doc in corpus.values())

    assert abs(words - 1_192_360) / 1_192_360 < 0.01


def test_rebuild_is_byte_identical(corpus, tmp_path):
    assert build(tmp_path / "again") == corpus
