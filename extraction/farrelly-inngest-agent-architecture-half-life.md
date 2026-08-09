# SPIKE extraction — "Your Agent Architecture Has a Half-Life of 6 Months" (Dan Farrelly, Inngest) — FOR REVIEW

Source transcript: `transcripts/farrelly-inngest-agent-architecture-half-life.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/X1kp-ABIIxQ — AI Engineer World's Fair, published 2026-07-21.
`stagingTimestamp` for the artifact and all signals: 2026-07-21 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-farrelly-architecture-half-life` | Your Agent Architecture Has a Half-Life of 6 Months (Dan Farrelly, Inngest — AI Engineer World's Fair) | youtube | https://youtu.be/X1kp-ABIIxQ |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-dan-farrelly`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-dan-farrelly` | Dan Farrelly (CTO & co-founder, Inngest; builds durable-execution infra for AI agents) | `AffiliatedWithCompany → co-inngest` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-inngest` | Inngest | developer | durable-execution platform for AI agents, workflows, and pipelines; positions itself as the "execution layer" of the agent stack |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-three-layer-agent-architecture` | Three-layer agent architecture (execution / context / compute) | concept | harness | Farrelly's mental model for agent harnesses: an execution layer (the "brain" — flow, state, durability, retries, orchestration), a context layer (the "knowledge" — models, prompts, tools, memory; changes fastest), and a compute layer (the "hands" — sandboxes, runtimes, browsers). Each layer has a different half-life (prompts: weeks; models: months; execution: years); coupling them lets the shortest half-life drag the whole system down, so the layers must be decoupled with durable, external state |
| `el-inngest` | Inngest | product | harness | Durable-execution platform for AI agents: durable steps, event triggers, scheduling, agent-to-agent coordination, full session traces, no infra to manage; pluggable context layer (any model/framework/tool) and compute layer (any sandbox/browser); positions the execution layer as the instrumentation point for outcome-based agent scoring |

Element edges: `el-inngest` `DevelopedByCompany → co-inngest`; `el-inngest` `UsesElement → el-three-layer-agent-architecture`; both `IdentifiedInArtifact → ia-aie-farrelly-architecture-half-life`; `el-three-layer-agent-architecture` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-farrelly-architecture-half-life`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-agent-architecture-churn-6mo` | Practitioner consensus stated as a given: any team building agents for more than 6 months has rewritten something, often more than once — a new model, framework version, tool-calling standard, or pattern breaks the architecture; prompts last weeks, models months; only the execution layer can last years if deliberately decoupled | `FormsPattern → pat-harness-over-model` **[registry]** | — |
| `sig-async-agent-architectures-emerging` | The emerging architectures across World's Fair sessions — background agents, dynamic workflows, autonomous loops, "agent factories" — are all long-running, asynchronous, and delegated; they need cron/event/API/human-in-the-loop triggers, sub-agent delegation, and inspectability by both humans and agents; the frameworks of 3 months ago were not designed for them | `FormsPattern → pat-harness-over-model` **[registry]** | — |
| `sig-inngest-durable-execution-vendor` | Inngest markets itself as "durable execution for AI agents" — a dedicated execution-layer vendor selling durability, orchestration primitives, and full-session traces as a product, with context and compute layers explicitly pluggable; second vendor at this World's Fair (after ZenML's Kitaru) planting a flag in the durable-runtime layer | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-inngest`, `RelevantCompany → co-inngest` |
| `sig-sandbox-consensus-state-antipattern` | "Agents need sandboxes" is now settled ("sandboxes are so hot") — but sandboxes are ephemeral and stateless by design, and an anti-pattern is spreading: teams using them for durability, snapshots, or state, then losing state and cobbling together manual checkpointing / log-replay hydration that leaks into every other layer | `FormsPattern → pat-harness-over-model` **[registry]** | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-architect-for-half-life` | Architect for half-life, not for the current stack: models, prompts, and frameworks are the shortest-lived, most swappable parts of an agent system, so the durable investment is the execution layer (state, retries, orchestration, resumability) — get its abstractions right and everything else can be swapped without a rewrite every 6 months | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-three-layer-agent-architecture` |
| `ins-execution-layer-observability-hub` | The execution layer sits between user input and everything the system does — user feedback, actions, and session results all flow through it — making it the natural hub for full-stack traces and for outcome-based agent scoring ("did the triage lead to an engineering action?", "was the PR opened?", "was the report saved?") instead of thumbs-up/thumbs-down | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-three-layer-agent-architecture` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-farrelly-architecture-half-life`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-decouple-agent-layers` | Decouple execution, context, and compute | Think in three layers and keep their abstractions separate; make state durable and external — a 3-hour run cannot hold state in memory or on disk; never use sandboxes for durability (sandbox = hands, execution = brain; execution gives the sandbox its context, sequence, durability); demand resumability (retry/wait/continue from a failed step 38, not from the beginning); use flexible invocation primitives (cron, events, APIs, human-in-the-loop, sync/async/delayed, sub-agents) so harness logic doesn't absorb queues, workers, polling, backoff; require full-session traces from trigger through the whole stack, not just LLM/tool calls | `ReferencesElement → el-three-layer-agent-architecture` |
| `how-outcome-based-agent-scoring` | Score agents on outcomes attached to sessions | Instrument scoring inside the execution layer where inputs, outputs, and the full trace already flow; defer scoring as a task after execution completes; attach real-world outcome events to the session (triage → did the engineering team act? research agent → was the report saved?) instead of thumbs-up/down; close the loop with a scheduled reviewer function that reads execution logs (what ran, what sub-agents fanned out, what workflows were called), evaluates system performance, and adjusts prompts/metrics or reports what to improve | `ReferencesElement → el-three-layer-agent-architecture` |

