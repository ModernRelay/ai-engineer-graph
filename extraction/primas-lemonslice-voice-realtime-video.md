# SPIKE extraction — "Voice agents with Realtime Video" (Sidney Primas, LemonSlice) — FOR REVIEW

Source transcript: `transcripts/primas-lemonslice-voice-realtime-video.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/z1dqv74SpUs — AI Engineer World's Fair, **Generative Media track**, published 2026-08-18.
`stagingTimestamp`: 2026-08-18. Entities marked **[registry]** are already in the registry.
Shape of the talk: LemonSlice's bet on **breaking the "avatar Turing test"** — a real-time avatar indistinguishable from a human on a video call. Their approach: take a **video/world model and focus it on humans** (getting emergent physics, micro-expressions, emotions), then make it causal (past-only attention), one-step (30→1 denoising steps), and solve **error accumulation** and **model hardness** (real-time GPU/CPU orchestration). Long-term bet: a single end-to-end **EQ layer** (video+audio in/out) paired with a separate IQ model. Caption garbles: "Lemon Slice" → **LemonSlice**, "DIT" → **DiT**, "model hardness" → **model harness** (systematic — the orchestration layer), "Teddy Roosevelt"/Microsoft partnership kept.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-primas-voice-realtime-video` | Voice agents with Realtime Video (Sidney Primas, LemonSlice — AI Engineer World's Fair) | youtube | https://youtu.be/z1dqv74SpUs |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-sidney-primas`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-sidney-primas` | Sidney Primas (CTO and founder, LemonSlice) | `AffiliatedWithCompany → co-lemonslice` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-lemonslice` | LemonSlice | developer | Real-time avatar company on a mission to "break the avatar Turing test." API layer for the **visual layer** on voice agents (customers bring their own LLM and voice). Shipped a Microsoft partnership bringing Teddy Roosevelt to life in a presidential library. Cost of real-time video avatar "about the same as a voice model" |

Reused **[registry]**, edge-only: `co-microsoft` **[b2]** (the Roosevelt-library partnership). Not coined: Stanford (reference).

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-avatar-turing-test` | The avatar Turing test | concept | robotics | The goal: an avatar "indistinguishable from a human on a video call" — not just photorealism but the long tail (emotions, object interactions, micro-expressions, an internal state). LemonSlice's bet: **most AI-human interaction will have a visual layer**, because humans are biologically wired to understand best with a visual component. They plan to define and publish their own avatar-Turing-test with real people ("we won't pass it this year, but we'll track it") |
| `el-human-focused-world-model` | Human-focused world model | technology | robotics | The approach: rather than the usual avatar methods, **take a video/world model and focus it on humans**. Harder to train and deploy, but you get **emergent properties for free-ish** — full-body movement, object interactions, physics (earrings swing, water moves), micro-expressions, emotions. Trained with heavy focus on **audio** (audio drives emotion/expression; standard audiobook-trained audio encoders are too monotone, so they built expressive audio embeddings) |
| `el-causal-realtime-video` | Causal, one-step, low-error real-time video | technology | inference | The three technical moves that make a video model real-time and interactive: (1) **causal attention mask** — past-only, since the future doesn't exist yet at inference (no future audio); (2) **step distillation** — 30 denoising steps → 1, noise-to-video in a single step; (3) a novel solution to **error accumulation** — the compounding-drift problem where past-only generation feeds its own errors forward, which is fatal for the 8–16-hour continuous streams they run. Cost brought to ~voice-model parity |
| `el-model-harness-orchestration` | Model harness (real-time orchestration) | technology | harness | The overlooked-but-decisive layer: "a lot of our value is in the model **harness**" — orchestrating many threads of real streaming data across GPU and CPU so the video "always remains real time, never stutters," handling interrupts, queues, buffering, cleanup. "Over time more of the value will be in figuring out the model harness — especially for real-time applications." Plus the long-term bet: an end-to-end **EQ layer** (user video+audio in, avatar video+audio out, internal emotional state) paired with a separate **IQ model** for tool-calling/reasoning |
| `el-visual-layer` | The visual layer on every AI interaction | concept | robotics | The market thesis: because humans understand best with a visual component, **most AI-human interaction will carry a visual layer**, and LemonSlice builds that layer as an API over any voice agent — "anything that's a voice agent today becomes a video agent." A claim about the default modality of future AI interfaces, not just an avatar product |

Element edges: all five `IdentifiedInArtifact → ia-aie-primas-voice-realtime-video`.
`el-human-focused-world-model` `EnablesElement → el-causal-realtime-video`;
`el-causal-realtime-video` `UsesElement → el-model-harness-orchestration`;
`el-model-harness-orchestration` `DevelopedByCompany → co-lemonslice`, `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-avatar-turing-test` `ExemplifiesPattern → pat-verification-gap` **[registry]**;
`el-visual-layer` `IdentifiedInArtifact → ia-aie-primas-voice-realtime-video`, `EnablesElement → el-avatar-turing-test`.

Reused elements (no new nodes): `el-realtime-interactive-video` **[b21, Ahres]** (same-batch), `el-world-model` (uncoined — see the Ahres file's review note 4).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-primas-voice-realtime-video`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-lemonslice`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-visual-layer-on-every-ai-interaction` | robotics | The bet: "most interactions between AI and humans will have a visual layer" because humans understand best visually, so LemonSlice builds that layer as an API on top of any voice agent (bring-your-own LLM and voice) — "anything that's a voice agent today becomes a video agent." Evidenced by a Microsoft partnership (Teddy Roosevelt in a presidential library; a VIP stayed 10 min). **HELD PATTERN-LESS** — media-as-medium ledger (see Ahres review note 1) | — (held pattern-less) | `OnElement → el-avatar-turing-test`, `el-visual-layer` |
| `sig-human-focused-world-model-emergence` | robotics | The technical bet: focus a video/world model on humans and get emergent physics, movement, micro-expressions and emotions "more for free" than other avatar approaches — harder to train, but the world-model substrate pays off. Audio is the key data (emotion lives in expressive audio embeddings, not audiobook-trained encoders). World models specialized to a domain as a capability strategy | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-human-focused-world-model`, `el-causal-realtime-video` |
| `sig-model-harness-is-the-real-time-value` | harness | The claim most relevant to the corpus: "a lot of our value is in the **model harness**" — orchestrating streaming data across GPU/CPU so real-time video never stutters, handling interrupts/queues/buffering — "over time more of the value will be in the harness, especially for real-time." A frontier-media practitioner locating durable value in the deterministic orchestration layer around the model, a direct `pat-harness-over-model` claim-1 (reliability) data point from generative media | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-model-harness-orchestration` |
| `sig-eq-layer-vs-iq-layer` | robotics | The architectural forecast: within 2–3 years, a single **end-to-end EQ model** (user video+audio in → avatar video+audio out, with an internal emotional state) paired with a **separate IQ model** for the intelligent work (tool calls, reasoning). Splitting emotional/interactive capability from reasoning capability into two composed models — an architecture claim about how human-facing AI gets built | — (held pattern-less) | `OnElement → el-model-harness-orchestration`, `el-avatar-turing-test` |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-realtime-value-is-in-the-harness` | The most transferable point is that for real-time systems the durable value migrates to the **orchestration harness** — the GPU/CPU thread management that keeps a stream stutter-free through interrupts and buffering — more than to the model, because the model capability commoditizes while flawless real-time orchestration stays hard. That is the corpus's harness-over-model thesis (claim-1, reliability) confirmed from an entirely different domain, and it predicts that real-time media companies compete on hardness, not on model quality — the same conclusion the CUA and voice-agent talks reached | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-model-harness-orchestration`, `el-causal-realtime-video` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-primas-voice-realtime-video`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-realtime-avatars` | Build real-time avatars on a human-focused world model | Start from a **video/world model focused on humans** rather than a bespoke avatar method — it's harder to train but gives emergent physics, movement, micro-expressions and emotions more cheaply; invest heavily in **audio**, since emotion and expression are driven by it and standard audiobook-trained encoders are too monotone; make the model real-time with three moves — a **causal (past-only) attention mask** (the future doesn't exist at inference), **step distillation** from ~30 denoising steps to 1, and a real solution to **error accumulation** (past-only generation compounds its own drift, fatal for hour-long streams); and recognize that **the model harness is where much of the value is** — orchestrating streaming data across GPU and CPU so the video never stutters through interrupts, queues and buffering, especially for real-time; architecturally, expect to split an **EQ layer** (end-to-end video+audio with internal state) from a separate **IQ model** for reasoning and tool use | `ReferencesElement → el-avatar-turing-test`, `el-human-focused-world-model`, `el-causal-realtime-video`, `el-model-harness-orchestration` |

