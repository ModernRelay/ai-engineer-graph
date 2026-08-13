# Local deployment runbook (this machine)

Stood up 2026-07-22. Native RustFS (no Docker) + cluster-booted omnigraph-server.

## Topology

- **RustFS** (S3-compatible object store): `127.0.0.1:9100`, native binary,
  data in `~/.local/share/rustfs-intel-data/`, bucket `intel-graph`.
- **Cluster root**: `s3://intel-graph/clusters/spike-intel` (schema, stored
  queries, policies, graph datasets — applied via `omnigraph cluster apply`).
- **Graph**: `spike` → `s3://intel-graph/clusters/spike-intel/graphs/spike.omni`
  — **rebuilt clean 2026-08-14 on omnigraph 0.9.0 (internal schema v6)**.
  6,590 nodes / 13,107 edges: 3,300 entity nodes (959 signals, 713 elements,
  451 insights, 428 knowhows, 254 experts, 238 artifacts, 230 companies,
  17 sources, 10 patterns) + 3,290 embedded transcript chunks (3072-dim,
  gemini-embedding-2-preview).
  ⚠ **Data currency**: the graph holds the corpus **through batch 16**
  (218 talks). Batches 17–19 (22 talks) and the two patterns coined
  2026-08-14 (`pat-agent-memory-layer`, `pat-continual-learning-turn`) are
  **not loaded** — their extractions exist but were never converted to
  fragments. See "Bringing the graph current" below.
- **Server**: `http://127.0.0.1:8081` (cluster-booted, bearer-token auth).
  Port 8080 is occupied by an unrelated stale 0.6.2 dev server (June,
  serving ~/exp/intel) — left untouched. Port 9000 is held by an unrelated
  `container` process with a wildcard bind — RustFS deliberately avoids it
  (a dead RustFS on 9000 would silently fall through to that listener).

## Credentials

- `.env.omni` (gitignored): RustFS AWS_* creds + endpoint, bearer tokens for
  `act-reader` / `act-analyst` / `act-admin`
  (`OMNIGRAPH_SERVER_BEARER_TOKENS_JSON` + individual `TOKEN_ACT_*`),
  `OMNIGRAPH_EMBED_PROVIDER=gemini`, `OMNIGRAPH_EMBED_MODEL=gemini-embedding-2-preview`.
- `.env.embedding` (gitignored): `GEMINI_API_KEY` (embeddings, query-time
  `nearest()` on the server).

## Start / restart

```bash
cd ~/code/intel-graph
set -a && source .env.omni && source .env.embedding && set +a

# 1. object store (if not running) — detached so it survives the shell
nohup rustfs server ~/.local/share/rustfs-intel-data \
  --address 127.0.0.1:9100 \
  --access-key "$AWS_ACCESS_KEY_ID" --secret-key "$AWS_SECRET_ACCESS_KEY" \
  > ~/.local/share/rustfs-intel-data/rustfs.log 2>&1 & disown

# 2. server (config-free from the bucket; needs AWS_* + tokens + GEMINI key in env)
nohup omnigraph-server --cluster s3://intel-graph/clusters/spike-intel \
  --bind 127.0.0.1:8081 \
  > ~/.local/share/rustfs-intel-data/omnigraph-server.log 2>&1 & disown
```

## Use (CLI — the intended interface)

