# SPIKE extraction — "Local Agentic Theory For Mobile Games" (Shafik Quoraishee & Joanne Song, The New York Times) — FOR REVIEW

Source transcript: `transcripts/quoraishee-song-nyt-mobile-games.txt` (auto-captions — quotes are paraphrases, not verbatim; "Shafiq" → **Shafik Quoraishee**, "Google Seema" → likely **Google Gemma**, see Review notes).
Video: https://youtu.be/418t26CVz-w · published 2026-07-23 (AI Engineer, World's Fair — Graphs track).
`stagingTimestamp` for the artifact and all signals: 2026-07-23 (publish date).
Entities marked **[registry]** already exist — edges link, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-quoraishee-song-mobile-games` | Local Agentic Theory For Mobile Games (Shafik Quoraishee & Joanne Song, The New York Times — AI Engineer World's Fair) | youtube | https://youtu.be/418t26CVz-w |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-shafik-quoraishee`, `ContributedByExpert → exp-joanne-song`.

## Experts (2 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-shafik-quoraishee` | Shafik Quoraishee (The New York Times games; presented a Connections solver at last year's World's Fair) | `co-nyt` |
| `exp-joanne-song` | Joanne Song (The New York Times; accessibility) | `co-nyt` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-nyt` | The New York Times | media | Games/puzzles group; talk is experimental research, not shipped features — "our puzzles are made by people, not AI" |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-on-device-agentic-games` | On-device agentic games | concept | inference | Running game-agent intelligence locally on the device instead of the cloud: lower latency (no round-trip), privacy (compute stays in the device security zone), offline play (subway tunnel), and per-player personalization; the umbrella thesis — "billions of small local brains" over one centralized brain |
| `el-agentic-game-loop` | Agentic game loop | concept | harness | A perceive→predict→decide→act loop where LLM agents reason over game state via in-context learning and local tool calls (no reward to grind), adapting dynamically to new situations — contrasted with RL, which changes model weights and must be tuned per game; demoed as agentic Space Invaders and a backtracking constraint-satisfaction mini-crossword agent |
| `el-on-device-agent-constraints` | On-device agent constraint graph | concept | harness | Three-axis budget for an on-device agent modeled as a constraint graph: space (fit weights + compressed state history + planning artifacts + render headroom), time (plan inside the 16 ms / 60 Hz frame or the game janks), energy (battery; NPUs/AI chips not yet optimized for agentic workloads); managed with soft-constraining tradeoffs so no single axis is over-penalized |
| `el-adaptive-accessibility-agent` | Adaptive accessibility agent | concept | harness | On-device agent that dynamically tunes accessibility "dials" (input tolerance, step granularity) to the player's live context — grounded in WCAG 2.2's four pillars and following WCAG 3.0's shift from binary pass/fail to graded bronze/silver/gold; senses friction (eye-gaze vision models, shaky taps, keyboard focus traps), flags violations, and rewrites the layout live (resizes targets, injects exit routes) — adapting the game to the human |

