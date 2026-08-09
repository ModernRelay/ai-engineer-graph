# SPIKE extraction — "The 100-Tool Agent Is a Trap" (Sohail Shaikh & Ankush Rastogi, Prosodica) — FOR REVIEW

Source transcript: `transcripts/shaikh-rastogi-prosodica-100-tool-trap.txt` (auto-captions — quotes are paraphrases, not verbatim; speaker/company names heavily garbled, resolved against the official listing — see Review notes).
Video: https://youtu.be/vh2VGuQ3zhY — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact and all signals: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-shaikh-rastogi-100-tool-trap` | The 100-Tool Agent Is a Trap (Sohail Shaikh & Ankush Rastogi, Prosodica — AI Engineer World's Fair) | youtube | https://youtu.be/vh2VGuQ3zhY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-sohail-shaikh`; `ContributedByExpert → exp-ankush-rastogi`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-sohail-shaikh` | Sohail Shaikh (data scientist at Prosodica; applied AI/NLP, conversational intelligence, RAG) | `AffiliatedWithCompany → co-prosodica` |
| `exp-ankush-rastogi` | Ankush Rastogi (senior data solutions engineer at Prosodica; 10+ years in AI/data engineering/production systems) | `AffiliatedWithCompany → co-prosodica` |

## Companies (1 new)

| slug | name | type | brief |
|---|---|---|---|
| `co-prosodica` | Prosodica | developer | Conversational-intelligence / contact-center voice-and-text analytics vendor; appears here as a production-agent practitioner (captions render it "Presodica") |

## Elements (3 new + 1 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-semantic-tool-routing` | Semantic tool routing | concept | context | "RAG for tools": embed every tool's description into a vector index offline; at runtime embed the user query, nearest-neighbor search, and inject only the top-K (K≈3–5) matching tool schemas into the model call — the model picks from a focused set instead of the full catalog; the router both adds the right tools and removes the wrong ones from the choice set |
| `el-just-in-time-context` | Just-in-time context injection | concept | context | Context-management strategy paired with semantic routing: wait until the query is known, then inject only the context that request needs — lazy loading / JIT compilation applied to the LLM context window; the fat-agent design does the reverse (load everything, then reason). ⚠ merge candidate vs `el-progressive-disclosure` **[registry, batch 2]** |
| `el-bfcl` | Berkeley Function Calling Leaderboard (BFCL) | technology | harness | Public benchmark/leaderboard for LLM function/tool calling; used (with synthetic tool pools scaled to 10→~1,000 tools) as the eval basis for the fat-agent vs router comparison in this talk |

Reused **[registry]**: `el-mcp` — Anthropic's on-demand tool loading via MCP is the ecosystem confirmation the talk leans on. Edge: `el-mcp` `IdentifiedInArtifact → ia-aie-shaikh-rastogi-100-tool-trap`.

Element edges: all three new `IdentifiedInArtifact → ia-aie-shaikh-rastogi-100-tool-trap`; `el-semantic-tool-routing` `UsesElement → el-just-in-time-context`; `el-semantic-tool-routing` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

## Signals (4 new)

