"""Rebuild the talk transcripts as markdown files from the seed's chunks.

Each talk's chunks are found through their PartOfArtifact edges and joined in
chunk_index order. The header carries only what someone browsing the talks
would see: title, video link and publish date. Nothing else from the graph.
"""

import json
from collections import defaultdict
from pathlib import Path

# Transcript label -> talk, for chunks the seed attaches to the wrong talk. Applied to the
# corpus build and (via `bench relink-chunks`) to the local graph's chunk edges. Empty now:
# the one known case, Chatterjee's "Guide, Verify, Solve" chunks attached to Shaukat's talk
# by the 2026-09-08 audit backfill, was fixed in seed/chunks/part-03.jsonl on 2026-09-23.
CHUNK_TALK_OVERRIDES: dict[str, str] = {}


def _read_jsonl(path: Path):
    with path.open(encoding="utf-8") as f:
        for line in f:
            yield json.loads(line)


def build_corpus(seed_dir: Path, out_dir: Path, overrides: dict[str, str]) -> int:
    artifacts = {r["id"]: r["data"] for r in _read_jsonl(seed_dir / "04-artifacts.jsonl")}

    chunks = {}  # chunk id -> Chunk data
    talk_of = {}  # chunk id -> artifact id, from PartOfArtifact
    for part in sorted((seed_dir / "chunks").glob("part-*.jsonl")):
        for row in _read_jsonl(part):
            if row.get("type") == "Chunk":
                chunks[row["id"]] = row["data"]
            elif row.get("edge") == "PartOfArtifact":
                talk_of[row["from"]] = row["to"]

    talks = defaultdict(list)  # artifact id -> [(prefix, chunk_index, text)]
    for chunk_id, data in chunks.items():
        prefix = chunk_id.rsplit("#", 1)[0]
        talk = overrides.get(prefix, talk_of[chunk_id])
        text = data["text"].removeprefix(f"[{prefix}] ")
        talks[talk].append((prefix, data["chunk_index"], text))

    for talk, rows in talks.items():
        prefixes = sorted({prefix for prefix, _, _ in rows})
        if len(prefixes) > 1:
            raise ValueError(
                f"{talk} has chunks from more than one transcript: {', '.join(prefixes)}"
            )

    out_dir.mkdir(parents=True, exist_ok=True)
    for stale in out_dir.glob("*.md"):
        stale.unlink()
    for talk, rows in talks.items():
        meta = artifacts[talk]
        header = (
            f"# {meta['name']}\n"
            f"- talk: {talk}\n"
            f"- video: {meta['link']}\n"
            f"- published: {meta['stagingTimestamp'][:10]}\n"
        )
        body = "\n\n".join(text for _, _, text in sorted(rows, key=lambda r: r[1]))
        (out_dir / f"{talk}.md").write_text(header + "\n" + body + "\n", encoding="utf-8")
    return len(talks)


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
