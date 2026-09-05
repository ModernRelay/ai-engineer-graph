# SPIKE extraction — "Your Agent Evolved. Your Evals Didn't." (Ameya Bhatawdekar, Braintrust) — FOR REVIEW

Source transcript: `transcripts/bhatawdekar-braintrust-agent-evolved-evals-didnt.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/nxokqOq1imY — AI Engineer World's Fair, published 2026-08-20.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-20 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: Braintrust's field CTO walks the generations of AI application architecture — single prompt → chain/RAG → ReAct loop (fell short on weak tool calling) → **workflow graphs** (teams took control back; brittle out of distribution) → ReAct again once mid/late-2025 models made tool calling and planning reliable (high trajectory variance → pass@k vs pass^k) → product systems with memory, sandboxes, MCP and skills — and argues that **architecture follows model updates and evals must follow architecture**, because evals are "the durable asset that describes how your system is supposed to work." Most teams' evals are static; the fix is a production flywheel, including clustering production data to surface unanticipated failure modes (Braintrust Topics). Caption garbles: "Amaya Bhavadkar" → **Ameya Bhatawdekar**, "S sur agent"/"SR agent" → **SRE agent**, "pass wedge K" → **pass^k**, "replplatforming" → **re-platforming**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-bhatawdekar-braintrust-agent-evolved-evals` | Your Agent Evolved. Your Evals Didn't. (Ameya Bhatawdekar, Braintrust — AI Engineer World's Fair) | youtube | https://youtu.be/nxokqOq1imY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-ameya-bhatawdekar`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-ameya-bhatawdekar` | Ameya Bhatawdekar (Field CTO, Braintrust) | `AffiliatedWithCompany → co-braintrust` **[registry]** |

## Companies (0 new)

Reused **[registry]**, edge-only: `co-braintrust` — new facts: an eval + observability platform providing the full flywheel (evals, observability, production insights) and **Topics**, a cluster analysis over production data that surfaces new categories of failure teams hadn't anticipated, feeding new eval cases. Reused `co-anthropic` **[seed]** and `co-openai` (the mid/late-2025 model capabilities that made the loop reliable again).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-architecture-generations-and-their-evals` | Architecture generations and the evals each needs | concept | harness | Grounded in an SRE agent with read and write tools (roll back, page). **Single prompt** (~3 years ago): eval the final answer — accuracy, factuality, hallucination, stale knowledge — against a golden dataset. **Chain/RAG**: parser, retrieval, context, synthesis — several failure points, still a fixed path. **ReAct loop** (late 2023–early 2024): flexible self-orchestration, but models mis-called tools, mis-orchestrated, collapsed on long context — "fell short of the promise." **Workflow graphs / state machines** (late 2024–early 2025): teams took orchestration control, models operated at the node level — reliable in distribution, brittle outside it, growing special-case branches; evals now per node, branch consistency, node contracts, retry loops. **ReAct again** (mid/late 2025): reliable tool calling, planning, long horizons, self-correction — high trajectory variance, so the unit of eval becomes a distribution (pass@k, pass^k). **Product systems** (now): the loop plus memory (in- and cross-session), code sandboxes, MCP/skill directories — new surfaces the old evals only partially cover |
| `el-evals-follow-architecture` | Architecture follows models; evals follow architecture | concept | harness | Every step-function model release (tool use, long context, sandboxed code, memory) unlocks capability the previous system — built around the old limitations — cannot tap without re-architecture, so teams are **re-platforming, not iterating**. Each re-architecture opens new surface area for failure, so evals must be made congruent with the new architecture; kept static they give partial coverage and miss the ways the new system is fragile. "Evals are the durable asset that describes how your system is supposed to work" across generational shifts |
| `el-pass-at-k-and-pass-hat-k` | pass@k vs pass^k | concept | harness | With reliable loops, the same input yields dramatically different trajectories that still reach the right answer, so one run is no longer a signal. Run each eval k times: **pass@k** — succeeds at least once — measures capability; **pass^k** — succeeds every time — measures reliability. A system with high pass@k and low pass^k is capable but unreliable, and the gap tells you what to work on |
| `el-eval-flywheel-in-practice` | The eval flywheel, and why teams skip it | concept | harness | Everyone accepts the diagram — harvest production data to keep evals reflective of the real world — and the best teams run it religiously; in practice many teams' evals are static, so even without architectural change they stagnate. Through a generational shift you need both: production harvesting for the failures you defined ("what good looks like") and something to **shine a light on new failure types** you didn't anticipate |
| `el-production-topic-clustering` | Production topic clustering for unknown failures | technology | harness | Braintrust Topics: cluster analysis over all production data to surface new categories of failure — situations with no guardrail and no eval — so teams expand their eval sets to cover them as they make systemic architectural changes. Turns the flywheel from "more examples of known failures" into "discovery of unknown ones" |

