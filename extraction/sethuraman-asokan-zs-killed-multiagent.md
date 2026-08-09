# SPIKE extraction — "Why We Killed Our Multi-Agent Pipeline" (Subbiah Sethuraman & Abhilash Asokan, ZS Associates) — FOR REVIEW

Source transcript: `transcripts/sethuraman-asokan-zs-killed-multiagent.txt` (auto-captions — quotes are paraphrases, not verbatim; speaker names heavily garbled: "Suba"/"Ablash", "CS" for ZS).
Video: https://youtu.be/u6jJcIFDLE4 — AI Engineer World's Fair, published 2026-07-23.
`stagingTimestamp` for the artifact and all signals: 2026-07-23 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Post-mortem talk — the failure evidence is stated by the practitioners themselves.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-sethuraman-asokan-killed-multiagent` | Why We Killed Our Multi-Agent Pipeline (Subbiah Sethuraman & Abhilash Asokan, ZS Associates — AI Engineer World's Fair) | youtube | https://youtu.be/u6jJcIFDLE4 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-subbiah-sethuraman`; `ContributedByExpert → exp-abhilash-asokan`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-subbiah-sethuraman` | Subbiah Sethuraman (head of AI engineering, ZS Associates) | `AffiliatedWithCompany → co-zs-associates` |
| `exp-abhilash-asokan` | Abhilash Asokan (director of AI engineering, ZS Associates) | `AffiliatedWithCompany → co-zs-associates` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-zs-associates` | ZS Associates | developer | consulting/tech firm serving top pharma companies; appears here as builder of commercial-analytics agent systems. Enum has no "consultancy" — `developer` chosen (precedent: co-tng, co-evil-martians) |

