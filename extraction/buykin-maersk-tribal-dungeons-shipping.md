# SPIKE extraction — "Tribal Dungeons of Global Shipping: AI Agents at Global Scale" (Dmitry Buykin, Maersk) — FOR REVIEW

Source transcript: `transcripts/buykin-maersk-tribal-dungeons-shipping.txt` (auto-captions — quotes are paraphrases, not verbatim; a short 12-minute practitioner report with heavy accent garbles).
Video: https://youtu.be/dQ-_i1tZiws — AI Engineer World's Fair, published 2026-08-29.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-29 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a production report from global shipping operations — 200+ concurrent agent instances executing exception work across legacy back-ends. The hard part is not the agent loop but turning **tribal knowledge** (SOPs as screenshots) into something an agent can execute safely, and building the **refining loop around the agent**: an SOP corpus as process memory, an execution runtime, and expert feedback capture, with 100,000+ corrections in nine months folded back into composite tools. Caption garbles: "EI builder" → **AI builder**, "archist expert" → **expert**, "theme bench"/"theme feedback" → ⚠ likely **"trace bench"** / an internal triage bench (see note 3), "SAP is okay" → a slide-switch aside, "disabled rights" → **disabled writes**, "pipe coding" → **vibe coding**, "mere view" → **review**, "right gate" → **write gate**, "MCPS" → **MCPs**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-buykin-tribal-dungeons-shipping` | Tribal Dungeons of Global Shipping: AI Agents at Global Scale (Dmitry Buykin, Maersk — AI Engineer World's Fair) | youtube | https://youtu.be/dQ-_i1tZiws |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-dmitry-buykin`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-dmitry-buykin` | Dmitry Buykin (Maersk) | `AffiliatedWithCompany → co-maersk` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-maersk` | Maersk | developer | Global shipping/logistics operator (coerced enterprise → developer). Runs 200+ concurrent agent instances in production on exception work across legacy back-ends; SOPs vary per country; 100,000+ expert corrections captured over nine months |

## Elements (7 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-tribal-dungeons` | Tribal dungeons | concept | harness | The knowledge exists but not in a form an agent can execute. Legacy SOPs are "a bunch of screenshots organized in sequence" — they explain what a person sees and clicks, not the process. The organization cannot represent its own standard procedures; an expert and a model read them differently, and "that gap is the hard part" |
| `el-agent-sop` | Agent SOP | ops | harness | What an executable procedure needs that a legacy SOP lacks: preconditions, decisions, identifiers, back-end calls, validation, recovery, and evidence of successful execution. "Experts own the what, agents own the how; an exception becomes a guardrail." Most of the effort is translation and negotiation between expert and engineer to align on common sense |
| `el-sop-corpus-as-process-memory` | SOP corpus as process memory | concept | context | The SOP memory is organized as a corpus — the company's process memory, modified and aligned per country (the same procedure means different things in different countries) — and is far larger than the runtime: roughly 20:1. It is the asset; the runtime is small |
| `el-refining-loop-around-the-agent` | The refining loop around the agent | concept | harness | "The agent loop is not the system. The refining loop around the agent is the system, and it's the most complex part." Three parts: SOP memory, execution runtime, and feedback capture from experts. Quality "comes from replaying real examples with writes disabled, not from vibes or a bigger model." Accuracy "wasn't designed in one diagram up front — it was earned one small correction at a time" |
| `el-correction-as-executable-change` | Correction as executable change | ops | harness | "A correction only counts when it becomes an executable change — that's the line between an opinion and a production fix." The trace is the shared evidence that lets an expert and an engineer review the same case and agree on what happened. 100,000+ corrections over nine months. Expert time is the bottleneck, so triage is automated |
| `el-failure-heatmap-triage` | Failure heat-map triage | ops | harness | A triage bench clusters failures and hands back something actionable; heat maps turn thousands of traces into priorities so experts and engineers look at the same problems. Every cell is a group of tracked scenarios; turning one cell green-to-red-to-green is "one to two months of the whole team's effort." "The agent failed" is where investigation starts, not ends — each failure maps to a specific fix: wrong workflow → classifier eval; wrong write → write gate; wrong assumption → review |
| `el-composite-tools-from-proven-scenarios` | Composite tools from proven scenarios | technology | harness | Repeatable successful step-sequences are aggregated and merged into bigger reusable tools — proven scenarios become snippets other agents can call — and rolled out to hundreds of countries in one go. "An AI-native operation is a system that learns from what works and folds it back into code as new composite tools." Tools are tuned via function calling with distilled responses; MCP deliberately not used ("bloated") |

