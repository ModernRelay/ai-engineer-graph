# SPIKE extraction — "Agents in Production: How OpenGov Built and Scaled OG Assist" (Gabe De Mesa, OpenGov) — FOR REVIEW

Source transcript: `transcripts/de-mesa-opengov-og-assist.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/4uFVSLgD2Q4 — AI Engineer World's Fair, published 2026-06-26.
`stagingTimestamp` for the artifact and all signals: 2026-06-26 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-de-mesa-og-assist` | Agents in Production: How OpenGov Built and Scaled OG Assist (Gabe De Mesa, OpenGov — AI Engineer World's Fair) | youtube | https://youtu.be/4uFVSLgD2Q4 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-gabe-de-mesa`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-gabe-de-mesa` | Gabe De Mesa (software engineer, OpenGov AI agents team; co-builder of OG Assist) | `AffiliatedWithCompany → co-opengov` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-opengov` | OpenGov | developer | ~14-year-old government ERP vendor (budgeting, procurement, asset management, permitting, utility billing) shipping an embedded production agent across its whole suite |

## Elements (3 new + 2 registry reuses)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-og-assist` | OG Assist | product | harness | OpenGov's embedded agent, a button in the navigation bar of every product in the ERP suite; each product team contributes tools and skills; the agent makes tool calls against suite data, sees what's on the user's screen and can highlight/act on page elements, executes code in on-demand ephemeral sandboxes, renders generative UI at runtime, and interrupts deterministically for human approval on mutating tool calls |
| `el-effect-ts` | Effect (TypeScript library) | framework | harness | Open-source TypeScript library (schema à la Zod, typed error handling, logging, structured concurrency, tracing with automatic spans) plus an Effect AI package (chat + language-model abstractions with dependency injection for hot-swapping models); OpenGov's agents team built its whole bespoke agent loop, toolkits, and observability on it — website: effect.website |
| `el-a2a-protocol` | A2A (agent-to-agent) protocol | technology | harness | Google's open protocol for agent intercommunication (agent cards carrying name/description/capabilities, plus extensions such as A2UI); at OpenGov repurposed as the internal spec for agent routes — the rigorous contract both front end and back end consume and produce | 
| **[registry]** `el-langgraph` | — | — | — | reused (batch 2); OG Assist's original framework, abandoned as the team scaled and use cases evolved — the "before" of the own-your-loop migration |
| **[registry]** `el-generative-ui` | — | — | — | reused (batch 2); OG Assist registers UI primitives (e.g., a form) the agent instantiates at runtime — "UI on the fly" options generated in the moment |

Element edges: `el-og-assist`, `el-effect-ts`, `el-a2a-protocol` `IdentifiedInArtifact → ia-aie-de-mesa-og-assist`; `el-langgraph` **[registry]** and `el-generative-ui` **[registry]** `IdentifiedInArtifact → ia-aie-de-mesa-og-assist`; `el-og-assist` `DevelopedByCompany → co-opengov`, `UsesElement → el-effect-ts`, `UsesElement → el-a2a-protocol`; `el-a2a-protocol` `DevelopedByCompany → co-google` **[registry]**.

## Signals (5 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-de-mesa-og-assist`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-opengov`.

| slug | name / brief | FormsPattern | OnElement |
|---|---|---|---|
| `sig-opengov-owns-agent-loop` | Production migration off a framework: OpenGov's agents team started on LangGraph, outgrew it as the team scaled and use cases evolved, and rebuilt a bespoke Effect-native agent loop for full control — tracing, structured concurrency, fine-grained logging, and dependency-injected model hot-swapping come from the general-purpose effect system rather than an agent framework | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-effect-ts`, `OnElement → el-langgraph` **[registry]** |
| `sig-a2a-as-internal-contract` | A2A adopted not for cross-org agent interop but as an internal spec: agent cards model OpenGov's agent routes, and the protocol's rigor is valued as the contract that keeps front end and back end aligned — an open agent protocol repurposed as intra-product schema | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-a2a-protocol` |
| `sig-agent-layer-across-erp` | An incumbent vertical-SaaS vendor (government ERP) ships one agent surface across its entire product line, with every product team contributing tools and skills to power it ("tools and skills are really all you need," paraphrase); capabilities span back-end tool calls against suite data and front-end screen awareness (agent sees the page and highlights actionable elements) | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-og-assist` |
| `sig-approval-gates-and-sandboxes` | Production safety posture: the agent loop is deterministically interrupted whenever a tool call requires approval — explicit accept/reject UI, "humans always in the driver's seat" (paraphrase), especially for mutating operations — and all code execution / file creation happens in on-demand ephemeral sandboxes that tear down after use, isolating production systems | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-og-assist` |
| `sig-ci-evals-on-real-completions` | "Shipping is the start, not the finish" (paraphrase): iteration engine is user thumbs-up/thumbs-down feedback plus automated evals running in CI against real completions (did the prompt hit the right tools, did it do what it's supposed to) — eval-in-CI as ordinary production practice at a non-frontier enterprise vendor | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-og-assist` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-own-thin-loop-on-strong-infra` | Agent frameworks are fine to start, but a production team with evolving use cases gets more from owning a thin agent loop built on strong general-purpose infrastructure (typed effects, structured concurrency, DI, out-of-the-box tracing) than from framework abstractions — the loop itself is small; the surrounding engineering is what scales, and full control of the loop is what "unlocks the full capabilities of the model" (paraphrase) | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-effect-ts` |
| `ins-tracing-precondition-for-scale` | "You can't scale what you can't see" (paraphrase): agentic systems integrate many teams' APIs and platform capabilities, so span-level traces that profile every function/tool call and cross-reference failures across services are the precondition for debugging and maintaining them — pick infrastructure where tracing is automatic rather than bolted on | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-effect-ts` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-de-mesa-og-assist`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-rolling-summary-memory` | Handle long conversations with a rolling summary plus recall | Instead of always stuffing the latest messages: after n messages keep a running summary plus only the ~n−5/n−10 most recent messages; answer "remember that thing we talked about?" by doing recall over the rolling summary rather than retaining full history — cheaper than token-limit overload on long threads, works with legacy models | `ReferencesElement → el-og-assist` |
| `how-gate-mutating-tools` | Gate mutating actions; sandbox code execution | Deterministically interrupt the agent loop when a tool call requires human approval and render an explicit accept/reject UI (explicit rejection as valuable as acceptance); scope approvals to mutating operations to build trust; give agents on-demand ephemeral sandboxes for writing/executing code and creating files, torn down at the end, so agent actions carry no risk to production systems | `ReferencesElement → el-og-assist` |

## Dropped

- A2UI — one passing mention as an A2A extension; registry `el-a2ui` NOT edged (no load-bearing content here).
- Claude / Cursor / "Claude agents" for internal developer velocity — endorsement prose ("such an accelerant"), no specifics; no edges to `el-claude-code` (captions say only "Claude").
- The get-dad-joke toolkit example — pedagogical sample from the Effect docs, folded into `el-effect-ts`'s brief.
- Thumbs up/down UI as an Element — generic feedback mechanism, kept inside `sig-ci-evals-on-real-completions`.

## Review notes

1. **Caption garbles:** "Ogie Assist" → OG Assist; "full regency over this Agent Loop" → full agency. Quotes are paraphrases.
2. `pat-saaspocalypse` **[registry]** was considered for `sig-agent-layer-across-erp` (incumbent vertical SaaS embedding an agent layer reads as the SaaS-adapts side of that thesis) — not linked on seed-brief uncertainty; parked on `pat-model-not-bottleneck` (differentiation living in the tool/skill/product-integration layer, not the model). Rehome at reconciliation if the saaspocalypse brief covers incumbent adaptation.
3. `how-rolling-summary-memory` overlaps registry `el-context-compaction` (batch 6, OpenAI keynote) — per the batch-8 hanchett precedent it is NOT edged on an uncertain brief; flag as a merge/link target at reconciliation.
4. Effect is developed by Effectful Technologies — company not coined (never discussed as a company in the talk); `el-effect-ts` carries the website instead.
5. Sandboxing deliberately not mapped to registry sandbox elements (`el-microsandbox`, `el-firecracker`, `el-microvm`) — the talk names no underlying technology.
6. Two signals share `pat-harness-over-model` and two share `pat-verification-gap` — the talk is a harness-engineering catalog; briefs differ enough to keep all five.