Registry reuses (edges only): `co-anthropic`.

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-knowledge-graph-control-plane` | Knowledge graph as agent control plane | concept | context | Domain knowledge graph (entities: geography, payers, accounts, brands, KPI hierarchies and drive-relationships, built with domain experts) used not as a data-lookup layer but as the control plane/control surface for an investigating agent: the graph dictates what the agent may look at and which paths it may take; every edge is a hypothesis; the agent loop is entity → graph neighborhood → hypothesis → back to raw data → support/contradict → traverse, until root cause or hypothesis exhaustion. Bounds an otherwise combinatorial investigation space |
| `el-single-reasoner` | Single reasoning owner | concept | harness | One agent owns the end-to-end reasoning and judgment; sub-agents are spawned dynamically only for focused investigations (e.g., rep activity in one region) and return results — never reasoning. Parallelism is kept; distributed reasoning is removed. Derived from observing how Claude Code launches sub-agents |
| `el-zs-signal-queue` | Deterministic signal-detection pipeline | ops | data-eng | Automated statistical pipeline (methods + guardrails + thresholds + prioritization) that scans commercial-pharma data for KPI anomalies/trends and puts confirmed signals on a queue; the agent wakes only when a signal arrives — "the agent's job is to investigate, not to identify" |

Element edges: all three `IdentifiedInArtifact → ia-aie-sethuraman-asokan-killed-multiagent`; `el-knowledge-graph-control-plane` `EnablesPattern → pat-context-graphs`; `el-zs-signal-queue` `ExemplifiesPattern → pat-harness-over-model` (deterministic scaffolding doing what the LLM shouldn't); `el-single-reasoner` `UsesElement → el-claude-code` **[registry]** (pattern observed in and copied from Claude Code).

Registry element reuses (edges only): `el-claude-code`, `el-deterministic-agentic-split` (batch 1 — this talk's takeaway #2 restates it verbatim).

## Signals (4 new)

All: domain `harness` unless noted, `SpottedInArtifact → ia-aie-sethuraman-asokan-killed-multiagent`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | pattern edges | other edges |
|---|---|---|---|
| `sig-zs-multiagent-incoherence` | ZS built a per-analyst-step multi-agent pipeline for pharma commercial analytics (signal detection → source localization + driver attribution → synthesis, plus an orchestrator). Each agent derived the right local fact but the packet was incoherent — e.g., cause correctly identified as payer moving the drug to a lower tier, yet the recommended action was "send more sales reps": context lost at every handoff, no agent owning the end-to-end picture, no shared business-domain knowledge. "It's not the LLM which failed — it's the way we split the work" | `FormsPattern → pat-model-not-bottleneck` | `RelevantCompany → co-zs-associates` |
| `sig-zs-claude-code-reference-architecture` | Instead of redesigning topology/handoffs on the whiteboard, ZS opened an empty directory, gave Claude Code just bash + the database and a real signal, and watched it work — then derived the production architecture from observed behavior: consolidate to a single agent, turn repeated operations into tools, delegate focused investigations to dynamic sub-agents. "Don't introduce human/design constraints into architecture — let the architecture be derived" | `FormsPattern → pat-harness-over-model` | `OnElement → el-claude-code` **[registry]**, `el-single-reasoner`; `RelevantCompany → co-anthropic` **[registry]**, `co-zs-associates` |
| `sig-zs-deterministic-signal-detection` | An LLM had been deciding what counts as a signal — sometimes applying statistics, sometimes barely looking at the data, mistaking noise for signal. Fix: pull identification entirely out of the agentic system into a deterministic statistical pipeline (guardrails, thresholds, prioritization) feeding a queue that wakes the agent. Takeaway: complex workflows have deterministic and agentic parts — never let agents run the deterministic part | `FormsPattern → pat-harness-over-model` | `OnElement → el-zs-signal-queue`, `el-deterministic-agentic-split` **[registry]**; domain `data-eng` |
| `sig-zs-graph-control-plane` | The lighter architecture still failed on business context (agent inferred non-existent relationships from raw tables — not scalable), so ZS built a domain knowledge graph with in-house pharma experts and made it the agent's control plane: graph gates the where (source localization across region/territory/payer/account permutations) and the why (KPI drive-relationships); each edge is a hypothesis evaluated against actual data. Result: after 50+ turns the agent produces in ~20–30 minutes what an analyst produced in 3–4 weeks | `FormsPattern → pat-context-graphs` | `OnElement → el-knowledge-graph-control-plane`; `RelevantCompany → co-zs-associates`; domain `context` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-derive-architecture-from-agent` | Mimicking the human org chart (one agent per analyst step) is the anti-pattern: agent topology should be derived from observing what a capable agent naturally does with minimal tools, not from human role decomposition — judgment consolidates, investigation parallelizes | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-claude-code` **[registry]**, `el-single-reasoner` |
| `ins-graph-is-control-plane-not-lookup` | A knowledge graph's highest-leverage use for agents is not retrieval but control: encoding the hypothesis space as edges gives the agent a bounded, expert-validated investigation surface — the graph decides what the agent may consider next | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-knowledge-graph-control-plane` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-sethuraman-asokan-killed-multiagent`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-kill-your-multiagent` | Rebuilding a failed multi-agent pipeline | (1) Don't bake human/design constraints into architecture — let it be derived from observed agent behavior; (2) split deterministic from agentic work and never let agents run the deterministic part (statistics finds signals, agents investigate them); (3) exactly one agent owns end-to-end reasoning — it may spawn sub-agents/tools/skills for tasks, but judgment never distributes; (4) treat the knowledge graph as a control plane the agent navigates, not a lookup layer | `ReferencesElement → el-knowledge-graph-control-plane`, `el-deterministic-agentic-split` **[registry]**, `el-single-reasoner` |

## Dropped

- The four-step pharma analyst workflow (signal → root cause → action → outlook) and the 18%-prescription-drop example — illustration, folded into signals.
- TRX / KPI definitions — domain vocabulary, prose only.
- The orchestrator agent as a separate element — it's the thing that was killed; captured in `sig-zs-multiagent-incoherence`.

## Review notes

1. Multi-agent-orchestration failure is becoming a recurring corpus theme (this talk is the most explicit post-mortem yet) but there is no registry pattern for it; the incoherence signal is parked on `pat-model-not-bottleneck` (failure lives in the layer around the model). If a "multi-agent skepticism / consolidate-the-reasoner" candidate ever recurs, this file is its anchor data point.
2. `el-knowledge-graph-control-plane` — merge-check against `el-agentic-control-plane` (batch 8, Meta: infra control plane) and `el-learned-execution-graphs` (batch 10): related names, different claims (this one is a domain KG gating hypothesis traversal). Kept distinct; flag raised so seeding can decide.
3. Speaker names are from the official talk listing; captions render them "Suba" and "Ablash" and the company as both "ZS" and "CS". Other garbles: "farmers" = pharmas, "KPA"/"KPS" = KPI(s), "the agent's dope" = job, "how to find the bear" = likely "the where", "by the judgment to be distributed" = "we didn't want the judgment to be distributed".
4. The 3–4-weeks-to-20-minutes claim is practitioner testimony with no external verification; kept inside the signal brief rather than as a standalone quantitative claim.
