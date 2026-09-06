# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

A SPIKE-framework knowledge graph of the AI Engineer World's Fair 2026 talk
corpus, built on [Omnigraph](https://github.com/ModernRelay/omnigraph). The
repository is the complete, loadable definition of the graph and nothing else:

- `schema.pg` — the schema (source of truth for the data model)
- `cluster.yaml` + `policies/` — cluster config and Cedar policy bundles
- `queries/*.gq` — the stored queries the server serves (reads + mutations)
- `seed/` — the full dataset in load order: `01-sources.jsonl` … `09-knowhow.jsonl`
  (one file per node type), `10-edges.jsonl`, and `chunks/part-NN.jsonl`
  (transcript chunks in parts of 400, embedded at load time with `embed-spec.json`)
- `omnigraph-config.example.yaml` — client profile and alias pack
- `README.md` — the one document: model, layout, setup, load, query, operate

The corpus pipeline that produces the seed (transcripts, per-talk extraction
notes, conversion scripts, fragments) is a local, gitignored workflow
(`transcripts/`, `extraction/`, `seed-work/`, `RUNBOOK.md` on the maintainer's
machine). Never add those paths, generated JSONL work files, `.env*`,
`__cluster/`, or `graphs/` to git.

## Commands

```bash
# The repo's only check: schema and every query must lint against each other.
for q in queries/*.gq; do omnigraph lint --schema schema.pg --query "$q"; done
omnigraph cluster validate --config .        # config + policies (an external_blobs WARN is expected)

# Control plane (after any schema / query / policy edit)
omnigraph cluster plan  --config .
omnigraph cluster apply --config . --as act-admin   # then restart the server

# Data plane — see README "Load the seed" for the full procedure
for f in seed/[0-9]*.jsonl; do omnigraph load --data "$f" --mode overwrite --as act-analyst --yes <graph-uri>; done
```

Environment for local operation comes from `.env.omni` + `.env.embedding`
(gitignored; key names are listed in the README). Source both before any
`omnigraph` command:
`set -a && source .env.omni && source .env.embedding && set +a`.

## Conventions

- `slug` is the external identity everywhere; prefixes `sig-`, `pat-`, `el-`,
  `ins-`, `how-`, `co-`, `exp-`, `ia-`, `source-`, chunks `<talk-slug>#<idx>`.
- Patterns are seed-altitude theses about change, never topics; coin them
  sparingly. Domain is an enum property on Signal/Element, not a node.
- Edges follow `VerbTargetType` naming; every Signal and KnowHow carries
  artifact provenance edges.
- Schema edits: `@rename_from(...)` on renames; enums over strings; `id` is an
  engine-reserved column name; keep the README's model section in sync.
- Loads: `--mode overwrite` replaces only the node/edge types present in the
  file; edges have no `@key`, so never re-load chunk edges on top of existing
  ones. Verify remote writes by comparing `commit list --branch main` heads.
- Keep the seed files the exact export of the served graph: regenerate them
  from the graph (`omnigraph export`) rather than hand-editing.
