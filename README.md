# AI Engineer Graph

A knowledge graph of the **AI Engineer World's Fair 2026** talk corpus — 326
talks published April–September 2026 — modelled with the SPIKE framework and
served by [Omnigraph](https://github.com/ModernRelay/omnigraph).

This repository is the complete, loadable definition of the graph:

| path | what it is |
|---|---|
| `schema.pg` | the schema — source of truth for the data model |
| `cluster.yaml`, `policies/` | Omnigraph cluster config and the two Cedar policy bundles |
| `queries/*.gq` | 113 stored queries the server serves (82 reads, 31 mutations) |
| `seed/01-sources.jsonl` … `09-knowhow.jsonl` | every node, one file per type in load order (4,874 nodes) |
| `seed/10-edges.jsonl` | all 15,937 edges between those nodes |
| `seed/chunks/part-01.jsonl` … `part-12.jsonl` | 4,691 transcript chunks + their `PartOfArtifact` edges, ≤400 chunks per part, embeddings added at load time |
| `seed/embed-spec.json` | the embedding spec for the chunks (`gemini-embedding-2-preview`, 3072-d) |
| `omnigraph-config.example.yaml` | client profile and alias pack for the CLI |

The seed files are an exact export of the served graph (last refreshed
2026-09-06). Nothing else is needed to stand the graph up.

## What is in the graph

| type | count | notes |
|---|---|---|
| Pattern | 16 | theses about change; the analytical spine |
| Signal | 1,455 | dated, sourced observations; each forms or contradicts patterns |
| Element | 1,214 | products, technologies, frameworks, concepts, ops practices |
| Insight | 612 | interpretations that highlight a pattern and rely on elements |
| KnowHow | 539 | practices with guidelines, referencing elements |
| Company | 307 | developers, labs, bigtech, investors, media, hardware |
| Expert | 369 | speakers, affiliated with companies |
| InformationArtifact | 345 | 326 talks (`youtube`, with video links) + 19 articles |
| SourceEntity | 17 | publishers; the talks publish via `source-aie-yt` |
| Chunk | 4,691 | ~220-word transcript passages over 303 talks, 3072-d embeddings |
| edges | 20,628 | 15,937 between entities + 4,691 chunk → talk |

### The 16 patterns

Support and counter are `FormsPattern` / `ContradictsPattern` signal counts.

| pattern | kind | support / counter | thesis |
|---|---|---|---|
| `pat-verification-gap` | challenge | 368 / 0 | generation has industrialized, verification has not |
| `pat-harness-over-model` | dynamic | 274 / 20 | the load-bearing engineering sits around the model, and thins as models improve |
| `pat-model-not-bottleneck` | dynamic | 187 / 8 | models are good enough; value and failure moved to the layers around them |
| `pat-context-graphs` | dynamic | 101 / 4 | decision traces, ontology and time as an infrastructure layer above databases |
| `pat-ai-native-org` | dynamic | 82 / 0 | organizations restructure around agent delegation |
| `pat-value-of-judgement` | dynamic | 82 / 0 | as execution industrializes, the durable human edge is judgement |
| `pat-saaspocalypse` | disruption | 77 / 2 | agents dissolve the SaaS presentation layer and per-seat pricing |
| `pat-sovereign-ai` | disruption | 69 / 2 | own the stack end to end; regulation removed optionality |
| `pat-new-cyber-threats` | challenge | 65 / 1 | autonomous exploitation and agentic attack surfaces |
| `pat-agent-economy` | dynamic | 54 / 1 | agents as primary economic actors, and the payment rails being rebuilt for them |
| `pat-accelerated-research` | dynamic | 48 / 2 | agents run research loops autonomously |
| `pat-agent-supply-chain` | challenge | 37 / 0 | skills, MCP servers and hallucinated packages form a new, weaker package ecosystem |
| `pat-benchmark-trust-crisis` | challenge | 25 / 2 | benchmarks decouple from real capability |
| `pat-continual-learning-turn` | dynamic | 23 / 1 | improvement shifts from pre-training scale to post-deployment learning |
| `pat-durable-execution` | dynamic | 22 / 1 | a durable runtime layer below the harness becomes a product category |
| `pat-agent-memory-layer` | dynamic | 19 / 6 | persistent memory becomes a first-class layer of the agent stack |

## The model

**SPIKE nodes:** Signal, Pattern, Insight, KnowHow, Element.
**Supporting nodes:** Company, Expert, SourceEntity, InformationArtifact, Chunk.

The analytical loop is Signals forming or contradicting Patterns; everything
else grounds, interprets, or attributes that loop.

| edge | route | meaning |
|---|---|---|
| `FormsPattern` / `ContradictsPattern` | Signal → Pattern | evidence for / against a thesis |
| `DrivesPattern` / `ReliesOnPattern` / `ContradictsToPattern` | Pattern → Pattern | causality and tension between theses |
| `OnElement` | Signal → Element | what the signal is about |
| `ExemplifiesPattern` / `EnablesPattern` | Element → Pattern | concrete examples or enablers of a thesis |
| `EnablesElement` / `UsesElement` | Element → Element | capability and dependency |
| `HighlightsPattern` / `ReliesOnElement` | Insight → Pattern / Element | what an insight illuminates and rests on |
| `ReferencesElement` | KnowHow → Element | practice grounded in a concrete thing |
| `SpottedInArtifact`, `IdentifiedInArtifact`, `SourcedFromArtifact` | Signal / Element / KnowHow → InformationArtifact | provenance: the talk it came from |
| `SourcedFromSource`, `PublishedBySource`, `ContributedByExpert` | → SourceEntity / Expert | publisher and speaker attribution |
| `RelevantCompany`, `DevelopedByCompany`, `AffiliatedWithCompany` | → Company | who it concerns, who built it, who employs whom |
| `PartOfArtifact` | Chunk → InformationArtifact | which talk a transcript chunk belongs to |

Design choices, all visible in `schema.pg`:

- `slug` is the external identity everywhere. Prefixes: `sig-`, `pat-`, `el-`,
  `ins-`, `how-`, `co-`, `exp-`, `ia-`, `source-`; chunks are `<talk-slug>#<index>`.
- Flat `kind` enums, no subtypes: `PatternKind` `challenge | disruption | dynamic`;
  `ElementKind` `product | technology | framework | concept | ops`.
- `domain` is an enum property on Signal and Element, not a node:
  `training | inference | infra | harness | robotics | security | data-eng | context`.
- Edges are named `VerbTargetType` so direction is unambiguous.
- Embeddings live only on `Chunk.embedding` (`Vector(3072) @embed("text")`).
- `stagingTimestamp` on Signals, KnowHow and artifacts is the talk's publish date.

## Setup

Prerequisites: Omnigraph 0.10.x (`brew install omnigraph` gives the CLI and
`omnigraph-server`; `omnigraph version` should report internal-schema 6), an
S3-compatible object store or a file-backed root, and a Gemini API key for
embeddings (chunk load and query-time `nearest()`).

### 1. Object store

`cluster.yaml` roots the cluster at `s3://intel-graph/clusters/spike-intel`.
A native [RustFS](https://rustfs.com) works locally without Docker:

```bash
brew install rustfs/tap/rustfs
mkdir -p ~/.local/share/rustfs-intel-data
nohup rustfs server ~/.local/share/rustfs-intel-data --address 127.0.0.1:9100 \
  --access-key "$AWS_ACCESS_KEY_ID" --secret-key "$AWS_SECRET_ACCESS_KEY" \
  > ~/.local/share/rustfs-intel-data/rustfs.log 2>&1 & disown
aws --endpoint-url http://127.0.0.1:9100 s3 mb s3://intel-graph      # once
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:9100/      # 403 means it is up
```

For a purely local sandbox, remove the `storage:` line from `cluster.yaml`;
Omnigraph then keeps the cluster under this directory (`__cluster/`,
`graphs/` — both gitignored) and the graph URI below becomes `graphs/spike.omni`.

### 2. Environment

Two gitignored files hold every secret. Source both before any command:
`set -a && source .env.omni && source .env.embedding && set +a`.

```bash
# .env.omni
AWS_ACCESS_KEY_ID=…
AWS_SECRET_ACCESS_KEY=…
AWS_ENDPOINT_URL=http://127.0.0.1:9100
AWS_REGION=us-east-1
AWS_ALLOW_HTTP=true
OMNIGRAPH_SERVER_BEARER_TOKENS_JSON={"act-reader":"…","act-analyst":"…","act-admin":"…"}
TOKEN_ACT_READER=…
TOKEN_ACT_ANALYST=…
TOKEN_ACT_ADMIN=…
OMNIGRAPH_EMBED_PROVIDER=gemini
OMNIGRAPH_EMBED_MODEL=gemini-embedding-2-preview

# .env.embedding
GEMINI_API_KEY=…
```

The three actors are the ones the policies know about (see Roles below).

### 3. Converge the cluster

```bash
omnigraph cluster validate --config .        # an external_blobs WARN is expected
omnigraph cluster plan     --config .
omnigraph cluster apply    --config . --as act-admin   # creates the graph, applies schema, publishes queries
```

### 4. Load the seed

```bash
G=s3://intel-graph/clusters/spike-intel/graphs/spike.omni

# entities: nodes in type order, then the edges (each file replaces its own tables)
for f in seed/[0-9]*.jsonl; do
  omnigraph load --data "$f" --mode overwrite --as act-analyst --yes "$G" || break
done

# chunks: embed each part with Gemini, then merge it (a part stays well under
# the 32 MiB-per-load limit for parsed Chunk rows)
mkdir -p embedded
for f in seed/chunks/part-*.jsonl; do
  omnigraph embed --input "$f" --output "embedded/$(basename "$f")" --spec seed/embed-spec.json &&
  omnigraph load --data "embedded/$(basename "$f")" --mode merge --as act-analyst --yes "$G" || break
done

omnigraph commit list --branch main "$G" | head -1     # the head advances once per load
```

Gemini rate-limits large embedding runs (HTTP 429, "Resource exhausted"); if a
part fails, wait and retry that part. Edge lines pass through `embed` untouched,
and a part already merged must not be merged again (see Load semantics below).

### 5. Serve

```bash
nohup omnigraph-server --cluster s3://intel-graph/clusters/spike-intel --bind 127.0.0.1:8081 \
  > omnigraph-server.log 2>&1 & disown
curl -s http://127.0.0.1:8081/healthz    # {"status":"ok","version":"0.10.0","internal_schema_version":6}
```

The server needs the `AWS_*` variables, `OMNIGRAPH_SERVER_BEARER_TOKENS_JSON`
and `GEMINI_API_KEY` in its environment. Add `--unauthenticated` only for a
throwaway local sandbox.

### 6. Query

Merge `omnigraph-config.example.yaml` into `~/.omnigraph/config.yaml`, then
register the token once: `omnigraph login intel-local` (paste the analyst
token). Every stored query is then an alias:

```bash
omnigraph alias top-patterns
omnigraph alias pattern-signals pat-context-graphs
omnigraph alias pattern-counter pat-harness-over-model      # counter-evidence
omnigraph alias company-footprint co-anthropic              # company ← signals → patterns
omnigraph alias expert-patterns exp-clare-liguori           # expert ← talks ← signals → patterns
omnigraph alias el-dependents el-mcp                        # everything built on MCP, ≤3 hops
omnigraph alias hybrid-search "give the agent a budget, not a token"   # RRF of nearest() + bm25()
omnigraph alias talk-semantic ia-aie-krieger-anthropic-how-anthropic-builds "how do they decide what to unship"
omnigraph alias triage                                      # signals not yet attached to a pattern
```

Direct stored-query and HTTP access work the same way:

```bash
omnigraph query top_patterns_by_signals --profile intel
curl -s -X POST http://127.0.0.1:8081/graphs/spike/queries/recent_signals \
  -H "authorization: Bearer $TOKEN_ACT_READER" -H 'content-type: application/json' \
  -d '{"params":{}}'
```

Writes go through the 31 stored mutations (`queries/mutations.gq`: nine
`add_*` node inserts and 22 `link_*` edge inserts), which are not aliasable:

```bash
omnigraph mutate add_signal --server intel-local --graph spike \
  --params '{"slug":"sig-…","name":"…","brief":"…","stagingTimestamp":"2026-09-01T00:00:00Z","createdAt":"2026-09-01T00:00:00Z","updatedAt":"2026-09-01T00:00:00Z"}'
omnigraph mutate link_signal_forms_pattern --server intel-local --graph spike \
  --params '{"signal":"sig-…","pattern":"pat-verification-gap"}'
```

## Roles

`policies/intel.policy.yaml` (graph-bound) and `policies/server.policy.yaml`
(cluster-bound) define three actors; `main` is a protected branch.

| actor | can |
|---|---|
| `act-reader` | invoke stored read queries; read and export data on any branch |
| `act-analyst` | everything above plus `change`: stored mutations and direct data-plane loads |
| `act-admin` | list the deployment's graphs; the actor for `cluster apply` and maintenance commands |

Anonymous requests get 401; an actor outside a rule gets 403.

## Operating notes

- **Changing schema, queries or policies:** edit the file, lint
  (`omnigraph lint --schema schema.pg --query queries/<f>.gq`), then
  `cluster plan` → `cluster apply --as act-admin` → restart the server. Use
  `@rename_from(...)` on renames; adding a required key needs a graph rebuild.
- **Load semantics:** `--mode overwrite` replaces only the node and edge types
  present in the file (chunks survive an entity overwrite); `--mode merge`
  upserts by `@key`. Edges have no key, so loading the same chunk file twice
  duplicates edges and trips `@unique` on `PartOfArtifact` — never re-load
  chunks that are already in the graph.
- **Verify every write** by comparing `omnigraph commit list --branch main`
  heads before and after; the CLI exit code is not authoritative on remote stores.
- **Full-text indexes on 0.10:** after bulk loads, rebuild them with the server
  stopped so new rows are indexed rather than scanned:
  `omnigraph rebuild-full-text-indexes "$G" --branch main --as act-admin --json`.
- **Binaries:** keep `omnigraph` and `omnigraph-server` on the same minor and
  never point a 0.9 binary at a store touched by 0.10. Check `/healthz` after
  every restart.
- **Refreshing the seed:** `omnigraph export --server intel-local --graph spike`
  streams the whole graph as JSONL. The seed files are that export split by
  node type (sorted by slug, unset optional fields dropped, timestamps as ISO
  time), the entity edges in one sorted file, and the chunk rows with
  `embedding` removed in parts of 400, each chunk followed by its edge.
  Regenerate rather than hand-edit; the sorted layout keeps refresh diffs small.

## Data notes

- Every talk-derived Signal, Element and KnowHow links to its talk
  (`ia-aie-*`, `artifactType: youtube`, `link` is the video URL), and every
  Signal also to the publisher (`source-aie-yt`, "AI Engineer"). Chunks carry the
  talk slug as a `[talk-slug]` prefix in their text.
- Transcripts came from YouTube auto-captions. Quotes in briefs are paraphrases,
  and names and figures can be caption garbles; treat numbers as unverified
  unless a linked source confirms them.
- The 19 `article` artifacts and the first five patterns are the original
  hand-authored seed (April 2026) the corpus was grown from.
- The corpus pipeline that produced the seed — transcripts, per-talk extraction
  notes, deterministic conversion, validation, chunking — lives outside this
  repository; the graph is the deliverable.
