# SPIKE extraction — "Semantic Blindness: 500,000 Sensors Confused an LLM" (Raahul Singh & Vanč Levstik, Phaidra) — FOR REVIEW

Source transcript: `transcripts/singh-levstik-phaidra-semantic-blindness.txt` (auto-captions — quotes are paraphrases, not verbatim; company name garbled as "Fedra"/"fidra" = Phaidra).
Video: https://youtu.be/EUsPvBeIx70 — AI Engineer World's Fair, published 2026-07-12.
`stagingTimestamp` for the artifact and all signals: 2026-07-12 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-phaidra-semantic-blindness` | Semantic Blindness: 500,000 Sensors Confused an LLM (Raahul Singh & Vanč Levstik, Phaidra — AI Engineer World's Fair) | youtube | https://youtu.be/EUsPvBeIx70 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-raahul-singh`, `ContributedByExpert → exp-vanc-levstik`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-raahul-singh` | Raahul Singh (staff AI research engineer, Phaidra; designed the architecture) | `AffiliatedWithCompany → co-phaidra` |
| `exp-vanc-levstik` | Vanč Levstik (senior engineering manager, Phaidra; production readiness/evals — captions render the name "Vance Kulistik", resolved from the official talk listing) | `AffiliatedWithCompany → co-phaidra` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-phaidra` | Phaidra | developer | Builds AI agents for "AI factories" — data-center/industrial-plant operations: customers converse with their data-center telemetry (chillers, GPUs, power meters) to diagnose day-to-day problems |

## Elements (1 new, 1 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-hierarchy-summarization` | Hierarchy summarization (sub-linear context) | concept | context | Exploiting the tree structure of physical infrastructure (data center → hall → aisle → row → rack → GPU) so LLM context grows with tree DEPTH, not instance count: describe the finite set of root-to-leaf paths instead of enumerating equipment — a 64-GPU and a 460,000-GPU system produce roughly the same-size summary; a planner LLM then emits a structured plan {what to collect, scope subtree, filter} or a name-pattern to execute, never reading raw name lists |
| **[registry]** `el-deterministic-agentic-split` | — | — | — | reused; Phaidra's planner-LLM + deterministic resolver (pre-indexed subtrees, set intersection) is this split — LLM plans, code searches |

