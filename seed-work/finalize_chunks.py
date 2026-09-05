#!/usr/bin/env python3
"""Finalize embedded chunk JSONL for loading: add keyed slug/id/createdAt and
PartOfArtifact edges.

The corpus convention is that each chunk's text is prefixed "[<talk-slug>] …"
and its key is "<talk-slug>#<chunk_index>". PartOfArtifact points the chunk at
its talk's InformationArtifact, whose slug is read from the FIRST `ia-...` token
in the matching extraction file (extraction/<talk-slug>.md).

Usage:
    python3 seed-work/finalize_chunks.py <embedded.jsonl> <final.jsonl> <YYYY-MM-DD>

Pipeline for a new batch:
    1. python3 seed-work/chunk_talks.py            # transcripts -> chunksNN-raw.jsonl
       (edit the stems list + output path in that file first)
    2. omnigraph embed --input chunksNN-raw.jsonl --output chunksNN-embedded.jsonl \
         --spec seed-work/embed-spec.json
    3. python3 seed-work/finalize_chunks.py chunksNN-embedded.jsonl chunksNN-final.jsonl <date>
    4. omnigraph load --data chunksNN-final.jsonl --mode merge ...
       (load AFTER the entity `--mode overwrite`, never before — overwrite is
       per-table and would not touch chunks, but re-loading chunks trips
       @unique on PartOfArtifact.src since edges have no @key)
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PREFIX = re.compile(r"^\[([a-z0-9-]+)\]")
IA = re.compile(r"`(ia-[a-z0-9-]+)`")


def ia_for(talk):
    md = ROOT / "extraction" / f"{talk}.md"
    m = IA.search(md.read_text(errors="replace"))
    if not m:
        raise SystemExit(f"no ia- slug found in {md}")
    return m.group(1)


def main(inp, out, date):
    ts = f"{date}T00:00:00Z"
    ia_cache = {}
    # verify each target artifact exists in the built seed before emitting edges
    have = set()
    seed = ROOT / "seed-work" / "seed-full.jsonl"
    if seed.exists():
        for l in open(seed):
            if '"InformationArtifact"' in l:
                have.add(json.loads(l)["data"]["slug"])
    n = e = 0
    with open(out, "w") as fh:
        for l in open(inp):
            l = l.strip()
            if not l:
                continue
            o = json.loads(l)
            d = o["data"]
            talk = PREFIX.match(d["text"]).group(1)
            ia = ia_cache.setdefault(talk, ia_for(talk))
            if have and ia not in have:
                raise SystemExit(f"artifact {ia} (talk {talk}) not in seed-full.jsonl — "
                                 f"load entities before finalizing chunks")
            slug = f"{talk}#{d['chunk_index']}"
            d["slug"], d["id"], d["createdAt"] = slug, slug, ts
            fh.write(json.dumps({"type": "Chunk", "data": d}, ensure_ascii=False) + "\n"); n += 1
            fh.write(json.dumps({"edge": "PartOfArtifact", "from": slug, "to": ia, "data": {}}) + "\n"); e += 1
    print(f"{out}: {n} chunks, {e} PartOfArtifact edges across {len(ia_cache)} talks")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
