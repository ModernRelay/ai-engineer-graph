# SPIKE extraction — "Your Agents Need a Save Button" (Hamza Tahir, ZenML) — FOR REVIEW

Source transcript: `transcripts/tahir-zenml-agents-save-button.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/bZISsg7H7DA — AI Engineer World's Fair, published 2026-07-18.
`stagingTimestamp` for the artifact and all signals: 2026-07-18 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-tahir-save-button` | Your Agents Need a Save Button (Hamza Tahir, ZenML — AI Engineer World's Fair) | youtube | https://youtu.be/bZISsg7H7DA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-hamza-tahir`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-hamza-tahir` | Hamza Tahir (co-founder, ZenML) | `AffiliatedWithCompany → co-zenml` |

## Companies (3 new)

| slug | name | type | note |
|---|---|---|---|
| `co-zenml` | ZenML | developer | long-standing player in the ML orchestration space; recently launched Kitaru (open source), a durable runtime layer for agents |
| `co-doordash` | DoorDash | developer | appears as an enterprise practitioner (simulated replay of customer bots), not an AI vendor; `type` is a judgment call |
| `co-braintrust` | Braintrust | developer | AI eval platform; cited for its study on the "false economy" of naive model swaps |

## Elements (2 new, 2 registry / cross-file)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-checkpoint-replay` | Agent checkpoint-and-replay | concept | harness | Giving agents a "save button": a durable runtime *below* the harness/framework layer that snapshots full execution state at each step — code, variables, artifacts, environment (Docker image/sandbox) — connecting OTel-style observability spans to the actual execution. Enables replay-from-checkpoint with modifications (swap model, mock a tool, degrade intentionally), diffing outcomes against the grounded baseline, and cohort-scale what-if analysis on production runs: checkpoint → replay → diff → decide |
| `el-kitaru` | Kitaru | product | harness | ZenML's newly launched open-source tool implementing the durable-runtime/checkpoint-replay layer: timeline view of checkpoints with config/code/artifacts, replay-from-checkpoint CLI (skips checkpoints whose state is already held), side-by-side diff UI, cohort replay to JSON, and an MCP server so agents can query the runtime and analyze replay cohorts. ⚠ name garbled in captions — see Review notes |
| `el-mcp` **[registry]** | Model Context Protocol | — | — | reused: the Kitaru MCP server lets an agent read cohort-replay reports and recommend ship/don't-ship |
| `el-tau-bench` **[cross-file]** | tau-bench (τ-bench) | — | — | defined in `ung-lyft-evals-that-matter.md`; reused here for the self-consistency stat (a model passing 60% of the time is self-consistent only ~a quarter of the time) |

Element edges: `el-agent-checkpoint-replay` and `el-kitaru` `IdentifiedInArtifact → ia-aie-tahir-save-button`; `el-kitaru` `DevelopedByCompany → co-zenml`; `el-kitaru` `UsesElement → el-agent-checkpoint-replay`; `el-kitaru` `UsesElement → el-mcp`; `el-agent-checkpoint-replay` `EnablesPattern → pat-verification-gap` (verification against grounded production state); `el-agent-checkpoint-replay` `ExemplifiesPattern → pat-harness-over-model` (value delivered by a deterministic runtime layer beneath the model/harness).

## Signals (3 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-tahir-save-button`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-durable-runtime-category-emerging` | A new category of the agent stack is emerging: durable runtimes that sit below harnesses/frameworks, augment emitted traces with the surrounding code execution and state, and make runs replayable — ZenML (orchestration incumbent) just launched Kitaru into it; today's traces are read-only telemetry disconnected from the runtime, losing variables, filesystem, and code | `FormsPattern → pat-harness-over-model`; `OnElement → el-kitaru` | `RelevantCompany → co-zenml` |
| `sig-doordash-replay-simulations` | DoorDash (blog post dated June 1 [2026]) replays customer bots in a simulated environment grounded in production for what-if scenarios: analysis that took hours now takes ~5 minutes across hundreds of simulations, with 90% fewer hallucinations, and results staying within ~2 points of production observations | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-doordash` |
| `sig-naive-model-swap-false-economy` | Braintrust study + the tau-bench self-consistency stat (60% pass rate ≈ self-consistent only a quarter of the time): naive swaps to cheaper models look faster/cheaper on paper but can destroy value delivered (unresolved support requests); one replay is an anecdote — ZenML's own cohort analysis of a "cheaper and same result" single replay returned the verdict *don't ship* | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-braintrust` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-traces-alone-cant-answer-what-if` | Documents have had a save button since the 1980s; agents don't. A read-only trace in a far-away tool cannot answer "why did it do that / what if it had done otherwise" — only checkpointed runtime state can, and once production is checkpointing every step you already own the data needed to make the system better, cheaper, faster: evals become replays of reality (real runs, grounded baselines) instead of synthetic tests | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-agent-checkpoint-replay` |
| `ins-cohorts-not-anecdotes` | Because agents are non-deterministic and models are weakly self-consistent, a single successful replay proves nothing; decisions (model swaps, tool/policy changes) require cohort-scale replay distributions — and at thousands of replays the analysis itself must be delegated to agents via MCP/skills over a queryable runtime, with the human as final gate | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-agent-checkpoint-replay`, `ReliesOnElement → el-tau-bench` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-tahir-save-button`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-checkpoint-replay-playbook` | Evaluate changes by replaying production, not synthesizing tests | Model agents in a runtime that checkpoints state and can replay from code; start from real production runs, never synthetic; build cohorts that matter (most expensive, longest, riskiest); replay one change across the cohort (model swap, mocked tool, degraded dependency), diff against the grounded baseline, judge on value delivered not cost alone; never ship off one or two replays; be selective about what you replay (cohort replay is expensive); automate the loop — ideally an agent runs it — with a human in the loop at the end | `ReferencesElement → el-agent-checkpoint-replay`, `ReferencesElement → el-kitaru`, `ReferencesElement → el-mcp` |

## Dropped

- GPT-5 Nano — the cheaper model used in the demo swap; prose only.
- OTel/OpenTelemetry ("Odel") — mentioned as the span-emission standard; prose inside `el-agent-checkpoint-replay`.
- The chargeback-dispute/refund demo agent — illustration; folded into element/knowhow prose.
- DoorDash blog post as its own InformationArtifact — cited secondhand without URL; kept as a dated fact inside `sig-doordash-replay-simulations` (promote centrally if the post is located).

## Review notes

1. **Product-name garble (unresolved):** the tool is rendered "Kitaru", "Kitaro", and "Guitar Ru" across the captions. Slugged `el-kitaru` (most frequent form). Verify the real product name against ZenML's site/repo before seeding — the slug and name may need a rename.
2. DoorDash blog "1st of June" — year not stated in captions; inferred 2026 from talk context ("this conference is all about loops"). Verify when sourcing the post.
3. τ-bench self-consistency stat is attributed here to "the towel bench"; normalized to `el-tau-bench` (defined in `ung-lyft-evals-that-matter.md` — same-batch cross-reference, single node).
4. Company types: `co-doordash` as `developer` is a stretch (enum lacks an enterprise/consumer category), same call as `co-lyft`/`co-tesla`; flip at reconciliation if a convention lands.
5. Pattern call: no new pattern. "Durable runtime as an emerging stack category" was considered as a candidate pattern but is one talk's claim about one layer — parked on `pat-harness-over-model`, which it evidences well.
