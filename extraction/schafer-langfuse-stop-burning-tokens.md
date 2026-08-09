# SPIKE extraction — "Stop Burning Tokens: Why Self-Improvement Needs Domain Expertise First" (Annabell Schäfer, Langfuse) — FOR REVIEW

Source transcript: `transcripts/schafer-langfuse-stop-burning-tokens.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/eAXxdtNlK04 — AI Engineer World's Fair, published 2026-07-18.
`stagingTimestamp` for the artifact and all signals: 2026-07-18 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-schafer-stop-burning-tokens` | Stop Burning Tokens: Why Self-Improvement Needs Domain Expertise First (Annabell Schäfer, Langfuse — AI Engineer World's Fair) | youtube | https://youtu.be/eAXxdtNlK04 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-annabell-schafer`.

## Experts (1 new, 1 registry)

| slug | name | edges |
|---|---|---|
| `exp-annabell-schafer` | Annabell Schäfer (growth engineer, Langfuse) | `AffiliatedWithCompany → co-langfuse` |
| `exp-karpathy` **[registry]** | Andrej Karpathy | reused: his auto-research/auto-improvement topic anchors the loops zeitgeist signal |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-langfuse` | Langfuse | developer | self-described largest open-source observability and evaluation platform for AI systems |

## Elements (1 new, 1 registry)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-target-function` | Target function (for self-improving loops) | concept | harness | The measurable objective a self-improvement loop optimizes against. Coding got loops first because it had one for free ("does the code compile"); most domains (healthcare, compliance, chatbots) do not, and any target you give an agent is inherently incomplete. Loop performance is bounded by target-function signal quality: binary right/wrong checks are high-signal; generic 0–1 scale evaluators (correctness, helpfulness, hallucination) are low-signal and inconsistent across runs |
| `el-autoresearch` **[registry]** | Auto-research | — | — | reused: "the whole Karpathy auto-research and auto-improvement topic blew up earlier this year" — anchor of the loops zeitgeist |

Element edges: `el-target-function` `IdentifiedInArtifact → ia-aie-schafer-stop-burning-tokens`; `el-target-function` `EnablesPattern → pat-accelerated-research` (a good target function is what makes self-improvement loops work); `el-target-function` `ExemplifiesPattern → pat-verification-gap` (the scarce half of the loop is verification signal, not generation).

## Signals (3 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-schafer-stop-burning-tokens`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-loops-zeitgeist-june-2026` | As of June 2026 "the whole internet is about loops": Boris [Cherny — garbled, see notes] says he no longer writes prompts, only loops; Peter Steinberger urges designing loops, not prompting agents; Karpathy's auto-research/auto-improvement discourse blew up earlier in the year — but all of it comes from the developer/coding perspective, where a free target function (code compiles) exists | `FormsPattern → pat-accelerated-research`; `OnElement → el-autoresearch` | — |
| `sig-langfuse-self-optimization-experiment` | Langfuse's minimal self-optimization loop — GPT-5-nano classifier prompt over arXiv papers (200 fit / 100 validate / 300 test), optimized by Claude Code with a frontier Claude model proposing prompt updates from error-cluster analysis — gained +15pts (68%→83%, plateauing ~80%; 80.2% on untouched test data), with a +10pt jump on the very first iteration off one clear binary error signal; the optimizer chose rules + few-shot examples over label descriptions | `FormsPattern → pat-accelerated-research` | `RelevantCompany → co-langfuse` |
| `sig-generic-evaluators-low-signal` | Langfuse observes across its user base: teams that continuously improve and ship with confidence are those investing in encoded target functions and domain-specific binary evaluators; generic scale-based scores (correctness 0–1, helpfulness 1–5) with undefined anchors are low-signal, inconsistent across runs (the judge itself is non-deterministic), and fail to drive auto-improvement | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-langfuse` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-signal-quality-bounds-self-improvement` | Self-improvement is bounded by target-function signal quality, not optimizer intelligence: the frontier optimizer extracted almost all of its gain (+10 of +15pts) in one pass from a clean binary right/wrong signal over enough volume (200 items, 10 labels each covered enough times). Outside code-compiles domains the scarce asset is domain expertise encoded into high-signal binary checks — hence "stop burning tokens" on loops driven by vague scores | `HighlightsPattern → pat-verification-gap`, `HighlightsPattern → pat-model-not-bottleneck` | `ReliesOnElement → el-target-function` |
| `ins-no-perfect-target-function` | Even the cleanest real-world target function leaks subjectivity: arXiv authors have creative freedom in choosing primary labels, capping the loop's accuracy near 80% — and any target given to an agent is always incomplete (the goal you specify is not quite the destination you want). Every domain therefore ultimately needs human/domain-expert calibration and periodic re-grounding, not a set-and-forget objective | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-target-function` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-schafer-stop-burning-tokens`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-high-signal-eval-design` | Encode domain expertise as binary, high-signal evaluators | Replace scale scores with domain-specific yes/no checks: is the answer grounded in the retrieved knowledge-base snippet; is the brand voice/name correct (e.g. company name not translated); which of N known failure modes occurred. Build them with domain experts: have them create concrete expected-output examples, review sample runs together, ask "why this here and the other way there" to surface implicit knowledge; review production data as a human (not only via coding agents) because scope and failure modes shift over time | `ReferencesElement → el-target-function` |
| `how-self-improvement-loop-guardrails` | Run improvement loops with ML-style validation and escape hatches | Split data fit/validate/test and never show the loop the test set; run baseline first, do error-cluster analysis on fit, propose an update per biggest error category, accept only if it also improves on validation (anti-overfit); set explicit stopping criteria (e.g. 15 runs or 92% accuracy) and give the system an escape hatch instead of letting it grind against a wall for hours burning tokens; ensure enough volume per label/category for the signal to be readable | `ReferencesElement → el-target-function` |

## Dropped

- Peter Steinberger — one-line zeitgeist quote; prose inside `sig-loops-zeitgeist-june-2026`, no Expert node.
- "Boris" — see Review notes; prose only.
- GPT-5-nano / "Claude Opus 4.8" as Elements — model mentions are load-bearing for the experiment narrative but kept as prose (and the Opus version number is garbled, see notes).
- GPT-5 prompting guide ("GPT54 prompting guide") — context document given to the optimizer; prose.
- OpenAI/Anthropic company edges — models named but neither company is the subject of an observation; no `RelevantCompany` edges.

## Review notes

1. Name garbles: "Lenfuse" → **Langfuse**, "Annabelle" → **Annabell Schäfer** (official listing). "Boris Journey" is almost certainly **Boris Cherny** (Claude Code creator, known for the loops-not-prompts line) but left as prose with this flag rather than coining an Expert on a garbled name. "cloud us 4.8"/"clude oppus 4.8" → a Claude Opus 4.x model driving Claude Code; registry has `el-claude-opus-47` — if "4.8" is a mis-hearing of 4.7 this could link there, but it may be a genuinely newer release; left unresolved. "GPD5 for nano" → GPT-5-nano (corroborated by the ZenML talk's GPT-5 Nano mention).
2. Pattern call: no new pattern coined. The talk's thesis ("self-improvement needs domain expertise first") is read as the intersection of `pat-verification-gap` (verification signal is the scarce half) and `pat-accelerated-research` (self-improving loops as the industry direction) — evidence didn't demand a new node.
3. `sig-langfuse-self-optimization-experiment` → `pat-accelerated-research` could alternatively form `pat-model-not-bottleneck` (cheap nano model + good signal beat expensive models + vague signal); the model-not-bottleneck reading is carried on `ins-signal-quality-bounds-self-improvement` instead.
4. Experiment numbers (68/83/80.2%, 200/100/300 splits, 15-run cap, 92% target) are read off caption narration of slides; plausible-consistent but paraphrase-grade.
