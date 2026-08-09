# SPIKE extraction — "A Practitioner's Guide to Graphs" (Tim Ainge, Good Collective) — FOR REVIEW

Source transcript: `transcripts/ainge-good-collective-graphs-guide.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/3ySF0I5iE_0 — AI Engineer World's Fair, published 2026-07-18.
`stagingTimestamp` for the artifact and all signals: 2026-07-18 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-ainge-graphs-guide` | A Practitioner's Guide to Graphs (Tim Ainge, Good Collective — AI Engineer World's Fair) | youtube | https://youtu.be/3ySF0I5iE_0 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-tim-ainge`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-tim-ainge` | Tim Ainge (Good Collective; practitioner focused on graph data structures and algorithms for AI applications) | `AffiliatedWithCompany → co-good-collective` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-good-collective` | Good Collective | developer | consultancy/studio the speaker represents ("The Good Collective" in captions); AI + graph engineering |

Reused: `co-pinterest` **[registry]** (Pixie paper reference, edge from signal below).

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-schema-guided-graph-extraction` | Schema-guided graph extraction | concept | context | Extracting graphs from unstructured text by giving the extractor an explicit schema (typed nodes/edges instead of free-form triples) plus an ontology of formatting/standardization instructions, then entity-matching with embeddings before creating nodes; consistent types make relationships queryable |
| `el-personalized-pagerank` | Personalized PageRank | technology | context | PageRank variant (random walk with teleport back to a starting node) that surfaces the nodes most strongly related to a seed node in dense graphs; classic reference the Pinterest Pixie paper, contemporary use in HippoRAG-style memory linking |
| `el-subgraph-matching` | Subgraph matching | technology | context | Querying a graph purely on relationship shape — finding structures (design patterns, anti-patterns, malicious transaction shapes, legal argument structures) without knowing any specific node/symbol up front; described as an enabling capability rather than an optimization, not easy to replicate with other tools |
| `el-hipporag` | HippoRAG | framework | context | Memory/retrieval system that uses personalized PageRank and other graph techniques to link memories to questions and answers; cited as the contemporary reference point for PPR in AI systems |

Element edges: all four `IdentifiedInArtifact → ia-aie-ainge-graphs-guide`; `el-hipporag` `UsesElement → el-personalized-pagerank`; `el-schema-guided-graph-extraction` `EnablesPattern → pat-context-graphs` **[registry]**.

## Signals (4 new)

All: domain `context`, `SpottedInArtifact → ia-aie-ainge-graphs-guide`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-graph-code-context-40pct` | In an evaluation on a .NET codebase, retrieving shortest-path subgraphs between two known code nodes as agent context cut tool calls for code search by 40% — intermediate nodes that vector search or symbol lookups would not have found | `FormsPattern → pat-context-graphs` | `OnElement → el-subgraph-matching` |
| `sig-graph-hype-disillusionment` | Practitioner observation: many teams rush into GraphRAG or graph-database rebuilds expecting instant payoff, don't get it, and abandon graphs in a "valley of despair" — the gap between graph hype and graph fundamentals is a live adoption dynamic in the AI-builder community | `FormsPattern → pat-context-graphs` | — |
| `sig-embedding-entity-resolution` | Embedding models have removed the classic pain of entity resolution in graph construction (garlic/minced garlic/garlic cloves): flexible matching without knowing terms in advance, so hybrid graph+AI construction now beats either technique alone | `FormsPattern → pat-context-graphs` | `OnElement → el-schema-guided-graph-extraction` |
| `sig-ppr-resurfaces-in-ai-memory` | 1998-era graph algorithms are resurfacing in AI systems: personalized PageRank, popularized by Pinterest's Pixie recommendations, now powers memory-to-question linking in HippoRAG — graph-native ranking as retrieval infrastructure | `FormsPattern → pat-context-graphs` | `OnElement → el-personalized-pagerank`, `RelevantCompany → co-pinterest` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-schema-before-graph` | The payoff of a graph comes from discipline at extraction time — schema, ontology instructions, embedding-based entity matching — not from the database. Free-form triple extraction produces a graph you "wouldn't get very far with"; typed structure is what makes relationships meaningful and queryable | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-schema-guided-graph-extraction` |
| `ins-graph-native-algorithms-unlock` | Graph-native algorithms deliver retrieval capabilities that vector search cannot: PPR finds important nodes in dense clusters, shortest paths explain relationships between two known nodes (and citation chains to landmark cases never directly cited), and subgraph matching finds things by shape with no known instance — an enabling class, not an optimization | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-subgraph-matching`, `ReliesOnElement → el-personalized-pagerank` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-ainge-graphs-guide`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-schema-guided-extraction` | Extract graphs with a schema, an ontology, and entity matching | Don't ask for raw subject-predicate-object triples; define domain types (recipe → ingredients → quantities, steps → techniques) and use structured outputs. Add ontology instructions (standardize names, units) to the extraction prompt — they matter as much as the schema. Before creating a node, entity-match against existing nodes with an embedding model; unification both deduplicates and strengthens cross-document relationships | `ReferencesElement → el-schema-guided-graph-extraction` |
| `how-subgraph-context-retrieval` | Retrieve subgraphs as agent context | When two nodes are known but the relationship isn't ("checkout broke after we changed the basket constructor"), traverse the code/knowledge graph between them and return symbols/text/summary of the path as context; pick the variant that fits (K-shortest paths, via-node, cheapest weighted path). For shape-only questions, query on relationship structure (subgraph match) with no node IDs at all | `ReferencesElement → el-subgraph-matching` |

## Dropped

- Cypher-vs-SQL comparison, basic graph definitions — tutorial material, no signal content.
- Traditional flow/cost/search algorithms, prediction/similarity/clustering — explicitly deferred by the speaker to the presentation pack.
- The Supreme Court citation example (Miranda v. Arizona found transitively) — folded into `ins-graph-native-algorithms-unlock` as evidence, not its own node.

## Review notes

1. Captions say "Tim Angers from The Good Collective" — normalized to Tim Ainge / Good Collective per the official talk listing. Company name might officially carry "The"; verify before publishing.
2. The second case name in the Supreme Court example is garbled ("Canvas v. Sheba" — possibly Kansas v. Cheever). Left out of any node text; flagging here only.
3. `sig-graph-hype-disillusionment` is the weakest signal (undated community observation). Drop to prose in the artifact description if it fails the bar.
4. The 40% tool-call reduction has no named customer/codebase ("a .NET code base", presumably a Good Collective engagement) — kept because it's the talk's one quantified result.
5. `el-hipporag` and `el-personalized-pagerank` could be collapsed into one element if the registry prefers fewer algorithm nodes; kept separate because HippoRAG is a product-like system and PPR a technique other talks may reference.
