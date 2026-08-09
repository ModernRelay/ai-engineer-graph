# Local deployment runbook (this machine)

Stood up 2026-07-22. Native RustFS (no Docker) + cluster-booted omnigraph-server.

## Topology

- **RustFS** (S3-compatible object store): `127.0.0.1:9100`, native binary,
  data in `~/.local/share/rustfs-intel-data/`, bucket `intel-graph`.
- **Cluster root**: `s3://intel-graph/clusters/spike-intel` (schema, stored
  queries, policies, graph datasets — applied via `omnigraph cluster apply`).
- **Graph**: `spike` → `s3://intel-graph/clusters/spike-intel/graphs/spike.omni`
  — 1,901 entity nodes + 4,640 edges (136 talks, 538 signals) + 1,966
  embedded transcript chunks (3072-dim, gemini-embedding-2-preview).
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

# semantic / hybrid search over 1,966 transcript chunks
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
