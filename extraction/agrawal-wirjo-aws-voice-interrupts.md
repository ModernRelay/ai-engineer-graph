# SPIKE extraction — "Voice Agents That Handle Interrupts" (Chintan Agrawal & Daniel Wirjo, AWS) — FOR REVIEW

Source transcript: `transcripts/agrawal-wirjo-aws-voice-interrupts.txt` (auto-captions — paraphrases; "Silero"↔"Celero/Silario", "Cartesia"↔"Cartesiant/Katisha", "Pipecat"↔"Pipe Cat/Pipe Band", "Nemotron"↔"Nemotron-3", "Quindos/Quintela"↔Kwindla Kramer of Daily; "Daniel Weijia" → **Daniel Wirjo**, "Jinson" → **Chintan**).
Video: https://youtu.be/hMlLw1LeIK8 · published 2026-07-20 (AI Engineer, World's Fair).
Slugs follow seed conventions. `pat-harness-over-model` is defined in `bahidika-allou-msft-dont-let-llm-drive.md`.
`stagingTimestamp` for the artifact and all signals: 2026-07-20 (publish date); incident/benchmark dates noted per-signal.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-aws-voice-interrupts` | Voice Agents That Handle Interrupts (Chintan Agrawal & Daniel Wirjo, AWS — AI Engineer World's Fair) | youtube | https://youtu.be/hMlLw1LeIK8 |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-chintan-agrawal`, `ContributedByExpert → exp-daniel-wirjo`.

## Experts (2 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-chintan-agrawal` | Chintan Agrawal (Solutions Architect, AWS APJ startup team) | `co-aws` |
| `exp-daniel-wirjo` | Daniel Wirjo (Solutions Architect, AWS startups team) | `co-aws` |

## Companies (2 new; 2 registry reuse)

| slug | name | type | note |
|---|---|---|---|
| `co-aws` | Amazon Web Services (AWS) | bigtech | speakers' employer; publishes voice reference architecture |
| `co-daily` | Daily.co | developer | maker of Pipecat + Smart Turn; Kwindla Kramer (co-founder) authored the cited latency breakdown |
| **[registry]** `co-salesforce` | — | — | published re-architected voice pipeline (755ms) |
| **[registry]** `co-meta` | — | — | turn-detection paper (87.7% recall, no code) |

> Not promoted to nodes (left as prose in signals): Cartesia, Deepgram, Picovoice, Silero (open-source project), NVIDIA (Nemotron), OpenAI (GPT-4.1). Promote if you want their latency numbers queryable by company.

## Elements (4 new; 1 registry reuse)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-turn-detection` | Turn detection (turn-taking) | concept | harness | Deciding when the user has finished speaking so the agent may respond — the load-bearing voice-UX component; an audio-engineering problem, not an LLM problem |
| `el-silero-vad` | Silero VAD | technology | harness | ~300K-param, 2MB voice-activity-detection model (STFT → 4 conv layers → LSTM → sigmoid speech probability); "level 1" turn-taking you fully own; `minimum_silence_ms` is the whole UX knob |
| `el-smart-turn` | Smart Turn (v3) | framework | harness | Small open (BSD-2, 8MB, pip-installable) end-of-turn model that runs during silence on prosody/intonation; "level 3" atop a local VAD safety-net; v3.2 ≈ 58.9% recall / 68.4% precision |
| `el-pipecat` | Pipecat | framework | harness | Open-source voice-agent orchestration framework (Daily.co); owns pipeline flush/barge-in (~32ms detect + ~15ms flush) and a local prototyping environment |
| **[registry]** `el-mcp` | — | — | not used here — listed only to note no reuse |

Element edges: `el-smart-turn` DevelopedByCompany → `co-daily`; `el-pipecat` DevelopedByCompany → `co-daily`; `el-silero-vad` UsesElement → (n/a; open project — no company node); `el-smart-turn` UsesElement → `el-silero-vad` (VAD backstops Smart Turn); `el-silero-vad` ExemplifiesPattern → `pat-harness-over-model`; `el-smart-turn` ExemplifiesPattern → `pat-harness-over-model`; `el-turn-detection` EnablesPattern → `pat-harness-over-model`. All `IdentifiedInArtifact → ia-aie-aws-voice-interrupts`.

## Patterns

- `FormsPattern → pat-harness-over-model` **[defined in `bahidika-allou-msft-dont-let-llm-drive.md`]** — the whole talk's thesis is that voice quality comes from the audio pipeline, not the model (same LLM+prompt feels broken or smooth purely on turn-taking).

## Signals (6 new)

