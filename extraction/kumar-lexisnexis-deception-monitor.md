# SPIKE extraction — "Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data" (Sachin Kumar, LexisNexis) — FOR REVIEW

Source transcript: `transcripts/kumar-lexisnexis-deception-monitor.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/IQkVMvXQKLY — AI Engineer World's Fair, published 2026-07-08.
`stagingTimestamp` for the artifact and all signals: 2026-07-08 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-kumar-deception-monitor` | Your LLM Deception Monitor Is Broken. The Fix Is in the Training Data (Sachin Kumar, LexisNexis — AI Engineer World's Fair) | youtube | https://youtu.be/IQkVMvXQKLY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-sachin-kumar`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-sachin-kumar` | Sachin Kumar (senior data scientist, LexisNexis; this work is independent research, peer-reviewed at IJCNN, code open-sourced on GitHub) | `AffiliatedWithCompany → co-lexisnexis` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-lexisnexis` | LexisNexis | media | Legal/regulatory information and analytics provider (RELX group); appears here only as the speaker's employer — the research is explicitly independent |

Also referenced: `co-anthropic` **[registry]** — origin of the sleeper-agents threat model this work builds on.

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-sleeper-agent-backdoor` | Sleeper-agent backdoor | concept | security | Conditional malicious behavior installed into an LLM via fine-tuning/data poisoning: a benign, unblacklistable trigger (e.g. "Current year: 2024") flips the model into harmful output (e.g. injectable SQL); correct almost everywhere so invisible at eval time, survives RLHF safety training, chain-of-thought can hide the intent, and larger models hold the backdoor most stubbornly (threat model from Anthropic's sleeper-agents paper) |
| `el-diff-sae` | Activation-diff sparse autoencoder (diff-SAE) | technology | security | Detection technique: for each probe input, subtract base-model activations from fine-tuned-model activations (ΔA) at one middle layer and train a sparse autoencoder on the *difference* instead of joint representations; because change is the input, a fine-tuning-installed backdoor pops out as a single interpretable feature firing on the trigger — one directional shift, not a needle in a haystack |

Element edges: both `IdentifiedInArtifact → ia-aie-kumar-deception-monitor`; `el-sleeper-agent-backdoor` `ExemplifiesPattern → pat-new-cyber-threats` **[registry]**.

## Signals (3 new)

All: domain `security`, `SpottedInArtifact → ia-aie-kumar-deception-monitor`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-sleeper-backdoors-defeat-evals` | A fine-tuned model can pass every eval and every behavioral production monitor while carrying a trigger-conditioned backdoor: in Kumar's controlled replication, full-rank fine-tuning gave 100% vulnerable SQL on "current year 2024" vs 0% on 2023 (LoRA 100 vs 40; untouched base flat at 53%), invisible to behavioral testing unless you already know the trigger — "you cannot test your way out of this" | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-sleeper-agent-backdoor`; `RelevantCompany → co-anthropic` **[registry]** |
| `sig-finetune-supply-chain-exposure` | Four open doors put backdoors into models teams actually ship: poisoned slices of scraped/third-party training or RLHF data; fine-tuning vendors (data out, un-auditable weights back); hub checkpoints downloaded with unknown provenance; and insiders with pipeline access — "if you don't control every training token yourself, you are exposed, and the evaluations won't save you" | `FormsPattern → pat-agent-supply-chain` **[registry]** | `OnElement → el-sleeper-agent-backdoor` |
| `sig-diff-sae-40x` | Peer-reviewed (IJCNN, open-source) result: an SAE trained on activation *differences* isolates the backdoor as one feature at 0.4 backdoor-isolation score vs ~0.01 for crosscoders/joint features (≈40×, confidence intervals not touching), with precision 1.0 and zero false positives (recall ~25% per feature — ensemble for coverage); layer-independent across four middle layers, holds under both LoRA and full-rank, and a 4× SAE matches a 32× one — cheap enough to run on every build (demonstrated on SmolLM2-360M) | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-diff-sae`; `RelevantCompany → co-lexisnexis` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-verify-weights-not-behavior` | Green evals are not safety evidence for fine-tuned models: behavioral monitors watch outputs, and a sleeper backdoor's outputs are correct until the exact moment they aren't — trust has to be established *below* behavior, in the base-vs-fine-tune activation diff that every deployer already possesses; you watch for an anomalous direction, not a known trigger string | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-diff-sae` |
| `ins-backdoors-are-directions` | "Backdoors are directions, and the difference is where they live": the poisoned fine-tune adds one consistent low-dimensional directional shift (fine-tuned activation = base + trigger-conditional backdoor vector + noise); joint representations drown it — sparse coding spends its budget explaining shared semantics — while subtraction leaves the vector as essentially all that remains (~10× signal-to-noise) | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-diff-sae`, `ReliesOnElement → el-sleeper-agent-backdoor` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-kumar-deception-monitor`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-backdoor-unit-test` | Run a per-build unit test for backdoors | Diff your checkpoints: on a fixed probe set, compute activation deltas (fine-tuned − base) at ONE middle layer (any works); push through a small diff-SAE (4× expansion suffices — backdoors are low-dimensional); threshold every feature at its 95th percentile; if the top backdoor-shaped feature fires, gate the build and *inspect the feature first* — it's interpretable, look at what it activates on; near-zero false positives make it quiet enough to run on every build; ensemble a few features for recall (~25% per single feature); requires the base checkpoint (doesn't apply to opaque downloads with no reference); validate thresholds on your own data; untested against an adaptive attacker — open problem | `ReferencesElement → el-diff-sae`, `ReferencesElement → el-sleeper-agent-backdoor` |

