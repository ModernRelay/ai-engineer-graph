# SPIKE extraction — "Why Your Enterprise Tech Stack Isn't Ready for AI Agents" (Christopher Lovejoy, Anthropic & Saul Howard, Anterior) — FOR REVIEW

Source transcript: `transcripts/lovejoy-howard-enterprise-stack-not-ready.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/mav15aW9lLM — AI Engineer World's Fair (healthcare / AI-native enterprise track), published 2026-08-19.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-19 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a forward-deployed engineer at Anthropic (previously at Anterior) and Anterior's VP of engineering on the **enterprise PoC trap** in regulated industries: a four-week proof of concept hits its metrics, everyone assumes the hard part is done, and the next-day meeting asks for the audit trail, the PHI data lifecycle, who approves decisions, and how you know it still performs. Their primitives: an **immutable action ledger** (event-sourced, auditability falls out), **orchestration-adjacent schema-driven object storage** (PHI separated from the event stream; zero-trust tokens at point of use; defeats the lethal trifecta by construction), **human–agent equivalency** (any action an LLM takes a human can take; escalation anywhere), and **evals as an emergent property** of those three. Build from production constraints back to PoC accuracy, not the reverse. Caption garbles: "for deployed engineer" → **forward-deployed engineer**, "Aentic" → **agentic**, "PC"/"P" → **PoC**, "SOCK 2"/"High Trust"/"HIPPA" → **SOC 2 / HITRUST / HIPAA**, "rback" → **RBAC**, "on-rem" → **on-prem**, "LMS" → **LLMs**, "Sol" → **Saul**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-lovejoy-howard-enterprise-stack-not-ready` | Why Your Enterprise Tech Stack Isn't Ready for AI Agents (Christopher Lovejoy, Anthropic & Saul Howard, Anterior — AI Engineer World's Fair) | youtube | https://youtu.be/mav15aW9lLM |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-christopher-lovejoy`, `exp-saul-howard`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-christopher-lovejoy` | Christopher Lovejoy (Member of Technical Staff / forward-deployed engineer, Anthropic; ex-Anterior) | `AffiliatedWithCompany → co-anthropic` **[seed]**, `co-anterior` |
| `exp-saul-howard` | Saul Howard (VP Engineering, Anterior) | `AffiliatedWithCompany → co-anterior` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-anterior` | Anterior | developer | New York company selling agentic AI to US health insurers; the architectural primitives in the talk come from building there (and generalize to finance, defense, government) |

Reused **[seed]**, edge-only: `co-anthropic` — new fact: employs forward-deployed engineers who "embed within enterprise organizations and help them get value from AI agents" (Lovejoy). Referenced, not coined: Epic, Salesforce (integration targets), Datadog (the "developer log" an audit trail is not).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-enterprise-poc-trap` | The enterprise PoC trap | concept | | Scope a priority use case with a large health system, define the metrics, four weeks of build, the AI hits the numbers, the CFO asks about next year's budget, the CMO wants to tell colleagues, sales asks when "powered by AI" goes on the website — "everyone assumes the hard part is done." The next-day productionization meeting: *can I see the audit trail? how is sensitive data handled and where can it go? who approves the decisions — we must escalate to a clinician? can untrusted data manipulate the model? how do we know it keeps performing? how does it connect to Epic and Salesforce?* Bolting these onto the PoC yields "something very brittle, hard to externalize or generalize"; the fix is to take production constraints as the architectural principles from day one and build back up to PoC accuracy on the new primitives |
| `el-immutable-action-ledger` | The immutable action ledger | technology | harness | For SOC 2 / HITRUST / HIPAA an audit trail is not a developer log: a *complete* record of every action the agent took, every data access, every authorization — "if the agent's decision came up in a court of law, could we show a justifiable chain of evidence?" Architecture choice: decide what you want to be *easy*. An append-only, timestamped, **unified** transaction log as the single source of truth across all parallel agents makes auditability "fall out of your storage paradigm — it's impossible not to be able to roll back time." Trade-off (event sourcing): writes trivial, reads require replay (mitigated by snapshots/caching); views are ephemeral projections, which healthcare wants anyway when later events change the interpretation of a journey |
| `el-orchestration-adjacent-object-storage` | Orchestration-adjacent, schema-driven object storage | technology | security | PHI is complex, mixed structured/unstructured, often >1 MB per record, under strict RBAC, and sometimes not allowed to leave the customer's VPC. So the events hold only **references** to schema-driven, immutably stored blobs; the data lives separately from the orchestration stream. Benefits: developers debug and retrace an agent's steps *without* PHI access (they see the schema, not the data); **zero trust** — agents bear tokens and fetch data at the point of use rather than letting it flow around; and a constructive mitigation of the lethal trifecta — "if the agent at point A has this data, can it also access data over here?" becomes a constraint the architecture answers with no |
| `el-human-agent-equivalency` | Human–agent equivalency | concept | harness | Escalation is dynamic (the agent escalates when unsure, or a rule fires above a treatment threshold) and humans and LLMs consume context differently. So the platform enforces a wider definition of "agent" covering both: **any action an LLM can take, a human can take**, at any point in the chain, and downstream steps don't care who did the upstream ones. A shared context definition maps into an agent-friendly prompt or a human-friendly UI |
| `el-evals-as-emergent-property` | Evals as an emergent property | concept | harness | Evals are hard: non-determinism makes it tricky to pin the change that moved an output, offline datasets may not represent production, and data drifts. The three primitives give **privacy-preserving evals as a byproduct**: the ledger lets you replay any point in time and tweak a prompt, model or code to see the exact impact; human–agent equivalency means the human's and the agent's performance on the same task *is* the eval; object storage lets evals run on production data inside the customer's environment without the sensitive data ever leaving. "Eval emerges as a first-class property of the system rather than something bolted on" |

