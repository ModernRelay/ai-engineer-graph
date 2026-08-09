# SPIKE extraction — "Your Voice Agent Doesn't Need a Frontier Model" (Joel Allou & Ornella Bahidika, Microsoft) — FOR REVIEW

Source transcript: `transcripts/allou-bahidika-msft-voice-agent-no-frontier.txt` (auto-captions — paraphrases; "A"/"A is" → **Ace**; heavy transcription noise in the opening).
Video: https://youtu.be/fnLBmfsI_Fg · published 2026-07-20 (AI Engineer, World's Fair).
**Companion to `ia-aie-msft-dont-let-llm-drive`** — same speakers, same Ace product, latency/cost emphasis instead of control emphasis. Shared entities (experts, `co-microsoft`, `el-ace-voice-tutor`, `el-harness-engineering`, `el-agent-state-machine`, `el-claude-haiku-45`, `el-claude-opus-47`, `pat-harness-over-model`) are **defined in that file** and referenced here by slug.
`stagingTimestamp` for the artifact and all signals: 2026-07-20.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-msft-voice-no-frontier` | Your Voice Agent Doesn't Need a Frontier Model (Joel Allou & Ornella Bahidika, Microsoft — AI Engineer World's Fair) | youtube | https://youtu.be/fnLBmfsI_Fg |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-joel-allou`, `ContributedByExpert → exp-ornella-bahidika`.

## Experts / Companies / Elements (all registry reuse — see paired file)

- Experts: `exp-joel-allou`, `exp-ornella-bahidika` (both AffiliatedWithCompany `co-microsoft`).
- Companies: `co-microsoft`, `co-anthropic`.
- Elements: `el-ace-voice-tutor`, `el-harness-engineering`, `el-agent-state-machine`, `el-claude-haiku-45`, `el-claude-opus-47`. All also `IdentifiedInArtifact → ia-aie-msft-voice-no-frontier` (an element can be identified in more than one artifact).

No new supportive nodes in this talk.

## Signals (3 new)

All: domain `harness` (sig 2 arguably `inference`), `SpottedInArtifact → ia-aie-msft-voice-no-frontier`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|
| `sig-voice-950ms-budget` | Microsoft: a live voice tutor must start talking in ~950ms or the user's brain reads the agent as "dead"; a frontier model that thinks for a full second "has already lost the room, no matter how good the answer" — the budget is milliseconds, not IQ | harness-over-model | — | co-microsoft |
| `sig-ace-900ms-haiku` | On Ace, replacing Opus 4.7 with harness-scaffolded Haiku 4.5 dropped time-to-first-response to ~900ms (vs several seconds of Opus reasoning shown side-by-side) with no perceived quality loss | harness-over-model | el-claude-haiku-45, el-claude-opus-47 | co-microsoft, co-anthropic |
| `sig-scaffolding-paid-once` | Small models drift on long structure and need strict scaffolding — but the scaffolding cost is "paid once, in code," not on every turn; inverts the per-token cost of letting a big model reason each turn | harness-over-model | el-harness-engineering | co-microsoft |

## Insights (1 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-fastest-model-latency-budget` | The rule for real-time agents: pick the fastest model your latency budget allows, then spend the rest of your effort on scaffolding — for voice/real-time/high-volume systems the model is the smallest part of the system | pat-harness-over-model | el-harness-engineering |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-msft-voice-no-frontier`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-small-model-plus-scaffolding` | Trade a frontier model for small-model-plus-scaffolding | Extract all thinking/state/logic into code (state machine + an "intelligent layer" that hands the model a fresh summary every turn); leave the model only the one thing it's best at (speaking); pick the fastest model in budget; accept the one-time scaffolding cost. True for voice, real-time, and any high-volume system | el-harness-engineering, el-ace-voice-tutor |

## Dropped

- Nothing beyond vendor framing was cut. The talk is short and overlaps the companion talk heavily; signals here are deliberately the **latency/cost** claims (950ms budget, ~900ms result, cost-paid-once) to avoid duplicating the companion's **control/reliability** signals.

## Review notes

1. Overlap: this and `ia-aie-msft-dont-let-llm-drive` are two halves of one Ace pitch. I kept them as two artifacts (as instructed) with disjoint signal sets — merge the signal sets only if you'd rather collapse to one talk.
2. `sig-voice-950ms-budget` vs the AWS talk's `sig-200ms-turn-taking` (human turn-taking ~200ms) are different measurements (start-talking budget vs turn-switch physics) from different artifacts — kept separate, both under `pat-harness-over-model`.
3. The "hand the model a summary every turn" mechanism is folded into `how-small-model-plus-scaffolding` rather than made its own element.
