# SPIKE extraction — "Computer-Use 2.0: Agents Just Got Multi-Cursor" (Francesco Bonacci, Cua) — FOR REVIEW

Source transcript: `transcripts/bonacci-cua-computer-use-multicursor.txt` (auto-captions — quotes are paraphrases, not verbatim; product names heavily garbled, see review note 1).
Video: https://youtu.be/ZSQb5fzRFPw — AI Engineer World's Fair, published 2026-07-15.
`stagingTimestamp` for the artifact and all signals: 2026-07-15 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-bonacci-computer-use` | Computer-Use 2.0: Agents Just Got Multi-Cursor (Francesco Bonacci, Cua — AI Engineer World's Fair) | youtube | https://youtu.be/ZSQb5fzRFPw |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-francesco-bonacci` (co-presenters not coined — see review note 2).

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-francesco-bonacci` | Francesco Bonacci (CEO, Cua; ex-Microsoft GUI-agents work) | `AffiliatedWithCompany → co-cua` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-cua` | Cua | developer | computer-use agent infrastructure company (Cua Driver, Cua Bench, Cua Fleet); team traces to GUI-agent work at Microsoft |
| `co-snorkel-ai` | Snorkel AI | developer | data-labeling/eval company; collaborator on Cua's electrical-engineering computer-use benchmark |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-cua-driver` | Cua Driver | framework | harness | Open-source (released ~2 months before the talk, spurred by Codex's computer-use model) background computer-use driver: lives at the OS level (incl. undocumented Apple framework APIs) across macOS/Windows/Linux, exposes window-state snapshots (accessibility tree + screenshot), attempts background execution via the accessibility tree and falls back to pixel-level background clicks — agents operate apps without taking over the user's screen |
| `el-cua-bench` | Cua Bench | framework | harness | Cross-platform computer-use benchmark + SDK: tasks are setup/oracle/evaluator triples (oracle = golden GUI-action trajectory) authorable by anyone (or any agent) as a single Python file targeting 5+ desktop platforms; 130+ verifiable tasks, 42 environments; includes a Snorkel AI collaboration testing agents on real professional electrical-engineering software with evaluators that actually simulate the circuits; recorded runs can be forked at any trajectory moment to probe a model's world-model predictions |
| `el-cua-fleet` | Cua Fleet | product | infra | Instant-sandbox infrastructure for computer-use RL training: a demand-based autoscaler grows a warm sandbox pool to match how many GPU workers currently need one, moving sandbox startup/reset cost (e.g. 40 GB environments) off expensive GPU time; Windows/Linux/Android, macOS coming |

Element edges: all three `IdentifiedInArtifact → ia-aie-bonacci-computer-use` and `DevelopedByCompany → co-cua`; `el-cua-driver` `ExemplifiesPattern → pat-harness-over-model` **[registry]**; `el-cua-bench` `ExemplifiesPattern → pat-verification-gap` **[registry]**; `el-cua-fleet` `EnablesElement → el-cua-bench`.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-bonacci-computer-use`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-cua` unless noted.

