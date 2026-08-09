# SPIKE extraction — "Agents Building Agents" (Alfonso Graziano, Nearform) — FOR REVIEW

Source transcript: `transcripts/graziano-nearform-agents-building-agents.txt` (auto-captions — quotes are paraphrases, not verbatim; ~4.7k words).
Video: https://youtu.be/aHhB3sjGjkI — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact and all signals: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-graziano-agents-building-agents` | Agents Building Agents (Alfonso Graziano, Nearform — AI Engineer World's Fair) | youtube | https://youtu.be/aHhB3sjGjkI |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-alfonso-graziano`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-alfonso-graziano` | Alfonso Graziano (tech lead at Nearform on AI agentic projects; O'Reilly author, "Learning AI Native Software Engineering") | `AffiliatedWithCompany → co-nearform` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-nearform` | Nearform | developer | Software services/consultancy; supports client teams adopting AI-native engineering and runs agentic delivery projects |

## Elements (2 new)

All new elements `IdentifiedInArtifact → ia-aie-graziano-agents-building-agents`.

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-autoagent` | AutoAgent | framework | harness | Graziano's eval-gated agent-optimization loop, Karpathy's autoresearch applied to agents instead of ML models: a coding agent (Claude Code) rewrites a target agent — system prompt, tools, tool logic — one hypothesis per git branch, runs the eval suite, continues from improvements and rolls back regressions, keeping a cross-run memory file and per-hypothesis reports.md; the human steers via a markdown job spec and hypothesis review |
| `el-golden-dataset` | Golden dataset | concept | harness | SME-co-authored suite of input → expected-output cases (outputs can be text, tool-call expectations, parameters, or call chains) plus scorers producing an accuracy number — "a test suite in a non-deterministic scenario"; serves simultaneously as baseline, regression suite, and the optimizing agent's objective function; production failure modes are folded into it continuously |

Element edges: `el-autoagent` `DevelopedByCompany → co-nearform`, `UsesElement → el-claude-code` **[registry]**, `UsesElement → el-golden-dataset`, `ExemplifiesPattern → pat-accelerated-research` **[registry]**.

Registry elements referenced (edges only, no new nodes): `el-autoresearch` (Karpathy's loop, cited as the template), `el-claude-code`, `el-harness-engineering`.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-graziano-agents-building-agents`, `SourcedFromSource → source-aie-yt` **[registry]**, domain `harness`.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-autoagent-eval-selfimprovement` | AutoAgent took a naive Mastra hello-world agent from 18% → 83% eval pass rate in ~10 autonomous iterations, and lifted an already human-optimized production agent from 67% → 86% "without cheating" — finding edge cases, improving system prompt and tool descriptions, and fixing tool logic in ways the humans hadn't found (+10% on internal benchmarks) | `FormsPattern → pat-accelerated-research` **[registry]** | `OnElement → el-autoagent`, `el-autoresearch` **[registry]**; `RelevantCompany → co-nearform` |
| `sig-evals-gate-agents-building-agents` | The agents-building-agents loop is only safe because verification is externalized: golden datasets + scorers define success, and humans must explicitly forbid the optimizing agent from editing the golden dataset or the scorers to make evals pass | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-golden-dataset` |
| `sig-nearform-trace-clustering-loop` | Nearform's production cadence: collect traces with user thumbs-up/down + comments or SME annotations (114 traces in the shown example); a skill instructs the coding agent to cluster failure modes, adversarially review them, and root-cause against the agent's actual code; SMEs triage; a coding agent then implements fixes — often an entire failure suite from one prompt when given context + regression tests — and every failure mode becomes a golden-dataset regression | `FormsPattern → pat-verification-gap` **[registry]** | `RelevantCompany → co-nearform`; `OnElement → el-golden-dataset` |
| `sig-harness-engineering-precondition` | Graziano attributes the whole capability to Harness Engineering: a spec-driven environment (every failure mode becomes a spec), quality gates (lint, unit tests, evals, LLM code review), context engineering, and observability — the environment around the coding agent, not the model, is what makes autonomous improvement reliable | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-harness-engineering` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-agents-are-just-software` | Because an AI agent is, from first principles, just software — an LLM in an agentic loop with tools and context — coding agents can build and improve other agents; the eval suite replaces the human in the inner loop, while humans move up to hypothesis-level steering and SME triage | `HighlightsPattern → pat-accelerated-research` **[registry]** | `ReliesOnElement → el-autoagent` |
| `ins-golden-dataset-is-the-flywheel` | The golden dataset is the load-bearing artifact of agent development — baseline, regression suite, and optimizer objective in one; a live-data loop that converts production failures into golden-dataset entries turns user pain into a compounding verification asset | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-golden-dataset` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-graziano-agents-building-agents`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-run-agent-optimization-loop` | Run an AutoAgent-style self-optimization safely | Define the job in markdown (objective, target repo, metrics, hard constraints); generate a baseline eval run + report first; one hypothesis per iteration, each on a fresh branch, one problem class at a time; run evals, write reports.md, update a global cross-run memory file; continue from improving branches, roll back regressions; explicitly forbid editing golden data/scorers to pass; cap iterations; review promising-but-failed hypotheses by hand and re-steer the next run | `ReferencesElement → el-autoagent`, `el-golden-dataset` |
| `how-live-trace-improvement-loop` | Improve production agents from live data | Instrument everything (interactions, tool usage, latency, tokens); collect user feedback (thumbs + comment on expected behavior) or SME trace annotations when user feedback is missing; roughly once per sprint (scale with trace volume), run failure-mode clustering with adversarial review + root-cause analysis into a markdown report; triage with SMEs into fix-now / fix-later / discard (false positives and intended behaviors exist); hand the coding agent the failure mode + traces + regression tests to implement the fix — or point AutoAgent at a failure cluster for draft PRs; append every confirmed failure mode to the golden dataset | `ReferencesElement → el-golden-dataset`, `el-harness-engineering` **[registry]** |

## Dropped

- Mastra (TypeScript agent framework used for the hello-world demo) — passing mention ("in this case, I'm using Mastra"); prose only.
- The demo agent's name — captions render it "mad agent"/"stat agent"; given the addition/multiplication eval examples this is likely "math agent". Not an entity.
- The naive contains-check evaluator, thumbs-up/down UI, JSON trace export — mechanics folded into knowhows.
- LinkedIn outro and book plug beyond the expert brief.

## Review notes

1. **`pat-adaptive-harness` / `pat-adaptive-software` candidate (NOT coined, per instruction) — specifics for the ledger:** AutoAgent is a concrete instance of the agent/harness being rewritten by an optimizer from eval and production signals — directly parallel to RELAI's optimizer-rewrites-the-harness and Mutagent's agents-mutating-agents (batch 8) and the ten Teije/Chandegra pair (batch 7). Distinctive specifics here: branch-per-hypothesis rollback discipline; +10% on an already human-optimized production agent (i.e., the machine found improvements humans missed); production failure clusters → specs → agent-implemented fixes. `sig-autoagent-eval-selfimprovement` is the natural rehome if the pattern is coined.
2. `FormsPattern → pat-accelerated-research` on sig-1: chosen because Karpathy's autoresearch (`el-autoresearch`, seed) is the talk's explicit template, extended from ML training code to agent code — AI improving AI systems. If review reads accelerated-research as strictly *scientific* research, rehome to `pat-harness-over-model` or hold for the adaptive candidate.
3. `el-golden-dataset` vs `el-eval-driven-development` [registry, batch 8]: adjacent — golden dataset is the artifact, EDD the methodology. Kept separate; merge call is central's.
4. AutoAgent is a cousin of `el-ralph-loop` [registry, batch 3] (loop-until-done) — differs by eval-gating, hypothesis tracking, and rollback; noted, no edge.
5. Attribution of AutoAgent: "I built something called AutoAgent," but the practice, internal benchmarks, and production agents are consistently "we/our projects" — `DevelopedByCompany → co-nearform` kept; drop the edge if you read it as personal work.
6. Garbles: "spectrum environment" ≈ "spec-driven environment" (confirmed by the surrounding spec/quality-gates list); "Mastra" assumed correct (real framework); "founding" = "finding". Karpathy cited by name — `exp-karpathy` **[registry]** exists but no edge type fits a citation.
