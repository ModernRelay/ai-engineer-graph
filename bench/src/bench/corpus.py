"""Build the talk transcripts as markdown files from the source transcripts.

Each talk's text comes from `transcripts/<label>.txt`, the cleaned captions the seed's
chunks were cut from; the label is the transcript prefix of the talk's chunk ids, and the
talk is where the chunks' PartOfArtifact edges point. The header carries only what
someone browsing the talks would see: title, video link and publish date. Nothing else
from the graph.

The body keeps the transcript's words in order and only changes the layout: one
paragraph per speaker turn (the captions' `>>` marker, dropped) and one sentence per
line, so a phrase is never split across lines by the captions' fixed-width wrapping.
"""

import json
import re
from collections import defaultdict
from pathlib import Path

# Transcript label -> talk, for chunks the seed attaches to the wrong talk. Applied to the
# corpus build and (via `bench relink-chunks`) to the local graph's chunk edges. Empty now:
# the one known case, Chatterjee's "Guide, Verify, Solve" chunks attached to Shaukat's talk
# by the 2026-09-08 audit backfill, was fixed in seed/chunks/part-03.jsonl on 2026-09-23.
CHUNK_TALK_OVERRIDES: dict[str, str] = {}

TURN = re.compile(r"\s*>>\s*")
SENTENCE_END = re.compile(r"(?<=[.!?])\s+")
PASSAGE_WORDS = 220  # the seed's chunk size (seed-work/chunk_talks.py)


def _read_jsonl(path: Path):
    with path.open(encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


def transcript_body(raw: str) -> str:
    """A caption transcript as markdown: a paragraph per speaker turn, a sentence per line."""
    turns = [" ".join(turn.split()) for turn in TURN.split(raw)]
    return "\n\n".join("\n".join(SENTENCE_END.split(turn)) for turn in turns if turn)


def passages(text: str, words: int = PASSAGE_WORDS) -> list[str]:
    """A transcript packed into ~`words`-word passages on sentence boundaries, the way the
    seed's chunks were cut, so the support judge sees chunk-sized context."""
    out, buf, n = [], [], 0
    for sentence in SENTENCE_END.split(" ".join(text.split())):
        w = len(sentence.split())
        if n + w > words and buf:
            out.append(" ".join(buf))
            buf, n = [], 0
        buf.append(sentence)
        n += w
    if buf:
        out.append(" ".join(buf))
    return out


def build_corpus(
    seed_dir: Path, transcripts_dir: Path, out_dir: Path, overrides: dict[str, str]
) -> int:
    artifacts = {r["id"]: r["data"] for r in _read_jsonl(seed_dir / "04-artifacts.jsonl")}

    labels_of = defaultdict(set)  # talk -> transcript labels
    for label, talk in talk_labels(seed_dir, overrides).items():
        labels_of[talk].add(label)
    for talk, labels in labels_of.items():
        if len(labels) > 1:
            raise ValueError(
                f"{talk} has chunks from more than one transcript: {', '.join(sorted(labels))}"
            )
    missing = sorted(
        label
        for labels in labels_of.values()
        for label in labels
        if not (transcripts_dir / f"{label}.txt").is_file()
    )
    if missing:
        raise FileNotFoundError(f"no transcript in {transcripts_dir} for: {', '.join(missing)}")

    out_dir.mkdir(parents=True, exist_ok=True)
    for stale in out_dir.glob("*.md"):
        stale.unlink()
    for talk, (label,) in labels_of.items():
        meta = artifacts[talk]
        header = (
            f"# {meta['name']}\n"
            f"- talk: {talk}\n"
            f"- video: {meta['link']}\n"
            f"- published: {meta['stagingTimestamp'][:10]}\n"
        )
        body = transcript_body((transcripts_dir / f"{label}.txt").read_text(encoding="utf-8"))
        (out_dir / f"{talk}.md").write_text(header + "\n" + body + "\n", encoding="utf-8")
    return len(labels_of)


def talk_labels(seed_dir: Path, overrides: dict[str, str]) -> dict[str, str]:
    """Transcript label -> talk, from the chunks' PartOfArtifact edges plus the overrides.

    Chunk text starts with its transcript's [label], which is how the Omnigraph arm cites a
    talk; the corpus files drop the label, so the quote check resolves it through this map.
    """
    labels = {}
    for part in sorted((seed_dir / "chunks").glob("part-*.jsonl")):
        for row in _read_jsonl(part):
            if row.get("edge") == "PartOfArtifact":
                prefix = row["from"].rsplit("#", 1)[0]
                labels[prefix] = overrides.get(prefix, row["to"])
    return labels


def relink_chunk_edges(part: Path, overrides: dict[str, str]) -> int:
    """Re-point PartOfArtifact edges of overridden transcripts in one chunk part file.

    Used on the local graph's embedded parts (never on the tracked seed), so the
    graph agrees with the corpus. Only changed lines are rewritten; everything else
    (chunk rows with their embeddings) stays byte-for-byte. Returns edges moved.
    """
    lines = part.read_text(encoding="utf-8").splitlines()
    changed = 0
    for i, line in enumerate(lines):
        if not line.startswith('{"edge"'):
            continue
        row = json.loads(line)
        target = overrides.get(row["from"].rsplit("#", 1)[0])
        if row.get("edge") == "PartOfArtifact" and target and row["to"] != target:
            row["to"] = target
            lines[i] = json.dumps(row)
            changed += 1
    if changed:
        part.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return changed