Element edges: all seven `IdentifiedInArtifact → ia-aie-buykin-tribal-dungeons-shipping`.
`el-agent-sop` `UsesElement → el-tribal-dungeons`;
`el-refining-loop-around-the-agent` `UsesElement → el-sop-corpus-as-process-memory`, `el-correction-as-executable-change`, `el-failure-heatmap-triage`, `el-agent-execution-traces` **[registry]**;
`el-composite-tools-from-proven-scenarios` `UsesElement → el-correction-as-executable-change`;
`el-refining-loop-around-the-agent` `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-correction-as-executable-change` `EnablesPattern → pat-continual-learning-turn` **[registry]**;
`el-sop-corpus-as-process-memory` `ExemplifiesPattern → pat-agent-memory-layer` **[registry]**.

Reused elements (no new nodes): `el-agent-execution-traces` **[registry]** (the trace as shared evidence), `el-mcp` **[seed]** (explicitly rejected in favor of tuned function calling), `el-spec-driven-development` **[registry]** (named as the stage where accuracy stops improving at this scale).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-buykin-tribal-dungeons-shipping`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-maersk`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-long-tail-exceptions-are-the-expensive-part` | harness | On paper a shipment is one workflow; in reality it is "an orchestration of many parallel state machines," and the moment one drifts you get exception work. The easy majority is already automated across the industry; what is left is the long tail, with "more exceptions than systems built to handle them" — that tail is the expensive part, and it depends on many legacy systems being coherent at once. Production latencies of minutes up to ten minutes are bounded by the legacy systems, not the agent loop | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-tribal-dungeons` |
| `sig-the-refining-loop-is-the-system` | harness | The central claim: the agent loop is not the system — the refining loop around it is, and it is the most complex part (SOP memory + execution runtime + expert feedback capture). Quality comes from replaying real examples with writes disabled and checking whether behavior improved — "not from vibes, not from a bigger model." Vibe coding and spec-driven development both stall before this stage; "the real work starts" past them | `FormsPattern → pat-harness-over-model` **[registry]**; `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-refining-loop-around-the-agent`, `el-spec-driven-development` **[registry]** |
| `sig-100k-corrections-folded-into-composite-tools` | harness | 100,000+ expert corrections over nine months, each counting only once it became an executable change, with successful step-sequences merged into composite tools and rolled out to hundreds of countries at once. "AI-native operation is a system that learns from what works and folds it back into code." An organization-level learning loop that compounds outside the weights — the corpus's clearest operations-scale instance of the accumulation loop, with the SOP corpus as its process memory (20:1 to runtime) | `FormsPattern → pat-continual-learning-turn` **[registry]**; `FormsPattern → pat-agent-memory-layer` **[registry]**; `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-correction-as-executable-change`, `el-composite-tools-from-proven-scenarios`, `el-sop-corpus-as-process-memory` |
| `sig-harness-makes-dumb-mistakes-impossible` | harness | "Discovery needs agent freedom; production needs a cage. The harness isn't there to give the agent more room — it's there to make the dumb mistakes impossible. At this scale 'please be careful' is not a guard." Each failure class gets a structural fix (classifier eval / write gate / review); preventive measures eliminate the unsafe path on critical paths while review and approval stay in the loop. The engineering focus is safe hand-offs and a trail you can trust | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-failure-heatmap-triage`, `el-agent-sop` |
| `sig-maersk-rejects-mcp-for-tuned-function-calling` | harness | A deliberate production stance against the emerging consensus: "we're not using MCPs — for us it's never the best choice. Systems are bloated; we distill responses and tune the tools through function calling so we can control quality." The same batch's Navan talk calls MCP "the de facto protocol" — a live disagreement between two enterprise practitioners | | `OnElement → el-mcp` **[seed]**, `el-composite-tools-from-proven-scenarios` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-experts-own-the-what-agents-own-the-how` | The durable organizational claim is the division of labor: the expert owns the *what* (the procedure, its exceptions, its evidence), the agent owns the *how*, and the engineering is the translation layer between them — making work representable, execution bounded, behavior observable, correction cheap, improvement compounding. The "AI-native operation" here is not agents in a workflow but a methodology whose main asset is the corrected, country-aligned process memory | `HighlightsPattern → pat-ai-native-org` **[registry]** | `ReliesOnElement → el-agent-sop`, `el-tribal-dungeons`, `el-sop-corpus-as-process-memory` |
| `ins-corrections-are-the-compounding-asset` | Accuracy was "earned one small correction at a time, at scale" — and only corrections that became executable changes count. That makes the corrections ledger (and the composite tools distilled from it) the appreciating asset, not the model: a shipping company arriving independently at the corpus's continual-learning thesis from the operations side, with the loop living in code and process memory rather than in weights | `HighlightsPattern → pat-continual-learning-turn` **[registry]** | `ReliesOnElement → el-correction-as-executable-change`, `el-composite-tools-from-proven-scenarios`, `el-refining-loop-around-the-agent` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-buykin-tribal-dungeons-shipping`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-turn-tribal-knowledge-into-executable-sops` | The five moves for agents on legacy operations | **Make work representable** — rewrite screenshot-SOPs as agent SOPs with preconditions, decisions, identifiers, back-end calls, validation, recovery and evidence, negotiated between expert and engineer; **make execution bounded** — a cage in production: classifier evals for wrong workflows, write gates for wrong writes, review for wrong assumptions, preventive measures that eliminate the unsafe path ("please be careful" is not a guard); **make behavior observable** — the trace is the shared evidence expert and engineer both review; **make correction cheap** — a correction counts only when it is an executable change; triage failures automatically into heat maps because expert time is the bottleneck; **make improvement compound** — replay real examples with writes disabled to check behavior improved, merge proven step-sequences into composite tools, roll them out across countries in one go; and control tool quality by distilling responses and tuning function calls rather than adopting bloated MCP surfaces | `ReferencesElement → el-agent-sop`, `el-refining-loop-around-the-agent`, `el-correction-as-executable-change`, `el-failure-heatmap-triage`, `el-composite-tools-from-proven-scenarios` |

