# SPIKE extraction — "AI Evals for Cross-Functional Teams" (Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash) — FOR REVIEW

Source transcript: `transcripts/paranjape-haridas-doordash-cross-functional-evals.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/bMjlRrWjdT0 — AI Engineer World's Fair, published 2026-08-28.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: DoorDash's GenAI platform team (LLM gateway, agent gateway with central auth/identity, open-weights hosting, evals) on how evals "started as another engineering thing" and became a **cross-functional sport**: strategy & operations set the quality bar, PMs write rubrics, ops annotate, engineering supplies APIs/telemetry/datasets/judges. The platform went UI-first → API-first → **workflow-first**, letting operators vibe-code their own annotation UIs and calibrate LLM judges self-serve (GEPA), cutting annotation cost and cycle time. Caption garbles: "Farup"/"Faroo"/"Surup" → **Swaroop**, "Nachig" → **Nachiket**, "Door Dash Genai" → **DoorDash GenAI**, "SNO"/"statops" → **S&O (strategy & operations)**, "JPEA" → **GEPA**, "Ragago"/"Ragav" → a prior speaker, "v code" → **vibe-code**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-paranjape-haridas-doordash-evals` | AI Evals for Cross-Functional Teams (Nachiket Paranjape & Swaroop Chitlur Haridas, DoorDash — AI Engineer World's Fair) | youtube | https://youtu.be/bMjlRrWjdT0 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-nachiket-paranjape`, `exp-swaroop-chitlur-haridas`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-nachiket-paranjape` | Nachiket Paranjape (GenAI Platform, DoorDash) | `AffiliatedWithCompany → co-doordash` **[registry]** |
| `exp-swaroop-chitlur-haridas` | Swaroop Chitlur Haridas (GenAI Platform, DoorDash) | `AffiliatedWithCompany → co-doordash` **[registry]** |

## Companies (0 new)

Reused **[registry]**, edge-only: `co-doordash` — new facts: a horizontal GenAI platform team with four pillars — an LLM gateway (switch models freely), an agent gateway (tools, other agents, central authentication and agent identity "our security team can bless"), open-weights model hosting ("cost is the number one concern… significant impact already"), and an eval platform; thousands of annotation rows per week; guidance from co-founder Andy Fang to be UI-first for non-engineers.

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-evals-as-cross-functional-sport` | Evals as a cross-functional sport | concept | | Evals are "not just an engineering harness" — a team sport that injects domain knowledge into AI quality. Strategy & operations set priorities and the quality bar; product translates requirements into rubrics and workflows; operations run annotation; engineering provides APIs, telemetry, datasets and judges. Teams differ in who owns the judge prompt (S&O, PM, or engineering) and the platform lets that org design evolve |
| `el-eight-step-quality-loop` | The continuous quality loop | ops | harness | Trace → view sessions/traces → sample down to a reviewable set → annotate with domain expertise → review → build **golden datasets** → calibrate judges (and agents and workflows) against them → monitor over time → repeat. Two surfaces: a telemetry plane (traces, scores, observations; reachable by MCP, SDK, APIs) and a workflow plane where S&O and product set annotation tasks, review golden sets, create and calibrate judges |
| `el-ui-first-api-first-workflow-first` | UI-first → API-first → workflow-first | concept | harness | The platform's evolution: UIs so non-engineers can contribute; then stable table APIs (scores, datasets) so engineers build without being blocked on the central team; then, with coding agents, **workflow-first** — S&O and PMs navigate the platform and run operations themselves. "As self-served as possible so people aren't blocked by our team" |
| `el-vibe-coded-annotation-uis` | Vibe-coded annotation UIs on stable APIs | concept | harness | Use cases vary (session-level quality judgments, image annotation, manual testing, trajectory evals for multi-agent systems) and a platform team can't build a UI per case — but the underlying patterns are the same, so with stable APIs the operators use Codex or Claude Code to vibe-code their own annotation UIs. Result: reduced per-annotation spend at DoorDash scale, faster loops, higher velocity |
| `el-self-serve-judge-calibration` | Self-serve LLM-judge calibration | technology | harness | Start from a judge prompt and what to measure → baseline scores on traces → an optimization loop (the GEPA prompt-optimization library) against the golden dataset → promote the calibrated prompt as the LLM-as-judge. Packaged as a self-serve UI: a PM or operator sets a few configs and runs the loop with any model (Gemini, Claude, OpenAI); the original and calibrated prompts are shown side by side so partners can see why the judge improved and trust it |

Element edges: all five `IdentifiedInArtifact → ia-aie-paranjape-haridas-doordash-evals`.
`el-eight-step-quality-loop` `UsesElement → el-golden-dataset` **[registry]**, `el-agent-execution-traces` **[registry]**, `el-trajectory-evals` **[registry]**;
`el-self-serve-judge-calibration` `UsesElement → el-gepa` **[registry]**, `el-judge-as-classifier` **[registry]**, `el-rater-rubrics` **[registry]**, `el-judge-human-calibration` **[registry]**;
`el-vibe-coded-annotation-uis` `UsesElement → el-ui-first-api-first-workflow-first`;
`el-evals-as-cross-functional-sport` `UsesElement → el-eight-step-quality-loop`;
`el-eight-step-quality-loop` `ExemplifiesPattern → pat-verification-gap` **[registry]**;
`el-evals-as-cross-functional-sport` `ExemplifiesPattern → pat-ai-native-org` **[registry]**;
`el-self-serve-judge-calibration` `EnablesPattern → pat-verification-gap` **[registry]**.

Reused elements (no new nodes): `el-golden-dataset` **[registry]**, `el-agent-execution-traces` **[registry]**, `el-trajectory-evals` **[registry, b22]**, `el-gepa` **[registry]**, `el-judge-as-classifier` **[registry]**, `el-rater-rubrics` **[registry]**, `el-judge-human-calibration` **[registry]**, `el-model-routing` **[registry]** (the LLM gateway), `el-agent-identity-broker` **[registry]** (the agent gateway's central auth/identity).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-paranjape-haridas-doordash-evals`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-doordash` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-evals-became-a-cross-functional-effort` | | DoorDash's platform team found that catering to consumer discovery, personalization ML and multi-agent trajectory evals under one platform meant empowering the domain experts — strategy & operations, PMs, even labeling partners — not only engineers. Evals moved from an engineering harness to an org-wide loop with owners in every function and a per-team choice of who owns the judge prompt | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-evals-as-cross-functional-sport`, `el-eight-step-quality-loop` |
| `sig-api-first-lets-operators-vibe-code-their-tools` | harness | Because the platform is API-first on stable table APIs, operators vibe-code their own annotation UIs with Codex or Claude Code instead of waiting for the platform team — image annotation, session judgments, manual-testing flows — with "significant reduction in per-annotation spend" at thousands of rows per week and faster iteration. The platform's product became its APIs plus the operators' coding agents | `FormsPattern → pat-ai-native-org` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-vibe-coded-annotation-uis`, `el-ui-first-api-first-workflow-first` |
| `sig-self-serve-judge-calibration-with-gepa` | harness | LLM-as-judge calibration — baseline, GEPA optimization against a golden set, promote — packaged so a PM or operator runs it with any model and sees the before/after prompt diff. The judge, the corpus's recurring "constrained external verifier," is now something non-engineers tune and audit themselves | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-self-serve-judge-calibration`, `el-gepa` **[registry]**, `el-golden-dataset` **[registry]** |
| `sig-open-weights-hosting-for-cost-at-doordash` | inference | The platform's value proposition is balancing accuracy, latency and cost — for models and now for agents — and "cost is the number one concern these days," so DoorDash paired its LLM gateway with open-weights model hosting and has "seen significant impact already." A large consumer company moving inference in-house on cost grounds | `FormsPattern → pat-sovereign-ai` **[registry]**; `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-model-routing` **[registry]** |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-quality-is-an-org-loop-not-a-harness` | The durable claim: AI quality at scale is produced by an organizational loop — trace, sample, annotate with domain expertise, build golden sets, calibrate judges, monitor — in which every function owns a step, and the platform's job is to make each step self-serve (stable APIs, vibe-coded UIs, judge calibration anyone can run). Verification is relocated not only outside the model but outside engineering | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-evals-as-cross-functional-sport`, `el-eight-step-quality-loop`, `el-self-serve-judge-calibration` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-paranjape-haridas-doordash-evals`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-run-cross-functional-evals` | Trace, sample, annotate, calibrate — with every function owning a step | Treat evals as a team sport: S&O set the quality bar, product writes rubrics, ops annotate, engineering provides APIs, telemetry, datasets and judges; run the loop continuously — capture traces and sessions, sample to a reviewable set, annotate with domain expertise, review, build **golden datasets**, calibrate judges against them, monitor, repeat; build the platform **API-first** on stable table APIs so engineers aren't blocked, then **workflow-first** so operators run it themselves; let operators vibe-code their own annotation UIs with coding agents instead of building one per use case; make judge calibration self-serve (baseline → GEPA optimization → promote) with any model and show the prompt diff so partners trust the result; and let each team choose who owns the judge prompt | `ReferencesElement → el-eight-step-quality-loop`, `el-evals-as-cross-functional-sport`, `el-vibe-coded-annotation-uis`, `el-self-serve-judge-calibration`, `el-ui-first-api-first-workflow-first` |

## Dropped

- **The France-match joke** and the prior-speaker references — color.
- **Detailed results** beyond "significant reduction in per-annotation spend" — not quantified.

## Review notes

1. **Pairs with Hong/Ironclad (b22) and Bhatawdekar/Braintrust (this batch)** on evals as the organizing loop; DoorDash contributes the *who owns which step* map and the vibe-coded-tooling twist.
2. **`sig-open-weights-hosting-for-cost-at-doordash` → `pat-sovereign-ai`** is a cost-motivated reading (in-house open models), not a sovereignty one — flag as widening.
3. **⚠ Verify before seeding:** the GEPA identification (captions "JPEA"), Andy Fang's guidance, "thousands of rows per week."
