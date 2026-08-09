# SPIKE extraction — "Continual Learning for AI Agents: From Failures to Durable Improvements" (Soheil Feizi, RELAI) — FOR REVIEW

Source transcript: `transcripts/feizi-relai-continual-learning.txt` (auto-captions — quotes are paraphrases, not verbatim; "RELAI" renders as "Rely"/"rely.ai").
Video: https://youtu.be/2IxD9OB3XuQ — AI Engineer World's Fair, published 2026-07-05.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-07-05 (publish date).
Entities marked **[registry]** already exist — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-feizi-continual-learning` | Continual Learning for AI Agents: From Failures to Durable Improvements (Soheil Feizi, RELAI — AI Engineer World's Fair) | youtube | https://youtu.be/2IxD9OB3XuQ |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-soheil-feizi`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-soheil-feizi` | Soheil Feizi (founder & CEO, RELAI; associate professor of computer science, University of Maryland — both stated in-talk) | `AffiliatedWithCompany → co-relai`, `AffiliatedWithCompany → co-university-of-maryland` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-relai` | RELAI | developer | verifiable continual-learning engine for AI agents; site relai.ai (captions render "rely.ai" — verify domain spelling) |
| `co-university-of-maryland` | University of Maryland | research | Feizi's academic affiliation (CS department); precedent for universities-as-Company: `co-ucla` [seed], `co-mit-media-lab` [batch5] |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-continual-learning` | Continual learning for agents | concept | training | Agents improving from their own experience — acting, getting feedback, updating — without forgetting; updates can land in any of three layers: model weights (SFT / RL post-training / LoRA), harness (prompts, skills, tools, code, workflow), or memory (session/persistent facts and distilled skills) |
| `el-replayable-learning-environment` | Replayable learning environment | concept | training | Simulation + evaluation environment inferred from a single production log + feedback: synthetic users/personas and intents, mock-or-real tools, and inferred evaluators that define success — "inferring a distribution from one observation" so a one-off failure becomes a rerunnable, gradeable test of the pattern, not the instance |
| `el-verifiable-continual-learning` | Verifiable continual learning (VCL) | concept | training | RELAI's coinage: continual learning where every fix is proven to help and proven to break nothing that already worked — executable test (replay the failure), measured delta (score before/after), regression tests (prior tests still pass); four principles: replayability, holisticness, lifelongness, efficiency |
| `el-relai-vcl-engine` | RELAI VCL engine | product | training | RELAI's learning loop as a product: lifts logs/feedback/instructions into replayable learning environments, does root-cause analysis and routes fixes to the right layer (memory/harness/model), runs regression-aware optimization, and outputs a reviewable version-update pull request; added to an existing agent (any major framework, own LLM) with a one-time learning-harness setup plus two commands |

