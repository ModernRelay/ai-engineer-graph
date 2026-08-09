# SPIKE extraction — "Modern Post-Training: A Deep Dive" (Will Brown, Prime Intellect) — FOR REVIEW

Source transcript: `transcripts/brown-prime-intellect-post-training.txt` (auto-captions — quotes are paraphrases, not verbatim; "Primed and Loaded" throughout the captions = **Prime Intellect**).
Video: https://youtu.be/V-EDrhIhHzQ — AI Engineer World's Fair, published 2026-07-13.
`stagingTimestamp` for the artifact and all signals: 2026-07-13 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-brown-modern-post-training` | Modern Post-Training: A Deep Dive (Will Brown, Prime Intellect — AI Engineer World's Fair) | youtube | https://youtu.be/V-EDrhIhHzQ |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-will-brown`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-will-brown` | Will Brown (leads applied research at Prime Intellect; author of the Verifiers RL-environments library) | `AffiliatedWithCompany → co-prime-intellect` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-prime-intellect` | Prime Intellect | developer | Open-source AI research infrastructure company ("open superintelligence stack"): global GPU marketplace (10,000+ GPUs), Prime RL training framework, Verifiers environments + Environments Hub, hosted training/lab platform, Intellect model series; <40 people, SF-based |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-verifiers` | Verifiers (V1) | framework | training | Prime Intellect's open-source library for RL environments and evals; V1 overhaul decomposes an environment into composable task set (agent-agnostic data + rules), harness (default tool-loop, or real CLI agents like Codex / Claude Code / OpenCode / mini-SWE-agent / RLMs), and runtime (local, Docker, or sandbox layer); repo: PrimeIntellect-ai/verifiers |
| `el-prime-rl` | Prime RL | framework | training | Prime Intellect's async-from-the-ground-up open-source RL training framework on a TorchTitan base: orchestrator decouples inference and trainer as separate servers; FP8, wide expert parallelism, disaggregated prefill, pluggable loss/algorithm registry; also runs as a hosted platform (multi-tenant LoRA today, full fine-tuning rolling out) |
| `el-harness-interception` | Harness interception server | concept | training | RL-integration pattern where a real, unmodified production harness is pointed at a fake OpenAI/Anthropic-compatible base URL; the server intercepts each request (log probs, temperature, dialect translation, renderer) and routes it to the trainer's inference server — the harness never knows it is doing RL, so training and deployment use identical agent code |
| `el-on-policy-distillation` | On-policy distillation | technology | training | Post-training algorithm family where the student does rollouts in an environment but the score is the teacher's log-likelihood over those rollouts rather than a reward; standard recipe for merging per-environment RL experts (trained from one base model) into a single checkpoint, plus variants like self-distillation with hints |

Element edges:
- `el-verifiers`, `el-prime-rl` `DevelopedByCompany → co-prime-intellect`
- all four `IdentifiedInArtifact → ia-aie-brown-modern-post-training`
- `el-verifiers` `UsesElement → el-harness-interception`; `el-verifiers` `UsesElement → el-mcp` **[registry]** (MCP as back-end for tools and LLM-backed user simulators); `el-prime-rl` `UsesElement → el-verifiers`
- `el-recursive-language-models` — reused, defined in `shashi-superagentic-rlm-codebases.md` (this talk names RLMs as a supported harness class).

## Signals (5 new)

All: domain `training`, `SpottedInArtifact → ia-aie-brown-modern-post-training`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-frontier-rl-run-50k` | Concrete cost floor for frontier-scale custom RL: on latest Prime RL, a GLM-5 step on 28 nodes takes <5 min at 131K context for long-horizon coding tasks — a 1,000-step run in 3 days for ~$50K at rental prices, i.e. what some enterprises spend on API tokens in a month | `FormsPattern → pat-sovereign-ai` **[registry]** | `RelevantCompany → co-prime-intellect` |
| `sig-open-superintelligence-stack-real` | "A year ago 'open superintelligence stack' felt like marketing; now it's just what it is" (paraphrase): open models are superhuman at many things, and a full open stack exists to train/deploy your own — 10,000+ GPU marketplace, Prime RL, Verifiers + Environments Hub, hosted lab; customers train models on their own production workflows | `FormsPattern → pat-sovereign-ai` | `RelevantCompany → co-prime-intellect` |
| `sig-environments-become-the-unit` | Environments (task set + harness + runtime) are consolidating into the single unit of post-training: the same package drives evals, SFT data generation, RL, and distillation; Verifiers V1 was rearchitected because agent use cases outgrew the simple tools-in-a-loop pattern toward real CLI-agent harnesses | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-verifiers` |
| `sig-harness-unaware-rl` | Production harnesses now do RL without modification: the interception-server pattern gives each rollout a fake OpenAI/Anthropic-compatible endpoint, so "the harness doesn't know it's doing RL" (paraphrase) — collapsing the gap between the trained setting and the deployed setting | `FormsPattern → pat-harness-over-model` | `OnElement → el-harness-interception` |
| `sig-posttraining-algorithm-wave` | "It is the age of research indeed" (paraphrase): a rapid wave of post-training algorithms within months — on-policy distillation, self-distillation, Echo-style world-modeling RL, MaxRL, DPPO — pushed Prime RL to refactor into a pluggable loss/algorithm registry (rollout source × advantage definition) so new papers become config entries, not forks | `FormsPattern → pat-accelerated-research` **[registry]** | `OnElement → el-prime-rl`, `OnElement → el-on-policy-distillation` |

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-evals-are-environments` | Evals and environments are the same artifact: building evals for model min-maxing (Opus vs Sonnet vs GPT, intelligence vs dollars) already produces the unit needed for post-training — so eval investment opens a flywheel where your custom model keeps improving on real-world signal alongside the frontier, with training compute amortized as a small fraction of inference spend | `HighlightsPattern → pat-sovereign-ai` | `ReliesOnElement → el-verifiers` |
| `ins-async-off-policy-bargain` | Agent rollouts are long-tailed (30 s to 3 h for coding tasks), so synchronous on-policy RL means always waiting on the slowest rollout; accepting bounded off-policyness (~16 steps average, DPPO-stabilized to thousands of steps) decouples forward progress from rollout latency and lets sandbox boots, judge grading, and weight sync overlap without wasting GPU | `HighlightsPattern → pat-accelerated-research` | `ReliesOnElement → el-prime-rl` |
| `ins-tokens-vs-messages-duality` | Retokenization is many-to-one, so message-space and token-space silently diverge (chat templates stripping newlines forces off-policy mismatches or phantom branches) — an unavoidable systems problem at agentic-RL scale that explains why stateful model APIs exist; renderers (standalone library, in the lineage of OpenAI Harmony) turn chat templates into programmable artifacts maintaining both streams | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-prime-rl` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-brown-modern-post-training`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-group-variance-rewards` | Shape rewards with group-level variance, not absolute targets | You can't know the optimal chain-of-thought length per problem up front (it changes per task and as the model improves); instead exploit multiple rollouts per group — e.g. conciseness bonus to the shortest correct answers alongside a correctness reward; keep group rewards first-class (pairwise judging, ranking) rather than assuming rollouts are independent | `ReferencesElement → el-verifiers` |
| `how-experts-then-distill` | For multi-domain models: train RL experts, then distill | When one model must be good at several environments, train individual RL experts on top of the same base model, then on-policy-distill the teachers into a single checkpoint — generally more reliable than joint multi-environment RL | `ReferencesElement → el-on-policy-distillation` |
| `how-decouple-rl-systems` | Pull the RL stack apart into client-server pieces | Run inference, trainer, and orchestrator as separate processes that only consume from each other (no shared GPUs); environments as engines that send requests/batches over APIs; scaling concerns then decouple (N environments, M inference replicas, sandboxes or none) and the same environments double as standalone evals — avoid folding training+inference into one logical stack | `ReferencesElement → el-prime-rl` |

## Dropped

- Renderers as a separate Element — load-bearing but captured inside `ins-tokens-vs-messages-duality`; promote to `el-renderers` at review if it recurs.
- Task-set integrations (Hugging Face datasets, Harbor, NeMo Gym, "Open Ended" [garble?]), UV-script runtime pattern, TOML/Pydantic config — prose-level detail.
- Multi-tenant LoRA hosted platform mechanics, hiring/company news — not signals.
- GLM-5/GLM-5.2 and Kimi K2.5/2.6 model support — kept as prose in `sig-frontier-rl-run-50k`; no new element (registry has `el-glm-52`, `el-kimi-k25`).

## Review notes

1. **Caption garbles**: "Primed and Loaded" = Prime Intellect (confirmed by "prim and elect AI / verifiers" = PrimeIntellect-ai/verifiers on GitHub); "VLUM" = vLLM; "Torch Titan" = TorchTitan; "JLM" = GLM; "Swix" = swyx; "Mythos" matches registry `el-claude-mythos-preview` (passing model-choice mention, no edge). "Echo paper" and "Max RL paper" kept as-heard — verify exact paper names before publication.
2. Deep-technical talk per the brief: systems detail (FP8, router replay metadata, context parallelism, KV offloading, balloon of parallelism options) deliberately compressed into element briefs rather than signals.
3. `sig-frontier-rl-run-50k` and `sig-open-superintelligence-stack-real` are both vendor self-claims from the speaker's own company — standard for practitioner talks, but weight accordingly.
4. `ins-async-off-policy-bargain` pattern link is debatable (`pat-accelerated-research` chosen as it's about research-iteration speed); `pat-harness-over-model` is the alternative.
