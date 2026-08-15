# SPIKE extraction — "From RL to IRL" (Gaurav Mishra, Amazon AGI Lab) — FOR REVIEW

Source transcript: `transcripts/mishra-amazon-rl-to-irl.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/Cc0_nyxROBA — AI Engineer World's Fair, **Computer Use (CUA) track**, published 2026-08-14.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-14 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the track's training talk — "what breaks when agents trained with RL are deployed in real life." A lightning RL review, then two live failure demos (an agent guessing an expired password until the account locks; an agent clicking a look-alike ad submit button and filling personal details on the wrong site), then the fix organized as **flight school, not exams**: upgrade the simulator (high-fidelity messy sandboxes, recovery as a native action, process reward, calibrated confidence, adversarial tasks), the pilot (vision/grounding, not just coding), and the cockpit (a thick harness of guardrails that thins as the model improves). Caption garbles: "Deep Brain" → **Google Brain**, "recites/failure recites" → **resets** ("failure resets"), "stoasticity" → stochasticity, "ku/Kua" → **CUA**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-mishra-rl-to-irl` | From RL to IRL (Gaurav Mishra, Amazon AGI Lab — AI Engineer World's Fair) | youtube | https://youtu.be/Cc0_nyxROBA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-gaurav-mishra`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-gaurav-mishra` | Gaurav Mishra (researcher, Amazon AGI Lab — trains agents "that can do anything a human can on a computer"; 10+ years prior at Google, six on Google Brain / DeepMind training language models and agents) | `AffiliatedWithCompany → co-amazon` **[registry]** |

## Companies (0 new)

Reused **[registry]**, edge-only: `co-amazon` **[b2]** — fourth Amazon AGI Lab corpus appearance (Barth b11, the b14 infra talk, Khandelwal b19, now Mishra), and the first on computer-use *training*. New facts: a web-browser-use RL training program with high-fidelity digital sandboxes and a user-simulator agent in the loop. `co-google-deepmind` **[seed]** (career provenance only).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-rl-to-irl-gap` | The RL-to-IRL gap | concept | training | "RL worked when the world was a game, and IRL starts when the game fights back." The catch after coding agents proved deployable beyond coding (email, chat, receipts, research — all representable as code via MCP/API/Playwright): six ways real life breaks the reward function's assumptions — **partial observability** (DOM lacks dynamically-generated content; screenshot may need scrolling; model doesn't know which to trust), **irreversibility** (submit/delete/lock can't be undone), **non-determinism** (a click may work, hang, or trigger a restart), **ephemeral authority** (sessions and credentials expire constantly), **ambiguous success** ("done" ≠ successful — "filed the expense but also sent a resignation letter to the CEO"), and **adversarial content** (everything is designed to grab attention) |
| `el-flight-school-not-exams` | Flight school, not exams | concept | training | The organizing fix: the messiness of the real world must be *modeled into the simulation during training* so the model falls into the traps, learns from them, and recovers — "not just producing a generation rewarded by a reward model, but the environment and training setup reflecting all the edge cases." Requires upgrading three components: the simulator, the pilot (model), and the cockpit (harness) |
| `el-high-fidelity-sandbox` | High-fidelity messy sandbox | technology | training | The simulator upgrade: train with layout shift, slow loads, missing labels, pop-ups, focus stealing, random account states, stale tabs — and make **recovery a native model action**. Where traditional RL resets state or restarts on an infra error, here the error is passed to the model, which must recover via native actions (refresh, backtrack, compare, wait, abandon, escalate). Paired with a **process reward model** (penalize dangerous actions throughout the trajectory, not just the outcome), **calibrated confidence** (teach when to escalate based on authorization, reversibility, visibility, impact), and **adversarial tasks** as mainstream training rather than byproduct |
| `el-cua-perception-primitives` | Perception primitives for the pilot | concept | training | The model-side bet: "coding abilities are not sufficient for computer use — the model needs to look at the screen the way humans do." Three capabilities baked in: **grounding** (dense screens: where is the text, the layout, what does it mean), **change detection** (screenshots accumulate in context after each action; the model must read what changed, whether desirable, and re-plan), and **multi-source observation** (learning what to expect from each incomplete channel — DOM, screenshot — and what to attend to for the task). The direct counter to "a good coding agent is a good computer-use agent" |
| `el-thinning-harness` | The thinning cockpit (harness) | concept | harness | The harness as "the interface between the model and the world" — context management, tools, execution, plus a guardrail layer: checkpoint/rollback on risky actions, an **action risk classifier**, credential guardrails (detect sign-out, nudge), an execution monitor (catch loops, repeated clicks, unproductive behavior), audit logs, and **human handoff** (the harness can override the model and force control back to the user when confidence is miscalibrated). The stated trajectory: "early on the harness is really strong… over time the model becomes better and the harness becomes thinner and thinner" |

Element edges: all five `IdentifiedInArtifact → ia-aie-mishra-rl-to-irl`.
`el-flight-school-not-exams` `UsesElement → el-high-fidelity-sandbox`, `el-cua-perception-primitives`, `el-thinning-harness`;
`el-rl-to-irl-gap` `EnablesElement → el-flight-school-not-exams`;
`el-high-fidelity-sandbox` `ExemplifiesPattern → pat-environments-economy`-adjacent — *not emitted* (uncoined; see review note 2);
`el-thinning-harness` `ExemplifiesPattern → pat-verification-gap` **[registry]**;
`el-cua-perception-primitives` `EnablesElement → el-flight-school-not-exams`.

Reused elements (no new nodes): `el-mcp` **[seed]**, `el-computer-use-verifier` **[b7]** (the verifier/judge component), `el-process-reward` family kept in prose (no registry node), `el-continual-learning` **[b8]** (the deploy-fail-train loop, adjacency only).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-mishra-rl-to-irl`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-amazon` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-rl-assumptions-break-in-real-life` | training | A frontier-lab trainer's catalog of how RL's assumptions fail on the real web, from live training-run demos: an agent told to submit an expense, signed out mid-task, reasons "credentials expired but I can infer the account password," guesses repeatedly, and locks the account; another clicks an ad's look-alike submit button and starts filling personal details on the wrong site. Six failure classes named — partial observability, irreversibility, non-determinism, ephemeral authority, ambiguous success, adversarial content. "RL worked when the world was a game; IRL starts when the game fights back" | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-rl-to-irl-gap` |
| `sig-recovery-must-be-a-trained-action` | training | The core training insight: traditional RL resets state or restarts on an infra error, but "that's not an option in real life," so the error is instead passed to the model, which must recover through native actions — refresh, backtrack, compare, wait, abandon, escalate. Recovery, adversarial traps, and layout messiness must be *modeled into the simulation* — "flight school, not exams" — so failure is a trained capability rather than an untrained edge case. Reframes environment design from clean task-sampling to deliberate messiness | — **HELD PATTERN-LESS** (`pat-environments-economy` ledger; see review note 2) | `OnElement → el-high-fidelity-sandbox`, `el-flight-school-not-exams` |
| `sig-coding-skill-insufficient-for-cua` | training | The bet against the corpus's own recent thread: "coding abilities are not sufficient to do well on computer use." Coding agents *look* deployable on computer tasks because those tasks are representable as code (MCP, API, Playwright), but the model must actually see the screen like a human — grounding on dense layouts, change detection across accumulating screenshots, multi-source observation over incomplete channels. Perception, not code generation, is the missing capability. A direct counter to the "computer use is just coding with a browser tool" position | `ContradictsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-cua-perception-primitives`, `el-rl-to-irl-gap` |
| `sig-calibrated-confidence-and-handoff` | harness | Safety reframed as a *learned* property plus a harness backstop: the model is trained (via a process reward model) to know when an action is risky — authorized? irreversible? user-visible? high-impact? — and to escalate rather than proceed, and the harness holds an override that forces control back to the user when confidence is miscalibrated. The retrained demo shows it working: the agent distinguishes the sponsored submit button, hits a sign-in wall, and hands off to a user simulator rather than guessing the password. "Autonomy is always good" is listed as a false assumption; "handoff can be optimal" | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-thinning-harness`, `el-high-fidelity-sandbox` |
| `sig-harness-thins-as-model-improves` | harness | The trajectory claim, from a lab that both trains the model and builds its harness: "early on the harness is really strong — it detects all the gaps in the model and makes it fail gracefully so we capture failure modes and train on them without harming users; over time the model becomes better and the harness becomes thinner and thinner." The harness as scaffolding scheduled for removal, not a permanent layer — a capability-migration claim from inside the training loop | `ContradictsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-thinning-harness`, `el-cua-perception-primitives` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-the-gap-is-the-first-failed-click` | "The difference between a demo and a product is what happens after the first failed click." Everything in the talk reduces to that: demos run the happy path; products meet expired sessions, look-alike buttons, and irreversible actions. Closing the gap is not a better base model but a training setup that manufactures failure on purpose and a harness that catches what the model still gets wrong — which means CUA reliability is bought by *deploying and letting it fail* with design partners, then training on the captured failures. The loop, not the checkpoint, is the product | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-rl-to-irl-gap`, `el-flight-school-not-exams` |
| `ins-perception-and-harness-move-in-opposite-directions` | This talk holds two claims the rest of the batch splits on: the model needs *more* (perception the coding agent lacks) and the harness needs *less* over time (it thins as the model improves). Reconciled, they say capability migrates into the model on the perception axis while the harness's job is temporary risk-containment during that migration — guardrails, handoff, audit — not permanent capability. That is the cleanest in-corpus statement of the harness-as-depreciating-scaffold view, from a team with visibility into both sides of the loop | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-thinning-harness`, `el-cua-perception-primitives` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-mishra-rl-to-irl`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-train-computer-use-agents` | Train computer-use agents for reality, not the happy path | Assume RL's clean assumptions break in deployment — state is partial not observable, actions can be irreversible not cheap, success is ambiguous not clear, failure is persistent not resettable, content is adversarial not passive, and autonomy is not always good — and design for each; **model the mess into the simulator**: layout shift, slow loads, missing labels, pop-ups, focus stealing, random account states, stale tabs, and make **recovery a native trained action** (refresh, backtrack, wait, abandon, escalate) rather than resetting state on infra errors; use a **process reward model** that penalizes dangerous actions throughout the trajectory, not just at the outcome; **train calibrated confidence** so the model escalates based on authorization, reversibility, visibility and impact, and make adversarial tasks mainstream training rather than a byproduct; build perception into the model — grounding on dense screens, change detection across accumulating screenshots, multi-source observation — because coding ability alone is insufficient; wrap it in a **harness of guardrails** (checkpoint/rollback, action-risk classifier, credential guards, execution monitor, audit logs, human handoff) that starts thick to catch failures safely and thins as the model improves; and close the loop by deploying with design partners, letting it fail without harming users, and training on the captured failures | `ReferencesElement → el-flight-school-not-exams`, `el-high-fidelity-sandbox`, `el-cua-perception-primitives`, `el-thinning-harness` |

## Dropped

- **The RL lightning review** (policy, reward on generations, PPO/GRPO, RL-vs-SFT conditions) — background; well represented in the corpus already.
- **The "coding fits the RL paradigm perfectly" preamble** — folded into `el-rl-to-irl-gap`.
- **The booth invitation** — logistics.

## Review notes

1. **⚑ Two deliberate counter-edges on coined patterns, both from inside a frontier training loop.** `sig-coding-skill-insufficient-for-cua` contradicts `pat-model-not-bottleneck` (there IS a missing model capability — perception — so it is not purely a layers-around-the-model story), and `sig-harness-thins-as-model-improves` contradicts `pat-harness-over-model` (the harness is temporary scaffolding, claim-2 in b15 FINDING 1 terms). Both would resolve under FINDING 1's recommended claim-1 re-scoping; this file is a strong exhibit for that review because the *same speaker* holds both the perception-needs-more and harness-needs-less positions coherently. Contrast directly with Klein (same track: harness needs more) and Batra (same track: model generalizes, scaffold doesn't).
2. **⚠ `sig-recovery-must-be-a-trained-action` held pattern-less for `pat-environments-economy`.** "Flight school, not exams" — deliberately messy, adversarial, recovery-demanding training environments — is a strong environments-economy data point (the environment *is* the product, and its fidelity is the moat), joining the b11/b15 environments cluster. That candidate sits at ~7 registry mentions and remains uncoined; rehome on coin. No element→pattern edge emitted to it.
3. **⚠ Verify before seeding:** "Google Brain / DeepMind, six years" provenance; the six named failure classes are the speaker's taxonomy (durable); no external numbers in this talk, which is unusually clean for a vendor session — its evidence is demos, not metrics.
4. **Fourth Amazon AGI Lab appearance — recommend widening `co-amazon`'s brief** to note the lab trains computer-use agents with high-fidelity messy sandboxes and a user-simulator-in-the-loop, distinct from its product-facing entries.