Element edges: all four `DevelopedByCompany → co-nyt`; all four `IdentifiedInArtifact → ia-aie-quoraishee-song-mobile-games`; `el-agentic-game-loop` `UsesElement → el-on-device-agent-constraints`; `el-adaptive-accessibility-agent` `UsesElement → el-agentic-game-loop`; `el-agentic-game-loop` `EnablesElement → el-on-device-agentic-games`.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-quoraishee-song-mobile-games`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | domain | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|---|
| `sig-on-device-agentic-games-thesis` | NYT experimental thesis: move game-agent intelligence on-device for lower latency (no cloud round-trip), privacy (compute stays in the device's security zone), offline play, and personalization; the future of game AI need not be one giant centralized brain but billions of small local brains, each shaped by its user | inference | `pat-sovereign-ai` **[registry]** | `el-on-device-agentic-games` | `co-nyt` |
| `sig-agentic-vs-rl-games` | Shift in game AI: from RL that changes model weights per game (AlphaZero → EfficientZero V2 sample-efficient SOTA ~2024) to agentic systems where LLM agents reason over game state via in-context learning + local tool calls with no reward to grind, adapting dynamically; demoed as agentic Space Invaders and a constraint-satisfaction mini-crossword agent | harness | `pat-harness-over-model` **[registry]** | `el-agentic-game-loop` | `co-nyt` |
| `sig-on-device-agent-constraint-budget` | Running agents on-device is a three-way constraint problem — space (weights + compressed state history + planning artifacts + render headroom), time (plan within a 16 ms / 60 Hz frame or the game janks), energy (battery; NPUs not yet optimized for agentic loops) — solved via a constraint graph with soft-constraining tradeoffs; base model intelligence (ARC-AGI level) is not yet enough for the most complex game decisions | harness | `pat-harness-over-model` **[registry]** | `el-on-device-agent-constraints` | `co-nyt` |
| `sig-adaptive-accessibility-dials` | Accessibility reframed from fixed hand-authored states/toggles to on-device agents that tune "dials" (input tolerance, step granularity) to the player's live context — grounded in WCAG 2.2, following WCAG 3.0's graded scoring; the agent senses friction (eye-gaze, shaky taps, focus traps), flags violations, and rewrites the layout live (resizes targets, injects exit routes), adapting the game to the human rather than the reverse | harness | `pat-harness-over-model` **[registry]** | `el-adaptive-accessibility-agent` | `co-nyt` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-local-brains-not-one-brain` | The future of AI need not be one centralized brain; it can be billions of small local brains, each running on a personal device and shaped by the individual it serves — enabling privacy, offline capability, and deep personalization for gameplay | `pat-sovereign-ai` **[registry]** | `el-on-device-agentic-games` |
| `ins-adapt-game-to-human` | Accessibility and challenge stop being separate concerns and become two ends of one continuously-tuned dial; a live layout auditor adapts the game to the human in real time rather than forcing the human to adapt to fixed menus — turning devices into responsive, empathetic partners | `pat-harness-over-model` **[registry]** | `el-adaptive-accessibility-agent` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-quoraishee-song-mobile-games`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-budget-on-device-agent` | Budget an on-device game agent across space, time, and energy | Model a constraint graph over space (fit weights + compress agent state history and planning artifacts + reserve render headroom), time (fit agent planning inside the 16 ms / 60 Hz frame or accept jank), and energy (minimize per-loop compute to protect battery until NPUs mature); use soft-constraining so one axis isn't over-penalized (allow a little extra space, but penalize extra time that disrupts UX); keep the on-device loop tightly curated for minimum energy | `el-on-device-agent-constraints`, `el-agentic-game-loop` |
| `how-dynamic-accessibility-agent` | Build accessibility as a live, agent-tuned scale | Ground in an existing standard (WCAG 2.2 pillars; adopt WCAG 3.0's graded scoring); expose dials (input tolerance, step granularity) instead of a static easy-mode; use on-device vision (eye-gaze), tap-jitter, and focus-path monitoring to sense real-time friction; act, don't just watch — resize controls, inject exit routes from keyboard/focus traps, allow handwriting recognition; groundwork still needed: sub-16 ms decisions, game-outcome prediction before applying a change, long-term per-user memory, a shared game-state language across games, and faster chips paired with honest benchmarks | `el-adaptive-accessibility-agent` |

## Dropped

- Pac-Man finite-state-machine as classic symbolic game AI — historical framing; no node.
- AlphaGo/AlphaZero and EfficientZero/EfficientZero V2 detail — RL history; folded into `sig-agentic-vs-rl-games` prose (⚠ "EfficientZero" caption-read).
- Google "Seema" generalist on-device model (likely **Gemma**, garbled), gaze-estimation CNNs, generative worlds — named as models/factors under consideration; kept in prose, no nodes.
- "Wordle Bot is not an AI feature" / "our puzzles are made by people" disclaimers — context, not signal.
- Last year's Connections-solver talk — self-reference (noted on `exp-shafik-quoraishee`).

## Review notes

1. `co-nyt` typed `media` per task. Both speakers affiliated at company level; sub-team not stated.
2. Four signals split: the on-device/local-first compute thesis → `pat-sovereign-ai` **[registry]** (the established mapping for local/on-device AI, cf. Osman batch 4, Local-AI panel batch 6); the agentic-loop, constraint-engineering, and adaptive-accessibility claims → `pat-harness-over-model` **[registry]** (behavior/reliability from scaffolding + constraints around a base model whose raw intelligence isn't yet sufficient).
3. **Candidate-pattern evidence (not coined):** `sig-adaptive-accessibility-dials` / `ins-adapt-game-to-human` — "the agent rewrites the layout live, adapting to the human" — is a clean data point for the uncoined **`pat-adaptive-software`/`pat-adaptive-harness`** candidate (software that reshapes itself per user at runtime). Parked on `pat-harness-over-model`; flag for the adaptive-software coin decision.
4. Caption garbles flagged: speaker "Shafiq" → Shafik Quoraishee (task); "Seema" → Gemma; "EfficientZero" as auto-transcribed. ARC-AGI referenced as the base-intelligence bar.