Element edges: `el-hierarchy-summarization` `IdentifiedInArtifact → ia-aie-phaidra-semantic-blindness`; `el-hierarchy-summarization` `UsesElement → el-deterministic-agentic-split`; `el-hierarchy-summarization` `ExemplifiesPattern → pat-harness-over-model`.

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-phaidra-semantic-blindness`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany | OnElement |
|---|---|---|---|---|
| `sig-semantic-blindness-at-scale` (domain: context) | "Semantic blindness": at 1 GW AI-factory scale (400k+ GPUs, ~1M equipment nodes, no industry naming standard) every LLM-native approach to resolving user queries against sensor names fails — full name lists saturate context; embeddings can't separate 20-char names differing by one character (Chiller 6 vs 7) so vector RAG recall collapses; repetitive-token frequency penalties shut output off mid-list; sharded parallel LLM calls invent phantom equipment and silently drop real ones. "A product works for all scenarios and doesn't fail silently; a demo just has to work for one" | `pat-harness-over-model` | `co-phaidra` | `el-hierarchy-summarization` |
| `sig-phaidra-flat-cost-100pct` (domain: harness) | Head-to-head evals, same model/data, 3 runs per case: old LLM-search approach degraded 80% → ~30% correctness scaling 64 → 460,000 GPUs; the planner+deterministic-resolver system held 100% across all scales, with zero failures on 66 real cases across 6 production systems; a 1 GW validation pass dropped 116M → 390k tokens (~300x), and per-query cost is flat (~9k tokens) regardless of system size — a 2–3-step pipeline, not an open-ended agentic loop | `pat-harness-over-model` | `co-phaidra` | `el-deterministic-agentic-split` |
| `sig-karpathy-trend-inverted` (domain: harness) | Phaidra ran Karpathy's software 1.0/3.0 trend backwards: legacy software drifts from deterministic 1.0 toward prompted 3.0, but their AI-native system started nearly pure 3.0 (everything in the context window — fastest way to find what's worth building), then matured the parts with known structure into 1.0 code as scale demanded; heuristic — "if you can write down the structure or the rules, it's a 1.0 job", and pure LLM is weakest exactly where systems are large and well-structured | `pat-harness-over-model` | `co-phaidra` | `el-deterministic-agentic-split` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-llm-plans-code-searches` | Keep the LLM on what it's uniquely good at — parsing ambiguous requests, judging where/what to look for, handling never-seen phrasing, synthesizing the human-readable answer — and move everything data-modelable into code: retrieval, exact set logic, counting, dedup across near-identical names, anything that must be 100% reproducible. Structured outputs are the interface: the LLM emits the search plan, deterministic code executes it with perfect recall | `pat-harness-over-model` | `el-deterministic-agentic-split`, `el-hierarchy-summarization` |
| `ins-1-0-tools-ground-the-model` | The endgame isn't replacing model judgment but flooring it: every deterministic function added is "more reliable ground for the LLM to stand on" (their "1.1.0 tools" framing) — develop with software 3.0, productionize by adding software 1.0 for the use cases that earn it | `pat-harness-over-model`, `pat-model-not-bottleneck` | `el-deterministic-agentic-split` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-phaidra-semantic-blindness`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-sublinear-entity-resolution` | Resolve fuzzy queries over massive structured inventories sub-linearly | (1) Model the domain as its natural hierarchy and give the LLM a path-summary of the tree (grows with depth, not width) instead of instance lists; (2) planner LLM converts the fuzzy query into a structured plan — collect-target, scope subtree, filters — via structured outputs; (3) deterministic resolver executes over pre-indexed subtrees (by location, by interaction) with set intersections → perfect recall/accuracy by construction; (4) for very vague queries, have the LLM emit name/data PATTERNS to execute backend-side rather than scan name lists; (5) keep it a 2–3-step pipeline, not a looping agent, for flat cost; (6) eval head-to-head against the naive system on real production cases before shipping | `el-hierarchy-summarization`, `el-deterministic-agentic-split` |

## Dropped

- Karpathy software 1.0/3.0 framing as an Element — attributed framing device; `exp-karpathy` **[registry]** exists but schema has no Signal→Expert edge, so the attribution lives in `sig-karpathy-trend-inverted` prose.
- "AI factories" as an Element — sector descriptor, kept in the company brief.
- Specific query examples ("what chiller is running hot", "GPUs in data hall 11") — illustrations folded into signals/knowhow.

## Review notes

1. Name garbles: "Fedra"/"fidra.ai" = Phaidra (phaidra.ai); "Rahul Singh" vs official "Raahul Singh" — used official spelling; "Vance Kulistik" resolved to Vanč Levstik from the official talk title — **verify spelling before seeding** (weakest name resolution in my set). Contact emails at the end are fully garbled ("Rahul Russell Google at fidra.ai") — not extracted.
2. `pat-harness-over-model` carries all three signals — this talk is about as pure an instance of that pattern's engineering claim as exists (deterministic scaffolding for reliability/cost, model kept for judgment). Considered `pat-model-not-bottleneck` for `sig-phaidra-flat-cost-100pct` but the failure here WAS partly the model's (recall, frequency penalties), fixed in the harness — kept on harness-over-model; the industry-level echo is on `ins-1-0-tools-ground-the-model` instead.
3. Considered coining the "3.0 → 1.0 maturation" inversion as its own element/pattern candidate; it's one talk's framing of `pat-harness-over-model`, so kept as signal + insight only. If other talks repeat the inversion framing, it may deserve an element.
4. The eval numbers (80→30%, 100%, 116M→390k, 66 cases/6 systems, ~9k tokens/query) are vendor self-reported; kept attributed.
