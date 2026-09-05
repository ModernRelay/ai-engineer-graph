# Local deployment runbook (this machine)

Stood up 2026-07-22. Native RustFS (no Docker) + cluster-booted omnigraph-server.

## Topology

- **RustFS** (S3-compatible object store): `127.0.0.1:9100`, native binary,
  data in `~/.local/share/rustfs-intel-data/`, bucket `intel-graph`.
- **Cluster root**: `s3://intel-graph/clusters/spike-intel` (schema, stored
  queries, policies, graph datasets — applied via `omnigraph cluster apply`).
- **Graph**: `spike` → `s3://intel-graph/clusters/spike-intel/graphs/spike.omni`
  — clean base rebuilt 2026-08-14 on omnigraph 0.9.0 (internal schema v6);
  upgraded in place to **0.10.0** on 2026-09-05 (same v6 format; full-text
  indexes rebuilt for Lance 11 — see "The 0.10 upgrade");
  kept current per batch since. **As of batch 21 (2026-08-18):**
  7,525 nodes / 15,448 edges: 3,920 entity nodes (1,150 signals, 906 elements,
  523 insights, 472 knowhows, 295 experts, 278 artifacts, 263 companies,
  17 sources, **16 patterns**) + 3,605 embedded transcript chunks (3072-dim,
  gemini-embedding-2-preview) covering **258 talks**.
  ⚠ These counts drift every batch — re-check with
  `omnigraph snapshot --store <graph-uri> --json` rather than trusting them;
  the numbers here are a sanity anchor, not a live source of truth.
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

## First-time setup (new machine)

Nothing below is committed — `.env.omni` and `.env.embedding` are gitignored
secrets. To stand up this cluster from zero:

```bash
# 1. Tools
brew install rustfs/tap/rustfs           # native S3-compatible object store (no Docker)
brew install omnigraph                    # CLI + omnigraph-server — 0.10.x (v6 format; FTS indexes are Lance 11 — never mix 0.9 and 0.10 binaries on this store)
omnigraph version                         # confirm; the graph is internal-schema v6

# 2. Start RustFS and create the bucket (one-time)
mkdir -p ~/.local/share/rustfs-intel-data
nohup rustfs server ~/.local/share/rustfs-intel-data --address 127.0.0.1:9100 \
  --access-key <ACCESS_KEY> --secret-key <SECRET_KEY> \
  > ~/.local/share/rustfs-intel-data/rustfs.log 2>&1 & disown
aws --endpoint-url http://127.0.0.1:9100 s3 mb s3://intel-graph   # create the bucket once
```

Then write the two env files (key names are fixed; fill in your own values):

```bash
# .env.omni  (gitignored) — RustFS creds + endpoint, bearer tokens, embed provider
AWS_ACCESS_KEY_ID=<access-key>
AWS_SECRET_ACCESS_KEY=<secret-key>
AWS_ENDPOINT_URL=http://127.0.0.1:9100
AWS_REGION=us-east-1
AWS_ALLOW_HTTP=true
OMNIGRAPH_SERVER_BEARER_TOKENS_JSON={"act-reader":"<tok>","act-analyst":"<tok>","act-admin":"<tok>"}
TOKEN_ACT_READER=<tok>
TOKEN_ACT_ANALYST=<tok>
TOKEN_ACT_ADMIN=<tok>
OMNIGRAPH_EMBED_PROVIDER=gemini
OMNIGRAPH_EMBED_MODEL=gemini-embedding-2-preview

# .env.embedding  (gitignored) — query-time embedding key(s)
GEMINI_API_KEY=<key>
OPENAI_API_KEY=<key>          # optional; only if you switch embed provider
```

Converge the cluster and load the data (see also README.md for the generic
control-plane flow, and the "Adding a batch" pipeline below for the data plane):

```bash
set -a && source .env.omni && source .env.embedding && set +a
omnigraph cluster plan  --config .
omnigraph cluster apply --config . --as act-admin        # creates graphs/spike.omni at internal v6
omnigraph load --data seed-work/seed-full.jsonl --mode overwrite --as act-analyst --yes \
  s3://intel-graph/clusters/spike-intel/graphs/spike.omni
# then load each seed-work/chunks*-final.jsonl with --mode merge (see "Adding a batch")
```

