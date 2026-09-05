# Intel Explorer — design for a bespoke graph explorer on Orbit

**Status: proposal** (2026-08-19). A separate web React app for exploring the
SPIKE intelligence graph visually — thesis-first, evidence-aware, provenance-
deep-linked — built on [Orbit](https://github.com/ModernRelay/orbit)
(`~/code/orbit`, `0.15.0`).

## Why Orbit, and why this is mostly assembly

Three facts make this a composition job rather than a build:

1. **Orbit ships a first-party Omnigraph adapter.** `@modernrelay/orbit-omnigraph`
   streams a graph via `og.export` (one NDJSON pass) into a typed, atomic
   replace-ingest, parses `.pg` schemas, generates TypeScript attr types from
   `schema.pg`, and wires stored queries as a `SearchService`. Its pinned SDK
   (`@modernrelay/omnigraph@0.9.0`) matched our server exactly at design time.
   **Update 2026-09-05:** the server is now omnigraph **0.10.0** (in-place
   upgrade, storage format v6 unchanged). The 0.9.0 SDK was verified against
   it with the explorer's live Playwright suite (export stream, deep links —
   3/3): the routes it uses (`/healthz`, `POST /graphs/{id}/export`) are
   unchanged. 0.10 removed legacy response aliases elsewhere and is not
   rolling-compatible in general, so bump the SDK/adapter to the 0.10 line
   when Orbit ships it rather than mixing further.
2. **The scale is trivial for it.** Orbit's envelope is 100K+ nodes; our
   entity graph is ~3.9K nodes / ~11.8K edges. Everything interactive —
   crossfilter, timeline brushing, semantic zoom — stays instant.
3. **The analyst UI is packaged.** Search, timeline, histogram, table,
   inspector, legend, minimap, context menu, selection actions — 13 headless-
   styleable components wired through one `GraphProvider`. The bespoke work is
   the *SPIKE semantics*, not the widgets.

## What "bespoke" means here — the SPIKE visual grammar

The generic graph explorer shows nodes and edges. This one must show **theses
and evidence**:

| SPIKE concept | Visual encoding |
|---|---|
| Pattern (16) | Large, always-labeled anchors; sized by `FormsPattern` in-degree |
| Signal → Pattern support | Edge tinted **support green** (`FormsPattern`) |
| Signal → Pattern counter | Edge tinted **counter red** (`ContradictsPattern`) — contested patterns visibly bicolored at a glance |
| Contested-ness | Pattern ring split by support/counter share (custom `renderNodeLabel` badge) |
| Node type (10 types) | Categorical palette + `GraphLegend` with row-click filtering |
| Element `kind`, Signal `domain` | Secondary legends (enum unions come typed from codegen) |
| Provenance (`SpottedInArtifact`, `PublishedBySource`, …) | Dimmed by default; revealed in Provenance view |
| Evidence over time | `GraphTimeline` over `Signal.stagingTimestamp` — brush + playback replays the corpus accruing evidence Jul→Aug 2026 |
| Talk (InformationArtifact) | Inspector deep-links to the `youtu.be` URL; chunks reachable via server-side semantic search (below) |

## Architecture

```
┌─────────────────────────── intel-explorer (new repo) ───────────────────────────┐
│                                                                                  │
│  React 18 + Vite + TS (strict)                                                   │
│  ┌────────────┐  ┌───────────────────────────────┐  ┌─────────────────────────┐  │
│  │ ViewPresets │  │ <GraphProvider> + <Graph/>    │  │ Panels                  │  │
│  │ (Thesis /   │  │  orbit-react + engine-cosmos  │  │  Inspector (bespoke     │  │
│  │  Timeline / │  │  styling: SPIKE grammar       │  │   renderers per type)   │  │
│  │  Company /  │  │  scope/expand/folds           │  │  Search ×2 (entity +    │  │
│  │  Provenance)│  │                               │  │   "ask the corpus")     │  │
│  └────────────┘  └───────────────────────────────┘  │  Table/Histogram/Legend │  │
│                                                      └─────────────────────────┘  │
│                    browser talks ONLY same-origin /og/*                           │
└───────────────────────────────────┬──────────────────────────────────────────────┘
                                    │  BFF proxy (dev: vite proxy; prod: ~50-line
                                    │  node/hono server) — injects TOKEN_ACT_READER,
                                    │  allows ONLY read routes (export, read queries)
                                    ▼
                     omnigraph-server http://127.0.0.1:8081
                     s3://intel-graph/clusters/spike-intel  (graph `spike`)
```

