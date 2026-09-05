# SPIKE extraction — "While my guitar gently speaks" (Todd Fisher, Philo Ventures) — FOR REVIEW

Source transcript: `transcripts/fisher-philo-guitar-gently-speaks.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/E_Txocq-Lrw — AI Engineer World's Fair, **Generative Media track**, published 2026-08-18.
`stagingTimestamp`: 2026-08-18. Entities marked **[registry]** are already in the registry.
Shape of the talk: a **hobbyist passion-project talk** — an engineer builds a guitar that speaks and sings, chaining audio DSP (JUCE plugin, energy-gap/syllable segmentation, YIN pitch detection, vocoder) with TTS (Piper) and a local LLM for conversational responses. **Thin SPIKE signal** — its only industry-intelligence thread is the "AI makes passion projects buildable; time is no longer the bottleneck" framing. Light extraction by design. Caption garbles: "JUCE" kept, "Piper" kept, "Yin pitch" → **YIN pitch algorithm**, "World" → the **WORLD vocoder**, "Peter Frampton"/"talk box" kept.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-fisher-guitar-gently-speaks` | While my guitar gently speaks (Todd Fisher, Philo Ventures — AI Engineer World's Fair) | youtube | https://youtu.be/E_Txocq-Lrw |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-todd-fisher`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-todd-fisher` | Todd Fisher (Philo Ventures; guitarist building a speaking/singing-guitar side project) | `AffiliatedWithCompany → co-philo-ventures` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-philo-ventures` | Philo Ventures | investor | The speaker's affiliation; no product facts in the talk (the content is a personal passion project). Coined only to carry the affiliation edge; type inferred as investor from "Ventures" — ⚠ unverified, see review note 2 |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-ai-lowers-build-cost` | AI collapses the cost of building | concept | harness | The talk's one transferable point: "the last 6 months with AI have pushed these projects forward — it's super easy now to build whatever cool thing you're passionate about; time is typically not the big time-suck it once was." The charge to the audience: pick a passion project and build it, because AI has removed the friction. A hobbyist-side echo of the democratization-of-building thread |
| `el-guitar-speech-pipeline` | Guitar speech/singing pipeline | technology | robotics | The technical artifact (domain-specific, low industry signal): a JUCE audio plugin chaining **TTS (Piper)** → per-word slicing via **energy-gap + sonority-peak syllable segmentation** → **YIN pitch detection** → synthesized-note + vocoder to make the guitar "sing," plus a conversational mode (mic → Whisper → local LLM → guitar). Pre-baked pitch-shifted vocal samples (WORLD vocoder) mapped per fret. Included for completeness; carries no pattern edge |

Element edges: both `IdentifiedInArtifact → ia-aie-fisher-guitar-gently-speaks`.
`el-guitar-speech-pipeline` `DevelopedByCompany → co-philo-ventures` — *not emitted* (personal project, not a company product; see review note 2);
`el-ai-lowers-build-cost` `ExemplifiesPattern → pat-value-of-judgement` **[registry]**.

Reused elements (no new nodes): `el-whisper`-adjacency (speech-to-text; no dedicated node). No other reuse.

## Signals (1 new)

All: `SpottedInArtifact → ia-aie-fisher-guitar-gently-speaks`, `SourcedFromSource → source-aie-yt` **[registry]**; `RelevantCompany → co-philo-ventures`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-ai-makes-passion-projects-buildable` | harness | The talk's single industry-relevant claim, from a hobbyist: "the last 6 months with AI have pushed these projects forward — it's super easy now to build whatever you're passionate about; time is no longer the big time-suck." Delivered as a charge to build side projects. Weak, anecdotal evidence for the broader democratization-of-building / time-is-not-the-bottleneck thread; a single-person passion-project data point, not an org or market claim | `FormsPattern → pat-value-of-judgement` **[registry]** | `OnElement → el-ai-lowers-build-cost` |

## Insights (0 new)

None — the talk is a personal build story; the one transferable idea is carried by the single signal.

## KnowHow (0 new)

None coined — the guitar-speech pipeline is domain-specific audio DSP with no generalizable agent/industry KnowHow.

## Dropped

- **Essentially the whole talk** — the Slipknot/Stranger-Things live-performance framing, the Halloween-costume origin, the guitar/rock-and-roll history, and the full audio-DSP walkthrough (JUCE, segmentation, YIN, vocoder, WORLD, live demos) are a personal creative-project narrative with no industry-intelligence signal. Retained only: the "AI collapses build cost" charge and the pipeline element (for completeness).

## Review notes

1. **⚑ Thinnest extraction in the batch, by design.** This is a hobbyist passion-project talk with near-zero SPIKE signal — one anecdotal signal on the democratization/time-is-not-the-bottleneck thread (homed weakly on `pat-value-of-judgement`). Included because the user asked to parse all 11; flagged as a candidate to drop entirely if review prefers not to dilute the corpus with a single-person creative project. No pattern-defining content.
2. **⚠ `co-philo-ventures` is barely a company node** — no product facts, type ("investor") inferred from the name and unverified; the guitar project is personal, not a Philo product, so `el-guitar-speech-pipeline`'s `DevelopedByCompany` edge is deliberately **not emitted**. If review wants to keep the corpus tight, this company + the pipeline element are the first things to cut.
3. **⚠ Verify before seeding:** Philo Ventures' nature and the speaker's role there (unclear from the talk); tool names (JUCE, Piper, YIN, WORLD vocoder) are audio-domain and caption-legible but peripheral.
