# SPIKE extraction — "Production Evals For Agentic AI Systems" (Nishant Gupta, Meta Superintelligence Labs) — FOR REVIEW

Source transcript: `transcripts/gupta-meta-production-evals.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/vljxQZfJ9wY — AI Engineer World's Fair, published 2026-06-25.
`stagingTimestamp` for the artifact and all signals: 2026-06-25 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-gupta-production-evals` | Production Evals For Agentic AI Systems (Nishant Gupta, Meta Superintelligence Labs — AI Engineer World's Fair) | youtube | https://youtu.be/vljxQZfJ9wY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-nishant-gupta` **[registry]**.

## Experts (0 new)

- `exp-nishant-gupta` **[registry]** (batch 8, software engineering tech lead, Meta Superintelligence Labs — training & inference infrastructure) — no new node. This is his second talk in the corpus (first: `ia-aie-gupta-deterministic-infra`). NOT the registry's `exp-sachin-gupta` — different person.

## Companies (0 new)

- `co-meta` **[registry]** — reused; Meta Superintelligence Labs treated as a division of Meta per the batch-8 precedent in `gupta-meta-deterministic-infra.md`.

## Elements (1 new + 1 registry reuse)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-scenario-based-evals` | Scenario-based agent evaluation | concept | harness | Offline agent evaluation built around simulated end-to-end workflows (customer support, code generation, research) rather than single prompts: the agent operates inside the simulated environment and is scored on task completion rate, tool correctness, planning quality, and resource usage — the middle tier of Gupta's eval pyramid between benchmarks and production telemetry |
| **[registry]** `el-agentic-control-plane` | — | — | — | reused (batch 8, coined from this speaker's other talk); here evaluation itself is named a control-plane function — the control plane observes systems, collects telemetry, runs simulations, coordinates human review, and governs the execution plane that performs the work |

Element edges: `el-scenario-based-evals` `IdentifiedInArtifact → ia-aie-gupta-production-evals`, `ExemplifiesPattern → pat-verification-gap` **[registry]**; `el-agentic-control-plane` **[registry]** `IdentifiedInArtifact → ia-aie-gupta-production-evals`.

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-gupta-production-evals`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-meta` **[registry]**.

| slug | domain | name / brief | FormsPattern | OnElement |
|---|---|---|---|---|
| `sig-benchmark-prod-gap-widens` | harness | Meta Superintelligence Labs infra tech lead: offline benchmarks keep improving while production reliability stays unpredictable — benchmarks measure model capability, production measures system behavior (tool failures, API outages, context changes, user variability, long-running workflows), and the gap between benchmark and production performance grows as systems become more autonomous; "high benchmark scores, unreliable production behavior" (paraphrase) is what almost every AI organization is experiencing | `FormsPattern → pat-verification-gap` **[registry]** | — |
| `sig-evals-become-control-plane` | infra | Evaluation is moving from a pre-deployment testing phase to always-running production infrastructure: an evaluation control plane that observes systems, collects telemetry, runs simulations, and coordinates human review, governing a separate execution plane that performs the work — "evaluation is becoming the infrastructure, not testing, not QA" (paraphrase); he names the control/execution-plane separation as where the industry is heading | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-agentic-control-plane` **[registry]** |
| `sig-prod-traffic-is-eval-data` | harness | Production telemetry sits at the top of the evaluation pyramid (above benchmarks and scenario evals): every interaction becomes evaluation data — execution traces, user outcomes, escalations, failures, feedback signals — "the largest and most representative evaluation data any organization will ever have" (paraphrase); humans are reframed from fallback systems to evaluators whose judgments calibrate automated pipelines and expose blind spots | `FormsPattern → pat-verification-gap` **[registry]** | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-reliability-north-star` | Evaluate agents like an SRE, not a researcher: reliability, availability, latency, cost, and recovery are the metric set, each mapping to a business outcome (task completion = value delivered, tool success = operational reliability, escalation rate = human burden, safety violations = risk exposure, recovery rate = resilience) — accuracy is deliberately absent from the scorecard because it is an input to dependable outcomes, not the goal | `HighlightsPattern → pat-verification-gap` **[registry]** | — |
| `ins-behavior-not-answers` | Agentic systems change the eval question from "did the model produce the right answer" to "did the system behave correctly" — planning quality, tool usage, workflow execution, recovery, decision-making. Hallucinations are just one category in a failure hierarchy (memory/retrieval/safety at the base → reasoning, planning, tool-execution errors → multi-agent coordination failures at the top), so evaluating only model output misses most production risk | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-scenario-based-evals` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-gupta-production-evals`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-scenario-driven-evals` | Make offline agent evals scenario-driven, not prompt-driven | Simulate realistic workflows (customer support, code generation, research) as the unit of offline evaluation; let the agent operate inside the simulated environment; measure task completion rate, tool correctness, planning quality, and resource usage (which grows exponentially at scale) rather than answer accuracy | `ReferencesElement → el-scenario-based-evals` |
| `how-always-on-eval-loop` | Run evaluation as an always-on service, instrumented like microservices | Keep the loop running after deployment: production telemetry surfaces issues → humans review edge cases → feedback improves datasets → offline scenarios validate updates. Instrument agent traces like distributed tracing (reasoning paths, tool calls, memory access, execution timelines, state transitions) — traditional logs are insufficient. Monitor continuously for drift: model versions, prompts, tools, and user behavior all change, and no single change looks catastrophic — success rate declines and escalations rise slowly until users complain | `ReferencesElement → el-agentic-control-plane` **[registry]**, `ReferencesElement → el-scenario-based-evals` |

## Dropped

- The evaluation pyramid (benchmarks → scenario evals → production telemetry) as its own Element — folded into `el-scenario-based-evals`'s brief and `sig-prod-traffic-is-eval-data`.
- SRE analogy as an Element — rhetorical frame, captured in `ins-reliability-north-star`.

## Review notes

1. **Caption garbles resolved from official title/registry:** "Meta Super Dangerous Lab" → Meta Superintelligence Labs; "production of ads" → production evals; "Accuracy becomes the only input" → almost certainly "only an input". All quotes are paraphrases of auto-captions.
2. **Same-speaker reuse:** `exp-nishant-gupta` + `co-meta` reused from batch 8 (`gupta-meta-deterministic-infra.md`). The control-plane framing recurs across both talks — this talk extends `el-agentic-control-plane` **[registry]** by naming evaluation as one of its core functions; strengthens that element rather than coining a sibling.
3. **`pat-benchmark-trust-crisis` (UNCOINED candidate) — added evidence, no edge:** `sig-benchmark-prod-gap-widens` is a Meta-infra practitioner stating benchmarks systematically fail to predict production behavior. This is gap-evidence (benchmarks insufficient) rather than gaming-evidence (benchmarks manipulated), so it is moderate support; parked on `pat-verification-gap` per registry briefs.
4. `el-eval-driven-development` **[registry]** adjacent but deliberately NOT edged — Gupta's thesis is evals-as-production-infrastructure (post-deploy, continuous), not evals-driving-development (pre-build); link or merge at reconciliation if central reads them as one.
5. Thin-talk allowance: ~1.1k words, 3 signals per the short-talk bar; the talk is prescriptive framework material, so most content landed in insights/knowhow.
