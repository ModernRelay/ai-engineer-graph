# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A SPIKE-framework knowledge graph of AI/ML industry intelligence, built on
[Omnigraph](https://github.com/ModernRelay/omnigraph). Two halves:

1. **Graph cookbook** — `schema.pg` (source of truth), `queries/*.gq`,
   `cluster.yaml`, `policies/`, `seed.md`. No application code.
2. **Corpus pipeline** — AI Engineer World's Fair talks flowing through
   `transcripts/` → `extraction/` → `seed-work/` → the loaded graph. This is
   the ongoing work (200+ talks so far, processed in batches).

## Commands

```bash
# Validate schema + query against each other — run after ANY schema or query edit.
# This is the repo's only check; there are no tests.
omnigraph lint --schema schema.pg --query queries/<file>.gq

# Control plane (schema/query/policy changes)
omnigraph cluster plan  --config .
omnigraph cluster apply --config . --as act-admin   # then restart the server

# Rebuild full seed from fragments (validates and reports)
python3 seed-work/merge_validate.py                  # → seed-work/seed-full.jsonl

# Data plane
omnigraph load --data <f.jsonl> --mode merge --as act-analyst \
  s3://intel-graph/clusters/spike-intel/graphs/spike.omni
omnigraph embed --input <raw.jsonl> --output <embedded.jsonl> --spec seed-work/embed-spec.json

# Query the running server (alias pack merged into ~/.omnigraph/config.yaml)
omnigraph alias pattern-signals pat-context-graphs
omnigraph alias hybrid-search "reward hacking"
omnigraph mutate add_signal --server intel-local --graph spike --params '{…}'
```

**RUNBOOK.md is the operational truth for this machine**: RustFS on
`127.0.0.1:9100`, cluster root `s3://intel-graph/clusters/spike-intel`,
server on `127.0.0.1:8081` (bearer-token auth; 8080 is an unrelated stale
server — leave it alone). Env comes from `.env.omni` + `.env.embedding`
(gitignored). README.md's quick start describes the generic local-cluster
path instead; prefer RUNBOOK.md when operating here.

## Corpus Pipeline

Each batch of talks moves through fixed stages, each with an index file that
must be updated in the same change:

1. **`transcripts/<talk>.txt`** — yt-dlp auto-captions (unreliable for
   verbatim quotes; garbles like "Snyk"→"Sneak" are normal). Register in the
   batch table in `transcripts/README.md` with the video URL.
2. **`extraction/<talk>.md`** — one SPIKE extraction per talk, entity tables
   for human review. Register in `extraction/README.md` with status
   (`for review` → `reviewed`). Note caption garbles and their
   normalizations in the file header; quotes are paraphrases.
3. **`extraction/registry.md`** — single source of truth for shared slugs.
   Extraction files define only talk-local entities and reference shared
   ones by slug marked **[registry]**/**[seed]** (never re-defined). New
   cross-cutting entities and merge-review flags get reconciled here per
   batch.
4. **`seed-work/`** — extractions become `frag-N.jsonl` following
   `seed-work/CONVERSION-SPEC.md` EXACTLY (legal fields, enum coercions, the
   complete edge set); `merge_validate.py` merges + validates into
   `seed-full.jsonl`. Batches 16–23 are converted **deterministically** by
   `seed-work/convert_1719.py` (add new batch stems to its `BATCHES` dict);
   earlier fragments were agent-authored. Cross-batch pattern coinage goes in a
   supplementary `frag-N-coinage.jsonl` rather than re-converting old batches.
   Transcript chunks: `chunk_talks.py` → `omnigraph embed` → `finalize_chunks.py`
   → `load --mode merge` (chunk slug = `<talk-slug>#<idx>`, linked via
   PartOfArtifact). **RUNBOOK.md "Adding a batch" is the authoritative
   step-by-step for loading the graph.**

All generated JSONL (`seed.jsonl`, `seed-work/*.jsonl`) is gitignored — the
committed artifacts are the markdown, schema, and queries.

**Extraction conventions:**
- Slug prefixes: `sig-`, `pat-`, `el-`, `ins-`, `how-`, `co-`, `exp-`,
  `ia-`, `source-`; slug is the external identity everywhere.
- Patterns are seed-altitude **theses about change** (e.g. "The Verification
  Gap"), never domains or topics — the field lives in the `domain:` enum.
  Coin new patterns sparingly (~1 per batch, reconciled in registry.md);
  near-duplicates get an explicit merge-review note instead of silent merging.
- Every Signal/KnowHow carries artifact provenance edges; talks publish as
  `ia-aie-*` → `PublishedBySource → source-aie-yt`.

## Schema Language (`.pg`)

- `node` defines entity types; `edge` defines typed relationships (`edge Name: Source -> Target`)
- `@key` marks external identity (always `slug` here)
- `@index`, `@unique`, `@card(min..max)`, `@range(lo..hi)`, `@embed("prop")`
- `?` = optional, `[Type]` = list, `enum(...)` = inline closed set
- Comments use `//` not `#`

## Domain Model

**SPIKE nodes:** Signal, Element, Pattern, Insight, KnowHow.
**Supportive:** Company, SourceEntity, Expert, InformationArtifact, Chunk.

**Core analytical loop:** Signals form or contradict Patterns. Patterns drive
or rely on other Patterns. Everything else supports this loop or maps the domain.

**Design choices to preserve:**
- Flat `kind` enums on Element and Pattern — no interfaces or subtypes
- ElementKind: `product, technology, framework, concept, ops`; PatternKind: `challenge, disruption, dynamic`
- Domain is an enum property on Signal/Element, not a node
- Edges follow `VerbTargetType` naming (e.g. `FormsPattern`, `DevelopedByCompany`)
- Embeddings only on Chunk: `Vector(3072) @embed("text")` (engine default `gemini-embedding-2-preview`)
- Chunk is immutable (no `updatedAt`)

## When Editing

- Use `@rename_from(...)` on property/type renames for migration support.
  Known engine limits: `id` is a reserved column name; migration v1 cannot
  add a required key in place (needs a graph rebuild — see RUNBOOK.md Day-2).
- Keep README.md in sync with schema.pg
- Prefer semantic edge names over generic ones (`Enables` not `RelatedTo`)
- Use the narrowest type that fits (enums over strings, Date over String)
- Required vs optional is deliberate — don't add `?` without reason
- Never commit `__cluster/`, `graphs/`, or `.env*` (gitignored — local state and secrets)

## Other Directories

- `skill/` — the `omnigraph-intel-bootstrap` skill (published upstream in
  omnigraph-cookbooks): bootstraps a new SPIKE graph for any domain. Not part
  of this repo's pipeline; keep in sync only if the cookbook structure changes.
- `report.md` — a generated analysis artifact, not infrastructure.