`seed-work/seed-full.jsonl` and the `chunks*-final.jsonl` are gitignored and
regenerated locally — rebuild them with `convert_1719.py` + `merge_validate.py`
(entities) and `chunk_talks.py` + `omnigraph embed` + `finalize_chunks.py`
(chunks) before the loads above. Once loaded, start the server as below.

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

# semantic / hybrid search over the transcript chunks
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
- New chunks: `chunk_talks.py` → `omnigraph embed` → `finalize_chunks.py` →
  `load --mode merge` (see "Adding a batch" below for the full commands).
  Chunks are keyed (`slug` = "<talk-slug>#<idx>") with a `PartOfArtifact`
  edge to their talk; `finalize_chunks.py` adds both (the raw/embedded JSONL
  is keyless — the `[talk-slug]` text prefix carries provenance until then).
  ("id" is an engine-reserved column name; the keyed-chunk schema was added
  2026-07-22 via graph rebuild since migration v1 can't add a required key in
  place.) Graph-scoped semantic search works:
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

## The 0.10 upgrade (2026-09-05)

Homebrew had already moved `omnigraph`/`omnigraph-server` to **0.10.0**; the
server picked it up at the batch-22 restart and opened the graph fine, because
**0.9 and 0.10 share storage format v6** (Lance 9 → Lance 11 underneath). The
upgrade is therefore *not* a rebuild — but it is not a no-op either. Per the
0.10 upgrade guide (`docs/user/operations/upgrade.md` in the omnigraph repo):

- The Lance 11 line changes the English **stemmer**, so pre-0.10 full-text
  indexes must be rebuilt explicitly; `optimize` does not do it. Unindexed
  fields keep working via scan, which is why `bm25()` queries *appeared* fine
  before the rebuild — coverage, not correctness, was the gap.
- The **CLI/HTTP vocabulary is not rolling-compatible** across 0.9/0.10
  (legacy aliases such as `table_key`, `row_id`, `manifest_version`,
  `rows_loaded`, `export --table` are removed). Update CLI, server and client
  integrations together; never run a 0.9 and a 0.10 binary against the same
  store.
