# SPIKE extraction — "Stop AI Agent Hallucinations: 5 Techniques + Production Patterns" (Elizabeth Fuentes, AWS) — FOR REVIEW

Source transcript: `transcripts/fuentes-stop-agent-hallucinations.txt` (auto-captions of a live-demo talk — quotes are paraphrases, not verbatim; heavy garbling, see notes).
Video: https://youtu.be/vJukHCIv7Ck — AI Engineer World's Fair, published 2026-07-11.
`stagingTimestamp` for the artifact and all signals: 2026-07-11 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-fuentes-agent-hallucinations` | Stop AI Agent Hallucinations: 5 Techniques + Production Patterns (Elizabeth Fuentes, AWS — AI Engineer World's Fair) | youtube | https://youtu.be/vJukHCIv7Ck |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-elizabeth-fuentes`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-elizabeth-fuentes` | Elizabeth Fuentes Leon (developer advocate, AWS; focused on agentic applications — confirmed in transcript) | `AffiliatedWithCompany → co-aws` **[registry]** |

## Companies (0 new)

- **[registry]** `co-aws` — reused.

## Elements (3 new, 1 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-strands-agents` | Strands Agents | framework | harness | Open-source agent framework maintained by AWS: tool-decorator → auto-generated schemas, full runtime control of the agent loop (tool registry swap per invocation), hooks (BeforeToolCall/AfterToolCall) for intercepting tool execution, and a built-in Swarm class managing multi-agent handoffs; works with Bedrock, OpenAI, Ollama and most model providers | 
| `el-bedrock-agentcore` | Amazon Bedrock AgentCore | product | infra | AWS managed service "dedicated only to agents in production": serverless runtime (any framework inside), Gateway with built-in semantic tool routing (register tools once, it selects per request), short/long-term memory, policy service enforcing code-level rules structurally, steering rules stored in DynamoDB (live-updated without redeploy), CloudWatch observability | 
| `el-graphrag` | GraphRAG | concept | context | Replacing vector-retrieval RAG with a knowledge graph + structured query (e.g. LLM-written Cypher over Neo4j) for precise questions — aggregations, counts, multi-hop relationships: the graph computes a verified answer over the full dataset instead of the model estimating from top-k chunks, and returns honest zeros instead of hallucinated positives |
| **[registry]** `el-generator-validator-separation` | — | — | — | reused; the executor/validator/critic swarm is this concept in multi-agent form |