All: domain `context`, `SpottedInArtifact → ia-aie-shaikh-rastogi-100-tool-trap`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | Pattern edges | RelevantCompany |
|---|---|---|---|
| `sig-fat-agent-accuracy-collapse` | Benchmarked decay of the "fat agent" (every tool schema in every prompt): ~78% tool-selection accuracy at 10 tools → ~40% at 100 → 13.6% at 741 (roughly one correct call in eight); driver is lost-in-the-middle attention over hundreds of mid-prompt schemas plus confusable similar tools — the design fails as a whole, not because any single tool is badly written ("the architecture is asking the model to solve the wrong problem") | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-prosodica` |
| `sig-fat-agent-token-latency-tax` | The catalog is a per-request tax: 741 tool schemas ≈ 127k tokens before the user's question is even considered; at 100k requests/day that's billions of tokens spent just describing tools; time-to-first-token passes 5 seconds around 500 tools — the demo-fine design degrades into a slow, expensive, hard-to-test monolith as the product grows | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-prosodica` |
| `sig-semantic-router-holds-83` | Same queries, same model, same catalog, routed: retrieving top-K tools by embedding similarity holds accuracy above 83% flat across catalog sizes, with ~1k tokens of tool context (≈99% reduction vs 127k) and near-flat time-to-first-token; measured on BFCL-style tasks plus synthetic tool pools, K swept 3/5/10 (K=5 the recommended default); from the model's point of view it always chooses among a handful | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-prosodica` |
| `sig-jit-tool-loading-ecosystem` | Ecosystem converging on on-demand tool loading: Anthropic's published MCP write-up reports 150k → 2k tokens (98.7% reduction) from on-demand tool loading; open-source MCP Zero explores routing at thousands-of-tools scale across many servers; mainstream agent/SDK issue trackers and builder forums log tool-confusion complaints starting well below 100 tools | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-anthropic` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-catalog-vs-working-set` | The catalog can grow; the model's working set must not — decouple the registered capability surface from the per-request context via retrieval. The router's underrated benefit is subtractive: for "weather in Paris" the flight and hotel tools aren't ranked lower, they simply don't exist in the model's choice set for that request | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-semantic-tool-routing` |
| `ins-tool-selection-is-retrieval` | Tool selection is a retrieval problem, not a reasoning problem: dumping the catalog into the prompt forces the model to solve the wrong problem, so failures as tools are added don't mean the prompts (or model) are bad. Teams with an embedding model and a vector DB already own the infrastructure — the same RAG pattern pointed at tool descriptions instead of documents; a focused sprint, not a 6-month platform rewrite | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-just-in-time-context` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-shaikh-rastogi-100-tool-trap`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-semantic-tool-router` | Build a semantic router for large tool catalogs | Offline: catalog every tool (name, description, schema, owner, version); embed descriptions into a vector index (Chroma/Pinecone/Qdrant/…); re-embed whenever descriptions or schemas change. Per request: embed the query with the same model, nearest-neighbor search, take top-K (start K=5), fetch and inject only those schemas; the agent loop's tool list must come from the router, never a hard-coded catalog. Operate: log every selection, final call, failure, and fallback; eval at K=3/5/10 against a real answer key and pick the smallest K that meets the accuracy target; on router miss widen K, run a second retrieval pass, or fall back to a broader tool group; write descriptions in the words users actually use (intent + action + key entities); monitor rare tools that never score and rewrite their descriptions | `ReferencesElement → el-semantic-tool-routing`, `ReferencesElement → el-just-in-time-context` |
| `how-when-routing-pays` | Route only when the catalog actually hurts | Under ~20 tools a router is unnecessary — static loading is fine and routing is over-engineering; past ~50 tools in a production system the router earns its keep; adopt when prompt size, latency, or tool confusion becomes a measured production problem, not before — the goal is not a more complicated agent, it's to stop forcing the model to reason over irrelevant tools | `ReferencesElement → el-semantic-tool-routing` |

## Dropped

- ToolBench, MCP Zero, Aurelio Labs' open-source semantic-router library, Chroma/Pinecone/Qdrant — pointer mentions (starting points for builders); kept as prose in signals/knowhow, no elements. ("Areilo Labs" in captions ≈ Aurelio Labs, see Review notes.)
- "Skills bench style scenarios" as an eval dataset — possibly `el-skillsbench` **[registry, batch 5, itself flagged]**; caption too garbled to link — prose only.
- Lost-in-the-middle — named mechanism folded into `sig-fat-agent-accuracy-collapse` rather than coined (well-known literature concept, not load-bearing as a node here).
- The flight/weather worked examples and the LinkedIn QR close — illustration/housekeeping.

## Review notes

1. **Name garbles (resolved against the official talk listing):** "Presodica" → Prosodica; "Sohaib Shaikh"/"Suhail"/"Suheel"/"Sohil" → Sohail Shaikh; "Ankush Astogi"/"Ankur" → Ankush Rastogi. Speaker attribution of individual segments (Shaikh = routing/model behavior, Rastogi = system design/production) is per their own intro.
2. **Catalog-size inconsistency in captions:** the max tool count appears as both "741 tools" (13.6% accuracy) and "1041 tools" ("13% at 1041") in different passes over the same chart — slide numbers unverified; I kept 741 in the signal briefs (stated with the precise 13.6%/127k-token figures) and flag 1,041 as the alternative reading.
3. All benchmark figures (78/40/13.6%, 83%, 127k→1k tokens, 5s TTFT) are the speakers' own slide-reported results via auto-captions — treat as practitioner-reported, not independently verified.
4. Anthropic's 150k→2k (98.7%) figure is the speakers citing Anthropic's published MCP on-demand-tool-loading write-up — second-hand but consistent with the known post.
5. `el-just-in-time-context` vs `el-progressive-disclosure` **[registry]**: same family (reveal context only when needed). Coined separately because this talk treats JIT injection as the named counterpart of routing, but a merge at seeding is reasonable — flag carried in the element brief.
6. **No new pattern:** the talk is a clean engineering statement of `pat-harness-over-model` (with the accuracy-collapse signal read as `pat-model-not-bottleneck`: the model was fine, the context architecture wasn't). No material new evidence for the central candidate ledger (`pat-durable-execution`, `pat-benchmark-trust-crisis`, `pat-agent-economy`, `pat-ai-native-org`, `pat-adaptive-*`).
7. Prosodica's own numbers may generalize weakly (synthetic tool pools dominate the large-catalog end) — worth noting if this signal is ever cited quantitatively.
