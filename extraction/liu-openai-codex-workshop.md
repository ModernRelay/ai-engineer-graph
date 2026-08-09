# SPIKE extraction — "Full Workshop: Setting Yourself Up for Success" (Jason Liu, OpenAI Codex) — FOR REVIEW

Source transcript: `transcripts/liu-openai-codex-workshop.txt` (auto-captions, ~10.6k words — quotes are paraphrases, not verbatim; many phrases are stutter-duplicated in the captions; "Codeex"/"codecs" → **Codex**, "monorreo" → **monorepo**, "appshots"/"app shots" → **appshots**).
Video: https://youtu.be/il1c1a2FufU · published 2026-07-24 (AI Engineer, World's Fair — full workshop).
`stagingTimestamp` for the artifact and all signals: 2026-07-24 (publish date).
Entities marked **[registry]** already exist — edges link, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-liu-codex-workshop` | Setting Yourself Up for Success (Jason Liu, OpenAI Codex — AI Engineer World's Fair full workshop) | youtube | https://youtu.be/il1c1a2FufU |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-jason-liu`.

## Experts (1 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-jason-liu` | Jason Liu (OpenAI; developer-experience team — "I make a lot of demos") | `co-openai` **[registry]** |

## Companies (1 registry reuse)

| slug | name | type | note |
|---|---|---|---|
| **[registry]** `co-openai` | OpenAI | bigtech | Speaker's employer; the whole workshop is Codex practice |

## Elements (7 new; 3 registry reuse)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-appshots` | Appshots | technology | harness | Codex capture that sends not just a screenshot image but the app's entire accessibility tree (channel IDs, user IDs, field IDs), so a task that used to need OCR + multi-hop tool discovery collapses to a single one-hop tool call; Liu's most-cited feature and primary context-ingestion path |
| `el-codex-skills-plugins` | Codex skills & plugins | concept | harness | Skills = a few files + scripts; plugins = a library of skills; skills self-improve (allowed to edit their own file when they learn); installable from an in-app registry (Slack/Gmail/Teams/Notion/Linear/Obsidian) plus external registries (skillset.sh, Vercel skills); team-shared plugins are the "AI champion" force-multiplier (reward = how often teammates use your plugin, not tokens burned) |
| `el-codex-pinned-threads` | Codex pinned threads | concept | harness | Pinned, self-managing threads that behave like teammates: pin + rename to a project ID, delegate to sub-agents, create new threads, write to memory; threads can list/rename/message each other, composing into manager-threads directing IC-threads — an org of agents |
| `el-codex-heartbeat-automations` | Codex heartbeat automations | concept | harness | "Loop"/"keep an eye on this every 30 min" automations that schedule a message back into the *same* thread (not a new one each time), waking a thread over time to take real-world actions |
| `el-codex-goals` | Codex goal / ultra-goal | concept | harness | `slash goal` defines a verification step and loops until it passes; ultra-goal externalizes the goal + plan to an editable `goal.md` (plus a work-log/`state.md`) so scope can change mid-run; with a good verifier, large autonomous migrations become tractable |
| `el-personal-memory-vault` | Personal memory vault (monorepo) | concept | context | A personal monorepo kept as a git repo that the agent reads and gardens; front-matter links each project file to its relevant Slack channels and each person file to their emails/Slack/connectors; code is stored outside it (via AGENTS.md); `git diff` to review what the agent updated |
| `el-codex-computer-use` | Codex computer use | technology | harness | Codex's computer-use + Chrome extension that controls any application in the background without taking over the screen; "locked use" lets you trigger it from your phone while the laptop is closed; used for tasks the CLI can't do (fill a form, edit iMovie, DocuSign + fax) |

| slug | reuse | note |
|---|---|---|
| **[registry]** `el-codex` | OpenAI Codex | the app/harness the workshop is entirely about |
| **[registry]** `el-agents-md` | AGENTS.md | used to route file-saving ("save code in /dev, not the monorepo") and per-project instructions |
| **[registry]** `el-context-compaction` | Context compaction | the enabling capability behind long-lived pinned threads |

