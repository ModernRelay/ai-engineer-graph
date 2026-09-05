# SPIKE extraction — "FinOps for AI Agents: Who Spent All the Tokens?" (Tisha Chawla & Susheem Koul, Microsoft) — FOR REVIEW

Source transcript: `transcripts/chawla-koul-microsoft-finops-agents.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/GJX19pNhmSw — AI Engineer World's Fair, published 2026-08-22.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-22 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the same Microsoft pair as the earlier "agent failed in prod" talk, now on cost: the industry is **token-maxing** ("token billionaires"), and the agentic era has no cost control plane at the boundary where *code calls the model* — gateways cap and route per request, but runaway loops, sub-agent spawning and growing context happen at the **run** level. Their answer, **TokenOps**: an out-of-band governance plane that attributes every run, keeps a ledger, and enforces in the call path with *steer* actions (compaction, tool-output reduction, budget-aware instructions) before the *halt* of last resort. Benchmarked on browser-use and MetaGPT: average spend −78%, completion 67% → 96% versus plain throttling. Caption garbles: "Sushim"/"Sashim" → **Susheem**, "Disha" → **Tisha**, "port key" → **Portkey**, "light LLM" → **LiteLLM**, "metagp" → **MetaGPT**, "sub aents" → **sub-agents**, "cost in microns" → ⚠ unclear (cost in micro-units).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-chawla-koul-microsoft-finops-agents` | FinOps for AI Agents: Who Spent All the Tokens? (Tisha Chawla & Susheem Koul, Microsoft — AI Engineer World's Fair) | youtube | https://youtu.be/GJX19pNhmSw |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-tisha-chawla` **[registry]**, `exp-susheem-koul` **[registry]**.

## Experts (0 new)

Reused **[registry]**: `exp-tisha-chawla`, `exp-susheem-koul` — second corpus appearance (their earlier talk on why agents fail in production); both `co-microsoft`.

## Companies (0 new)

Reused **[registry]**, edge-only: `co-microsoft` — new facts: ships **TokenOps**, a runaway-token-governance plane for agents (out-of-band, tenant-resident control plane; public wiki updated regularly). Referenced, not coined: Uber (the "AI budget exhausted in four months" story), LiteLLM, Portkey, Cloudflare (request-level gateways), browser-use and MetaGPT (benchmark targets).

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-cost-control-surface-by-era` | The cost control surface, by era | concept | infra | SaaS era: the interface was UI and control was usage caps, seat limits, tiers. Cloud era: pay-as-you-go, control moved to auto-provisioning and autoscaling policies. Agentic era: cost is created at the model-call boundary, and there is **no control plane where code calls the model** — gateways (LiteLLM, Portkey, Cloudflare) offer hard caps and model-downgrade routing at the request level, which cannot see a runaway loop, sub-agent fan-out, or a context growing out of range |
| `el-run-level-token-governance` | Run-level token governance | concept | harness | First principles: the token is the unit of cost, so value must be seen in tokens too; cost is created at the model-call boundary; without **attribution** (which agent, which run, which user cohort) you can't control it; policies should fix problems **in place** (compact the context, cache, trim tool output, detect loops and lack of progress) and only **halt at a budget cap as the last resort**. Enforcement must be in the call path and cumulative across attributed runs, at the run layer not the request layer |
| `el-tokenops` | TokenOps | product | harness | Microsoft's runaway-token governance for agents. **Out-of-band plane** (doesn't touch your code): instrumentation (OpenTelemetry telemetry, cost, enrichment, attribution), accounting (a ledger of runs), enforcement (steer via policies; halt in place). **Bridge**: attribution to user dimensions; a framework-agnostic `boundary` annotation on any method that records input/output to the ledger *and* is the channel through which the control plane pushes actions down; a **governor** that applies only developer-allowed actions non-destructively; `wrap_complete` for model-provider objects. **Control plane** (in your tenant): segments (cohort budgets on floated dimensions), ledger, budgets (thresholds per time window), actions — **halt** (kill) or **steer** (allow / mutate / inject) — and policies binding them to segments or runs. Preview mode runs policies without enforcing. **Cost guard** predicts budget exhaustion from consumption and velocity and injects "be more succinct" into system instructions. Roadmap: a self-learning module that mines the ledger for uncaught failure modes and generates or tunes policies |
| `el-steer-not-halt` | Steer, don't halt | concept | harness | Throttling and circuit breakers kill runs regardless; steering fits the run inside its budget by changing agent behavior mid-flight (limit a RAG tool from 20 chunks to the 5 the model actually uses; compact context; inject budget awareness). On browser-use and MetaGPT across stress and hard scenarios: average spend down ~78% with the full policy suite, completion up from ~67% (throttling) to ~96%. The policy catalog covers spend management, context management (compaction, tool-output reduction), loop and progress detection |

Element edges: all four `IdentifiedInArtifact → ia-aie-chawla-koul-microsoft-finops-agents`.
`el-tokenops` `DevelopedByCompany → co-microsoft` **[registry]**;
`el-tokenops` `UsesElement → el-run-level-token-governance`, `el-steer-not-halt`, `el-opentelemetry` **[registry]**, `el-context-compaction` **[registry]**, `el-prompt-caching` **[registry]**;
`el-run-level-token-governance` `UsesElement → el-cost-control-surface-by-era`, `el-token-maxing` **[registry]**;
`el-cost-control-surface-by-era` `UsesElement → el-model-routing` **[registry]**;
`el-tokenops` `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-run-level-token-governance` `ExemplifiesPattern → pat-durable-execution` **[registry]**.

Reused elements (no new nodes): `el-token-maxing` **[registry]** (the culture being governed), `el-opentelemetry` **[registry]**, `el-context-compaction` **[registry]**, `el-prompt-caching` **[registry]**, `el-model-routing` **[registry]** (request-level downgrade routing as the insufficient incumbent).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-chawla-koul-microsoft-finops-agents`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-microsoft` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-agentic-era-has-no-cost-control-plane` | infra | "The most expensive question in AI today": you open the bill and can't trace which agent run produced it. Each software era had a control surface matched to its cost model (seat caps; autoscaling policies); the agentic era's cost is created where code calls the model, and today's gateways only cap or route per request — blind to loops, sub-agent fan-out and context growth. The missing layer is governance at the **run** | `FormsPattern → pat-harness-over-model` **[registry]**; `FormsPattern → pat-durable-execution` **[registry]** | `OnElement → el-cost-control-surface-by-era`, `el-run-level-token-governance` |
| `sig-token-billionaires-and-budgets-gone-in-months` | infra | The unbounded-consumption year: the industry "values token maxing" and people are "proud to call themselves token billionaires"; Uber's AI budget reportedly exhausted within four months; companies at "hundreds of millions of dollars within months or days"; runaway loops with no mechanism to stop them. The culture and the missing control plane are the same story from two sides | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-token-maxing` **[registry]**, `el-cost-control-surface-by-era` |
| `sig-steering-beats-throttling-78-percent` | harness | The measured claim: with TokenOps' full policy suite on browser-use and MetaGPT, average spend fell ~78% while completion rose from ~67% (plain throttling kills runs) to ~96% — because policies steer the run into its budget (compaction, tool-output trimming, budget-aware instructions, loop/progress detection) and halt only last. Cost control as an in-flight harness policy, not a kill switch | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-steer-not-halt`, `el-tokenops` |
| `sig-out-of-band-annotation-governs-any-framework` | harness | The integration shape: no code changes — a `boundary` annotation on any method (LangChain or otherwise) floats I/O to a tenant-resident ledger and receives control-plane actions, applied by a governor limited to developer-allowed actions; preview mode lets production teams tune thresholds before enforcing. Roadmap: the ledger feeds a self-learning module that generates and refines policies for failure modes not yet caught | `FormsPattern → pat-harness-over-model` **[registry]**; `FormsPattern → pat-continual-learning-turn` **[registry]** | `OnElement → el-tokenops`, `el-run-level-token-governance` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-cost-is-a-run-level-harness-problem` | The durable claim is where cost control belongs: not at the model gateway (per request) and not in the model (which cannot see its own budget), but at the run — the loop between agent, tools and sub-agents — where the same in-place mechanisms the harness already uses for quality (compaction, tool-output trimming, loop detection) double as cost policies. This makes FinOps a harness concern and explains why request-level gateways plateau at caps and downgrades | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-run-level-token-governance`, `el-steer-not-halt`, `el-cost-control-surface-by-era` |
| `ins-attribution-is-the-precondition-for-value-maxing` | Moving "from token maxing to value maxing" requires the ledger first: attribute every model call to a run, a user and a cohort, then budget at the cohort, then steer — because value can only be expressed in the unit you are charged in. The self-learning policy roadmap is the accumulation loop applied to spend: the ledger of what ran becomes the training signal for what to govern | `HighlightsPattern → pat-ai-native-org` **[registry]** | `ReliesOnElement → el-tokenops`, `el-run-level-token-governance` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-chawla-koul-microsoft-finops-agents`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-govern-agent-token-spend-at-the-run` | Attribute, ledger, steer, then halt | Treat the token as the unit of both cost and value; instrument the **model-call boundary** and attribute every call to an agent run and to user dimensions (cohorts) so budgets can roll up or drill down; keep a ledger of every run; put enforcement **in the call path and cumulative across runs**, not in a request-level gateway; write policies that fix problems in place — compact context, cache, trim tool output to what the model actually uses, detect loops and lack of progress, inject budget awareness when consumption velocity predicts overrun — and halt at a budget cap only as the last resort; integrate out of band (annotate methods; a governor applies only the actions you allow, non-destructively); run in **preview mode** in production to tune thresholds before enforcing; keep the control plane in your own tenant; and mine the ledger for failure modes your policies still miss | `ReferencesElement → el-run-level-token-governance`, `el-tokenops`, `el-steer-not-halt`, `el-cost-control-surface-by-era` |

## Dropped

- **The three-scenario demo mechanics** (preview → halt → steer on a research + summarizer pair) — summarized inside `el-tokenops` and `el-steer-not-halt`.
- **The QR/wiki pointer** — no URL recoverable.

## Review notes

1. **⚑ Same-batch cluster: agent spend governance.** Three talks — this one (control plane), Anthropic/Malhotra (budgets over tokens for *writes*), Ironclad/Hong (token ROI metrics) — plus Navan naming cost "unsolved." Recommend a **held ledger "agent spend governance"** in the batch-22 registry section; no pattern proposed yet (mechanism-level, and `pat-durable-execution`/`pat-harness-over-model` absorb it).
2. **`sig-agentic-era-has-no-cost-control-plane` → `pat-durable-execution`** is a widening: cost governance as a runtime-layer product beneath the harness. Review may prefer `pat-harness-over-model` alone.
3. **`sig-out-of-band-annotation-governs-any-framework` → `pat-continual-learning-turn`** rests on a roadmap item (self-learning policy generation); hold if review wants shipped-only evidence.
4. **⚠ Verify before seeding:** the −78% / 67%→96% benchmark figures, the Uber four-month story and the "$500M in a month" number (also cited by Hong/Ironclad in this batch), and the product name TokenOps.
