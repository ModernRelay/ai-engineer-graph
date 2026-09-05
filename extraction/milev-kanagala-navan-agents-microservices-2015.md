# SPIKE extraction — "Agents Are Where Microservices Were in 2015" (Roberto Milev & Uday Kanagala, Navan) — FOR REVIEW

Source transcript: `transcripts/milev-kanagala-navan-agents-microservices-2015.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/32nrHU6zHU8 — AI Engineer World's Fair, published 2026-08-29.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-29 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: Navan's chief architect and an architecture-team colleague walk an emerging **agentic reference architecture** layer by layer — runtime, memory, context, cross-cutting operations (tracing, evals, guardrails/authorization), orchestration — and grade each layer's maturity, with the microservices era (Kubernetes, service mesh, circuit breakers took years to settle) as the analogy. Caption garbles: "Nvono"/"Nvone" → **Navan**, "Rudra" → **Roberto**, "Hotel"/"OTEL" → **OpenTelemetry**, "agent core" → **AWS Bedrock AgentCore**, "trajectory vals" → **trajectory evals**, "sub aents" → **sub-agents**, "Woody" (a previous speaker) kept.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-milev-kanagala-navan-agents-microservices` | Agents Are Where Microservices Were in 2015 (Roberto Milev & Uday Kanagala, Navan — AI Engineer World's Fair) | youtube | https://youtu.be/32nrHU6zHU8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-roberto-milev`, `exp-uday-kanagala`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-roberto-milev` | Roberto Milev (Chief Architect, Navan) | `AffiliatedWithCompany → co-navan` |
| `exp-uday-kanagala` | Uday Kanagala (Architecture, Navan) | `AffiliatedWithCompany → co-navan` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-navan` | Navan | developer | Travel and expense management company; runs many production agents ("a lot of tokens per day") on AWS Bedrock AgentCore runtime + memory, with self-built session persistence/rehydration; single master agent with progressively loaded skills |

Reused **[registry]**, edge-only: `co-aws` (AgentCore runtime/memory), `co-anthropic` **[seed]** (Claude hooks as the interception model). Referenced, not coined: GCP, Azure (their agent runtimes).

## Elements (6 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agentic-reference-architecture` | The agentic reference architecture | concept | infra | The layers that "have crystallized" for running agentic flows reliably: runtime (stateful, persistent sessions, isolation, a different lifecycle than an API service — cloud providers have each shipped an agent runtime), memory (ingest → extract → consolidate → retrieve; short-term → long-term → episodic), context management, cross-cutting operations (tracing, evals, guardrails/authz, cost), orchestration. Graded: runtime solved, memory maturing, MCP de facto, OTel pushed but unproven for agentic calls, testing hard but workable, orchestration "don't over-engineer," cost and replay/debugging unsolved. "If you can't build a well-structured monolith, why try microservices" → "if you can't build a single agentic loop, why build a multi-agent system" |
| `el-skills-as-unit-of-context` | Skills as the unit of context | concept | context | Context is composed dynamically out of skills — each carrying both context (instructions/setup for a domain or task) and the agentic part (tool execution) — as pluggable units of work that can be tested independently and reused, relying on progressive disclosure to start with limited scope and expand via metadata |
| `el-hook-based-agent-tracing` | Hook-based agent tracing | technology | harness | Logs don't work for agents ("too much thinking to consume"). Instead, intercept at pre/post tool-call and pre/post decision hooks (the Claude model) to block, log or emit metrics, producing OTel-style spans/traces. The trace carries judgment pointers: the current goal, the reasons for operations, belief status, tool calls, and a **confidence score** — whether an answer came from multiple converging paths or was *inferred*, which routes it to a human |
| `el-trajectory-evals` | Trajectory evals | concept | harness | A 30-step agent makes up its own steps differently every run, so a deterministic graph can't be charted. Instead measure how far along the source→goal trajectory the agent got, as completeness/efficiency; feed inferred-answer signals back as regression classifiers. Navan "relies heavily" on these because "the moment we change something, something else breaks" |
| `el-pre-post-tool-guardrails` | Pre/post-tool guardrails and authorization | technology | security | Guardrail and authorization checks before and after every tool call — the governance layer for sensitive data piped to models. The identity question has changed: an agent acts *on behalf of* a user ("book me a flight whenever it's under $200 — is it me buying, or agent-me?") or under a service account; the line blurs and fine-grained policy decisions are needed at the tool boundary |
| `el-single-master-agent-with-subskills` | Single master agent with sub-skills | concept | harness | Navan's orchestration answer to the "orchestration wars": one master agent that progressively loads skills and sub-skills and decides what enters context, rather than multi-agent orchestration. Agent-to-agent (A2A) is reserved for team boundaries in large organizations where teams don't otherwise talk — the protocol as the contract between them |

Element edges: all six `IdentifiedInArtifact → ia-aie-milev-kanagala-navan-agents-microservices`.
`el-agentic-reference-architecture` `UsesElement → el-bedrock-agentcore` **[registry]**, `el-mcp` **[seed]**, `el-opentelemetry` **[registry]**;
`el-skills-as-unit-of-context` `UsesElement → el-agent-skills` **[registry]**, `el-progressive-disclosure` **[registry]**;
`el-hook-based-agent-tracing` `UsesElement → el-agent-hooks` **[registry]**, `el-opentelemetry` **[registry]**;
`el-single-master-agent-with-subskills` `UsesElement → el-skills-as-unit-of-context`, `el-a2a-protocol` **[registry]**;
`el-pre-post-tool-guardrails` `UsesElement → el-agent-scoped-authorization` **[registry]**;
`el-agentic-reference-architecture` `ExemplifiesPattern → pat-durable-execution` **[registry]**;
`el-trajectory-evals` `EnablesPattern → pat-verification-gap` **[registry]**;
`el-single-master-agent-with-subskills` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

Reused elements (no new nodes): `el-bedrock-agentcore` **[registry]** (the runtime they run on — with self-built session persistence/rehydration filling its gaps), `el-agent-skills` **[registry]**, `el-progressive-disclosure` **[registry]**, `el-agent-hooks` **[registry]**, `el-opentelemetry` **[registry]**, `el-a2a-protocol` **[registry]**, `el-mcp` **[seed]**, `el-agent-scoped-authorization` **[registry]**.

## Signals (6 new)

All: `SpottedInArtifact → ia-aie-milev-kanagala-navan-agents-microservices`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-navan`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-agent-reference-architecture-crystallizing` | infra | Navan's chief architect: agents are where microservices were in 2015 — the paradigm is real, the reference architecture is emerging by doing, and it will take time to settle as Kubernetes/service mesh/circuit breakers did. Layers have already crystallized (runtime, memory, context, cross-cutting ops, orchestration); AWS, GCP and Azure each ship an agent runtime; Navan runs on AgentCore but had to build session persistence and rehydration itself | `FormsPattern → pat-durable-execution` **[registry]** | `OnElement → el-agentic-reference-architecture`, `el-bedrock-agentcore` **[registry]** |
| `sig-runtime-solved-cost-and-replay-unsolved` | infra | The maturity map: runtime "pretty much solved," memory maturing (cloud providers' ingest→extract→consolidate→retrieve pipelines), MCP the de facto protocol now going stateless, OTel pushed but "does it really work for agentic calls?", testing hard but workable, orchestration "don't over-engineer." Unsolved: **cost** — very hard to predict or manage, "driven by the big AI vendors whose interest is for us all to spend more tokens" — and **replay/debugging**, which agents themselves may end up solving | `FormsPattern → pat-durable-execution` **[registry]**; `FormsPattern → pat-agent-memory-layer` **[registry]** | `OnElement → el-agentic-reference-architecture`, `el-mcp` **[seed]**, `el-a2a-protocol` **[registry]** |
| `sig-skills-as-the-unit-of-context` | context | What worked for context management at Navan: skills as the unit — each bundling domain context and tool execution — composed dynamically per agent, testable and reusable independently, with progressive disclosure expanding scope from metadata. The orchestration corollary: one master agent progressively loading skills beat multi-agent designs — "if you can't perfect a single agent, why go multi-agent" | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-skills-as-unit-of-context`, `el-single-master-agent-with-subskills`, `el-agent-skills` **[registry]** |
| `sig-trajectory-evals-over-deterministic-tests` | harness | A hands-up in the room: almost nobody is "100% confident" in their agent test pipelines. Navan's answer — you can't chart a deterministic graph for a 30-step non-deterministic run, so measure distance along the source→goal trajectory, treat inferred (low-confidence) answers as regression signals, and route them to a human. Verification relocated from asserting outputs to grading trajectories | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-trajectory-evals`, `el-hook-based-agent-tracing` |
| `sig-agent-on-behalf-of-blurs-authorization` | security | Enterprise governance reframed at the tool boundary: an agent acting on behalf of a user ("book a flight whenever it's under $200") or under a service account blurs who is acting, so authorization must become fine-grained policy at pre/post-tool hooks that can check and block. A production enterprise arriving at the same "agent identity is the new perimeter" conclusion as the corpus's security track | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-pre-post-tool-guardrails`, `el-agent-scoped-authorization` **[registry]** |
| `sig-observability-must-capture-judgment-not-logs` | harness | Logs "change everything the moment we switch to agents" — too much thinking to consume. The replacement is hook-level interception emitting traces that carry the agent's goal, reasons, belief status and a confidence score per decision, so that an operator can see where a 20–30-step agent got stuck and whether an answer was inferred. Observability re-targeted from events to judgment | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-hook-based-agent-tracing`, `el-agent-hooks` **[registry]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-agents-repeat-the-microservices-curve` | The analogy is load-bearing, not decorative: a paradigm whose reference architecture crystallizes layer by layer through production practice, with the infrastructure vendors racing to productize each layer (runtime first, memory next). It predicts where value pools — the unsolved layers (cost control, replay/debug) are where the next Kubernetes-equivalents will be built — and warns against the 2015 mistake of over-engineering orchestration before the single loop is solid | `HighlightsPattern → pat-durable-execution` **[registry]** | `ReliesOnElement → el-agentic-reference-architecture`, `el-single-master-agent-with-subskills` |
| `ins-verification-moves-to-trajectories-and-confidence` | For non-deterministic multi-step agents, the testable object is no longer the output but the trajectory (how far toward the goal) plus the agent's own declared confidence (converged vs inferred), captured at hooks. That is the same relocation of verification the corpus sees elsewhere — outside the model, into a structured trace a human can grade — applied to day-to-day operations rather than code review | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-trajectory-evals`, `el-hook-based-agent-tracing`, `el-pre-post-tool-guardrails` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-milev-kanagala-navan-agents-microservices`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-run-agents-like-a-2015-microservices-shop` | Build the single loop first, then layer the reference architecture | Don't build multi-agent orchestration until a single agentic loop is solid — start with one master agent that progressively loads skills; treat **skills as the unit of context** (context + tool execution), composed dynamically, tested and reused independently, with progressive disclosure; use a managed agent runtime but expect to fill gaps (session persistence, rehydration) yourself; replace logs with **hook-based tracing** at pre/post tool and decision points, emitting goal, reasons, belief status and confidence, so you can see where a 30-step agent got stuck; evaluate with **trajectory evals** (distance toward the goal) and treat inferred answers as regression signals routed to a human; put **guardrails and fine-grained authorization** at pre/post-tool hooks because agents act on behalf of users; reserve A2A for team boundaries; and budget for the two unsolved layers — cost and replay/debugging | `ReferencesElement → el-agentic-reference-architecture`, `el-skills-as-unit-of-context`, `el-hook-based-agent-tracing`, `el-trajectory-evals`, `el-pre-post-tool-guardrails`, `el-single-master-agent-with-subskills` |

## Dropped

- **The QR-code cloud-runtime comparison slides** — not recoverable from captions.
- **The memory-pipeline taxonomy** (short-term → long-term → episodic) — folded into `el-agentic-reference-architecture` rather than coined as an element (well covered by b19's memory elements).
- **The previous-speaker references** ("Woody" on replay; the developer-cost talk) — pointers only.

## Review notes

1. **⚑ A vendor-neutral enterprise maturity map for `pat-durable-execution`.** The talk grades the runtime layer "solved" by the cloud providers while naming *replay/debugging* and *cost* as the unsolved layers — useful calibration against the pattern's product-side claims (Temporal/Inngest/Modal in earlier batches): the durable layer is productized, but replay is not yet.
2. **Two same-batch disagreements to surface:** Navan calls MCP "the de facto protocol" where Maersk (Buykin) rejects it for tuned function calling; Navan says "don't over-engineer multi-agent" where Warp (Abdalla) productizes multi-harness sub-agent orchestration. Both are texture, not contradictions of a coined pattern.
3. **`el-skills-as-unit-of-context`** is the third same-batch skills-centric harness claim (with QuantumBlack's skills governance and Box's approach ladder) — recommend widening `el-agent-skills` (b1) at review rather than a new pattern.
4. **⚠ Verify before seeding:** that Navan's runtime is AWS Bedrock AgentCore (captions say "agent core"), the "20/30-step" figures, and the claim that MCP "is becoming stateless."
