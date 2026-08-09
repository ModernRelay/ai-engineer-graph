# SPIKE extraction — "Stop Evaluating Models Like It's the 50s" (Alejandro Vidal, Mindmakers) — FOR REVIEW

Source transcript: `transcripts/vidal-mindmakers-evaluating-models.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/O3FEoMYvUf8 — AI Engineer World's Fair, published 2026-07-13.
`stagingTimestamp` for the artifact and all signals: 2026-07-13 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-vidal-psychometric-evals` | Stop Evaluating Models Like It's the 50s (Alejandro Vidal, Mindmakers — AI Engineer World's Fair) | youtube | https://youtu.be/O3FEoMYvUf8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-alejandro-vidal`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-alejandro-vidal` | Alejandro Vidal (founder, Mindmakers; background in psychology + computer science) | `AffiliatedWithCompany → co-mindmakers` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-mindmakers` | Mindmakers | developer | Vidal's company bringing psychometric methods to LLM evaluation; talk title styles it "Mind Makers" in captions — verify official styling |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-item-response-theory` | Item Response Theory for LLM evals | concept | harness | Psychometric successor to classical test theory applied to LLM benchmarks: fit each question ("item") a difficulty (B) and discrimination (A) parameter and each model a latent ability (theta), via per-item curves mapping ability → P(correct). Yields calibrated model comparisons with likelihood intervals, item-quality audits (negative-A items are broken), benchmark compression, outlier/residual analysis, and bias detection between model groups |
| `el-residual-fingerprinting` | Residual fingerprinting of models and benchmarks | concept | harness | Using IRT residuals (observed − expected correctness per item) as a signature: (a) anchor set + per-organization secret "fingerprint sets" of very hard items expose orgs that later train on a leaked benchmark; (b) residual-correlation "DNA" clusters models by lineage — same lab, same base, distillations, effort variants — enabling detection of unconsented distillation |

Element edges: both `IdentifiedInArtifact → ia-aie-vidal-psychometric-evals`; `el-residual-fingerprinting` `UsesElement → el-item-response-theory`; `el-item-response-theory` `EnablesPattern → pat-verification-gap`.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-vidal-psychometric-evals`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany | OnElement |
|---|---|---|---|---|
| `sig-llm-evals-are-classical-test-theory` | The industry's standard LLM evaluation — counting right answers with every question weighted equally — is literally classical test theory, superseded in psychometrics decades ago by IRT; the field measuring machine intelligence is behind the field measuring human intelligence | `pat-verification-gap` | — | `el-item-response-theory` |
| `sig-irt-reranks-frontier-models` | On real epoch.ai benchmark data (337 questions), Claude Opus 4.1 (245 correct) and Gemini 3 Pro (247) look tied by accuracy — but IRT ability estimates separate them by nearly one standard deviation, because which questions were answered (hard vs easy) matters; accuracy leaderboards can misrank models | `pat-verification-gap` | — | `el-item-response-theory` |
| `sig-benchmark-items-broken` | IRT discrimination audits of real public benchmarks surface items that anti-correlate with ability — including gold answers that are simply wrong or subtly mislabeled (e.g. "total passengers" keyed to passengers + crew); widely used benchmarks contain items rewarding wrong answers, detectable with a cheap fit + LLM review | `pat-verification-gap` | — | `el-item-response-theory` |
| `sig-residual-dna-detects-distillation` | Residual-correlation fingerprints on real data cluster models by lab and lineage — DeepSeek distillations, Qwen family, Llama versions, same-model effort levels — and per-org fingerprint sets flag organizations whose new models are improbably good on secret hard items: statistical tooling now exists to detect benchmark training and unconsented distillation | `pat-verification-gap` | — | `el-residual-fingerprinting` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-uncalibrated-benchmarks-mislead` | Summing right answers embeds a strong hidden assumption — that every question is equally informative; uncalibrated benchmarks have overlapping, noisy, and even negatively-correlated items, so "more questions" doesn't mean better measurement and small accuracy gaps mean nothing. Calibration can invert ranking conclusions; a well-designed set (GPQA) is the exception that proves it — random subsets there work because every item discriminates | `pat-verification-gap` | `el-item-response-theory` |
| `ins-psychometrics-open-frontier` | Psychometrics offers a mostly untapped research program for LLMs: multidimensional/hierarchical models for per-skill ability, merging benchmarks under one scale (cf. the Meta-Benchmark paper), auxiliary signals (latency, tokens) as ability indicators, and psychometric measurement of alignment coupled to mechanistic interpretability | `pat-verification-gap`, `pat-accelerated-research` | `el-item-response-theory` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-vidal-psychometric-evals`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-irt-benchmark-audit` | Audit and compress a benchmark with IRT | Fit IRT over the model×item response matrix (open data like epoch.ai works); flag items with discrimination significantly below zero and review them with an LLM — most are mislabeled gold answers, fix or drop; compress: greedily pick highest-discrimination items until rank-correlation with the full benchmark hits target (real case: 97 of 484 items ≈ 99% correlation, ~5x cheaper — random subsets do far worse); use residual outliers to catch inconsistent runs, e.g. a broken inference platform or wrong quantization producing improbable answer patterns; re-sample outlier questions to average out noise | `el-item-response-theory` |
| `how-benchmark-fingerprint-protection` | Protect a private benchmark with fingerprint sets | For an expensive benchmark you must not leak: define an anchor set (representative items shown to every evaluated org) plus a per-organization fingerprint set of extremely hard items shown only to that org; months later, re-run and compare average residuals on each fingerprint set — an org improbably good on its own secret hard items likely trained on them. Not bulletproof, but a strong contamination tripwire | `el-residual-fingerprinting`, `el-item-response-theory` |

## Dropped

- epoch.ai as a Company/SourceEntity — credited data provider, prose only; coin centrally if it recurs.
- GPQA as an Element — used as the well-calibrated counterexample; prose inside `ins-uncalibrated-benchmarks-mislead`.
- "Meta-Benchmark" research paper — recommended reading, prose only.
- Adaptive testing as a separate concept — subsumed into `how-benchmark-fingerprint-protection` / `el-residual-fingerprinting`.
- Differential item functioning (open-weights vs closed-weights bias per item) — kept as prose capability of `el-item-response-theory`; he deliberately withheld the items.

## Review notes

1. **Benchmark-trust crisis candidate**: registry flags an uncoined "benchmark-trust crisis" pattern from the Han file (batch 3). This talk is a second independent data point — its whole thesis is that accuracy-count benchmarks misrank models, contain broken items, leak, and get trained on. Per instructions I did NOT coin; all signals parked on `pat-verification-gap`. If the pattern is coined centrally, `sig-llm-evals-are-classical-test-theory`, `sig-irt-reranks-frontier-models`, `sig-benchmark-items-broken`, and `ins-uncalibrated-benchmarks-mislead` are natural rehomes.
2. Caption garbles: "Cloud Opus 4.1" → Claude Opus 4.1; "the minute three pro" → likely Gemini 3 Pro; "O4Minnie" → likely o4-mini; "Deep Six"/"Queen" → DeepSeek / Qwen; "GPT 5.5"/"GPT 5" inconsistent in the theta example. Model names in signals kept to the confident resolutions.
3. Domain call: `harness` chosen for all signals (eval tooling); `training` defensible for `sig-residual-dna-detects-distillation` since it probes training lineage.
4. `pat-accelerated-research` on `ins-psychometrics-open-frontier` is a soft link (he's proposing a research program, not observing acceleration) — drop if too loose.
5. Speaker says materials/skills/benchmarks are all published for reuse — no URL captured in captions.
