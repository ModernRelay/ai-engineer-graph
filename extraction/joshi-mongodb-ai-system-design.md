# SPIKE extraction — "AI System Design: From Idea to Production" (Apoorva Joshi, MongoDB) — FOR REVIEW

Source transcript: `transcripts/joshi-mongodb-ai-system-design.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/T0HhO4YtTfE — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact, signals, and knowhows: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-joshi-ai-system-design` | AI System Design: From Idea to Production (Apoorva Joshi, MongoDB — AI Engineer World's Fair) | youtube | https://youtu.be/T0HhO4YtTfE |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-apoorva-joshi`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-apoorva-joshi` | Apoorva Joshi (data scientist turned developer advocate, MongoDB; ex-ML for cybersecurity) | `AffiliatedWithCompany → co-mongodb` |

## Companies (1 new)

| slug | name | type | brief |
|---|---|---|---|
| `co-mongodb` | MongoDB | developer | Database company (document DB + Atlas vector search; owns Voyage AI embeddings); appears here evangelizing AI system-design methodology to builders |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-ai-system-design-framework` | Four-phase AI system design framework | concept | harness | Repeatable end-to-end design lifecycle for AI systems: (1) product requirements — quantified solution-agnostic business problem, business/performance constraints, AI's role (critical vs complementary, reactive vs proactive, autonomy ceiling), SMART success metrics; (2) system design — data strategy, retrieval choices, architecture from a pattern menu (RAG, agents, control-flow agentic systems, LLM-as-router, human-in-the-loop, fine-tuning), UX + feedback capture; (3) evaluation before ship + monitoring after; (4) optimization for cost, latency, reliability — with every downstream decision traceable to a constraint gathered upfront |

Element edges: `el-ai-system-design-framework` `IdentifiedInArtifact → ia-aie-joshi-ai-system-design`; `EnablesPattern → pat-value-of-judgement` **[registry]** (it operationalizes spec-first judgment work).

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-joshi-ai-system-design`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-specs-new-code-convergence` | harness | Speakers from Anthropic and OpenAI — the labs most bullish on AI coding — converged in recent talks on "specs are the new code" (paraphrase): the art now is defining product requirements, system design, and eval criteria so you can be confident AI coding agents build the right thing; a MongoDB advocate builds an entire methodology on that premise | `FormsPattern → pat-value-of-judgement` **[registry]** | `RelevantCompany → co-anthropic` **[registry]**, `RelevantCompany → co-openai` **[registry]** |
| `sig-vibe-coding-stops-at-stakes` | harness | Practitioner boundary-drawing: vibe coding works when stakes are low and you can eyeball the output; the moment others depend on the system, "just ship it" is dangerous — because you can no longer eyeball correctness, explicit eval criteria must replace intuition | `FormsPattern → pat-verification-gap` **[registry]** | — |
| `sig-agent-first-overengineering` | harness | Field observation from a developer advocate: jumping straight to (multi-)agents on hype, or letting a coding agent choose your architecture and stack, is the most common failure mode — it yields over-engineered systems that ignore your constraints; regulated workflows mostly reduce to RAG + pre-structured control flow + human-in-the-loop, with autonomy as the exception | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-mongodb` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-spec-is-the-hard-part` | With code generation cheap, the engineering artifact that matters is the spec: the quantified business problem, the latency budget, the cost ceiling, the regulatory constraints — these shape every architectural decision downstream, so gathering them **before** design (not discovering them in production) is where AI-era engineering effort belongs | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-ai-system-design-framework` |
| `ins-eval-first-or-blind` | "You can't improve what you can't measure": guardrails, evaluation (pre-ship) and monitoring (post-ship) are one continuous discipline for probabilistic systems — without measured guardrail-compliance, faithfulness, and domain metrics you can't even *investigate* failures; production adds implicit indicators (human-override rate, review duration) that no offline eval captures | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-ai-system-design-framework` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-joshi-ai-system-design`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-ai-product-requirements` | Nail AI product requirements before any code | Write the business problem user-specific, baseline-quantified, and solution-agnostic (don't prescribe "agent" upfront). Collect business constraints early: data residency, approved clouds/models/vendors, where human review is mandatory (e.g. all denial decisions) — plus performance constraints (latency needs, monthly inference budget, uptime SLAs). Classify AI's role on three axes: critical vs complementary, reactive vs proactive, autonomy level (constraints often cap you at semi-autonomous). Define 1–2 SMART success metrics tied to the business problem (e.g. "urgent claim processing from 2 days to 1 hour within 90 days of launch") | `ReferencesElement → el-ai-system-design-framework` |
| `how-ai-data-strategy` | Design the data strategy source by source | Inventory data sources, where they reside, raw formats, and whether you even have access. Match pipeline cadence to each source's update frequency (annual guidelines vs hourly claims) — stale context is fatal in high-stakes use cases. Process per source: chunk + embed + extract metadata (procedure names, dates) for long documents; strip PII from already-structured records. Pick retrieval per source: vector search with metadata pre-filtering or hybrid search where domain codes defeat pure vectors; exact match on identifiers. Choose the simplest architecture the claim flow supports (RAG + control flow + human-in-the-loop before autonomous agents), then evaluate and iterate | `ReferencesElement → el-ai-system-design-framework` |
| `how-eval-monitoring-optimization` | Layer evaluation, monitoring, and optimization | Define input guardrails (reject invalid/irrelevant/harmful inputs) and output guardrails (invalid = e.g. missing citations), and measure compliance rates — rejection rate, missing-citation rate. Measure faithfulness (is the verdict rooted in retrieved evidence), at least one domain North-Star metric (claim processing time), and system health (cost per recommendation). Post-ship, monitor the same metrics plus implicit indicators: human-override rate (rising = system not doing its job), time-to-review (long = verbose/confusing output). Design user feedback into the UX: verdict overrides with reasons, flagging irrelevant/hallucinated citations. Optimize accuracy via what enters the context window (prompt engineering, reranking, persisted memory); cost/latency via semantic caching and batch processing; reliability via structured outputs (decision + citations always present) | `ReferencesElement → el-ai-system-design-framework` |

