# SPIKE extraction — "HTML Is All Agents Need" (James Russo, HeyGen) — FOR REVIEW

Source transcript: `transcripts/russo-heygen-html-all-agents-need.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/Cz4v1WHVyZc — AI Engineer World's Fair, published 2026-07-21.
`stagingTimestamp` for the artifact and all signals: 2026-07-21 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
NOTE (review 2026-07-22): `pat-html-native-medium` was coined here and DEMOTED — kept as element `el-html-native-medium`; edges rehomed to `pat-model-not-bottleneck`. `kapoor-nori-html-for-graphics.md` and `raj-ark-browser-agents-better-eyes.md` updated to match.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-russo-html-agents-need` | HTML Is All Agents Need (James Russo, HeyGen — AI Engineer World's Fair) | youtube | https://youtu.be/Cz4v1WHVyZc |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-james-russo`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-james-russo` | James Russo (co-creator & tech lead of Hyperframes at HeyGen) | `AffiliatedWithCompany → co-heygen` |

## Companies (1 new)

| slug | name | type | brief |
|---|---|---|---|
| `co-heygen` | HeyGen | developer | AI-video company ("solve communication through video"); built its name on AI avatars (the A-roll layer) and now owns Hyperframes, the open-source HTML-to-video framework for agents |

## Patterns (0 new — coin REJECTED at review 2026-07-22)

`pat-html-native-medium` was coined here on two-talk evidence and **demoted at
review** (user: mechanism, not a seed-altitude industry thesis). Per this
file's pre-written rejection fallback: the thesis is kept as element
`el-html-native-medium` (below), and every `FormsPattern`/`HighlightsPattern`/
`ExemplifiesPattern` edge that pointed at the pattern is rehomed to
`pat-model-not-bottleneck` **[registry]** (nearest existing thesis: "it's not
the model, it's the medium").

## Elements (2 new + 1 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-html-native-medium` | HTML as the agent-native medium | concept | harness | Agent-facing creative and interface tooling converging on the web stack — HTML/CSS/JS, and text-structured markup generally — as the medium agents read and write, because it is what the models were trained on (the scraped web). Builders let the model author markup and make the browser do the rendering; human tools and formats (MP4, PDF, PPT, canvas editors, DSLs) get demoted to render targets, and agent *perception* likewise moves from pixels/raw DOM to compressed markup. Central thesis of this talk and Kapoor/Nori; input-side echo in ARK; industry meme "HTML is the new markdown" (Karpathy, Thariq [Shihipar?]). Prior-corpus resonance: Amazon rendering layer (batch 2), `el-generative-ui`, `el-a2ui`, `el-mcp-apps`. Was briefly coined as `pat-html-native-medium`; demoted to element at review |
| `el-hyperframes` | Hyperframes | framework | harness | HeyGen's open-source framework (free forever; released ~2 months before the talk) that turns agent-authored HTML/CSS/JS into deterministic MP4 video: it freezes the browser clock and seeks frame-by-frame, waiting for every asset before screenshotting, so the pixels the browser previews are exactly the pixels the video gets; anything a browser can render (three.js, charts, SVG, shaders, WebGL/WebGPU, Lottie) becomes video-able; markup is plain HTML plus a few data attributes for timing metadata; ships skills that teach video taste rather than syntax, plus a studio (incl. keyframes) for human last-mile editing; works with any coding agent that writes HTML |

Reused **[registry]**: `el-remotion` — discussed as the evaluated-and-rejected alternative (great LLM coding demo, but the framework/language had to be taught, costing creativity). Edge: `el-remotion` `IdentifiedInArtifact → ia-aie-russo-html-agents-need`.

Element edges: `el-hyperframes` `IdentifiedInArtifact → ia-aie-russo-html-agents-need`; `DevelopedByCompany → co-heygen`; `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]** (rehomed); `UsesElement → el-html-native-medium`.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-russo-html-agents-need`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | Pattern edges | RelevantCompany |
|---|---|---|---|
| `sig-hyperframes-open-source-scale` | Hyperframes HTML-to-video running at scale: speaker-reported 1.3M videos rendered by open-source users in the last 90 days, 267k creators, ~15k videos/day, 32k GitHub stars, ~2 months after release; works with any coding agent that can write HTML/CSS/JS (Claude Code, Codex, Cursor, …) — "the same agent that builds your product makes your launch video" | `FormsPattern → pat-model-not-bottleneck` **[registry]** (rehomed) | `RelevantCompany → co-heygen` |
| `sig-heygen-thinnest-wrapper-won` | A year of format experiments ended with the thinnest wrapper winning: After Effects/Premiere are great-output but agent-hostile; Lottie/Rive (JSON/custom XML DSLs) and Remotion all required teaching the model a language; heavier wrappers with more context, bigger system prompts, and skills lost to essentially-plain HTML with a few data attributes — validated by using small Gemini 3 Flash as design partner; with the Gemini 3 generation (Nov 2025) models "naturally gravitated" to HTML/CSS/JS, so HeyGen chose "don't fight the model" | `FormsPattern → pat-model-not-bottleneck` **[registry]** (rehomed); `ContradictsPattern → pat-harness-over-model` **[registry]** (see Review notes) | `RelevantCompany → co-heygen` |
| `sig-html-new-markdown-convergence` | Independent industry convergence on HTML as the LLM visual-output format: Karpathy and Thariq [Shihipar? — garbled, see Review notes] publicly pushing "HTML is the new markdown" over recent months; Russo notes he submitted this talk before those tweets — multiple parties reached the same conclusion separately | `FormsPattern → pat-model-not-bottleneck` **[registry]** (rehomed) | — |
| `sig-models-weak-at-creative-craft` | Practitioner honesty: models still aren't good at creative work even in their native format; HeyGen compensates with skills that teach taste (not syntax), continuous agent-run evals to raise the single-shot floor, a human-in-the-loop studio for last-mile edits — and is starting a code-to-video benchmark with LLM labs and video-agent builders to raise the floor industry-wide | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-heygen` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-native-tongue-over-dsl` | Teaching a model your DSL or custom JSON discards its pretraining ("asking Shakespeare to write a poem in Japanese" — examples don't fix a non-native tongue); adopting the model's native format instead turns the entire scraped web into your product's training corpus and every model upgrade into free product improvement — the format compounds with the frontier rather than fighting it | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** (rehomed) | `ReliesOnElement → el-hyperframes`, `ReliesOnElement → el-html-native-medium` |
| `ins-determinism-is-the-hard-part` | The hard part of agent video isn't authoring, it's determinism: browsers are async on purpose (fonts, images, assets load late) while video needs every pixel present on every frame; freezing the browser clock and seeking frame-by-frame converts the browser into a deterministic renderer — which is what upgrades "LLMs write web pages" into "anything a browser renders can ship as an MP4" | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** (rehomed) | `ReliesOnElement → el-hyperframes` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-russo-html-agents-need`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-small-model-design-partner` | Validate agent-facing formats against the smallest model | Use a small model (HeyGen used Gemini 3 Flash) as the design partner for any agent-authored format; if the small model can author workable code in it, every larger model and coding agent clears it, and model progress compounds for free; prefer the thinnest wrapper — plain HTML plus data attributes as metadata — over new syntax; if you find yourself adding context, bigger prompts, and skills just to teach the format, the format is wrong | `ReferencesElement → el-hyperframes` |
| `how-skills-teach-taste-not-syntax` | Spend the skill budget on taste, not language | Don't teach HTML/CSS/JS — models already know it; write skills about what makes a great video: motion examples, storyboarding, brand/asset retrieval from a website (website-to-video via a design/frame .md); eval continuously, using agents to improve the skills, so single-shot output keeps rising; for great (vs decent) output keep pre-AI craft — narrative and vision → storyboard frame-by-frame → motion per frame → merge → human last-mile editing in the studio | `ReferencesElement → el-hyperframes` |

## Dropped

- Claude Code ("Cloud Code" in captions), Codex, Cursor — compatibility name-drops only; no `IdentifiedInArtifact` edges to `el-claude-code`/`el-codex`/`co-cursor` **[registry]**.
- Gemini 3 / Gemini 3 Flash as Element nodes — the load-bearing entity is the small-model-design-partner method (captured in KnowHow), not the model; kept as prose.
- DesignMD / FrameMD, the keyframes studio feature, the AI Engineer World's Fair showcase video ("AI engineer Warfare" garble) made with Hyperframes — product detail folded into `el-hyperframes` brief and prose.
- The code-to-video benchmark — announced initiative, nothing shipped/named to node yet; lives inside `sig-models-weak-at-creative-craft`.
- After Effects / Premiere / Lottie / Rive — evaluated-alternative mentions, folded into `sig-heygen-thinnest-wrapper-won`.

## Review notes

1. **RESOLVED at review 2026-07-22 — coin rejected (mechanism, not thesis); fallback below applied verbatim.** Original note: `pat-html-native-medium` is coined on TWO talks that state it as their central thesis (this one and Kapoor/Nori — titles are near-duplicates by design of the claim, not coincidence), plus in-talk citation of the wider meme (Karpathy/Thariq "HTML is the new markdown") and prior-batch resonance (Ramdoss rendering layer, `el-generative-ui`, `el-a2ui`, `el-mcp-apps`). I read it as seed-altitude: it predicts industry-wide re-basing of the agent↔visual-artifact interface on web markup and the demotion of human canvas tools to render targets — a claim about how tooling gets built, not a single technique. Kind `dynamic` (a case for `disruption` exists — it displaces PowerPoint/AE/Figma as agent surfaces). If review rejects the coin: rehome its `FormsPattern` edges to `pat-model-not-bottleneck` (nearest existing thesis) and keep the talks' mechanisms as elements.
2. **`ContradictsPattern → pat-harness-over-model` on `sig-heygen-thinnest-wrapper-won`:** heavier wrappers/context/skills lost to the thinnest format + "don't fight the model, bet on it improving" — same shape as the batch-7 Shihipar prompt-shrink counter-edge. Note the same talk *supports* the harness thesis elsewhere (`sig-models-weak-at-creative-craft`: taste-skills, evals, deterministic renderer, studio) — the harness didn't vanish, it moved from format-teaching to taste/verification. Both edges kept deliberately.
3. **"Tarik" garble:** captions say "Tarik, Andrej Karpathy have been talking about HTML is a new markdown". Likely `exp-thariq-shihipar` **[registry]** given his HTML/generative-output commentary, but unverified — kept as prose with a question mark, no expert edge (he's not a contributor to this artifact).
4. Adoption numbers (1.3M videos/90d, 267k creators, 15k/day, 32k stars) are speaker-reported marketing figures via auto-captions — treat as claims, not verified facts.
5. "November of last year" = November 2025 (Gemini 3 release wave) given the 2026-07-21 publish date.
6. Candidate patterns from the central ledger (`pat-durable-execution`, `pat-benchmark-trust-crisis`, `pat-agent-economy`, `pat-ai-native-org`, `pat-adaptive-*`): no material new evidence in this talk. (The code-to-video benchmark effort is benchmark *creation*, not benchmark distrust — not counted toward `pat-benchmark-trust-crisis`.)
7. Casing of "Hyperframes"/"HyperFrames" varies in captions; element uses "Hyperframes".
