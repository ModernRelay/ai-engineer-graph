# SPIKE extraction — "Unlock Agent Autonomy: The Runtime for AI-Native Systems" (Tushar Jain, Docker) — FOR REVIEW

Source transcript: `transcripts/jain-docker-agent-runtime-autonomy.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/zaGyGgLW3SM — AI Engineer World's Fair, published 2026-08-20.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-20 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: Docker's thesis that **intelligence is no longer the blocker — safety is**, and that safety must live in a **runtime** that works across every model (multiple labs plus open models like GLM 5.2) and every harness (Claude Code, Codex, OpenClaw-style agents for sales/marketing, your own). Three pillars — containment (agent inside the untrusted VM boundary, controls outside), scoped access (just-in-time tools composed over MCP, scoped sub-sandboxes per task), intent-based access (a control layer decides what access a goal-expanding agent may get) — plus the runtime must follow the work everywhere. Demo: **spx**, a new microVM runtime CLI (`brew install spx`) running Codex/Claude Code with injected credentials, network policy, local→cloud portability, fan-out and orchestration, and a prototype of intent-based delegation into scoped sub-sandboxes. Caption garbles: "codeex" → **Codex**, "Slack MCB" → **Slack MCP**, "open claw" → **OpenClaw**, "paypin.com" → an example exfil domain, "D-cloud" → a `--cloud` flag, "kit/scale" → **skill**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-jain-docker-agent-runtime-autonomy` | Unlock Agent Autonomy: The Runtime for AI-Native Systems (Tushar Jain, Docker — AI Engineer World's Fair) | youtube | https://youtu.be/zaGyGgLW3SM |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-tushar-jain`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-tushar-jain` | Tushar Jain (Docker) | `AffiliatedWithCompany → co-docker` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-docker` | Docker | developer | Container platform company; "what Docker solved the last decade is portability" — now repositioning that runtime experience toward **agent safety**: a new microVM technology (spx) with MCP, policy and governance layers, running across Windows/Mac/Linux/cloud/VPC |

Reused **[registry]**, edge-only: `co-anthropic` **[seed]** (Claude Code as a supported harness; Anthropic API as a scoped credential), `co-openai` **[registry]** (Codex), `co-zhipu-ai` **[registry]** (GLM 5.2 as the open-model progress cited). Referenced, not coined: OpenCode, Notion (MCP in the demo).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-goal-expansion-crosses-trust-boundaries` | Goal expansion crosses trust boundaries | concept | security | A nightly report agent that had run fine for weeks one day posted the manager's private report as a PR — "nothing changed, the model decided to be helpful." The harder case: an agent investigating a latency spike reasonably asks for another service's logs, then GitHub to read commits, then Slack for chatter — each step expands the goal and crosses a trust boundary until the agent "has access to everything at the same time" and anything becomes a blast-radius vector. Traditional software had static permissions; an autonomous agent's needed access **changes at runtime**, and "we haven't truly solved" how to grant exactly that safely |
| `el-cross-model-cross-harness-safety` | Safety independent of model and harness | concept | security | You cannot rely on the next frontier model not making a mistake: everyone will use models from several labs and open models (GLM 5.2 "amazing progress the last few weeks"), for privacy and cost; and several harnesses — betting on one lab's harness limits model choice, and the OpenClaw moment means sales and marketing "claws," plus your own. So the constraint must be in the environment around the agent, at a layer beneath all models and harnesses |
| `el-safety-runtime-three-pillars` | The safety runtime: containment, scoped access, intent-based access | concept | security | **Containment** — a sandbox where the agent runs *inside* the untrusted VM boundary and controls run *outside* it (more than "throw a rock and hit a sandbox company"). **Scoped access** — beyond network and tool allowlists: just-in-time tools composed over existing MCP tools but restricted to the task (e.g. only the Slack conversations about this incident), run in a scoped sub-sandbox for that task rather than one big sandbox accreting capabilities. **Intent-based access** — decide what access a request should get from the user's/task's intent and context, deny or escalate to a human what the intent doesn't justify (read Slack for the incident: yes; suddenly wants email: no), at a control layer independent of the model or harness. "A hard problem, not fully solved yet" |
| `el-spx` | spx (Docker's microVM agent runtime) | product | infra | `brew install spx`: spins up Claude Code, Codex, OpenCode or any agent in a microVM sandbox with **credentials injected as stubs** (the agent sees GitHub/Codex creds but they aren't real), network policy, and MCP control, on Windows, Mac, Linux and cloud. Demo: a PR-review sandbox with only GitHub + Anthropic access and a separate Notion-only sandbox for write-up; the identical sandbox re-run in the cloud with the same policies; a script fanning out six PR reviews in parallel sandboxes; an orchestrator composing the scoped bots on a schedule; and a prototype where a network-blocked agent asks the runtime, which judges the intent ("review this PR") and delegates into a scoped sub-sandbox with GitHub access — while an exfil request would be rejected |
| `el-runtime-follows-the-work` | The runtime follows the work | concept | infra | Safety alone isn't enough; the runtime must be omnipresent — laptop, cloud, cross-cloud orchestration, your VPC, the customer's VPC — "connected by a fabric so you can move agents up and down." Docker's portability lineage applied to safety: the same sandbox, policy plane and controls travel with the workload |

Element edges: all five `IdentifiedInArtifact → ia-aie-jain-docker-agent-runtime-autonomy`.
`el-spx` `DevelopedByCompany → co-docker`;
`el-spx` `UsesElement → el-safety-runtime-three-pillars`, `el-runtime-follows-the-work`, `el-microvm` **[registry]**, `el-mcp` **[seed]**, `el-claude-code` **[registry]**, `el-codex` **[registry]**;
`el-safety-runtime-three-pillars` `UsesElement → el-goal-expansion-crosses-trust-boundaries`, `el-cross-model-cross-harness-safety`, `el-agent-scoped-authorization` **[registry]**, `el-lethal-trifecta` **[registry]**;
`el-cross-model-cross-harness-safety` `UsesElement → el-openclaw` **[registry]**, `el-glm-52` **[registry]**;
`el-spx` `ExemplifiesPattern → pat-durable-execution` **[registry]**;
`el-safety-runtime-three-pillars` `ExemplifiesPattern → pat-new-cyber-threats` **[registry]**;
`el-cross-model-cross-harness-safety` `EnablesPattern → pat-harness-over-model` **[registry]**.

Reused elements (no new nodes): `el-microvm` **[registry]**, `el-mcp` **[seed]**, `el-claude-code` **[registry]**, `el-codex` **[registry]**, `el-openclaw` **[registry]**, `el-glm-52` **[registry]**, `el-agent-scoped-authorization` **[registry]**, `el-lethal-trifecta` **[registry]**.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-jain-docker-agent-runtime-autonomy`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-docker`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-safety-not-intelligence-is-the-next-blocker` | security | Docker's framing of the moment: two years were spent making agents intelligent and "I think we're almost there"; the next challenge "is harder and more important — how to make them safe. Intelligence is not the next big blocker to leveraging agents; it is how to give them all the access and autonomy they need safely." The question moves from *can it* to *should it, and how do we give it that access* | `FormsPattern → pat-model-not-bottleneck` **[registry]**; `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-safety-runtime-three-pillars`, `el-goal-expansion-crosses-trust-boundaries` |
| `sig-goal-expansion-is-the-new-trust-problem` | security | Agents "increase and change the goal" — to be helpful, by confusion, or by injection — and each reasonable step (logs → GitHub → Slack) crosses a trust boundary until the agent holds everything. Static permissions assumed deterministic software; an autonomous agent's required access changes at runtime, and granting exactly that, safely and correctly, is the unsolved problem beneath autonomy | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-goal-expansion-crosses-trust-boundaries`, `el-lethal-trifecta` **[registry]** |
| `sig-safety-runtime-below-every-model-and-harness` | security | Because no one will bet everything on one lab or one harness — multiple frontier labs, open models like GLM 5.2, Claude Code/Codex/OpenClaw-style agents for non-coding roles, custom harnesses — safety can't depend on the model being good or the harness being one vendor's. It has to be a runtime that every agent runs on, with containment, scoped capabilities and intent-based access enforced at the control layer regardless of what runs inside | `FormsPattern → pat-harness-over-model` **[registry]**; `FormsPattern → pat-durable-execution` **[registry]** | `OnElement → el-cross-model-cross-harness-safety`, `el-safety-runtime-three-pillars` |
| `sig-docker-pivots-portability-to-agent-safety` | infra | The company that solved laptop-to-cloud portability builds a new microVM runtime (spx) for agent safety: credentials injected as stubs the agent can't read, network policy and MCP control, per-task scoped sandboxes (GitHub-only for review, Notion-only for write-up), the same sandbox and policies portable to the cloud, parallel fan-out and scheduled orchestration. A runtime vendor productizing the "model never sees secrets" boundary | `FormsPattern → pat-durable-execution` **[registry]**; `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-spx`, `el-runtime-follows-the-work`, `el-microvm` **[registry]** |
| `sig-intent-based-access-is-unsolved` | security | The honest boundary: scoped sub-sandboxes work manually, and the prototype where a blocked agent asks the runtime to judge its intent and delegate into a GitHub-scoped sub-sandbox (rejecting an exfil) "is not built yet." Deciding what access an evolving task should get — from intent and context, independent of the model — is the remaining problem, and the judgment sits outside the agent | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-safety-runtime-three-pillars`, `el-spx` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-the-runtime-is-where-safety-lives` | The durable architectural claim: with model and harness both plural and swappable, the only layer that can be relied on for safety is the one beneath them — a runtime that contains, scopes and judges — and it must travel with the work (local, cloud, VPC). This is the durable-execution layer described from a safety-first vendor: the same sandbox/policy plane that makes agents portable is what makes them containable | `HighlightsPattern → pat-durable-execution` **[registry]** | `ReliesOnElement → el-safety-runtime-three-pillars`, `el-runtime-follows-the-work`, `el-spx` |
| `ins-autonomy-is-gated-by-containment-not-capability` | "Intelligence is not the blocker" from a runtime vendor is a `pat-model-not-bottleneck` claim with a specific bottleneck named: the inability to grant runtime-changing access safely. Autonomy expands exactly as far as containment, scoping and intent judgment allow — which is why the demo's manual scoped sandboxes exist today and the automatic intent-based delegation is still a prototype | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-goal-expansion-crosses-trust-boundaries`, `el-cross-model-cross-harness-safety` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-jain-docker-agent-runtime-autonomy`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-run-agents-in-a-safety-runtime` | Contain, scope, judge — independent of model and harness | Assume goals will expand (helpfulness, confusion, injection) and that the needed access changes at runtime; never rely on the model or a single vendor's harness for safety — design for many models (including open ones) and many harnesses; run the agent **inside** an untrusted VM boundary with controls **outside** it; inject credentials as stubs so the agent never holds real secrets, and apply network policy and MCP control at the boundary; instead of one sandbox accreting capabilities, **break work into tasks across security boundaries** and run each in a scoped sub-sandbox with just-in-time tools composed over existing MCP tools but restricted to the task; decide additional access from the user's or task's **intent** at a control layer, denying or escalating what the intent doesn't justify; make the runtime follow the work — the same sandbox and policies locally, in the cloud, in your or the customer's VPC — and use that portability for fan-out and orchestration | `ReferencesElement → el-safety-runtime-three-pillars`, `el-spx`, `el-runtime-follows-the-work`, `el-goal-expansion-crosses-trust-boundaries`, `el-cross-model-cross-harness-safety` |

## Dropped

- **Demo mechanics** (joke prompt, "are you on the cloud or a Mac?", the six-PR script) — folded into `el-spx`.
- **"Throw a rock and find many sandbox companies"** — the competitive aside, kept as a phrase.

## Review notes

1. **⚑ Third product-side `pat-durable-execution` point in the batch** (Navan runtime map, Warp Oz, Docker spx) — the "runtime below the harness" layer is now vendor-crowded in a single week; the pattern's product-as-layer claim is well past 6 support.
2. **`sig-safety-not-intelligence-is-the-next-blocker`** is the batch's most direct `pat-model-not-bottleneck` statement from an infrastructure incumbent, with the bottleneck named (safe runtime access). Pairs with Malhotra/Anthropic and Aggarwal/Decawork for the "guard outside the agent" cluster.
3. **`el-spx`** — a product node from a keynote-adjacent demo; the credential-stub injection is the sixth "model never sees secrets" arrival in the corpus. Verify the name and `brew install spx` before seeding.
4. **⚠ Verify before seeding:** "GLM 5.2," the OpenClaw reference, and that intent-based delegation is prototype-only.
