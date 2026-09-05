# SPIKE extraction — "Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons" (Kanish Manuja, Twilio) — FOR REVIEW

Source transcript: `transcripts/manuja-twilio-llm-gateways.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/zrZ1amZBSPw — AI Engineer World's Fair, published 2026-08-28.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a Twilio principal engineer on the system behind "Something went wrong, please try again": an LLM gateway is a fight between **availability, latency, guardrails and cost** — under degradation you cannot maximize all four, so the gateway must expose the levers. Classic retries and circuit breakers don't fit LLMs (retries eat the latency budget; breaking when a second provider is healthy is wrong): use per-request fallback with a normalization layer, know that streaming forfeits fallback mid-stream, and give the fallback provider *more* headroom. Track P99 per model per route, set timeouts per model class ("a reasoning model's normal is a chat model's outage"), fix reasoning levels, hedge the tail. Guardrails are unreliable dependencies too: fail-open or fail-closed by the worst case you can live with. And "they don't want a central gateway, they want centralized governance." Caption garbles: "Kanesh" → **Kanish**, "LMS" → **LLMs**, "undeterministic" → **non-deterministic**, "government" → governance.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-manuja-twilio-llm-gateways` | Productionizing LLM Gateways: Architecture, Tradeoffs and Hard Lessons (Kanish Manuja, Twilio — AI Engineer World's Fair) | youtube | https://youtu.be/zrZ1amZBSPw |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-kanish-manuja`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-kanish-manuja` | Kanish Manuja (Principal Engineer, Twilio) | `AffiliatedWithCompany → co-twilio` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-twilio` | Twilio | developer | Communications platform; runs production LLM gateways serving mixed workloads (embeddings, classification, chat, reasoning) with per-request cross-provider fallback; the talk's lessons are Twilio's incident scars |

Referenced, not coined: the model providers (unnamed), "OpenAI API compatible format" as the converging but imperfect standard.

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-gateway-four-way-tradeoff` | The gateway's four-way fight | concept | infra | An LLM gateway — routing, auth, fallback, rate limits, governance between apps and providers — has at its heart a fight between availability, latency, guardrails and cost. In a degradation you cannot maximize all four; pick per use case. If you use a gateway, choose the trade-off; if you build one, expose those levers to callers |
| `el-per-request-fallback-for-llms` | Per-request fallback instead of retries | technology | infra | Retry-with-backoff plus circuit breaker is the standard answer to an unreliable dependency, and it is wrong for LLMs: retries eat the latency budget fast, breaking the circuit when another provider is healthy is pointless, and blind retries multiply cost and tail latency. Instead: **per-request fallback** — try provider A, then B in sequence (parallel firing only if latency-obsessed, since it doubles cost); cool down a failing primary and re-probe; decide whether failure counts live per instance (deployment size changes your thresholds) or fleet-wide (faster failover). Fallbacks are not transparent — OpenAI-compatible formats still differ in tool-calling schemas, token limits, stop reasons — so add a **normalization layer** and test the fallback path. **Streaming forfeits the lever**: once bytes are sent you cannot switch providers; "something went wrong" is by design. Give the fallback provider *more* headroom than the primary — it is the last line of defense |
| `el-per-route-latency-discipline` | Per-route latency discipline | ops | infra | Availability failures page you; high latency is quiet. A gateway runs mixed workloads (sub-second embeddings and classification, 3-second chat, long reasoning), so an aggregate latency "is a lie" — track **P99 per model per route**, and set **timeouts per model class per route**: missing timeouts are "the number one root cause of silent outages" (the gateway thinks a request is being served). "A reasoning model's normal is a chat model's outage." Reasoning and router models are the worst: the same prompt can take 2–60 s and temperature 0 often isn't allowed — fix the reasoning level per route, make requests as deterministic as possible, and **hedge the tail** by firing a second request when the first passes P90 of its budget |
| `el-guardrails-fail-open-or-closed` | Guardrails as unreliable dependencies | concept | security | Guardrails (prompt-injection defense, PII filters, toxicity) are services that can be down, so choose **fail-open** (serve anyway) or **fail-closed** (block) per guardrail by "the worst case you can live with" — a toxicity filter down can fail open. Give guardrails a **time budget** so the LLM, not the guardrail, is the rate-determining step; give them fallbacks too (secondary provider, secondary checks, cached decisions). Placement: pre-hook on input (safest, serial latency), **parallel** (best for structured outputs — don't stream those), post-hook (output monitoring and audit) |
| `el-decentralized-gateway-centralized-governance` | Decentralize the gateway, centralize governance | concept | infra | The gateway is itself a new dependency and a single point of failure. Lessons: segregate API keys and limits per route and use case to the finest grain (noisy tenants); support **load shedding** — under a retry storm you cannot simply scale out; bound the web servers' internal queues; prioritize traffic so the important use cases survive. And question the central gateway: "in most scenarios it's not the central gateway they want, it's centralized governance" — cost tracking and rate-limit management via plugins and custom code over decentralized traffic, managed by one team but not one deployment |

Element edges: all five `IdentifiedInArtifact → ia-aie-manuja-twilio-llm-gateways`.
`el-per-request-fallback-for-llms` `UsesElement → el-gateway-four-way-tradeoff`, `el-model-routing` **[registry]**, `el-agent-circuit-breakers-and-budgets` **[registry]**;
`el-per-route-latency-discipline` `UsesElement → el-inference-nondeterminism` **[registry]**;
`el-guardrails-fail-open-or-closed` `UsesElement → el-guardrail-sandwich` **[registry]**, `el-gateway-four-way-tradeoff`;
`el-decentralized-gateway-centralized-governance` `UsesElement → el-gateway-four-way-tradeoff`, `el-run-level-token-governance` **[registry]**;
`el-per-request-fallback-for-llms` `ExemplifiesPattern → pat-durable-execution` **[registry]**;
`el-gateway-four-way-tradeoff` `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-guardrails-fail-open-or-closed` `ExemplifiesPattern → pat-new-cyber-threats` **[registry]**.

Reused elements (no new nodes): `el-model-routing` **[registry]**, `el-agent-circuit-breakers-and-budgets` **[registry, b22]** (TikTok's checklist, here refined for LLM calls), `el-inference-nondeterminism` **[registry]**, `el-guardrail-sandwich` **[registry]**, `el-run-level-token-governance` **[registry, b22]**, `el-cost-control-surface-by-era` **[registry, b22]**.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-manuja-twilio-llm-gateways`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-twilio`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-the-gateway-is-a-four-way-fight` | infra | Behind "something went wrong" is a gateway choosing among availability, latency, guardrails and cost during a provider degradation — and no configuration maximizes all four. The production lesson is to make the trade-off explicit per use case and to expose the levers to callers; the model provider's ceiling is your ceiling unless the gateway can route around it | `FormsPattern → pat-harness-over-model` **[registry]**; `FormsPattern → pat-durable-execution` **[registry]** | `OnElement → el-gateway-four-way-tradeoff`, `el-model-routing` **[registry]** |
| `sig-retries-and-circuit-breakers-dont-fit-llms` | infra | The distributed-systems reflex — retry with backoff, then break the circuit — fails for LLM calls: retries burn the latency budget and multiply cost, and breaking when a second provider is healthy is wrong. Per-request cross-provider fallback with a normalization layer replaces it, streaming forfeits the fallback, and the fallback provider needs more headroom than the primary. The durable-runtime playbook gets an LLM-specific rewrite | `FormsPattern → pat-durable-execution` **[registry]** | `OnElement → el-per-request-fallback-for-llms`, `el-agent-circuit-breakers-and-budgets` **[registry]** |
| `sig-a-reasoning-models-normal-is-a-chat-models-outage` | inference | Mixed workloads make gateway-wide latency meaningless; reasoning and router models make it unpredictable (2–60 s for the same prompt, P99 jumping to 60 s "for no good reason," temperature often not settable). Per-route P99, per-model-class timeouts (the missing timeout is the top cause of silent outages), fixed reasoning levels and tail hedging are the operational responses to models whose variance is now the dominant latency risk | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-per-route-latency-discipline`, `el-inference-nondeterminism` **[registry]** |
| `sig-decentralize-the-gateway-centralize-governance` | infra | Guardrails and the gateway itself are dependencies that fail: choose fail-open vs fail-closed per guardrail by the worst case you can live with, budget guardrail time so the LLM is the rate-determining step, segregate keys per route, shed load under retry storms — and reconsider the company-wide central gateway: what teams want is centralized governance (cost tracking, rate limits) over decentralized traffic, one team but not one deployment | `FormsPattern → pat-harness-over-model` **[registry]**; `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-decentralized-gateway-centralized-governance`, `el-guardrails-fail-open-or-closed` |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-the-gateway-is-where-the-tradeoff-becomes-policy` | The durable claim: every classic reliability primitive needs an LLM-specific rewrite because the calls are slow, expensive, non-deterministic and provider-shaped — so the gateway is the place where availability, latency, guardrails and cost stop being aspirations and become per-route policy (fallback order, timeouts, reasoning level, fail-open/closed, key segregation). Which is why the right architecture is governance centralized as code over traffic that is not | `HighlightsPattern → pat-durable-execution` **[registry]** | `ReliesOnElement → el-gateway-four-way-tradeoff`, `el-per-request-fallback-for-llms`, `el-per-route-latency-discipline`, `el-decentralized-gateway-centralized-governance` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-manuja-twilio-llm-gateways`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-productionize-an-llm-gateway` | Fallback, not retry; per-route everything; governance without a chokepoint | Decide per use case which of availability, latency, guardrails and cost you protect in a degradation, and expose those levers; replace retries and circuit breakers with **per-request fallback** across providers behind a normalization layer (tool schemas, token limits, stop reasons), cool down failing primaries, choose instance-local vs fleet-wide failure counts deliberately, and provision the fallback provider with *more* headroom; accept that streaming forfeits fallback mid-stream; track **P99 per model per route**, set **timeouts per model class per route**, fix reasoning levels, make router-model requests as deterministic as possible, and hedge the tail at P90; treat guardrails as unreliable dependencies — fail-open or fail-closed by the worst case you can live with, give them time budgets and fallbacks, and place them pre-hook, parallel (structured outputs, no streaming) or post-hook (audit); segregate keys and limits per route, support load shedding and bounded queues, prioritize traffic; and prefer **centralized governance over decentralized traffic** to a single company-wide gateway deployment | `ReferencesElement → el-gateway-four-way-tradeoff`, `el-per-request-fallback-for-llms`, `el-per-route-latency-discipline`, `el-guardrails-fail-open-or-closed`, `el-decentralized-gateway-centralized-governance` |

## Dropped

- **The son's-birthday close** — color.
- **Parallel-firing to both providers** — mentioned as a latency-obsessed option; one clause in the fallback element.

## Review notes

1. **Pairs with DoorDash (this batch) and Uber (this batch) on gateways** — DoorDash and Uber describe *what* their gateways do; Twilio supplies the failure-mode discipline. Consider a "gateway" element cluster at review (`el-model-routing` widening).
2. **"Agent spend governance" ledger (b22):** "centralized governance, decentralized traffic" is the architectural form of the b22 talks' run-level attribution.
3. **⚠ Verify before seeding:** the 2–60 s / P99-60 s figures (speaker's production anecdotes) and the OpenAI-compatibility caveats as stated.
