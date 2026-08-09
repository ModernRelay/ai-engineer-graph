# SPIKE extraction — "Teaching Coding Agents to do Spreadsheets" (Nuno Campos, Witan Labs) — FOR REVIEW

Source transcript: `transcripts/campos-witan-spreadsheet-agents.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/HEFSExa0xl0 — AI Engineer World's Fair, published 2026-07-08.
`stagingTimestamp` for the artifact and all signals: 2026-07-08 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-campos-spreadsheet-agents` | Teaching Coding Agents to do Spreadsheets (Nuno Campos, Witan Labs — AI Engineer World's Fair) | youtube | https://youtu.be/HEFSExa0xl0 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-nuno-campos`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-nuno-campos` | Nuno Campos (Witan Labs; spent 4 months teaching coding agents spreadsheets; ex-LangChain — see review note 1) | `AffiliatedWithCompany → co-witan-labs` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-witan-labs` | Witan Labs | developer | Building spreadsheet-native coding agents for financial analysis; took an internal benchmark from ~50% to 92% via harness work (REPL, formula/render engines) |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-code-mode` | Code mode | concept | harness | Replace many tool schemas with one code-execution tool: the agent writes code that composes tool functions in a single call instead of chaining sequential tool calls; industry-visible (shipped in the Anthropic API, promoted by Cloudflare) |
| `el-agent-repl` | Agent REPL (persistent code mode) | concept | harness | Code mode plus persistent state: variables survive across REPL tool calls, so the agent builds on prior work; observed effects vs plain code mode: shorter scripts, reasoning interleaved between steps, better answers faster; new capabilities ship as runtime methods plus a TypeScript type-definitions file in the prompt rather than new tool schemas |

Element edges: `el-agent-repl` `UsesElement → el-code-mode`; both `IdentifiedInArtifact → ia-aie-campos-spreadsheet-agents`; `el-agent-repl` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

## Signals (5 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-campos-spreadsheet-agents`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-witan-spreadsheet-92pct` | Witan Labs spent 4 months (2026) teaching coding agents spreadsheets: ~50% → 92% on an internal financial-analysis benchmark; the single biggest jump (50 → 74) came from replacing ~15 tools with one Node.js REPL, the rest from fuzzy search, formula-dependency tracing, system-prompt work, and bug fixes — not from waiting on better models | `FormsPattern → pat-model-not-bottleneck` | `RelevantCompany → co-witan-labs`; `OnElement → el-agent-repl` |
| `sig-code-mode-goes-mainstream` | Code mode is spreading as an agent interface (shipped in the Anthropic API, talked up by Cloudflare); Witan extended it to a REPL with persistent state and saw sequential-tool timeouts (5-minute budget, previously common on 10–15-call explorations) drop to zero | `FormsPattern → pat-harness-over-model` | `OnElement → el-code-mode`; `OnElement → el-agent-repl`; `RelevantCompany → co-anthropic` **[registry]** |
| `sig-verification-loop-compounds-with-models` | Across the 4–5 frontier model releases that shipped during the project, each more capable model extracted MORE from the same verification loop (formula engine + render engine); speaker's forecast: interfaces (REPL today) get superseded as model skills shift (e.g. computer use), the verification engines don't | `FormsPattern → pat-verification-gap` | — |
| `sig-llm-judge-attribution-problem` | Witan moved evals from LLM-as-judge to deterministic golden-spreadsheet comparisons (fixed inputs → expected outputs as a black-box test on the model-produced spreadsheet) wherever possible, because with a judge you cannot attribute a score change to the agent vs the evaluator | `FormsPattern → pat-verification-gap` | — |
| `sig-harness-bugs-masquerade-as-model-failures` | Practitioner observation: many apparent reasoning failures were plumbing — a wrong example in the prompt/skill that the model followed faithfully, or failing tools that caused retry loops reading as the model "being dumb"; trace reading, not model swaps, produced the fixes | `FormsPattern → pat-model-not-bottleneck` | — |

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-sequential-tools-are-a-bad-language` | An agent making many sequential (or even parallel) tool calls means you've invented a bad scripting language — give it a real one (code mode, REPL, whatever fits the domain) | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-agent-repl`, `ReliesOnElement → el-code-mode` |
| `ins-interfaces-transient-verification-durable` | The interface is rented, the verification loop is owned: a REPL wins today only because coding is what current models are best at (computer use may take over); the domain engines behind the feedback loop appreciate with every model release | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-agent-repl` |
| `ins-engine-fidelity-floor` | A verification loop is only as good as the engine powering it: an engine implementing ~50% of Excel's formulas is worse than none — the agent writes a correct formula, gets an engine error, and "fixes" what wasn't broken | `HighlightsPattern → pat-verification-gap` | — |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-campos-spreadsheet-agents`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-repl-tool-consolidation` | Consolidate agent tools into a persistent REPL | Pick a sandboxable scripting language models know cold (JS here; Python would work equally well); keep heavy domain logic in the right implementation language behind it (C# here); expose new capabilities as runtime methods documented by a TypeScript type-definitions file in the prompt — no tool-schema churn; keep state persistent across calls so the agent interleaves reasoning between steps; avoid rigid multi-agent phase splits — Witan's three-agent define/plan/execute/verify pipeline was a dead end because discovery ran once up front and context didn't flow between agents | `ReferencesElement → el-agent-repl`, `ReferencesElement → el-code-mode` |
| `how-domain-feedback-engines` | Build the feedback loop your domain lacks | Coding agents excel because compiler/linter/tests close the loop; for other domains build the equivalent — Witan built a formula engine (recalculation) and a rendering engine (range → image with layout/formatting) as the source of truth the agent must verify against; fidelity must be near-complete or results degrade below baseline; CSV/TSV range views and rendered-image views earn their keep as complementary methods inside the loop (they failed as standalone representations, as did SQL and XML) | — |
| `how-deterministic-eval-first` | Evaluate deterministically; treat LLM-as-judge as the fallback | Prefer golden-artifact black-box comparisons (same inputs → same outputs) for attribution; keep the judge only where determinism is impossible; read traces before blaming the model — prompt examples, tool failures, and infra bugs masquerade as reasoning failures; domain-knowledge prompt sections are portable across tool architectures and work by focusing attention ("pigeonholing"), not teaching the model new facts | — |

## Dropped

- SQL / XML / HTML spreadsheet representations — the dead-end catalog; kept as prose in `how-repl-tool-consolidation` / `how-domain-feedback-engines` (HTML credited as the step toward the render engine).
- Claude Code / Codex — passing analogy for coding's built-in feedback loops; no edges.
- Cloudflare — passing code-mode attribution, prose in `sig-code-mode-goes-mainstream`; not coined.

## Review notes

1. `exp-nuno-campos` ex-LangChain: supplied by task context (`co-langchain` **[registry]** exists); the transcript never mentions LangChain, so no `AffiliatedWithCompany → co-langchain` edge was added — add centrally if former affiliations belong on Expert nodes.
2. "Witan Labs" never appears in the captions (speaker introduces himself only as "Nuno"); company name comes from the official talk listing.
3. Benchmark numbers (50/74/92, zero timeouts, 5-minute budget) are speaker-claimed on an internal, unnamed benchmark.
4. No new pattern coined. `sig-llm-judge-attribution-problem` is weak added evidence for the `pat-benchmark-trust-crisis` candidate (eval-methodology trust) — noted here, no edge.
5. `el-code-mode` (industry-wide) vs `el-agent-repl` (Witan's persistent-state extension) kept as two nodes joined by `UsesElement`; merge into one if that's too granular.
