# SPIKE extraction — "Your LLM Stack Is a 2008 Database With Better Marketing" (Lovina Dmello, NVIDIA) — FOR REVIEW

Source transcript: `transcripts/dmello-nvidia-llm-stack-2008-database.txt` (auto-captions — quotes are paraphrases; "Lavina D'Mello" = Lovina Dmello per talk listing; "2028 playbook" = 2008 playbook).
Published 2026-07-20 on the AI Engineer channel (World's Fair). `stagingTimestamp` for all nodes: 2026-07-20.
Entities marked **[registry]** already exist — edges link to them, no new node.

---

## InformationArtifact

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-dmello-llm-stack` | Your LLM Stack Is a 2008 Database With Better Marketing (Lovina Dmello, NVIDIA — AI Engineer World's Fair) | youtube | https://youtu.be/XjI-AR4pt7Y |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-lovina-dmello`.

## Experts (1 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-lovina-dmello` | Lovina Dmello (Senior Software Developer, NVIDIA deep learning infrastructure) | `co-nvidia` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-nvidia` | NVIDIA | hardware | Speaker affiliation; deep learning infrastructure team |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-ray` | Ray | framework | infra | Popular distributed-compute framework for ML workloads; authentication was off by default, which produced the 2023 open-cluster exposure |
| `el-nist-ai-rmf` | NIST AI Risk Management Framework | framework | security | US NIST framework for AI risk; used here as the mapping target for a 4-level ML-security maturity model with per-level overhead budgets |

Element edges: `el-ray` IdentifiedInArtifact → `ia-aie-dmello-llm-stack`; `el-nist-ai-rmf` IdentifiedInArtifact → `ia-aie-dmello-llm-stack`.

## Patterns (1 NEW — the batch's one new pattern, defined here)

| slug | name | kind | brief |
|---|---|---|---|
| `pat-model-not-bottleneck` | The Model Is Not the Bottleneck | dynamic | The models are good enough; production failure and value have migrated to the layers around them — and the industry is now productizing that periphery. Evidence keeps arriving from independent directions: real ML security breaches are 2008-style infrastructure misconfigurations, not exotic adversarial attacks (78% of audited production setups had a critical mistake; thousands of Ray clusters open because a default was never flipped); agent "inconsistency" traces to label ambiguity and missing context, not model stochasticity; raw model output only becomes product through a typed rendering layer (Google's A2UI open spec); autonomous cross-org agent work is blocked on transaction/trust infrastructure, not tool count. The recurring practitioner refrain is literal: "the model was fine" / "stop blaming your model" / "not a model problem." Consequence: budgets, standards (NIST AI RMF mappings, A2UI), and startups concentrate on the unglamorous surrounding layers — configuration, delivery, memory, receipts — where the 2008 playbook was never re-applied. |

Pattern↔Pattern (proposed, flag for review): `pat-model-not-bottleneck` DrivesPattern → `pat-verification-gap` — once generation is good enough, the surrounding trust/verification layers become where the work and the value are; the verification gap is the sharpest instance of the periphery lagging the model.

This talk is the pattern's strongest evidencer; the Lin (`ia-aie-lin-agent-consistency`), Ramdoss (`ia-aie-ramdoss-rendering-layer`), and Povilionis (`ia-aie-povilionis-receipts`) extractions link to it from their own angles.

## Signals (3 new)

All: domain `security`, `SpottedInArtifact → ia-aie-dmello-llm-stack`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-ray-open-clusters-2023` | 2023: security researchers found thousands of Ray ML clusters sitting open on the internet — dashboards and job APIs exposed because authentication was off by default and nobody turned it on; estimated exposure over $1B. Not a zero-day, not a clever neural-network attack — a default setting | `pat-model-not-bottleneck`; **ContradictsPattern** → `pat-new-cyber-threats` | OnElement → `el-ray` |
| `sig-prod-ml-audit-78pct` | Researchers audited 50 real production ML setups: 78% had at least one critical security mistake, with the same three recurring — access controls left wide open (any account can do almost anything), no separation between system parts, and credentials/trained model weights sitting in storage anyone could reach | `pat-model-not-bottleneck` | — |
| `sig-security-control-overhead` | Measured cost of ML security controls in latency/throughput: basics (auth, input checking) <~8% — always on; heavy workload isolation 10–20% — selective; real-time malicious-input detection 15–30% — a non-starter on every request. SLA cost, not defense novelty, decides what survives to production | `pat-model-not-bottleneck` | — |

> `sig-ray-open-clusters-2023`'s ContradictsPattern edge is deliberate: the
> talk's core claim is that what's actually breaking is NOT the novel-AI-attack
> story `pat-new-cyber-threats` tells. First use of ContradictsPattern in the
> graph — confirm you want it.

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-2008-playbook-gap` | Moving to ML changed everything about the stack — probabilistic behavior ("correct is a distribution"), copyable weights leaking through the serving API, shared multi-tenant GPUs, prompts as control flow — but nobody changed the security assumptions: we run a 2008 playbook on a 2026 system. The fix is the boring one: secure the LLM stack like a database — lock down access, segment the network, protect data at rest | `pat-model-not-bottleneck` | — |
| `ins-deployability-is-frontier` | The field has enough defenses; it needs deployable ones. The frontier isn't a new attack-defense pair but making existing controls run at production overhead — an engineering problem. Research defends against invisible pixel tweaks while reality loses to stolen passwords and over-privileged accounts, and expertise silos (security doesn't speak ML, ML doesn't speak security, ops knows neither) leave the gap unowned | `pat-model-not-bottleneck` | — |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-dmello-llm-stack`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-ml-security-maturity-model` | Locate yourself honestly on a maturity model, then climb on purpose | Map to NIST AI RMF with overhead budgets per level: L1 <5% = bare basics, test-only; L2 5–10% = production minimum (proper logins, encryption, network separation, basic monitoring); L3 = advanced controls for regulated industries (healthcare, finance); most teams believe they're L3 but sit at L1–2; run cheap controls everywhere, reserve expensive ones (real-time input detection, heavy isolation) for sensitive/untrusted workloads | `el-nist-ai-rmf` |
| `how-fix-three-misconfigs` | Fix the three misconfigurations behind most ML breaches first | (1) Default full-admin accounts + never-expiring credentials → least privilege per account, fast credential expiry; (2) flat networks → wall system parts from each other and require verified service identity, not mere network reachability; (3) hardcoded passwords + model files in open storage → proper secret manager, encryption, automated scanning before anything ships | — |

## Dropped

- Emerging-threat watch list (prompt injection, RAG poisoning, GPU side-channels, model supply chain) — speaker explicitly framed it as "direction, not gospel"; undated speculation, no signal.
- Four-pillar defense-in-depth map and six-threat-category taxonomy — framing devices; substance folded into insights/knowhows.
- "Well-built vs sloppy control can double response time" — folded into `sig-security-control-overhead`.

## Review notes

1. **This file defines the batch's ONE new pattern** (`pat-model-not-bottleneck`). Four of the five batch-2 talks independently voice it; if you'd rather not coin it, the fallback homes are weak (these signals don't form `pat-verification-gap` or `pat-new-cyber-threats`).
2. The 50-setup audit and overhead numbers are research the speaker aggregates without naming sources — provenance is the talk only.
3. Ray incident date (2023) predates the batch; keep `stagingTimestamp` 2026-07-20 (artifact date) unless you want incident dates, per the batch-1 open question.
