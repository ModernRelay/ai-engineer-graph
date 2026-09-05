# SPIKE extraction — "The Next Medium: Real-Time Interactive Video" (Ahmed Ahres, Reactor) — FOR REVIEW

Source transcript: `transcripts/ahres-reactor-realtime-interactive-video.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/5dCAmSDOAjI — AI Engineer World's Fair, **Generative Media track**, published 2026-08-18.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-18 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the thesis talk of the media track — **world models = real-time interactive video**, and real-time changes what the medium *is* (as GPS did for maps → Uber, and digital viewfinders did for film → Instagram/TikTok). Surveys three model classes (infinite/interactive Veo-like; Genie-3-like controllable worlds; live avatars) and Reactor's "world behind an API" infra thesis: sub-100ms latency needs global GPUs, live sessions need memory, streaming isn't batch inference. Caption garbles: "Reactor" kept, "Vio/VO3" → **Veo 3**, "C dance 2/CDNS" → **Seedance 2**, "Link bot" → likely a world-model name (⚠ note 3), "Long live 2" → **LongLive 2** (NVIDIA), "sound streaming" → likely a video-to-video model name.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-ahres-realtime-interactive-video` | The Next Medium: Real-Time Interactive Video (Ahmed Ahres, Reactor — AI Engineer World's Fair) | youtube | https://youtu.be/5dCAmSDOAjI |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-ahmed-ahres`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-ahmed-ahres` | Ahmed Ahres (head of go-to-market, Reactor; background in computer vision / ML; shipped iOS/Android games) | `AffiliatedWithCompany → co-reactor` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-reactor` | Reactor | developer | Series-A platform for **real-time world models** — a developer platform/API serving interactive-video models (Helios/ByteDance, a Genie-3-like world model from Alibaba, LongLive 2 and a video-to-video model from NVIDIA). Thesis: "the world behind an API" — democratize real-time interactive video |

Reused **[registry]**, edge-only: `co-bytedance` — *new-adjacent* (Helios model; coined here as reference? see review note 2), `co-nvidia` **[b2]** (LongLive 2), `co-google` **[b2]** (Genie 3, Veo 3). Not coined: Alibaba, Netflix (Bandersnatch reference).

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-realtime-interactive-video` | Real-time interactive video as a medium | concept | robotics | The core claim: generated video today "is still a recording — a slot machine you can't change," but **real-time makes video programmable** (addressable, conditionable, changeable like software). The historical argument: real-time has always been the unlock — GPS made maps real-time and enabled Uber; digital viewfinders let you see what you're shooting and enabled Instagram/TikTok. "Instant feedback is the ultimate level of control." Defines world models *as* real-time interactive video, against the Gaussian-splatting or batch-video readings |
| `el-interactive-video-model-classes` | Three classes of interactive video models | concept | robotics | The taxonomy: (1) **infinite/interactive Veo-likes** — continue forever, changeable mid-stream, real-time (prompt "a cat shows up" and it appears); (2) **Genie-3-like controllable worlds** — image+text in, control a character/world, beyond games into interactive experiences (Bandersnatch-style), robotics training-data generation, and education ("step into a history lesson"); (3) **live interactive avatars** — still not cracked, "kind of off," but rising in research preview for customer support, sales, streaming. Combining the three is where new experiences emerge |
| `el-world-behind-an-api` | The world behind an API | concept | infra | Reactor's infra thesis: serving real-time interactive video is fundamentally different from batch video generation. Batch = a request runs a cloud job returning a file; **real-time needs streaming pixels server→client**, treats everything as a **live session with memory** (the hard problem: models like Genie 3 forget when a character looks away, so maintaining the context window is core), and needs **global scale** — sub-100ms latency means routing a user in India/Japan to a nearby GPU, or "the medium breaks." Integratable in ~10 lines of code behind an API key |
| `el-realtime-video-evals-unsolved` | Real-time video evals are unsolved | concept | robotics | An honest limitation: evaluating real-time interactive video for consistency/fidelity is an **open research problem** — "the entire research community, including DeepMind, hasn't solved this." Fidelity is easy (pixels); consistency and world-coherence evaluation is "literally just look at it and human judgment" today. A frontier-labs-included admission that the field lacks measurement for its core capability |

Element edges: all four `IdentifiedInArtifact → ia-aie-ahres-realtime-interactive-video`.
`el-realtime-interactive-video` `EnablesElement → el-interactive-video-model-classes`;
`el-world-behind-an-api` `UsesElement → el-realtime-interactive-video`, `DevelopedByCompany → co-reactor`;
`el-interactive-video-model-classes` `UsesElement → el-world-model` *(see reuse note)*;
`el-realtime-video-evals-unsolved` `ExemplifiesPattern → pat-verification-gap` **[registry]**.

Reused elements (no new nodes): `el-world-model` — ⚠ **not previously coined** as a registry element despite many mentions; this file uses "world model" as the organizing concept but coins the more specific `el-realtime-interactive-video` instead (see review note 4). `el-microworlds` **[b6]** adjacency (world simulation) kept in prose.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-ahres-realtime-interactive-video`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-reactor`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-realtime-makes-video-a-new-medium` | robotics | The thesis: real-time doesn't just make video faster, it changes the medium — generated video becomes **programmable** (addressable, changeable mid-stream) rather than a fixed recording, "ending the slot-machine mentality." The historical pattern offered as evidence: GPS→Uber, digital viewfinder→Instagram/TikTok — real-time feedback each time unlocked a category that couldn't exist before. A claim that world models are a new interactive medium, not a video-quality improvement. **HELD PATTERN-LESS** — opens a media-as-medium ledger (see review note 1) | — (held pattern-less) | `OnElement → el-realtime-interactive-video`, `el-interactive-video-model-classes` |
| `sig-world-models-generate-robotics-data` | robotics | A concrete application beyond entertainment: because controllable world models can simulate any environment, they generate **infinite training data for robotics** — "a ginormous market; I can't tell you the number of robotics labs training these models." World simulation as a data-supply engine for embodied AI, connecting the generative-media track to the robotics/training thread | `FormsPattern → pat-environments-economy` **[registry]**-adjacent — **HELD PATTERN-LESS** (uncoined; see review note 1) | `OnElement → el-interactive-video-model-classes` |
| `sig-realtime-media-infra-is-the-hard-part` | infra | The infra claim: real-time interactive video "is a different ballgame" from batch — streaming pixels, live sessions with **memory** (the forgetting problem is core), and **global sub-100ms GPU placement** or the medium breaks. Value in the serving infrastructure and the developer platform ("world behind an API"), not just the model. Convergent with the uRun/Krea infra talks in this batch on real-time-media-serving as the differentiator | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-world-behind-an-api` |
| `sig-video-consistency-evals-unsolved` | robotics | The honest gap: evaluating real-time video consistency is unsolved "including DeepMind — nobody has solved this; today it's literally look at it and human judgment." The field's core capability lacks a measurement, echoing the benchmark-trust and evals threads from the LLM side — generative media has a verification gap of its own | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-realtime-video-evals-unsolved` |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-realtime-is-a-medium-shift-not-a-speedup` | The talk's one durable idea is the GPS/viewfinder analogy: real-time doesn't make an existing medium faster, it changes what the medium *is* by adding a feedback loop, and each historical instance unlocked a category (ride-hailing, short-form video) invisible from the batch version. If interactive video is genuinely that kind of shift, the applications won't be "better AI video" but new interactive forms — games-that-are-movies, real-time ads, embodied-AI simulators — which is why the infra bet (memory, streaming, global latency) matters more than model quality. The unsolved-evals admission is the honest counterweight | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-realtime-interactive-video`, `el-world-behind-an-api` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-ahres-realtime-interactive-video`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-realtime-interactive-video` | Build for real-time interactive video as a new medium | Treat real-time as a **medium change, not a speedup** — the value is the feedback loop that makes video programmable (addressable, changeable mid-stream), so design for interaction rather than better one-shot generation; know the **three model classes** and that combining them (infinite interactive video + controllable worlds + live avatars) is where new experiences emerge; build **real-time infrastructure, not batch** — stream pixels server-to-client, treat every generation as a **live session with memory** (solving the forgetting problem is core, since world models lose coherence when the view changes), and place GPUs **globally for sub-100ms latency** or the medium breaks; look beyond entertainment to **robotics training-data generation** (simulate any environment for infinite data) and education; and accept that **consistency evaluation is unsolved** — fidelity is pixels but coherence is human judgment today, so don't over-claim measurable quality | `ReferencesElement → el-realtime-interactive-video`, `el-interactive-video-model-classes`, `el-world-behind-an-api`, `el-realtime-video-evals-unsolved` |

## Dropped

- **The advertising vision** (real-time ads inserted based on what you looked at) — speculative; one clause in `el-interactive-video-model-classes`.
- **The community-use-case list** (interactive livestreams, medical/cooking simulation, video editing) — illustration.
- **The promo code / 16-vs-30-FPS Q&A** — logistics/technical asides.

## Review notes

1. **⚑ Media-track scope note.** This is the media track's thesis talk. Two signals are held pattern-less because they open threads the corpus hasn't coined: a **media-as-new-medium** thread (real-time interactive video / world models as an interactive form, shared with uRun, LemonSlice, Nereu, Reelful in this batch) and the **world-models-as-robotics-data** thread (touching the uncoined `pat-environments-economy`). If the media track recurs, these are candidate ledgers. Per the standing scope question (media vs the agent-engineering spine), flagged for review rather than coined.
2. **⚠ `co-bytedance` coined-on-reference status** — Helios (the interactive video model Reactor serves) is ByteDance's; ByteDance had no prior corpus node. Coined here on reference per the b2 precedent, OR left as a prose reference — flagged for the reconciler. Alibaba similarly referenced (the Genie-3-like model) but not coined.
3. **⚠ Verify before seeding:** model names are heavily garbled — "Seedance 2" (C dance 2), "Helios", "LongLive 2" (Long live 2), the Alibaba world model ("Link bot"), the NVIDIA video-to-video model ("sound streaming"). Sub-100ms latency and 10-lines-of-code claims are vendor-stated.
4. **⚠ `el-world-model` is uncoined despite heavy corpus use.** "World model" appears across b6 (microworlds), b19 (Su's world-model-of-environment), and this whole media track, but no registry element `el-world-model` exists. Recommend coining it centrally at review as the shared concept, and re-pointing this file's `el-interactive-video-model-classes` `UsesElement` edge to it. Left as a flag, not emitted, to avoid a half-defined node.
