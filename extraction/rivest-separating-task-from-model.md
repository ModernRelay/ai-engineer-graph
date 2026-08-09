# SPIKE extraction — "The Unreasonable Effectiveness of Separating the Task from the Model" (Maxime Rivest & Isaac Miller, DSPy) — FOR REVIEW

Source transcript: `transcripts/rivest-separating-task-from-model.txt` (auto-captions — quotes are paraphrases, not verbatim; "Maxim Rest" = Maxime Rivest; "DSPI/DSP/Aspire/DSpay" = DSPy).
Video: https://youtu.be/GgLQ02aO-hs — AI Engineer World's Fair, published 2026-07-23.
`stagingTimestamp` for the artifact and all signals: 2026-07-23 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
NOTE: the listing credits Rivest, but the stage intro is "Maxime Rivest and Isaac Miller" and Miller delivers the second half — both are contributors.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-rivest-task-from-model` | The Unreasonable Effectiveness of Separating the Task from the Model (Maxime Rivest & Isaac Miller, DSPy — AI Engineer World's Fair) | youtube | https://youtu.be/GgLQ02aO-hs |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-maxime-rivest`; `ContributedByExpert → exp-isaac-miller`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-maxime-rivest` | Maxime Rivest (DSPy community; AI programming educator, farm-invoice-to-taxes origin story) | — (see note 2) |
| `exp-isaac-miller` | Isaac Miller (DSPy community; presented DSPy 4 roadmap — Flex, qualitative learning) | — (see note 2) |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-shopify` | Shopify | developer | appears as DSPy enterprise case study (550× cost reduction), not an AI vendor; enum has no "e-commerce" — `developer` chosen |

Registry reuses (edges only): `co-uc-berkeley` (batch 10 — GEPA attributed "out of Berkeley" in-talk).

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-task-model-separation` | Task–model separation (AI functions) | concept | harness | Treat a repeated AI task as a function: fixed name + input/output contract, everything inside — prompt, model, chain-of-thought, agent loop, tools, harness — is a swappable implementation detail. Full task specification takes three languages: natural-language instructions (what should happen), code constraints (what must happen — enforced even under AGI, e.g., rerun with reasoning if extraction fails, escalate to human below zero), and examples/evals (what good looks like — the latent long tail you learn like a mentee, not a rulebook). A hard boundary makes AI programs reusable, composable, testable, distributable — and automatically optimizable |
| `el-gepa` | GEPA prompt optimizer ⚠ | technology | harness | Reflective prompt optimizer "out of Berkeley" used on DSPy metrics + programs; the instruction-optimization rung of DSPy's ladder. ⚠ captions render it "Japa"/"Jeepa" — name reconstructed; verify before public-facing use |
| `el-dspy-flex` | DSPy Flex | technology | harness | New DSPy 4 module kind: for any function contract, *learn a custom harness over time* to solve it — implementation fully delegated as long as it satisfies the specs/code/evals triple; "you don't care about the implementation as long as it solves your business problem" |
| `el-qualitative-learning` | Qualitative learning | concept | harness | DSPy 4 research direction: instead of hand-building evals (lossy "good/bad" labels, proxy hills), models interpret whatever textual feedback the environment produces — production traces, user actions, product analytics, questions back to the developer — and convert it into evals and a hill that is iteratively refined; "use reality to inform our evals automatically" |

Element edges: all four `IdentifiedInArtifact → ia-aie-rivest-task-from-model`; `el-gepa` `DevelopedByCompany → co-uc-berkeley` **[registry]** (⚠ per-talk attribution only); `el-dspy-flex` and `el-qualitative-learning` `UsesElement → el-dspy` **[registry]**; `el-dspy` **[registry]** `IdentifiedInArtifact → ia-aie-rivest-task-from-model`; `el-task-model-separation` `EnablesPattern → pat-harness-over-model` (fixed contract is what lets the scaffold/implementation evolve freely around a swappable model).

Registry element reuses (edges only): `el-dspy` (batch 9), `el-recursive-language-models` (batch 5 — Alex Zhang's MIT paper, adoptable in DSPy as a one-line module swap).

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-rivest-task-from-model`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | pattern edges | other edges |
|---|---|---|---|
| `sig-dspy-fixed-contract-agility` | DSPy thesis restated for the harness era: with new models every other week and a constant stream of techniques (agents, tools, loop engineering, RLMs), fix the task's input/output contract and treat all of it as internals — a new technique becomes a one-line swap with the signature unchanged, and nothing outside the boundary changes. The model is explicitly configured *independently* of the task signature | `FormsPattern → pat-harness-over-model` | `OnElement → el-dspy` **[registry]**, `el-task-model-separation`, `el-recursive-language-models` **[registry]** |
| `sig-shopify-550x-cost-drop` | Enterprise evidence: with the contract and evals held fixed, Shopify swapped an expensive model for a cheap one for a 550× cost reduction while continuing to iterate business logic inside the boundary — flexible implementation lets you "use the bitter lesson to search over solutions" and scale to data sizes impossible under the expensive implementation | `FormsPattern → pat-model-not-bottleneck` | `RelevantCompany → co-shopify`; `OnElement → el-dspy` **[registry]** |
| `sig-dspy-optimization-ladder` | DSPy's automated-optimization ladder has tracked model capability since before ChatGPT: few-shot example search (models too weak for more) → automatic instruction optimization (GEPA) → now, in DSPy 4, learned harnesses (Flex) and community techniques (RLMs, Better Together, multi-module GEPA) — progressively "liberating you from the implementation details and delegating that away" | `FormsPattern → pat-harness-over-model` (see note 3 — also prime `pat-adaptive-harness` candidate evidence) | `OnElement → el-gepa`, `el-dspy-flex`, `el-dspy` **[registry]** |
| `sig-qualitative-learning-evals` | Building evals is the hard problem of AI engineering (defining good is hard, labels lose detail, every dataset is a proxy for reality) — and models are now good enough to interpret textual feedback from the environment and convert it into evals the system refines and climbs iteratively; DSPy 4's qualitative learning aims to shrink the human assistance needed | `FormsPattern → pat-verification-gap` | `OnElement → el-qualitative-learning` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-agi-still-needs-last-mile` | Even AGI won't know your tasks, context, or relationships — "if you asked Einstein to help with your emails, he'd ask what's an email"; intelligence is different from being all-knowing, so last-mile learning (task specs, context acquisition, your evals) remains the durable layer no model release dissolves | `HighlightsPattern → pat-model-not-bottleneck` | `ReliesOnElement → el-task-model-separation` |
| `ins-three-languages-fully-specify` | A task is fully specified only with all three languages — instructions, code constraints, examples — and *full* specification is the precondition for delegating implementation to optimizers; under-specified tasks can't be optimized against, no matter the model ("learn the board game from examples only and you'll have a long night") | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-task-model-separation` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-rivest-task-from-model`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-hold-implementations-accountable` | Adopt new AI techniques through a fixed contract, data-driven | For every hyped technique ask "does it help *my* task?" and answer empirically: define the problem as specs + code + evals; keep the signature fixed so trying a technique (RLM, GEPA, new model, agent loop) is a one-line change; hold prompts, models, and code accountable to the metric; a flexible implementation unlocks the whole ecosystem's techniques as drop-ins | `ReferencesElement → el-task-model-separation`, `el-dspy` **[registry]** |

