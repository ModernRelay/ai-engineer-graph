# SPIKE extraction — "When All Context Matters: Extended Cache Augmented Generation" (Luis Romero-Sevilla, Orbis) — FOR REVIEW

Source transcript: `transcripts/romero-sevilla-orbis-cache-augmented.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/XovaGv4f39A — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact and all signals: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

Context: very short talk (~860 words) — capped at 3 signals per extraction guidance. Problem shape: a document collection where *every* document is relevant to the user's question set AND the whole collection is replaced frequently. The talk walks RAG → GraphRAG → CAG → the proposed extension (parallel CAG buckets + supervisor).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-romero-sevilla-extended-cag` | When All Context Matters: Extended Cache Augmented Generation (Luis Romero-Sevilla, Orbis — AI Engineer World's Fair) | youtube | https://youtu.be/XovaGv4f39A |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-luis-romero-sevilla`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-luis-romero-sevilla` | Luis Romero-Sevilla (VP of AI, Orbis) ⚠ captions render the employer "the Orbifold operation" — Review note 1 | `AffiliatedWithCompany → co-orbis` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-orbis` | Orbis | developer | company per the official talk listing; ⚠ captions say "Orbifold operation" — verify legal/brand name before public use |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-cache-augmented-generation` | Cache-augmented generation (CAG) | technology | inference | Load the whole document collection into a large context window and persist the model's KV cache (captions: "KB matrix" = KV matrix), so questions are answered from cached context with no per-query retrieval; corpus refresh = reload + re-cache, cheap relative to graph recomputation. Limits: the context window is finite, and overfilling it degrades answer quality |
| `el-extended-cag` | Extended CAG (parallel cache buckets + supervisor) | technology | context | Orbis's extension for all-documents-relevant, fast-churn corpora: shard documents across multiple parallel CAG context buckets — deliberately NOT organized by domain (balanced counts, fewest buckets needed) — and put a smarter supervisor model on top that interrogates each bucket, progressively builds its internal understanding, directs follow-up questions to specific buckets, and synthesizes the final answer; because all caches load in parallel, knowledge-building is significantly faster than GraphRAG construction while staying more accurate than plain vector RAG; KV-cache cost is contained by optimizing how long each cache lives |

Element edges: both `IdentifiedInArtifact → ia-aie-romero-sevilla-extended-cag`; `el-extended-cag` `UsesElement → el-cache-augmented-generation`; `el-extended-cag` `DevelopedByCompany → co-orbis`; `el-cache-augmented-generation` `UsesElement → el-prefix-caching` **[registry]** (⚠ Review note 4).

Registry element reuse (no new node, edge only): `el-graphrag` **[registry]** `IdentifiedInArtifact → ia-aie-romero-sevilla-extended-cag` — evaluated and rejected for fast-churn corpora; `el-context-rot` **[registry]** `IdentifiedInArtifact → ia-aie-romero-sevilla-extended-cag` — window-overfill degradation is the stated reason single-cache CAG fails.

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-romero-sevilla-extended-cag`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-orbis`.

| slug | domain | name / brief | FormsPattern / ContradictsPattern |
|---|---|---|---|
| `sig-churn-breaks-graphrag` | context | For corpora where every document is relevant to the question set and the whole collection is replaced frequently (each document represents an event; collections go obsolete fast), both standard approaches fail: plain RAG can't serve an all-relevant collection through a similarity threshold, and GraphRAG — "an excellent approach" when data is stable — requires an LLM pass over all documents for entity/relationship extraction, making every refresh computationally expensive and slow. Knowledge-graph context has a churn boundary | `ContradictsPattern → pat-context-graphs` **[registry]** (⚠ scoped counter-evidence, Review note 2) |
| `sig-orbis-parallel-cag-supervisor` | context | Orbis's production answer: distribute the corpus across parallel KV-cache buckets with a supervisor model interrogating them; bucket assignment is deliberately order-free because domain-organized buckets fail in practice — with dense cross-document relationships, "the supervisor tends to ignore domains that at first glance seem irrelevant"; net result claimed: knowledge-building significantly faster than GraphRAG with more accurate answers than simple RAG | `FormsPattern → pat-model-not-bottleneck` **[registry]** |
| `sig-context-overfill-degrades` | inference | Independent practitioner corroboration of context rot: "if you fill the context window too much, the quality of the answer gets degraded too" — stated as the structural reason a single big-window CAG can't just swallow the collection and buckets must be sharded; KV-cache cost is acknowledged as real ("can be pretty expensive") and managed via per-cache lifetime | — (OnElement carries it, Review note 3) |

Signal `OnElement` edges: `sig-orbis-parallel-cag-supervisor` `OnElement → el-extended-cag`; `sig-context-overfill-degrades` `OnElement → el-context-rot` **[registry]**; `sig-churn-breaks-graphrag` `OnElement → el-graphrag` **[registry]**.

## Insights (1 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-match-retrieval-to-churn` | There is no one-size-fits-all retrieval: choose the architecture by corpus churn rate and relevance density — stable + deeply interconnected → GraphRAG; fast-replacement + all-documents-relevant → parallel CAG buckets; sparse relevance at scale → plain vector RAG; every strategy trades compute, cost, and speed differently, so fit the solution to the specific problem rather than defaulting to one stack | `HighlightsPattern → pat-context-graphs` **[registry]** (scopes where graph context pays off) | `ReliesOnElement → el-extended-cag`, `ReliesOnElement → el-graphrag` **[registry]** |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-romero-sevilla-extended-cag`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-shard-cag-buckets` | Shard CAG buckets order-free, not by domain | Distribute documents across buckets in no particular order — never by domain/category (supervisors prune seemingly-irrelevant domains and miss dense cross-links); balance document counts so the fewest buckets are needed; load all caches in parallel; let the supervisor explore buckets progressively and direct follow-up questions at specific buckets before synthesizing; contain KV-cache cost by optimizing how long each cache lives | `ReferencesElement → el-extended-cag`, `ReferencesElement → el-cache-augmented-generation` |

## Dropped

- Vector-database / embedding-model explainer (what an embedding is, similarity thresholds) — background, prose.
- "KB matrix" caption garble — read as KV matrix/cache, folded into `el-cache-augmented-generation`.
- Closing contact-details offer — color.

## Review notes

1. Company name: captions say "VP of AI at the Orbifold operation"; the official talk listing says Orbis — `co-orbis` follows the listing. Verify whether the entity is "Orbis", "Orbifold", or an operation/division name before public-facing use.
2. `ContradictsPattern` call on `sig-churn-breaks-graphrag`: this is *scoped* counter-evidence — graph-shaped context is unfit at high churn because of recompute cost, not wrong in general (the same talk calls GraphRAG "excellent" for stable corpora, and `ins-match-retrieval-to-churn` still highlights the pattern). Downgrade to no-edge if counter-edges are reserved for stronger contradictions; kept because the registry values living patterns with honest counter-edges.
3. `sig-context-overfill-degrades` carries no pattern edge: it's a model-behavior corroboration (context rot) rather than an industry-change claim; `OnElement → el-context-rot` records it. If you want an edge, `pat-model-not-bottleneck` is the least-bad fit (long windows exist but aren't usable naively).
4. `el-prefix-caching` **[registry]** chosen as CAG's mechanism edge; the registry already flags `el-prefix-caching`/`el-prompt-caching` as merge candidates — whichever node survives seeding, rehome the `UsesElement` edge.
5. Short talk: no benchmarks, no customer names, no numbers beyond qualitative claims — briefs kept minimal on purpose; "faster than GraphRAG / more accurate than simple RAG" is the speaker's claim, unmeasured in-talk.
