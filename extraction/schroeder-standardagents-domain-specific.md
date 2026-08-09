# SPIKE extraction — "The Future Is Domain-Specific Agents" (Justin Schroeder, StandardAgents) — FOR REVIEW

Source transcript: `transcripts/schroeder-standardagents-domain-specific.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/spNAUEgq_A8 — AI Engineer World's Fair, published 2026-06-29.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-06-29 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-schroeder-domain-specific-agents` | The Future Is Domain-Specific Agents (Justin Schroeder, StandardAgents — AI Engineer World's Fair) | youtube | https://youtu.be/spNAUEgq_A8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-justin-schroeder`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-justin-schroeder` | Justin Schroeder (StandardAgents, in stealth; open-source author — Dmux coding-agent multiplexer, ArrowJS) | `AffiliatedWithCompany → co-standardagents` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-standardagents` | StandardAgents | developer | stealth startup (standardagents.ai) building a domain-specific-agent ecosystem/platform; early access sign-ups open, no product announced |
| `co-vercel` | Vercel | developer | web/AI platform company; ships the Vercel AI SDK (`el-vercel-ai-sdk` **[registry]**) and, days before this talk, the Eve agent framework |

## Elements (2 new, several reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-domain-specific-agents` | Domain-specific agents | concept | harness | Small but complete agents — own domain-written system prompt, precise minimal toolset, own message history and agentic loop, sandboxed per-agent filesystem + sandboxed code execution — scoped to a single domain (Figma, Gmail, GDPR compliance…) and composed under a coordinator that delegates in plain English. Claimed properties: >80% token efficiency per task; small/cheap and even non-language models become viable; capabilities are explicitly bounded (security by construction rather than bypassed permission prompts); parallel, region-independent cloud scaling. Sub-agents can recurse (coordinator → Salesforce agent → asset-generation agent; legal-team agent → GDPR/OSHA agents) |
| `el-vercel-eve` | Vercel Eve | framework | harness | Vercel's agent framework, released days before the talk — pitched as "build a company brain, personal assistant, or domain-specific agent"; cited by the speaker as the closest thing yet to a defined way to build an agent, and the first mainstream product copy to use the term "domain-specific agent" |

Reused: `el-mcp` **[registry]**, `el-agent-skills` **[registry]**, `el-agent-hooks` **[registry]**, `el-context-rot` **[registry]**.
Element edges: `el-domain-specific-agents` `ExemplifiesPattern → pat-harness-over-model` **[registry]**; `el-vercel-eve` `DevelopedByCompany → co-vercel`; both `IdentifiedInArtifact → ia-aie-schroeder-domain-specific-agents`.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-schroeder-domain-specific-agents`, `SourcedFromSource → source-aie-yt` **[registry]**. Domain `harness` except `sig-token-cost-reversal-2026` (`inference`).

| slug | name / brief | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|
| `sig-everyone-builds-custom-agents` | Everyone is building custom agents — a local real-estate agency, independent insurance brokers, many Fortune 500s — despite ubiquitous AI access, while the general public can barely name one agent (Claude, maybe Codex). The driver is integration: getting business data properly into AI. Most efforts die as demos: agentic-loop orchestration, provider abstractions, durable execution, telemetry at scale, portability, and composability are unsolved for them; "there's no defined way to build an agent" | `FormsPattern → pat-model-not-bottleneck` | — | — |
| `sig-mcp-reduced-to-tools` | Reading MCP's own client-support matrix: only the tools column is implemented across clients — MCP has become a de facto tool-distribution mechanism into large general-purpose agents, its other primitives unrealized; enterprises retreat to it after failed custom-agent attempts, but "tools are not enough" (you don't land a man on the moon by giving one guy a ton of tools) | — (pattern-less; see notes) | `OnElement → el-mcp` | — |
| `sig-context-inflation-diminishing-returns` | Skills/MCP stacking is inheritance — inflating one general agent's context layer; the speaker cites research that installing very many skills makes an agent substantially worse, and argues 100–1,000 skills obviously hit diminishing returns | — (pattern-less; see notes) | `OnElement → el-agent-skills`, `OnElement → el-context-rot` | — |
| `sig-token-cost-reversal-2026` | The cost-of-intelligence decline reversed in 2026 (speaker tracks it on a website): IQ-adjusted token prices up 29% and raw prices up ~76% in H1 2026, memory crunch cited. Customer-facing economics: "you can't put Fable in front of a customer" — vs DeepSeek V4 Flash at ~137× cheaper per task, viable when scope is narrowed | — (pattern-less; candidate flagged) | — | `co-deepseek` **[registry]**, `co-anthropic` **[registry]** |
| `sig-dsa-prediction-h2-2026` | Public prediction: from mid-2026, a dramatic uptick in domain-specific-agent frameworks, ecosystems, and discourse; 2027 the year of "multi-agent orchestration". Vercel's Eve release (days earlier), whose copy names domain-specific agents, cited as the first external echo; StandardAgents runs them internally daily but they "don't exist in a big public way" yet | `FormsPattern → pat-harness-over-model` | `OnElement → el-domain-specific-agents`, `OnElement → el-vercel-eve` | `co-vercel` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-composition-over-inheritance-agents` | Bolting skills/MCP onto one agent is inheritance: it works, then breaks down as context inflates. The alternative is composition — many minimal, complete agents (not tool servers: own prompt, loop, history) coordinated in natural language, the Apollo-control-room model ("teams of experts", each person an agent with only their tools). Capability should come from structure, not from an ever-fatter context window | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-domain-specific-agents` |
| `ins-small-models-viable-when-scoped` | With tasks pre-picked and context minimal (system prompt + precise tools + a single incoming instruction like "get the last email from Debbie"), much smaller and cheaper models — even non-language models (diffusion, image generation) — execute faithfully; the ~137× price gap makes customer-facing AI economically possible, and bounded toolsets give IT enforceable capability limits instead of everyone bypassing permissions | `HighlightsPattern → pat-model-not-bottleneck` | `ReliesOnElement → el-domain-specific-agents` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-schroeder-domain-specific-agents`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-domain-agent-anatomy` | Anatomy of an ideal domain agent | Split the tool layer into three kinds: plain functions; prompts-as-tools (a tool call that invokes a different model, e.g. an image model like Nano Banana while GLM 5.2 runs the loop); and full sub-agents-as-tools (recursive). Add hooks that inject synthetic messages/tool-calls (e.g. current time — LLMs don't know it) and fire side effects; agent rules (turn/step caps, tool-call validation requirements); and bake in a sandboxed per-agent filesystem plus sandboxed code execution as primitives — the big labs already learned chat needs a filesystem. Keep each agent's context minimal and delegate across agents in plain English | `ReferencesElement → el-domain-specific-agents`, `ReferencesElement → el-agent-hooks` **[registry]** |

## Dropped

- Dmux / ArrowJS — speaker's own OSS, intro color (kept in expert brief).
- The Vercel AI SDK compliment ("is great") — passing; `el-vercel-ai-sdk` **[registry]** not edged.
- Industrial-Revolution framing ("harness energy with machines → harness intelligence with agents") and the speaker's agent definition ("deterministic software that harnesses the non-deterministic results produced by models"; agent ≈ harness, distinction "pedantic") — folded into element brief and insight prose.
- Apollo 11 imagery — folded into `ins-composition-over-inheritance-agents`.
- Nano Banana / GLM 5.2 model name-drops — illustrative, kept as prose inside the knowhow.

## Review notes

1. Speaker name: captions say "Justin Schrader" / X handle "JP Schrader"; official title says Justin Schroeder — Schroeder used. Company rendered "Standard Agents" (standardagents.ai).
2. `sig-token-cost-reversal-2026` numbers (29% IQ-adjusted, 76% raw, 137× DeepSeek-vs-Fable) are speaker claims from an unnamed tracker; a stray "and 37 times" utterance follows the 137× figure (possibly input-vs-output pricing) — caption noise, not extracted. "DeepSeek V4 Flash" is caption-spelled. Verify all before quoting.
3. **Candidates flagged WITHOUT coining** (no edges): (a) *domain-specific agents / multi-agent composition era* — one-talk evidence here, with Vercel Eve's copy as a weak second source; (b) *intelligence-cost reversal* (`sig-token-cost-reversal-2026`) — one-talk; if it recurs it is counter-evidence to the cheap-intelligence assumption embedded in several existing files.
4. Durable execution appears once as a named hard problem in custom-agent building — passing mention, deliberately NOT counted toward the `pat-durable-execution` candidate (Kalandadze precedent).
5. `sig-mcp-reduced-to-tools` and `sig-context-inflation-diminishing-returns` left pattern-less deliberately: closest fits (`pat-agent-supply-chain` for MCP-as-distribution-channel; `pat-model-not-bottleneck` for context-inflation) both felt like stretches. Rehome at review if you read them otherwise.
6. Registry `el-custom-agents` (batch6) NOT linked from `sig-everyone-builds-custom-agents` — that element appears to denote a specific product feature (GitHub Copilot custom agents), not the generic build-your-own-agent activity.
7. `el-context-rot` **[registry]** edge on sig-3 assumes the registry element carries the common "performance degrades as context grows" sense; drop the edge if it is scoped to staleness only.
8. "There's lots of research out there that shows that if you use very many of these [skills], it makes your agent substantially worse" — uncited claim, kept as reported speech inside sig-3.