## Dropped

- Rivest's personal AI programs (invoice tax extraction, clipboard grammar/clarity rewriters, inbox draft-reply) — thesis illustrations, folded into element/signal prose.
- Alex Zhang (MIT PhD student, RLM paper author) — name-check; `el-recursive-language-models` already carries the concept.
- "Better Together" and "multi-module GEPA" as separate elements — one-line technique mentions, prose inside `sig-dspy-optimization-ladder`.
- Two additional unnamed enterprise case studies ("three awesome case studies") — no extractable facts.
- Databricks/DSPy institutional affiliations — never stated in-talk; nothing coined.

## Review notes

1. **The DSPy angle cuts opposite to Horthy's talk in the same batch:** here the fixed contract + evolving scaffold is the whole point (`FormsPattern → pat-harness-over-model` ×2), while Horthy's file carries three ContradictsPattern counter-edges. Good adversarial pairing for the pattern.
2. No Company node exists for DSPy (open-source project; represented as `el-dspy`), so both experts have **no** `AffiliatedWithCompany` edge — precedent: `exp-sachin-gupta` (batch 3), `exp-simon-willison` (batch 5). If you'd rather have an org node, a `SourceEntity`/Company for the DSPy project would be a registry-level decision.
3. **`pat-adaptive-harness` (uncoined candidate) — DSPy Flex is a clean new data point:** an optimizer that *learns the harness itself* per function, plus qualitative learning evolving the evals. Adds to ten Teije/Chandegra (batch 7) + Tornow/RELAI/Mutagent (batch 8) + Graziano/Weitekamp/Pankaj (batch 9). Flagged only; `sig-dspy-optimization-ladder` is the rehome candidate if coined.
4. Caption garbles: "Japa"/"Jeepa" = GEPA (flagged on the element); "Chat GPD" = ChatGPT; "Alex Zang" = Alex Zhang; and — load-bearing — "keep the same **emails**" / "evolving your **emails** over time" are almost certainly "**evals**" (both read as eval-context; extracted as evals with this flag). "Sol define them" = "so we define them".
5. The 550× Shopify number is the talk's headline stat, unverified externally; kept as testimony inside the signal.