All: domain `harness` (sig `sig-voice-llm-latency-june26` is `inference`), `SpottedInArtifact → ia-aie-aws-voice-interrupts`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|
| `sig-200ms-turn-taking` | Humans switch conversational turns in ~200ms; at ~800ms voice "feels off," at ~1.5s users hang up — the physics constraint that makes voice a turn-taking problem, not an LLM problem | harness-over-model | el-turn-detection | co-aws |
| `sig-salesforce-755ms` | Salesforce published (Mar 26, 2026) a re-architected voice pipeline whose best measured voice-to-voice response was 755ms — ~4x slower than human turn-taking, still cited as the best measured for a cascaded pipeline | harness-over-model | — | co-salesforce |
| `sig-smart-turn-v3-recall` | Smart Turn v3.2 (open, BSD-2, 8MB) gives ~58.9% recall / 68.4% precision on end-of-turn detection — the best deployable turn detector today; a local VAD timer (~300ms) backstops the ~4-in-10 it misses | harness-over-model | el-smart-turn, el-silero-vad | co-daily |
| `sig-meta-turn-paper-87` | Meta paper (~Mar 2026) reported higher end-of-turn recall (87.7%) but released no code — not deployable | harness-over-model | el-turn-detection | co-meta |
| `sig-voice-llm-latency-june26` | AWS June-2026 voice-LLM benchmark (<700ms TTFT target): Nemotron-3 Ultra 529ms P50, GPT-4.1 536ms P50 but 1.7s P95, Claude 3 over 4s P95 — the P95 tail, not P50, is what breaks voice | harness-over-model | — | — |
| `sig-voice-pipeline-latency-budget` | Daily/Pipecat production breakdown: a standard cloud-API voice pipeline totals ~1,100–1,300ms; STT+LLM eat ~2/3 of budget; co-locating all models on one GPU cluster hit a ~500ms voice-to-voice floor | harness-over-model | el-pipecat | co-daily |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-turn-taking-not-llm-problem` | Voice UX quality is an audio-pipeline problem, not a model problem: identical LLM + identical prompt feels broken or smooth purely based on turn detection and interrupt handling | pat-harness-over-model | el-turn-detection |
| `ins-p95-tail-breaks-voice` | In voice you cannot average latency — one slow P95 response kills the whole conversation, so tail latency and multi-turn instruction-following decay matter more than headline P50 benchmarks | pat-harness-over-model | — |

## KnowHow (2 new)

Both `SourcedFromArtifact → ia-aie-aws-voice-interrupts`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-three-level-turn-detection` | Choose turn detection by the control/portability tradeoff | L1 Silero VAD — own silence detection, tune `minimum_silence_ms` per domain (~200ms sales, ~1–1.2s deliberative); L2 STT-provider endpointing (Cartesia ~300ms / Deepgram Nova-3 ~250ms P50) — smarter but opaque, decisions made in someone else's server; L3 VAD + Smart Turn — own everything, classify barge-ins (correction=stop, backchannel=continue, noise=ignore) | el-silero-vad, el-smart-turn |
| `how-voice-latency-levers` | Engineer the voice latency budget | STT + LLM are the only meaningful levers (~2/3 of budget); benchmark models on P95 not P50 and target <700ms TTFT; co-locate models to kill network hops (~500ms floor); prune context / reset sessions to fight multi-turn instruction decay; false interruptions raise human-escalation rate, so tune the interrupt handler | el-pipecat |

## Dropped

- Live demo narration (British-voice travel assistant; three example runs) — illustrative, no new fact.
- Cartesia/Deepgram P50 endpointing numbers (~300 / ~250ms) kept inside `how-three-level-turn-detection` rather than as standalone signals (vendor latency, no dated study).
- Picovoice Cloud / AWS reference-architecture mentions — deployment options, not intel.

## Review notes

1. `co-daily` (Daily.co) owns both Pipecat and Smart Turn and the cited production latency data (via Kwindla Kramer) — three signals lean on it; confirm the company node.
2. Names are caption-recovered: **Chintan Agrawal** and **Daniel Wirjo** per the task metadata (captions rendered "Jinson" / "Daniel Weijia"). Model/vendor spellings normalized in prose.
3. `sig-voice-llm-latency-june26` has no `RelevantCompany` edge (spans NVIDIA/OpenAI/Anthropic); promote those companies if you want per-vendor queries.
4. All six signals `FormsPattern → pat-harness-over-model`; `sig-salesforce-755ms` and `sig-meta-turn-paper-87` carry real 2026 dates if you'd rather stage them on incident date than publish date.