**Transport is the one hard rule.** `omnigraph-server` ships no CORS and uses
static bearer tokens; the adapter *enforces* this by accepting only a
preconfigured client in its browser entry (authenticated construction lives in
`orbit-omnigraph/server`, gated out of client bundles). So the app follows the
adapter's intended same-origin BFF pattern: dev = Vite proxy `/og` →
`127.0.0.1:8081` with the reader token injected proxy-side; prod = a tiny
server that does the same and refuses mutation routes. **Only `act-reader`
ever reaches the BFF config** — the explorer is read-only by construction.

## Data plan

**Load the entity graph; exclude chunks.** A partial export
(`typeNames`: the 9 entity node types + 22 non-`PartOfArtifact` edge types)
loads ~3.9K nodes / ~11.8K edges in one streamed pass. Chunks stay server-side
deliberately: 3.6K chunks × 3072-dim vectors is megabytes of floats the
browser never needs, and `PartOfArtifact` would double the edge count for no
visual value. The adapter records the partial-load `typeNames` subset in its
revision stamp, and `driftPolicy: 'retry-once'` handles a batch landing
mid-load; the status bar shows the loaded `dataRef` (branch + head) with a
refresh button for after new batches load.

**Typed attrs from the schema.** `orbit-omnigraph-codegen` over `schema.pg`
emits a committed, diff-stable `omnigraph-types.generated.ts` — Signal/Pattern
/Element attr interfaces with enum string-literal unions (`kind`, `domain`),
regenerated only when `schema.pg` changes (fingerprint in the header).

