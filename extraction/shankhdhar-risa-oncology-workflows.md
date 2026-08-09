# SPIKE extraction — "Can Oncology Workflows Run Without Human Touch?" (Anant Shankhdhar, Risa Labs) — FOR REVIEW

Source transcript: `transcripts/shankhdhar-risa-oncology-workflows.txt` (auto-captions — paraphrases; company "Trisca" → **Risa Labs**, speaker "Anant Shankar" → **Anant Shankhdhar**; "EVBV/EV" = eligibility & benefits verification; "PHN" ≈ pipeline).
Video: https://youtu.be/_cVfz88_j7A · published 2026-07-20 (AI Engineer, World's Fair).
Slugs follow seed conventions. `pat-harness-over-model` is defined in `bahidika-allou-msft-dont-let-llm-drive.md`; `pat-verification-gap` and `pat-context-graphs` are registry patterns.
`stagingTimestamp` for the artifact and all signals: 2026-07-20.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-risa-oncology` | Can Oncology Workflows Run Without Human Touch? (Anant Shankhdhar, Risa Labs — AI Engineer World's Fair) | youtube | https://youtu.be/_cVfz88_j7A |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-anant-shankhdhar`.

## Experts (1 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-anant-shankhdhar` | Anant Shankhdhar (AI Engineer, Risa Labs) | `co-risa-labs` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-risa-labs` | Risa Labs | developer | automates oncology back-office workflows (prior authorization, eligibility) |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-risa-prior-auth` | Risa prior-authorization pipeline | product | harness | End-to-end oncology prior-auth automation: intake → eligibility/benefits verification → auth-status determination → medical necessity → submission, with a growing "no-touch" (no human review) share |
| `el-medical-necessity-agent` | Medical necessity agent | product | harness | "Clinical brain": reads patient notes + policy criteria, queries a per-patient biomarker graph, returns answers with supporting **and** contradictory facts plus a confidence score; escalates only low-confidence cases to a clinician (has a linked publication) |
| `el-patient-medical-graph` | Patient medical graph | technology | context | Per-patient graph of biomarkers extracted from notes, queried against drug policy criteria to judge medical necessity |
| `el-payer-rule-kb` | Payer rule knowledge base | technology | data-eng | SQL knowledge base of payer/drug coverage rules (which drugs a payer does/doesn't require auth for, time-bounded), built from portal checks + configurable LLM extraction over payer documents |

Element edges: `el-risa-prior-auth` DevelopedByCompany → `co-risa-labs`; `el-medical-necessity-agent` DevelopedByCompany → `co-risa-labs`; `el-risa-prior-auth` UsesElement → `el-medical-necessity-agent`; `el-medical-necessity-agent` UsesElement → `el-patient-medical-graph`; `el-risa-prior-auth` UsesElement → `el-payer-rule-kb`; `el-patient-medical-graph` ExemplifiesPattern → `pat-context-graphs`; `el-risa-prior-auth` ExemplifiesPattern → `pat-harness-over-model`. All `IdentifiedInArtifact → ia-aie-risa-oncology`.

## Patterns (registry reuse — no new)

- `FormsPattern → pat-harness-over-model` — deterministic engine first, agents only where rules can't decide; the automation-share grows from the deterministic core outward.
- `FormsPattern → pat-verification-gap` — indeterministic LLM extraction can't be blindly trusted; confidence scoring + multi-source corroboration is what makes trust land outside the model.
- `FormsPattern → pat-context-graphs` — the per-patient biomarker graph as the reasoning substrate for clinical questions.

## Signals (4 new)

All: domain `harness` (sig `sig-medical-necessity-graph` is `context`), `SpottedInArtifact → ia-aie-risa-oncology`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|
| `sig-risa-no-touch-oncology` | Risa Labs runs oncology prior-authorization orders to submission with **no human touch** for a growing share, by resolving/flagging deterministically first and invoking agents only where rules can't decide | harness-over-model | el-risa-prior-auth | co-risa-labs |
| `sig-multi-source-evidence-confidence` | Risa beats indeterministic single-source LLM extraction by reconciling multiple evidence sources (patient notes + prior authorization letters + a payer-rule KB); only where sources concur is confidence high enough to skip human review | verification-gap | el-payer-rule-kb | co-risa-labs |
| `sig-medical-necessity-graph` | Risa's medical-necessity agent queries a per-patient biomarker "medical graph" against drug policy criteria and returns supporting + contradictory facts with a confidence score, escalating only low-confidence cases to clinicians | context-graphs | el-patient-medical-graph, el-medical-necessity-agent | co-risa-labs |
| `sig-self-healing-rpa` | Risa generates portal-automation (RPA) configs with an LLM from a reusable action repository, plus a production self-healing loop that detects and mitigates broken automations at runtime — cutting integration time across dozens of fragile payer portals | harness-over-model | el-risa-prior-auth | co-risa-labs |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-determinism-first-agents-last` | Path to no-touch automation: a deterministic rule engine resolves/flags everything it can first, agents handle only the residual reasoning, and a confidence gate decides human escalation — the automated share grows outward from the deterministic core | pat-harness-over-model | el-risa-prior-auth |
| `ins-multi-source-beats-single-source` | Indeterministic LLM extraction can't be blindly tested, so it only improves efficiency; corroborating an independent second/third source is what converts "efficiency gain" into genuine human elimination | pat-verification-gap | el-payer-rule-kb |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-risa-oncology`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-confidence-gated-escalation` | Gate no-touch automation on confidence + corroboration | Attach a confidence score to every agentic decision; require multi-source evidence concurrence before auto-proceeding; return contradictory facts alongside supporting ones; route only low-confidence/contradictory cases to humans; keep every rule configurable for override; add a self-healing loop for fragile integrations | el-medical-necessity-agent, el-payer-rule-kb |

## Dropped

- The four-agent decomposition (EV / auth / necessity / submission agent) is described structurally but only the necessity agent carries transferable substance — the others are folded into `el-risa-prior-auth` rather than made separate elements.
- API-vs-RPA "coverage orchestrator" routing detail — implementation color, no standalone intel.
- The unnamed "publication" on the medical-necessity agent is noted in `el-medical-necessity-agent`; no URL given in captions, so no separate artifact node.

## Review notes

1. Domain call: I tagged the pipeline signals `harness` and the graph signal `context`. Alternative: treat the whole talk as `data-eng` (payer integration). Say if you'd prefer.
2. This talk triple-links patterns (`pat-harness-over-model` + `pat-verification-gap` + `pat-context-graphs`) — it genuinely straddles all three; trim if you want a single dominant pattern per signal.
3. `co-risa-labs` typed `developer`; could be `research` given the clinical publication. Left as `developer` (it's a product company).
