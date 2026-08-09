# SPIKE extraction — "Citation Needed: Provenance for LLM-Built Knowledge Graphs" (Daniel Chalef, Zep AI) — FOR REVIEW

Source transcript: `transcripts/chalef-zep-kg-provenance.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/H7puB0RwJMM — AI Engineer World's Fair, published 2026-07-23.
`stagingTimestamp` for the artifact and all signals: 2026-07-23 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-chalef-kg-provenance` | Citation Needed: Provenance for LLM-Built Knowledge Graphs (Daniel Chalef, Zep AI — AI Engineer World's Fair) | youtube | https://youtu.be/H7puB0RwJMM |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-daniel-chalef`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-daniel-chalef` | Daniel Chalef (founder, Zep AI; leads the team behind the Graphiti temporal graph framework) | `AffiliatedWithCompany → co-zep` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-zep` | Zep AI | developer | enterprise agent-memory infrastructure vendor; builds and maintains the open-source Graphiti framework |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-graphiti` | Graphiti | framework | context | Open-source temporal knowledge graph framework (Zep). Source data enters as verbatim "episode" nodes; entities/relationships/candidate facts are extracted single-shot with a reflection step, then deduplicated/deconflicted; contradicted facts get invalid-dates rather than deletion, with the mutating episodes noted. Search: vector similarity, full-text, and graph-relational ops (BFS) |
| `el-zep` | Zep | product | context | Enterprise agent-memory infrastructure built on Graphiti; derives context/agent memory from many user touchpoints (chat, voice transcripts, email, business data) for multi-agent, multi-user, multi-source scenarios |
| `el-graph-native-provenance` | Graph-native provenance | concept | context | Lineage engineered into the memory data structure rather than logged afterwards: every derived artifact (fact, summary, classification) is a graph node/edge linked back to verbatim source episodes; tracing a fact to its sources is a graph walk; links survive entity merges (merged entity keeps all parents' source links) and fact invalidation (mutating episodes recorded against the fact) |

Element edges: `el-graphiti` `DevelopedByCompany → co-zep`; `el-zep` `DevelopedByCompany → co-zep`, `UsesElement → el-graphiti`; `el-graphiti` `UsesElement → el-graph-native-provenance`; `el-graph-native-provenance` `ExemplifiesPattern → pat-context-graphs` **[registry]**; all three `IdentifiedInArtifact → ia-aie-chalef-kg-provenance`.

## Signals (4 new)

All: domain `context`, `SpottedInArtifact → ia-aie-chalef-kg-provenance`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-zep-provenance-kg` | Zep/Graphiti engineer provenance as graph structure: a fact is a hydrated entity-edge triple linked to verbatim source episodes, so tracing fact→source is a graph walk; entity merges (J. Smith + John Smith) retain all source links from both parents; contradicting data adds an invalid-date to the mutated edge and records the mutating episodes — lineage as an evolving set that survives mutation | `FormsPattern → pat-context-graphs` **[registry]** | `OnElement → el-graphiti`, `el-graph-native-provenance`; `RelevantCompany → co-zep` |
| `sig-llm-synthesis-breaks-source-pointers` | LLM context pipelines break store-a-source-ID lineage that works in deterministic warehouses: synthesis destroys the paper trail (outputs don't appear verbatim in inputs), facts derive from several sources at once, entities merge, and new data invalidates old facts under the pointer; append-only logs become unmanageable at scale. Stylized failure: "patient has a penicillin allergy" synthesized from an EHR, a PDF lab report, and patient-typed intake chat — presented to a doctor without indicating the source was the patient | `FormsPattern → pat-verification-gap` **[registry]** | `RelevantCompany → co-zep` |
| `sig-file-memory-fails-enterprise-provenance` | Zep, asked about the file-based memory wave (markdown/wikis/knowledge bases): markdown "suffers from provenance" — mutating lines in a file destroys the lineage of why changes occurred — and breaks down in multi-agent, multi-user, multi-source server scenarios at enterprise scale; works well for desktop / single-user single-agent use | `FormsPattern → pat-context-graphs` **[registry]** | `RelevantCompany → co-zep` |
| `sig-zep-deterministic-extraction-pipeline` | Zep pushes LLMs out of the graph-construction loop wherever possible: single-shot LLM extraction (entities + relationships + facts) with a built-in reflection step, then traditional IR/NLP for dedup/deconfliction (simhash, entropy measures) — "far cheaper, far faster, far more deterministic"; graph-construction cost/latency named the team's major engineering battle | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-graphiti`; `RelevantCompany → co-zep` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-lineage-is-a-data-structure` | Deriving context is lossy and generative, so lineage cannot be reconstructed or logged after the fact — it must be engineered into the data structure itself, which is a graph keeping sources verbatim and linking everything derived back to them; compliance, veracity assessment, debugging ("why do I have this fact?"), and deletion decisions then fall out of the structure for free | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-graph-native-provenance` |
| `ins-veracity-policy-belongs-to-agent` | The store can expose which parent episodes carry a verified tag, but fact-level veracity is situational business logic: an allergy flag should block a prescription if ANY parent is unverified, while consent-on-file requires EVERY parent verified — identically shaped facts (three parents each), opposite policies. The graph exposes the choice; the agent executes the rule — veracity policy is not baked into the store | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-graph-native-provenance` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-chalef-kg-provenance`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-metadata-projection-veracity` | Tag provenance once at ingestion, filter at retrieval | Tag source episodes with veracity/origin metadata (e.g. EHR, verified) at ingestion; let all subsequently derived entities and facts inherit the tag; retrieve by walking the graph with a tag filter (e.g. only facts from verified clinical sources) — one tagging action supports fact-veracity evaluation forever after; keep any-parent-vs-all-parents policy in the agent's business rules, not the graph | `ReferencesElement → el-graphiti`, `ReferencesElement → el-graph-native-provenance` |
| `how-lineage-driven-deletion` | Drive retention / right-to-be-forgotten deletions through lineage | For deletion requests over derived context, walk lineage from the doomed source data to the facts derived from it; delete a fact only if no remaining episodes support it (a fact with two surviving parents survives; a fact derived solely from the deleted source goes) — the rule is simple precisely because the links exist | `ReferencesElement → el-graph-native-provenance` |

## Dropped

- The Adidas-shoes fact-invalidation example ("Daniel loves Adidas shoes" → returned shoes + nastygram) — illustration, folded into `el-graphiti` brief.
- Q&A on edge-weight/relevancy provenance — Zep traces relevancy-weight changes in a separate data structure OUTSIDE the graph ("not all of the provenance is in the graph"); interesting caveat, kept as review note 4 rather than a node.
- QR codes / repo pointers — no content.

## Review notes

1. Caption garbles resolved against official product names: "graffiti" = **Graphiti**, "Zap" = **Zep**, "penicellin" = penicillin, "deconliction" = deconfliction, "appendon log" = append-only log. All quotes are paraphrases.
2. **Candidate pattern (NOT coined, no edges): "persistent agent memory as a first-class stack layer"** — this talk adds a vendor-infrastructure data point on top of the batch-9 trio (iusztin-bouchard / savkin-nx / pankaj-starlight): Zep sells agent memory as a dedicated enterprise layer, and explicitly argues the filesystem-memory alternative breaks at enterprise scale (`sig-file-memory-fails-enterprise-provenance`). Left for central decision.
3. `el-semantic-episodic-memory` **[registry, batch 2]** resonance: Graphiti's verbatim "episode" nodes are the episodic half of that concept — noted for central cross-linking, no edge added.
4. Caveat from Q&A: Zep's provenance is not 100% graph-resident — relevancy-weight tracing lives in a separate structure. `ins-lineage-is-a-data-structure` states the talk's thesis; this softens it slightly at the edges.
5. `sig-file-memory-fails-enterprise-provenance` is a direct counterpoint to `el-filesystem-agent-state` **[registry, batch 6]** and the agents-md/file-memory wave — noted for central cross-linking (no ContradictsPattern available at the right altitude; no file-memory pattern exists).
6. Company name given as "Zep" / built "Zep AI"; slug `co-zep`.
