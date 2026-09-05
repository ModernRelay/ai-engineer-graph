# SPIKE extraction — "Generative Video at the Speed of Light" (Keegan McCallum, uRun) — FOR REVIEW

Source transcript: `transcripts/mccallum-urun-generative-video-speed.txt` (auto-captions — quotes are paraphrases, not verbatim; short talk, ~9 min).
Video: https://youtu.be/Xln-On3syJk — AI Engineer World's Fair, **Generative Media track**, published 2026-08-18.
`stagingTimestamp`: 2026-08-18. Entities marked **[registry]** are already in the registry.
Shape of the talk: the efficiency-axis counterpart to the media-track thesis — generative video is improving not just on quality (Will-Smith-spaghetti → Sora → Seedance) but on **efficiency and long-horizon generation**: ~40 real-time-capable models released this year, $10 buys ~3 hours of continuous generated video. uRun is an inference provider for interactive media, arguing 2026 needs **software factories for media** — CLI/MCP so agents can build these applications. Caption garbles: "U Run/You Run/YURUN" → **uRun**, "Juan 2.1 14B" → **Wan 2.1 14B**, "Clockwork" → likely **OpenClaw/a coding agent** (⚠ note 3), "Gemini Omni" kept.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-mccallum-generative-video-speed` | Generative Video at the Speed of Light (Keegan McCallum, uRun — AI Engineer World's Fair) | youtube | https://youtu.be/Xln-On3syJk |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-keegan-mccallum`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-keegan-mccallum` | Keegan McCallum (founder, uRun) | `AffiliatedWithCompany → co-urun` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-urun` | uRun | developer | "A new kind of inference provider focused around interactive media." Serves **Helios** (a distill of Wan 2.1 14B) and other real-time models; ships a React component + programmable Python runtime + CLI/MCP for building interactive-video apps. Hiring; looking for design partners on human-computer interaction |