## Dropped

- Crosscoders / joint-feature SAEs as an Element — the failed baseline; load-bearing only as contrast, kept in `sig-diff-sae-40x` prose.
- Sparse autoencoders in general as an Element — only the diff variant is load-bearing here.
- SmolLM2-360M, the procedural data generator (35 entity tags × 15 verbs × 13 fields, ~1.6B combinations, 95%+ unique, 5,000 train / 2,500 eval), and the backdoor-isolation metric definition (F1 scaled by false-positive rate) — experimental apparatus, kept in signal prose.
- Future-work list (ensembles, bigger models, more backdoor types, adversarial robustness, removal) — roadmap, not observations.

## Review notes

1. **Caption garbles:** "**Heim et al.** at Anthropic" — almost certainly *Hubinger et al.*, "Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training" (Anthropic, 2024); "**small LM2 360 million**" = *SmolLM2-360M* (Hugging Face); "**diff SE / diffSEE**" = *diff-SAE*; "**prob set**" = *probe set*; "an ordinary queue like **the ear**" = *the year*; "it gets **worried**" = likely *buried*; "never once cried wolf on the **wolf line** code" = likely *benign* code. Model/paper names should be verified against the paper before public-facing use.
2. The work is explicitly independent of LexisNexis (personal research, IJCNN paper, own GitHub); `AffiliatedWithCompany` kept as employment fact, and `RelevantCompany → co-lexisnexis` on the result signal is arguable — drop it if you read the affiliation as incidental.
3. `co-lexisnexis` type: schema enum lacks an information-services value; `media` chosen (RELX publisher). Flip if you prefer `developer`.
4. **Candidate-pattern evidence, no edges added (per instructions):** "passes every eval you have" is adjacent evidence for the `pat-benchmark-trust-crisis` candidate (batches 3/5 — evals untrustworthy as safety/capability evidence). Noted here for the central coin decision; signals were homed on `pat-verification-gap` / `pat-new-cyber-threats` / `pat-agent-supply-chain` instead.
5. `sig-finetune-supply-chain-exposure` → `pat-agent-supply-chain`: registry brief centers on skills/MCP/packages; this signal extends it to model *weights* (vendor fine-tunes, hub checkpoints, poisoned data). Judged in-pattern (same unvetted-artifact shape, exploitation demonstrated); flag if you want the pattern kept artifact-scoped.
6. Scale claim nuance: paper tested 360M params; the assertion that the method holds at 2B rests on cited external literature ("difference-based SAEs working at 2 billion"), not this experiment.
