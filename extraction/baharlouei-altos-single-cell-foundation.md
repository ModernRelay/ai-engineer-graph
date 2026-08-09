# SPIKE extraction — "From Tokens to Cells: Foundation Models for Single-Cell Biology" (Akram Baharlouei, Altos Labs) — FOR REVIEW

Source transcript: `transcripts/baharlouei-altos-single-cell-foundation.txt` (auto-captions — paraphrases; "SCGPT" → **scGPT**, "Informer" → likely **Geneformer**, "CPADR/CPA" a perturbation-model baseline, "SCGENE scope" → **scGenScope**; model/paper names are caption-recovered — verify before publishing externally).
Video: https://youtu.be/-561cZmir5Q · published 2026-07-20 (AI Engineer, World's Fair).
Slugs follow seed conventions. `pat-accelerated-research` is a registry (seed) pattern.
`stagingTimestamp` for the artifact and all signals: 2026-07-20.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-altos-single-cell` | From Tokens to Cells: Foundation Models for Single-Cell Biology (Akram Baharlouei, Altos Labs — AI Engineer World's Fair) | youtube | https://youtu.be/-561cZmir5Q |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-akram-baharlouei`.

## Experts (1 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-akram-baharlouei` | Akram Baharlouei (Machine Learning Engineer, Altos Labs) | `co-altos-labs` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-altos-labs` | Altos Labs | research | biotech; cellular rejuvenation to restore cell health/resilience; builds single-cell foundation models |

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-single-cell-foundation-model` | Single-cell foundation model | concept | training | Foundation models over single-cell data toward a unified "virtual cell → tissue → human / digital twin"; the "tokens to cells" analogy (cell = sentence, genes = tokens) |
| `el-rna-seq` | Single-cell RNA-seq | technology | training | Transcriptomic modality (~20K-gene expression matrix per cell); the most-available/most-used modality for foundation-model training, but a noisy, heterogeneous *snapshot* of a continuous process |
| `el-scgpt` | scGPT (transformer single-cell models) | product | training | BERT-style masked-gene-count prediction over cells-as-sentences (with Geneformer et al.); compresses cells to a latent vector — where information is lost |
| `el-flow-matching` | Flow matching (for single-cell) | concept | training | Generative modeling that matches the data *distribution* from Gaussian noise rather than compressing to a latent vector; empirically better on single-cell data |
| `el-primeflow` | PrimeFlow | product | training | Altos flow-matching single-cell model (on arXiv) that matches ground-truth distributions where autoregressive/autoencoder baselines predict the mean; evaluated via MMD |

Element edges: `el-primeflow` DevelopedByCompany → `co-altos-labs`; `el-primeflow` UsesElement → `el-flow-matching`; `el-scgpt` UsesElement → `el-rna-seq`; `el-primeflow` UsesElement → `el-rna-seq`; `el-single-cell-foundation-model` UsesElement → `el-rna-seq`; `el-scgpt` ExemplifiesPattern → `pat-accelerated-research`; `el-primeflow` ExemplifiesPattern → `pat-accelerated-research`. All `IdentifiedInArtifact → ia-aie-altos-single-cell`.

## Patterns (registry reuse — no new)

- `FormsPattern → pat-accelerated-research` — foundation models / virtual-cell modeling aimed at compressing the ~10-year, billions-of-dollars drug-development cycle; the talk is a state-of-the-art read on how far the AI actually gets.

## Signals (5 new)

All: domain `training`, `SpottedInArtifact → ia-aie-altos-single-cell`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|
| `sig-single-cell-transformers-underperform` | Benchmarks (two NeurIPS 2025 papers — multimodal imaging+RNA-seq, and perturbation-response) show transformer single-cell foundation models often only match or lose to simple linear baselines despite far higher training cost | accelerated-research | el-scgpt | co-altos-labs |
| `sig-flow-matching-beats-autoregressive` | Altos' PrimeFlow (arXiv) shows flow-matching models that match the data distribution outperform autoregressive/autoencoder single-cell models that compress to a latent vector and lose information | accelerated-research | el-primeflow, el-flow-matching | co-altos-labs |
| `sig-rna-seq-scale-vs-quality` | Single-cell RNA-seq datasets now reach hundreds of millions of cells (a "1 billion cells" project cited), but the data is noisy heterogeneous snapshots of a continuous process — measurement realism/quality, not just quantity, is the bottleneck | accelerated-research | el-rna-seq | — |
| `sig-drug-development-declining` | Against Moore's law, new-drug output per year is declining; a full pipeline takes up to ~10 years, costs billions, with ~5% (or less) acceptance — the gap virtual-cell/human models aim to close | accelerated-research | el-single-cell-foundation-model | — |
| `sig-osk-reprogramming-human-2026` | 2026: the first partial-reprogramming ("OSK", Yamanaka-factor-based) medicine is entering human testing — ~20 years after the 2006 discovery (2012 Nobel) | accelerated-research | — | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-compression-loses-cell-info` | Compressing single-cell data into a latent vector discards biologically load-bearing information — which is why heavy transformer models can underperform linear baselines, while distribution-matching (flow) preserves more | pat-accelerated-research | el-flow-matching |
| `ins-data-quality-over-scale` | For single-cell foundation models, measurement realism and data quality gate generalization more than raw dataset scale — the opposite of the text-LLM "just scale it" story | pat-accelerated-research | el-rna-seq |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-altos-single-cell`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-flow-matching-for-single-cell` | Model single-cell data by matching distributions, not compressing them | Prefer flow-matching / distribution-matching objectives over autoregressive latent-vector compression; always benchmark against a simple linear baseline before trusting a large transformer; invest in measurement quality and realism alongside dataset scale; evaluate distribution fit (e.g. MMD), not just point prediction | el-flow-matching, el-single-cell-foundation-model |

## Dropped

- Modality tour (genome/proteomics/morphology tradeoffs) — background; only RNA-seq carries a signal (`el-rna-seq`).
- Quantum-computing aside ("might be a natural fit, we don't know") — speculative, not intel.
- Human Cell Atlas mention — context for `el-single-cell-foundation-model`, not promoted to its own node (no claim attached).
- Paper titles (scGenScope, the perturbation benchmark, PrimeFlow) — captured in `sig-*` descriptions; no separate artifact nodes (links shown on-slide but not in captions).

## Review notes

1. **Name reliability:** model/paper names are the weakest captions in the batch. "Informer" is almost certainly **Geneformer**; "SCGENE scope" ≈ scGenScope; "CPADR" is a perturbation baseline. Verify against the arXiv/NeurIPS record before these become public-facing.
2. `el-scgpt` is scoped as a *family* (scGPT + Geneformer-style transformer single-cell models) rather than one product — split if you want per-model nodes.
3. This is the only batch-2 talk in the `training` domain and the only one on `pat-accelerated-research`; no overlap with the voice/harness cluster.
4. Only 1 KnowHow — a research survey talk yields thin actionable practice; the substance is in the signals/insights.
