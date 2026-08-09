# SPIKE extraction — "Build Evals That Actually Matter" (Nick Ung, Lyft) — FOR REVIEW

Source transcript: `transcripts/ung-lyft-evals-that-matter.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/3z2uT5aDx_Y — AI Engineer World's Fair, published 2026-07-19.
`stagingTimestamp` for the artifact and all signals: 2026-07-19 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Two presenters: Nick Ung plus a teammate whose name the captions garble ("Ashe"/"Aka"/"Ash") — see Review notes.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-ung-evals-that-matter` | Build Evals That Actually Matter (Nick Ung, Lyft — AI Engineer World's Fair) | youtube | https://youtu.be/3z2uT5aDx_Y |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-nick-ung`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-nick-ung` | Nick Ung (data science manager, Lyft; ~6 years at Lyft, leads the customer-support AI agent team) | `AffiliatedWithCompany → co-lyft` |

## Companies (2 new, 2 registry)

| slug | name | type | note |
|---|---|---|---|
| `co-lyft` | Lyft | developer | appears as an enterprise operating a production multi-agent customer-support system for 1–2 years, not as an AI vendor; `type` is a judgment call (no "enterprise" enum) |
| `co-sierra` | Sierra | developer | Bret Taylor's AI customer-support agent company; authors of the tau-bench benchmark/paper that Lyft's offline simulator is modeled on |
| `co-microsoft` **[registry]** | Microsoft | — | reused: UserLM paper (fine-tuned user simulator, eval scores drop) cited as parallel evidence |
| `co-langchain` **[registry]** | LangChain | — | reused: Lyft's agents are built on LangGraph (see `el-langgraph`) |

## Elements (2 new, 2 registry)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-tau-bench` | tau-bench (τ-bench) | framework | harness | Sierra's benchmark/methodology for evaluating conversational agents: an agent LLM and a user-simulator LLM play out complete multi-turn conversations against a domain policy, graded on outcomes; also the source of the widely-cited stat that a model passing 60% of the time is self-consistent only ~25% of the time. Basis for Lyft's offline simulator |
| `el-judge-as-classifier` | LLM judge as classifier | concept | harness | Treating an LLM-as-judge as a trained binary classifier rather than a score generator: define pass/fail per metric, hand-label ~100 examples, split train/dev/validation (few-shots from train inform the judge prompt, iterate on dev, hold out test), then report the judge's precision/recall against human ground truth — plus ongoing re-calibration for criteria drift |
| `el-langgraph` **[registry]** | LangGraph | — | — | reused: Lyft's customer-support agents are LangGraph agents; simulator drives them against a user LLM |
| `el-context-rot` **[registry]** | Context rot | — | — | not edged — considered for the criteria-drift discussion but that is evaluator drift, not context staleness; listed here only to record the decision |

Element edges: `el-tau-bench` `IdentifiedInArtifact → ia-aie-ung-evals-that-matter`; `el-tau-bench` `DevelopedByCompany → co-sierra`; `el-judge-as-classifier` `IdentifiedInArtifact → ia-aie-ung-evals-that-matter`; `el-judge-as-classifier` `EnablesPattern → pat-verification-gap`.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-ung-evals-that-matter`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-lyft-frontier-user-sims-too-nice` | Lyft's first offline eval scored ~90% pass — too good to be true: frontier-lab models roleplaying users are trained to be helpful assistants and patiently over-explain, unlike real impatient, frustrated support users. Fine-tuning the user LLM on real Lyft verbatims made evals harder and scores drop — which is the desired outcome; Microsoft's UserLM paper reports the same effect | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-lyft`, `RelevantCompany → co-microsoft` |
| `sig-generic-judge-metrics-unactionable` | Lyft started with pre-built judge metrics (DeepEval: tool-usage appropriateness, response helpfulness, conversation naturalness, toxicity…) and found them noisy, too generic, and non-actionable — "if response helpfulness is 0.5, what do we do with it?"; nobody believed or gated on the scores. Replaced with binary, domain-expert-built rubrics (e.g. an "education rubric": escalated too soon vs. tried to educate too many times) | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-lyft` |
| `sig-lyft-eval-harness-investment` | After 1–2 years in production, Lyft's offline sims still live as scattered scripts across notebooks and analysis repos; the team's next investment is a systematic config-driven eval harness (YAML; primitives: task, dataset, persona, LLM adapter, evaluator) runnable at dev-time, pre-commit and CI/CD, editable by analysts and data scientists, not just engineers | `FormsPattern → pat-harness-over-model` | `RelevantCompany → co-lyft` |
| `sig-lyft-post-training-next` | Having exhausted much of the context- and harness-learning headroom, Lyft is starting to plan post-training: fine-tuning task models for customer support and framing a reward-modeling problem over years of accumulated real user signal to enable reinforcement learning | `FormsPattern → pat-harness-over-model` (as the boundary case: model learning picked up only after harness/context learning) | `RelevantCompany → co-lyft` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-validate-the-validators` | An unvalidated judge tells you nothing: judges must be treated as classifiers with human-labeled ground truth, measured precision/recall, and re-calibration as criteria drift — evaluation criteria are *discovered* by grading data, so evals must be co-developed with the system, not frozen up front. Chain of dependency: no looking at data → no labels → no judge validation → no idea if the agent pipeline works | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-judge-as-classifier` |
| `ins-eval-difficulty-is-the-point` | A too-easy eval (90% pass off polite simulated users) is a warning sign, not a win: realistic difficulty (real-verbatim-tuned users, adversarial personas — bypasser, refund-seeker, AI-skeptic) lowers scores but is the only way an offline eval predicts production and leaves room to improve the agent against hard users; scores only matter when they gate a decision (launch gates, regression gates with clear owners) | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-tau-bench` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-ung-evals-that-matter`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-validate-llm-judges` | Build judges you can trust: binary, expert-grounded, measured | Frame each metric as task success/failure (binary is easy to calibrate); build rubrics with domain experts, tied to business outcomes and decisions; hand-label ~100 examples, split train (few-shots for the judge prompt) / dev (iterate) / validation (check overfit); report judge precision/recall vs human labels; re-grade as criteria drift; add confidence intervals when a number gates a ship decision (an 84%→88% gain on 50 samples proves nothing) | `ReferencesElement → el-judge-as-classifier` |
| `how-realistic-user-simulation` | Make the user simulator as difficult as production | Don't prompt an LLM for "50 test queries": sample real production conversations, mutate criteria to cover golden paths and edge cases; fine-tune the user LLM on real user verbatims (terse, impatient, frustrated); define user personas (bypasser, refund seeker, AI skeptic) and world state (e.g. long-tenured luxury driver); accept that eval scores drop — that's the realism working | `ReferencesElement → el-tau-bench`, `ReferencesElement → el-langgraph` |
| `how-error-analysis-loop` | Run error analysis as a continuous loop, not a one-off audit | Log full traces (nodes ran, what the LLM saw, tool calls, tokens, latency; tools like LangSmith/Langfuse); deep-dive raw traces → pinpoint failure modes → keep only metrics that change a decision, delete the noise → form a fresh premise → repeat on a weekly/bi-weekly cadence; give domain experts annotation queues (not raw JSON) to label and feed ground truth back into datasets and judge validation; route findings into context learning (what the agent sees) and harness learning (prompts, tool schemas, routing, retries) | `ReferencesElement → el-judge-as-classifier` |

## Dropped

- DeepEval, LangSmith, Langfuse — tool mentions inside signals/knowhow; not load-bearing as Elements here. (Langfuse the company is defined in `schafer-langfuse-stop-burning-tokens.md`; this talk's mention is a passing list item, no edge.)
- Microsoft UserLM paper as its own InformationArtifact — cited secondhand; kept as prose inside `sig-lyft-frontier-user-sims-too-nice` + `RelevantCompany → co-microsoft`.
- "Model learning / context learning / harness learning" taxonomy as an Element — a useful trichotomy, but kept as prose in `how-error-analysis-loop` and `sig-lyft-post-training-next`.

## Review notes

1. Co-presenter garble: the second speaker (introduces themself as "Aka", later "Ash"/"Ashe", team member of Nick's who covers the LLM-judge half) could not be resolved to a real name from captions or the official listing (which credits only Nick Ung). No Expert node coined; add one at reconciliation if the video credits resolve the name.
2. "Taobench ... by the wonderful people at Sierra AI" → normalized to **tau-bench (τ-bench)**, the Sierra benchmark; "Microsoft user alen" → **UserLM**. Both are high-confidence garble fixes but worth a spot-check.
3. `sig-lyft-post-training-next` → `pat-harness-over-model` is the most debatable edge: the signal is about *leaving* harness-only learning. Read it as the boundary datapoint (harness first, model learning only after years of signal accumulation); alternatively drop the edge.
4. `co-lyft` type: schema enum has no enterprise/consumer category; `developer` chosen (they build their own agent system). Flip to `bigtech` if you prefer.
5. `co-sierra`: the talk says only "Sierra AI"; brief includes Bret Taylor from general knowledge, not the transcript — trim if you want transcript-only briefs.
