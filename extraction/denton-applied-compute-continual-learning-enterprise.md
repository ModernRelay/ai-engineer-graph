# SPIKE extraction — "Bringing Continual Learning into Enterprises" (Samuel Denton, Applied Compute) — FOR REVIEW

Source transcript: `transcripts/denton-applied-compute-continual-learning-enterprise.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/ZTA0GwpAUak — AI Engineer World's Fair, **Continual Learning track**, published 2026-08-12.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-12 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the track's **enterprise-delivery talk**, and its most operationally concrete. Builds a 2×2 — offline/online *traces* against offline/online *hints* — locates where value accrues in each quadrant, then reports two measured results (a SWE-bench behaviour change from fully offline data; a hyperlink-format fix from online hinting) plus two techniques that made distillation work at all. Caption garbles: "hardens" → **harness**, "climate overall emails" → likely *climb overall evals*, "Qwen 3.5 thinking" → ⚠ version uncertain, "sweet bench"/"SWE-bench" → **SWE-bench**, "\{{}quote}" → quote marks, "amotized" → amortized.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-denton-continual-learning-enterprise` | Bringing Continual Learning into Enterprises (Samuel Denton, Applied Compute — AI Engineer World's Fair) | youtube | https://youtu.be/ZTA0GwpAUak |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-samuel-denton`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-samuel-denton` | Samuel Denton (leads the platform research team at Applied Compute; presents work he credits to colleagues — "a lot of the work was done by others, I just got to present it") | `AffiliatedWithCompany → co-applied-compute` **[registry]** |

## Companies (0 new)

Reused **[registry]**, edge-only:

| slug | reuse note |
|---|---|
| `co-applied-compute` **[b15]** | Second corpus appearance (after Feng's "Learning on the Job"). Substantial new facts: a platform research team; a four-quadrant distillation taxonomy; commercial posture of meeting enterprises "where they are" across the offline→online spectrum; published work on relevance-masked self-distillation; hiring for continual-learning research |

Not coined: the customer whose harness required a specific hyperlink format is described but never named.

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-distillation-spectrum` | The offline–online distillation spectrum | concept | training | The first axis. At the **offline** end, a single batch of production traces from an agent in the wild that you must learn from by hindsight. In the **middle**, a daily batch collected from a deployed model. At the **online** end, "the holy grail of continual learning" — a unified engine where serving and training collapse together: the model serves production traffic, produces a trace, learns from it, and serves the next request. Positioned commercially rather than aspirationally: most enterprises sit at the offline end today, some are willing to run the full flywheel, and the stated goal is to provide value across the whole spectrum |
| `el-hint-provenance-axis` | Offline versus online hints | concept | training | The second axis, and the file's genuine contribution to the batch's distillation thread. Distillation needs a teacher smarter than the on-policy student, which requires **privileged information — a hint**; the question is where the hint comes from. **Offline hints** derive from static data: known rubrics, general behavioural priors ("a customer-support agent too willing to give refunds"), or aggregate loss reports — independent of any particular rollout. **Online hints** are constructed dynamically *from* the online rollout, so the guidance is conditioned on what the model actually just did |
| `el-distillation-quadrants` | The four distillation quadrants | concept | training | Crossing the two axes. **Q1** offline hint + offline trace: apply a behavioural prior across a batch of production traces. **Q2** offline hint + online rollout. **Q3** offline trace with a single **on-policy step** — replay a production trace to a chosen moment, roll out one step from the current model without touching the environment, and hint against that step. **Q4** online hint + online trace: let the on-policy model finish, construct a hint from the full rollout, distil against it. Applied Compute focuses on **Q1 and Q4** — Q1 as day-one value requiring no replayable environment, Q4 as "our most scalable solution" and the complete flywheel. Framed with the caveat that these are spectrums drawn as boxes |
| `el-per-step-hinting` | Per-step hint injection | technology | training | The first of two techniques presented as what makes distillation actually work: rather than prepending a hint to the whole rollout, use a **judge to choose where in the rollout to inject it**, then distil on the next step or few steps rather than the entire trajectory — "that's really the moment in time you want the teacher to teach something to the student." Supported by the observation that the KL learning signal decays with distance from the hint |
| `el-relevance-masked-distillation` | Relevance-masked self-distillation | technology | training | The second technique, with a published write-up on the company's site: use an **LLM judge to select which tokens to learn from** in the teacher's output, because "the teacher model has preferences of certain connector words that are not really relevant to what we're trying to teach the student." Reported to improve learning of very out-of-distribution behaviour while reducing catastrophic degradation — i.e. it attacks the plasticity and stability sides simultaneously |

Element edges: all five `IdentifiedInArtifact → ia-aie-denton-continual-learning-enterprise`.
`el-distillation-quadrants` `UsesElement → el-distillation-spectrum`, `el-hint-provenance-axis`;
`el-per-step-hinting` `EnablesElement → el-distillation-quadrants`;
`el-relevance-masked-distillation` `EnablesElement → el-distillation-quadrants`;
`el-distillation-quadrants` `UsesElement → el-on-policy-distillation` **[registry, b5]**;
`el-hint-provenance-axis` `UsesElement → el-on-policy-self-distillation` — **cross-file edge within this batch**, see review note 2;
`el-distillation-spectrum` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**.

Reused elements (no new nodes): `el-on-policy-distillation` **[b5]**, `el-swe-bench` **[b11]** (the Q1 experiment's environment), `el-continual-learning` **[b8]**.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-denton-continual-learning-enterprise`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-applied-compute` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-enterprises-start-at-offline-traces` | training | The market read from a vendor selling into it: "this is sort of where a lot of enterprises are today" — they have production traffic and a pile of traces and say "figure out a way to make our agent better. It's clearly doing something, but it clearly can be better." The commercial framing is a spectrum rather than a product: **improve for free today** from a dump of offline production data, and **raise all ceilings tomorrow** once an online policy model is deployed and updating while serving. Some enterprises are already willing to run the fully online flywheel. A concrete picture of where continual learning actually sits in enterprise adoption, against a track full of frontier claims | — **HELD PATTERN-LESS** (`pat-continual-learning-turn` ledger) | `OnElement → el-distillation-spectrum`, `el-distillation-quadrants` |
| `sig-hint-provenance-is-the-second-axis` | training | The conceptual contribution: distillation's teacher must be smarter than the student, which requires privileged information, so **where the hint comes from** is a design axis independent of how online the traces are. Offline hints encode static behavioural priors and target specific known problems; online hints are constructed from what the model just did and therefore "can cater to a bunch of different behaviours" without enumerating them in advance. Crossing hint provenance with trace recency yields four working regimes rather than one method | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-hint-provenance-axis`, `el-distillation-quadrants` |
| `sig-offline-distillation-shifts-behaviour` | training | The Q1 measured result, and the surprising one. Goal: get a Qwen 3.5 thinking model on SWE-bench to stop taking up to 80 turns and call its submit tool before turn 40. Task-complete call rate rose from **~22% to ~60%** with the test pass rate flat (in fact slightly up), so the behaviour was added without regression. The surprise is mechanical: the rollout is conditioned on a production trace that **never called the tool**, so "the teacher doesn't force the tool call — it just starts to force the reasoning path towards the tool call without ever actually changing the tool call." Adding one on-policy step to an otherwise offline setup raised SWE-bench pass rate further | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-distillation-quadrants`, `el-swe-bench` **[registry, b11]** |
| `sig-online-hinting-beats-offline-on-ood` | training | The Q4 measured result, on a real customer constraint: a coding agent had to emit a hyperlink format dictated by a customer's harness, a format "very very out of distribution for previously post-trained models." Adding a format reward degraded overall coding performance; SFT on correctly-formatted traces did too. Online hinting — roll out, then inject a hint referencing *that* rollout ("in your prior rollout you formatted hyperlinks like this; next time format them this way") — moved correct formatting from **~15% to ~80%**, while applying the same static hint to every rollout climbed "far less." Direct A/B evidence that hint provenance, not hint content, carries the gain | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-hint-provenance-axis`, `el-distillation-quadrants` |
| `sig-distillation-without-golden-answers` | training | The methodological stance, offered as a standing frustration with the field: "a lot of distillation work is done assuming you have some kind of golden answer that you can distil into the model, and this is often not the case." Applied Compute's whole taxonomy is built to work **without a golden rubric per task** — behavioural priors and rollout-derived hints substitute for ground truth. Paired with the infrastructure prediction that closes the loop: "as the infra collapses between serving and training, we're automatically going to raise the ceiling continuously via online distillation" | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-hint-provenance-axis`, `el-distillation-spectrum` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-privileged-information-is-the-real-axis` | Read alongside the OPSD talk earlier in the same track, this file completes a shift in what distillation *is*: not compression of a larger model into a smaller one, but a general mechanism for converting privileged information into policy. Once that is the frame, the design questions become where privilege comes from, how much of it the student could plausibly have derived, and where in a trajectory to apply it — which is why both talks independently identify hint construction as the discipline that reward design was for RL. The 15%→80% online-versus-offline gap is the cleanest available evidence that *provenance* of the hint, not its content, carries the learning | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-hint-provenance-axis`, `el-distillation-quadrants` |
| `ins-behaviour-can-be-installed-from-hindsight` | The SWE-bench result shows a model being taught to take an action it never took in any training trace, because the teacher shaped the reasoning path leading toward the action rather than the action token itself. That decouples behaviour change from demonstration data and makes a large class of enterprise asks tractable from logs alone — no replayable environment, no golden answers, no new labelling. It also sets the boundary condition: what can be installed this way is behaviour reachable by reasoning the model already has, which is the same limit hint leakage describes from the failure side | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-distillation-quadrants`, `el-per-step-hinting` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-denton-continual-learning-enterprise`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-run-enterprise-distillation` | Run enterprise distillation from production traces | Locate your situation on two axes before choosing a method — how **online your traces** are (a one-time dump, a daily batch, or a live serving loop) and where your **hints** come from (static behavioural priors versus guidance constructed from the rollout just observed) — because the four combinations have genuinely different requirements and pay-offs; start in the offline-trace, offline-hint quadrant if you have nothing but logs, since it needs no replayable environment and can still install targeted behaviour changes; **do not assume golden answers**, as most real tasks have no per-task rubric — encode what good looks like as a behavioural prior instead; when you need broad improvement rather than one targeted behaviour, move to online hints constructed from each rollout, which adapt to whatever the model actually did and in measured comparison outperform applying one static hint to every rollout by a wide margin; cheat toward on-policy where you can — replaying an offline trace and rolling out a **single on-policy step** before hinting measurably beats the fully offline setup at almost no infrastructure cost; use a judge to pick **where** in the rollout to inject the hint and distil on the next step or few rather than the whole trajectory, since the KL learning signal decays with distance from the hint; mask irrelevant tokens with an LLM judge so you learn the behaviour rather than the teacher's connector-word habits, which improves out-of-distribution learning while limiting catastrophic degradation; and always track a non-regression metric alongside your target behaviour, since format rewards and naive SFT both degrade base capability in exactly the cases where the target behaviour is most out of distribution | `ReferencesElement → el-distillation-quadrants`, `el-hint-provenance-axis`, `el-per-step-hinting`, `el-relevance-masked-distillation` |

## Dropped

- **The "I assume you've had enough distillation by 3pm on a continual-learning day" preamble** — logistics, though it confirms the track ordering.
- **The metric definitions for the SWE-bench experiment** (task complete rate, test pass rate, and their intersection as SWE-bench pass rate) — method detail folded into `sig-offline-distillation-shifts-behaviour`.
- **The example hint text** ("you are near your 40-turn limit… finalize and verify your fix and then call this tool") — illustrative; the mechanism is in the KnowHow.
- **The hiring pitch and team acknowledgement** — logistics.

## Review notes

1. **The batch's best-measured vendor talk.** Two before/after results with non-regression controls (22%→60% task-complete with test pass rate flat; 15%→80% hyperlink formatting with an explicit offline-hint comparison arm), plus a stated negative result on the two obvious alternatives (format reward and SFT both degraded base coding performance). Compare with Hooker's talk in the same batch, which has stronger credentials and far weaker evidence.
2. **⚑ Cross-file edge emitted within this batch.** `el-hint-provenance-axis` `UsesElement → el-on-policy-self-distillation` (Malde/Trajectory). This is deliberate: the two talks are the same technique from two vantage points — Malde derives the algorithm and names its failure mode (**hint leakage**), Denton industrializes it and adds the provenance axis, per-step injection and relevance masking. Neither cites the other. **If review prefers strictly within-file edges, drop this one**; the relationship is also recorded here in prose.
3. **⚠ Notable convergence worth carrying to review.** Malde warns that hints containing underivable information teach the model to fake the reasoning; Denton reports success precisely by shaping the *reasoning path* rather than the target token. These are the same mechanism seen from the failure and success sides, arrived at independently on the same day. Together they are the strongest evidence in the corpus that hint design is becoming a named discipline — and a good anchor if `pat-continual-learning-turn` is coined.
4. **⚠ Verify before seeding.** "Qwen 3.5 thinking" is caption-sourced and the version is uncertain; the 80-turn/40-turn thresholds, the 22%→60% and 15%→80% figures, and the KL-decay claim are all single-mention. The relevance-masking blog post is referenced but not titled. The customer requiring the hyperlink format is unnamed, so the Q4 result cannot be independently attributed.
5. **Second corpus appearance for Applied Compute.** Feng's b15 talk ("Learning on the Job") argued the thesis; this one shows the delivery mechanics. Worth noting that the same company now supplies data points to both `pat-harness-over-model` (b15's BYOH training, per the registry's FINDING 1 claim-1 list) and to this batch's continual-learning ledger — **recommend widening `co-applied-compute`'s brief** at seeding to cover the platform-research function and the distillation taxonomy.
