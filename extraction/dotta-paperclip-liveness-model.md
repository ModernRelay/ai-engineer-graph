# SPIKE extraction — "What Does Done Even Mean? Agents and Paperclip's Liveness Model" (Dotta, Paperclip) — FOR REVIEW

Source transcript: `transcripts/dotta-paperclip-liveness-model.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/7P0elyLIxXo — AI Engineer World's Fair, published 2026-07-12.
`stagingTimestamp` for the artifact and all signals: 2026-07-12 (publish date).
Short talk (~5 min) — 3 signals per the thin-talk allowance.
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-dotta-liveness` | What Does Done Even Mean? Agents and Paperclip's Liveness Model (Dotta, Paperclip — AI Engineer World's Fair) | youtube | https://youtu.be/7P0elyLIxXo |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-dotta`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-dotta` | Dotta (creator of Paperclip; self-introduces only as "I'm Dota" — appears to be a handle, no legal name given in the talk) | `AffiliatedWithCompany → co-paperclip` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-paperclip` | Paperclip | developer | maker of the Paperclip agent-work control plane (liveness model, watchdogs, first-class blockers) |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-done-as-object` | Done-as-object | concept | harness | "Done" is a bundle of claims, not a Boolean: artifact produced, scope, rubric/standard, evidence, who verified, who had authority to sign off, residual risk, and next action + next owner; done-for-merge, done-for-deploy, and done-for-customer-announcement are different operational claims most agent systems flatten to one green checkmark; ladder of doneness: producer-claimed → reviewed → verified-against-standard → approved-by-authorized-party → stood-behind → survived real-world conditions |
| `el-liveness-model` | Liveness model (agent control plane) | concept | harness | Balancing liveness (work keeps moving, no blockers) against verification (a human-reviewed task is assured but dead in its tracks); three invariants for an agentic control plane: productive work continues, only real blockers stop work, infinite loops are bounded; full liveness with no approvals = AI slop, full human review = an unreviewable queue |
| `el-paperclip` | Paperclip | product | harness | Agent-work control plane implementing the liveness model: explicit task-state transitions, first-class enforced blockers between tasks, dependency trees, idempotent checkouts/locks, interactive human approvals that leave an audit trail, explicit reviewers/approvers per task (incl. agent reviewers), and harness-agnostic "watchdog" maximizer agents that hold a goal and keep all agents working until it is achieved — one interface across Claude Code, Codex, Hermes, and other harnesses |

Element edges: all three `IdentifiedInArtifact → ia-aie-dotta-liveness`; `el-paperclip` `UsesElement → el-liveness-model`, `UsesElement → el-done-as-object`, `DevelopedByCompany → co-paperclip`; `el-liveness-model` `ExemplifiesPattern → pat-verification-gap` **[registry]**.

## Signals (3 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-dotta-liveness`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-agents-create-unverifiable-volume` | Practitioner claim from a control-plane builder: "programming is solved" — agents now produce more code and documentation than any human can verify, a new failure mode where agents create more *work* than humans have time to check; mandatory human sign-off at that volume degrades into verification theater | `FormsPattern → pat-verification-gap` **[registry]** | — |
| `sig-done-flattened-to-checkmark` | Current agent systems flatten operationally distinct claims — done-to-merge vs done-to-deploy vs done-to-announce — into a single green checkmark; an agent passing tests, updating docs, and commenting "looks done to me" is a producer *claim*, not verification | `FormsPattern → pat-verification-gap` | `OnElement → el-done-as-object` |
| `sig-watchdogs-above-harnesses` | Paperclip ships harness-agnostic watchdog agents: a goal-holding agent enforces that all worker agents keep going until the goal is achieved, with one consistent interface across harnesses (Claude Code, Codex, Hermes, others per captions) — evidence of a control-plane layer forming *above* interchangeable agent harnesses | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-paperclip` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-liveness-verification-tension` | The core design tension of agentic work systems: verification kills liveness (a human-reviewed task stops moving) and liveness kills verification (unapproved work compounds into slop that is worse than nothing); a naive for-loop over a task manager collapses once dependency trees, blockers, multi-agent handoffs, and checkout locks enter — the balance must be enforced by a control plane with contracts, not by the agents | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-liveness-model` |
| `ins-treat-done-as-object` | Stop treating done as a Boolean and treat it as an object: humans paper over the artifact/scope/rubric/evidence/verifier/authority/risk/next-action distinctions automatically, but agents must carry them explicitly for delegated work to be trustworthy at volume | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-done-as-object` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-dotta-liveness`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-define-done-for-agents` | Define done for agent work (the "100× checklist") | Define exactly what done means per task, in detail; separate verifier from author — ideally a different model (code with Claude, verify with Codex); require evidence, and give agents the tools to produce it (custom browser harness, screenshots, hooks/tooling to click through and try the work themselves); establish a clear chain of custody — every agent knows who receives the work next; set explicit reviewers and approvers so completion triggers review; use goal-holding watchdogs to keep work moving within bounds | `ReferencesElement → el-done-as-object`, `ReferencesElement → el-paperclip` |

## Dropped

- "Custom agent hooks" mention — passing; no edge to `el-agent-hooks` [registry, batch1].
- The opening PR vignette (passes tests, updates docs, "looks done to me") — folded into `sig-done-flattened-to-checkmark`.
- Watchdog as its own Element — it is a Paperclip mechanism; folded into `el-paperclip` brief.

## Review notes

1. **Speaker identity:** transcript self-introduction is "I'm Dota"; the official talk title spells it Dotta — Expert named `exp-dotta` per the title. It reads as a handle/mononym; the transcript reveals nothing beyond "creator of Paperclip". Verify spelling/identity against the video description before seeding.
2. **Caption garble:** the harness list for watchdogs reads "Pi, OpenGL, Hermes, Claude Code, Codex". "OpenGL" is almost certainly **OpenClaw** (`el-openclaw` [registry]) mis-captioned; "Pi" is unresolved (an agent harness? "Poe"?). Because the garble is unconfirmed, no `OnElement → el-openclaw` edge was added — add it if the video confirms. "Hermes" plausibly matches seed `el-hermes-agent`; also left unlinked pending confirmation. "Item potent" = idempotent.
3. `sig-watchdogs-above-harnesses` → `pat-harness-over-model`: read as the control-plane-above-swappable-harnesses claim; it also brushes the uncoined "durable runtime / durable execution as a stack layer" candidate (batch-4 review note, `pat-durable-execution` proposal) — Paperclip is arguably a third data point (task-state machines, locks, bounded loops, audit trails) for that candidate. Noted for the central coin decision; NOT coined here.
4. Thin-talk allowance used: 3 signals, all practitioner-testimony (no external dated facts in the talk).
