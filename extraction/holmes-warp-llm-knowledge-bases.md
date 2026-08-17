# SPIKE extraction — "LLM Knowledge Bases: a practical guide" (Ben Holmes, Warp) — FOR REVIEW

Source transcript: `transcripts/holmes-warp-llm-knowledge-bases.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/I3bpdgFJCUY — AI Engineer World's Fair, **Continual Learning track**, published 2026-08-12.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-12 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the track's **hands-on counterpoint** — no models trained, no algorithms. A four-stage pipeline for turning scattered personal notes into a navigable knowledge base: voice-dictate raw material, enrich it with an agent skill (tags, sources, backlinks, an enrichment timestamp), generate wikis over the corpus, then visualize it — and finally move the whole loop to a nightly cloud schedule so it runs while you sleep. Caption garbles: "Voice Inc." → likely **VoiceInk**, "hub.md" → the presenter's open-source notes app (⚠ name uncertain, see review note 4), "wiks" → wikis, "Andre Carpathy" → **Andrej Karpathy**, "nodes" → notes (in the cloud-run walkthrough).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-holmes-llm-knowledge-bases` | LLM Knowledge Bases: a practical guide (Ben Holmes, Warp — AI Engineer World's Fair) | youtube | https://youtu.be/I3bpdgFJCUY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-ben-holmes`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-ben-holmes` | Ben Holmes (developer relations lead, Warp; author of the open-source notes app demoed throughout and of the enrich-note skill) | `AffiliatedWithCompany → co-warp` |

Referenced without coining: **Andrej Karpathy**, whose public gist is credited as the origin of the LLM-knowledge-base idea ("this is where the LLM knowledge base idea kind of came together… you can find it if you search his name and then wiki").

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-warp` | Warp | developer | Terminal built for developers and their coding agents, positioned also as "a cloud platform that helps you build out software factories"; gives access to any model including open-weight. Ships **oz.dev** (warp.dev/oz), the cloud automation platform used for the scheduled runs in this talk |

Not coined: Obsidian (the app) — `el-obsidian` **[registry]** already exists and is reused; Apple Notes, Handy and VoiceInk are tools named in passing (see review note 4).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-llm-knowledge-base` | LLM knowledge base | concept | context | The talk's organizing artifact, credited to a Karpathy gist: take a **raw directory** of unstructured personal notes and have an agent compile it into a navigable, interconnected knowledge base scoped to a focus area. Four stages — raw capture, enrichment, wiki generation, visualization — with markdown as the substrate throughout so any viewer (Warp, Obsidian, a custom app) works. Framed as the antidote to "an Apple Notes folder that's a complete disorganized mess," and as making forgotten ideas rediscoverable rather than merely stored |
| `el-voice-capture-pipeline` | Voice-first raw capture | ops | context | The input stage, argued as the load-bearing one: dictation runs ~200 words per minute and "will be faster than any other method unless you're an absolute Olympic typist," so it is how you generate the volume of raw material the later stages need. Explicitly permissive about quality — scrappy, rambly, unformatted is fine, because the agent does the structuring. Local, on-device options named (**Handy**, open source; **VoiceInk**, one-off fee) as removing the subscription barrier |
| `el-enrich-note-skill` | The enrich-note skill | technology | context | The enrichment stage as a reusable agent skill, and the file's most transferable artifact. For each note it: writes an **enrichment timestamp** so later passes can skip already-processed notes; generates **tags drawn from a fixed reference folder** rather than inventing new ones ("I actually instruct the agent to be reluctant to add new tags, because Claude loves to get creative" — with permission to add only on a genuine pattern); researches and attaches the **source** via web tools; and finds **backlinks** to related notes by key-term search. The timestamp is what makes the skill idempotent and therefore schedulable |
| `el-generated-wiki` | Agent-generated wiki | product | context | The synthesis stage: over the enriched corpus, an agent generates a browsable wiki per focus area, structured as **people, concepts, organizations and sources**, with entries and backlinks to the raw notes. Demonstrated on two corpora (an AI-news wiki and a religious-texts study wiki) and pitched for workplace use — a people section built from meeting notes, with backlinks to every related meeting, useful for customer-success and client work. The point of the structure is that entity extraction turns a pile of notes into something with an index |
| `el-nightly-agent-schedule` | Nightly knowledge-base automation | ops | harness | The operational stage that makes the rest compound: sync the markdown folder into a cloud sandbox, run the skills against unenriched notes, sync back. Implemented with the **Obsidian headless CLI** for two-way sync (a git clone is the low-tech alternative) inside a Docker-backed cloud sandbox on oz.dev, triggered on a daily or weekly schedule or by events like a Slack or iMessage. Contrasted explicitly with local automations such as the Codex app's, which "means your laptop has to be cracked open when it runs." The payoff framing: "I wake up to a perfectly fresh wiki — it's like the daily paper, but it's your own" |

Element edges: all five `IdentifiedInArtifact → ia-aie-holmes-llm-knowledge-bases`.
`el-llm-knowledge-base` `UsesElement → el-voice-capture-pipeline`, `el-enrich-note-skill`, `el-generated-wiki`;
`el-enrich-note-skill` `EnablesElement → el-generated-wiki`, `UsesElement → el-agent-skills` **[registry, batch1]**;
`el-nightly-agent-schedule` `UsesElement → el-enrich-note-skill`, `el-obsidian` **[registry]`;
`el-generated-wiki` `UsesElement → el-llm-knowledge-base`;
`el-llm-knowledge-base` `ExemplifiesPattern → pat-context-graphs` **[registry]**.

Reused elements (no new nodes): `el-agent-skills` **[batch1]** — the enrichment and wiki generators are both skills, and the fixed-tag-vocabulary discipline is a genuinely new authoring detail for that node. `el-obsidian` **[registry]** — reused for the headless CLI sync mechanism, a new fact for its brief. `el-html-native-medium` **[b9]** — the visualization stage ("I told an agent: build this for me… HTML and Tailwind") is a direct instance; edge left to review, see note 5.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-holmes-llm-knowledge-bases`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-warp`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-personal-knowledge-base-as-agent-output` | context | The practical thesis of the track's most accessible talk: the interconnected knowledge base people have wanted from personal-wiki tools for two decades is now **generated rather than maintained** — tags, sources, backlinks, entity indexes and browsable wikis all produced by agents over a raw markdown folder, with the human contributing only unstructured capture. "All of that is generated programmatically. I didn't write any of this, because all I have time to do is generate the raw ingredients, not connect it all together myself." Credited to a Karpathy gist and shown working over two unrelated personal corpora | `FormsPattern → pat-context-graphs` **[registry]** | `OnElement → el-llm-knowledge-base`, `el-generated-wiki` |
| `sig-capture-bandwidth-is-the-input-constraint` | context | The input-side argument that mirrors Khemani's finding from the opposite direction: the binding constraint on a personal knowledge system is how much raw material you actually capture, so the highest-leverage intervention is **dictation at ~200 wpm** rather than better organization. Quality standards are deliberately abandoned at capture time — scrappy and rambly is fine because the agent structures it later — and the tooling barrier has fallen, with on-device local models (Handy, VoiceInk) replacing subscription transcription | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-voice-capture-pipeline` |
| `sig-skills-need-fixed-vocabularies` | harness | A small, concrete authoring finding with wide applicability: agents generating metadata will invent new categories unless constrained, so the enrich-note skill keeps tags in a **fixed reference folder** and instructs the agent to be reluctant to add to it — "Claude loves to get creative, so just telling it please don't do that" — with permission to extend only on a genuine pattern. Paired with an **enrichment timestamp** per note, which makes the skill idempotent and therefore safe to run repeatedly and on a schedule. Vocabulary control and idempotence as the two properties that turn a prompt into infrastructure | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-enrich-note-skill`, `el-agent-skills` **[registry, batch1]** |
| `sig-knowledge-work-moves-to-nightly-cloud` | harness | The operational shift: the enrichment and wiki-generation skills run **unattended in a cloud sandbox on a schedule**, syncing a markdown folder down via the Obsidian headless CLI, running the agent, and syncing back — so the user wakes to an updated knowledge base. Explicitly contrasted with local automation (the Codex app's scheduled tasks) which requires the laptop open. The framing is that background compounding, not interactive speed, is what makes the knowledge base worth having: "it's like the daily paper, but it's your own" | `FormsPattern → pat-durable-execution` — **HELD PATTERN-LESS** (see review note 2) | `OnElement → el-nightly-agent-schedule` |
| `sig-visualizations-are-now-disposable` | context | The closing demonstration and its economic point: a force-directed graph view over the note corpus, clickable nodes, a GitHub-style habit chart, and an on-request restyle into a starfield — none of it installed, all of it generated. "This is not a tool that you have to install. I told an agent: build this for me. So you can do that now." Bespoke visualization drops from a tooling decision to a throwaway prompt, which changes what personal software is worth building versus asking for | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-llm-knowledge-base` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-capture-cheap-structure-later` | Personal knowledge management historically failed because it demanded structure at capture time — tags, folders, links — precisely when the user has the least patience and the most to say. Inverting the order removes the failure mode: make capture as close to free as speech, then spend agent compute on the structuring nobody was ever going to do by hand. The corollary for tool design is that the valuable interface is a very fast unstructured inbox plus a scheduled enrichment loop, and that almost every feature between those two is now something an agent generates on request | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-voice-capture-pipeline`, `el-enrich-note-skill` |
| `ins-idempotence-makes-skills-schedulable` | The two unglamorous details in the enrich-note skill — a fixed tag vocabulary and a per-note enrichment timestamp — are what let a prompt become a nightly job. The timestamp makes reruns cheap and safe by scoping work to unprocessed items; the fixed vocabulary keeps repeated passes from drifting into an ever-growing taxonomy. Any agent skill intended to run unattended and repeatedly needs both properties, and most published skills have neither, which is why they demo well and degrade under schedule | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-enrich-note-skill`, `el-nightly-agent-schedule` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-holmes-llm-knowledge-bases`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-an-llm-knowledge-base` | Build a knowledge base agents maintain for you | Optimize the capture step first, because raw volume is what every later stage feeds on — use voice dictation (~200 wpm, faster than typing for almost everyone) with a hotkey on desktop and phone, and accept scrappy, rambly, unformatted output since structuring is the agent's job; keep everything as **markdown in a plain folder** so any viewer works and any agent can read it; write enrichment as a **skill**, not a prompt, and give it two properties that make it schedulable — a per-note **enrichment timestamp** so reruns only touch unprocessed notes, and a **fixed tag vocabulary in a reference folder** with explicit instructions to be reluctant to add to it, because agents will otherwise invent a new taxonomy on every pass; have the skill attach sources via web search and generate backlinks by key-term search, so the corpus grows more interconnected with each run; generate **wikis** over the enriched corpus structured as people, concepts, organizations and sources, which is what turns a pile of notes into something with an index — this works as well for meeting notes and client histories as for personal research; then move the whole loop to a **cloud schedule** rather than a local one, syncing the folder down (Obsidian headless CLI, or just a git clone), running the skills, and syncing back, so it compounds nightly without your laptop being open; and treat visualizations as disposable — ask an agent for the graph view or the habit chart rather than adopting a tool for it | `ReferencesElement → el-enrich-note-skill`, `el-voice-capture-pipeline`, `el-generated-wiki`, `el-nightly-agent-schedule` |

## Dropped

- **The show-of-hands openers** (disorganized Apple Notes folders, Obsidian usage, Whisper Flow usage) — logistics, though the third motivates `el-voice-capture-pipeline`.
- **The personal-corpus examples** (Acquired podcast episodes on Walt Disney and Ferrari, *The Left Hand of Darkness*, the Bible-in-a-year study wiki, the jazz-musician entry on AI in music) — demonstration material; the mechanics they illustrate are in the elements.
- **The live enrichment run and its background completion** — stagecraft.
- **The product plugs** (oz.dev, the open-source notes app, the booth, the side event) — logistics; oz.dev survives inside `el-nightly-agent-schedule` because it is the execution substrate.

## Review notes

1. **Why this file matters despite being the least technical in the track.** It is the only talk in the batch that shows continual learning as something an individual can run **today with no model training** — capture, enrich, synthesize, schedule — and it lands on `pat-context-graphs`, the seed pattern this whole cluster keeps circling. Read alongside Khemani (whose complaint is that products do not reason over the context you already have), it is the DIY answer to that complaint: build the corpus yourself and point an agent at it.
2. **⚠ `sig-knowledge-work-moves-to-nightly-cloud` held pattern-less — a `pat-durable-execution` data point.** Scheduled, unattended, sandbox-isolated agent runs with sync-in/sync-out state is squarely that candidate's shape, and it joins the b17 finding that the ledger is complete. Rehome on coin. Note the deliberate contrast the speaker draws with laptop-bound local automation, which is a cleaner statement of the cloud-durability argument than most of the ledger's existing points.
3. **⚠ Terminology and pattern caution on `sig-visualizations-are-now-disposable`.** Homed to `pat-saaspocalypse` on the grounds that generate-on-demand replaces a category of installed tooling. It is a *personal-software* instance rather than the per-seat-SaaS-pricing collapse the seed pattern describes, so it is the weakest edge in the file. **Drop-option:** rehome to `pat-model-not-bottleneck` or hold pattern-less if review reads the seed pattern narrowly.
4. **⚠ Verify before seeding.** Several tool names are caption-reconstructed: the notes app the speaker built and open-sourced (rendered "hub.md", also described as "an Apple Notes that's agent accessible"), **VoiceInk** (rendered "Voice Inc."), and the oz.dev URL form (given as both `oz.dev` and `warp.dev/oz`). The ~200 wpm dictation figure is asserted, not sourced. None of these carry a signal on their own, but the app name would be needed if review wants an element for it.
5. **Proposed cross-file edge, left to review.** The visualization stage is a textbook instance of `el-html-native-medium` **[b9, Russo/HeyGen]** — agent-generated HTML as the output medium, here for a graph view and a habit chart. Proposed at seeding: `el-llm-knowledge-base` `UsesElement → el-html-native-medium`. Not emitted, since the speaker never frames it as a medium claim.
6. **Company note.** `co-warp` is a first corpus appearance for a terminal vendor positioning itself as a software-factory cloud platform, which puts it adjacent to the b13/b17 software-factory thread (HumanLayer, Horthy). Only the automation substrate is evidenced here; the software-factory positioning is a single self-description and no signal is emitted for it.
