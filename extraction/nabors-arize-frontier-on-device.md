# SPIKE extraction — "Frontier results, on device" (RL Nabors, Arize) — FOR REVIEW

Source transcript: `transcripts/nabors-arize-frontier-on-device.txt` (auto-captions — quotes are paraphrases, not verbatim; speaker renders as "Rachel Lee Neighbors" — official listing: RL Nabors).
Video: https://youtu.be/fWXJM-J0ZB8 — AI Engineer World's Fair, published 2026-06-29.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-06-29 (publish date).
Entities marked **[registry]** already exist — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-nabors-frontier-on-device` | Frontier results, on device (RL Nabors, Arize — AI Engineer World's Fair) | youtube | https://youtu.be/fWXJM-J0ZB8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-rl-nabors`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-rl-nabors` | RL Nabors (Arize; previously Mozilla/Firefox DevTools, W3C web standards, Microsoft Edge, React team; 3 years consulting AI/LLM/browser companies; site nearestneighbors.com) | `AffiliatedWithCompany → co-arize` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-arize` | Arize | developer | AI observability & evaluation platform for models and agents; maintains the open-source Phoenix eval/observability framework (confirmed absent from registry before coining) |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-arize-phoenix` | Arize Phoenix | product | harness | Open-source LLM observability and evaluation framework from Arize (phoenix.arize.com); used here to run capability evals (small-vs-frontier model comparisons over a golden dataset) and CI/CD-style regression evals |
| `el-small-language-models` | Small language models (SLMs) | technology | inference | Millions-to-low-billions-parameter language models, typically shipped quantized (8/4-bit; ~2 GB per 1B params at FP16, ~quarter that quantized), runnable on phones/laptops/in-browser; ~25% of an LLM's energy per task (task-specific expert models — vision: MobileNet/YOLO/MediaPipe; audio: Whisper/Wav2Vec2 — cheaper still); for when you need a GPT's language power but not "the sum total of human knowledge in a black box" |

Element edges: both `IdentifiedInArtifact → ia-aie-nabors-frontier-on-device`; `el-arize-phoenix` `DevelopedByCompany → co-arize`; `el-small-language-models` `EnablesPattern → pat-sovereign-ai` **[registry]**.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-nabors-frontier-on-device`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | pattern edge | RelevantCompany |
|---|---|---|---|---|
| `sig-nvidia-slms-future-agentic` | inference | Nvidia's 2025 position paper "SLMs are the future of agentic AI" cited as the production-readiness stamp: small language models are sufficiently powerful for agentic task loads at a fraction of LLM energy per task (~25%; task-specific models less still) | `FormsPattern → pat-sovereign-ai` | `RelevantCompany → co-nvidia` **[registry]** |
| `sig-frontier-inference-cost-stack` | inference | The itemized case against one-size-fits-all frontier inference: cloud LLMs carry exposure/interception/retention risk (real cases of chatbot business data breached and leaked); >4 s responses break user believability (VR-chat research) and many frontier calls exceed it; third-party inference costs are uncontrollable and agentic/reasoning workloads consume tokens faster than prices fall — total spend rising despite token deflation; and remote models die offline (outages, air-gapped and disconnected environments) | `FormsPattern → pat-sovereign-ai` | — |
| `sig-on-device-models-preinstalled` | inference | On-device SLMs are shipping as platform defaults: Google's Pixel 10 Pro ships with one, and Chrome exposes built-in Gemini Nano via the Prompt API — web apps get local inference without shipping a model, and product AI can target what's already on the device | `FormsPattern → pat-sovereign-ai` | `RelevantCompany → co-google` **[registry]** |
| `sig-llama-3b-matches-sonnet-with-harness` | harness | Case study: on a social-thread summarization feature, on-device Llama 3.2 3B + a few-shot prompt + deterministic post-processing met/beat the Claude Sonnet baseline — 100% JSON and structural validity, ~93% factual consistency (residual gap traced to a too-strict LLM judge), P50 ~1 s — taking marginal inference cost from ~$1/day (~$0.22 per 14 tasks on Sonnet) to $0, with inference pushed to the user's device | `FormsPattern → pat-harness-over-model` | `RelevantCompany → co-meta` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-prototype-big-deploy-small` | Frontier models' production-displacing role: use the biggest model to prove feasibility and to mint the golden dataset, then let evals — not vibes or peer folklore ("everyone said Gemma 4 is best"; it ran ~8 s vs Llama's ~1 s here and lost) — pick the smallest model that passes: the "SAGE model" (smallest-and-good-enough, her coinage) | `HighlightsPattern → pat-sovereign-ai` | `ReliesOnElement → el-small-language-models` |
| `ins-llm-judges-favor-siblings` | LLM judges import bias: Claude Opus judging graded Llama's near-indistinguishable summaries harsher than sibling Claude Sonnet's ("angsty" vs "cross" quibbles) — eval scores can't be trusted until you open the raw comparisons; judge strictness/self-preference can masquerade as a capability gap | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-judge-as-classifier` **[registry]** |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-nabors-frontier-on-device`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-right-size-model-selection` | Right-size the model in four steps ("prototype big, deploy small") | (1) Prove it's possible at all with the largest capable model; (2) define success measures up front — output validity (e.g. JSON parses), reference/structural validity, factual consistency (LLM- or human-judged), length compliance, P50/P95 latency budgets (here P95 ≤3.5 s against the 4 s believability limit) — and export a golden dataset of curated, preferably human-labeled input→output pairs as ground truth; (3) test candidates from small to large against the criteria (here: Qwen 2.5 1.5B, Qwen 3 1.7B, Llama 3.2 3B, Gemma 4 E2B vs a Claude Sonnet ceiling — the fastest model, Qwen 2.5, lost on accuracy); (4) select the smallest model with acceptable responses; framework built with Google, published on web.dev | `ReferencesElement → el-small-language-models`, `ReferencesElement → el-arize-phoenix` |
| `how-close-the-slm-gap` | Close the SLM-frontier gap in the harness, then guard it | Prompt-engineer one isolated variable per variant: numbered-message input vs raw JSON, few-shot examples, strict negative rules, chain-of-thought — here few-shot won (better length/accuracy, +200 ms) while explicit "don't" rules made the small model *worse*; move structural checks into deterministic post-processing (ref-count validation against thread length, truncation for length); crack open raw eval outputs before trusting judge scores; then keep regression evals running CI/CD-style so a prompt tweak or model upgrade can't silently blow up the feature ("how you keep your CTO from blowing away your agentic experience one morning") | `ReferencesElement → el-small-language-models`, `ReferencesElement → el-arize-phoenix`, `ReferencesElement → el-judge-as-classifier` **[registry]** |

## Dropped

- Goose (open agent harness screenshot), Mima (her side product, mima.social), Pixel 10 Pro, MobileNet/YOLO/MediaPipe/Whisper/Wav2Vec2, Gemma/Qwen/Llama as individual model elements — contestants and examples, prose only.
- The ichthyosaur-echolocation reasoning party trick and "Claude hedges 1 in 3 times" aside.
- Opening Arize ad segment ("you probably need Arize's observability platform").
- Distilled task-specific models tradeoff (retraining + re-shipping 1–2 GB to users' devices per capability) — folded into `how-close-the-slm-gap` context.

## Review notes

1. **`pat-sovereign-ai` link (per extraction guidance):** read here as the developer/product face of sovereignty — data residency on device, offline operation, independence from third-party inference. Three signals form it and the element enables it. If reviewers scope the pattern strictly to nation/enterprise sovereignty, sigs 1–3 have no better existing home and would go pattern-less.
2. **Speaker name:** captions say "Rachel Lee Neighbors" and she signs off "Rachel Neighbors"; official listing says RL Nabors; nearestneighbors.com is a surname pun. Coined `exp-rl-nabors`.
3. **Model-name caution:** "Gemma 4 E2B" (5B params, 3.1 GB) and the Qwen sizes read cleanly, but auto-caption model names are historically unreliable (cf. batch-2 Altos warning) — verify Gemma 4 E2B naming before public-facing use.
4. Scale caveat on `sig-llama-3b-matches-sonnet-with-harness`: it's a solo-developer side project (Mima), not enterprise data — kept because the mechanics (few-shot + post-processing close the gap; inference cost pushed to the consumer device) are the signal, not the dollar figure.
5. The 4-second believability limit is attributed to unnamed "research on mitigating response delays in LLM chats in VR" — treat as citation-needed; same for the "same-or-less energy for correct responses" claim.
6. **Candidate evidence (no coin):** `ins-llm-judges-favor-siblings` adds an LLM-judge-bias data point adjacent to the `pat-benchmark-trust-crisis` candidate (judge-reliability wing: Campos batch-6, Vidal batch-5) — noted, not edged (the insight highlights `pat-verification-gap` instead).
7. `sig-frontier-inference-cost-stack`'s spend claim ("token costs falling, total inference spend rising because agentic workloads consume faster than prices drop") independently corroborates the Yaron survey's cost-as-first-class-constraint signal in this same batch.
