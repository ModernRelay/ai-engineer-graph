# SPIKE extraction — "Privacy-Preserving Intelligence" (Steve Korshakov, Bee / Amazon) — FOR REVIEW

Source transcript: `transcripts/korshakov-bee-privacy-intelligence.txt` (auto-captions — quotes are paraphrases; "six store" = Sigstore, "confidation compute" = confidential compute, "at the station" = attestation).
Published 2026-07-20 on the AI Engineer channel (World's Fair). `stagingTimestamp`: 2026-07-20.
Registry reuse marked **[registry]**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-korshakov-privacy` | Privacy-Preserving Intelligence (Steve Korshakov, Bee/Amazon, AI Engineer World's Fair security track) | youtube | https://youtu.be/IvE8n-ylFYY |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-steve-korshakov`.

## Experts (1 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-steve-korshakov` | Steve Korshakov (Bee, now Amazon; ex-Telegram) | `co-bee`, `co-amazon` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-amazon` | Amazon | bigtech | acquirer of Bee (~late 2025); also referenced from the Johner file as Firecracker's developer |
| `co-bee` | Bee | developer | AI-wearable / personal-agent startup; acquired by Amazon ~8 months before the talk (≈Nov 2025) |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-bee` | Bee wearable + personal agent | product | context | Always-on wrist microphone that records everything and builds a personal agent over a stateful, persistent-memory runtime; captured data is user-extractable into other systems/agents; backend is provider-blind (Amazon cannot read it) |
| `el-sigstore` | Sigstore | technology | security | Public transparency log / signing infrastructure (OpenSSF); Bee anchors workload attestation in it so anyone can verify a deployed workload is genuine |
| `el-confidential-computing` | Confidential computing | technology | security | TEE-based encrypted-in-use compute; Bee replicates device-held keys only to attested confidential-compute nodes and runs its own inference inside the perimeter because unencrypted data may never leave it |

Element edges: `el-bee` `DevelopedByCompany → co-bee`, `UsesElement → el-sigstore`, `UsesElement → el-confidential-computing`; `el-bee` `ExemplifiesPattern → pat-context-graphs` **[registry]**.

## Signals (3 new)

All: SpottedInArtifact → `ia-aie-korshakov-privacy`, SourcedFromSource → `source-aie-yt`.

| slug | name / brief | domain | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-bee-capture-scale` | Bee telemetry: one wearer captures ~10M tokens/year of ambient conversation, and within the first week users say things sensitive enough to "learn virtually everything" about them — possibly the most sensitive capture device on the market; acquired by Amazon ≈Nov 2025 | context | pat-context-graphs **[registry]** | co-amazon, co-bee |
| `sig-provider-blind-backend-shipped` | Bee/Amazon shipped a production personal-agent backend its own operator cannot read: keys generated and persisted only on the customer phone, no encryption opt-out, workload attestation against Sigstore, keys replicated only to attested confidential-compute nodes running Bee's own inference, 7-day forced in-memory key expiry, TCB of ~20k lines of memory-safe code, release-signing keys held by a separate internal team so Bee's own engineers can't ship unnoticed | security | pat-context-graphs | co-amazon, co-bee |
| `sig-request-response-to-stateful-agents` | Personal-agent architecture is moving from request-response to always-on stateful runtimes with persistent memory that run autonomously for days without the user's device online — with Claude Code's few-months shift from request-response edits to hours-long runs cited as the glimpse of where all personal agents go | harness | pat-context-graphs | co-bee, co-anthropic **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-provider-blind-trust` | When capture is ambient and total, the threat model must include the operator itself — inside a bigtech acquirer that gets *harder*, not easier (customer-facing guarantees stop applying to you). Trust then can't be policy — it must be verifiable architecture: public transparency logs, attestation, org-split signing keys, and a TCB small enough (~20k LOC) for outside auditors to actually verify | pat-context-graphs | el-sigstore, el-confidential-computing |
| `ins-sandboxing-only-taming` | From running always-on personal agents: attempts to instruction-tame agents "don't work"; the only reliable control is structural — sandbox them so harm is impossible ("our brains can't stop the heart at will") and mediate anything that changes state. Locking down after the fact (the OpenClaw path) costs most of the usefulness — so build the cage before the wildness, not around it | pat-verification-gap **[registry]** | el-bee |

## KnowHow (1 new)

SourcedFromArtifact → `ia-aie-korshakov-privacy`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-provider-blind-agent-backend` | Build an agent backend you provably can't read | Keys live and persist only on the user device — the backend never stores them; encryption has no opt-out and no bypass path; client releases keys only after an attestation pipeline verifies node integrity AND that the workload is in a public transparency log (Sigstore); replicate keys only to attested confidential-compute nodes, scope-limited per node; run inference inside the perimeter (unencrypted data never leaves); force in-memory key expiry sized to the usefulness horizon (Bee: 7 days — 24h loses offline users); split release power: a separate team's signing keys are hardcoded into clients and backends so your own team can't ship unnoticed; keep the TCB tiny (~20k LOC, memory-safe) and reuse vetted crypto — "don't invent your own" (Telegram lesson); use a private CA to embed attestation proofs in certs (public CT logs would leak the fleet) | el-sigstore, el-confidential-computing, el-bee |

## Dropped

- "Two high-profile audit firms review every deployed image" — assurance color, folded into `sig-provider-blind-backend-shipped`.
- The planned attestation-TLS proxy ("lighter mode") — not built yet.
- Base-image vs manifest two-part deploy mechanics — detail inside the knowhow's split-release guideline.
- Q&A OpenClaw remark ("once they tightened it down it became much less useful") — kept as the closing clause of `ins-sandboxing-only-taming` rather than a standalone signal; promote if you want an OpenClaw-specific datapoint (`el-openclaw` **[registry]** exists).

## Review notes

1. **RESOLVED at review 2026-07-22 — `pat-provider-blind-ai` rejected as a pattern (user: it's a design property/mechanism, not an industry-change thesis); candidate retired. The mechanism stays captured as elements (`el-confidential-computing`, `el-sigstore`, `el-bee`) and the signals keep their existing pattern homes.** Original note: Pattern fit: both context signals link to `pat-context-graphs` (personal-context accumulation and its consequences). There is arguably a distinct macro-thesis here — *provider-blind personal AI: trust re-architected against the operator via attestation + user-held keys* — but one talk isn't enough to coin it; flagging per the zero-or-one-new-patterns rule.
2. `co-bee` kept as a Company node distinct from `co-amazon` (DevelopedByCompany target for `el-bee`, and the acquisition date is itself informative). Collapse into co-amazon if you'd rather not track absorbed startups.
3. Numbers (10M tokens/yr, 20k LOC, 7-day expiry, ~Nov 2025 acquisition) are speaker-stated, auto-captioned — treat as approximate at conversion.
4. The attestation method is unpublished ("we will publish details at some point") — knowhow captures the shape, not a reproducible recipe; `url` field left empty.