Reused **[registry]**, edge-only: `co-google` **[b2]** (Gemini Omni for full-fidelity render-out). Referenced: LemonSlice (avatar models — same batch), OpenAI/Sora, ByteDance/Seedance.

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-generative-video-efficiency-axis` | The efficiency axis of generative video | concept | inference | The reframe from quality to cost/length: quality gets the attention (Will-Smith-spaghetti 2023 → Sora → Seedance photorealism), but the bigger shift is **efficiency and long-horizon generation** — ~40 real-time-capable, long-horizon models released this year; Helios (a Wan 2.1 14B distill) generates continuously at ~last-year's-frontier quality for ~1/100th the cost. "$10 gets you 3 hours of continuous generated video; $50 gives you a full day interacting with an AI in a visual medium." Steerable in <1s while generating, ending the slot-machine approach |
| `el-realtime-media-harness` | Real-time media harness | technology | infra | The infra the applications need: GPUs worldwide, connection routing, **WebRTC/ICE/TURN**, and for the interesting use cases **multiple models wired into continuous streaming workflows** synchronized frame-by-frame with user controls. uRun's answer: a drop-in **React component** plus a **programmable Python runtime** to build avatar / video-to-video / magic-mirror pipelines generating asynchronously. "The models are here; the frontier is really in how we serve them" |
| `el-software-factories-for-media` | Software factories for media | concept | harness | The 2026 claim: "we don't just need platforms, we need **software factories** and ways for agents to interact with these" — so uRun exposes a **CLI and MCP server** letting agents build interactive-media applications. The software-factory thesis (b11/b13/b17) extended from code to generative media: agents building media apps, not just humans | 

Element edges: all three `IdentifiedInArtifact → ia-aie-mccallum-generative-video-speed`.
`el-realtime-media-harness` `DevelopedByCompany → co-urun`, `UsesElement → el-generative-video-efficiency-axis`;
`el-software-factories-for-media` `UsesElement → el-realtime-media-harness`, `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-generative-video-efficiency-axis` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**.

Reused elements (no new nodes): `el-mcp` **[seed]** (agent access to media generation), `el-realtime-interactive-video` **[b21, Ahres]** (same-batch shared concept), `el-lights-off-software-factory`/`el-humanlayer` adjacency (software-factory thread).

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-mccallum-generative-video-speed`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-urun`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-generative-video-collapses-in-cost` | inference | The efficiency claim: ~40 real-time/long-horizon video models released this year, and a Wan-2.1-14B distill generates continuously at last-year's-frontier quality for ~1/100th the cost — "$10 buys 3 hours, $50 a full day of visual AI interaction," steerable in under a second. Generative video following the same cost-collapse curve the corpus tracked for LLM inference, moving the frontier from quality to serving efficiency | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-generative-video-efficiency-axis` |
| `sig-realtime-media-needs-a-harness` | infra | The infra claim: building interactive-media apps needs global GPUs, WebRTC/ICE/TURN, and multiple models wired into frame-synchronized streaming workflows — "the models are here; the frontier is how we serve them." uRun's drop-in React component + Python runtime is the harness. The value-in-the-harness thesis applied to real-time media serving, convergent with Ahres/Reactor and the Krea infra talks this batch | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-realtime-media-harness` |
| `sig-agents-build-media-apps` | harness | The software-factory extension: "in 2026 we need software factories and ways for agents to interact with these," so uRun ships a **CLI and MCP** for agents to build interactive-media applications. Agents building media apps, not just code — the software-factory thread crossing from software into generative media. **HELD PATTERN-LESS** — bears on `pat-ai-native-org` (agents as the builders) and the media-as-medium ledger | — (held pattern-less) | `OnElement → el-software-factories-for-media`, `el-mcp` **[registry, seed]** |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-media-frontier-is-serving-not-quality` | The talk's sharp point is that the interesting frontier in generative video has moved from model quality (already photorealistic) to **serving efficiency and orchestration** — cost-per-hour, steerability-under-a-second, and wiring multiple models into synchronized real-time streams. That mirrors the LLM story exactly: once the model is good enough, value migrates to the layers around it (inference, harness, agent access), which is why a media company positions itself as an inference provider and ships CLI/MCP for agents rather than a better model | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-generative-video-efficiency-axis`, `el-realtime-media-harness` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-mccallum-generative-video-speed`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-serve-interactive-media` | Serve interactive media as the real frontier | Recognize that generative video's frontier has shifted from quality to **efficiency, long-horizon generation, and serving** — quality is largely solved, so compete on cost-per-hour and steerability (aim for <1s in-generation steering, not slot-machine one-shots); build the **real-time media harness** the applications actually need — global GPUs, WebRTC/ICE/TURN, and multiple models wired into frame-synchronized streaming workflows generating asynchronously — and consider a drop-in component so app builders don't rebuild it; expose your capability to **agents via CLI and MCP**, since 2026 media apps will increasingly be agent-built ("software factories for media"), not hand-assembled; and target the interaction modes cost unlocks (magic-mirror try-on, visual companions/accessibility, real-time content steering) rather than just longer clips | `ReferencesElement → el-generative-video-efficiency-axis`, `el-realtime-media-harness`, `el-software-factories-for-media` |

## Dropped

- **The quality-progression montage** (Will Smith spaghetti → Sora → Seedance) — framing for `el-generative-video-efficiency-axis`.
- **The use-case tour** (magic mirror, accessibility, content creation) — illustration.
- **The over/under-time meta-joke and hiring pitch** — logistics.

## Review notes

1. **Tight convergence with the rest of the media track** — with Ahres/Reactor and both Krea talks, four same-batch talks argue the media frontier is *serving infrastructure*, not model quality, which is the cleanest cross-domain confirmation of `pat-model-not-bottleneck` outside language. `sig-agents-build-media-apps` is held pattern-less on the media-as-medium / `pat-ai-native-org` boundary.
2. **⚠ Verify before seeding:** the ~40-models and $10/3-hours and 1/100th-cost figures; "Helios = Wan 2.1 14B distill"; "Clockwork" (the token-burning coding agent — likely OpenClaw or a garble). All vendor-stated in a short talk.
3. **`el-software-factories-for-media` extends the software-factory thread** (b11 Horthy, b13, b17) into generative media — worth noting if that thread is ever coined.
