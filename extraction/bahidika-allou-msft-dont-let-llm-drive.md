# SPIKE extraction — "Don't Let the LLM Drive" (Ornella Bahidika & Joel Allou, Microsoft) — FOR REVIEW

Source transcript: `transcripts/bahidika-allou-msft-dont-let-llm-drive.txt` (auto-captions — quotes are paraphrases, not verbatim; the tutor product is transcribed as "A"/"ACE" → **Ace**, speaker "Onela" → **Ornella**).
Video: https://youtu.be/m24UKZomm7k · published 2026-07-20 (AI Engineer, World's Fair).
Slugs follow seed conventions. Entities marked **[registry]** already exist — edges link, no new node.
`stagingTimestamp` for the artifact and all signals: 2026-07-20 (publish date).

> This file also **defines the one new pattern** shared across the batch-2 voice/harness talks: `pat-harness-over-model`. Talks 2–4 reference it by slug.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-msft-dont-let-llm-drive` | Don't Let the LLM Drive (Ornella Bahidika & Joel Allou, Microsoft — AI Engineer World's Fair) | youtube | https://youtu.be/m24UKZomm7k |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-ornella-bahidika`, `ContributedByExpert → exp-joel-allou`.

## Experts (2 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-ornella-bahidika` | Ornella Bahidika (Microsoft; co-builder of Ace) | `co-microsoft` |
| `exp-joel-allou` | Joel Allou (Microsoft; co-builder of Ace) | `co-microsoft` |

## Companies (1 new; 1 registry reuse)

| slug | name | type | note |
|---|---|---|---|
| `co-microsoft` | Microsoft | bigtech | employer of both speakers; Ace built here |
| **[registry]** `co-anthropic` | — | — | Claude Opus 4.7 / Haiku 4.5 references |

## Elements (5 new — shared with the paired talk `ia-aie-msft-voice-no-frontier`)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-ace-voice-tutor` | Ace | product | harness | Live AI voice tutor that runs a full multi-step lesson start-to-finish reliably by keeping the LLM out of the control loop |
| `el-harness-engineering` | Harness engineering | concept | harness | Moving reasoning, state, and control flow out of the model into deterministic scaffolding — "the model is the talent, the harness is the director"; model proposes, harness decides |
| `el-agent-state-machine` | Agent state machine | concept | harness | A workflow expressed as explicit states with harness-owned transitions; each step hands the model a single-step "neural contract" (do one thing, return it) and the model never decides which step it is on |
| `el-claude-haiku-45` | Claude Haiku 4.5 | product | inference | Anthropic's small/fast model; carries Ace's per-turn work once the reasoning is scaffolded out |
| `el-claude-opus-47` | Claude Opus 4.7 | product | inference | Anthropic frontier model; the "heavy" baseline Ace deliberately avoids for the live loop |

Element edges: `el-ace-voice-tutor` DevelopedByCompany → `co-microsoft`; `el-claude-haiku-45` DevelopedByCompany → `co-anthropic`; `el-claude-opus-47` DevelopedByCompany → `co-anthropic`; `el-ace-voice-tutor` UsesElement → `el-harness-engineering`; `el-ace-voice-tutor` UsesElement → `el-claude-haiku-45`; `el-harness-engineering` UsesElement → `el-agent-state-machine`; `el-harness-engineering` EnablesPattern → `pat-harness-over-model`; `el-agent-state-machine` ExemplifiesPattern → `pat-harness-over-model`.
All five `IdentifiedInArtifact → ia-aie-msft-dont-let-llm-drive`.

## Patterns (1 new — the batch-2 macro-thesis; 0 reuse here)

| slug | name | kind | brief |
|---|---|---|---|
| `pat-harness-over-model` | The Harness Over the Model | dynamic | As multi-step and real-time agents move from demo to production, the load-bearing engineering shifts **off the model and into the deterministic scaffolding around it** — state machines, validators, turn-detection, rule engines, latency budgets. Reliability is reframed as a control problem, not a prompting problem; the frontier model is often the smallest, most swappable part of the system, and a smaller/faster/cheaper model plus scaffolding beats a bigger model driving itself. |

> **Pattern altitude note:** this is a seed-level claim about *what is changing* (a design center of gravity moving outward from the model), not a domain — signals carry `domain: harness`. It is distinct from `pat-verification-gap` (trust/validation outside the model): verification-outside-the-model is one *special case* of control-outside-the-model.
> Cross-link: `pat-verification-gap` ReliesOnPattern → `pat-harness-over-model`.
> Evolution seed: named by the voice/harness talks (Microsoft Ace ×2, AWS turn-taking) and echoed by the Risa no-touch-oncology talk (deterministic engine first, agents only where rules can't decide).

## Signals (3 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-msft-dont-let-llm-drive`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|
| `sig-ace-state-machine-reliability` | Microsoft's Ace models each lesson as a state machine (intro/teach/check/grade/advance/wrap); the harness validates model output and owns every transition, so lessons run start-to-finish where naive agents drift, loop, or quit early | harness-over-model | el-agent-state-machine, el-ace-voice-tutor | co-microsoft |
| `sig-model-proposes-harness-decides` | Framing: "the model proposes but the harness decides" — each step is a single-thing "neural contract"; reliability recast from a prompting problem ("prompt it harder, add more rules") to a control problem | harness-over-model | el-harness-engineering | co-microsoft |
| `sig-ace-haiku-over-opus` | By harnessing tightly, Ace meets its reliability bar on Claude Haiku 4.5 instead of Opus 4.7 — smaller model, saving cost/time/latency, "don't let it drive" | harness-over-model | el-claude-haiku-45 | co-microsoft, co-anthropic |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-reliability-is-control-not-prompting` | Agent reliability is a control-flow problem, not a prompting problem — more prompt rules don't fix mid-run drift/looping; moving state and decisions into a deterministic harness does | pat-harness-over-model | el-harness-engineering |
| `ins-model-talent-harness-director` | Division of labor: the model is "the talent" (great at delivering a line) and the harness is "the director" (owns where you are in the process); ask the model only to execute one single-step contract at a time | pat-harness-over-model | el-agent-state-machine |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-msft-dont-let-llm-drive`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-pull-control-flow-out-of-model` | Take control flow out of the model | Heuristic: if agent reliability is "a coin flip," stop prompting and pull the control flow out. Model the workflow as a state machine; hand the model one single-step contract per turn; validate its output in the harness; let the harness (not the model) decide the next state. Generalizes beyond voice — coding agents, ops runbooks, onboarding flows | el-agent-state-machine, el-harness-engineering |

## Dropped

- The generalization claim ("applies to coding agents, ops runbooks, onboarding flows") is captured inside `how-pull-control-flow-out-of-model` rather than as its own signal — it's advice, not a dated observation.
- No benchmark numbers in this talk (the latency figures live in the paired talk `ia-aie-msft-voice-no-frontier`), so signals here are qualitative-approach claims.

## Review notes

1. **New pattern** `pat-harness-over-model` is the batch's single new macro-thesis (the brief anticipated "zero or one"). Confirm the name/altitude; talks 2–4 all `FormsPattern` into it.
2. `co-microsoft` typed `bigtech`. Speakers' exact team/org not stated in captions — affiliation is company-level only.
3. Model version strings ("Opus 4.7", "Haiku 4.5") are as auto-transcribed; plausibly real given 2026-07 publish, but treat as caption-sourced.
