# SPIKE extraction — "How to Generate Mergeable Code with a Context Engine" (Peter Werry, Unblocked) — FOR REVIEW

Source transcript: `transcripts/werry-unblocked-mergeable-code-context-engine.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/qdAkxLoYNI8 — AI Engineer World's Fair, published 2026-08-27.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-27 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: Unblocked builds a **context engine** — organizational context (intent, conventions, past decisions, Slack discussions, architecture rationale) delivered to humans and agents. The problem: "you were the context layer," and agents are expert new employees who **reset their knowledge every task**; access to information isn't understanding — agents suffer **satisfaction of search** (find one thing and stop), don't distill how pieces fit, and get distracted if you dump everything into the window. Demo: a Claude Code optimization plan with vs without the engine — about half the time and cost, and the right plan because it found the PRs, Slack threads and docs where the idea was discussed; a customer reports 50% fewer tokens. Plus an expertise/social graph from review relationships, a code-review agent that surfaces senior engineers' prior comments, and open-source pieces (document query engine, context-engine simulator). Caption garbles: "Unblocks" → **Unblocked**, "Vim" → ⚠ the maturity-curve slide's author (unclear), "GBT35" → **GPT-3.5**, "Claude 48" → **Claude Opus 4.8**, "Tariq from Claude Code" / "Tariq from Sonar" → the keynote speakers.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-werry-unblocked-mergeable-code-context-engine` | How to Generate Mergeable Code with a Context Engine (Peter Werry, Unblocked — AI Engineer World's Fair) | youtube | https://youtu.be/qdAkxLoYNI8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-peter-werry`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-peter-werry` | Peter Werry (Unblocked) | `AffiliatedWithCompany → co-unblocked` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-unblocked` | Unblocked | developer | Builds a context engine delivering organizational context to humans and agents: a Q&A surface that shows its work (generated architecture diagrams, sources), a Slack presence that chimes in when confident, a cloud agent that relates its fixes to the conversations that motivated them, a code-review agent boosted by an expertise graph; open-source document query engine, engineering social graph, and a context-engine simulator. Customer quote: "50% fewer tokens, faster triage, better answers" |

Reused **[registry]**, edge-only: `co-anthropic` **[seed]** (Claude Code as the agent in the demo; the Opus 4.8 switch that changed review behavior). Referenced, not coined: Cursor and Copilot (maturity-curve stages), Notion.

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-context-engine` | The context engine | product | context | Delivers organizational context — beyond the code an agent can see: actual intent, team conventions, past decisions, Slack discussions, architecture rationale — to human workers and, increasingly, agents. Ingests PRs, Slack, Notion and architecture docs; answers questions with generated diagrams and cited sources ("show your work" builds trust and lets people correct the knowledge base); listens in Slack and chimes in when confident; generates best practices from PR history to align agents; feeds a code-review agent and a cloud agent whose PRs explain "this was created because…" with the correlated Slack thread |
| `el-agents-reset-like-new-employees` | Agents reset their knowledge every task | concept | context | Before agents, "you were the context layer": trawling data sources and discussions, building tribal knowledge, accumulating battle scars from incidents. Agents inherit all those challenges plus one: they reset every task — an expert engineer onboarding for the first time, rediscovering the codebase, how you build, test and deploy, on every task. The human layer hasn't gone away — accountability stops with whoever hits merge |
| `el-context-maturity-curve` | The AI maturity curve: context is the bottleneck | concept | | Autocomplete (GPT-3.5-era Copilot) → Cursor → organizational wikis → MCP and skills to teach agents to navigate (where most teams are: stage four or five, aware that context is the bottleneck) → … → software factories at stage eight, "where the puck is going": full automation that cannot operate without organizational context and the delivery of unknown unknowns |
| `el-satisfaction-of-search` | Satisfaction of search | concept | context | Access to information doesn't equal understanding. Attaching a wiki doesn't tell an agent where the needed information is; searching it triggers the radiologist's *satisfaction of search* — find one indicator and stop, missing the others. Agents don't distill how dependencies, architecture and future plans fit together without prior legwork. Dumping the whole codebase and docs into a million-token window fails too: it exceeds the window and distracts the agent from task-specific flow, wasting tokens and time |
| `el-engineering-social-graph` | The engineering social graph | technology | context | Review relationships between engineers, clustered into team labels, mapped to codebase coverage — showing where expert coverage is missing — and used inside the context engine as an expertise signal: seniority boosts which prior review comments the review agent surfaces ("that's something I would say" — it was). Open-sourced alongside a document query engine (ingests historical PRs, synthesizes a schema, answers arbitrary queries) and a context-engine simulator that runs a task with and without built-up context |

Element edges: all five `IdentifiedInArtifact → ia-aie-werry-unblocked-mergeable-code-context-engine`.
`el-context-engine` `DevelopedByCompany → co-unblocked`;
`el-context-engine` `UsesElement → el-agents-reset-like-new-employees`, `el-satisfaction-of-search`, `el-engineering-social-graph`, `el-company-brain` **[registry]**, `el-claude-code` **[registry]**;
`el-context-maturity-curve` `UsesElement → el-agents-md` **[registry]**, `el-generated-wiki` **[registry]**, `el-mcp` **[seed]`, `el-agent-skills` **[registry]**, `el-software-factory` **[registry]**;
`el-satisfaction-of-search` `UsesElement → el-context-acquisition-gap` **[registry]**;
`el-context-engine` `ExemplifiesPattern → pat-context-graphs` **[registry]**;
`el-agents-reset-like-new-employees` `ExemplifiesPattern → pat-agent-memory-layer` **[registry]**;
`el-engineering-social-graph` `EnablesPattern → pat-verification-gap` **[registry]**.

Reused elements (no new nodes): `el-company-brain` **[registry]**, `el-claude-code` **[registry]**, `el-agents-md` **[registry]**, `el-generated-wiki` **[registry]**, `el-mcp` **[seed]**, `el-agent-skills` **[registry]**, `el-software-factory` **[registry]**, `el-context-acquisition-gap` **[registry]**, `el-context-layer` **[registry]**.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-werry-unblocked-mergeable-code-context-engine`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-unblocked`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-agents-reset-knowledge-every-task` | context | The framing a context-engine vendor gives the memory problem: humans used to be the context layer; agents are expert new hires who forget the codebase, the build, the tests and the deploy path on every task, and full automation "just can't operate without organizational context — they get lost." Most teams are at the MCP-and-skills stage and know context is the bottleneck | `FormsPattern → pat-agent-memory-layer` **[registry]**; `FormsPattern → pat-context-graphs` **[registry]** | `OnElement → el-agents-reset-like-new-employees`, `el-context-maturity-curve` |
| `sig-context-engine-halves-cost-and-compounds` | context | Live: Claude Code producing an optimization plan without the engine took ~2 minutes and cost more; with it, ~1 minute and sub-dollar — and it "nailed the nuances" because it found the PRs, Slack threads and docs where improvements had been discussed, with sources Claude could jump to. The value is not the upfront saving but the compounding: without the right context the agent operates on the wrong plan and loops. A customer: 50% fewer tokens, faster triage, better answers | `FormsPattern → pat-context-graphs` **[registry]**; `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-context-engine`, `el-claude-code` **[registry]** |
| `sig-satisfaction-of-search-agents-stop-early` | context | Why wikis and context-stuffing fail: an agent searching a wiki finds one plausible thing and stops (radiology's satisfaction of search), never distills how dependencies and architecture fit, and a million-token dump distracts it from task flow. "Access to information doesn't equal understanding" — the engine must deliver the unknown unknowns for the task, not everything | `FormsPattern → pat-context-graphs` **[registry]** | `OnElement → el-satisfaction-of-search`, `el-context-acquisition-gap` **[registry]** |
| `sig-expertise-graph-boosts-review-context` | harness | A social graph built from who reviews whom yields team clusters, coverage gaps, and an expertise signal that boosts senior engineers' prior comments in automated review — a reviewer recognizing his own past guidance surfaced by the agent. The same graph powered the debugging and fix of a drop in surfaced review issues after a model switch, with the fix PR citing the Slack thread that explained it | `FormsPattern → pat-context-graphs` **[registry]**; `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-engineering-social-graph`, `el-context-engine` |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-context-must-be-delivered-not-just-accessible` | The durable claim separates access from understanding: agents that can search everything still stop at the first plausible answer and never assemble the architecture, so the missing layer is one that *delivers* task-relevant organizational context — intent, decisions, conventions, discussions, expertise — with provenance the agent can follow. The measured effect is cost and time halved on a single plan and correctness that compounds across loops; the organizational effect is that the human context layer is finally externalized | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-context-engine`, `el-satisfaction-of-search`, `el-agents-reset-like-new-employees`, `el-engineering-social-graph` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-werry-unblocked-mergeable-code-context-engine`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-give-agents-organizational-context` | Deliver the unknown unknowns, with provenance | Assume every agent task starts as a new hire's first day and plan the context accordingly; don't rely on a wiki plus search (satisfaction of search) or on stuffing the codebase and docs into the window (distraction, waste) — build or buy a **context engine** that ingests PRs, Slack, docs and architecture rationale, and delivers task-specific context with sources the agent can follow; make it show its work so humans can correct the knowledge base; derive best practices from PR history to align agents and reviewers; build an **expertise graph** from review relationships to find coverage gaps and boost senior guidance in review; measure with and without context (time, cost, plan quality) and expect the gain to compound over loops; and keep the human accountable at merge | `ReferencesElement → el-context-engine`, `el-satisfaction-of-search`, `el-agents-reset-like-new-employees`, `el-engineering-social-graph`, `el-context-maturity-curve` |

## Dropped

- **Demo navigation hiccups, the coconut, and the pointer to a colleague's talk** — color.
- **The source-mark-engine internals** — the demo subject; not a claim.

## Review notes

1. **`pat-context-graphs` support from a context-engine vendor with a measured demo** (~2× time/cost on one plan; customer 50% tokens). Together with Uber's graph and Qodo's software graph this batch, the pattern has a strong coding-domain cluster; Box's counter (b22) stands beside it.
2. **`el-satisfaction-of-search`** is a useful new name for a known failure mode; cross-links to `el-context-acquisition-gap` and `el-context-rot` by `UsesElement`/notes.
3. **⚠ Verify before seeding:** the demo timings/costs, the "50% fewer tokens" customer quote, the maturity-curve slide's attribution, and the Opus 4.8 review-behavior anecdote.
