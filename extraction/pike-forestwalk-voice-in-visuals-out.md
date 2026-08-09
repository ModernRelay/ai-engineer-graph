# SPIKE extraction — "Voice In, Visuals Out: The Agony and the Ecstasy" (Allen Pike, Forestwalk Labs) — FOR REVIEW

Source transcript: `transcripts/pike-forestwalk-voice-in-visuals-out.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/65X0pQ6Lmbg — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact, signals, and knowhow: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-pike-voice-visuals` | Voice In, Visuals Out: The Agony and the Ecstasy (Allen Pike, Forestwalk Labs — AI Engineer World's Fair) | youtube | https://youtu.be/65X0pQ6Lmbg |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-allen-pike`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-allen-pike` | Allen Pike (co-founder, Forestwalk Labs; builds real-time voice-in/visuals-out agents) | `AffiliatedWithCompany → co-forestwalk` |

## Companies (2 new)

| slug | name | type | brief |
|---|---|---|---|
| `co-forestwalk` | Forestwalk Labs | developer | Startup building real-time in-call AI agents with voice input and generated-visual output |
| `co-thinking-machines-lab` | Thinking Machines Lab | research | AI research company (Mira Murati); cited for a continuous-inference voice architecture demo — ⚠ attribution partly garbled, see Review notes |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-voice-in-visuals-out` | Voice in, visuals out | concept | harness | Interaction paradigm pairing spoken input (highest-bandwidth human output: more words/minute, more meaning per word) with generated visual output (rich HTML, interactive controls, images); trades the ~200ms conversational-voice latency budget for the ~1s visual attention envelope, so real-time AI feels seamless without waiting for novel model architectures |
| `el-prefix-caching` | Prefix caching | technology | inference | Inference-platform optimization: when the leading portion of the context is identical across requests it is cached, giving up to ~90% cheaper/faster turns; architectural consequence — keep the first ~90% of the context window stable request-to-request, vary only the tail, and minimize output tokens |

Element edges: `el-voice-in-visuals-out` `UsesElement → el-generative-ui` **[registry]**; both `IdentifiedInArtifact → ia-aie-pike-voice-visuals`.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-pike-voice-visuals`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-karpathy-voice-in-visuals-out` | harness | Karpathy argued (month before talk, paraphrase) that voice is the human-preferred input for AI and visuals the preferred output; a practitioner reports the enabling breakthroughs landed only in recent months — models now emit rich HTML, interactive controls, and images via tool calling, lifting the ceiling on visual output | — | `OnElement → el-voice-in-visuals-out`, `OnElement → el-generative-ui` **[registry]** |
| `sig-gpt5-mini-latency-tax` | inference | Production finding: GPT-5 mini, though small and cheap, showed 5,000ms typical / 7,000–10,000ms P95 latencies — never fast enough for real-time; Haiku-class models on latency-prioritizing inference platforms are the only viable real-time tier. Small model ≠ fast model; the serving platform decides | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-claude-haiku-45` **[registry]**; `RelevantCompany → co-openai` **[registry]**, `RelevantCompany → co-anthropic` **[registry]** |
| `sig-forestwalk-incall-action-agent` | harness | Forestwalk runs a voice agent inside its team calls that takes real-time action on spoken intent — a bug mentioned in conversation was filed as a Linear issue within ~1 second of "let's file that"; ambient, non-interruptive action-taking during human conversation now feels natural once latency is dialed in | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-forestwalk` |
| `sig-thinking-machines-200ms-slices` | inference | Weeks before the talk, Thinking Machines (+ second name garbled, "Neolab") demoed a voice-in/voice-out architecture that time-slices continuous inference into 200ms chunks to hit the conversational latency floor — model-side workaround exists but isn't required if you switch the output modality | — | `RelevantCompany → co-thinking-machines-lab` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-visual-envelope-sidesteps-latency` | The tyranny of latency is beaten by paradigm choice, not model speed: full voice-to-voice needs ~200ms turns (network + STT + inference makes that near-impossible), but humans grant ~1s for something to appear on screen. Voice-in/visuals-out relocates the product into the envelope you can actually hit | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-voice-in-visuals-out` |
| `ins-latency-is-a-platform-property` | Real-time model selection is about serving characteristics, not intelligence or parameter count — a "small" model on a throughput-oriented platform can be 10x too slow while a Haiku-class model on a latency-prioritized platform meets budget; capability moved out of the bottleneck, the inference layer moved in | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | — |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-pike-voice-visuals`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-realtime-latency-envelope` | Hit the real-time envelope for voice-in/visuals-out agents | (1) Use a Haiku-class fast model on an inference platform that prioritizes latency (judge by P95, not size/price), with deliberately short context; hand heavier work to a larger model asynchronously and re-interleave its results into the real-time stream. (2) Send inference eagerly every 1–2 seconds while the user is still speaking instead of waiting for a second of silence — turn-end waiting alone blows a 1s budget. (3) Run a stable caching regimen: keep the first ~90% of the context identical across requests to exploit prefix caching (up to ~90% cheaper/faster), and minimize output tokens. Human limits to design against: ~100ms feels instant, ~1s is the train-of-thought limit, ~200ms is the conversational-voice floor | `ReferencesElement → el-voice-in-visuals-out`, `ReferencesElement → el-prefix-caching`, `ReferencesElement → el-claude-haiku-45` **[registry]** |

## Dropped

- Siri / ChatGPT voice mode anecdotes — color for "voice interfaces so far are slow and dumb"; folded into signal 1 context, no nodes.
- Linear (issue tracker) — the acted-on tool in the demo anecdote; prose only.
- 1960s HCI research on 100ms responsiveness — kept as context inside the knowhow.

## Review notes

1. **"Thinking Machines and Neolab" garble** — could be one entity ("Thinking Machines' Neolab") or two. Coined `co-thinking-machines-lab` (Mira Murati's lab is the obvious 2026 referent for a continuous-inference voice demo) and flagged. If the second token is actually MIT Media Lab, add `RelevantCompany → co-mit-media-lab` **[registry]** to `sig-thinking-machines-200ms-slices` at review; I did not add that edge on a phonetic guess.
2. "Haiku" is unversioned in-talk; linked registry `el-claude-haiku-45` as the contemporaneous Haiku. Downgrade to prose if too strong.
3. GPT-5 mini deliberately not coined as an Element (one benchmark anecdote); latency numbers live in `sig-gpt5-mini-latency-tax`.
4. Captions say "Alan Pike" / "Forest Walk"; normalized to Allen Pike / Forestwalk Labs per official listing.
5. Pattern split judgment: platform-latency material → `pat-model-not-bottleneck`; paradigm/technique material (design around the model) → `pat-harness-over-model`. `sig-karpathy-voice-in-visuals-out` and `sig-thinking-machines-200ms-slices` left pattern-less on purpose (paradigm observation / dated demo fact).
6. Karpathy is cited (registry `exp-karpathy`) but schema has no Signal→Expert edge; attribution kept in the signal brief.