Operator config: server `intel-local` (http://127.0.0.1:8081), profile
`intel`, and the alias pack are merged into `~/.omnigraph/config.yaml`
(backup at config.yaml.bak-2026-07-22). Credential stored via
`omnigraph login intel-local` (analyst token — read + stored mutations).

```bash
# lookups / drill-downs
omnigraph alias signal sig-replit-db-deletion
omnigraph alias pattern pat-verification-gap
omnigraph alias pattern-signals pat-context-graphs
omnigraph alias pattern-counter pat-harness-over-model    # counter-evidence
omnigraph alias company co-anthropic
omnigraph alias company-signals co-cursor
omnigraph alias expert-talks exp-thariq-shihipar
omnigraph alias talk-signals ia-aie-han-kernels-rl

# leaderboards / review loop
omnigraph alias top-patterns
omnigraph alias top-companies
omnigraph alias contested
omnigraph alias triage                                    # orphan signals
omnigraph alias signals-since 2026-07-20T00:00:00Z

# semantic / hybrid search over 3,290 transcript chunks
omnigraph alias related "keeping voice conversation latency low enough to feel natural"
omnigraph alias hybrid-search "models cheating their reward function during RL training"

# traversals (multi-hop / variable-hop / negation — traversals.gq)
omnigraph alias expert-patterns exp-thariq-shihipar   # expert ← talks ← signals → patterns
omnigraph alias pattern-experts pat-verification-gap  # who's the authority on a thesis
omnigraph alias company-footprint co-cursor           # company ← signals → patterns
omnigraph alias company-tech co-openai                # company ← experts ← talks → elements
omnigraph alias company-risk co-anthropic             # signals about company contradicting patterns
omnigraph alias el-deps el-ace-voice-tutor            # transitive UsesElement, ≤3 hops
omnigraph alias el-dependents el-mcp                  # everything built on X, ≤3 hops
omnigraph alias el-neighbors el-claude-code           # undirected <usesElement>
omnigraph alias pattern-pairs                         # theses that co-occur on signals
omnigraph alias pattern-bridges                       # elements exemplifying one thesis, enabling another
omnigraph alias pattern-knowhow pat-context-graphs    # 3-hop: pattern ← elements ← knowhow
omnigraph alias pattern-timeline pat-durable-execution # evidence accumulation, oldest first
omnigraph alias co-presenters exp-cat-wu              # shared-artifact experts
omnigraph alias gaps-products                         # negation: products w/o developer
omnigraph alias gaps-patternless                      # negation: elements w/o any pattern edge
omnigraph alias signal-hybrid "reward hacking"        # RRF of bm25(name)+bm25(brief)
omnigraph alias domain-search security "supply chain compromise"

# stored mutations run via mutate (NOT aliases), e.g.:
omnigraph mutate add_signal --server intel-local --graph spike --params '{…}'
# ad-hoc queries:
omnigraph query top_patterns_by_signals --profile intel
```

Roles (verified): reader = stored reads; analyst = + stored mutations and
data-plane writes; admin = + `GET /graphs`. Anonymous → 401.

## Day-2

- Schema/query/policy change: edit files → `omnigraph cluster plan --config .`
  → `omnigraph cluster apply --config . --as act-admin` → restart server.
- Data: `omnigraph load --data <f.jsonl> --mode merge --as act-analyst \
  s3://intel-graph/clusters/spike-intel/graphs/spike.omni`
- New chunks: raw JSONL → `omnigraph embed --input <raw> --output <embedded>
  --spec seed-work/embed-spec.json` → load embedded (Chunk is keyless — no
  PartOfArtifact edges in bulk JSONL; text carries a `[talk-slug]` prefix
  for provenance instead).
- Chunks are keyed (`slug` = "<talk-slug>#<idx>") and connected to their
  talks via PartOfArtifact (schema evolved 2026-07-22 via graph rebuild —
  note: "id" is an engine-reserved column name; migration v1 can't add a
  required key in place, hence rebuild). Graph-scoped semantic search works:
  `omnigraph alias talk-semantic <ia-slug> "<question>"` (join + nearest);
  an FTS *filter* + nearest in one query is still an engine limit.
- Full-seed rebuild: `python3 seed-work/merge_validate.py` regenerates
  `seed-work/seed-full.jsonl` from `seed.jsonl` + `seed-work/frag-*.jsonl`,
  then `load --mode overwrite` + re-load chunks.

## The 0.9 upgrade and clean rebuild (2026-08-14)

The graph was rebuilt from scratch because **omnigraph binaries read exactly
one on-disk format version** — `MIN_SUPPORTED_INTERNAL_SCHEMA_VERSION ==
INTERNAL_MANIFEST_SCHEMA_VERSION`, with no in-place migration. The old graph
was stamped internal **v4** (written by the 0.8.x-era binary that created the
cluster on 2026-07-22); 0.9.0 reads only **v6** and refuses v4 outright —
including refusing to *export* it.

**⚠ Binary version strings do not track the on-disk format.** Measured on this
machine:

| binary | `--version` | reads internal |
|---|---|---|
| `/opt/homebrew/bin/omnigraph` | 0.9.0 | v6 |
| `~/code/omnigraph/target/debug/omnigraph` (Aug 12) | 0.10.0 | v6 |
| `~/code/omnigraph/target/release/omnigraph` (Jul 19) | 0.8.1 | **v8** |

Never assume a lower version string means it can open an older graph. Check by
running any command against the graph and reading the refusal message.

### What the rebuild actually required

1. **Policy schema change** — `policies/server.policy.yaml` had `kind: server`, which 0.9 rejects (`unknown field 'kind'`, valid: `version`, `groups`, `protected_branches`, `rules`). Scope now comes solely from `applies_to` in `cluster.yaml`. Removed; `cluster plan` then passed.
2. **Delete + refresh + apply** — deleting the graph prefix is *not* enough: `cluster plan` still reported "no changes" because the ledger records the graph. **`omnigraph cluster refresh` reconciles state from storage** (117 → 115 resources); only then does `plan` show `Create graph.spike` / `Create schema.spike`, with no approval gate. `cluster apply --as act-admin` recreates it at v6.
3. **32 MiB per-node-type load limit** — `chunks-final.jsonl` (1,966 chunks × 3072-dim) failed with `resource limit exceeded for keyed parsed value bytes for node:Chunk: actual 33554556, limit 33554432` — over by 124 bytes. Split into 3 slug-partitioned parts (keeping each chunk with its `PartOfArtifact` edge) and loaded fine.
4. **Edges have no `@key`, so overlapping loads duplicate them** — `chunks14-final.jsonl` overlaps `chunks1112-final.jsonl` on 11 `shaw-marten-everything-is-a-rollout` chunks (that talk was re-extracted at batch 11). Second load hit `@unique violation on PartOfArtifact.src`. Fix: drop already-present slugs before loading, don't rely on `merge` to dedupe edges.

### Rebuild recipe (if this is ever needed again)

```bash
set -a && source .env.omni && source .env.embedding && set +a
G=s3://intel-graph/clusters/spike-intel/graphs/spike.omni

aws --endpoint-url "$AWS_ENDPOINT_URL" s3 sync \
  s3://intel-graph/clusters/spike-intel/ ~/backup/ --only-show-errors  # byte backup FIRST
aws --endpoint-url "$AWS_ENDPOINT_URL" s3 rm --recursive "$G"/
omnigraph cluster refresh --config .          # REQUIRED — else plan sees no change
omnigraph cluster plan    --config .          # expect: Create graph.spike, Create schema.spike
omnigraph cluster apply   --config . --as act-admin
omnigraph load --data seed-work/seed-full.jsonl --mode overwrite --as act-analyst --yes "$G"
# then each chunks*-final.jsonl with --mode merge, splitting any file >32 MiB of parsed Chunk bytes
```

A byte-level `s3 sync` of the cluster prefix is a **better** fallback than a
logical export: it restores the exact prior graph, readable by the old binary.
A logical export drops commit history and branches anyway. Current backup:
`~/.local/share/intel-graph-backups/spike-omni-raw-2026-08-14` (111 MB, 5,506
objects, verified exact).

### ⚠ Two RustFS processes contend for :9100

`~/.local/share/rustfs-intel-data` (creds `intelgraph`) is the intel-graph
store and currently owns the port. A second, unrelated RustFS on
`~/exp/rustfs-data` (creds `rustfsadmin`) is also running and will seize
:9100 if the first dies — the cluster would then silently resolve to an empty
object store. Same hazard this runbook already documents for :9000. Kill the
stale one before any load.

## Bringing the graph current

The graph trails the corpus by 22 talks and 2 patterns. To close the gap:

1. Convert `extraction/` batches 17, 18, 19 to `seed-work/frag-17.jsonl` … `frag-19.jsonl` per `seed-work/CONVERSION-SPEC.md` (the two coined patterns are defined in `khemani-every-memory-system.md` and `su-neocognition-continual-learning-expertise.md`, so a conversion pass picks them up).
2. `python3 seed-work/merge_validate.py` → regenerate `seed-work/seed-full.jsonl`.
3. `omnigraph load --data seed-work/seed-full.jsonl --mode overwrite …`, then re-load every `chunks*-final.jsonl` (overwrite is whole-graph clean-slate — chunks must follow it, not precede it).
4. Chunks are missing for **15 talks** (all of batches 18–19): raw JSONL → `omnigraph embed --spec seed-work/embed-spec.json` → finalize with `slug = "<talk-slug>#<idx>"` + `PartOfArtifact` edges → load. `seed-work/chunks19-embedded.jsonl` (117 chunks) is also still keyless and needs the same finalize step before it can load.
