# SPIKE extraction — "RLM: Recursive Language Models for Large Codebases" (Shashi, Superagentic AI) — FOR REVIEW

Source transcript: `transcripts/shashi-superagentic-rlm-codebases.txt` (auto-captions — quotes are paraphrases, not verbatim; "ripple" = REPL, "recussion" = recursion, "grab" = grep throughout).
Video: https://youtu.be/8oyalrfwgjw — AI Engineer World's Fair (online track), published 2026-07-12.
`stagingTimestamp` for the artifact and all signals: 2026-07-12 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-shashi-rlm-codebases` | RLM: Recursive Language Models for Large Codebases (Shashi, Superagentic AI — AI Engineer World's Fair) | youtube | https://youtu.be/8oyalrfwgjw |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-shashi`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-shashi` | Shashi (founder, Superagentic AI; author of the RLM-Code open-source harness) — full name not stated in captions or title, flagged below | `AffiliatedWithCompany → co-superagentic` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-superagentic` | Superagentic AI | developer | Small AI tooling shop; publishes RLM-Code, an open-source research playground for recursive language models |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-recursive-language-models` | Recursive Language Models (RLM) | concept | context | Context-management pattern from an MIT paper: externalize context into a programmable execution environment — the repo (or corpus) is treated as data, the model writes REPL code to inspect/slice/compute relevant chunks feeding the main context window, and recursion happens via LLM sub-queries (delegating sub-questions to another model) until the loop terminates with a synthesized answer; a pattern to implement, not a product |
| `el-rlm-code` | RLM-Code | framework | context | Superagentic AI's open-source reference implementation of the RLM pattern: CLI + experimental coding-agent-style TUI harness, Docker-sandboxed REPL, pluggable local or cloud models (demoed with Gemini), budget/recursion-depth limits, JSONL traces exportable to any observability platform |

Element edges:
- `el-rlm-code` `DevelopedByCompany → co-superagentic`; `el-rlm-code` `UsesElement → el-recursive-language-models`
- both `IdentifiedInArtifact → ia-aie-shashi-rlm-codebases`
- `el-recursive-language-models` `EnablesPattern → pat-harness-over-model` **[registry]**

## Signals (3 new)

All: domain `context`, `SpottedInArtifact → ia-aie-shashi-rlm-codebases`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-monorepo-context-wall` | Coding agents work exceptionally well on small repos but degrade as context grows in large monorepos, and the standard mitigations shipped in today's harnesses — grep-style search tools, semantic/local search, context compaction/summarization, memory layers — don't hold up; the gap is driving new context-management architectures | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-recursive-language-models` |
| `sig-rlm-spreads-to-production` | RLM concepts are moving from the MIT paper into proprietary production harnesses within months: the speaker observed the Codex harness writing Python REPL code to curate its own context; Claude Code engineers at Anthropic acknowledged on X that they use RLM concepts; managed agents (Claude/Gemini) and dynamic multi-sandbox agent workflows read as RLM under the hood | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-recursive-language-models`; `RelevantCompany → co-openai` **[registry]**, `RelevantCompany → co-anthropic` **[registry]** |
| `sig-rlm-reimplementation-wave` | The RLM pattern is being independently reimplemented across the ecosystem shortly after publication — the authors' RLM / RLM-minimal, a DSPy implementation by the paper's author (also DSPy's author), Superagentic's RLM-Code, and assorted community variants — with the paper explicitly treated as a pattern anyone can re-implement in their own harness | `FormsPattern → pat-accelerated-research` **[registry]** | `OnElement → el-rlm-code` |

## Insights (1 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-context-as-external-program` | A codebase is structured data (directories, imports, tests, configs, dependencies), not flat text — which is why naive long-context stuffing fails; the RLM move is to manage context the way a lead engineer onboards a huge repo: inspect and take notes in a scratch environment (REPL), write scripts to search, and delegate what you don't understand to another specialist (recursive LLM query) — context curation becomes a program the model writes, not a window the model fills | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-recursive-language-models` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-shashi-rlm-codebases`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-apply-rlm-large-repos` | Apply the RLM pattern to large/unfamiliar codebases | Best-fit use cases: root-cause analysis and repo onboarding on large monorepos; run the REPL in a dedicated sandbox (e.g. Docker), treat the whole repo as data; design your harness to capture the full trajectory — planning, REPL code, bounded observations, LLM sub-calls, budget, final output; set explicit spend budgets and max recursion depth per run; emit JSONL traces and plug them into your observability platform of choice | `ReferencesElement → el-recursive-language-models`, `ReferencesElement → el-rlm-code` |

## Dropped

- DSPy as an Element — named as carrying an RLM implementation; kept as prose in `sig-rlm-reimplementation-wave`.
- Pydantic AI / Google ADK ("padenti", "Google ad" — garbles) — named only as frameworks you *could* implement RLM in.
- `el-anthropic-managed-agents` **[registry]** — the "Claude managed agents / Gemini managed agents" mention is speculation about RLM use under the hood; kept as prose in `sig-rlm-spreads-to-production`, no OnElement edge.
- Live-demo mechanics (connect/doctor commands, research-lab reward view) — product walkthrough, not extractable.

## Review notes

1. **Speaker identity unresolved**: only "Shashi" in both the official title and captions; `exp-shashi` coined without a surname — resolve against the AIE speaker roster before seeding.
2. **Caption garbles resolved**: ripple→REPL, recussion→recursion, grab→grep, "ally asking"→likely "actually asking", "eleant query"→LLM query, "Omar"→Omar Khattab (DSPy/RLM author; surname not in captions, left as prose). "monor repo"→monorepo.
3. `sig-rlm-spreads-to-production` rests partly on the speaker's reading of X posts and his own observation of Codex behavior — attributable but secondhand/anecdotal; weight accordingly.
4. Shared entity: `el-recursive-language-models` is also referenced by `brown-prime-intellect-post-training.md` (Verifiers V1 supports RLM harnesses) — defined here only.
5. Pattern-fit judgment: `sig-monorepo-context-wall` sits between `pat-model-not-bottleneck` (failure is in the context layer, not the model) and `pat-context-graphs`; chose the former since RLM is programmatic curation, not graph structure.