## Dropped

- The MDB Health claims-review worked example — explicitly hypothetical; used only to concretize knowhow guidelines, no signals extracted from its specifics.
- The AI-design-pattern taxonomy (RAG / agents / agentic control flows / LLM-as-router / human-in-the-loop / fine-tuning) as separate Elements — folded into `el-ai-system-design-framework`'s brief and the knowhows; coin individually only if later talks make one load-bearing.
- Voyage AI — mentioned as part of MongoDB's offering; prose in `co-mongodb` brief.
- Semantic caching, batch processing, structured outputs as Elements — optimization checklist items, kept in knowhow.
- The GenAI cookbook resource link — not captured (URL not legible from captions).

## Review notes

1. "Apurva" (captions) = Apoorva Joshi per official listing; "wipe code / wipe coding" = vibe coding.
2. "Specs are the new code" is attributed to unnamed "folks from Anthropic and OpenAI… quotes from their talks over the past few months" — kept as a convergence signal without naming individuals; treat the phrasing as paraphrase.
3. `el-ai-system-design-framework` is a talk-branded methodology with a generic name — flag for merge if a canonical systems-design element emerges in later batches; its `EnablesPattern → pat-value-of-judgement` edge is a judgment call (drop if Element→Pattern edges are reserved for tech artifacts).
4. Pattern spread: judgment-over-execution (spec-first), verification-gap (eval-first), harness-over-model (control flow over autonomous agents) — no new pattern tempted; this talk adds soft methodological resonance to all three.
5. No numbers/dated facts in the talk beyond the vendor-quote convergence — it is a framework talk; signal quality leans on practitioner testimony (same caveat as the daga file).
