# SPIKE extraction — "Perception Agents" (Antje Barth, Amazon AGI Lab) — FOR REVIEW

Source transcript: `transcripts/barth-amazon-perception-agents.txt` (auto-captions — quotes are paraphrases, not verbatim; "member of technical staff at Amazon AGI lab onjab. bar" → **Antje Barth**).
Video: https://youtu.be/2JX6JYyQG4Y · published 2026-07-23 (AI Engineer, World's Fair).
`stagingTimestamp` for the artifact and all signals: 2026-07-23 (publish date).
Entities marked **[registry]** already exist — edges link, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-barth-perception-agents` | Perception Agents (Antje Barth, Amazon AGI Lab — AI Engineer World's Fair) | youtube | https://youtu.be/2JX6JYyQG4Y |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-antje-barth`.

## Experts (1 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-antje-barth` | Antje Barth (member of technical staff, Amazon AGI Lab) | `co-amazon` **[registry]** |

## Companies (1 registry reuse)

| slug | name | type | note |
|---|---|---|---|
| **[registry]** `co-amazon` | Amazon | bigtech | "Amazon AGI Lab" reused as `co-amazon` per the `co-meta`/Meta-Superintelligence precedent (see Review note 2); `co-bee` (below) is Amazon-acquired but kept distinct |
| **[registry]** `co-bee` | Bee | developer | AI wearable (Amazon-acquired) sponsoring the ambient-audio demo |

## Elements (3 new; 1 registry reuse)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-perception-agent` | Perception agent | concept | harness | Agent that perceives the *rendered* screen (layout/state/what changed) rather than scraping the code behind it, then plans and acts in a robotics-style perceive→plan→act loop; reacts in real time while you work (no turn-taking wait), confirms its own output, needs no API/backend, and accepts point-and-annotate input as a precise, less-lossy signal than text |
| `el-annotation-tool` | Perception-agent annotation tool | product | harness | Open-source Chrome extension (first of two harness pieces): select/mark elements on any screen and describe a change; captures the exact location, style, and feedback into a complete structured summary handed to the coding agent — removing the write-a-long-description back-and-forth |
| `el-visual-verification` | Perception-agent verification | concept | harness | Open-source verification piece: the agent turns a `design.md` of design rules into checks (inferring them if unwritten) and runs two kinds — a visual on-brand/layout check and an automated user-flow walkthrough (adds/deletes tasks like a real user) — then writes a pass/fail report a human reviews |

| slug | reuse | note |
|---|---|---|
| **[registry]** `el-bee` | Bee wearable | ambient-audio perception: the design-meeting demo used Bee to transcribe the room and feed insights ("apply") straight to the agent |

