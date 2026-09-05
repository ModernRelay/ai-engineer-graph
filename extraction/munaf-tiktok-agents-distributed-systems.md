# SPIKE extraction — "AI Agents Are Just Distributed Systems Now" (Salman Munaf, TikTok) — FOR REVIEW

Source transcript: `transcripts/munaf-tiktok-agents-distributed-systems.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/hD9-V56FNRI — AI Engineer World's Fair, published 2026-08-29.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-29 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a systems engineer's argument that once an agent can call tools and change state, it *is* a distributed system with a **probabilistic coordinator**, and the classic toolkit applies: persist every step, explicit transactions and compensation, idempotency keys because a timeout means *unknown*, circuit breakers and backoff against retry storms, budgets (max turns / parallelism / spend), scoped read/write credentials, approvals bound to parameters, and traces that reconstruct what the agent reacted to. Closing line: smarter models reduce mistakes but "cannot eliminate network failures, stale data or adversarial input — ask what the system lets it do when it is wrong." Caption garbles: "replicate"/"replet" → **Replit**, "item potency" → **idempotency**, "cues" → **queues**, "jet thread" → **chat thread**, "readr access" → **read/write access**, "rights" → **writes**, "provenence" → **provenance**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-munaf-tiktok-agents-distributed-systems` | AI Agents Are Just Distributed Systems Now (Salman Munaf, TikTok — AI Engineer World's Fair) | youtube | https://youtu.be/hD9-V56FNRI |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-salman-munaf`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-salman-munaf` | Salman Munaf (TikTok) | `AffiliatedWithCompany → co-tiktok` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-tiktok` | TikTok | bigtech | ByteDance's short-video platform (parent `co-bytedance` **[b21]** exists as a thin node); the talk is vendor-neutral systems guidance from a TikTok engineer, no TikTok-specific agent facts given |

Reused **[registry]**, edge-only: `co-replit` **[b1]** (the production-database deletion incident — cited as preventable by backups and scoped authority). Referenced, not coined: Air Canada (the chatbot refund ruling — preventable by authoritative source-of-truth retrieval).

## Elements (6 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-probabilistic-coordinator` | The agent as a probabilistic coordinator | concept | harness | Distributed systems have always had services coordinating multi-step workflows, but deterministically — a decision tree mapped out in advance. An agent is a **probabilistic coordinator**: the range of actions it may take varies widely and can have severe consequences unless **confined by deterministic controls**. Text-in/text-out LLMs could only produce a wrong output; agents that call external services, tools and state have moved the architectural boundary beyond the model and can cause side effects in the world — so recognize which external systems, states, credentials and actions are in scope |
| `el-agent-loop-boundary-crossings` | Every step of the agent loop crosses a boundary | concept | harness | Plan (retrieves from data sources) → act (calls APIs, tools, databases) → observe (partial results drive the next action) → persist (may store incorrect data) → decide (may choose a wrong action or start a **retry storm**). Because each step crosses a boundary, **persist every step** — actions taken, context retrieved — so a failed run can recognize where it failed and take a reversible/undo action, and define an **explicit transaction per step** with its compensation for irreversible or unsafe operations (a wrong email to a customer needs a defined corrective email) |
| `el-timeout-means-unknown` | A timeout means unknown, not failure | concept | infra | Tool calls are wrappers around remote APIs, databases and queues, with network delays, timeouts, duplicate requests — and the worst case: the server succeeded but the client saw an error. Humans check the source of truth before retrying; an agent's first instinct is to retry. "Did the refund happen? Would it refund again?" So tools need **request IDs and idempotency keys** so duplicates cause no duplicate side effects, plus a **status lookup** for the previous request; and typed **tool contracts** (request/response schemas, allowlisted operations) with idempotency baked in |
| `el-compensating-transactions-for-agents` | Compensating transactions across system boundaries | concept | harness | Multi-step runs succeed on the first steps and fail later, often across systems — update the internal ticket, email the customer, fail to update the CRM. The whole transaction must be reversible, so define the **compensation operation** for each failure point (an apology or correction email, an undo), the saga pattern applied to agents |
| `el-memory-as-cache-with-provenance` | Memory is state; treat it as a cache with provenance | concept | context | Teams think of agent context "as just context," but **context that can influence an action is state** — it goes stale, conflicts with authoritative data, and corrupts future actions. Two memories: short-term (the chat thread, tied to one execution) and long-term (project files, system prompts, databases, the cache layer). Decide the **source of truth** when they conflict, and treat memory as a cache that carries provenance and is **invalidated when the source of truth changes** |
| `el-agent-circuit-breakers-and-budgets` | Circuit breakers, budgets and parameter-bound approvals | technology | security | Retrying agents cause cascading failures: put **circuit breakers** in front of unhealthy downstreams, exponential backoff, and hard **budgets** — max turns, max parallel calls, max spend — so fan-out and cost are bounded. The default of granting every privilege ("read/write on the whole table") must become **scoped credentials** with separate read and write permissions and tool allowlists — "a harmless model becomes dangerous when it can perform unsafe operations." Human approval must not be blanket: bind it to **action, timestamp, actor, expiration and parameters** — approving a $30 refund must not authorize a $300 one |

Element edges: all six `IdentifiedInArtifact → ia-aie-munaf-tiktok-agents-distributed-systems`.
`el-agent-loop-boundary-crossings` `UsesElement → el-probabilistic-coordinator`, `el-durable-session-log` **[registry]**;
`el-timeout-means-unknown` `UsesElement → el-agent-idempotency` **[registry]**, `el-agent-output-contracts` **[registry]**;
`el-compensating-transactions-for-agents` `UsesElement → el-agent-loop-boundary-crossings`, `el-timeout-means-unknown`;
`el-memory-as-cache-with-provenance` `UsesElement → el-source-of-truth-hierarchy` **[registry]**;
`el-agent-circuit-breakers-and-budgets` `UsesElement → el-agent-scoped-authorization` **[registry]**, `el-agent-execution-traces` **[registry]**;
`el-probabilistic-coordinator` `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-compensating-transactions-for-agents` `ExemplifiesPattern → pat-durable-execution` **[registry]**;
`el-agent-circuit-breakers-and-budgets` `ExemplifiesPattern → pat-new-cyber-threats` **[registry]**;
`el-memory-as-cache-with-provenance` `ExemplifiesPattern → pat-agent-memory-layer` **[registry]**.

Reused elements (no new nodes): `el-agent-idempotency` **[registry]**, `el-agent-output-contracts` **[registry]**, `el-durable-session-log` **[registry]**, `el-source-of-truth-hierarchy` **[registry]**, `el-agent-scoped-authorization` **[registry]**, `el-agent-execution-traces` **[registry]** (the trace must cover model, prompt, tool requests/responses, errors, retrieved context, writes and approvals — "logs are not enough").

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-munaf-tiktok-agents-distributed-systems`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-tiktok`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-agents-are-distributed-systems-now` | harness | The moment an LLM can run a loop, call external services and change state, "it has turned into a distributed system" with a probabilistic coordinator, and the architectural boundary has moved beyond the model. The Replit production-database deletion and the Air Canada chatbot refund were preventable by systems thinking — backups, scoped authority, authoritative source-of-truth retrieval — not by a better model | `FormsPattern → pat-harness-over-model` **[registry]**; `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-probabilistic-coordinator`, `el-agent-loop-boundary-crossings` |
| `sig-timeouts-mean-unknown-so-tools-need-idempotency` | infra | A refund tool times out — did it happen? An agent's first move is to retry, so duplicate side effects follow unless every tool carries request IDs, idempotency keys and a status lookup, and retry storms are bounded by circuit breakers, exponential backoff and max-turns/parallelism/spend budgets. The durable-runtime concerns (retries, idempotency, compensation, budgets) arrive as a checklist from a large-scale systems shop | `FormsPattern → pat-durable-execution` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-timeout-means-unknown`, `el-agent-circuit-breakers-and-budgets`, `el-agent-idempotency` **[registry]** |
| `sig-context-that-drives-action-is-state` | context | "When context can influence an action, it's state" — it goes stale, conflicts with authoritative data and corrupts later actions. Short-term (thread) and long-term (files, prompts, databases, cache) memories need an explicit source-of-truth decision on conflict, and memory should be a provenance-carrying cache invalidated when the source of truth changes. Memory management framed as cache-coherence, from the systems side | `FormsPattern → pat-agent-memory-layer` **[registry]** | `OnElement → el-memory-as-cache-with-provenance`, `el-source-of-truth-hierarchy` **[registry]** |
| `sig-approvals-bound-to-parameters-not-blanket` | security | Teams start by granting agents every privilege; instead: scoped credentials with separate read/write, tool allowlists, and approvals bound to action, timestamp, actor, expiration and the exact parameters — a $30 refund approval must not become a $300 one. The same "budget, not a token" conclusion as Anthropic's CI team, reached from distributed-systems practice | `FormsPattern → pat-new-cyber-threats` **[registry]**; `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-agent-circuit-breakers-and-budgets`, `el-agent-scoped-authorization` **[registry]** |
| `sig-smarter-models-cannot-eliminate-network-failures` | harness | The closing claim: model capability matters and smarter models reduce mistakes, "but it cannot eliminate network failures, stale data or adversarial input." The architecture must be able to bound, observe and recover from the agent's actions — tool contracts with idempotency, source-of-truth decisions, retry policies and rate limits, permissions, traces, recovery paths — "ask what the system lets it do when it is wrong" | `FormsPattern → pat-model-not-bottleneck` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-probabilistic-coordinator`, `el-agent-execution-traces` **[registry]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-ask-what-the-system-lets-it-do-when-wrong` | The durable reframing is to stop asking whether the model will be right and start asking what the surrounding system permits when it is wrong: the coordinator is probabilistic by nature, so correctness has to be a property of the deterministic controls — contracts, idempotency, compensation, budgets, scoped credentials, parameter-bound approvals — not of the model. The same conclusion the batch's security and runtime talks reach, derived here from three decades of distributed-systems failure modes | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-probabilistic-coordinator`, `el-agent-circuit-breakers-and-budgets`, `el-timeout-means-unknown` |
| `ins-agent-loops-need-saga-semantics` | Each step of plan/act/observe/persist/decide crosses a boundary and can leave the world half-changed, so an agent run is a distributed transaction: persist every step, make every tool idempotent, define the compensation for every irreversible action, and treat memory as a cache with provenance. That is the durable-execution layer's requirements list written from first principles — which suggests why the runtime vendors in this batch are converging on it | `HighlightsPattern → pat-durable-execution` **[registry]** | `ReliesOnElement → el-agent-loop-boundary-crossings`, `el-compensating-transactions-for-agents`, `el-memory-as-cache-with-provenance` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-munaf-tiktok-agents-distributed-systems`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-apply-distributed-systems-thinking-to-agents` | Bound, observe and recover — the systems checklist for agents | Map the external systems, states, credentials and actions in the agent's reach; **persist every step** of the loop (actions and retrieved context) so failures are locatable and reversible; define an **explicit transaction and compensation** for every step that has side effects across systems (ticket, email, CRM); treat a **timeout as unknown** — give every tool request IDs, idempotency keys and a status lookup so retries cause no duplicate side effects; write typed **tool contracts** with allowlisted operations; put **circuit breakers** and exponential backoff in front of downstreams and set **max turns, max parallelism and max spend**; treat context that influences action as **state** — decide the source of truth on conflict and invalidate memory when it changes; grant **scoped credentials** with separate read/write and tool allowlists instead of blanket access; bind every human approval to action, timestamp, actor, expiration and parameters; and trace the model, prompt, tool calls, responses, errors, retrieved context, writes and approvals so the team can reconstruct what the agent reacted to | `ReferencesElement → el-agent-loop-boundary-crossings`, `el-timeout-means-unknown`, `el-compensating-transactions-for-agents`, `el-memory-as-cache-with-provenance`, `el-agent-circuit-breakers-and-budgets` |

## Dropped

- **The chatbot → production-system history** — folded into `el-probabilistic-coordinator`.
- **The Air Canada case** — referenced in prose, not coined.

## Review notes

1. **A vendor-neutral, first-principles statement of `pat-durable-execution`'s requirements** (persist, idempotency, compensation, budgets) alongside the batch's three vendor products (Navan's map, Warp Oz, Docker spx) and Louf's build-it-yourself runtime — the demand-side and supply-side of the layer now sit in the same batch.
2. **`sig-approvals-bound-to-parameters-not-blanket`** independently matches Malhotra/Anthropic's "budget, not a token" and Aggarwal/Decawork's short-lived parameter-bound capabilities — three same-batch arrivals at *approvals must be scoped to parameters*. Recorded in the registry's guard-outside-the-agent cluster.
3. **`co-tiktok` coined as `bigtech`** with a pointer to the thin `co-bytedance` (b21); review may merge.
4. **⚠ Verify before seeding:** the speaker's exact role at TikTok (not stated) and the Air Canada / Replit incident descriptions as recounted.