Element edges: `el-verifiable-continual-learning` `UsesElement → el-replayable-learning-environment`; `el-relai-vcl-engine` `UsesElement → el-verifiable-continual-learning`; `el-relai-vcl-engine` `DevelopedByCompany → co-relai`; `el-verifiable-continual-learning` `ExemplifiesPattern → pat-verification-gap` **[registry]**; all four `IdentifiedInArtifact → ia-aie-feizi-continual-learning`.

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-feizi-continual-learning`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | pattern edge | RelevantCompany |
|---|---|---|---|---|
| `sig-relai-vcl-engine-launch` | training | RELAI ships a verifiable continual-learning engine (usable today at relai.ai): logs/feedback/instructions lifted into replayable learning environments, a regression-aware optimizer routes fixes across memory/harness/model, output is a reviewable version-update PR; demoed on a tool-using support-agent benchmark with deterministic evaluators and deliberate regression traps — ~10% average score improvement from a single optimize loop (caption numbers garbled, see notes) | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-relai` |
| `sig-logs-are-not-learning-environments` | training | Practitioner claim: production gives you logs, not benchmarks — a session log plus feedback (automated critic or scarce human-expert review) is still untestable; and the standard optimizers presuppose what production lacks: SFT / RL post-training (DPO, GRPO, RLVR) and prompt-search methods (GEPA-style mutate-score-keep) all need benchmarks and explicit evaluators, so logs must first be lifted into replayable simulation + evaluation environments | `FormsPattern → pat-verification-gap` | — |
| `sig-continual-learning-not-finetuning` | training | Feizi (RELAI/UMD): agent continual learning ≠ model fine-tuning — the cheapest, fastest durable fixes usually land in the harness (prompts, skills, tools, code, workflow) and memory (facts, distilled skills) layers, with weight updates the expensive last resort; a good learning engine "asks for the smallest durable change at the right layer" (paraphrase) | `FormsPattern → pat-harness-over-model` | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-regression-inside-the-loop` | Regression-awareness must live inside the optimizer, not after it: fixing failure K+1 in isolation silently trades old wins for new ones, so "no regression on the K past learning environments" has to be a constraint of the optimization itself — and computed sub-linearly in K, or the loop stops being frequently runnable | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-verifiable-continual-learning` |
| `ins-vibe-fixes-hide-regressions` | Trace-to-harness fixing — handing a coding agent a log + feedback and asking it to improve the agent — is vibe-based twice over: unverifiable even on the triggering sample, and blind to hidden regressions elsewhere; testability via a replayable environment is what separates agent tinkering from agent engineering | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-replayable-learning-environment` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-feizi-continual-learning`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-lift-logs-into-learning-environments` | Lift failures into replayable learning environments | From one observed session: infer synthetic users/personas and intents; decide real vs mock tools (and what data feeds the mocks); infer evaluators that define success for the *pattern*, not the instance; then run candidate agent versions against the environment — everything downstream becomes testable. Environments can also be created from bare instructions ("caller is rude and adversarial") before any log exists | `ReferencesElement → el-replayable-learning-environment` |
| `how-route-smallest-durable-change` | Route each fix to the layer that explains the failure | One failure has many candidate repairs (worked example: agent cites a stale policy and skips escalation — could be a stale memory fact, an unoptimized prompt, a tool that doesn't normalize the policy, a missing workflow escalation gate, or a weak-reasoning model); do root-cause analysis and take the smallest durable change: memory writes (facts, distilled skills) cheapest/fastest → prompt/harness edits medium → weight updates (SFT/RL/LoRA) most expensive; score the fix before/after and run regression tests before shipping | `ReferencesElement → el-verifiable-continual-learning`, `ReferencesElement → el-semantic-episodic-memory` **[registry]** |

## Dropped

- Letta (captions: "LETA") and Mem0 (captions: "MemZero") — named only as example memory products; prose (daga precedent for mem0/memory.md).
- SFT / DPO / GRPO / RLVR / LoRA as separate elements — standard post-training methods, kept prose inside `sig-logs-are-not-learning-environments`.
- Skill distillation (compressing successful trajectories into reusable how-to skills) — folded into `el-continual-learning`'s memory-layer brief.

## Review notes

1. **Demo numbers garbled:** captions say the initial score is "78%", then "increases to 97% from 87%" — internally inconsistent. Brief keeps only the clean "~10% average improvement in one loop"; verify exact scores against the video before quoting.
2. **Company naming:** captions say "Rely"/"rely.ai"; the official listing says RELAI. Coined `co-relai`; the site is written relai.ai here but the domain spelling is unverified — check before seeding.
3. **Affiliation verified in transcript as instructed:** "I'm also an associate professor in the computer science department at University of Maryland." Coined `co-university-of-maryland` (research) for the second affiliation edge; drop it if universities-as-companies is unwanted.
4. **Pattern-candidate evidence (no coin, no edges):** the whole talk adds evidence to the batch-7 paired candidate `pat-adaptive-harness` / `pat-adaptive-software` — here the harness is continuously rewritten by an optimizer from production signals (harness-as-output-not-input, Chandegra's framing), now from a second independent vendor; see also the Mutagent file in this batch (third data point). Soft resonance with `pat-accelerated-research` (the loop as automated research on the agent itself) — not edged.
5. `el-continual-learning` coined as the umbrella concept (confirmed absent from registry before coining); `el-verifiable-continual-learning` kept separate because VCL is RELAI's stricter, specific claim (proof-carrying fixes). Merge to one node at review if the pair reads redundant.
6. **Unresolved garble:** "there are different methods like get past race to harness" — from context this introduces the trace-to-harness category; the mangled phrase may hide a method name (GEPA? a product?). Flagged. "GEPPO" is read as GEPA (prompt-evolution method) with moderate confidence.
7. `el-semantic-episodic-memory` **[registry]** reference in `how-route-smallest-durable-change` is an approximate fit (Feizi says session/persistent memory, facts + skills; the registry element is the closest existing memory concept) — drop the edge if reviewers find it a stretch.
