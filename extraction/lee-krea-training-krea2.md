# SPIKE extraction — "Training Krea 2: What matters in generative model training" (Sangwu Lee, Krea) — FOR REVIEW

Source transcript: `transcripts/lee-krea-training-krea2.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/-tviRdpmHvs — AI Engineer World's Fair, **Generative Media track**, published 2026-08-18.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-18 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the research/data side of Krea 2 (companion to the Menezes infra talk). Thesis: **data is everything** — once you lock the architecture, model quality is determined by data curation. Concrete techniques: ~30–40 in-house classifiers, SAE-based unsupervised tagging, aggressive removal of AI-generated images ("synthetic data is sticky"), and an LLM-research-borrowed pipeline (pre-train → mid-train → SFT → preference optimization → GRPO). Caption garbles: "Create/Korea 2" → **Krea 2**, "Chat GPT-2/Nano Banana Pro" → competitor image models (kept as named), "Barry LM" → likely **Bagel/an LLM-inspired** pipeline (⚠ note 3), "SigLip"/"SSCD"/"pHash" kept, "Fei-Fei Li" kept.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-lee-training-krea2` | Training Krea 2: What matters in generative model training (Sangwu Lee, Krea — AI Engineer World's Fair) | youtube | https://youtu.be/-tviRdpmHvs |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-sangwu-lee`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-sangwu-lee` | Sangwu Lee (research, Krea; trained the Krea 2 image foundation model) | `AffiliatedWithCompany → co-krea` **[registry]** |

## Companies (0 new)

Reused **[registry]**, edge-only: `co-krea` **[b21, this batch]** — the research side of the same model the Menezes talk covers from infra. Referenced for behaviour: OpenAI (ChatGPT image gen), Google (Nano Banana). No new company nodes.

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-data-is-everything` | Data curation as the lever | concept | training | The talk's refrain: "once you lock in your architecture, most of the work goes into data curation — data is quite literally everything." For Krea 2 the focus was **stylistic diversity**: not over-relying on standard aesthetic/quality scores that would cut low-res-CRT or unconventional aesthetics some users want. The contrast: frontier models (ChatGPT image, Nano Banana Pro) get consistency by **mode-collapsing** ("render the most boring average person, center-framed"); Krea chose faster generation with knobs so creative studios can explore before they know what they want. Echoes the b15 data-quality-as-compute-multiplier thesis (Morcos/Datology) in the image domain |
| `el-classifier-distillation-pipeline` | Big-VLM-to-small-classifier distillation | technology | training | The scalable-filtering method: use a large vision-language model to make a filtering decision (is this an AI image? does it have watermarks/borders?), then **distill that decision into a cheap SigLip-sized classifier** you can run over a billion+ images affordably — the same approach cited for text (essential-web-data's LLM-taxonomy distilled to a ~500M model). Plus **SAE-based unsupervised tagging**: a sparse autoencoder on a vision model yields off-the-shelf feature tags (horse, blurry, watermark) to oversample/filter on. Krea ended with ~30–40 custom in-house classifiers/heuristics |
| `el-synthetic-data-is-sticky` | Synthetic data is sticky | concept | training | The caution that shaped curation: they "tried very hard to remove any AI images at all," because distillation on AI-generated data "provides a shortcut to a good model but synthetic data is so sticky to the model that you lose the point" — the output converges to ChatGPT/Nano-Banana aesthetics, detectable to a trained eye. A quality/identity argument against the easy path, and a data-provenance concern parallel to the corpus's contamination thread |
| `el-diffusion-borrows-llm-recipe` | Diffusion training borrows the LLM recipe | concept | training | The convergence observation: Krea 2's pipeline mirrors LLM post-training — low→high-resolution **pre-training → mid-training → SFT → preference optimization → GRPO** (reward servers scoring generated images for text-rendering/anatomy), plus a small **prompt-expander LLM** (now near-essential for production diffusion, expanding user prompts into long in-distribution ones) and **multi-expert on-policy distillation** into one student. "Steal a lot from LLM research so I can reuse their kernels and literature." Image generation framed as "a proxy for VLM progress" |

Element edges: all four `IdentifiedInArtifact → ia-aie-lee-training-krea2`.
`el-data-is-everything` `UsesElement → el-classifier-distillation-pipeline`, `el-synthetic-data-is-sticky`;
`el-diffusion-borrows-llm-recipe` `UsesElement → el-on-policy-distillation` **[registry]**;
`el-data-is-everything` `DevelopedByCompany → co-krea` **[registry]**, `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**.

Reused elements (no new nodes): `el-on-policy-distillation` **[b5]** (multi-expert distillation into a student), `el-grpo`-adjacency (GRPO for diffusion reward — no dedicated node), `el-data-quality-multiplier` **[b15]** (Morcos/Datology — the strongest cross-file resonance; edge left to review).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-lee-training-krea2`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-krea` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-data-curation-determines-image-quality` | training | A from-scratch image-model team's core claim: architecture is commodity, **data curation determines quality** — "data is everything," and for Krea the goal was preserving stylistic diversity rather than optimizing standard aesthetic scores that mode-collapse. Frontier consistency comes from mode collapse (the boring average, center-framed); Krea traded that for faster, knob-driven exploration. The b15 data-quality-as-compute-multiplier thesis, independently restated in generative media | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-data-is-everything` |
| `sig-distill-big-vlm-to-cheap-filter` | training | The scalable-curation method: use a large VLM to make a filtering judgement, then **distill it into a SigLip-sized classifier** cheap enough to run over a billion+ images (paralleling the essential-web-data text approach), plus SAE-based unsupervised tagging — ~30–40 in-house classifiers total. Data infrastructure, not model architecture, as where the differentiated work lives | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-classifier-distillation-pipeline` |
| `sig-synthetic-data-is-sticky` | training | A data-provenance caution: Krea removed AI-generated images aggressively because "synthetic data is so sticky that once you train on it your model good but you lose the point" — outputs converge to ChatGPT/Nano-Banana aesthetics, detectable to experts. Distilling on synthetic data is the easy shortcut that costs identity; a generative-media parallel to the corpus's contamination/benchmark-trust concerns about synthetic-data feedback loops | `FormsPattern → pat-benchmark-trust-crisis` **[registry]** | `OnElement → el-synthetic-data-is-sticky` |
| `sig-diffusion-adopts-llm-post-training` | training | The convergence signal: diffusion training now mirrors the LLM recipe — pre/mid-training, SFT, preference optimization, **GRPO with reward servers**, a prompt-expander LLM, and multi-expert on-policy distillation — deliberately "stealing from LLM research to reuse kernels and literature." The post-training methods coined for language (b5/b19 OPSD) crossing into image generation, with image generation framed as a proxy for VLM progress | `FormsPattern → pat-continual-learning-turn` **[registry]** | `OnElement → el-diffusion-borrows-llm-recipe`, `el-on-policy-distillation` **[registry]** |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-curation-is-the-differentiator` | The talk's durable claim is that in a world where the transformer architecture is shared and kernels are reused across LLM and diffusion, the only remaining lever is data — and specifically the *taste* encoded in curation choices (preserve unconventional aesthetics vs optimize aesthetic scores, remove synthetic data despite the shortcut it offers). That reframes model differentiation as a data-and-judgement problem, the same "data is the compute multiplier" thesis the corpus reached in language, and it makes the in-house classifier suite — not the architecture — the moat | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-data-is-everything`, `el-classifier-distillation-pipeline` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-lee-training-krea2`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-curate-data-for-image-models` | Curate data as the real lever for image models | Once the architecture is locked, put the work into **data curation**, because it determines model quality more than any other choice; decide deliberately what "good" means — optimizing standard aesthetic/quality scores mode-collapses toward the boring average, so if you want stylistic diversity you must *not* cut unconventional aesthetics (low-res, CRT, etc.); dedup in stages (cheap pHash/MD5 first, then embedding-based SSCD/SigLip for near-duplicates); scale filtering by **distilling a large VLM's judgement into a cheap SigLip-sized classifier** you can run over a billion images, and use **SAE unsupervised tagging** for oversample/filter features; **remove AI-generated images** despite the shortcut they offer, because synthetic data is sticky and collapses your model toward frontier aesthetics you can't undo; borrow the **LLM post-training recipe** (pre/mid-train, SFT, preference optimization, GRPO with reward servers, a prompt-expander, multi-expert distillation) to reuse kernels and literature; and check captioner failure modes, since a captioner that consistently omits a fact (e.g. "framed on a white wall") biases every generation | `ReferencesElement → el-data-is-everything`, `el-classifier-distillation-pipeline`, `el-synthetic-data-is-sticky`, `el-diffusion-borrows-llm-recipe` |

## Dropped

- **The diffusion-model primer** (noise/denoise, latent diffusion, autoencoders, DiT quadratic cost) — background.
- **The Barack-Obama-the-horse Wikipedia aside** and page-rank world-knowledge injection — colour, one clause in the curation logic.
- **The DALL-E-2-resemblance and future-directions musings** (bounding boxes, scene graphs, Fei-Fei Li 2017) — forward-looking, no signal.

## Review notes

1. **Peripheral-but-real corpus value on three coined patterns.** Lands mainly on `pat-model-not-bottleneck` (data curation, not architecture, is the differentiator — a strong echo of b15 Morcos/Datology in a new domain), touches `pat-benchmark-trust-crisis` (synthetic-data stickiness / provenance), and `pat-continual-learning-turn` (LLM post-training methods — GRPO, OPSD — crossing into diffusion). The clearest cross-domain confirmation that the corpus's language-model theses generalize to generative media.
2. **Companion to `menezes-krea-infra-train-serve.md`** (same model, infra side). `co-krea` should carry both research and infra facts.
3. **⚠ Verify before seeding:** "~30–40 in-house classifiers"; "2–10 billion images"; the essential-web-data ~500M distillation reference; "Barry LM" (likely a garble of an LLM-inspired pipeline name — Bagel?); competitor model names ("ChatGPT-2", "Nano Banana Pro"). All caption-sourced.
4. **Proposed cross-file edge, left to review:** `el-data-is-everything` → `el-data-quality-multiplier` (b15 Morcos) — same thesis, different modality.
