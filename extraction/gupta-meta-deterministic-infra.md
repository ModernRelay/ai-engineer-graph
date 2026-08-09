# SPIKE extraction — "Deterministic Infra for Non-Deterministic AI Agents" (Nishant Gupta, Meta Superintelligence Labs) — FOR REVIEW

Source transcript: `transcripts/gupta-meta-deterministic-infra.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/APh1Vx0oLmQ — AI Engineer World's Fair, published 2026-06-29.
`stagingTimestamp` for the artifact and all signals: 2026-06-29 (publish date).
Entities marked **[registry]** are already in the shared registry — edges link to them, no new node defined here.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-gupta-deterministic-infra` | Deterministic Infra for Non-Deterministic AI Agents (Nishant Gupta, Meta Superintelligence Labs — AI Engineer World's Fair) | youtube | https://youtu.be/APh1Vx0oLmQ |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-nishant-gupta`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-nishant-gupta` | Nishant Gupta (software engineering tech lead, Meta Superintelligence Labs — training & inference infrastructure) | `AffiliatedWithCompany → co-meta` **[registry]** |

NOT the registry's `exp-sachin-gupta` (batches 3/5) — different person; new node coined deliberately.

## Companies (0 new)

- **[registry]** `co-meta` — reused. Meta Superintelligence Labs treated as a division of Meta, not a distinct company node (see Review notes).

## Elements (1 new, 1 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agentic-control-plane` | Agentic control plane | concept | infra | Emerging infrastructure layer for autonomous agents — scheduling, memory coordination, policy enforcement, evaluation, monitoring, workload routing — analogous to what Kubernetes was for containers and service meshes for microservices; "an operating system for autonomous AI" (paraphrase) |
| **[registry]** `el-generator-validator-separation` | — | — | — | reused; Gupta's central principle — model generates proposals, infrastructure validates, policy engine approves, execution gateway enforces ("the model suggests, the platform decides") — is this concept applied at the infra level |

Element edges: `el-agentic-control-plane` `IdentifiedInArtifact → ia-aie-gupta-deterministic-infra`, `ExemplifiesPattern → pat-harness-over-model` **[registry]**; `el-generator-validator-separation` `IdentifiedInArtifact → ia-aie-gupta-deterministic-infra`.

## Signals (3 new)

All: domain `infra`, `SpottedInArtifact → ia-aie-gupta-deterministic-infra`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-agent-infra-great-mismatch` | Meta infra tech lead: autonomous agents violate every core assumption of modern cloud infrastructure (short-lived requests, deterministic services, known execution paths, bounded failures) — agents are stateful, long-running, dynamically branching, and may execute different workflows for the same input. He names it "the great mismatch" (paraphrase); the majority of engineering effort moves below the model layer into orchestration, monitoring, safety evaluation, and recovery | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-meta` |
| `sig-infra-turns-mistakes-into-outages` | Production failure taxonomy from inside Meta and across industry: hallucinations are "often the least interesting failure mode" (paraphrase) — real incidents are recursive reasoning loops, workflow deadlocks, retry amplification (invalid tool call → slightly-different still-invalid retry → rising reasoning depth → exponential GPU/compute growth), context corruption, memory poisoning, cost explosions. The model makes a mistake; the infrastructure turns it into an outage | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-meta` |
| `sig-control-plane-next-frontier` | Prompts were the differentiator, then models — both "rapidly commoditizing" (paraphrase); the next frontier is reliability infrastructure. An agentic control plane (scheduling, memory coordination, policy enforcement, evaluation, workload routing) is emerging the way Kubernetes followed containers, and organizations that build this layer gain significant competitive advantage: "the future of AI won't be won by better prompts, it will be won by better systems" (paraphrase) | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-agentic-control-plane` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-model-proposes-platform-decides` | Never let the model directly control production systems: the model generates proposals; deterministic infrastructure validates them, a policy engine approves them, an execution gateway enforces them. Reliability becomes buildable on top of a probabilistic model precisely because the platform, not the model, holds authority | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-generator-validator-separation` **[registry]**, `ReliesOnElement → el-agentic-control-plane` |
| `ins-consistency-masquerades-as-reasoning` | Once multiple agents share state, classic distributed-systems pathologies appear — stale reads, conflicting updates, context drift, inconsistent views — and get misdiagnosed: "many multi-agent failures are consistency failures masquerading as reasoning failures" (paraphrase). Debugging blames the model when the fault is the memory layer, made harder because agent memory itself may be probabilistic and retrieval-based | `HighlightsPattern → pat-model-not-bottleneck` | — |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-gupta-deterministic-infra`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-adapt-distsys-reliability-patterns` | Treat agents as distributed systems; adapt proven reliability patterns | Circuit breakers → tool isolation; rate limits → agent limits; retries → controlled recovery; resource quotas → cost governance; observability → agent tracing that captures planning decisions, tool calls, memory lookups, and state transitions (the why, not just the what — logs alone make agent debugging nearly impossible); treat inference as a cluster-scheduling problem (bursty demand, minutes-long workflows, elastic GPU placement) rather than a pure model problem | `ReferencesElement → el-agentic-control-plane` |
| `how-humans-as-exception-handlers` | Design human supervision as permanent, not a temporary crutch | Humans become exception handlers: they review ambiguous situations and provide calibration signals; layer safety so each layer catches a different failure class — prompt-level controls, tool permissions, policy validation, human approvals, audit systems (defense in depth applied to autonomous AI); the goal is allocating human attention where it provides maximum value, not removing humans | — |

## Dropped

- Kubernetes / service-mesh references — analogies only (`el-kubernetes` exists in the registry but is purely rhetorical here; no edge).
- Memory poisoning, context corruption, workflow deadlocks as separate elements — failure-mode vocabulary, kept in `sig-infra-turns-mistakes-into-outages` prose.
- "Defense in depth" as an element — classical security principle invoked by analogy; carried in `how-humans-as-exception-handlers`.

## Review notes

1. **Meta Superintelligence Labs vs `co-meta`:** the conference listing bills the speaker as Meta Superintelligence Labs; the transcript says only "tech lead at Meta … building the training and inference infrastructure." Chose to reuse `co-meta` **[registry]** and treat MSL as a division, not a distinct node — the talk is about Meta-wide infra practice, not MSL-specific research. Flip to a distinct `co-meta-superintelligence-labs` at reconciliation if you want the corp/lab split (precedent: `co-google` vs `co-google-deepmind` kept separate).
2. **Different Gupta:** `exp-nishant-gupta` ≠ registry `exp-sachin-gupta`; artifact slug `ia-aie-gupta-deterministic-infra` shares the surname prefix with the other Gupta's `ia-aie-gupta-feature-flags` / `ia-aie-gupta-reviewdebt` but tails disambiguate.
3. **Pattern ledger (no coin):** the agentic-control-plane claim — long-running, stateful, minutes-scale agent workloads needing a new scheduling/recovery/state layer — is adjacent evidence for the UNCOINED `pat-durable-execution` candidate. Noted here without an edge; signals parked on `pat-model-not-bottleneck` / `pat-harness-over-model` per registry briefs.
4. Short talk (~1k words) with no dated external facts — all three signals are practitioner testimony / industry observation from a Meta infra lead, per the short-talk allowance.
