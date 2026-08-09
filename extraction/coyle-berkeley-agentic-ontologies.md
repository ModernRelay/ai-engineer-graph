# SPIKE extraction — "Why Agentic Systems Need Ontologies" (Frank Coyle, UC Berkeley) — FOR REVIEW

Source transcript: `transcripts/coyle-berkeley-agentic-ontologies.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/Sir59K8ZDPU — AI Engineer World's Fair, graph track, published 2026-07-23.
`stagingTimestamp` for the artifact and all signals: 2026-07-23 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-coyle-agentic-ontologies` | Why Agentic Systems Need Ontologies (Frank Coyle, UC Berkeley — AI Engineer World's Fair) | youtube | https://youtu.be/Sir59K8ZDPU |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-frank-coyle`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-frank-coyle` | Frank Coyle (educator, UC Berkeley; 30–35 years in CS, 1980s expert-systems practitioner, early career in neuroscience) | `AffiliatedWithCompany → co-uc-berkeley` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-uc-berkeley` | UC Berkeley | research | University; appears as the speaker's affiliation (registry has `co-ucla` but not Berkeley) |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-neuro-symbolic-ai` | Neuro-symbolic AI | concept | context | Convergence of probabilistic neural systems (LLMs/agents) with formal symbolic representations — ontologies, knowledge graphs, rule systems (Gruber 1993: an ontology is "a formal specification of a shared conceptualization"). The symbolic side supplies the guardrails and inference that keep probabilistic generation on track; framed as the return of 1980s symbolic AI with the scaling problem solved by the neural side |
| `el-owl-rdfs` | RDFS + OWL ontology semantics | technology | context | W3C-lineage machinery that sits *beside* the graph rather than in it: RDFS domain/range typing infers new facts from statements ("teaches has domain teacher" ⇒ Bob teaches Scooter makes Bob a teacher, and a person); OWL transitive properties derive facts never stored (ancestor chains), functional properties act as constraints and identity-resolution (one father ⇒ Bob and BB are the same individual), disjoint classes and enumerated value ranges reject invalid states |
| `el-pydantic` | Pydantic | framework | harness | Python runtime type-validation library; adds typing to an untyped language so agent tool parameters conform to declared types before execution — the "at the door" half of the talk's validation stack |

Element edges: all three `IdentifiedInArtifact → ia-aie-coyle-agentic-ontologies`; `el-neuro-symbolic-ai` `UsesElement → el-owl-rdfs`, `EnablesPattern → pat-context-graphs` **[registry]**; `el-owl-rdfs` `EnablesPattern → pat-verification-gap` **[registry]**.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-coyle-agentic-ontologies`, `SourcedFromSource → source-aie-yt` **[registry]**. Domain `context` except where noted.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-expert-systems-second-act` | Veteran of the 1980s expert-systems boom (companies rose, millions spent, Japan's Fifth Generation project, then the AI winter — symbolic AI couldn't scale, and neural nets waited decades for NVIDIA's GPUs): agentic AI is re-running symbolic AI with the scaling inverted — LLMs supply scale, and ontologies/knowledge graphs return as the formal layer; the convergence now travels under the name "neuro-symbolic AI" | `FormsPattern → pat-context-graphs` | `OnElement → el-neuro-symbolic-ai` |
| `sig-agent-loops-turing-complete` | (domain `harness`) Loops complete Böhm–Jacopini's trio (sequence, selection, iteration) for agents: agentic AI is now Turing-complete — capable of anything computable, and heir to loop pathologies: infinite loops, drift as agents talk to each other, token-cost blowups. Hence deterministic checks must surround the loop | `FormsPattern → pat-harness-over-model` **[registry]** | — |
| `sig-owl-catches-agent-errors` | Concrete agent-error classes formal ontologies catch that are "very tricky" to catch in English/prose rules: a second refund on the same order (functional property), a payout routed to the support rep instead of the buyer (disjoint classes), invented status values like "probably shipped" (enumerated ranges: paid, shipped, refunded — nothing else) | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-owl-rdfs` |
| `sig-cs-degree-guarantee-gone` | (no domain) Educator's ground truth on the talent pipeline: a CS degree "used to be the only game in town — a guaranteed job; now, thanks to AI, it's not", and students are being redirected toward agents/AI as the growth path (soft workforce data point) | `FormsPattern → pat-value-of-judgement` **[registry]** | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-hallucination-is-the-feature` | Hallucination is the feature, not the bug — probabilistic imagination is what LLMs *are* (as it is for humans, who imagine things and then make them real). The fix is not eliminating it inside the model but pairing the neural generator with a symbolic validator outside it: reasoner-backed guardrails keep the LLM honest while preserving what makes it useful | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-neuro-symbolic-ai`, `ReliesOnElement → el-generator-validator-separation` **[registry]** |
| `ins-reasoner-beside-the-graph` | An ontology's value to agents is not just the graph: RDFS/OWL semantics sitting beside it *derive* facts the graph never stored (domain/range typing, transitive closure) and *enforce* constraints (functional, disjoint, enumerations) — inference and guardrails from one formalism, applied to LLM output at the point it touches your records | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-owl-rdfs` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-coyle-agentic-ontologies`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-pydantic-door-ontology-ledger` | "Pydantic at the door, ontology at the ledger" | Surround the agent loop with checks: type-validate tool parameters with Pydantic at the boundary; run tool results through an ontology-backed reasoner before accepting them into records; keep agents side-effect-free until validation passes — no database writes pre-check; on an unreasonable result, loop back to the LLM or bring a human into the loop; remember the LLM can't execute anything — it only proposes tool calls, so the checkpoints are yours to place | `ReferencesElement → el-pydantic`, `ReferencesElement → el-owl-rdfs`, `ReferencesElement → el-generator-validator-separation` **[registry]** |
| `how-build-ontology-pragmatically` | Build ontologies top-down, bottom-up, and second-hand | Top-down: domain experts enumerate the entities, relationships, and properties (the '80s expert-systems method). Bottom-up: mine entities/relations from customer interactions and grow the graph incrementally — graph databases let you attach a property or relationship without restructuring, unlike relational schemas. Reuse existing public taxonomies before inventing: schema.org, FOAF (social), Dublin Core (bibliographic), DBpedia (backs Wikipedia). Treat "ontology" as just a graph data structure plus side-car semantics | `ReferencesElement → el-owl-rdfs` |

## Dropped

- Sister Corita Kent / John Cage pedagogy ("nothing is a mistake... there's only make") and the handwriting-over-typing advice — teaching philosophy, not industry intel.
- AI-history recap (McCarthy, Selfridge, Minsky's Society of Mind, 1956 Dartmouth; Aristotle's categories, Quine) — background; Gruber's 1993 definition folded into `el-neuro-symbolic-ai`.
- The Python/Claude tool-use code walkthrough (while-loop, `stop_reason == tool_use`, parameter formulation) — standard Anthropic API mechanics; its lesson lives in `how-pydantic-door-ontology-ledger`. No `RelevantCompany → co-anthropic` edge: the SDK is incidental here.
- schema.org / FOAF / Dublin Core / DBpedia as Element nodes — kept as guideline prose; coin if they recur.
- codesupreme.ai / Coltrane sign-off — personal plug.

## Review notes

1. Resolved garbles: "Von Quine" = W.V.O. Quine; "Bohm and Jacopini" = Böhm–Jacopini (1966); "web object language" = Web Ontology Language (OWL); "future world project" = Japan's Fifth Generation Computer Systems project (reasonably confident; verify); "coil@burkly" = coyle@berkeley. Quotes are paraphrases.
2. Zero new patterns. The obvious candidate ("ontology-first agents") is `pat-context-graphs` territory per instructions; the validator half was deliberately mapped onto existing `el-generator-validator-separation` **[registry]** instead of coining a near-duplicate element.
3. `sig-cs-degree-guarantee-gone` is a soft, one-line workforce observation parked on `pat-value-of-judgement`; drop the signal (or just the edge) if it fails the bar.
4. `el-pydantic` is mainstream OSS coined per precedent (`el-dspy`, `el-langgraph`, `el-effect-ts`); demote to prose if the bar differs.
5. Batch context: this is the only non-Neo4j talk of the four, arguing the same substrate thesis from an independent academic lineage (expert systems → neuro-symbolic) — useful evidentiary diversity for `pat-context-graphs`, and its verification-side signals land on `pat-verification-gap` rather than the graph pattern.
