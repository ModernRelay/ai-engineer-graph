# SPIKE extraction — "The Future of Evals: From LLM as a Judge to Agent as a Judge" (Aparna Dhinakaran, Arize) — FOR REVIEW

Source transcript: `transcripts/dhinakaran-arize-agent-as-judge.txt` (auto-captions — quotes are paraphrases, not verbatim). Short talk (~1k words, evals-track opener) — 3 signals by design.
Video: https://youtu.be/q2JrUKBMf0w — AI Engineer World's Fair (evals track), published 2026-07-24.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-07-24 (publish date).
Entities marked **[registry]** already exist — edges link to them, no new node. Entities marked **[batch: lopatecki]** are defined in `lopatecki-arize-signal-to-pr.md` (same batch, same company) — referenced here, not redefined.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-dhinakaran-agent-as-judge` | The Future of Evals: From LLM as a Judge to Agent as a Judge (Aparna Dhinakaran, Arize — AI Engineer World's Fair) | youtube | https://youtu.be/q2JrUKBMf0w |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-aparna-dhinakaran`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-aparna-dhinakaran` | Aparna Dhinakaran (co-founder, Arize; hosts the World's Fair evals track) | `AffiliatedWithCompany → co-arize` **[registry]** |

## Companies (0 new)

| slug | name | status |
|---|---|---|
| `co-arize` | Arize | **[registry, batch 8]** — reused; speaker's company, the eval-volume statistics and the agent-as-a-judge release both belong to it |

## Elements (1 new, 2 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-as-a-judge` | Agent as a judge | concept | harness | Adaptive, dynamic evaluation of an agent *by* an agent: instead of scoring one output against a fixed rubric with fixed scores, a long-running evaluator agent reads incoming traces, roams whole trajectories, and discovers failure classes nobody enumerated in advance — looping on the same tool call repeatedly, an inefficient trajectory, not recognising a task is done, dropped context — then acts on them (opens a PR with a fix). Motivated by trajectory variance: when every user interaction produces a different path and a freshly generated UI, there is no stable rubric to score against. Explicitly positioned as a *third tier* added to deterministic evals and LLM-as-judge, not a replacement for either |
| `el-arize-signal` **[batch: lopatecki]** | Arize Signal | — | — | reused — the shipped implementation of agent-as-a-judge: a long-running agent over trace streams that discovers issue patterns and puts up a PR; defined in `lopatecki-arize-signal-to-pr.md` |
| `el-arize-alex` **[batch: lopatecki]** | Alex (Arize in-product agent) | — | — | reused — the dogfood source of the failure taxonomy: as each frontier-lab capability (longer memory, dynamic UI generation, search over large trace volumes) was added to Alex, a matching failure mode appeared (forgets context, doesn't know when it's done, gets stuck in loops) |

Element edges: `el-agent-as-a-judge` `IdentifiedInArtifact → ia-aie-dhinakaran-agent-as-judge`; `el-arize-signal` and `el-arize-alex` `IdentifiedInArtifact → ia-aie-dhinakaran-agent-as-judge` (second artifact each); `el-arize-signal` `UsesElement → el-agent-as-a-judge`; `el-agent-as-a-judge` `EnablesPattern → pat-verification-gap` **[registry]**; `el-arize-alex` `EnablesElement → el-agent-as-a-judge` (dogfood → technique lineage).

## Signals (3 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-dhinakaran-agent-as-judge`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-arize` **[registry]**.

