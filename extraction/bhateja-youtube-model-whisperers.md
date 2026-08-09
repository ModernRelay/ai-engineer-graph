# SPIKE extraction — "YouTube's Model Whisperers: How Evals and Prompts Shape Agent Behavior" (Preetika Bhateja & Daniel Bump, YouTube Ads) — FOR REVIEW

Source transcript: `transcripts/bhateja-youtube-model-whisperers.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/xyL2Ltkh-SA — AI Engineer World's Fair, published 2026-07-24.
`stagingTimestamp` for the artifact and all signals: 2026-07-24 (publish date).
Entities marked **[registry]** / **[batch1]** already exist — edges link to them, no new node.
Entities marked **[this batch]** are defined in a sibling file of the same evals-track batch.
Two presenters from the YouTube Ads team, which builds image and video models for ads. **Org choice:** YouTube is folded into `co-google` **[registry]** — see Review notes.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-bhateja-model-whisperers` | YouTube's Model Whisperers: How Evals and Prompts Shape Agent Behavior (Preetika Bhateja & Daniel Bump, YouTube Ads — AI Engineer World's Fair) | youtube | https://youtu.be/xyL2Ltkh-SA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-preetika-bhateja`; `ContributedByExpert → exp-daniel-bump`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-preetika-bhateja` | Preetika Bhateja (YouTube Ads; image and video models — covers rater programs, LLM raters, traces and the eval-system recap) | `AffiliatedWithCompany → co-google` **[registry]** |
| `exp-daniel-bump` | Daniel Bump (YouTube Ads — covers agent foundations, early intuition-based evals, hill climbing and launch readiness) | `AffiliatedWithCompany → co-google` **[registry]** |

⚠ The transcript names the second speaker only as "Daniel" (and the MC closes with "Daniel and Pratika"). The surname **Bump** comes from the video byline, not the captions — confirm at reconciliation.

## Companies (0 new, 1 registry)

| slug | name | type | note |
|---|---|---|---|
| `co-google` **[registry]** | Google | bigtech | reused for YouTube per the corp/lab precedent that already keeps `co-google` (corp) and `co-google-deepmind` (lab) as separate nodes. The talk consistently says "YouTube ads team" and never says Google — the flag and the alternative (`co-youtube`) are in Review notes |

## Elements (4 new, 5 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-intuition-first-evals` | Intuition-first evals (deliberate early "vibing") | concept | harness | Starting evaluation with deliberately non-scalable, intuition-based inspection of agent outputs instead of building the comprehensive eval first. Justified by three properties of the early stage: failure modes are obvious to the naked eye, prompt tweaks and radical architecture changes still produce large swings, and a premature scaled eval both hinders those changes and produces violent up-and-down measurement while you are calibrating the eval and the agent at the same time. The output of the phase is familiarity with the failure patterns — which is the input to building the real eval |
| `el-rater-rubrics` | Rater rubrics and templates | concept | harness | The operational kit that makes human rating usable: rubrics with explicit pass/fail criteria and worked examples so raters don't return "I'm not sure" or a pile of unknowns; rater templates; explicit training of scale raters and cross-functional teams on what is expected; multi-dimensional ratings when an output has independent quality axes (accuracy vs brand safety vs expectation match) rather than one verdict; and a **required written explanation with every rating**, single-side or side-by-side, because pass/fail alone says nothing about where the agent should improve — and the explanations themselves become training input |
| `el-online-evals` | Online evals | concept | harness | Evaluation that keeps running against the live system rather than a frozen offline suite: sampling pipelines over production, held-out test sets used sparingly and refreshed with production data, and explicit investment in online measurement so the eval distribution keeps matching real-world representation as use cases evolve |
| `el-launch-readiness-gate` | Launch-readiness gate | concept | harness | Agreeing the gatekeeping rule *before* it is needed: a stated launch criterion (a precision/recall threshold, or a use-case-appropriate metric when precision/recall is the wrong frame), an A/B diff or ablation to localize where a regression comes from, and an explicit classification of each regression as an acceptable trade-off or a critical failure rather than reading one aggregate number |
| `el-golden-dataset` **[registry]** | Golden dataset | — | — | reused, and the talk adds its growth curve: you do not need a massive golden set on day one — start with a few core tasks that name what you want the agent to be great at, expand toward a broad, highly curated set as use cases evolve, keep intra-team human agreement high on every case, include negatives (checking the agent did *not* do the bad thing is as critical as checking it did the task), and cover each failure *pattern* with multiple examples |
| `el-agent-execution-traces` **[registry]** | Agent execution traces | — | — | reused: going beyond pass/fail to read the agent's reasoning trace — the only instrument that surfaced an agent detecting a legally-mandatory disclaimer and then deciding to remove it. Also used to spot-check *why* an LLM rater reached a verdict rather than trusting the verdict |
| `el-generator-validator-separation` **[batch1]** | Generator/validator separation | — | — | reused: an independent critique agent with a remediation loop, added on top of the optimized tool set as a self-correction mechanism that fills gaps the base tools cannot cover |
| `el-eval-driven-development` **[registry]** | Eval-driven development | — | — | reused: the eval is the instrument that proves the value of a change and makes ablation experiments possible — "the essential tool for climbing the quality ladder"; the suite is discovered and kept evolving rather than pre-written |
| `el-judge-human-calibration` **[this batch]** | Human calibration of model judges | — | — | reused (defined in `bril-characterai-evaling-video-slop.md`): a sampling pipeline that compares how a human or expert rater would rate a case against how the LLM rater rated it, and monitors the agreement/disagreement rate's trend as the calibration alarm |

