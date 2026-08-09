# SPIKE extraction — "Harness Engineering is not Enough: Why Software Factories Fail" (Dex Horthy, HumanLayer) — FOR REVIEW

Source transcript: `transcripts/horthy-humanlayer-software-factories.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/Ib5GBkD555M — AI Engineer World's Fair, published 2026-07-23.
`stagingTimestamp` for the artifact and all signals: 2026-07-23 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
This is Horthy's SECOND talk in the corpus (first: `ia-aie-horthy-loops-debate`, batch 3) — `exp-dex-horthy` and `co-humanlayer` are strict reuses.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-horthy-software-factories` | Harness Engineering is not Enough: Why Software Factories Fail (Dex Horthy, HumanLayer — AI Engineer World's Fair) | youtube | https://youtu.be/Ib5GBkD555M |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-dex-horthy` **[registry]**.

## Experts (0 new)

- `exp-dex-horthy` **[registry]** (batch 3; `AffiliatedWithCompany → co-humanlayer` already exists — no new edge needed).

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-cognition` | Cognition (Devin; builds the Frontier Code multi-PR benchmark) | developer | first appearance in corpus, coined here because `el-frontier-code` needs a developer edge |

Registry reuses (edges only, no new nodes): `co-humanlayer`, `co-faros-ai`, `co-abundant-ai`, `co-anthropic`, `co-openai`.

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-lights-off-software-factory` | Lights-off software factory | concept | harness | Software factory run with no human code reading: code review is dropped entirely, investment shifts to testing/monitoring/rollout, and the human job reduces to queueing work. Term "software factory" dates to a 1968 NATO conference; "lights off" coined by Dan Shapiro (StrongDM built one). Horthy's talk is an argument that this configuration fails |
| `el-swe-bench` | SWE-bench (Multilingual) | technology | training | Canonical coding-agent RL/eval benchmark family: ~15-minute tasks from OSS repos (Redis, jq, Django), binary 0/1 reward — did you fix the issue without breaking anything else; agent test-file edits reverted, hidden golden test patch applied. Critiqued here: the reward has no channel to penalize design erosion |
| `el-frontier-code` | Frontier Code (Cognition) | technology | training | Cognition's maintainability-oriented benchmark: multi-PR tasks; penalizes model-written tests that don't fail on pre-patch code; judge model scores adherence to code-quality rules |
| `el-deepsuite` | DeepSuite (DataCurve) ⚠ | technology | training | Large coding tasks on OSS repos that are guaranteed out-of-training-set because they were never actually built in the real world. ⚠ both product and company name from garbled captions ("deep suite from data curve") — verify before seeding |
| `el-humanlayer` | HumanLayer platform | product | harness | AI IDE and collaboration platform — "building blocks for your software factory": a Figma-like collaborative workspace for Claude Code / Codex-style agents that walks teams through product review → architecture → program design → vertical-slice workflows; software-quality verifiers announced as upcoming. Free for small teams |

Element edges: all five `IdentifiedInArtifact → ia-aie-horthy-software-factories`; `el-frontier-code` `DevelopedByCompany → co-cognition`; `el-humanlayer` `DevelopedByCompany → co-humanlayer` **[registry]**; `el-swe-marathon` **[registry]** `IdentifiedInArtifact → ia-aie-horthy-software-factories` (cited as the 400-hour-task future of maintainability evals).

Registry element reuses (edges only): `el-swe-marathon`, `el-ralph-loop`, `el-claude-code`.

## Signals (6 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-horthy-software-factories`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | pattern edges | other edges |
|---|---|---|---|
| `sig-ai-coding-quality-metrics-down` | Faros AI report since mass AI-coding adoption (Jan–Feb 2026): PR review quality way down, more and longer comments, "tons of PRs merged without any review at all"; incidents way up, bugs per developer way up; companies that shouldn't have outages are having coding-agent-caused outages (Mario's plea at AI Engineer Europe) | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-faros-ai` |
| `sig-lights-off-model-training-limit` | Horthy's thesis: software factories fail on a model-training shortcoming, not a scale/skill issue — models cannot maintain and improve codebase quality over time without human steering, and no amount of harness engineering or loops-maxing fixes that; agents start struggling in codebases after just 3–6 months at AI shipping pace | `ContradictsPattern → pat-harness-over-model`; `ContradictsPattern → pat-model-not-bottleneck` | `OnElement → el-lights-off-software-factory`; `OnElement → el-ralph-loop` **[registry]** ("loops maxing" = the Ralph-loop discourse) |
| `sig-humanlayer-lights-off-postmortem` | HumanLayer went full lights-off in July 2025: within months hit an issue the agent couldn't solve with any prompting; had to dig into a codebase nobody had read for three months while the site was down and users were angry — reading "slop code that you let slip into your system" | `ContradictsPattern → pat-harness-over-model` | `RelevantCompany → co-humanlayer` **[registry]**; `OnElement → el-lights-off-software-factory` |
| `sig-rl-reward-blind-to-maintainability` | Mechanism: coding-agent RL rewards binary test-pass (SWE-bench shape); there is no way to penalize poor program design — hence unneeded try/catch, casts-to-anything, tests commented out to pass. Verifying maintainability is orders of magnitude harder than "tests pass" because bad architecture's cost function is measured in months–years, and the reward signal can't propagate back across that gap | `FormsPattern → pat-verification-gap` | `OnElement → el-swe-bench` |
| `sig-claude-code-rl-in-harness-moat` | Why Claude Code went from nothing to $4B (now ~$9B) revenue in under a year despite prior CLI agents (Aider, Codebuff) having identical tools: first time a lab RL-trained the model against the harness it ships in; OpenAI team's own November talk: a harness builder who doesn't own the model weights is always at a disadvantage vs. someone who owns both | `ContradictsPattern → pat-harness-over-model` (the moat is model-in-harness training, not the scaffolding) | `OnElement → el-claude-code` **[registry]**; `RelevantCompany → co-anthropic` **[registry]**; `RelevantCompany → co-openai` **[registry]** |
| `sig-maintainability-benchmarks-wave` | A wave of maintainability-oriented benchmarks is emerging: SWE Marathon (Abundant AI — ~400-hour clone-all-of-Excel tasks, sophisticated reward channels), DeepSuite (DataCurve — large tasks on never-built OSS repos), Frontier Code (Cognition — multi-PR, pre-patch-failing-test penalty, code-quality judge model); but judge models can only go so far — "if the model knew what good code looks like, it would write it in the first place" | `FormsPattern → pat-verification-gap` | `OnElement → el-swe-marathon` **[registry]**, `el-deepsuite`, `el-frontier-code`; `RelevantCompany → co-abundant-ai` **[registry]**, `co-cognition` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-stuck-reading-code` | For now we're stuck reading the code: review agents and more tokens raise the floor but are constrained by what RL can teach; the escape is front-loaded alignment — 30 minutes of pre-planning saves hours of review and keeps reading every line feasible while still moving fast | `HighlightsPattern → pat-verification-gap`; `HighlightsPattern → pat-value-of-judgement` | `ReliesOnElement → el-humanlayer` |
| `ins-judge-models-self-limiting` | Model-judged code quality is self-limiting: a model that could reliably recognize good code would already write it; so quality verification cannot be fully delegated back to the same class of model being verified | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-frontier-code` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-horthy-software-factories`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-plan-before-delegating` | Turn the lights back on: plan up front, read every line | Keep human code review; small stuff still goes straight to the agent. For the rest run a four-stage pre-alignment: (1) product review — problem, desired behavior, mockups; (2) system architecture — component contracts, data models, constraints; (3) program design — types, method signatures, layout, call graphs (underemphasized; don't assume the model "can cook" from architecture alone); (4) vertical slices — implementation order, multi-repo coordination, checks along the way. Diagnosis: you don't have too many PRs, you have too many bad PRs — a well-aligned PR is a joy to review; even 20% rework is an emotional and intellectual burden on both sides | `ReferencesElement → el-humanlayer` |

## Dropped

- StrongDM / Dan Shapiro — kept as prose inside `el-lights-off-software-factory`; not coined as company/expert (single exemplar mention).
- Addy Osmani's vibe-coding-vs-brownfield quote — `exp-addy-osmani` **[registry]** exists but is quoted, not a contributor; prose only.
- Calvin French-Owen (ex-Codex MTS, cited slides), Dylan Mulroy (Cloudflare, call-graph planning), John Ousterhout ("John Austerhood" garble, *A Philosophy of Software Design*), Martin Fowler (shotgun surgery) — name-checks, prose only.
- Aider ("ADER") and Codebuff as pre-Claude-Code CLI agents — prose inside `sig-claude-code-rl-in-harness-moat`.
- DataCurve as a Company node — held back pending name verification (see `el-deepsuite` flag).

## Review notes

1. This talk is deliberately contrarian to `pat-harness-over-model` — three of six signals carry `ContradictsPattern` edges (plus one against `pat-model-not-bottleneck`). With batch-6/7's counter-edges, the harness thesis now has 6+ counter-signals; that contest is healthy, but check you're happy with three from a single talk. Downgrade option: drop the edge on `sig-claude-code-rl-in-harness-moat` (it's the most interpretive of the three).
2. `pat-benchmark-trust-crisis` (uncoined candidate) gets more evidence here: binary rewards are gameable (models comment out tests), and judge-model quality scoring is argued self-limiting. Noted only — no edges, per the no-coin instruction.
3. Caption garbles: "cloud code" = Claude Code, "Swebench" = SWE-bench, "Reddus" = Redis, "Farosai" = Faros AI, "human layer" = HumanLayer, "ADER" = Aider. "I think VBOV gave us this example earlier" — unresolved speaker reference (possibly Volkov?); left out of the graph.
4. Revenue figures ($4B → $9B Claude Code) are Horthy's stage numbers, not verified financials — treat as testimony.
5. `el-swe-bench` is coined late (the corpus has referenced SWE-bench shapes since batch 2 via critiques) — grep earlier files before seeding in case you prefer to rehome older prose mentions onto it.