Element edges: all five `IdentifiedInArtifact → ia-aie-lovejoy-howard-enterprise-stack-not-ready`.
`el-immutable-action-ledger` `UsesElement → el-durable-session-log` **[registry]**, `el-agent-checkpoint-replay` **[registry]**;
`el-orchestration-adjacent-object-storage` `UsesElement → el-immutable-action-ledger`, `el-lethal-trifecta` **[registry]**, `el-agent-scoped-authorization` **[registry]**;
`el-evals-as-emergent-property` `UsesElement → el-immutable-action-ledger`, `el-orchestration-adjacent-object-storage`, `el-human-agent-equivalency`;
`el-enterprise-poc-trap` `UsesElement → el-immutable-action-ledger`;
`el-immutable-action-ledger` `ExemplifiesPattern → pat-durable-execution` **[registry]**;
`el-orchestration-adjacent-object-storage` `ExemplifiesPattern → pat-new-cyber-threats` **[registry]**;
`el-evals-as-emergent-property` `EnablesPattern → pat-verification-gap` **[registry]**;
`el-enterprise-poc-trap` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**.

Reused elements (no new nodes): `el-durable-session-log` **[registry]**, `el-agent-checkpoint-replay` **[registry]**, `el-lethal-trifecta` **[registry]**, `el-agent-scoped-authorization` **[registry]**, `el-forward-deployed-engineering` **[registry]** (Lovejoy's role — see note 3).

## Signals (6 new)

All: `SpottedInArtifact → ia-aie-lovejoy-howard-enterprise-stack-not-ready`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-anterior`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-poc-accuracy-is-not-the-hard-part` | | The regulated-enterprise version of "the demo isn't production": a four-week PoC hits its accuracy, speed and cost targets and every stakeholder assumes the hard part is done — then compliance asks for the audit trail, the data lifecycle, the approval mechanism and the drift story, none of which the PoC's ad-hoc integrations can answer. "Where I've seen it go wrong is taking the point solution and strapping the enterprise requirements on as you meet them" | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-enterprise-poc-trap` |
| `sig-audit-trail-means-a-complete-action-ledger` | harness | An audit trail under SOC 2 / HITRUST / HIPAA is a court-grade chain of evidence — every action, data access and authorization — and the way to make it trivial is architectural: an append-only, unified transaction log as the source of truth for all agents, from which auditability, time travel and reinterpretation "fall out" (event sourcing's write-easy/read-hard trade-off accepted deliberately) | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-durable-execution` **[registry]** | `OnElement → el-immutable-action-ledger`, `el-durable-session-log` **[registry]** |
| `sig-separating-data-from-orchestration-defeats-the-trifecta` | security | Keeping PHI in schema-driven immutable object storage that events only reference — with zero-trust tokens fetched at point of use and data allowed to stay in the customer's VPC — lets developers observe and debug agents without seeing the data, and turns the lethal-trifecta question ("can the agent holding this data also reach that data?") into a constraint the architecture answers by construction rather than a guardrail | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-orchestration-adjacent-object-storage`, `el-lethal-trifecta` **[registry]** |
| `sig-any-action-an-agent-takes-a-human-can-take` | harness | Because escalation is dynamic and humans and LLMs read context differently, the platform defines "agent" to include humans: any action an LLM can take, a human can take at any point in the chain, with downstream steps indifferent to who acted, and a shared context definition rendered as prompt or UI. Escalation to a clinician stops being a special path and becomes a property of the workflow model | `FormsPattern → pat-ai-native-org` **[registry]**; `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-human-agent-equivalency` |
| `sig-evals-fall-out-of-the-architecture` | harness | Offline eval sets misrepresent production and drift; non-determinism hides which change moved an output. With the ledger (replay any moment, tweak prompt/model/code, see the exact effect), human–agent equivalency (the human's result on the same task is the eval) and in-VPC object storage (evals on production data without exposing it), privacy-preserving evals emerge "as a first-class property rather than something you attach on the side" | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-benchmark-trust-crisis` **[registry]** | `OnElement → el-evals-as-emergent-property`, `el-agent-checkpoint-replay` **[registry]** |
| `sig-anthropic-fde-embedded-in-enterprises` | | A speaker introducing himself as an Anthropic forward-deployed engineer who "embeds within enterprise organizations and helps them get value from AI agents" — with an enterprise-architecture talk, not a model talk. The lab's own FDE function presenting production primitives is a data point for the corpus's uncoined rise-of-FDE thesis | | `OnElement → el-forward-deployed-engineering` **[registry]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-build-from-constraints-not-from-the-poc` | The durable meta-claim is a design order: in regulated enterprises, take the production constraints (audit, data boundaries, approvals, evals) as the architectural principles first and build back up to the PoC's accuracy — because the constraints are what make the system generalize across use cases, and the accuracy is the easy part. Patterns that already exist in finance and defense (transaction logs, object storage, zero trust) cover most of it; AI adds the need to combine them | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-enterprise-poc-trap`, `el-immutable-action-ledger`, `el-orchestration-adjacent-object-storage` |
| `ins-the-ledger-makes-audit-replay-and-evals-one-thing` | Three enterprise demands that are usually three bolt-ons — auditability, debuggability/replay, and evals — collapse into one primitive once actions live in an immutable event log with data referenced from separate immutable storage: the same log answers "what did the agent do and why," "what if we change the prompt," and "how does it compare to the clinician," without the data leaving the customer. Verification becomes a storage decision | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-immutable-action-ledger`, `el-evals-as-emergent-property`, `el-human-agent-equivalency` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-lovejoy-howard-enterprise-stack-not-ready`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-architect-agents-for-regulated-enterprises` | Four primitives, chosen from the constraints | Before the PoC, list the production questions compliance will ask (audit trail, data lifecycle, approvals, injection, drift, integrations) and pick what you want to be *easy*; keep an **append-only, unified, timestamped action ledger** as the single source of truth for all agents so audit and time travel fall out — accept write-easy/read-hard and use snapshots; store sensitive data in **schema-driven immutable object storage** that events only reference, so developers debug without seeing PHI, agents fetch with **zero-trust tokens at point of use**, and data can stay in the customer's VPC — and use that separation to answer the lethal-trifecta question by construction; define "agent" to include humans so **any action an LLM can take a human can take** at any point, with a shared context rendered as prompt or UI; get **evals for free** by replaying the ledger with changed prompts/models/code, comparing human vs agent on the same task, and running on production data in-environment; and build back up from these primitives to the PoC's accuracy rather than bolting them onto the PoC | `ReferencesElement → el-enterprise-poc-trap`, `el-immutable-action-ledger`, `el-orchestration-adjacent-object-storage`, `el-human-agent-equivalency`, `el-evals-as-emergent-property` |

## Dropped

- **The two deferred questions** (untrusted data manipulating the model; integrations to Epic/Salesforce) — explicitly parked by the speakers.
- **The enterprise stack diagram** (application / control plane / data plane / model provider) — folded into `el-enterprise-poc-trap`.

## Review notes

1. **⚑ Cross-batch echo: the immutable ledger.** Louf/.txt (append-only causal event log), Lovejoy/Howard (event-sourced action ledger), Malhotra/Anthropic (proxy-stamped audit rows), Buykin/Maersk (trace as shared evidence) — four same-batch instances of *the log is the system of record for agent behavior*. Consider widening `el-durable-session-log` / `el-flat-trace-log` at review rather than new nodes.
2. **`el-orchestration-adjacent-object-storage`** is a constructive lethal-trifecta mitigation (data-plane separation) distinct from the runtime/proxy approaches elsewhere in the batch; recommend citing alongside them in `pat-new-cyber-threats`.
3. **`sig-anthropic-fde-embedded-in-enterprises` is held pattern-less for the uncoined `pat-fde-rise` ledger** — a first-person Anthropic FDE on the enterprise stage. Adds to the coin case.
4. **⚠ Verify before seeding:** Lovejoy's exact title, the ">1 MB per record" figure, and that Anterior's customers are US health insurers (as stated).
5. **Domain empty on the PoC and FDE signals** (leadership-track content); others carry `harness`/`security`.
