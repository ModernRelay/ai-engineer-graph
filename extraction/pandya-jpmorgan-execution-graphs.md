# SPIKE extraction — "Learned Execution Graphs for Anomaly Detection & Drift in APIs" (Ritvik Pandya, JP Morgan Chase) — FOR REVIEW

Source transcript: `transcripts/pandya-jpmorgan-execution-graphs.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/u1yaOeEX4e8 — AI Engineer World's Fair, published 2026-07-23.
`stagingTimestamp` for the artifact and all signals: 2026-07-23 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-pandya-execution-graphs` | Learned Execution Graphs for Anomaly Detection & Drift in APIs (Ritvik Pandya, JP Morgan Chase — AI Engineer World's Fair) | youtube | https://youtu.be/u1yaOeEX4e8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-ritvik-pandya`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-ritvik-pandya` | Ritvik Pandya (leads the payments team at JP Morgan Chase; real-time payment-processing reliability) | `AffiliatedWithCompany → co-jpmorgan` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-jpmorgan` | JPMorgan Chase | — | global bank; appears as an enterprise instrumenting real-time payments infrastructure. No finance value in the type enum — left empty; pick at seeding. Batch-8's `el-cross-document-correlation` (Shah talk) is the adjacent financial-graph node — different problem (compliance docs), no merge |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-learned-execution-graphs` | Learned execution graphs | concept | infra | Short-lived, request-scoped execution DAGs — explicitly contrasted with persistent/property graphs (Neo4j-style) you query — that represent how a request actually flows through services (edge layer → gateway/ingress → authn/authz → orchestration → parallel systems → client notification), with each loop/retry modeled as its own entity. Baselines learned per client/endpoint from telemetry; deviations detected against the baseline and localized to the exact node |
| `el-opentelemetry` | OpenTelemetry | technology | infra | Open observability standard whose traces feed the execution-graph system asynchronously (so detection never slows the hot request path); millions of traces with injected anomalies were used to train/benchmark the system pre-production. website: opentelemetry.io |
| `el-execution-drift-taxonomy` | Execution-drift taxonomy | concept | infra | Practitioner taxonomy separating anomaly (one-off incident — the commute that took an extra hour once) from drift (the baseline itself shifted over a year), then categorizing drift: structural (node/step added or removed), scale/volume (service saturating under load), covariate (traffic mix changed — 60/40 local/foreign becomes inverted while the system itself is fine), and behavioral (same request, different behavior). Each category maps to a different response: rebaseline, scale out / go async, segment baselines, or roll back |

Element edges: all three `IdentifiedInArtifact → ia-aie-pandya-execution-graphs`; `el-learned-execution-graphs` `DevelopedByCompany → co-jpmorgan`, `UsesElement → el-opentelemetry`.

## Signals (3 new)

All: domain `infra`, `SpottedInArtifact → ia-aie-pandya-execution-graphs`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-jpm-learned-execution-graphs` | JP Morgan payments models real-time request processing as learned execution DAGs over OpenTelemetry traces: tiered checks (a cheap tier-1 "boarding pass glance" against the end-to-end baseline; deeper tiers only on deviation), per-client baselines, and node-level localization (e.g., pinpointing the FX-rate service as the slow step and recalling its past failure modes); the system was trained pre-production by injecting anomalies into millions of traces over 7 days | `FormsPattern → pat-context-graphs` **[registry]** (fit flagged — see notes) | `RelevantCompany → co-jpmorgan` |
| `sig-mttd-single-window` | Reported outcome: mean time to discovery dropped sharply — detection works off a single time window instead of waiting across multiple windows, made near-real-time by an async split into a hot path (Kafka/stream processing for fast decisions/automation) and a recon path (slower, more accurate) | — | `RelevantCompany → co-jpmorgan` |
| `sig-classified-drift-automated-remediation` | Remediation is being automated behind classification: OpenTelemetry feeds root-cause analysis, drift type determines the solution, risk is assessed, and fixes roll out canary-style (5–10% of machines → monitor/verify → 100%), with an admin-confirmation gate before classification-triggered action | — | `RelevantCompany → co-jpmorgan` |

Additional signal edges: `sig-jpm-learned-execution-graphs` `OnElement → el-learned-execution-graphs`, `OnElement → el-opentelemetry`; `sig-classified-drift-automated-remediation` `OnElement → el-execution-drift-taxonomy`.

## Insights (1 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-graphs-localize-understanding` | The graph representation earns its keep through localization and explanation: knowing WHICH node deviated and WHAT kind of drift it is turns raw telemetry into an actionable, explainable decision — "your health score is 22" from a doctor means nothing without the underlying data. It is the same move context graphs make for agents — structure as the understanding layer — applied to system behavior instead of knowledge | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-learned-execution-graphs` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-pandya-execution-graphs`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-execution-graph-detection` | Detect anomalies with learned, tiered, per-context baselines | Represent request processing as a DAG; put every loop/retry in the graph as its own entity. Run a cheap tier-1 end-to-end baseline check first; escalate to deeper tiers only on deviation. Never use generic baselines — segment per client (local vs foreign), per endpoint, per use case (POST for real-time payments ≠ POST for wire payments); give new/cold-start endpoints their own fresh baseline. Feed telemetry asynchronously (hot path via Kafka/stream for fast decisions + recon path for accuracy) so detection never delays the payment path. Use tail-based sampling (you need request start AND end per node); MMD or KL divergence for detection; tune for the delayed-event case so a late-reporting node isn't misread as a structural change; make every alert explainable with underlying data; keep the system deployment-aware so rollback is a valid response | `ReferencesElement → el-learned-execution-graphs`, `ReferencesElement → el-opentelemetry` |
| `how-drift-response-mapping` | Classify drift before acting | Distinguish anomaly (one-off; handle per criticality) from drift (baseline shift; rebaseline). Then classify: structural (step added/removed — e.g., the coffee shop adding a membership question) → fold the new step into baselines and alerts; scale/volume → scale instances out or make calls asynchronous; covariate (traffic mix changed, system fine) → maintain segmented baselines or consciously raise the average-time baseline; behavioral (same request, new behavior) → consider rollback. Once classified, risk-assess the automated fix and canary it: 5–10% of nodes → monitor and verify → 100%; keep an admin confirmation before classification-triggered automation | `ReferencesElement → el-execution-drift-taxonomy` |

## Dropped

- The commute/coffee-shop/airport analogies — teaching devices; folded into taxonomy briefs.
- Kafka, MMD, KL divergence, tail-based sampling as Element nodes — implementation ingredients; kept inside knowhow guidelines.
- "Part of a bigger neuro[-symbolic?] algorithm system, this is just one module" — too garbled to extract; noted below.
- Labels-help-learning remark — generic ML hygiene; folded into knowhow.

## Review notes

1. **Pattern fit flag:** this is not an LLM/agent talk — it's statistical anomaly detection over service telemetry. `sig-jpm-learned-execution-graphs → pat-context-graphs` reads execution graphs as the operational cousin of context graphs (graph structure as the understanding layer, per the insight). If that stretches the pattern, drop the edge and hold the signal pattern-less — the talk stands on its elements and knowhow. The other two signals are deliberately pattern-less.
2. **Unresolved garbles:** the benchmark line — "open telemetry and that star bench were used" (some trace benchmark, name unrecoverable; the 7-days / millions-of-traces / injected-anomalies methodology is kept, the benchmark name is not); "part of bigger neuro specific algorithms"; "what happened in Bay Area in number of carc" (car count?). **Resolved:** "if k is there... ingress layer" → Kubernetes/K8s ingress; "tail by based" → tail-based sampling; "exponential ma" → exponential moving average; "opal telemetry" → OpenTelemetry.
3. Captions say "Ritik"; official listing says Ritvik Pandya — official used.
4. Thin-signal talk (methodology, few dated external facts): if `sig-mttd-single-window` and `sig-classified-drift-automated-remediation` fail your signal bar, the fallback is 1 signal + the insight + both knowhows.
