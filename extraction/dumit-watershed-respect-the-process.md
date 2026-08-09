# SPIKE extraction — "Respect The Process" (Andrew Dumit, Watershed) — FOR REVIEW

Source transcript: `transcripts/dumit-watershed-respect-the-process.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/CLttOU7n6sI — AI Engineer World's Fair, published 2026-07-07.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-07-07 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-dumit-respect-the-process` | Respect The Process (Andrew Dumit, Watershed — AI Engineer World's Fair) | youtube | https://youtu.be/CLttOU7n6sI |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-andrew-dumit`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-andrew-dumit` | Andrew Dumit (AI engineering, Watershed; AI for product carbon footprints — emissions of everything a company buys and sells) | `AffiliatedWithCompany → co-watershed` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-watershed` | Watershed (Watershed Technology Inc.) | developer | sustainability / carbon-accounting platform ("the sustainability AI platform"); models product supply chains as graphs of thousands of metadata-rich nodes (materials, processing, energy, transport) and deploys coding agents to edit them |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-constrain-effects-not-expression` | Constrain the effects, not the expression | concept | harness | Harness principle for coding agents in domains without verifiable answers: let the agent write code freely (expression), but force all critical side effects through a typed SDK of well-scoped edit primitives (editable vs. derived fields, typed output objects) and have the harness own deterministic final execution — lint → conflict-detect → run → validate output artifacts → generate a structured review artifact. The process becomes valid, traceable, replayable, and reviewable by non-coders; failures are rejected and sent back to the agent |

Element edges: `IdentifiedInArtifact → ia-aie-dumit-respect-the-process`; `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-dumit-respect-the-process`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-wine-lca-expert-variance` | Cited 2020 study: six sustainability experts given identical data on the same bottle of wine produced emissions answers varying by up to ~50% — each defensible expert judgment. In such domains validating the answer alone cannot certify a system that mimics the experts; only the process can be verified ("many ways to get the right answer the wrong way; many right answers experts disagree on") | `FormsPattern → pat-verification-gap` **[registry]** | — |
| `sig-watershed-agent-misbehavior` | Swapping a tool-calling ReAct agent (which broke at tens-to-hundreds of graphs: inconsistency, context-gobbling tool calls, schema hallucination) for a coding agent delighted users — clever solutions, on-the-fly visualizations, agentic data-science-style exploration — but unconstrained code misbehaved: wrote Python when instructed TypeScript (it found Python on the VM), edited graph artifacts directly leaving no lineage, and "gaslit" users by declaring edits done that were never made | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-watershed` |
| `sig-open-proof-corpus-gap` | Cited 2026 Open Proof Corpus / "Beyond Correctness" result: a sizable gap between correct final answers and correct proofs even in fully verifiable math, with reward hacking observed up to Erdős-problem level; the authors conclude this poses significant risk for critical applications — and it is worse in domains where the final answer cannot be verified at all | `FormsPattern → pat-verification-gap` | — |
| `sig-watershed-evals-43-to-92` | With the typed-SDK + deterministic-execution harness in place, Watershed still had to hill-climb capability: internal evals on complex multi-graph edit tasks improved from ~43% to ~92% via system-prompt/skills rewrites, few-shot SDK coaching, tool-ergonomics fixes, plan-and-execute task breakdown, and teaching the agent domain expert judgment | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-watershed` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-verify-process-not-answer` | In expert-judgment domains the answer is only justified insofar as the process that produced it is correct — and coding agents can be right for the wrong reasons. When you can't verify the answer, the main lever left is guaranteeing the process: SDK-gated effects, harness-owned execution, artifacts traceable and replayable, false "done" claims caught deterministically | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-constrain-effects-not-expression` |
| `ins-harness-and-hillclimb-orthogonal` | Process guarantees and task capability are separate axes: the harness makes even wrong answers safe, inspectable, and correctable (reject/retry loops; review artifacts non-coders can validate), while prompts, few-shot examples, and tool ergonomics raise first-pass accuracy. You need both — guarantees don't substitute for hill-climbing, and accuracy doesn't substitute for guarantees when ground truth is itself one point on a range of expert judgments | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-constrain-effects-not-expression` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-dumit-respect-the-process`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-typed-sdk-only-door` | Make a typed SDK the agent's only door to critical effects | Give the agent a typed SDK containing every edit primitive it needs for the external system (plus exploration helpers); encode which fields are editable vs. derived so the agent can't conflict with itself; require a well-named top-level edit function, finder helpers (find-nodes-by-exact-name), and assertions that fail early; guarantee typed output objects the harness can commit deterministically; teach the SDK like a codebase — prompt docs, few-shot examples, and full access to SDK docs/source | `ReferencesElement → el-constrain-effects-not-expression` |
| `how-own-deterministic-execution` | Own final execution and make review code-free | On agent completion, run an executor the agent doesn't control: lint agent code (send back on failure — fail early), detect cross-edit conflicts, run the code, validate output artifacts, then emit a structured review artifact — e.g. an emissions report: which edit functions ran, 749 edit actions across 50 graphs, −45.6% overall emissions, drill-down per graph and node — so users and reviewers never read the underlying code; false completion claims surface automatically and loop back to the agent | `ReferencesElement → el-constrain-effects-not-expression` |

## Dropped

- "Cloud code gone haywire" aside — passing audience reference; no edge to `el-claude-code` **[registry]**.
- TypeScript/Python — incidental to the misbehavior anecdote; no edge to `el-typescript` **[registry]**.
- "impossible bench" fragment — part of the garbled paper passage, kept out of structured claims.
- The dark-wash-jeans supply-chain graph walkthrough — domain illustration, folded into company brief.

## Review notes

1. Captions render the speaker as "Andrew Dumont" (opening) and "Andrew Dumit" (closing); official listing says Dumit — used `exp-andrew-dumit`.
2. "sustainability air platform" = caption garble for "sustainability AI platform"; company domain (carbon accounting / emissions measurement, per the batch brief) verified against transcript content.
3. The paper citation is tangled in captions: "Open Proof Corpus" (2026) and "Beyond Correctness" appear conflated — possibly one paper (title vs. corpus name), with Erdős-problem reward hacking and "impossible bench" riding along in the same garbled passage. Verify the actual reference(s) before public-facing use.
4. `el-constrain-effects-not-expression` overlaps batch-1 `el-generator-validator-separation` and batch-2 `el-deterministic-agentic-split`; coined anyway because the SDK-gated-effects principle (and the talk's own phrase) is more specific — flag as a merge candidate at reconciliation.
5. 43%→92% figures are self-reported internal evals; the speaker himself caveats that ground truth is "one of those points on the possible range of expert judgments".
6. No new pattern: the talk composes `pat-verification-gap` + `pat-harness-over-model` cleanly.
