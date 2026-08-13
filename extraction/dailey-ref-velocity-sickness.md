# SPIKE extraction — "Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster" (Matt Dailey, Ref) — FOR REVIEW

Source transcript: `transcripts/dailey-ref-velocity-sickness.txt` (auto-captions — quotes are paraphrases, not verbatim; "spectrum and development" garble resolved, see review note 2).
Video: https://youtu.be/Kz4QJmNrVXU — AI Engineer World's Fair, published 2026-08-09.
`stagingTimestamp` for the artifact and all dated nodes (signals, knowhows): 2026-08-09 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a founder names and dissects a team-level pathology — **velocity sickness**, "the stress caused by sudden output increases thanks to AI… output without impact" — then argues the cure is a new tool category (the *decision layer*: docs, not chat) where humans own decisions, agents are stateless actuators, and state lives in a shared doc. Ends with three do-today practices.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-dailey-velocity-sickness` | Velocity Sickness: What Happens When Your Whole Team Gets 10x Faster (Matt Dailey, Ref — AI Engineer World's Fair) | youtube | https://youtu.be/Kz4QJmNrVXU |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-matt-dailey`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-matt-dailey` | Matt Dailey (CEO and founder, Ref — building a tool for the decision layer; part of the job he describes is field research with practitioners "really pushing the forefront") | `AffiliatedWithCompany → co-ref` |

Kept in prose (no node): the anonymous newsletter author of the book-a-week story (deliberately unnamed by the speaker).

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-ref` | Ref | developer | Startup building a decision-layer tool for engineering teams ("individual engineers are going really fast with AI, but the team as a whole is not — we're working to close that gap"); works alongside existing implementation tools |

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-velocity-sickness` | Velocity sickness | concept | harness | Named team pathology: "the stress caused by sudden output increases thanks to AI… the result is output without impact." Four presenting symptoms, each individual-level and magnified at team scale: (1) too many PRs to merge (merge queue breaks down); (2) moving in many directions at once (engineers sprinting apart, colliding); (3) **declaring agent bankruptcy** — 12 terminals cranking all day, next morning "a room of strangers," so you discard the agents and redo the work, "spending tokens twice"; (4) the most important: critical decisions being made by agents — "you are ceding control of your code… if engineers across your team give up ownership of the code, you no longer own the product" |
| `el-decision-layer` | The decision layer | concept | harness | The stratum of engineering work the IDE was never built for: work has re-shaped into **planning** (exploratory, creative, collaborative — understanding a complex system's contours, pulling out what's relevant, expressing engineering taste) and **polish** (holding what the agent made and asking "is this what I wanted?"), with implementation in between belonging to agents ("arguably should not even be on this slide — it's not our human work anymore"). The skill becomes knowing which gear you're in and whether your tool serves it; the decision layer is where key decisions are surfaced, made and recorded — framed as a "portal to the software system": Tony-Stark-style *show me what matters*, with AI laying the relevant pieces on the table |
| `el-doc-as-shared-state` | Doc as state, agent as action | concept | context | The conceptual flip under docs-not-chat: chat is "the relic of building for implementation" — isolated, ephemeral, brain-off, with decisions disappearing into a session and into unexplained code. Instead **separate the agent (action) from the doc (state)**: do the context engineering in a durable, shared doc so every agent is stateless and starts from the same place, spawn parallel agents from one doc, and let the team read the doc to see exactly which decisions are being made. Yields a durable decision log by construction — decisions agreed up front and saved, "rather than some LLM summarizing it and maybe picking the wrong things later." Positioned deliberately between plan mode (a rich but still ephemeral chat message) and full spec-driven development (too far from engineering reality) |
| `el-idea-velocity` | Idea velocity | concept | harness | Shifting the unit of velocity from code shipped to ideas explored: when teams adopt decision-layer work, "people start to plan and then *not* implement their plan — and this is actually a really good sign," because ideas get fleshed out, compared and triaged before any build. The cure for shipping too much code that goes nowhere: escape "prototype gravity" (building the first navigable path and falling in love with it) and explore the whole idea maze to "find the gold around the corner." ⚠ terminology convergence with the b6 Snap talk (see review note 3) |
| `el-ref` | Ref (decision-layer tool) | product | harness | "A tool built for the decision layer" — doc-centric planning surface that works with existing implementation tools; the productization of the talk's docs-not-chat / stateless-agents model |

Element edges: all five `IdentifiedInArtifact → ia-aie-dailey-velocity-sickness`; `el-ref` `DevelopedByCompany → co-ref`, `UsesElement → el-doc-as-shared-state`; `el-decision-layer` `UsesElement → el-doc-as-shared-state`, `ExemplifiesPattern → pat-value-of-judgement` **[registry]**; `el-idea-velocity` `UsesElement → el-decision-layer`; `el-doc-as-shared-state` `EnablesElement → el-idea-velocity`.

Reused elements (no new nodes): `el-spec-driven-development` **[registry, b9]** (contrast anchor — see review note 2). "Plan mode" kept as prose (no registry node; one-line contrast).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-dailey-velocity-sickness`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-ref`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-velocity-sickness-pathologies` | harness | A vendor names the team-scale failure mode of AI adoption and gives it a symptom taxonomy: unmergeable PR floods; engineers sprinting in incompatible directions; **agent bankruptcy** ("you come back and it's like walking into a room of strangers… you're doing the same work and spending tokens twice"); and agents making critical decisions, which at company scale means "you no longer own the product." The emblem story: a newsletter author with an impressive, decidedly non-slop agent pipeline who is "basically writing a book every week" — asked whether his audience reads a book a week: "no, they're probably not." Output without impact, at 10×. **HELD PATTERN-LESS** — `pat-ai-native-org` ledger (uncoined): this is the candidate's pathology/dark-side texture, the team-velocity quantification the ledger has been missing between the adoption stats (Yaron, Uber) and the restructure narratives (Block) | — (held pattern-less) | `OnElement → el-velocity-sickness` |
| `sig-work-shape-flipped-ide-obsolete` | harness | The tool-category claim: pre-AI engineering was plan → heads-down build → polish, and "all our history of coding tools" — the IDE, "our workhorse" — was built for the middle. Now implementation belongs to the agent and the human work is the two ends, so the load-bearing tool slot moves to the decision layer: "a tool built for docs and not chat." A structural claim that the incumbent tool category is mis-fit to the new shape of work, and that a new layer is being productized above it | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-decision-layer`, `el-ref` |
| `sig-humans-must-own-decisions` | harness | Ranked "the most important" of the four problems: an engineer letting an agent make a critical decision "is ceding control of your code — you are no longer the owner; the agent is," and at scale the company no longer owns its product. The prescription re-defines the job: "our work now is figure out what decisions matter, then make those decisions, and then get out of the way while the agents fill in the rest" — humans owning decisions is "how we retain ownership of our software and make it a true expression of what we're trying to create" | `FormsPattern → pat-value-of-judgement` **[registry]** | `OnElement → el-decision-layer`, `el-velocity-sickness` |
| `sig-docs-replace-chats-as-work-atom` | context | The mechanism: make the doc, not the chat, the atom of work. Chats are isolated, ephemeral and "brain off" (the agent proposes, you hit the recommended option without thinking); decisions made there vanish into code. Docs bring key decisions forward for the team, and the deeper flip is architectural — **pull the state out of the session**: doc as state, agent as stateless action, parallel agents spawned from one shared context, agent bankruptcy dissolved ("the result of their work is in the doc — to rebuild your human context, you just read the doc"), and a durable decision log with no LLM-summarization lottery. **HELD PATTERN-LESS** — bears on the uncoined `pat-agent-memory-layer` and `pat-durable-execution` candidates, on the *convention* side: the state layer here is a shared document, not a memory product (see review note 4) | `ContradictsPattern → pat-agent-memory-layer` (convention-side counter, attached on coin 2026-08-14) | `OnElement → el-doc-as-shared-state`, `el-decision-layer` |
| `sig-code-velocity-to-idea-velocity` | harness | What actually happens when teams adopt the model: "people start to plan and then not implement their plan — and this is a really good sign," because exploration and triage replace reflexive building; velocity shifts "from code velocity to idea velocity." And the review economics invert: aligning on key decisions up front moves the review point earlier — "the hardest part of any code review is *what actually matters here*; if you move that earlier, the code review becomes much simpler" — which is his answer to the unmergeable-PR flood. Closing claim: "the future of engineering is multiplayer… multiplayer by default sooner than we think" | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-idea-velocity`, `el-decision-layer` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-review-moves-to-the-decision-point` | When generation industrializes, the scarce reviewing resource stops being code-reading capacity and becomes decision-alignment capacity. Post-hoc review of an agent-authored PR flood cannot answer "what matters here?" fast enough; moving review to the decision point — shared plans aligned before anyone (human or agent) spends a day building — converts unreviewable output back into simple reviews, and catches direction-divergence before it costs a prototype. Verification is re-architected *earlier in the pipeline* rather than scaled at the end | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-decision-layer`, `el-doc-as-shared-state` |
| `ins-stateless-agents-durable-docs` | Extracting state from agent sessions into a shared doc inverts who is durable: the agents become disposable actuators (spawn as many as you like from the same context, discard without loss) while the doc accumulates the team's actual asset — its decisions. That single move dissolves agent bankruptcy, makes parallelism cheap, gives humans a re-grounding surface, and produces the decision log everyone is otherwise trying to reconstruct with LLM summarizers. The layer around the model — shared, durable, human-legible state — is where team leverage lives | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-doc-as-shared-state`, `el-idea-velocity` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-dailey-velocity-sickness`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-work-in-decision-docs` | Work in decision docs, not chat sessions | Think of your work as two gears — planning and polish — and notice when you drift between them inside one session and whether your tool still fits the gear you're in; treat the plan as a portal to the software system: ask AI to pull out and arrange exactly what's relevant to the decision at hand ("show me what matters"); do context engineering in the doc so every agent is stateless and starts from the same shared state; bring key decisions forward in the doc and agree on them *before* implementation, so code review reduces to checking against decisions already aligned; expect and welcome plans that never get implemented — that is idea triage working; and **share the plan with a teammate before giving it to an agent** — "very unnatural for a lot of people… but your smart teammates have great context in their heads; they will give you good feedback" | `ReferencesElement → el-decision-layer`, `el-doc-as-shared-state`, `el-idea-velocity` |