Element edges: all seven new elements `DevelopedByCompany → co-openai` **[registry]** and `IdentifiedInArtifact → ia-aie-liu-codex-workshop`; `el-codex` `UsesElement → el-appshots`, `UsesElement → el-codex-skills-plugins`, `UsesElement → el-codex-pinned-threads`, `UsesElement → el-codex-goals`, `UsesElement → el-codex-computer-use`; `el-codex-pinned-threads` `UsesElement → el-codex-heartbeat-automations`; `el-personal-memory-vault` `UsesElement → el-agents-md` **[registry]**; `el-context-compaction` **[registry]** `EnablesElement → el-codex-pinned-threads`; `el-codex-skills-plugins` `UsesElement → el-agent-skills`? (see Review note 4 — left unedged); `el-codex-goals` `EnablesPattern → pat-verification-gap` **[registry]**.

## Signals (6 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-liu-codex-workshop`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-openai` **[registry]**.

| slug | name / brief | FormsPattern | OnElement |
|---|---|---|---|
| `sig-compaction-kills-new-thread-rule` | Practitioner claim: context compaction now works well enough that the old advice ("start a new thread after ~20 messages, one conversation per feature") is obsolete — Liu runs pinned threads 5 weeks old with ~400 sub-agents that still know their job; the pattern is pin + rename + delegate + write-to-memory + wake-on-automation | `pat-harness-over-model` **[registry]** | `el-context-compaction`, `el-codex-pinned-threads` |
| `sig-threads-as-agent-org` | Threads can now list/rename/message each other, so a single user goes from "IC enabled by an IDE" to manager of teammate threads, then to manager-threads directing IC-threads — an org of self-managing agents; "where the puck is going"; Liu: "I've become a worse and worse manager over time" as the AI needs only a high-level ask | `pat-value-of-judgement` **[registry]** | `el-codex-pinned-threads` |
| `sig-appshots-accessibility-tree` | Appshots carry the app's full accessibility tree (channel/user IDs) alongside the image, collapsing OCR + multi-hop tool discovery into a single one-hop tool call — a far richer, cheaper context-ingestion path than a plain screenshot; "haven't filled out a form in two weeks" | `pat-harness-over-model` **[registry]** | `el-appshots`, `el-codex-computer-use` |
| `sig-self-improving-team-skills` | Skills are a few files + scripts, packaged into plugins; the highest-leverage move for a company's "AI champion" is building team-shared plugins (rewarded by teammate usage, not tokens burned); skills self-improve (allowed to edit their own file on learning); "review my code like Charlie" skills encode a specific reviewer's past year of PR feedback | `pat-harness-over-model` **[registry]** | `el-codex-skills-plugins` |
| `sig-voice-first-agent-input` | Liu works voice-first — a "foot pedal" (transcribe + enter buttons) and messy 15-minute voice memos (you talk ~3× faster than you type); "there's no future where text input is the thing that matters"; dictation as the primary interface frees him to be present with coworkers while the AI runs | `pat-value-of-judgement` **[registry]** | `el-codex` **[registry]** |
| `sig-goal-verifier-loops` | Goal/ultra-goal: define a verification step and loop until it passes; with a good verifier, big autonomous migrations become tractable — Liu rewrote the Rich terminal library, UV, and TypeScript into Rust at ~100% test coverage via goal loops; ultra-goal's editable `goal.md` lets scope change mid-run | `pat-verification-gap` **[registry]** | `el-codex-goals` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-context-in-work-actions-out` | Working in Codex has three acts — bring context in (voice, plugins/connectors, appshots), do the work (in-app), take actions out in the real world; with coding "solved," mastery is less about writing code and more about knowing what you can do and how to organize the work product (a new thread? a skill? a goal? a doc?) | `pat-value-of-judgement` **[registry]** | `el-codex` **[registry]** |
| `ins-invest-in-memory-and-plugins` | The compounding investments are a personal memory system and team plugins: like an employee of seven years, an agent with long history + pinned threads + memory needs only a high-level ask; the "AI champion" who builds team plugins becomes a company-wide force multiplier | `pat-harness-over-model` **[registry]** | `el-personal-memory-vault` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-liu-codex-workshop`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-codex-personal-memory-vault` | Run a personal monorepo memory vault | Keep one pinned project (personal monorepo) as a git repo; store code outside it (AGENTS.md: "save code in /dev"); add front-matter to each project file linking its relevant Slack channels, and to each person file their emails/Slack/work addresses, so the agent reads the right context automatically; make the vault a git repo and `git diff` to review what the agent changed; optionally run automations that garden the vault | `el-personal-memory-vault`, `el-agents-md` **[registry]**, `el-codex` **[registry]** |
| `how-threads-as-teammates` | Operate pinned threads as teammates with heartbeats and goals | Pin a thread, rename it to the project ID, let it delegate to sub-agents / create threads / write memory; wake it with a heartbeat ("keep an eye on this every 30 min" schedules a message back into the *same* thread); for long-running work use goal/ultra-goal with a real verifier plus an editable `goal.md` and a work-log/`state.md`; a chief-of-staff thread that checks all connectors each morning becomes a single source of truth for your day | `el-codex-pinned-threads`, `el-codex-heartbeat-automations`, `el-codex-goals` |
| `how-appshots-context` | Feed rich context with appshots instead of screenshots | Prefer appshots — they carry the app's accessibility tree (channel/user IDs) so the model skips OCR and multi-hop discovery and acts in one tool call; appshot a Slack channel to post with the exact channel/user IDs; appshot a form and let Codex fill it (Chrome extension in Chrome, computer use elsewhere); appshot a video/doc to summarize while you keep working | `el-appshots`, `el-codex-computer-use` |

