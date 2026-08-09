# SPIKE extraction — "User Signal Dies at the Retrieval Boundary" (Sonam Pankaj, StarlightSearch) — FOR REVIEW

Source transcript: `transcripts/pankaj-starlight-retrieval-boundary.txt` (auto-captions — quotes are paraphrases, not verbatim; this transcript is among the rougher ones of the set).
Video: https://youtu.be/Jx4ZFEAq6bY — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact and all signals: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

Context: thesis — agents reason, act, and retrieve but never *learn*; eval and outcome signal terminates in dashboards instead of feeding back into retrieval. StarlightSearch's answer is "Agent RX", a runtime-experience memory layer with outcome-weighted (utility-score) retrieval.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-pankaj-retrieval-boundary` | User Signal Dies at the Retrieval Boundary (Sonam Pankaj, StarlightSearch — AI Engineer World's Fair) | youtube | https://youtu.be/Jx4ZFEAq6bY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-sonam-pankaj`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-sonam-pankaj` | Sonam Pankaj (CEO & co-founder, StarlightSearch) ⚠ captions open "I'm Surim" — name from the official talk listing | `AffiliatedWithCompany → co-starlight-search` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-starlight-search` | StarlightSearch | developer | retrieval / agent-memory startup (Agent RX runtime-experience layer); ⚠ captions render it "Starling Search" — official listing spelling used |
| `co-pinecone` | Pinecone | developer | vector-database company; appears via a quoted post by its ex-CTO (⚠ attribution garbled, Review note 2) |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-rx` | Agent RX (agent runtime experience) | product | context | StarlightSearch's runtime memory layer that lets agents improve from execution experience without retraining, fine-tuning, or manual prompt engineering: it consumes traces, absorbs eval/outcome verdicts (including human-submitted failure reports via a dashboard), and converts both into retrieval guidance for future runs; contrasts with compile-time optimizers (captions "DS5" ≈ DSPy — lessons baked into the prompt) by improving *while executing*; once enough memories accumulate, validated reasoning is baked into skills. ⚠ also referred to as "reflect" in captions — product naming unresolved (Review note 4) |
| `el-utility-score` | Utility score (outcome-weighted retrieval) | concept | context | Retrieval scoring = semantic similarity to the current task weighted by whether each memory historically helped or hurt task outcomes; outcome becomes a first-class signal in retrieval re-ranking rather than similarity alone; components include a credit/re-ranking hyperparameter (lambda); known failure modes: cold start (pure semantic search until reviews accumulate), utility drift, and noisy review labels making utility noisy |
| `el-memory-as-reasoning` | Memory as reasoning, not facts | concept | context | Store agent memory as outcome-tested *reasoning about tasks* ("if someone asks for a refund, check the settlement first so the customer isn't refunded twice") rather than static facts/preferences ("user prefers dark theme", "call the user by a shorter name"); context is updated per task instead of stuffed; positions memory as the agent's accumulated judgment, distinct from chat personalization |

Element edges: all three `IdentifiedInArtifact → ia-aie-pankaj-retrieval-boundary`; `el-agent-rx` `DevelopedByCompany → co-starlight-search`; `el-agent-rx` `UsesElement → el-utility-score` and `UsesElement → el-memory-as-reasoning`.

Registry element reuse (no new node, edge only): `el-tau-bench` **[registry]** `IdentifiedInArtifact → ia-aie-pankaj-retrieval-boundary` — benchmark for the headline numbers (captions: "towel bench"); `el-agent-skills` **[registry]** `IdentifiedInArtifact → ia-aie-pankaj-retrieval-boundary` — skills as the consolidation target for matured memories.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-pankaj-retrieval-boundary`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-retrieval-fails-not-generation` | context | Claimed failure anatomy for production agents: 85% of AI projects fail to get traction (captions attribute this jointly to Gartner and "McKinsey's 2025 report" — mangled, ⚠ Review note 3), and 73% of pipelines fail at *retrieval*, not generation; quoted post from Pinecone's ex-CTO (captions "Ram Sriram", likely Ram Sriharsha ⚠): "we have been optimizing for the wrong thing… we made wrong answers appear faster and cheaper, but we forgot to make retrieval learn" | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-pinecone` |
| `sig-eval-signal-dies-in-dashboard` | harness | The missing layer between evals and action: observability stacks capture every tool call, LLM completion, and exception; eval suites judge final outputs pass/fail — but none of it feeds back into agent context, skills, or retrieval, so "the eval signal dies in the dashboard" and agents keep failing the same task; today's fix is manual — an engineer reads dashboards, rewrites the prompt, redeploys, upgrades to a more expensive model, restructures the harness, or fine-tunes | `FormsPattern → pat-verification-gap` **[registry]** (extension reading, ⚠ Review note 6) | `RelevantCompany → co-starlight-search` |
| `sig-outcome-weighted-memory-lifts-benchmarks` | context | Reported gains from utility-score memory, no retraining: tau-bench policy-following 66%→76% without skills, 80% with matured memories baked into skills; on multi-step agentic benchmarks (Humanity's Last Exam-style): baseline 35.7 → 47.5 with RAG → 58.2 with other memory systems → 61.3% with theirs; similar trend claimed on BigCodeBench and one unresolved benchmark (captions: "Long TV") — ⚠ all numbers are caption-read, Review note 5 | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-starlight-search` |
| `sig-memory-products-store-preferences-not-outcomes` | context | Category critique of current memory products (LangChain memory, Mem0): they store user preferences, profiles, conversation history — long-lived chat personalization retrieved by embedding similarity alone; they do not learn from outcomes, so they are "chat experience, not self-improving learning systems for production"; stale knowledge persists indefinitely — a dropped SQL column stays in the system prompt forever because nothing exists to retire it | `FormsPattern → pat-model-not-bottleneck` **[registry]** (⚠ concentration, Review note 6) | `RelevantCompany → co-langchain` **[registry]** |

Signal `OnElement` edges: `sig-outcome-weighted-memory-lifts-benchmarks` `OnElement → el-utility-score` and `OnElement → el-tau-bench` **[registry]**; `sig-eval-signal-dies-in-dashboard` `OnElement → el-agent-rx`.

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-close-the-loop-retrieval-learns` | The missing production layer is one that consumes traces, absorbs evals, and converts both into retrieval guidance for future runs — outcomes must become first-class retrieval signals (utility re-ranking) or agents repeat identical failures forever; the standard ReAct loop lists reason/act/retrieve but omits *learn*, and that omission is where the user's signal dies | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-utility-score` |
| `ins-production-memory-is-reasoning` | Production agent memory is a different product from personalization memory: what matters is outcome-weighted reasoning — what to check before acting, which trajectories worked — not who the user is; systems built to remember preferences structurally cannot make an agent better at its job | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-memory-as-reasoning` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-pankaj-retrieval-boundary`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-outcome-weighted-retrieval` | Make retrieval learn from outcomes | Score memories by semantic similarity × historical utility (did this memory help or hurt past executions); submit failures as explicit feedback so trajectories change (demo: "find me a gaming mouse" returned nothing → failure submitted → next run reformulated to wireless mouse and succeeded, with a visibly changed tool-call trajectory); expect a cold-start phase of pure semantic retrieval until reviews accumulate; guard against utility drift and noisy review labels; tune the lambda credit/re-ranking hyperparameter | `ReferencesElement → el-utility-score`, `ReferencesElement → el-agent-rx` |
| `how-bake-memories-into-skills` | Consolidate matured memories into skills | Once enough memories/reviews accumulate on a theme (~10 memories / ~5 reviews in the talk), bake the validated reasoning into a skill so the agent always loads the updated version; this is the mechanism that retires stale system-prompt facts (e.g., a SQL column that no longer exists) without prompt rewrites — the skill, not the prompt, becomes the living document | `ReferencesElement → el-agent-skills` **[registry]**, `ReferencesElement → el-agent-rx` |

## Dropped

- ReAct-architecture explainer — background, prose in `ins-close-the-loop-retrieval-learns`.
- "The similar behavior has been seen in GPT-5.4" — too garbled to carry any claim; dropped entirely.
- Mem0 as an Element — named incumbent, kept as prose (consistent with the daga-file precedent); LangChain carried as `co-langchain` **[registry]** RelevantCompany instead.
- Demo mechanics beyond the trajectory-change point (dashboard walkthrough, repeated benchmark recap mid-demo — the transcript loops the same benchmark paragraph twice) — noise.
- Closing email address ("grace@alishascollection.com") — clearly caption-garbled; color.

## Review notes

1. Name garbles: captions open "I'm Surim, CEO and co-founder of Starling Search"; official listing = Sonam Pankaj, StarlightSearch — official forms used for `exp-sonam-pankaj` / `co-starlight-search`.
2. Quote attribution: "Ram Sriram, the ex-CTO of Pinecone" — Pinecone's former CTO is Ram Sriharsha; the quote is a paraphrase of a social post. Verify person + wording before public-facing use; `co-pinecone` coined for the RelevantCompany edge, no Expert node for the misnamed third party.
3. Stats hygiene: "Gartner reported 85%… it's in McKinsey's 2025 report" is a mangled double attribution, and the 73%-retrieval-failure figure is unsourced in-talk — both kept *inside* the signal brief with flags, not extracted as standalone facts.
4. Product naming unresolved: "Agent RX" (expanded in-talk as "agent's runtime experience") and "reflect" both appear to name the system ("we have built reflect in such a way…"); `el-agent-rx` chosen as the slug — rename centrally after checking the company's site.
5. Benchmark numbers (66→76→80; 35.7/47.5/58.2/61.3) read consistently across the transcript's two recitations, but surrounding benchmark names garble: "towel bench" = tau-bench (`el-tau-bench` **[registry]**), "human last exam" = Humanity's Last Exam, "Big Code Bench" = BigCodeBench, "Long TV" unresolved. Treat exact figures as caption-risk.
6. Pattern concentration: three of four signals form `pat-model-not-bottleneck` — honest but heavy; `sig-eval-signal-dies-in-dashboard` parked on `pat-verification-gap` under an extension reading (verification exists but its verdicts are stranded outside the loop — the gap between verification and *improvement*). If that stretches the pattern, the fallback is `pat-model-not-bottleneck` for it too.
7. Added evidence for the uncoined candidate `pat-adaptive-harness` (registry batch-7/8 ledger): a runtime layer that rewrites retrieval guidance and updates skills from production outcomes is agent scaffolding adapting from live signals — alongside RELAI (batch 8) and Mutagent (batch 8). NOT coined, no edges.
8. `el-agent-sleep-cycle` **[registry]** resonance: bake-memories-into-skills is a consolidation step akin to the KRAFTON sleep cycle (batch 6) — noted for central cross-linking, no edge.
9. Candidate pattern (NOT coined, no edges): "persistent agent memory as a first-class stack layer" — third same-batch data point alongside `iusztin-bouchard-notes-into-memory` and `savkin-nx-genius-with-amnesia`; this talk adds the outcome-learning variant.
