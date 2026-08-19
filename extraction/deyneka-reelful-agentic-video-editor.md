# SPIKE extraction — "Building an Agentic Video Editor for Mass Consumer" (Ekaterina Deyneka, Reelful) — FOR REVIEW

Source transcript: `transcripts/deyneka-reelful-agentic-video-editor.txt` (auto-captions — quotes are paraphrases, not verbatim; short talk).
Video: https://youtu.be/pPj_tjlvYjA — AI Engineer World's Fair, **Generative Media track**, published 2026-08-18.
`stagingTimestamp`: 2026-08-18. Entities marked **[registry]** are already in the registry.
Shape of the talk: **agentic video editing = agentic app building** in a different medium. Reelful edits *real* footage (not generation) via a sandbox + agent + skills + a verification layer, emitting **Remotion (video-as-React-code)** compositions. The infra mirrors an agentic app builder (media+prompt → sandbox → agent-with-skills → rendered video), with the twist that editing real footage is harder than a blank canvas (must select best moments, deliver polish). Caption garbles: "RealFull/Real Fall/Real Flow/Reelful" → **Reelful** (systematic), "Remotion" kept, "Argentic" → agentic, "A16Z speed run" → **a16z Speedrun**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-deyneka-agentic-video-editor` | Building an Agentic Video Editor for Mass Consumer (Ekaterina Deyneka, Reelful — AI Engineer World's Fair) | youtube | https://youtu.be/pPj_tjlvYjA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-ekaterina-deyneka`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-ekaterina-deyneka` | Ekaterina Deyneka (founder and CEO, Reelful) | `AffiliatedWithCompany → co-reelful` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-reelful` | Reelful | developer | Mobile-first **agentic video editor** for mass consumer — edits real user footage (photos/videos) into ready-to-share clips. Backed by **a16z Speedrun**. Editing (not generating) real footage is the deliberate, harder bet |

