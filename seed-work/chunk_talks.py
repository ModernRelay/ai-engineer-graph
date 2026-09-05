#!/usr/bin/env python3
"""Chunk transcript .txt files into raw Chunk JSONL matching the corpus format.

Emits one line per chunk: {"type":"Chunk","data":{"text":"[slug] …","chunk_index":N}}
~220 words per chunk, on sentence-ish boundaries. Feed the output through
`omnigraph embed` (adds `embedding`), then finalize.py (adds slug/id/createdAt
+ PartOfArtifact edges). Talk slug = transcript filename stem; the corpus
convention prefixes each chunk's text with "[<slug>] " for provenance.
"""
import json, re, sys, pathlib

TARGET_WORDS = 220
ROOT = pathlib.Path("/Users/andrew/code/intel-graph")


def clean(text):
    text = re.sub(r"^>>\s*", "", text)
    text = text.replace("\n", " ")
    return re.sub(r"\s+", " ", text).strip()


def chunk(text):
    # split into sentences, then greedily pack to ~TARGET_WORDS
    sents = re.split(r"(?<=[.!?])\s+", text)
    chunks, buf, n = [], [], 0
    for s in sents:
        w = len(s.split())
        if n + w > TARGET_WORDS and buf:
            chunks.append(" ".join(buf)); buf, n = [], 0
        buf.append(s); n += w
    if buf:
        chunks.append(" ".join(buf))
    return chunks


def main(stems, out_path):
    with open(out_path, "w") as fh:
        for stem in stems:
            text = clean((ROOT / "transcripts" / f"{stem}.txt").read_text())
            for i, c in enumerate(chunk(text)):
                rec = {"type": "Chunk", "data": {"text": f"[{stem}] {c}", "chunk_index": i}}
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    stems = [
        "hall-akamai-signal-layer", "buykin-maersk-tribal-dungeons-shipping",
        "milev-kanagala-navan-agents-microservices-2015", "kus-box-half-life-agent-infra",
        "lewis-millennium-startups-enterprise-contracts", "touil-quantumblack-ai-native-orgs-skills",
        "steimantas-oxylabs-missing-layer", "abdalla-warp-oz-cloud-agent-platform",
        "louf-dottxt-agent-frameworks-harmful", "chawla-koul-microsoft-finops-agents",
        "malhotra-anthropic-budget-not-token", "jain-docker-agent-runtime-autonomy",
        "bjornn-leaseend-finetuned-model-tech-debt", "aggarwal-decawork-it-admin-ai-workforce",
        "lovejoy-howard-enterprise-stack-not-ready", "hong-ironclad-tokenmaxxing-trusted-throughput",
        "munaf-tiktok-agents-distributed-systems",
    ]
    main(stems, ROOT / "seed-work" / "chunks22-raw.jsonl")