## Dropped

- OpenClaw + Hermes agent (`el-openclaw`, `el-hermes-agent` **[registry]**) — named once in a Q&A comparison ("what's the difference between this and an open claw and a Hermes agent"); Liu declines to draw a sharp line; no edge.
- Model-choice asides (GPT-5.5 vs "5.3 Spark" for simple computer-use tasks; auto-review vs full-auto/YOLO permissions) — operational preferences, folded into prose; no nodes.
- Org admin guardrails (can't MCP-email a non-OpenAI address; no external Slack) — security controls mentioned in Q&A; noted, no signal.
- "Write like me" style-guide skill, flight-check-in Spark agent, iMovie export loop — concrete anecdotes illustrating `el-codex-skills-plugins` / `el-codex-heartbeat-automations`; folded in.

## Review notes

1. **Signal count = 6 (task max).** This is a ~10.6k-word practice workshop; signals are practitioner-testimony (adoption claims and technique observations), not dated external facts — cut to 4 (`sig-compaction-kills-new-thread-rule`, `sig-appshots-accessibility-tree`, `sig-self-improving-team-skills`, `sig-goal-verifier-loops`) if you want the two "human-reallocation" claims (`sig-threads-as-agent-org`, `sig-voice-first-agent-input`) as insights instead.
2. **Affiliation flagged.** The transcript states only "I'm Jason. I work at OpenAI" (DX team); it does **not** mention the Instructor library or independent consulting. Credited `co-openai` **[registry]** on transcript evidence alone — do not assert Instructor authorship from this source; verify identity before public-facing use.
3. Pattern homes: the technique/adoption claims → `pat-harness-over-model` **[registry]** (portable scaffolding — skills/plugins/memory/appshots — carries the work around a swappable model); the human-reallocation claims → `pat-value-of-judgement` **[registry]** (human moves to relationships/judgment while agents execute). `sig-threads-as-agent-org` and `ins-invest-in-memory-and-plugins` are also evidence for the uncoined **`pat-ai-native-org`** candidate (an org of self-managing agents; the AI-champion force-multiplier) — noted, not edged.
4. **Element scope.** Seven new Codex-feature elements is high; several are product features. Merge candidates at reconciliation: `el-codex-heartbeat-automations` into `el-codex-pinned-threads`; `el-codex-skills-plugins` could `UsesElement → el-agent-skills` **[batch1]** (left unedged pending the merge call). Kept distinct because each is a named, reusable construct the workshop teaches.
5. `el-context-compaction` **[registry]** (batch 6, embiricos/OpenAI) reused as the enabling capability — `EnablesElement → el-codex-pinned-threads` is the load-bearing link ("all of this really is due to the fact that compaction works").