Element edges: all five `IdentifiedInArtifact → ia-aie-bhatawdekar-braintrust-agent-evolved-evals`.
`el-production-topic-clustering` `DevelopedByCompany → co-braintrust` **[registry]**;
`el-evals-follow-architecture` `UsesElement → el-architecture-generations-and-their-evals`, `el-eval-driven-development` **[registry]**, `el-golden-dataset` **[registry]**;
`el-pass-at-k-and-pass-hat-k` `UsesElement → el-pass-at-k` **[registry]**;
`el-eval-flywheel-in-practice` `UsesElement → el-online-evals` **[registry]**, `el-production-topic-clustering`;
`el-architecture-generations-and-their-evals` `UsesElement → el-langgraph` **[registry]**, `el-agent-loops` **[registry]**, `el-agent-skills` **[registry]**;
`el-evals-follow-architecture` `ExemplifiesPattern → pat-verification-gap` **[registry]**;
`el-eval-flywheel-in-practice` `ExemplifiesPattern → pat-benchmark-trust-crisis` **[registry]**;
`el-production-topic-clustering` `EnablesPattern → pat-continual-learning-turn` **[registry]**.

Reused elements (no new nodes): `el-pass-at-k` **[registry]**, `el-eval-driven-development` **[registry]**, `el-golden-dataset` **[registry]**, `el-online-evals` **[registry]**, `el-langgraph` **[registry]** (the graph-framework era), `el-agent-loops` **[registry]**, `el-agent-skills` **[registry]**, `el-agent-approach-succession` **[registry, b22]** (Box's ladder is the same history from a buyer's chair).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-bhatawdekar-braintrust-agent-evolved-evals`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-braintrust` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-architecture-follows-models-evals-follow-architecture` | harness | Every step-function model release forces re-architecture (systems built around old limitations can't tap new capability), and every re-architecture opens new failure surface — so evals kept from the previous generation cover the new system only partially. "We are moving from iterating on our applications to re-platforming them," and the eval suite is the durable description of intended behavior that must move with each platform | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-benchmark-trust-crisis` **[registry]** | `OnElement → el-evals-follow-architecture`, `el-architecture-generations-and-their-evals` |
| `sig-workflow-graphs-were-a-workaround-for-weak-models` | harness | The graph/state-machine era (late 2024–early 2025) existed because the ReAct loop's models couldn't be controlled — "you take the control and bake it into the system"; when mid/late-2025 models made tool calling, planning and self-correction reliable, those graph systems could not use the new capability and teams rebuilt the loop. An eval vendor dating the harness's heavy orchestration to a model deficit that has since closed | `ContradictsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-architecture-generations-and-their-evals`, `el-langgraph` **[registry]**, `el-agent-approach-succession` **[registry]** |
| `sig-agent-variance-needs-pass-at-k-and-pass-hat-k` | harness | Reliable loops produce dramatically different trajectories for the same input, so a single eval run is noise: run k times and read pass@k (capability) against pass^k (reliability). The unit of evaluation becomes a distribution, and the capability/reliability gap becomes the work list | `FormsPattern → pat-benchmark-trust-crisis` **[registry]**; `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-pass-at-k-and-pass-hat-k`, `el-pass-at-k` **[registry]** |
| `sig-most-teams-run-static-evals` | harness | "There is general acceptance that you need to run that flywheel; in practice a lot of teams don't" — evals are static, and even without architectural change they stop measuring what matters. Through generational shifts the stagnation compounds: known-failure harvesting continues, novel failure modes go unseen | `FormsPattern → pat-benchmark-trust-crisis` **[registry]** | `OnElement → el-eval-flywheel-in-practice` |
| `sig-cluster-production-to-find-unknown-failures` | harness | The vendor's answer to unknown unknowns: cluster all production traffic to surface new categories of failure with no guardrail and no eval, and turn them into eval cases — so the flywheel discovers failure types rather than only collecting examples of known ones. Continuous learning applied to the eval suite itself | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-continual-learning-turn` **[registry]** | `OnElement → el-production-topic-clustering`, `el-eval-flywheel-in-practice` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-evals-are-the-durable-asset-across-replatforms` | The durable claim inverts the usual hierarchy: models and architectures are transient (each release forces a re-platform), so the one artifact that persists is the eval suite — the executable description of how the system is supposed to behave — and it must be re-fitted to each architecture or it silently measures the wrong system. Verification is the continuity layer through generational change | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-evals-follow-architecture`, `el-architecture-generations-and-their-evals`, `el-eval-flywheel-in-practice` |
| `ins-orchestration-graphs-were-borrowed-control` | Read as history, the graph era was control borrowed from the harness while models were weak and returned to the model when they weren't — the same ladder Box's CTO described (b22) — which means "harness over model" is a moving boundary whose position must be re-measured with each model generation, exactly as the evals must. The counter-edge is recorded on purpose: the corpus's harness thesis should carry its own date stamp | `HighlightsPattern → pat-benchmark-trust-crisis` **[registry]** | `ReliesOnElement → el-architecture-generations-and-their-evals`, `el-pass-at-k-and-pass-hat-k` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-bhatawdekar-braintrust-agent-evolved-evals`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-keep-evals-congruent-with-your-architecture` | Re-fit evals at every re-platform; measure distributions; hunt unknown failures | Expect step-function model releases to force re-architecture, not iteration, and treat the eval suite as the durable asset that must be re-fitted each time — map the new failure surfaces (tool calls, orchestration, memory, sandboxes, skills) and add evals for them; for loop-based agents run each eval **k times** and track pass@k (capability) and pass^k (reliability) rather than single runs; actually run the production flywheel — harvest traces into eval cases for the failures you defined; and add a mechanism (production clustering) that surfaces failure categories you didn't anticipate, especially after systemic changes; keep both incremental and step-function improvement measurable so new capability is unlocked without regressing what worked | `ReferencesElement → el-evals-follow-architecture`, `el-pass-at-k-and-pass-hat-k`, `el-eval-flywheel-in-practice`, `el-production-topic-clustering`, `el-architecture-generations-and-their-evals` |

## Dropped

- **The SRE-agent worked example's per-generation eval lists** — summarized inside the first element.
- **Product tour** beyond Topics — the platform is described only as providing the flywheel.

## Review notes

1. **⚑ `ContradictsPattern → pat-harness-over-model`** from an eval vendor's architectural history, one batch after Box (b22) and beside Rogge (this batch): three sources dating heavy orchestration to a model deficit that closed in mid-2025. The pattern remains well supported (claim-1: control outside the model) but its *weight* is now explicitly time-dependent — recommend adding that qualifier to the brief.
2. **`pat-benchmark-trust-crisis` widening:** static private evals and single-run scoring as trust failures inside the org, not only in public benchmarks.
3. **⚠ Verify before seeding:** the generation dates (late 2023 ReAct, late 2024 graphs, mid/late 2025 reliable loops) are the speaker's periodization; "Topics" as the feature name.