| slug | name / brief | pattern edge | OnElement |
|---|---|---|---|
| `sig-arize-eval-volume-2026` | Vendor-side volume numbers for production evals (mid-2026): Arize runs **over 100 million evals per month**; the average team runs about **12 distinct eval jobs**, and top teams run **over 3,800 different evaluators**. Framing: evals moved from "the new skill every PM and AI engineer has to learn" to "the thing every serious AI team is betting on", with the industry consensus cited via the CPOs of Anthropic and OpenAI and Garry Tan's "evals are everything you need" | `FormsPattern → pat-verification-gap` **[registry]** | — |
| `sig-eval-target-outran-first-gen-evals` | The thing being evaluated changed underneath the evals: 2023 was answering a prompt; 2024 added tool calls, reasoning, and deep research; now teams run loops on real-world data with sub-agents on long-horizon tasks. Each jump was not just harder but a *different kind of problem*, and the failure modes changed with it — so classical LLM-as-judge evals with fixed rubrics "just weren't enough to catch all the types of failures". Sharpest instance: an agent that generates a new UI on every user interaction has a fundamentally different trajectory each run, leaving nothing fixed to score | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-arize-alex` **[batch: lopatecki]** |
| `sig-agent-as-judge-released` | Arize releases agent-as-a-judge, productized as Signal: a long-running agent that reads traces sent in, discovers patterns of issues that a deterministic rubric "would never be able to" express (a tool called repeatedly in a loop, an inefficient trajectory), and — because it already holds the analysis — opens a PR with the fix. Stated maturity read: most teams today run deterministic evals plus LLM-as-judge; the future of evals is running all three tiers | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-agent-as-a-judge`, `el-arize-signal` **[batch: lopatecki]** |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-eval-tiers-accrete` | Eval methods accrete rather than replace: deterministic evals, LLM-as-judge, and agent-as-judge are different tools for different problem shapes, and the correct selector is trajectory variance. Fixed rubrics work where the flow is deterministic and failures are enumerable; adaptive agentic analysis is required where every run takes a different path and the interesting failures (loops, wasted tool calls, no done-detection) are only visible across the whole trajectory. The corollary is that evals belong on live production traces — that is where the data for continual-learning loops comes from — not only in an offline suite | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-agent-as-a-judge` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-dhinakaran-agent-as-judge`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-pick-eval-tier-by-trajectory` | Choose the eval tier by how variable the trajectory is | Keep all three tiers and route by problem shape: deterministic checks where the output is structurally checkable; LLM-as-judge with a fixed rubric and fixed scores where the flow is stable and the failure set is known in advance; agent-as-judge — a long-running agent reading the trace stream — where each interaction produces a different trajectory (dynamically generated UIs, sub-agents, long-horizon loops) and the failure modes are not enumerable ahead of time. Run evals on live production traces, not only offline: that is what shows what's working, catches the failures, and produces the data that fuels continual-learning loops. Expect the discovered failures to be ones you would not have written a rubric for (same tool called repeatedly, inefficient trajectory, no done-detection), and wire the discovery straight through to a fix | `ReferencesElement → el-agent-as-a-judge`, `el-arize-signal` **[batch: lopatecki]** |

## Dropped

- **Anthropic / OpenAI CPOs, Garry Tan quote** — name-dropped as consensus evidence, one clause each; carried as prose in `sig-arize-eval-volume-2026`, no `RelevantCompany` edges and no reuse of `exp-garry-tan` **[registry, batch 3]** (he is quoted, not a contributor to this artifact).
- **Evals-track logistics / booth / World Cup viewing party** — conference housekeeping, no content.
- **Offline-vs-online eval aside** — one sentence ("they each have their own place"); folded into `ins-eval-tiers-accrete`.

## Review notes

1. **Thin talk by design.** ~1k words, an evals-track opener with a product announcement attached. Three signals, one insight, one knowhow — matching the batch brief. There are no external dated facts beyond the Arize-side volume statistics, which are vendor-reported and should be attributed as such if surfaced.
2. **Registry adjacency deliberately NOT edged:** `el-judge-as-classifier` **[registry, batch 3, Lyft]**. Dhinakaran's "LLM as a judge" is the generic fixed-rubric/fixed-score foil for her contrast, without the classifier framing (hand-labels, train/dev/test, precision/recall) that the registry element carries — same precedent as `schmid-deepmind-skills-evals.md`. If central prefers, add `el-agent-as-a-judge` `UsesElement → el-judge-as-classifier` at seeding to make the tier ladder explicit. Also considered and not edged: `el-eval-driven-development` **[registry, batch 8]** (development-loop gating, not a judging technique) and `el-jury-judge-workflow` **[registry, batch 6]** (multi-judge deliberation, a different axis).
3. **Cross-batch corroboration for `el-agent-as-a-judge`.** Coined here, and independently referenced in the same batch by `feyzkhanov-snorkel-traces-to-simulations.md` ("LLM as a judge, or even harness as a judge, or agent as a judge") — two vendors, same term, same week. That file's `how-verify-across-world-trace-artifacts` carries a `ReferencesElement` edge to this element.
4. **Pattern candidates: none new.** Every signal is straight `pat-verification-gap` **[registry]** material — this is one of the purest statements of that thesis in the corpus (the evaluated object outran its evaluators). Weak resonance only with `pat-adaptive-software`/`pat-adaptive-harness` (the judge writes the fix). Nothing coinable.
5. **Shared entities** — `el-arize-signal`, `el-arize-alex`, `co-arize`: defined elsewhere, referenced here. See review note 1 in `lopatecki-arize-signal-to-pr.md` for the full contract.
