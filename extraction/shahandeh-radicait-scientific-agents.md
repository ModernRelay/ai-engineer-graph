# SPIKE extraction — "Autonomous Agents for Scientific Tasks" (Sina Shahandeh, Radicait) — FOR REVIEW

Source transcript: `transcripts/shahandeh-radicait-scientific-agents.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/XLEYtv3cMlw — AI Engineer World's Fair, published 2026-07-18.
`stagingTimestamp` for the artifact and all signals: 2026-07-18 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-shahandeh-scientific-agents` | Autonomous Agents for Scientific Tasks (Sina Shahandeh, Radicait — AI Engineer World's Fair) | youtube | https://youtu.be/XLEYtv3cMlw |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-sina-shahandeh`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-sina-shahandeh` | Sina Shahandeh (Radicait; runs autonomous coding-agent loops for medical-imaging ML research) | `AffiliatedWithCompany → co-radicait` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-radicait` | Radicait | developer | building "in-silico PET": ML image translation that generates synthetic PET scans from CT scans (lung-cancer workup) — appears here as a practitioner of agentic auto-research, not an agent vendor |

## Elements (2 new, 1 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-hierarchical-decomposition` | Hierarchical problem-decomposition scaffold | concept | harness | Prompt a coding agent to decompose the codebase/problem into an explicit linked hierarchy of component documents (data, architecture, loss, metrics, ops, peripheral scripts — browsable as an Obsidian graph, leaves pointing at real code), then ask for improvement hypotheses per component. Turns plateaued hill-climbing into a structured search that surfaces radical changes; an explicit-action analogue of chain-of-thought |
| `el-oracle-cli` | Oracle CLI | product | harness | Peter Steinberger's CLI that packages a codebase + data and ships them to a big reasoning model's API (speaker uses GPT-5.5 Pro) for hypothesis generation and implementation critique inside an agent loop |
| **[registry]** `el-autoresearch` | — | — | — | referenced as the origin frame: Karpathy's original auto-research repo (coding agent hill-climbs a model against a metric) — reuse, no new node |

Element edges: `el-hierarchical-decomposition` and `el-oracle-cli` `IdentifiedInArtifact → ia-aie-shahandeh-scientific-agents`; `el-hierarchical-decomposition` `EnablesPattern → pat-accelerated-research` **[registry]**.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-shahandeh-scientific-agents`, `SourcedFromSource → source-aie-yt` **[registry]**. Domain `harness` unless noted.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-agents-saturate-research-taste` | Practitioner report from a real auto-research deployment (Radicait, Codex loops): on open-ended long-horizon scientific tasks agents saturate — excellent at implementation and running experiments over data, but they "run out of ideas" (research taste), while top-1% humans keep climbing | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-radicait`; `OnElement → el-autoresearch` |
| `sig-hierarchy-unlocks-radical-hypotheses` | Plain "here's the codebase, optimize the metric" prompting only yields conservative tweaks (hyperparameters); after inducing a component hierarchy, the same reasoning LLM proposed the radical 2.5D→3D-convolution redesign the speaker previously had to inject by hand — scaffold structure, not model change, unlocked it | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-hierarchical-decomposition` |
| `sig-multimodel-science-loops-routine` | Applied science loops now routinely wire multiple specialist models into one agent loop: a multimodal model (Gemini) reviews registration/QC images as a skill, a large reasoning model (GPT-5.5 Pro via Oracle CLI) generates and critiques hypotheses adversarially/collaboratively each iteration | `FormsPattern → pat-accelerated-research` **[registry]** | `OnElement → el-oracle-cli` |
| `sig-scientific-observation-gap` | Limiting observation: no current multimodal LLM can reliably spot subtle scientific-image features (e.g. a lung nodule on CT) because none are trained on scientific imagery — the speaker names this the biggest bottleneck to a full "scientist in a data center"; a trained human must still close the observation loop | `FormsPattern → pat-accelerated-research` **[registry]** (limiting evidence — see review note 2) | `RelevantCompany → co-radicait` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-hypothesis-is-the-bottleneck` | In agentic science, implementation is "already quite solved" (especially in simulatable environments) and memory/learning is an organization problem; the true bottleneck is hypothesis generation — so the leverage point is scaffolding that makes a reasoning model enumerate and attack every component of the problem, i.e. a structured way to scale test-time compute on the problem | `HighlightsPattern → pat-model-not-bottleneck`, `HighlightsPattern → pat-accelerated-research` **[registry]** | `ReliesOnElement → el-hierarchical-decomposition` |
| `ins-scaffolds-are-transitional-tricks` | The hierarchy scaffold is the same kind of trick chain-of-thought was on GPT-4-era models: a harness compensating for missing post-training. As models get better at compartmentalizing problems natively, these tricks should be needed less and less — harness value at this layer is expected to erode | `HighlightsPattern → pat-harness-over-model` **[registry]** (as a nuance/limit on the thesis) | `ReliesOnElement → el-hierarchical-decomposition` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-shahandeh-scientific-agents`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-hierarchy-scaffold-loop` | Escape auto-research plateaus with an explicit hierarchy | Have the coding agent generate a linked hierarchy of component docs over the codebase (one prompt; keep docs simple, leaves point at actual code); then ask for improvement hypotheses per component rather than globally; review the resulting plan adversarially or collaboratively with a second agent/model before implementing; run the hypothesize→implement→measure loop over the hierarchy | `ReferencesElement → el-hierarchical-decomposition` |
| `how-equip-loop-with-reviewer-models` | Equip the loop with specialist reviewer skills | Where metrics are qualitative (does this registration/mask look right?), build a skill that calls a multimodal model to review generated images inside the loop; for hypothesis generation and implementation critique, ship code+data to a large reasoning model (e.g. via Oracle CLI) and close each iteration with "this is what we implemented, this is the outcome — does it make sense, what next?" | `ReferencesElement → el-oracle-cli` |

## Dropped

- The in-silico PET / GAN encoder-decoder detail — product context, folded into `co-radicait` brief.
- Image registration as an Element — it's the domain example, not a reusable AI element; kept as prose in `sig-multimodel-science-loops-routine`.
- "Gemini" / "GPT-5.5 Pro" / "Codex" as Elements — named model/tool mentions without load-bearing standalone content here; kept in signal prose.

## Review notes

1. Auto-caption garbles resolved against the official title: "Sina Shahande"→Shahandeh, "Radicate"→Radicait, "codeex"→Codex, "carpat"→Karpathy, "Peter Spinberger"→Peter Steinberger (Oracle CLI), "545"/"GP 5.5"→GPT-5.5 (Pro). "GP 4.0" read as GPT-4o-era base models. All quotes paraphrased.
2. `sig-scientific-observation-gap` cuts against a strong reading of `pat-accelerated-research`; I kept `FormsPattern` (it refines the thesis by locating the remaining bottleneck) — flip to `ContradictsPattern` if your bar for "forms" is supportive-only.
3. `el-oracle-cli` is a small third-party tool; coined because the multi-model-loop KnowHow leans on it by name. Downgrade to prose if too thin.
4. `el-hierarchical-decomposition` overlaps conceptually with batch2 `el-progressive-disclosure` / `el-harness-engineering` but is a distinct mechanism (agent-generated component hierarchy for hypothesis search); kept separate.