## Dropped

- **The Teddy-Roosevelt/Trump demo footage** — the partnership is in `co-lemonslice`; the demo colour dropped.
- **The clothes/scene-change and physics-on-earrings demos** — illustration of emergent world-model properties.
- **The deepfake Q&A** ("not our goal, but you could with the right harness around it") — kept as one clause in `el-model-harness-orchestration`'s logic.

## Review notes

1. **The media talk with the clearest `pat-harness-over-model` (claim-1) contribution.** `sig-model-harness-is-the-real-time-value` is a reliability-side data point ("value is in the orchestration harness, not the model") from generative media — supporting the pattern on exactly the reading b15 FINDING 1 recommends scoping to. Note the systematic caption garble "model hardness" → **model harness**; confirm before seeding.
2. **⚑ `el-visual-layer` referenced but define carefully** — the "visual layer on every AI interaction" concept is coined implicitly via `sig-visual-layer-on-every-ai-interaction`'s OnElement edge; if seeding, coin `el-visual-layer` from this file. Held pattern-less on the media-as-medium ledger with Ahres/uRun/Nereu/Reelful.
3. **⚠ Verify before seeding:** the Microsoft/Roosevelt partnership; cost-parity-with-voice-model claim; 8–16-hour continuous stream figures; the EQ/IQ split forecast (2–3 years). All vendor-stated.
4. **`el-world-model` uncoined** — same flag as the Ahres file; recommend coining centrally and re-pointing.
