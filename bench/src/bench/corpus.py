"""Rebuild the talk transcripts as markdown files from the seed's chunks.

Each talk's chunks are found through their PartOfArtifact edges and joined in
chunk_index order. The header carries only what someone browsing the talks
would see: title, video link and publish date. Nothing else from the graph.
"""

import json
from collections import defaultdict
from pathlib import Path

# The graph attaches Anirban Chatterjee's "Guide, Verify, Solve" chunks to Tariq
# Shaukat's talk (added by the 2026-09-08 audit backfill, commit 026ff7e).
# Drop this entry once the PartOfArtifact edges are fixed in the graph.
CHUNK_TALK_OVERRIDES = {
    "chatterjee-sonar-guide-verify-solve": "ia-aie-chatterjee-guide-verify-solve",
}


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