## Dropped

- **"Yet another loop agent intro" skipped by the speaker** — nothing to extract.
- **The UK-vs-other-country SOP slide** — folded into `el-sop-corpus-as-process-memory` (the per-country variation is the point).
- **The Q&A** — none taken.

## Review notes

1. **⚑ Operations-scale evidence for three coined patterns at once.** `sig-100k-corrections-folded-into-composite-tools` is the corpus's first *non-software* accumulation loop (`pat-continual-learning-turn`) with a quantified corrections ledger, a process-memory corpus (`pat-agent-memory-layer`) and a methodology claim (`pat-ai-native-org`). Triple edge is deliberate; review may trim.
2. **`sig-maersk-rejects-mcp-for-tuned-function-calling` is held pattern-less** — a protocol-adoption counter-signal, not a thesis contradiction. It is the batch's cleanest practitioner disagreement (Maersk rejects MCP; Navan calls it de facto). Candidate texture if an "integration-surface" thread ever forms.
3. **⚠ Verify before seeding:** "theme bench" (likely an internal trace/triage bench — name uncertain), the 20:1 corpus-to-runtime ratio, "over 200 instances," "over 100,000 corrections over 9 months," and "one to two months per heat-map cell." All are speaker figures from a heavily garbled caption track.
4. **Cross-file:** `el-correction-as-executable-change` rhymes with b15's `el-trace-to-simulation` (Snorkel) and b17's `el-continuous-fix-loop`; `el-failure-heatmap-triage` with `el-agent-trace-mining`. Left to review.
