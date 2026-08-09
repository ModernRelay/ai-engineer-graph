# SPIKE extraction — "AI-Driven Multi-Document Correlation for Financial Compliance" (Varsha Shah) — FOR REVIEW

Source transcript: `transcripts/shah-financial-compliance-correlation.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/Iwe_RY-fYgI — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact, signals, and knowhow: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-shah-compliance-correlation` | AI-Driven Multi-Document Correlation for Financial Compliance (Varsha Shah — AI Engineer World's Fair) | youtube | https://youtu.be/Iwe_RY-fYgI |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-varsha-shah`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-varsha-shah` | Varsha Shah (enterprise technical architect — AI, compliance, finance governance, intelligent automation; researcher on cross-document fraud detection) | `AffiliatedWithCompany → co-tcs` (⚠ see Review notes — official listing says Independent) |

## Companies (1 new)

| slug | name | type | brief |
|---|---|---|---|
| `co-tcs` | Tata Consultancy Services | developer | Global IT services and consulting firm; speaker states she works there as an enterprise technical architect "working for Microsoft" (client engagement) |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-cross-document-correlation` | Graph-based cross-document entity correlation | concept | context | Connecting entities across enterprise financial systems (payroll, tax, procurement, transactions) — employees, vendors, accounts, transactions, regulatory filings — into one unified network so that fraud/compliance risks invisible at the single-document level surface as relational anomalies; paired with adaptive probabilistic risk scoring (learns from audit outcomes) and cross-jurisdictional normalization (currencies, tax structures, reporting standards) |

Element edges: `el-cross-document-correlation` `IdentifiedInArtifact → ia-aie-shah-compliance-correlation`; `EnablesPattern → pat-context-graphs` **[registry]**.

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-shah-compliance-correlation`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-fraud-lives-between-documents` | context | Compliance researcher: modern fraud rarely appears as an error within a single document — a payroll record, vendor invoice, and tax filing each pass their individual validation while the inconsistencies **across** them are the fraud; rule-based and document-level NLP systems are structurally blind to this because they validate records, not relationships | `FormsPattern → pat-context-graphs` **[registry]** | — |
| `sig-compliance-graph-detection-results` | security | Framework evaluation over ~3M financial records, 5 years, 4 regulatory jurisdictions: graph entity correlation + probabilistic risk scoring + jurisdictional normalization reached ~91% precision / ~87% recall (F1 0.89), a 76% reduction in false positives, and ~40% less manual audit effort vs rule-based baselines (self-reported research results) | `FormsPattern → pat-context-graphs` **[registry]** | — |
| `sig-compliance-reactive-to-predictive` | context | Because the risk model learns from every completed audit (confirmed fraud strengthens detection patterns; false positives refine scoring), compliance shifts from reactive post-audit review to predictive governance — from "what went wrong" to "what is likely to go wrong next"; compliance becomes a continuous intelligence function rather than a periodic review process | `FormsPattern → pat-context-graphs` **[registry]** | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-compliance-risk-is-relational` | The unit of compliance analysis must move from the document to the relationship: the information needed to catch cross-system fraud already exists in enterprise systems — what is missing is connecting it. Cross-document compliance is a context/structure problem, not a data-volume or model-capability problem | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-cross-document-correlation` |
| `ins-audit-feedback-flywheel` | Replacing static compliance rules with a risk model that ingests audit outcomes turns every investigation into training signal — each completed audit makes the next one cheaper, and the system adapts as fraud patterns evolve without manual rule updates; the flywheel only works on top of the connected entity graph | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-cross-document-correlation` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-shah-compliance-correlation`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-cross-document-compliance` | Build compliance AI as three layers over connected data | Layer 1 — entity-correlation graph across payroll/tax/procurement/finance ("what is connected?"). Layer 2 — adaptive probabilistic risk scoring combining anomaly strength, source reliability, and historical patterns into a confidence-based score ("what is genuinely risky?"), continuously retrained on audit outcomes. Layer 3 — cross-jurisdictional normalization of currencies, tax rules, reporting periods, classification schemes ("how should risk be interpreted here?"). Deployment: integrate with existing ERP/payroll/procurement/tax platforms; configure per jurisdiction; align outputs with the audit workflow so investigators work a prioritized risk-scored queue instead of routine document review; validate scalability to millions of records | `ReferencesElement → el-cross-document-correlation` |

## Dropped

- The payroll-record/vendor-invoice/tax-filing worked example — illustration, folded into `sig-fraud-lives-between-documents`.
- "Four key deployment considerations" as separate nodes — folded into the knowhow's deployment guidance.
- Microsoft as a Company node/edge — mentioned only as the client of her TCS engagement; registry has `co-microsoft` but no edge warranted by the content.

## Review notes

1. **Affiliation conflict**: the official listing says "Varsha Shah, Independent" but the transcript states "enterprise technical architect working at Tata Consultancy Services working for Microsoft". Coined `co-tcs` and kept the affiliation edge (in-talk self-description); drop the edge and `co-tcs` at review if the conference listing is treated as authoritative (research may be personal/independent of employer).
2. Metrics are **self-reported research results** (no named dataset, no external benchmark): ~3M records / 5 years / 4 jurisdictions; 91% precision, 87% recall, F1 0.89, 76% false-positive reduction, 40% audit-effort reduction. Caption garble "flat cases" read as "flagged cases". Whether the framework is production-deployed or a research prototype is ambiguous ("research driven… designed with enterprise deployment in mind") — signals phrased as evaluation results, not production outcomes.
3. All three signals form `pat-context-graphs` — single-thesis talk (precedent: daga file). The talk is the strongest pure "risks live between the documents, connect the entities" evidence in this batch.
4. `el-graphrag` **[registry]** considered (it was on the relevant-existing hint list) but not linked: this framework is graph-based correlation for detection/scoring, not retrieval-augmented generation.
5. `ins-audit-feedback-flywheel` could arguably highlight a learning/verification pattern instead; kept on `pat-context-graphs` since the flywheel's substrate is the connected graph. No new pattern coined.