**Client-side enrichment at ingest** (the demo app's proven pattern): wrap the
ingest session to compute per-node degree and per-Pattern support/counter
counts while lines stream (edges arrive before nodes in export order, so
counts are complete before any node lands). These drive node sizing and the
contested-ness badge without server round-trips.

## Search — two boxes, two systems

1. **Entity search** (`GraphSearch` + `createOmnigraphSearchService`): finds
   nodes *in the loaded graph* and focuses them. Requires one small server-side
   addition — a stored query with a score column and bare-variable projections,
   because the existing `signal_hybrid` returns scalar columns only:

   ```gq
   // queries/explorer.gq  (new; add to cluster.yaml, then cluster apply)
   query explorer_search($q: String)
   @description("Explorer entity search: RRF over names/briefs, whole-node rows")
   {
       match { $s: Signal }
       return { $s, score }
       order { rrf(bm25($s.name, $q), bm25($s.brief, $q)) }
       limit 20
   }
   // + siblings for Pattern / Element / Company / Expert, or one per type
   // wired with the adapter's typeOf mapping { '$s': 'Signal', ... }
   ```

   The adapter qualifies every result id through the same `encodeSourceId`
   codec the loader uses, so activation focuses the exact loaded node. Search
   queries are constrained to loaded types, which sidesteps the adapter's
   documented partial-load `'not-loaded'` caveat entirely.

2. **"Ask the corpus"** (bespoke panel): semantic/hybrid search over the 3.6K
   transcript chunks that we deliberately did *not* load — via BFF invoke of
   the existing `related_chunks` / `hybrid_chunks` stored queries (server-side
   `nearest()` embeds the question; `GEMINI_API_KEY` stays on the server).
   Results render as chunk-text cards; the `[talk-slug]` prefix maps each hit
   to its `ia-aie-*` artifact client-side, and clicking **focuses that talk's
   node in the graph**. RAG-grade navigation with zero vectors in the browser.

## The four view presets

Orbit is declarative — a "view" is just a props preset (scope + styling +
which panels are docked), not a route. One loaded graph, four lenses:

1. **Thesis map** (default) — scoped to Patterns + Signals with pattern
   edges; support/counter tinting; contested badge; `GraphLegend` on node
   type. The graph-shaped version of `top-patterns` + `contested`.
2. **Evidence timeline** — same scope + `GraphTimeline` docked on
   `stagingTimestamp`; brushing crossfilters the graph; playback replays
   evidence accumulation (the corpus's July→August story, watchable).
3. **Company footprint** — pick a Company (search or legend); scope-isolate
   its `RelevantCompany` signals and their patterns — the `company-footprint`
   alias as an interactive neighborhood. Same preset generalizes to Expert.
4. **Provenance** — talk-centric: an InformationArtifact with its signals,
   elements, experts, and source; provenance edges undimmed; inspector shows
   the YouTube link and per-talk stats. Entry point from "ask the corpus" hits.

Bespoke `GraphContextMenu` actions stitch the lenses together: *isolate
neighborhood*, *show counter-evidence* (scope to `ContradictsPattern`
incidents), *open talk on YouTube*, *copy slug* (for `omnigraph alias` CLI
follow-up). Deep-linkable view state makes any investigation a shareable URL
(`?view=thesis&focus=pat-agent-memory-layer`); undo/redo comes free.

## The inspector is the bridge to the corpus

`GraphInspector` with per-type bespoke renderers is where graph meets prose:

- **Signal** — name, full `brief`, domain chip, its pattern edges labeled
  support/counter, its talk (linked), its companies.
- **Pattern** — brief, kind, support/counter counts + a mini-list of counter
  signals (the graph answer to `pattern-counter`).
- **InformationArtifact** — YouTube link, expert(s), signal count, "search
  this talk" shortcut that pre-filters "ask the corpus" to the talk slug.
- **Company/Expert** — affiliations, footprint jump.

## Repo layout & stack

New repo `intel-explorer` (separate app, per requirement — not a package in
either existing repo):

```
intel-explorer/
├── src/
│   ├── main.tsx  app.tsx           # GraphProvider + Graph + dock layout
│   ├── views/                      # the 4 presets (scope+styling+panels)
│   ├── styling/spike.ts            # the visual grammar (one module)
│   ├── panels/  inspector/         # bespoke renderers, ask-the-corpus
│   ├── data/load.ts                # createOmnigraphSource wiring + enrichment
│   └── omnigraph-types.generated.ts
├── server/bff.ts                   # prod proxy (~50 lines; reads .env.omni)
├── e2e/                            # Playwright smoke on the real engine
├── src/**/*.test.tsx               # jsdom + FakeEngine integration tests
└── vite.config.ts                  # dev /og proxy, token injected

deps: @modernrelay/orbit-{react,core,engine-cosmos,omnigraph}@0.15.x,
      @modernrelay/omnigraph@0.9.x, react@18, react-dom@18
```

**Testing without WebGL** is an Orbit design goal: the `FakeEngine` seam lets
view-preset and inspector logic run in plain jsdom; a small **recorded export
fixture** (a scoped subset of the real graph, committed) makes CI hermetic —
no server, no tokens. Playwright covers load-against-live and the cosmos
engine path.

## What this needs from intel-graph (small, additive)

1. `queries/explorer.gq` — the score-column search queries above; register in
   `cluster.yaml`, `omnigraph lint`, `cluster apply` (revision bump only).
2. Nothing else. Export, read queries, and hybrid chunk search already exist;
   the reader token already has exactly the needed rights.

## Phases

| Phase | Scope | Exit criterion |
|---|---|---|
| **P1 — walking skeleton** | Repo, BFF proxy, partial export load w/ enrichment, codegen types, Thesis map styling, GraphSearch on `explorer_search`, stock toolbar/minimap/legend/tooltip | Live graph renders with support/counter tinting; search focuses nodes |
| **P2 — SPIKE lenses** | Inspector renderers, the 4 view presets, context-menu actions, timeline view, deep-linkable state | An investigation (e.g. "show me `pat-agent-memory-layer`'s counters and their talks") is 3 clicks and a shareable URL |
| **P3 — corpus bridge + polish** | "Ask the corpus" panel → focus-in-graph, drift/refresh UX, dark/light themes, SVG/PNG export, fixture-based CI + Playwright | Semantic question → chunk hits → talk node → provenance view, end to end |

## Open questions

- **Hosting**: local-only (BFF reads `.env.omni` on this machine) vs deployed
  read-only mirror. Local-only is P1; nothing in the design blocks deploying
  the BFF + a token-scoped reader later.
- **Chunks in-graph, ever?** Current answer: no — inspector + ask-the-corpus
  covers them. Revisit only if a per-talk "chunk constellation" view earns it.
- **Live updates**: batches land ~daily; a refresh button + drift stamp is
  enough. No streaming/websocket work warranted at this cadence.