## Dropped

- **The thumbs-up audience check and talk-structure preamble** — logistics.
- **The Tony Stark image** — kept as one clause inside `el-decision-layer`; no separate node.
- **"Everyone's company feels existential, small or big… we get through that by working together"** — motivational close; the substantive multiplayer claim is in `sig-code-velocity-to-idea-velocity`.
- **The manager-pre-AI alignment analogy** ("you would not tell a struggling team: let's all work in Slack DMs") — supporting argument, folded into `el-doc-as-shared-state`'s brief logic.

## Review notes

1. **Where the pattern weight went.** The talk's two firm coined-pattern homes are `pat-value-of-judgement` (humans-own-decisions is its purest tool-vendor statement since Osmani) and `pat-verification-gap` (review moved to the decision point). The org-pathology material was deliberately **held pattern-less** for the `pat-ai-native-org` ledger per the extraction brief — it is the strongest *dysfunction-side* evidence the candidate has (the ledger's existing points are mostly success stories plus Block's layoffs note).
2. **Garble resolved: "full-on factory spectrum and development" → full-on (software-factory) spec-driven development.** The sentence contrasts plan mode on one side and spec-driven development on the other, with the decision layer "in the middle" — the critique ("we just define the behaviors, operate at the product level — a little far away from the engineering reality") only parses against spec-driven development. `el-spec-driven-development` **[registry, b9]** reused as the contrast anchor on that basis. Lower-stakes garbles: "the stock" → *the doc* ("the result of their work is in the doc"); "seeding control" → *ceding* control.
3. **Terminology convergence — "idea velocity" (Lee-Chan, b6).** Dailey's "shifting from code velocity to idea velocity" reproduces the Snap talk's title concept ("Develop at Idea Velocity") with a different mechanism (decision docs vs layered agent org). Neither cites the other. `el-idea-velocity` is coined here because b6 never made it an element; if review prefers the term to live with its first corpus appearance, re-home the node to the Lee-Chan file and keep this file's edges.
4. **Ledger note — the "convention over infrastructure" shape, fourth practitioner.** `sig-docs-replace-chats-as-work-atom` puts agent state in a *shared document* and makes the agents stateless — the same architecture-as-convention shape as HumanLayer (loops on stock CI, b13), Netflix (memory as markdown in git, b14) and FlyersSoft (durability from stock Cosmos DB, b15), here from a vendor whose *product is the convention's surface*. Bears on both `pat-agent-memory-layer` and `pat-durable-execution` coin decisions; no edge emitted.
5. **Same-batch convergence with the Gazit/GitHub file.** GitHub Next's Ace lands on the identical mechanism independently — shared plan docs edited by the team, "edit the document and tell AI: make the document true" — and that file *reuses* `el-doc-as-shared-state` (defined here) with a convergence flag. Two vendors (a startup and GitHub) productizing doc-as-state in the same week is coin-relevant texture for any future "doc-centric development" candidate; none proposed (mechanism, not thesis).
6. **Signal-bar caveat.** No external numbers: the pathology taxonomy is the vendor's framing of prospect pain, and "what happens when teams implement this" is testimony about Ref's own users, unnamed and uncounted. The strongest externally-citable content is the conceptual architecture, not quantities. The newsletter-author story is second-hand and anonymized.
