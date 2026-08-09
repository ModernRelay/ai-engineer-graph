# SPIKE extraction — "The Golden Age of AI Engineering" (Alexander Embiricos, Romain Huet & Peter Steinberger, OpenAI) — FOR REVIEW

Source transcript: `transcripts/embiricos-huet-steinberger-openai-golden-age.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/pMggiOb18tc — AI Engineer World's Fair keynote, published 2026-07-09.
`stagingTimestamp` for the artifact and all dated nodes (signals, knowhows): 2026-07-09 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-openai-golden-age` | The Golden Age of AI Engineering (Alexander Embiricos, Romain Huet & Peter Steinberger, OpenAI — AI Engineer World's Fair keynote) | youtube | https://youtu.be/pMggiOb18tc |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-alexander-embiricos`, `ContributedByExpert → exp-romain-huet`, `ContributedByExpert → exp-peter-steinberger`.

## Experts (3 new)

| slug | name | edges |
|---|---|---|
| `exp-alexander-embiricos` | Alexander Embiricos (product lead on Codex at OpenAI) | `AffiliatedWithCompany → co-openai` **[registry]** |
| `exp-romain-huet` | Romain Huet (head of developer experience, OpenAI; "the demo god" — live-demo keynotes since Dev Day 2024) | `AffiliatedWithCompany → co-openai` **[registry]** |
| `exp-peter-steinberger` | Peter Steinberger (creator of OpenClaw — "the claw father"; PSPDFKit founder; joined OpenAI in 2026; registry already credits him as author of `el-oracle-cli`) | `AffiliatedWithCompany → co-openai` **[registry]** |

## Companies (0 new)

Reused: `co-openai` **[registry]**. Cerebras (5.6 Sol served at 750 tok/s) mentioned in prose only — not load-bearing enough to coin.

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-codex` | OpenAI Codex | product | harness | OpenAI's agentic coding system spanning CLI, IDE extension, the Codex app, iOS, and Codex Cloud; deliberately built as open layers — open-source harness, open-source app server (the same path OpenAI's own products use), open plugins (browser use, computer use, role-specific), models defaulted but not hardcoded — so anyone can fork or rebuild any layer while keeping the agent loop |
| `el-gpt-56` | GPT-5.6 model family (Sol / Terra / Luna) | product | inference | Frontier family previewed the week before the talk (early July 2026): 5.6 Sol tops Terminal-Bench; 5.6 Terra delivers GPT-5.5-level intelligence at half the cost; Luna beats notable models at $1/M input and $6/M output; Sol on Cerebras serves ~750 tokens/sec ("a substantial PR in ~10 seconds") |
| `el-agents-md` | AGENTS.md | technology | harness | Cross-agent instruction-file convention: OpenAI deliberately picked a vendor-neutral name instead of a Codex-proprietary format so other agents could adopt the same file; part of the open-layers strategy |
| `el-context-compaction` | Server-side context compaction | technology | harness | Compaction of long-running agent context done server-side; built because Codex needed it for long tasks, then baked into the responses API so external agents get the same primitive; Steinberger names it as change #1 that made long-running manager agents reliable ("I stopped optimizing around first sessions") |
| `el-agent-loops` | Agent loops (manager-agent pattern) | concept | harness | Long-lived agent cycles: persistent context + delegation + triggers (Steinberger's formula) — a schedule or event wakes a manager agent, which discovers the task, plans/writes its own prompts, delegates to worker agents, self-verifies, retries, and only surfaces a reviewable artifact (PR + issue + diff + video/VNC build) to the human; Volkov's gloss: "fancy cron jobs" that grade their own work against the goal |

Element edges: all five `IdentifiedInArtifact → ia-aie-openai-golden-age`; `el-codex` and `el-gpt-56` `DevelopedByCompany → co-openai` **[registry]**; `el-codex` `UsesElement → el-agents-md`; `el-codex` `ExemplifiesPattern → pat-harness-over-model` **[registry]**; `el-context-compaction` `EnablesElement → el-agent-loops`; `el-agent-loops` `EnablesPattern → pat-value-of-judgement` **[registry]**.

Reused in prose: `el-openclaw` **[registry]** (gateway + nodes; one of the third-party surfaces where Codex subscriptions work).

## Signals (6 new)

All: `SpottedInArtifact → ia-aie-openai-golden-age`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | domain | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-openai-6-week-model-cadence` | OpenAI's shipping cadence collapsed from a new model every ~15 months to roughly every 6 weeks; GPT-5.6 series previewed the week before the talk; capability phases (completion → inline prediction → command-K edits → models testing their own work → long-goal autonomy) each went from mind-blowing to mundane within months | training | `FormsPattern → pat-accelerated-research` **[registry]** | `RelevantCompany → co-openai` **[registry]**, `OnElement → el-gpt-56` |
| `sig-codex-open-at-every-layer` | OpenAI open-sourced the entire Codex stack around the model — harness, app server (the same path its own apps use), plugins, AGENTS.md — and states "we're not building one system for OpenAI and a second simplified one for developers"; the harness is fed into model post-training; ecosystem proof: opencode inspected the reference implementation, an outside dev built Codex Monitor on the app server before the Codex app launched and was then hired to build Codex for iOS; Codex subscriptions now work in opencode, Pi, Droids, OpenClaw, Xcode, JetBrains | harness | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-openai` **[registry]**, `OnElement → el-codex`, `OnElement → el-agents-md` |
| `sig-frontier-intelligence-price-speed` | Frontier intelligence is being repriced in real time: GPT-5.6 Terra = 5.5-level intelligence at half the cost; Luna competitive at $1/M in, $6/M out; 5.6 Sol on Cerebras at ~750 tok/s — fast enough to run five or six agent approaches in parallel and pick the best in less time than one generation used to take | inference | — (see review note 2) | `RelevantCompany → co-openai` **[registry]**, `OnElement → el-gpt-56` |
| `sig-agents-do-whole-computer-tasks` | Codex-class agents now do any task doable on a computer — the work before coding (triage, deciding why) and after (review, deploy), not just the coding; Embiricos: for a medium-length computer task with equal time, the model now does better than he does on the average task; OpenAI's stated product goal is squarely to empower engineers, not automate them (chat + a dig-in collaborative UI that preserves "the feeling of mastery") | harness | `FormsPattern → pat-value-of-judgement` **[registry]** | `RelevantCompany → co-openai` **[registry]**, `OnElement → el-codex` |
| `sig-steinberger-attention-bottleneck` | Steinberger's bottleneck migration, dated: January 2026 = 10+ terminals, "I thought I was orchestrating; really I was polling — I was the scheduler, the router, and the memory"; constraint moved tokens → compute → attention; today he manages one long-running manager agent that delegates to workers; watching agents generate code is now a waste of the one resource you can't add more of; a colleague's chief-of-staff agent wakes every 10 minutes to coordinate his GitHub work | harness | `FormsPattern → pat-value-of-judgement` **[registry]** | `RelevantCompany → co-openai` **[registry]**, `OnElement → el-agent-loops`, `OnElement → el-context-compaction` |
| `sig-local-cloud-boundary-dissolving` | The local-vs-cloud task distinction is being framed as a bug to eliminate: laptops stay open in offices so agents keep working; Codex Cloud (OpenAI's first major Codex launch) is "due major upgrades"; the target state is one agent you talk to anywhere that picks its own execution environment across your machines and the cloud; Steinberger: the manager agent "shouldn't be a session trapped inside your app" — text it, steer it from Slack; OpenAI publicly endorsed Theo Browne's tweet predicting this, saying it lands in well under 6 months | infra | — (see review note 3) | `RelevantCompany → co-openai` **[registry]**, `OnElement → el-codex` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-open-harness-flywheel` | OpenAI is running an open-ecosystem flywheel around a closed model: give away the harness, app server, plugins, and file conventions; use the identical stack internally; bake agent needs (compaction) into the public API first; feed the open harness into post-training. Every external fork and edge-case found returns as model and product improvement — the harness layer is where the ecosystem competes, while the model stays the swappable center | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-codex` |
| `ins-attention-is-the-scarce-resource` | Tokens can be bought and compute rented, but operator attention cannot be added — so agent products and workflows should be judged by where they let humans spend attention: talk-first delegation by default ("let them cook"), full-depth inspection on demand, review-once artifacts instead of streamed intermediate tokens. The engineering frontier moves from writing code to designing the loops and organizations around agents — "models are advancing faster than the harnesses and organizations around them" | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-agent-loops` |

## KnowHow (1 new)

All `SourcedFromArtifact → ia-aie-openai-golden-age`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-manager-agent-loop` | Run a manager agent, not N terminals | Replace parallel terminal-juggling with one long-running manager agent: rely on server-side compaction for persistent context; have the manager create and steer worker agents per task (investigate → implement → test → separate review agent); wire triggers so events (new issue, schedule) wake the manager against the project's goals/notes/vision; consume results as reviewable bundles (PR + original issue + diff + video or VNC-able build), review once, leave a note, let it land after checks; drop down to pair with a worker only for tricky work; stop watching code generation — spend attention on direction and decisions in the outer loop | `ReferencesElement → el-agent-loops`, `ReferencesElement → el-context-compaction` |

## Dropped

- "AI engineers are eating the world" / return-to-roots framing — keynote rhetoric, no extractable claim.
- Dev Day 2024 o1 drone demo and 2025 camera-system demo — anecdote supporting `sig-openai-6-week-model-cadence`, folded into prose.
- "Value maxing" vs "token maxing" vocabulary — coinage, kept in prose only.
- Codex image-gen illustration, World Cup score demo — color.

## Review notes

1. **Caption garbles:** "GPT 5.6 Sol" also appears as "Soul" (rendered Sol; verify official casing); "GPT 5.3 could spark" is unresolved (possibly "GPT-5.3 Codespark" — a speed-focused variant is implied); "Homan's predicted score" read as Romain's; "Toma, aka Demilyan on X" (Codex Monitor author, now OpenAI) — handle spelling unverified; "Paul" (chief-of-staff agent anecdote) surname never given, kept as prose. "Agent MD" read as AGENTS.md (matches OpenAI's public convention).
2. `sig-frontier-intelligence-price-speed` left pattern-less deliberately: the price/speed collapse is real and dated but no registry pattern captures cost-of-intelligence collapse; it indirectly feeds `pat-saaspocalypse` and `pat-model-not-bottleneck` — reconciler's call whether to add a FormsPattern edge.
3. **Added evidence for `pat-durable-execution` (candidate — NOT coined, no edges):** this is the first frontier-lab keynote to declare the local/cloud execution split obsolete — Codex Cloud upgrades, agent-picks-environment, manager agents that move work between hosts (OpenClaw gateway+nodes named as a partial form), "shut our computers" as the goal. Stacks on ZenML (b3), Inngest (b4), OpenAI sandbox-cloud (b5).
4. Steinberger's loops section overlaps Volkov's talk in this same batch (`volkov-thursdai-zl-continuum.md` reuses `el-agent-loops` defined here) and the batch-3 loops debate (`el-ralph-loop`). Loops are kept at element altitude, not pattern altitude — they're a mechanism, not an industry thesis.
5. Multi-speaker artifact: slug uses `openai` in the speaker slot (precedent: `ia-aie-msft-*` in batch 2).
6. Peter Steinberger is new as an Expert node but pre-exists in registry prose (batch-3 loops debate cites his "stop prompting, design loops" tweet; `el-oracle-cli` is his). His OpenAI affiliation is current as of this talk — earlier artifacts predate the move.
