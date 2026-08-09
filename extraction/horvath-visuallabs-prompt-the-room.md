# SPIKE extraction — "You Can't Prompt the Room: The Last Skill AI Won't Replace" (Balázs Horváth, VisualLabs) — FOR REVIEW

Source transcript: `transcripts/horvath-visuallabs-prompt-the-room.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/6bmM45jkMDY — AI Engineer World's Fair, published 2026-06-29.
`stagingTimestamp` for the artifact, signals, and knowhows: 2026-06-29 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-horvath-prompt-the-room` | You Can't Prompt the Room: The Last Skill AI Won't Replace (Balázs Horváth, VisualLabs — AI Engineer World's Fair) | youtube | https://youtu.be/6bmM45jkMDY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-balazs-horvath`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-balazs-horvath` | Balázs Horváth (founder, VisualLabs; 13 years bridging business and IT — functional consultant on large ERP/CRM programs in the US/UK before founding the firm) | `AffiliatedWithCompany → co-visuallabs` |

## Companies (1 new)

| slug | name | type | brief |
|---|---|---|---|
| `co-visuallabs` | VisualLabs | developer | Consultancy training teams to elicit requirements and turn them into specifications — for developers, for consultants to configure, and most recently for AI to build |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-story-mapping` | User story mapping | concept | — | Classic product-analysis technique repurposed as AI-era spec tooling: a backbone of process stages (e.g. contact → triage → resolve → close) with user stories beneath each, sliced into an MVP release row and backlog rows; each story in persona/what/need/why form with acceptance criteria, then daisy-chained into a coherent specification the AI builds from. Bonus: LLMs were trained on the ubiquitous user-story format, so specs in that shape elicit measurably better generations |
| `el-vad-framework` | VAD (Value → Architecture → Design) | concept | — | VisualLabs' elicitation sequence: start from how value is created (whose problem, what winning looks like), then the process and underlying architecture that support that value, and only then system design — never "build us an agent that handles support" first; paired with four screening questions (whose problem is this? what does winning look like? what would make them refuse to use it? would it change a decision?) whose answers live in a markdown file in the repo so the AI has the context |

Element edges: both `IdentifiedInArtifact → ia-aie-horvath-prompt-the-room`; `el-story-mapping` `EnablesPattern → pat-value-of-judgement` **[registry]** (the toolkit that operationalizes deciding-what-to-build).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-horvath-prompt-the-room`, `SourcedFromSource → source-aie-yt` **[registry]**. Domain: — (none of the enum values fit people/product-process content; left unset).

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-visuallabs-hackathon-value-filter` | VisualLabs' internal hackathon (start of 2026): 21 agent ideas, 17 abandoned for creating no business value (no data access, or no reason to exist); the 4 survivors materially changed how the firm works — build capacity wasn't the filter, value discovery was | `FormsPattern → pat-value-of-judgement` **[registry]** | `RelevantCompany → co-visuallabs` |
| `sig-bottleneck-moved-to-the-room` | 13-year business↔IT bridge consultant: over the past 2–3 years writing code stopped being the SDLC bottleneck; the constraint is now getting stakeholders and decision-makers into the room and eliciting real requirements — "you can prompt your code, your spec, your AI; you can't prompt the room" (paraphrase) | `FormsPattern → pat-value-of-judgement` **[registry]** | — |
| `sig-smartest-people-upstream` | Prescribed org shift: pre-AI, firms put their smartest people on writing code; now they belong customer-facing, deciding what gets built — deciding is the expensive part, building has become cheap; involve SMEs in build decisions and realign KPIs (count features used more than twice, not features shipped) | `FormsPattern → pat-value-of-judgement` **[registry]** | — |
| `sig-ai-defaults-to-average` | AI is built to return the most common answer, so using it naively replicates what already exists — Henry Ford's faster horse; the differentiated product (the car) requires humans to deliberately steer away from the statistical average. Same-tools economics: everyone has the latest model, so understanding the business need better is the only remaining edge | `FormsPattern → pat-value-of-judgement` **[registry]** | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-analyst-toolkit-new-moat` | "Old skill, new economics": with model access commoditized, the durable moat shifts to the analyst toolkit — story mapping, business model canvas, value canvas, design-thinking elicitation. The SDLC itself doesn't change with AI; the toolkit that feeds it does, and the functional-consultant skill set stops being overhead and becomes the mode of production | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-story-mapping`, `ReliesOnElement → el-vad-framework` |
| `ins-escape-velocity-from-average` | Because generative AI regresses to the training-set mean, human judgment has a specific new job: supplying the non-average direction — naming whose problem is being solved, what winning looks like, and which decision should change. Without that steering, AI-accelerated teams just ship the existing world faster | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-vad-framework` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-horvath-prompt-the-room`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-story-map-before-prompting` | Run a mapping session before you vibe-code | Before building, map the backbone of the user's process and hang user stories beneath each stage; slice the first release (MVP) and keep the rest as backlog. Write every story as persona / what / need / why with acceptance criteria (test cases derive from them) — LLMs know this format from training, so it elicits better results than freeform prompts. Daisy-chain the stories into a coherent spec, then generate. Answer the four VAD screening questions (whose problem? what does winning look like? what would make them refuse it — platform, friction, data security? which decision does it change?) and keep the answers in a markdown file in the repo so the AI always has that context. A/B it yourself: build the same use case with and without user stories and compare | `ReferencesElement → el-story-mapping`, `ReferencesElement → el-vad-framework` |
| `how-detect-building-wrong-thing` | Audit for building-the-wrong-thing anti-patterns | Watch for the signature: high shipping velocity + low adoption; logins/trials without **re-use** (track frequency of a specific activity, not time-on-site); "the demo is the deliverable" (demos are fast and pretty — production use is the bar); a PRD with no real user testers. Fix the measurements: replace "features shipped last quarter" with "features used more than twice"; move subject-matter experts into the decision-making about what gets built (they know what worked before) without forcing everyone to become a PM | `ReferencesElement → el-story-mapping` |

## Dropped

- Business model canvas / value canvas as separate Elements — named as toolkit members; kept in `ins-analyst-toolkit-new-moat` prose.
- The support-system story-map worked example (capture intent → classify urgency → draft grounded answer → log to system of record) — illustration inside the knowhow.
- Henry Ford anecdote as a node — folded into `sig-ai-defaults-to-average`.

## Review notes

1. As anticipated in the assignment, this human-skills talk maps cleanly onto `pat-value-of-judgement` (choosing what's worth doing as the durable edge) — all four signals form it; that concentration is honest for a single-thesis talk. Considered `pat-model-not-bottleneck` for `sig-bottleneck-moved-to-the-room` but that pattern is about production/value layers around models, not the SDLC's human bottleneck — not linked.
2. **Candidate-pattern evidence (not coined, no edges)**: `sig-smartest-people-upstream` (+ the KPI realignment to usage-over-output) adds soft evidence to the registry's uncoined `pat-ai-native-org` candidate — org redesign around "building is cheap, deciding is expensive". Note for the central ledger.
3. Signals carry no domain — the enum (training/inference/…/context) has no product/people slot.
4. `el-story-mapping` is a decades-old technique (Jeff Patton lineage); kept as an Element because it is the talk's load-bearing skill and the knowhow references it — same rationale as `el-semantic-layer` in the daga file. `el-vad-framework` is VisualLabs' own coinage.
5. Hackathon numbers (21 ideas / 17 abandoned / 4 impactful) read clearly in captions. "we just wiped Google it out" is an unresolved garble (probably "vibe-coded it") — not load-bearing, skipped.
6. The "user-story format plays to LLM pattern recognition" observation was considered as a fifth signal but folded into `el-story-mapping`'s brief and the knowhow — promote at review if wanted.
