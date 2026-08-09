# SPIKE extraction — "The Missing Layer After Launch" (Raphael Kalandadze, Wandero AI) — FOR REVIEW

Source transcript: `transcripts/kalandadze-wandero-missing-layer.txt` (auto-captions — quotes are paraphrases, not verbatim; this transcript is heavily garbled, see notes).
Video: https://youtu.be/kZsf_Sfm7RU — AI Engineer World's Fair, published 2026-07-05.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-07-05 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-kalandadze-missing-layer` | The Missing Layer After Launch (Raphael Kalandadze, Wandero AI — AI Engineer World's Fair) | youtube | https://youtu.be/kZsf_Sfm7RU |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-raphael-kalandadze`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-raphael-kalandadze` | Raphael Kalandadze (Wandero AI; operates production travel-planning agents with a three-person team) | `AffiliatedWithCompany → co-wandero` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-wandero` | Wandero AI | developer | AI travel startup — its production agent builds trips/itineraries for users; a three-person team runs a self-monitoring agent-ops stack around it (⚠ vertical inferred from the in-talk example, see notes) |

## Elements (1 new + 1 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-meta-harness` | Meta harness | concept | harness | Speaker's coinage for a self-watching harness of agents around a production agent: a log-monitoring agent (short-window cadence, codebase access, auto-PRs / Slack alerts), a separate fresh-context review agent that adversarially scores and criticizes those PRs, a session analyzer scoring every real conversation for system health, and a computer-use agent simulating the customer in the browser — all wired with human-grade access (trajectories, metrics, database, UI, code) so diagnoses are grounded in the real problem rather than guessed |

Reused: `el-codex` **[registry]** — used to drive the browser for customer simulation before a faster site-specific, DOM-aware skill replaced generic driving.

Element edges: `el-meta-harness` `IdentifiedInArtifact → ia-aie-kalandadze-missing-layer`, `ExemplifiesPattern → pat-harness-over-model` **[registry]**; `el-codex` `IdentifiedInArtifact → ia-aie-kalandadze-missing-layer` (reuse edge only).