Reused **[registry]**, edge-only: none load-bearing. Not coined: a16z (investor, passing reference).

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agentic-editor-equals-app-builder` | Agentic video editor ≈ agentic app builder | concept | harness | The framing insight: from an infrastructure standpoint an agentic video editor is **the same shape as an agentic app builder** — prompt (here media+prompt) → a **remote sandbox** spins up → an **agent with tools and skills** works → a result (there an app preview; here a rendered video). The difference: the artifact is a **video composition** instead of a codebase. Positions media agents inside the established coding-agent infrastructure pattern |
| `el-edit-not-generate` | Editing real footage, not generating | concept | harness | Reelful's deliberate harder bet: edit the user's **real, personal footage** rather than generate content. Harder than a blank canvas because the agent must **select the best moments, decide what to omit, organize a coherent result, and deliver professional polish from messy/incomplete footage** — ideally indistinguishable from human editing. A blank canvas lets the agent do anything; editing constrains it to judgement over real material |
| `el-media-agent-skills` | Media editing as agent skills | technology | harness | Where the taste lives: the agent's **skills** encode editing craft — cut rules (how to select best moments), font pairs, how to generate B-rolls — plus sub-processes for music generation, voiceover, sound, and photo animation. The composition is emitted as **Remotion (video-as-React-code)**, chosen because "agents are really good at writing code," so video generation becomes code generation. Skills as the repository of domain taste, the same shape as coding-agent skills |
| `el-media-verification-layer` | Media verification layer | technology | harness | The reliability piece: "agents make mistakes, so we developed a **verification layer** to make sure the composition is clean, well-defined, and will render — and if there are problems the agent reiterates." Deterministic verification that the generated Remotion composition is valid before rendering, with a retry loop. Plus mass-consumer delivery choices: mobile-first, **directional templates** (speak-to-camera, add-B-rolls) so no prompt is needed, and a building editor for manual tweaks |

Element edges: all four `IdentifiedInArtifact → ia-aie-deyneka-agentic-video-editor`.
`el-agentic-editor-equals-app-builder` `UsesElement → el-media-agent-skills`, `el-media-verification-layer`;
`el-edit-not-generate` `EnablesElement → el-agentic-editor-equals-app-builder`;
`el-media-verification-layer` `DevelopedByCompany → co-reelful`, `ExemplifiesPattern → pat-verification-gap` **[registry]**;
`el-media-agent-skills` `UsesElement → el-remotion` **[registry]**.

Reused elements (no new nodes): `el-remotion` **[b8]** (video-as-code framework — a new agent-generation use of that node), `el-agent-skills` **[batch1]** (media skills), `el-microvm`/`el-sandbox-snapshotting` adjacency (the sandbox).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-deyneka-agentic-video-editor`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-reelful`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-media-agents-mirror-coding-agents` | harness | The framing claim: an agentic video editor is infrastructurally identical to an agentic app builder — media+prompt → sandbox → agent-with-skills → rendered artifact — with a video composition standing in for a codebase. Media agents inheriting the coding-agent architecture pattern wholesale, evidence that the harness/sandbox/skills pattern is a general substrate, not code-specific | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-agentic-editor-equals-app-builder` |
| `sig-editing-harder-than-generating` | harness | A counterintuitive product bet: editing **real footage** is harder than generating, because a blank canvas lets the agent do anything while editing forces judgement — select best moments, omit, organize, polish messy footage indistinguishably from human editing. Chooses the harder problem (real personal content) over the easier one (generation) as the differentiated bet | — (held pattern-less; media-as-medium ledger) | `OnElement → el-edit-not-generate` |
| `sig-video-is-code-via-remotion` | harness | The mechanism: compositions are emitted as **Remotion (video-as-React-code)** precisely because "agents are really good at writing code," turning video editing into code generation the agent can do well. The HTML/code-as-the-medium thread (b9 Russo/Kapoor) extended to video — agents build media by writing code, then a verification layer checks it renders | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-media-agent-skills`, `el-remotion` **[registry]** |
| `sig-media-agent-needs-verification-layer` | harness | The reliability signal: because agents make mistakes, Reelful runs a **verification layer** ensuring the Remotion composition is clean, well-defined and will render, with an agent-reiterates retry loop. Deterministic verification of an agent-generated artifact before it ships — the verification-gap pattern applied to media compositions, same shape as coding agents' build/lint checks | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-media-verification-layer` |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-the-harness-pattern-is-medium-agnostic` | The transferable point is that the sandbox + agent + skills + verification-layer pattern established for coding agents is **medium-agnostic**: swap the codebase artifact for a Remotion video composition and the whole architecture carries over, because "agents are good at writing code" and video-as-code makes media a code-generation problem. That generalizes the corpus's coding-agent harness findings to any domain expressible as code, and it makes the verification layer (does the composition render?) the same reliability primitive as a build check | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-agentic-editor-equals-app-builder`, `el-media-verification-layer` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-deyneka-agentic-video-editor`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-an-agentic-media-editor` | Build a media agent like a coding agent | Treat an agentic media editor as an **agentic app builder in a different medium** — media+prompt → remote sandbox → agent with tools and skills → rendered artifact — and reuse the coding-agent infrastructure pattern directly; represent the output as **code** (Remotion / video-as-React) because agents are good at writing code, turning editing into code generation; encode craft as **skills** (cut rules, font pairs, B-roll generation) and spin sub-processes for music, voiceover, sound and photo animation; run a **verification layer** that checks the generated composition is clean, well-defined and will render, with a retry loop, since agents make mistakes; consider **editing real footage** rather than generating as the harder, more differentiated bet (the agent must select best moments and polish messy material, not fill a blank canvas); and for mass consumer, hide the workflow behind **mobile-first directional templates** (speak-to-camera, add-B-rolls) so no prompt is needed, with an optional manual editor for tweaks | `ReferencesElement → el-agentic-editor-equals-app-builder`, `el-edit-not-generate`, `el-media-agent-skills`, `el-media-verification-layer` |

## Dropped

- **The audience-poll opener** (who recorded/posted conference video) — framing.
- **The played demo clips** — colour.
- **The a16z Speedrun funding note and beta ask** — logistics (investor referenced, not coined).

## Review notes

1. **The media talk best-aligned with the corpus's coding-agent theses.** It lands cleanly on `pat-harness-over-model` (sandbox+skills+verification is medium-agnostic) and `pat-verification-gap` (verification layer on a generated artifact), and extends the b9 HTML/video-as-code thread. Least scope-questionable of the media cluster.
2. **New agent-generation use of `el-remotion` [b8]** — previously a video-as-code framework reference; here it's the agent's *output format*, chosen because agents write code well. Recommend widening that node's brief.
3. **⚠ Verify before seeding:** a16z Speedrun backing; the company name (heavily garbled — "RealFull"/"Real Flow"/"Real Fall" → Reelful). Confirm the canonical spelling before seeding.