Element edges: three new elements `IdentifiedInArtifact → ia-aie-fuentes-agent-hallucinations`; `el-strands-agents` `DevelopedByCompany → co-aws`; `el-bedrock-agentcore` `DevelopedByCompany → co-aws`; `el-bedrock-agentcore` `UsesElement → el-strands-agents`; `el-graphrag` `EnablesPattern → pat-context-graphs`; `el-strands-agents` `ExemplifiesPattern → pat-harness-over-model`.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-fuentes-agent-hallucinations`, `SourcedFromSource → source-aie-yt`. Domain `harness` unless noted.

| slug | name / brief | FormsPattern | RelevantCompany | OnElement |
|---|---|---|---|---|
| `sig-tool-schema-context-tax` | Measured tool-sprawl tax: a 29-tool travel agent ships ~3,000 tokens of tool schemas (~100–200 each) on every call, before any message — and with all 29 visible the model sometimes picks the wrong near-duplicate tool; semantic pre-filtering to top-3 relevant tools cuts schema tokens to <300 and improves selection accuracy | `pat-harness-over-model` | `co-aws` | `el-strands-agents` |
| `sig-rag-fails-aggregation` (domain: context) | Vector RAG structurally fails a whole query class — averages, counts, multi-hop ("average rating across all hotels in Paris") — because it always returns something and the model only sees top-k chunks, so it presents an estimate as fact; a graph query computes the true answer and returns honest "zero hotels in Antarctica" where RAG waffles | `pat-context-graphs`, `pat-verification-gap` | — | `el-graphrag` |
| `sig-agents-fabricate-success` | Single agents that act and validate in one loop rationalize failure: a tool errors and the agent generates a confident success response — user and operator both think it worked; splitting into executor/validator/critic (Strands Swarm) surfaces the error and rejects the fabricated confirmation | `pat-verification-gap` | — | `el-generator-validator-separation`, `el-strands-agents` |
| `sig-prompt-rules-not-constraints` | Rules written in system prompts and tool descriptions get ignored ("max 10 guests" → agent books 15): prompts are processed as text, suggestions to a probabilistic model — only code executes logic; moving rules into pre-tool-call hooks (neuro-symbolic guardrails) makes them inescapable, with same model/tools/prompt flipping outcomes | `pat-harness-over-model` | — | `el-strands-agents` |
| `sig-aws-productizes-agent-reliability` (domain: infra) | AWS is absorbing every demoed reliability technique into managed services: Bedrock AgentCore ships semantic tool routing in Gateway, code-level rule enforcement as a policy service, steering rules in DynamoDB live-editable without redeploy, plus runtime/memory/observability — agent-reliability harness engineering becoming cloud product | `pat-model-not-bottleneck`, `pat-harness-over-model` | `co-aws` | `el-bedrock-agentcore` |

## Insights (1 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-hallucination-fixes-are-code` | Each agent hallucination class has a deterministic code-level fix, not a prompt-level one: token waste → semantic tool filtering; fabricated aggregates → graph queries that compute; fabricated success → a separate validator; ignored rules → hooks the model cannot escape; over-blocking → runtime steering that lets the agent self-correct (split 6 guests into two rooms) instead of hard-stopping. "Each one is a code change, not a prompt change"; hard constraints get hooks, soft constraints get steering | `pat-harness-over-model` | `el-strands-agents`, `el-graphrag` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-fuentes-agent-hallucinations`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-semantic-tool-selection` | Filter tools into context per query | Embed all tool descriptions into a vector index (local sentence-transformers is enough); per user message, retrieve top-k (≈3) tools and instantiate the agent with only those; in multi-turn conversations, swap the tool registry inside the agent loop each invocation (clear + re-add) so history doesn't re-accumulate the full toolset; in production, AgentCore Gateway does the register-once/route-per-request version without infrastructure | `el-strands-agents`, `el-bedrock-agentcore` |
| `how-graphrag-for-precise-queries` | Route aggregation/count/multi-hop queries to a knowledge graph | Build a knowledge graph from raw text using an LLM-powered construction pipeline (demo: Neo4j's SimpleKGPipeline); expose one tool whose contract is "write a Cypher query" with schema context in the prompt; let the database compute aggregates/counts across the full dataset and return the result — fewer output tokens, verifiable answers, honest zeros; keep vector RAG for open-ended topical questions | `el-graphrag` |
| `how-hooks-vs-steering` | Hard rules in hooks, soft rules in steering | Encode inviolable constraints (payment-before-confirm, date validation, guest caps) as before-tool-call hooks that cancel the call — all-or-nothing, lives in the harness code; for soft rules where blocking is wrong (6 guests → book two rooms), use a runtime steering layer (open-source "agent-steering" control server in the demo; DynamoDB-backed in AgentCore) where rules register via API, the agent picks them up immediately, self-corrects, and completes the task — and rule changes need no code redeploy; add a validator/critic swarm when fabricated success is the failure mode | `el-strands-agents`, `el-bedrock-agentcore`, `el-generator-validator-separation` |

## Dropped

- Neo4j (and Aura DB free tier), OpenAI-as-demo-model, sentence-transformers, Ollama, Postgres, CDK — demo plumbing, prose only; no `co-openai` edge (model choice is incidental).
- "Agent control" open-source steering library — name unrecoverable from captions (rendered "AIN control"/"agent control"); described functionally inside `how-hooks-vs-steering`, flagged below.
- The travel-agent demo scenarios (Antarctica hotels, Lisbon bookings) — illustrations folded into signals.
- QR-code repo / AWS credits giveaway — logistics.

## Review notes

1. Worst captions of my five talks (live coding, presenter's second language): "Strands"/"a strands"/"E-strands"/"Swarms agent" all = Strands Agents; "Amazon Bedrock Agent Core"/"better agent car"/"Bella Betray in core"/"Aion core" all = Bedrock AgentCore; "graph rack" = GraphRAG; "neuro-symbolic guardians" kept as her term for code-level guardrails. Confident resolutions applied; the steering library's real name is NOT confidently recoverable — verify against the linked repo before seeding anything from it.
2. `sig-tool-schema-context-tax` numbers (3,000 → <300 tokens, ~2k tokens/query baseline) are from her dummy-tool demo, not production data — she says so explicitly. Kept because the mechanism (per-call schema tax) is general; downgrade to knowhow prose if demo-derived numbers fail the signal bar.
3. `el-graphrag` is a generic industry term (Microsoft coined GraphRAG in 2024), not her invention — coined as a concept element because two edges need it and the registry lacks it; central review may prefer a different canonical brief.
4. Five signals is at the top of the band; `sig-rag-fails-aggregation` is the most fold-able (into `how-graphrag-for-precise-queries`).
5. "Neuro-symbolic guardrails" and "runtime steering" were considered as separate Elements; both kept as prose/knowhow since they're technique names local to this talk (the hooks mechanism belongs to `el-strands-agents`, the managed version to `el-bedrock-agentcore`).