## Signals (5 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-kalandadze-missing-layer`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-agent-failure-hides-itself` | Agent failure hides itself: a long-running agent that struggles mid-task and recovers "by luck" (workarounds, alternate tool calls) raises no red alert while the defect stays live in the codebase — and "finished" ≠ helpful (Wandero example: itinerary built, but wrong service chosen and price miscalculated; technically successful, task failed). Unit tests, regex/rule checks, and simulated conversations cover only one slice, because real customers are endless, all different, and LLM paths are non-deterministic — production is where you learn what to test in the first place | `FormsPattern → pat-verification-gap` **[registry]** | `RelevantCompany → co-wandero` |
| `sig-wandero-agents-operate-agents` | Operating a production agent turned out to be an agent problem: Wandero's log-monitoring agent runs every 15–60 minutes over a one-hour log window with codebase access, deep-dives trajectories, determines whether users ended up stuck, and opens PRs — with description, metadata, mermaid/ASCII diagrams, and HTML artifacts for at-a-glance triage — or fires Slack alerts for critical issues; fix-PRs can be ready in ~30 minutes | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-wandero` |
| `sig-fresh-context-review-agent` | A separate review agent with deliberately fresh context — not biased by the diagnosing agent's framing — criticizes, scores, runs focused tests, requests changes, or closes PRs outright (eager PR-senders need a critic). The PR + review agents produce ~10× more PRs per day than the three humans; the human stays as final gate only until the loop earns trust: "close the loop first, make yourself the bottleneck, then remove yourself" | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-wandero` |
| `sig-score-every-conversation` | Wandero's session analyzer scores every production conversation — health score, success/rejection rates and why, trends, sentiment, entities, tool-call analytics, per-session ranked deep dives, and cross-session AI insights with root causes, sessions affected, and recommended fixes — visibility that "before agents was impossible"; built in-house despite existing vendor tools ("I know what I'm looking for") | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-wandero` |
| `sig-ops-loop-is-differentiator` | "Everyone can have the same model, the same agent, the same harness" — shipping is now the easiest part (a whole product or startup in days, 100k lines of code, lots of tokens); the internal system that closes the post-launch loop — detect, diagnose, fix, feel the health — is the differentiating asset, and the tight feedback loop is "at least as important as the product itself, sometimes more" | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-wandero` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-shipping-starts-real-work` | Most agent talks end at "we shipped; it worked" — but shipping is when the real work begins: coverage is endless, LLMs are non-deterministic, failures self-conceal, and without a post-launch loop you lose the feel for whether your own system is getting better or worse. The missing layer of the agent stack is everything after launch | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-meta-harness` |
| `ins-ops-agents-need-human-grade-access` | Log triage is a reasoning task (real bug vs. noise, symptom vs. root cause, deep-diving a fresh trajectory), so the ops layer must itself be agents — and they only work when given everything a human debugger gets: trajectories, metrics, database, UI, and code (e.g. the computer-use agent must be able to check the DB and trajectories to chase what it finds). Anything less produces guesses, not grounded diagnoses | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-meta-harness` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-kalandadze-missing-layer`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-agent-ops-pr-loop` | Run an agent-operated detect→diagnose→PR loop | Point a log-monitoring agent at production trajectories on a short-window cadence (every 15–60 min, ~1-hour log window) with codebase access; have it auto-open PRs carrying a readable diagnosis (description, metadata, mermaid/ASCII diagrams, HTML artifacts) and Slack-alert critical issues immediately; gate merges behind a second review agent with fresh context that criticizes, scores, and runs focused tests across iterations before any human sees it; keep a human as the final gate until the loop is calibrated and trusted — become the bottleneck deliberately, then remove yourself | `ReferencesElement → el-meta-harness` |
| `how-zoom-out-session-scoring` | Zoom out: score every session and simulate the customer | Complement the fast local-fix loop with a session analyzer run weekly-ish over all conversations: health score, success rate, sentiment, entities, tool-call analytics, ranked per-session deep dives, cross-session pattern insights with root causes and fixes (accept the token spend); add a computer-use agent that logs in and behaves like a customer to catch UI-facing failures that logs and code can't show — build it a site-specific, DOM-aware skill (generic driving, e.g. via Codex, is slow) and give it trajectory + database access so it can investigate what it finds | `ReferencesElement → el-meta-harness` |

## Dropped

- Anthropic blog-post reference (agents marking features complete without checking they actually worked — captions garble this as "marketing features") — supporting citation kept in prose; no edge to `co-anthropic` **[registry]**.
- Claude Code / Codex as examples of endless-coverage agents — passing capability mention (the `el-codex` edge is kept only for the actual computer-use usage).
- The in-house dashboard as a product node — unnamed internal tool; folded into `el-meta-harness` and `sig-score-every-conversation`.

## Review notes

1. **Heavy caption garbling.** Readings applied: "the failure height itself" → "failure hides itself"; "marketing features as complete" → "marking features as complete"; "runs a lot of state agents" → likely "sub-agents"; "Harrison for it in the same way" → unresolved, dropped. Verify all before quoting.
2. `co-wandero`'s travel vertical is inferred from the single in-talk example (user asks the agent to build an itinerary/trip; price miscalculated) plus the "Wandero AI" listing — brief kept minimal; verify the company description.
3. Operational numbers (15–60 min cadence, ~30-min PR turnaround, ~10× PR volume, three-person team) are self-reported paraphrases.
4. "Meta harness" is the speaker's own coinage and kept as the element name; adjacent to batch-2 `el-harness-engineering` but distinct (post-launch self-monitoring ops vs. build-time harness discipline) — flag for reconciliation if you read them as one.
5. No pattern candidate here: the talk composes `pat-verification-gap` + `pat-harness-over-model` + `pat-model-not-bottleneck`, all existing. It is ops/observability, not durable execution — deliberately NOT added as `pat-durable-execution` evidence.