## Dropped

- The three-function health-check → triage-agent → weekly-reviewer loop example — illustration of the primitives; its reviewer-function idea is folded into `how-outcome-based-agent-scoring`.
- "/loop commands in coding agents" mention — passing reference to the loop-architecture trend already covered by `el-ralph-loop` / the Horthy loops debate **[registry]**; no edge, the talk's own claim is captured in `sig-async-agent-architectures-emerging`.
- "Half-life" as a standalone Element — it is the framing device of `el-three-layer-agent-architecture`, not a separate concept.

## Review notes

1. **Pattern candidate NOT coined — "durable runtime as emerging stack category" now has two data points.** Registry batch-3 flags this candidate from `tahir-zenml-agents-save-button.md` (ZenML/Kitaru). This talk is a second, independent vendor (Inngest) making the same category claim at the same conference: a durable execution/runtime layer below the harness that outlives model/framework churn. Both talks are currently parked on `pat-harness-over-model`, which fits but is broader (deterministic scaffolding generally, not the specific claim that durable execution is becoming a productized stack layer). If reconciliation judges two vendors + the batch-2 verification set sufficient evidence, coin centrally and rehome `sig-inngest-durable-execution-vendor` and `sig-durable-runtime-category-emerging` (tahir). I did not coin per instructions.
2. All four signals link `pat-harness-over-model`; `pat-model-not-bottleneck` appears only via `ins-architect-for-half-life`. The talk supports both readings (churn of the model layer = model is the swappable commodity); add a second `FormsPattern → pat-model-not-bottleneck` edge on `sig-agent-architecture-churn-6mo` if double-linking is acceptable.
3. Vendor-talk discount: `sig-inngest-durable-execution-vendor` and everything about Inngest's product is the speaker's own pitch (he says so — "this is what we built Inngest for"). The signal is framed as a market-positioning observation, which stands regardless of product quality.
4. Caption garbles: "Ingest" throughout = **Inngest** (confirmed against talk title); "the ng-js booth" = the Inngest booth; "contact pipelines" likely = "content pipelines" or "compute pipelines" — unresolved, kept out of extracted text.
5. Signal bar: `sig-agent-architecture-churn-6mo` and `sig-sandbox-consensus-state-antipattern` are practitioner-testimony/consensus observations, not externally dated facts (same caveat as the Daga file). If that fails the bar, the fallback is 2 signals (`sig-inngest-durable-execution-vendor`, `sig-async-agent-architectures-emerging`) + the insights.
