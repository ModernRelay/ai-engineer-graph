# SPIKE extraction — "Agent Frameworks Considered Harmful" (Rémi Louf, .txt) — FOR REVIEW

Source transcript: `transcripts/louf-dottxt-agent-frameworks-harmful.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/KHudyx5wW3U — AI Engineer World's Fair (leadership track), published 2026-08-22.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-22 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the CEO of a 15-person structured-outputs company took two weeks off in January (after the Opus 4.6 "step function") to build "the dumbest thing that could work" for his morning briefing — and each failure (duplicate posts, a vanished voice note, an unversioned prompt change) turned into a piece of a **runtime**: markdown-defined agents, an event-driven topology instead of graphs, an append-only causal event log, and **content-addressed prompts** that make what the model saw diffable and replayable. Now 20 agents run inside the company, many contributed by non-technical staff. Caption garbles: "dot.text" → **.txt** (the company), "Opus 4.6" kept, "code X"/"Codex" kept, "Cortex" → ⚠ unclear (likely Codex), "linear PTROS" → Linear / PRs, "LMCBP" → ⚠ unclear, "Intropic" → **Anthropic**, "next" → **Nix** (build system), "get" → **git**, "KV cash" → **KV cache**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-louf-dottxt-agent-frameworks-harmful` | Agent Frameworks Considered Harmful (Rémi Louf, .txt — AI Engineer World's Fair) | youtube | https://youtu.be/KHudyx5wW3U |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-remi-louf`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-remi-louf` | Rémi Louf (CEO, .txt) | `AffiliatedWithCompany → co-dottxt` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-dottxt` | .txt | developer | 15-person company specializing in structured outputs ("our specialty — three years"); the runtime became an internal dogfooding project (~20 agents deployed, an internal "intranet" of briefs), open-sourced, explicitly not a product |

Reused **[registry]**, edge-only: `co-anthropic` **[seed]** (Opus 4.6 as the step function; "terrible at structured outputs" — ~20% of events rejected — which is why typed boundaries became non-negotiable), `co-openai` **[registry]** (Codex used to write the first version; its chat view "is a lie" about what the model saw).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-markdown-agents-over-frameworks` | Markdown agents over frameworks | concept | harness | With frameworks he "spent all my time editing the prompt within the code." Instead: an agent is a YAML/markdown file — versioned, diffable, reviewed in a PR — dropped in a folder, picked up by the runtime. "Frameworks just call code; your agents live inside their abstractions." Kernel analogy: the runtime schedules, isolates and journals agent processes; the markdown definition is user land (a front end that doesn't use markdown at all also exists) |
| `el-event-driven-agent-topology` | Event-driven agent topology | concept | harness | Cron covers *when* (one point in time); events cover *because this happened*. Each agent declares what it accepts and what it returns as typed events (voice note → `voice note processed`; the daily-brief agent subscribes to that plus the cron output; a Slack poster subscribes to `slack.message.post`). "Frameworks will sell you graphs. You do not need graphs. All you need is events — no edges to maintain; agents subscribe; anyone can edit; drop a file and the topology emerges — whatever the log says happened" |
| `el-append-only-event-log-as-memory` | The append-only event log | technology | harness | "The log is the system's memory. Nothing is lost and everything is observed": one append-only events table, events causally linked (which event triggered which), everything queryable — built because a voice note vanished and a brief posted twice (no queue, no attempt counting). Debugging headaches start "even with three agents" |
| `el-content-addressed-prompts` | Content-addressed prompts | technology | context | What a coding agent shows you "is kind of a lie" — compaction, quirks, hidden thinking traces mean you don't know what the model saw. So every prompt part (system prompt, each skill description, tool descriptions, user message) is stored by hash and a prompt is a list of hashes; the answer is stored the same way. Like git or Nix. Gives **exact provenance of context**, **diffs between runs** (which components changed), **replay** (rebuild the request, resend to a different model — how he re-evaluated open-source models when cost ramped), easier compaction ("you manipulate a graph, not strings") and indirectly KV-cache management. "Probably the main advantage at scale is auditability" |
| `el-typed-boundaries-kernel` | Typed boundaries: the kernel makes bad actions impossible | concept | harness | "The job of the kernel is to make bad actions impossible, not just unlikely." Two boundaries between an agent and the world: **typed tool calls** (no calling tools that don't exist) and **typed events** between agents — "non-negotiable, you get a lot of errors just from this." Structured outputs are the enforcement; ~20% of events were rejected before typing |

Element edges: all five `IdentifiedInArtifact → ia-aie-louf-dottxt-agent-frameworks-harmful`.
`el-markdown-agents-over-frameworks` `UsesElement → el-background-agents` **[registry]**;
`el-event-driven-agent-topology` `UsesElement → el-append-only-event-log-as-memory`, `el-typed-boundaries-kernel`;
`el-append-only-event-log-as-memory` `UsesElement → el-durable-session-log` **[registry]**;
`el-content-addressed-prompts` `UsesElement → el-append-only-event-log-as-memory`, `el-agent-checkpoint-replay` **[registry]**, `el-context-compaction` **[registry]**, `el-prompt-caching` **[registry]**;
`el-append-only-event-log-as-memory` `ExemplifiesPattern → pat-durable-execution` **[registry]**;
`el-content-addressed-prompts` `EnablesPattern → pat-verification-gap` **[registry]**;
`el-typed-boundaries-kernel` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

Reused elements (no new nodes): `el-background-agents` **[registry]** (the "robot mower"), `el-durable-session-log` **[registry]**, `el-agent-checkpoint-replay` **[registry]**, `el-context-compaction` **[registry]**, `el-prompt-caching` **[registry]**, `el-agentic-surface-generations` **[registry]** (his TUI → phone-app → background-agent ladder), `el-codex` **[registry]**.

## Signals (6 new)

All: `SpottedInArtifact → ia-aie-louf-dottxt-agent-frameworks-harmful`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-dottxt`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-runtime-emerged-from-failures-in-two-weeks` | harness | After the Opus 4.6 step function a 15-person CEO took two weeks to build the dumbest thing that could work; day one via Codex, then it broke — duplicate briefs, a vanished note, an unversioned prompt — and "each failure led to building one piece of what turned out to be a runtime": a log, a queue with attempt counts, content addressing. "Nothing new under the sun; good old distributed-systems engineering." The infra category "is definitely unsettled — build before you buy" | `FormsPattern → pat-durable-execution` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-append-only-event-log-as-memory`, `el-markdown-agents-over-frameworks` |
| `sig-events-not-graphs` | harness | Against framework orthodoxy: agents declare accepted/returned events and subscribe; no graph, no edges to maintain, no code — "drop a file and the topology emerges." Markdown definitions mean non-engineers contribute agents; a month after internal deployment, 20 agents were running, "not just contributed by technical people." Orchestration collapses into a log and a folder | `FormsPattern → pat-harness-over-model` **[registry]**; `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-event-driven-agent-topology`, `el-markdown-agents-over-frameworks` |
| `sig-content-addressed-prompts-make-agents-auditable` | context | The chat view of a coding agent is a lie about what the model saw (compaction, quirks, undisclosed thinking). Hashing every prompt part turns a prompt into a list of hashes, giving exact context provenance, diffs between runs, exact replay against another model, easier compaction and cache management — "the main advantage at scale is auditability." Verification of an agent's behavior becomes a build-system property | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-durable-execution` **[registry]** | `OnElement → el-content-addressed-prompts`, `el-agent-checkpoint-replay` **[registry]** |
| `sig-typed-boundaries-make-bad-actions-impossible` | harness | ~20% of events were rejected when a frontier model produced malformed structured outputs, which is why typed tool calls and typed inter-agent events became non-negotiable: "the job of the kernel is to make bad actions impossible, not just unlikely." Same architecture as Maersk's "please be careful is not a guard" — the constraint lives in the runtime's types, not in the prompt | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-typed-boundaries-kernel` |
| `sig-open-source-models-good-enough-for-background-agents` | inference | Once replay existed and cost ramped, he rebuilt every request against open-source models and switched: "I don't have any third-party APIs anymore," including a local model on the laptop — "good enough for what I do; for coding, I don't know." For the background-agent class (briefs, transcription, triage) the frontier model was swappable | `FormsPattern → pat-model-not-bottleneck` **[registry]**; `FormsPattern → pat-sovereign-ai` **[registry]** | `OnElement → el-content-addressed-prompts`, `el-background-agents` **[registry]** |
| `sig-tuis-and-phone-agents-are-transitional` | | The interface ladder as lived: a TUI is "a robot mower you still have to sit on"; the lab's phone apps ("SSH web vibes") are a remote control you steer on a walk — "kind of absurd, clearly transitional." The destination is the unattended background agent whose brief "just appears" — which is what changed the company's trajectory | | `OnElement → el-agentic-surface-generations` **[registry]**, `el-background-agents` **[registry]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-the-runtime-emerges-from-the-failures` | The durable claim is that the agent runtime is not designed but *precipitated*: every classic distributed-systems failure (duplicates, loss, unversioned change) reappears within days of running three background agents, and the fixes — a causal append-only log, queues with attempt counts, content-addressed inputs — are the runtime. Frameworks that hide these inside abstractions delay the failures rather than prevent them; hence "build before you buy" while the category is unsettled and "eat your own dog food" to those who sell it | `HighlightsPattern → pat-durable-execution` **[registry]** | `ReliesOnElement → el-append-only-event-log-as-memory`, `el-event-driven-agent-topology`, `el-markdown-agents-over-frameworks` |
| `ins-the-prompt-is-a-build-graph` | Treating a prompt as a content-addressed graph of parts (system, skills, tools, message) rather than a string converts the hardest agent question — *what did the model actually see?* — into a solved build-system problem: provenance, diff, replay, cache. It is the most concrete auditability mechanism in the corpus and the reason model swaps (frontier → open-source) became a re-run rather than a rewrite | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-content-addressed-prompts`, `el-typed-boundaries-kernel` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-louf-dottxt-agent-frameworks-harmful`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-a-background-agent-runtime` | Markdown, events, a log, and hashes | Define agents as markdown/YAML files that are versioned and reviewed in PRs, dropped into a folder the runtime watches; run them on cron for *when* and on **typed events** for *because this happened* — each agent declares what it accepts and emits; skip graphs, subscribe to events; keep **one append-only, causally linked, queryable event log** as the system's memory and add a real queue with attempt counting before you get duplicates; store every prompt part **content-addressed** so a prompt is a list of hashes and you can trace what the model saw, diff runs, and replay against another model; make **typed tool calls and typed events non-negotiable** so the kernel makes bad actions impossible; separate kernel (schedule, isolate, journal) from user land (the definitions); re-evaluate open-source models by replay once observability shows cost; build before you buy while the category is unsettled; and if you sell a framework, eat your own dog food | `ReferencesElement → el-markdown-agents-over-frameworks`, `el-event-driven-agent-topology`, `el-append-only-event-log-as-memory`, `el-content-addressed-prompts`, `el-typed-boundaries-kernel` |

## Dropped

- **The castle office / robot mower framing** — kept as one phrase in `el-background-agents` reuse.
- **"Don't tell my board"** — color.
- **The blog post / repo pointers** — no URL recoverable from captions.

## Review notes

1. **⚑ `pat-durable-execution` from the demand side, in miniature.** Louf independently re-derived the layer (log, queue, replay, typed boundaries) from three agents in two weeks and concludes "build before you buy" — a demand-side counterweight to the vendor talks (Navan/Warp/Docker) in the same batch. Worth pairing in the pattern brief.
2. **`el-content-addressed-prompts` is genuinely new to the corpus** — provenance/diff/replay at the prompt-part level. Cross-links to `el-agent-checkpoint-replay`, `el-durable-session-log`, `el-flat-trace-log` are by `UsesElement`; review may want a "prompt provenance" thread if it recurs.
3. **`sig-tuis-and-phone-agents-are-transitional` is held pattern-less** — texture for b19's `el-agentic-surface-generations`; if the "background agents as the destination surface" claim recurs it belongs with the uncoined `pat-liquid-software` ledger (interfaces dissolving into unattended agents).
4. **⚠ Verify before seeding:** "Opus 4.6" as the December step function, the ~20% rejected-events figure, "20 agents after a month," and the garbled "Cortex"/"LMCBP" references.