Element edges: all four new elements `IdentifiedInArtifact → ia-aie-bhateja-model-whisperers`; the five reused elements likewise `IdentifiedInArtifact → ia-aie-bhateja-model-whisperers`.
`el-intuition-first-evals` `EnablesElement → el-golden-dataset` (the failure patterns learned here are what the golden set is built from); `EnablesPattern → pat-verification-gap` **[registry]**.
`el-rater-rubrics` `UsesElement → el-golden-dataset`; `EnablesElement → el-judge-human-calibration`.
`el-online-evals` `UsesElement → el-golden-dataset`; `EnablesPattern → pat-verification-gap` **[registry]**.
`el-launch-readiness-gate` `UsesElement → el-online-evals`, `UsesElement → el-eval-driven-development`; `EnablesPattern → pat-verification-gap` **[registry]**.

## Signals (5 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-bhateja-model-whisperers`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-google` **[registry]**.

| slug | name / brief | FormsPattern | OnElement |
|---|---|---|---|
| `sig-youtube-ads-reliability-three-part` | YouTube Ads' image/video model team states agent reliability as a function of three things — the agent's capabilities, its guardrails, and its evals — and orders the build accordingly: first a focused, strong set of LLM-friendly tools (optimize those *before* any agent-level eval), then an independent critique agent with a remediation loop to cover what the base tools can't, and only then the eval that proves changes and enables ablations. Reason given: generative outputs are non-deterministic, the same input can succeed once and fail once, and for their use cases behaviour in the wild has to be measured at scale rather than guaranteed | `FormsPattern → pat-harness-over-model` | `OnElement → el-generator-validator-separation`, `el-eval-driven-development` |
| `sig-premature-scaled-evals-hinder` | Counterintuitive practitioner finding from a frontier-scale team: jumping to scaled raters too early causes big swings in measured quality, because you are calibrating the eval while radically changing the model. Early "vibing" — non-scalable, intuition-based inspection of outputs — is faster at that stage, makes issues easy to spot, leaves prompt tweaks and architecture rewrites unencumbered by an eval that would hinder them, and yields the failure-pattern understanding needed to build the comprehensive eval later | `FormsPattern → pat-verification-gap` | `OnElement → el-intuition-first-evals` |
| `sig-rubric-disagreement-is-the-real-work` | The eval bottleneck is human agreement, not eval code — the team's own visual gag is that writing the eval is a small dot next to humans arguing over what the rubric should be. Raters hit edge cases nobody tested and come back asking how to rate them, while the team itself disagrees internally on pass vs fail. Their answer is rubric clarity with worked examples, rater training, and mandatory written explanations; six months ago teams were "still figuring out how to do this", and it is only now becoming mainstream | `FormsPattern → pat-verification-gap` | `OnElement → el-rater-rubrics`, `el-golden-dataset` |
| `sig-pass-rate-blind-to-instructed-violation` | A categorical pass-rate metric could not surface a hard instruction violation: the agent had been told repeatedly and explicitly that for legal reasons disclaimers can never be removed, and in edge cases it detected the disclaimer in an ad and removed it anyway — demonstrated on a public-parks ad whose "paid by" line the agent stripped. Only the reasoning trace showed the agent finding the disclaimer and then deciding to remove it; the aggregate percentage was silent | `FormsPattern → pat-verification-gap` | `OnElement → el-agent-execution-traces` |
| `sig-classical-ml-discipline-returns-to-agents` | Agents inherit the generalization limits of the ML systems underneath them, so classical discipline transfers directly: hold out a test set and use it sparingly, refresh it with production data, keep a dataset for edge cases and broader capabilities, test negatives as well as positives, invest in online evals so the data matches real-world representation — and judge on patterns rather than isolated runs, because tuning the prompt off one failing trace of a non-deterministic system is a trap | `FormsPattern → pat-verification-gap` | `OnElement → el-online-evals`, `el-golden-dataset` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-eval-and-agent-co-evolve` | The eval is not a fixed measuring stick held against a moving agent — the two hill-climb together. When a run misses the bar, the correct move may be to review the eval set, recompute precision/recall, adjust the rating guide, change the tooling, or change the agent; all five are moves in the same loop. The corollary is that an eval built too early and frozen becomes a brake on architecture change, which is why the deliberately non-scalable phase comes first and the comprehensive suite comes after the failure patterns are understood | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-intuition-first-evals`, `ReliesOnElement → el-eval-driven-development` |
| `ins-judge-on-patterns-not-runs` | With non-deterministic systems the tempting move — hyperfixating on one failing run and patching the prompt from its trace — is the trap. The unit of judgment is the failure *pattern*: the golden set needs multiple examples covering each pattern, and the question is how often the system fails on that pattern, not whether it failed on that example. Traces are for understanding *why* a pattern exists, not for deciding whether a change is warranted | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-golden-dataset`, `ReliesOnElement → el-agent-execution-traces` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-bhateja-model-whisperers`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-eval-maturity-sequence` | Sequence eval investment: tools first, intuition second, scale last | Optimize the agent's tool surface — focused, strong, LLM-friendly — before building any agent-level eval; add an independent critique agent with a remediation loop to cover base-tool limitations; start evaluation with intuition-based inspection of a few core tasks you can name as the primary targets, accepting that it doesn't scale; keep the radical changes (architecture rewrites, big prompt swings) in that window while the eval isn't yet a constraint; grow to a golden set that covers broad use cases, tests negatives, and carries multiple examples per failure pattern; only then bring in scaled raters and LLM raters; expect the whole suite to keep evolving with the product — an MVP-stage eval and a production-rollout eval should not look the same | `ReferencesElement → el-intuition-first-evals`, `ReferencesElement → el-golden-dataset`, `ReferencesElement → el-generator-validator-separation` |
| `how-human-rater-program` | Run raters as a program, not a queue | Reach strong intra-team agreement on what "pass" means before anything leaves the team; ship rubrics with explicit criteria and worked examples covering the edge cases raters will actually hit; provide rater templates and invest in explicit training sessions on what you expect from them; require a written explanation with every rating, in both single-side and side-by-side setups, and use the explanations to locate what the agent is missing and to train it; use multi-dimensional ratings when an output has independent axes (accuracy, brand safety, expectation match) instead of forcing one pass/fail; when you move to LLM raters, run a sampling pipeline comparing human and LLM verdicts and watch the agreement-rate trend; spot-check the LLM rater's reasoning rather than trusting its verdict | `ReferencesElement → el-rater-rubrics`, `ReferencesElement → el-judge-human-calibration`, `ReferencesElement → el-agent-execution-traces` |
| `how-launch-readiness-evals` | Decide the gate before you need it | Agree the gatekeeping rule and launch criterion early — a precision/recall threshold, or a different metric where precision/recall is the wrong frame (a model eval's metric is not the usual one); run an A/B diff or ablation to localize where a regression is coming from; classify each regression explicitly as an acceptable trade-off or a critical failure instead of reading one aggregate number; keep a held-out test set, use it sparingly, and refresh it with production data; invest in online evals so what you measure matches real-world representation; make the eval representative of what you want the *product* to be great at, and re-derive that as the product's stage changes | `ReferencesElement → el-launch-readiness-gate`, `ReferencesElement → el-online-evals`, `ReferencesElement → el-eval-driven-development` |

## Dropped

- The specific ads use case (are these ads accurate, brand safe, as expected) — used as the example of multi-output rating; folded into `el-rater-rubrics` rather than coined as a domain element.
- The Q&A answer on judge calibration — the speaker declines to describe the benchmarking system ("I can't go into details"), and points back to the disagreement-rate and sampling-pipeline material already captured. No separate signal.
- The hill-climbing stack diagram (human eval → below bar → review eval set / precision-recall / adjust rating guide / adjust model, agent, tooling → iterate) — captured as `ins-eval-and-agent-co-evolve` rather than as its own element; it is the same loop `el-eval-driven-development` already names.
- "Scale raters" as a vendor/product reference — the transcript's "scale raiders"/"scale raers" reads as generic outsourced rating capacity, not necessarily Scale AI; deliberately not resolved to a company, no node.

## Review notes

1. **YouTube → `co-google` (flagged decision).** The talk never says "Google" — it says "the YouTube ads team" throughout, and the title treats YouTube as the org. Reused `co-google` anyway, on the corp/lab precedent already in the registry (`co-google` vs `co-google-deepmind`) and to avoid a third Google-family node. The alternative is coining `co-youtube` (type `media`) and edging both experts to it, with `co-youtube` as a subsidiary of `co-google` — the schema has no ownership edge, so that relationship would live in prose only. If you ever want per-product-org resolution across the corpus, coin it; otherwise the fold is the cheaper choice. Decide at reconciliation.
2. **Second speaker.** The transcript gives only "Daniel"; the video byline gives **Daniel Bump, YouTube Ads**. `exp-daniel-bump` follows the byline. If you'd rather not carry byline-sourced names, the fallback is to drop the node and keep a single-expert artifact (precedent: the unresolved co-presenters in `ung-lyft-evals-that-matter.md` and `raskar-mit-agentic-web.md`).
3. **Caption garbles**: "eval"/"e-vals"/"EVO"/"vowels" → evals; "raiders"/"raers" → raters; "wipe code"/"why eval" → vibe code / vibe eval (the speaker corrects herself mid-sentence); "PM and GX" → likely PM and UX; "Pratika" → Preetika; "hill climbing"/"climbing the quality ladder" are used interchangeably. No technical term is unresolvable.
4. **Practitioner-testimony talk.** No dated external facts, no products announced, no numbers — all five signals are testimony about practice inside one team. The distinctive, corpus-novel claims are `sig-premature-scaled-evals-hinder` (an argument *against* early rigorous evals from a frontier-scale team) and `sig-rubric-disagreement-is-the-real-work`; the rest is well-corroborated practice. If your signal bar is external verifiability, keep those two plus `sig-pass-rate-blind-to-instructed-violation` and drop the others to prose.
5. **Corpus adjacency, no new elements needed.** This talk restates from an independent team a lot of what `ung-lyft-evals-that-matter.md` (judge validation, expert-built rubrics), `sanftl-mutagent-agentic-ai-engineer.md` (eval-driven development), `graziano-nearform-agents-building-agents.md` (golden dataset) and `gupta-chopra-closed-loop-multimodal-evals.md` (this batch — human labels as ground truth, precision/recall gates) already carry. That convergence is itself the finding; the reuse edges above are the way it shows up in the graph.
6. **`el-judge-as-classifier` [registry] considered and not edged** — the talk uses precision/recall on the *eval set* for launch readiness, not as a method for validating the judge itself, which is the registry element's specific claim. `el-launch-readiness-gate` carries the precision/recall material instead. Revisit if you decide the two are one node.
7. **Pattern candidates — none advanced.** Nothing here moves `pat-benchmark-trust-crisis` (the rubric-disagreement material is about defining ground truth, not about benchmark trust collapsing), `pat-ai-native-org`, or the adaptive-harness pair. Recorded so the absence is deliberate.