Element edges: `el-perception-agent` `DevelopedByCompany → co-amazon` **[registry]**; `el-annotation-tool` `DevelopedByCompany → co-amazon`; `el-perception-agent` `UsesElement → el-annotation-tool`, `UsesElement → el-visual-verification`, `UsesElement → el-bee` **[registry]**; `el-visual-verification` `EnablesPattern → pat-verification-gap` **[registry]**; all three new elements `IdentifiedInArtifact → ia-aie-barth-perception-agents`.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-barth-perception-agents`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|
| `sig-capability-solved-reliability-gap` | Amazon AGI Lab observation: agents can perform each individual step of an end-to-end workflow (click/scroll/type/call an API) but fail across the "seams" between apps, where the real work lives; capabilities are mostly solved, reliability isn't — and without reliability there's no trust; 60-80% success is unusable when the failure deletes a database ("you need the nines") | `pat-model-not-bottleneck` **[registry]** | `el-perception-agent` | `co-amazon` **[registry]** |
| `sig-verification-wall-knowledge-work` | Coding got reliable and trusted first because code is verifiable (run/test/check); most knowledge work is not — "did the report land? is the design on brand?" has no unit test — so verification hits a wall exactly where most work lives (the seams between apps), and nobody has solved reliability without verifiability; "still wide open" | `pat-verification-gap` **[registry]** | `el-visual-verification` | `co-amazon` **[registry]** |
| `sig-perception-agents-close-loop` | Amazon's answer — perception agents that read the rendered screen to *complete the computer-use loop* (act → confirm it worked, instead of fire-and-forget), need no API/backend (works on the majority of software that exposes none), and take point-and-annotate input as a precise low-loss instruction | `pat-verification-gap` **[registry]** | `el-perception-agent`, `el-annotation-tool` | `co-amazon` **[registry]** |
| `sig-perception-harness-open-source` | Amazon launched the first two pieces of its perception-agent harness open source: an annotation Chrome extension (mark screen elements → structured summary for the agent) and a `design.md`-driven verification tool (visual on-brand check + automated user-flow walkthrough → pass/fail report); building the rest in the open so "these patterns get better as more people use and break them" | `pat-verification-gap` **[registry]** | `el-annotation-tool`, `el-visual-verification` | `co-amazon` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-shared-context-over-bigger-brain` | "You don't need a bigger brain, you need shared context": humans solve messy unverifiable work by looking at the same screen together and reacting in real time; the missing capability is an agent that perceives what you perceive and can react while you're still working — not a smarter model | `pat-model-not-bottleneck` **[registry]** | `el-perception-agent` |
| `ins-verify-your-own-output` | An agent that reads the rendered result can confirm its own action rather than firing and hoping; work you can't unit-test (brand, layout, user flows) becomes automatable by checking rendered output against a written spec and walking the flows — shifting the midnight click-through off the human | `pat-verification-gap` **[registry]** | `el-visual-verification` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-barth-perception-agents`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-perception-agent-verification` | Give agents perception plus self-verification for unverifiable work | Have the agent read the rendered interface (layout/state/what changed), not scraped code; complete the loop by checking its own output instead of firing actions and moving on; capture user input by pointing/annotating on-screen elements (an exact, low-loss instruction) rather than long text; write design rules in a `design.md` and have the agent turn them into a visual on-brand check plus an automated user-flow walkthrough, emitting a pass/fail report a human reviews; extend "perception" beyond the screen — e.g. ambient meeting audio via a wearable → transcript → applied changes | `el-perception-agent`, `el-annotation-tool`, `el-visual-verification`, `el-bee` **[registry]** |

## Dropped

- Robotics perceive→plan→act analogy — framing device; folded into `el-perception-agent`.
- Danielle Persik cognitive-scientist podcast + the AGI-ACI team, and colleague Gaf Mishra's "RL to IRL" computer-use-track talk — session/promo plugs; no nodes.
- Colleague "Giovanni" (design-meeting demo partner), booth/expo logistics — dropped.
- Coding-agent evolution recap (autocomplete → functions → PR-opening agents) — used as the "verifiability" contrast; carried inside `sig-verification-wall-knowledge-work`.

## Review notes

1. Four signals split across two registry patterns: the "capabilities solved, value/failure moved to reliability + shared context" claims sit on `pat-model-not-bottleneck`; the "verification wall / self-verification" claims sit on `pat-verification-gap`. `sig-perception-agents-close-loop` also carries a `pat-harness-over-model` **[registry]** resonance (perceive→plan→act loop as deterministic scaffolding) — noted, not edged.
2. **`co-amazon` reuse flagged.** "Amazon AGI Lab" is credited to `co-amazon` **[registry]** rather than a new node, following the `co-meta`/Meta-Superintelligence precedent named in the task. Flip to a dedicated `co-amazon-agi-lab` at reconciliation if you prefer lab-level granularity (Barr/`ramdoss-amazon-rendering-layer.md` also reuse `co-amazon`).
3. `co-bee`/`el-bee` **[registry]** reused from batch 2 (Korshakov). Bee is Amazon-acquired but kept as a distinct company node per the existing registry.
4. `el-annotation-tool` and `el-visual-verification` are named only descriptively in captions ("annotation", "verification") — product names not stated; slugs are descriptive. GitHub repos referenced but URLs not captured.
