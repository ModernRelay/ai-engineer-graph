# SPIKE extraction — "AI on Your Lakehouse: Context Comes in Shapes, Not Queries" (Zach Blumenfeld, Neo4j) — FOR REVIEW

Source transcript: `transcripts/blumenfeld-neo4j-lakehouse-context-shapes.txt` (auto-captions — quotes are paraphrases, not verbatim; "Neo Forj" = Neo4j, "cipher" = Cypher throughout).
Video: https://youtu.be/kRkcNOsRyYg — AI Engineer World's Fair, published 2026-07-23.
`stagingTimestamp` for the artifact and all signals: 2026-07-23 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
~18k-word workshop with Q&A; extraction deliberately limited to the load-bearing thesis content (see Review notes).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-blumenfeld-lakehouse-shapes` | AI on Your Lakehouse: Context Comes in Shapes, Not Queries (Zach Blumenfeld, Neo4j — AI Engineer World's Fair workshop) | youtube | https://youtu.be/kRkcNOsRyYg |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-zach-blumenfeld`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-zach-blumenfeld` | Zach Blumenfeld (AI research engineer, Neo4j; builds/teaches graph context patterns for lakehouse data) | `AffiliatedWithCompany → co-neo4j` |

## Companies (1 new — shared by three talks in this batch)

| slug | name | type | note |
|---|---|---|---|
| `co-neo4j` | Neo4j | developer | Graph database vendor, self-described "graph intelligence platform"; strategic pivot visible across this batch: from ETL-data-into-graph toward ontologies, metadata semantic layers, and virtual-graph views over data left in place. Defined here; referenced by the Eifrem and Chin files. |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-context-shapes` | Context shapes | concept | context | Delivering agent context as pre-designed graph *shapes* rather than raw query access. Three concrete shapes: **table of contents / outline** (deterministic containment tree + typed links over documents, hierarchical URIs as node IDs), **themes** (community-detected document clusters surfacing global groupings), **connections** (metadata semantic layer over the warehouse guiding text-to-SQL joins). The shape spec comes first; the data model is derived from it |
| `el-neocarta` | Neo4j Carta (⚠ name unverified) | product | data-eng | Neo4j Labs metadata-graph tool: an MCP server ingests warehouse metadata only (database → schema → tables → columns + representative values + reference join paths; BigQuery today, Databricks connector in progress) into a graph semantic layer that grounds agent text-to-SQL across hundreds of look-alike tables. No data ETL — data stays in place. Field-team/customer-driven Labs project |
| `el-leiden-community-detection` | Leiden community detection | technology | data-eng | Graph clustering algorithm (refinement of Louvain) that labels densely interlinked node clusters; powers the themes shape — surfacing document groupings deterministically from link structure alone (no LLM in the loop), with a conductance metric for tight/loose linkage and a gamma granularity parameter; the same algorithm Microsoft GraphRAG runs before its LLM community summaries |
| `el-neo4j-cli` | Neo4j CLI + Cypher/GDS agent skills | product | harness | CLI that lets a coding agent run queries directly against Neo4j, shipped with vendor-maintained skill files (current Cypher, graph data science, agent memory, language drivers) so the agent writes modern queries instead of regurgitating years-old Stack Overflow Cypher |

Element edges: all four `IdentifiedInArtifact → ia-aie-blumenfeld-lakehouse-shapes`. `el-neocarta` `DevelopedByCompany → co-neo4j`, `UsesElement → el-mcp` **[registry]**, `EnablesElement → el-semantic-layer` **[registry]**. `el-neo4j-cli` `DevelopedByCompany → co-neo4j`, `UsesElement → el-agent-skills` **[registry]**. `el-context-shapes` `UsesElement → el-semantic-layer` **[registry]**, `UsesElement → el-leiden-community-detection`, `EnablesPattern → pat-context-graphs` **[registry]**.

## Signals (5 new)