- New optional cluster-state field `external_blobs` (default-deny external
  Blob URIs). We don't use Blobs; `cluster validate` now prints an
  `external_blob_ingress_default_deny` WARN for `graphs.spike` — expected,
  ignore. (Rollback note: once an `external_blobs` policy is *applied*, 0.9
  can't read the cluster state; we have not applied one.)

What was done, in order:

```bash
set -a && source .env.omni && source .env.embedding && set +a
G=s3://intel-graph/clusters/spike-intel/graphs/spike.omni
omnigraph version                                   # 0.10.0 / internal-schema 6
for q in queries/*.gq; do omnigraph lint --schema schema.pg --query "$q"; done   # 10/10 clean
omnigraph cluster validate --config .               # valid, 117 resources (+ the blob WARN)
omnigraph cluster plan --config .                   # 0 changes
aws --endpoint-url "$AWS_ENDPOINT_URL" s3 sync s3://intel-graph/clusters/spike-intel/ \
  ~/.local/share/intel-graph-backups/spike-omni-raw-2026-09-05-pre-010/ --only-show-errors   # 1,122 objects, 73 MB
pkill -f "omnigraph-server --cluster s3://intel-graph"; sleep 3      # server MUST be stopped
omnigraph rebuild-full-text-indexes "$G" --branch main --as act-admin --json
# → 20 indexes rebuilt in ONE graph commit (head v25 → v26, actor act-admin):
#   Chunk: slug; Company: name, slug; Element: name, slug; Expert: name, slug; InformationArtifact: name, slug; Insight: name, slug; KnowHow: name, slug; Pattern: name, slug; Signal: brief, name, slug; SourceEntity: name, slug
#   warning: "rebuilt with the default English analyzer; custom tokenizer settings replaced" (we had none)
nohup omnigraph-server --cluster s3://intel-graph/clusters/spike-intel --bind 127.0.0.1:8081 \
  > ~/.local/share/rustfs-intel-data/omnigraph-server.log 2>&1 & disown
curl -s http://127.0.0.1:8081/healthz                # version 0.10.0, internal_schema_version 6
omnigraph alias top-patterns; omnigraph alias hybrid-search "give the agent a budget"   # unchanged counts, search OK
```

Only `main` was rebuilt — there are no other live branches. Historical
snapshots are not rewritten (restoring one would need another rebuild).

Verification after restart: talks 295 / chunks 3,879 / pattern counts
unchanged; `bm25()` over stem-sensitive words returns sensible rows; `nearest()`
and `rrf()` hybrid unchanged; `POST /graphs/spike/export` (what the explorer
streams) returns 200. The explorer (intel-graph-ui, SDK pinned at 0.9.0) was
exercised against the 0.10 server with its Playwright suite — see
EXPLORER-DESIGN.md for the result.

0.10 quirks worth knowing:

- **`omnigraph policy validate --cluster .` errors on our two-bundle layout**
  ("cluster has 2 policy bundles [intel, server]; pass --graph") and
  `--graph spike` still refuses ("matches 2 policy bundles; the cluster model
  expects one bundle per graph scope") — the CLI's per-graph check doesn't
  understand a cluster-scoped bundle (`applies_to: [cluster]`).
  `cluster validate` is the working policy check; the server enforces both
  bundles correctly (admin-only `graph_list` still denied to the analyst token).
- `graphs list` needs the admin token (server policy); the `intel-local`
  profile carries the analyst token, so it is denied by design.
- `queries list` is a cluster control command (`--cluster .`), not a server one.
- Rollback = restore the whole pre-0.10 backup above with 0.9 binaries; do not
  point a 0.9 binary at the rebuilt store.

## Adding a batch (the per-batch pipeline)

The graph is kept current per batch. As of batch 22 (2026-09-05, 276 talks) it is up to date. To add a
new batch of talks:

```bash
cd ~/code/intel-graph
set -a && source .env.omni && source .env.embedding && set +a
G=s3://intel-graph/clusters/spike-intel/graphs/spike.omni

# 1. Transcripts: yt-dlp captions -> clean .txt  (register in transcripts/README.md)
yt-dlp --skip-download --write-auto-subs --sub-lang "en.*" --convert-subs srt -o "<slug>.%(ext)s" <url>
python3 seed-work/srt2txt.py <slug>.en.srt transcripts/<slug>.txt

# 2. Extractions: one SPIKE extraction per talk in extraction/<slug>.md
#    (register in extraction/README.md; reconcile shared slugs in registry.md)

# 3. Convert extractions -> fragment. Add the batch's stems to the BATCHES dict
#    in seed-work/convert_1719.py first, then:
python3 seed-work/convert_1719.py            # writes seed-work/frag-NN.jsonl
python3 seed-work/merge_validate.py          # -> seed-work/seed-full.jsonl (+ validation-report.txt)

# 4. Load entities (per-table overwrite — see the trap below)
omnigraph load --data seed-work/seed-full.jsonl --mode overwrite --as act-analyst --yes "$G"

# 5. Chunks: chunk -> embed -> finalize -> load (merge)
#    Edit the stems list + output path in seed-work/chunk_talks.py first, then:
python3 seed-work/chunk_talks.py             # transcripts -> seed-work/chunksNN-raw.jsonl
omnigraph embed --input seed-work/chunksNN-raw.jsonl --output seed-work/chunksNN-embedded.jsonl   --spec seed-work/embed-spec.json
python3 seed-work/finalize_chunks.py seed-work/chunksNN-embedded.jsonl seed-work/chunksNN-final.jsonl <YYYY-MM-DD>
omnigraph load --data seed-work/chunksNN-final.jsonl --mode merge --as act-analyst --yes "$G"

# 5b. (0.10+) Rebuild full-text indexes so the new rows are indexed, not just scanned —
#     server must be stopped for this direct-storage maintenance command
pkill -f "omnigraph-server --cluster s3://intel-graph"; sleep 3
omnigraph rebuild-full-text-indexes "$G" --branch main --as act-admin --json

# 6. Restart the server so it re-pins to the new graph head, then verify
pkill -f "omnigraph-server --cluster s3://intel-graph"; sleep 3
nohup omnigraph-server --cluster s3://intel-graph/clusters/spike-intel \
  --bind 127.0.0.1:8081 > ~/.local/share/rustfs-intel-data/omnigraph-server.log 2>&1 & disown
sleep 8 && curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8081/healthz
omnigraph alias top-patterns                             # sanity
```

Three traps, all verified:
- **`--mode overwrite` is per-table, not whole-graph.** It replaces only the node/edge types present in the file, so `Chunk` and `PartOfArtifact` survive an entity-only overwrite untouched — which is why chunks are loaded separately with `--mode merge` and **must not** be re-loaded after an entity overwrite (re-loading trips `@unique` on `PartOfArtifact.src`, since edges have no `@key`).
- **Load entities before finalizing chunks.** `finalize_chunks.py` checks every chunk's target artifact exists in `seed-full.jsonl` and refuses otherwise.
- **A load >32 MiB of parsed bytes for one node type fails** (`resource limit exceeded`). The batch-1 `chunks-final.jsonl` (1,966 chunks) had to be split into 3 slug-partitioned parts; per-batch chunk files are far under the limit.
- **Check the object store is alive before loading** (found 2026-09-05: RustFS had
  died silently). `curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:9100/`
  must return `403`, not `000`. With RustFS down, `omnigraph load` fails at its
  first list call with a misleading `client.rs:304` storage error *before writing
  anything*, and `omnigraph-server` refuses to boot (`cluster … is not ready to
  serve`). Restart RustFS per "Start / restart", confirm `commit list` shows the
  expected head, then load. Don't pipe `load` into `tail` — it masks the exit code.
- **Server binary drift:** after the 2026-09-05 restart the server reports
  `0.10.0` (homebrew upgraded `omnigraph-server`); it opens the internal-v6 graph
  fine. Check `/healthz` `version` after any restart and keep `omnigraph` CLI and
  server on the same minor.

## Cross-batch pattern coinage

Coining a pattern that draws evidence from many batches does **not** require
re-converting old fragments (batches 1–15 aren't regenerable by
`convert_1719.py`). Instead write a supplementary coinage fragment
`seed-work/frag-NN-coinage.jsonl` containing the new `Pattern` node(s) plus the
`FormsPattern`/`ContradictsPattern` edges from already-defined signals; the
signal nodes already exist in the older fragments and `merge_validate.py`
resolves the edges. This is how `frag-20-coinage` (2 patterns, 2026-08-14) and
`frag-21-coinage` (4 patterns, 2026-08-16) were loaded. Also flip the source
extraction files' held-pattern-less columns to the edge for source-of-truth
(deduped against the coinage fragment on load).

## Conversion coverage — a gap worth knowing about (found 2026-08-14)

`seed-work/frag-*.jsonl` filenames do **not** map to corpus batch numbers.
`frag-16a` and `frag-16b` are batch **15**'s conversion (29 talks); batch 16's
own 9 talks (Temporal, MCP Apps, Cloudflare, Daily, NVIDIA, both panels,
Turbopuffer, Cline) had **never been converted at all** despite the corpus
commit reading "full corpus through batch 16". They are now in `frag-16c`.

Fragments as of 2026-08-14, with what they actually contain:

| fragment | corpus batches |
|---|---|
| `frag-1` … `frag-15` | batches 1–14 (agent-generated, various splits) |
| `frag-16a`, `frag-16b` | batch **15** |
| `frag-16c` | batch **16** (added 2026-08-14) |
| `frag-17`, `frag-18`, `frag-19` | batches 17, 18, 19 |
| `frag-20`, `frag-21` | batches 20, 21 (from `convert_1719.py`) |
| `frag-20-coinage` | 2 patterns coined 2026-08-14 (agent-memory-layer, continual-learning-turn) + rehomed edges |
| `frag-21-coinage` | 4 patterns coined 2026-08-16 (durable-execution, benchmark-trust-crisis, ai-native-org, agent-economy) + rehomed edges |

`seed-work/convert_1719.py` converts batches 16–21 deterministically from the
extraction markdown. If you re-run it, re-run `merge_validate.py` after.

⚠ **When you edit an already-converted extraction file, its fragment goes
stale.** The coinage pass edited files across batches 14, 15, 17 and 19; only
the 17/19 fragments were regenerated, so batch 14/15 edits needed a
supplementary fragment (`frag-20-coinage`) plus one hand-removed stale edge in
`frag-16b`. Check which fragment owns a file before assuming an edit landed.