| slug | name / brief | domain | FormsPattern |
|---|---|---|---|
| `sig-computer-use-goes-background` | Computer use is moving from 1.0 (screenshot → reason/plan → click/type/scroll, agent takes over the human's screen) to 2.0: background, windowed, OS-integrated drivers where agents run "multi-cursor" on the user's own laptop without seizing control — Cua shipped this open source within a weekend of Codex releasing its computer-use model (~2 months before the talk) | harness | `FormsPattern → pat-harness-over-model` **[registry]** |
| `sig-driver-swap-lifts-pass-rate` | Harness, not model, moved the number: on the Cua Bench basic set at 4K resolution, swapping the agent's built-in computer tool for Cua Driver raised pass rate 62% → 80% while using 34% fewer tokens — mostly because the driver scopes observation to a window instead of the whole desktop | harness | `FormsPattern → pat-harness-over-model`, `FormsPattern → pat-model-not-bottleneck` **[registry]** |
| `sig-professional-gui-work-unsolved` | Grounding result: on the Snorkel AI-collaboration benchmark (real professional electrical-engineering software, evaluators that simulate the circuits) the top agent fully passed only 6 of 25 tasks — 100% of those were edits to an existing schematic; from a blank schematic the success rate was 0%, no model exceeded 30% reward, and the leaderboard is flat across models (also `RelevantCompany → co-snorkel-ai`) | harness | — (capability-limit observation; see review note 4) |
| `sig-evals-get-red-teamed` | Eval trust is now itself engineered: before any task enters the Cua Bench dataset, a matrix of agents attempts reward hacking and environment breaking, results are compiled into a code-review-style report, and only surviving tasks ship — "it's evals all the way down" | harness | `FormsPattern → pat-verification-gap` **[registry]** |
| `sig-idle-gpus-dominate-cu-rl-cost` | In RL training for computer-use agents, GPUs sit idle while sandboxes spin up or reset (environments can be ~40 GB and can't always be made fast to start); demand-based autoscaled warm sandbox pools — sandbox capacity being 2–4× cheaper than GPU time — shift that cost off the GPUs and keep workers at full utilization | infra | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-agents-become-coworkers-not-puppeteers` | Once the computer-use "hands" live in an OS-level background driver, agents stop being screen puppeteers mimicking a human at the keyboard and become concurrent co-workers sharing your machine ("multi-cursor") — and the differentiating engineering moves into the driver/harness layer (accessibility-tree access, windowed observation, cross-OS lifting), not the model | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-cua-driver` |
| `ins-world-models-made-measurable` | Measuring an agent's intelligence requires more than action success: by forking a recorded run at any moment and asking a model to predict the reward, internal state, or other observations against the actual fork, the agent's world model becomes measurable — verification extended from "did it do the thing" to "does it understand the world it operates in" | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-cua-bench` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-bonacci-computer-use`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-harden-cu-evals` | Red-team environments before trusting the eval | Author tasks as setup/oracle/evaluator triples with real verifiers (e.g. actually simulate the circuit, don't pattern-match the UI); before accepting a task, run a matrix of agents that try to reward-hack and break the environment; review the compiled attack data code-review style; admit only surviving tasks; regression-test the harness itself against a suite of application harnesses across releases | `ReferencesElement → el-cua-bench` |
| `how-warm-sandbox-pools` | Keep RL GPUs hot with autoscaled sandbox pools | Minimize sandbox startup where practical, but don't assume you can (40 GB environments happen); instead run a warm pool sized by a demand-based autoscaler that tracks how many GPU workers currently need a sandbox — no upfront pool-size guess, and the right size drifts over a multi-day run (fewer sandboxes as generations lengthen); accept sandbox redundancy since it's 2–4× cheaper than the GPU time it saves | `ReferencesElement → el-cua-fleet` |

## Dropped

- Terminal Bench / Harbor — comparison anchors only; prose.
- Early adopters list ("clicky mass queno h company and droid factory") — too garbled to attribute; omitted entirely rather than guessed (review note 1).
- Q&A on Android/mobile (containerized background workloads, Activity framework, tool use over GUI) — directional aside; no entity.
- Microsoft provenance of the team — kept in `co-cua`/expert briefs; no `RelevantCompany → co-microsoft` edge since it's biography, not signal content.

## Review notes

1. Heaviest garble file of my set: captions render the company/products as "Kua/qua/KU", "quad driver"/"KU driver"/"cooler driver" (= Cua Driver), "kuab bench"/"KUBench"/"Kua bench" (= Cua Bench), "qua fleet" (= Cua Fleet) — resolved against the official title ("Cua"). "KUBench Kyad" (the Snorkel AI EE benchmark's name) is unresolved — plausibly "CAD"; I avoided naming it in node briefs. The early-adopters list is unrecoverable and was dropped, not guessed.
2. Co-presenters "Dylan" (CTO, Cua Bench section) and "Robert/Rob" (chief infrastructure officer, Cua Fleet section) are first-name-only in the captions; I did not coin Expert nodes on first names. If reconciliation can recover surnames from the video, add `exp-dylan-<surname>` / `exp-robert-<surname>` with `ContributedByExpert` + `AffiliatedWithCompany → co-cua`.
3. "Codex releasing their computer use model two months ago" — taken at face value as the trigger event for Cua Driver; attribution to OpenAI/Codex is caption-based, so I kept it in signal prose without a `RelevantCompany → co-openai` edge.
4. `sig-professional-gui-work-unsolved` carries no FormsPattern: it is a capability-limit result. Arguably `ContradictsPattern → pat-accelerated-research` (agents far from autonomous professional work) — I left it edge-free rather than stretch; add that edge if you read contradiction edges permissively.
5. `el-cua-bench` kind: it is dataset + SDK + methodology; `framework` chosen over `product`.