All: domain `context` (except `sig-agents-write-cypher-now`: `harness`), `SpottedInArtifact → ia-aie-blumenfeld-lakehouse-shapes`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-neo4j-lakehouse-shapes-workshop` | Neo4j ships a free hands-on workshop/course teaching graph "shapes" as agent context over lakehouses (BigQuery, extendable to Databricks/Snowflake): vector search + text-to-SQL access the data fine, but agents fail on the right *slice* — the fix is shaped graph views (outline, themes, connections), not more query access | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-neo4j`; `OnElement → el-context-shapes` |
| `sig-estate-questions-beat-vector` | Practitioner claim from customer work: point questions ("how do I fix this part?") work with vector/text-to-SQL, but "estate-level" questions — what documentation are we missing, what are we not leveraging, what patterns recur — require traversing the whole data estate; similarity search structurally cannot prove a negative | `FormsPattern → pat-context-graphs` | — |
| `sig-semantic-layer-not-etl` | Neo4j strategy shift: metadata semantic layers (Neo4j Carta) and a just-released virtual-graph preview (pushdown Cypher over SQL) instead of ETL-into-graph; terabyte-scale sync, custom ETL cost, and security posture make copying enterprise data into a graph a non-starter — ETL reserved for genuine graph-compute needs (recursive joins, graph algorithms/embeddings) | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-neo4j`; `OnElement → el-neocarta` |
| `sig-deterministic-doc-graph` | Deterministic, idempotent document-structure graphs (containment tree + next-section + named links, hierarchical URIs) as the lightweight on-ramp vs LLM entity-extraction GraphRAG: no LLM at ingest, faster, stable across reruns, whole-graph rebuild safe; LLM extraction reserved for messy or domain-ontology-heavy corpora (e.g. life sciences) | `FormsPattern → pat-context-graphs` | `OnElement → el-graphrag` **[registry]** |
| `sig-agents-write-cypher-now` | "A lot of us aren't hand-typing our own code line by line anymore": the whole workshop has the agent author every Cypher/GDS query from spec files via the Neo4j CLI + vendor-maintained skills — markedly better than the text2cypher experience of even 6–12 months ago; agents increasingly prefer free-form CLI queries over pre-built shapes as skills accumulate | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-neo4j`; `OnElement → el-neo4j-cli` |

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-shapes-not-queries` | Don't hand the agent a query interface and hope; design the exact view it should see (spec first), then derive the data model backward from that shape. The shape — tree, themes, connection map — is the agent's interface to the estate | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-context-shapes` |
| `ins-graphs-prove-negatives` | Similarity search can only match what exists; the differentiated value of graph context is estate-level reasoning — proving something is missing, finding unused documentation, surfacing mismatches between documented procedure and field reality | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-context-shapes` |
| `ins-ontology-vs-semantic-layer` | Working definitions that cut through the summer's buzzword fog: an *ontology* helps something interpret and reason about the data; a *semantic layer* establishes the consistent agreed-upon terms so the data can be queried accurately. Different jobs, both graph-representable | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-semantic-layer` **[registry]** |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-blumenfeld-lakehouse-shapes`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-spec-first-graph-shapes` | Spec the shape, let the agent write the query | Write a spec doc for the exact view the agent should see (format, arguments, depth parameters); point the coding agent at the spec + Cypher/GDS skills to fill in parameterized queries; keep pre-built shape scripts alongside free-form CLI access — agents glue shapes together for unanticipated questions; have the agent narrate which shapes/steps it used while learning, logs in production | `ReferencesElement → el-context-shapes`, `ReferencesElement → el-neo4j-cli` |
| `how-deterministic-doc-graph-load` | Deterministic document graphs before LLM extraction | Use hierarchical URIs as node IDs so any subtree is scopable by prefix filter (search post-filtered by URI "starts with"); keep the relationship vocabulary tiny (has, links-to) — naming granularity trades query precision against context-window manageability; make loads idempotent so full rebuild is always safe; pair with Lucene full-text + "semantic expansion" (model rewrites the query with synonyms from world knowledge) instead of vendor-locked vector wiring; document/link naming quality is load-bearing for traversal — add LLM assistance at ingest only when structure or link labels are poor | `ReferencesElement → el-context-shapes` |

## Dropped

- Workshop logistics wholesale: Codespaces setup, credentials, QR codes, Wi-Fi/Claude slowness, co-presenters Ben Squire and Ryan (no surnames/content), Graph Academy enrollment flow.
- Virtual graph as a separate Element — one strategy answer plus a passing mention; kept as prose inside `sig-semantic-layer-not-etl`.
- "PageIndex" namedrop (document-navigation inspiration) — no detail; prose only.
- "Karpathy-style knowledge bases" aside — passing; registry already has `el-karpathy-llm-wiki`, no edge warranted.
- "Opus 4.8" model mention — workshop plumbing, and the version number is caption-unreliable.
- pgvector / Genie / Databricks AI search comparisons, the AutoFix fictional scenario details, comeback-ratio metric — scenario color.
- Fraud / anti-money-laundering temporal community-detection use case — pre-AI aside in Q&A.

## Review notes

1. `co-neo4j` is coined here and reused by the Eifrem and Chin files (three Neo4j-affiliated talks in this batch).
2. ⚠ Product name "Neo4j Carta": auto-captions render it "Neoarta"/"Neo Carta"/"NeoAR Carta"/"Neil Carta". Slugged `el-neocarta`; verify the official Neo4j Labs spelling before seeding. Likewise "cipher 2526" read as a Cypher version reference (25/26?) — unresolved.
3. Zero new patterns. Everything here is element-level machinery evidencing `pat-context-graphs`; "context comes in shapes" is a mechanism statement, not a new seed-altitude thesis.
4. Per the extraction brief, this ~18k-word workshop was capped at 5 signals; Q&A yielded guideline material (relationship naming, partial re-sync, index setup) folded into the KnowHows rather than extra signals.
5. `el-leiden-community-detection` is a pre-AI algorithm coined per precedent (`el-personalized-pagerank`, batch 3); drop to prose if the bar differs. The Microsoft GraphRAG contrast overlaps registry `el-hierarchy-summarization` — no edge added (would edit an existing node's neighborhood).
6. `sig-agents-write-cypher-now` parked on `pat-harness-over-model` (vendor-maintained skills + CLI as the deterministic scaffolding that makes agent-authored queries reliable); rehome to `pat-context-graphs` if you read it as adoption evidence instead.
