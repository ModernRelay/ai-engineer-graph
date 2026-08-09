# SPIKE extraction — "Your Agent Is Wasting Tokens and You Don't Know It" (Erik Hanchett, AWS) — FOR REVIEW

Source transcript: `transcripts/hanchett-aws-agent-wasting-tokens.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/uiP88SpCi1Q — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact and all signals: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the shared registry — edges link to them, no new node defined here.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-hanchett-agent-wasting-tokens` | Your Agent Is Wasting Tokens and You Don't Know It (Erik Hanchett, AWS — AI Engineer World's Fair) | youtube | https://youtu.be/uiP88SpCi1Q |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-erik-hanchett`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-erik-hanchett` | Erik Hanchett (senior developer advocate, AWS; programwitheric.com) | `AffiliatedWithCompany → co-aws` **[registry]** |

## Companies (0 new)

- **[registry]** `co-aws` — reused.

## Elements (2 new, 1 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-prompt-caching` | Prompt caching | technology | inference | Provider-side caching of repeated prompt segments (system prompt, tool definitions, messages): the first call sends the full prompt, subsequent calls send a much-reduced cached reference — a one-flag cost lever (e.g., `cache_prompt="default"` in Strands Agents) that works across model providers |
| `el-model-routing` | Difficulty-based model routing | concept | inference | Routing each task to the cheapest adequate model — a frontier model for difficult tasks, a small cheap one (Haiku-class) for simple ones — instead of one expensive default for everything; the router can itself be a very cheap model |
| **[registry]** `el-strands-agents` | — | — | — | reused; all five cost levers are demonstrated on it (`cache_prompt` flag, tool-result offload APIs, sliding-window conversation manager) |

Element edges: `el-prompt-caching` and `el-model-routing` `IdentifiedInArtifact → ia-aie-hanchett-agent-wasting-tokens`; `el-strands-agents` `IdentifiedInArtifact → ia-aie-hanchett-agent-wasting-tokens`.

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-hanchett-agent-wasting-tokens`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-default-agent-loops-leak-tokens` | harness | AWS developer-advocate field observation: default agent-loop behavior silently multiplies token spend — the full conversation history is resent on every turn ("hundreds if not thousands of tokens"), large tool results are re-injected into context on every loop iteration, and uncapped tool loops run 10–20 times or go infinite; none of it is visible without pre-deploy observability of per-tool call counts and durations | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-aws` |
| `sig-route-dont-default-to-frontier` | inference | Cloud-vendor guidance now explicitly warns against defaulting to the most expensive model: route by difficulty (Haiku-class for simple tasks, Sonnet-class for harder ones), even letting another very cheap model decide the route — right-sizing as recommended standard practice reflects that smaller models are adequate for much of the workload | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-model-routing` |
| `sig-token-economy-productized` | harness | Token-economy controls are being productized into vendor agent SDKs: AWS's Strands Agents ships prompt-caching flags, tool-result offload APIs, and a sliding-window conversation manager as first-class framework features — cost control migrating from app-level hacks into the framework layer | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-strands-agents` **[registry]**; `RelevantCompany → co-aws` |

## Insights (1 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-token-cost-is-a-harness-property` | An agent's token bill is set by harness configuration — what gets cached, resent, summarized, capped, and windowed — more than by model choice: the same agent with caching, routing, tool-result offloading, loop caps, and history trimming costs a fraction of its default-config self. Cost is an engineering property of the loop, not a fixed price of intelligence | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-prompt-caching`, `ReliesOnElement → el-strands-agents` **[registry]** |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-hanchett-agent-wasting-tokens`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-five-token-cost-levers` | Five levers to cut agent token costs | (1) Cache the system prompt — and tool prompts/messages where supported — so only the first call pays full price; (2) route by difficulty: never one expensive model for every task, optionally with a cheap router model; (3) offload large tool results to local/cloud storage and pass back a summary, so the raw result isn't re-added to context on every agent/tool loop; (4) cap tool loops with a max-iterations setting, and before deploy run observability tooling over per-tool call counts and durations to spot loopers; (5) trim multi-turn history with a sliding window (e.g., last 10 messages) and summarize the truncated prefix into context — trade-off: raw early history is lost | `ReferencesElement → el-prompt-caching`, `ReferencesElement → el-model-routing`, `ReferencesElement → el-strands-agents` **[registry]** |

## Dropped

- Claude Haiku / Claude Sonnet as Elements — named as cheap/expensive placeholders with no versions; registry has versioned nodes (`el-claude-haiku-45` etc.) that would over-specify; prose only.
- SlidingWindowConversationManager as its own element — Strands API surface; folded into the `el-strands-agents` reuse and the knowhow.
- `el-bedrock-agentcore` **[registry]** — NOT edged; the talk never mentions AgentCore.

## Review notes

1. Lightning talk (~5 min) with zero dated external facts — all three signals are vendor-practitioner testimony / productization observations, per the short-talk allowance.
2. **Name spelling:** captions and the speaker's own sign-off use "Eric Hanchett" (programwitheric.com, @EricCH); the conference listing uses "Erik Hanchett" — slug `exp-erik-hanchett` per instructions/listing; flag the spelling for reconciliation. The same speaker has a second talk ("Using Spec-Driven Development", position 128, not in this batch) — reuse this node there.
3. `el-prompt-caching` is industry-generic (Anthropic/OpenAI/Bedrock all ship it) — coined because it is this talk's lead lever and reusable corpus-wide; no equivalent found in the registry, but treat as a merge target if another batch coined one under a different slug.
4. Adjacent registry element deliberately not edged: `el-context-compaction` **[registry]** (batch 6, OpenAI keynote) likely covers the same ground as lever 5 (trim + summarize history) — flagged for reconciliation rather than edging on an uncertain brief.
5. No pattern candidates; signals parked on `pat-harness-over-model` / `pat-model-not-bottleneck`.
