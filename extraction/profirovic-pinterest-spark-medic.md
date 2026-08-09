# SPIKE extraction — "Medic for Apache Spark — First Aid for Failing Jobs" (Draško Profirović, Pinterest) — FOR REVIEW

Source transcript: `transcripts/profirovic-pinterest-spark-medic.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/0RNNfxpdbQk — AI Engineer World's Fair, published 2026-07-20.
`stagingTimestamp` for the artifact and all signals: 2026-07-20 (publish date).
Entities marked **[existing]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-profirovic-spark-medic` | Medic for Apache Spark — First Aid for Failing Jobs (Draško Profirović, Pinterest — AI Engineer World's Fair) | youtube | https://youtu.be/0RNNfxpdbQk |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-drasko-profirovic`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-drasko-profirovic` | Draško Profirović (Staff Engineer, Pinterest data platform) | `AffiliatedWithCompany → co-pinterest` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-pinterest` | Pinterest | media | appears as an enterprise building internal agentic tooling on its data platform |
| `co-langchain` | LangChain | developer | maintainer of LangGraph and the deep-agents library Medic is built on |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-spark-medic` | Medic for Apache Spark | product | data-eng | Pinterest's internal agentic diagnostics tool: ask "why did this job fail?" and get an evidence-grounded deep-research report with ≤N suggested fixes; multi-agent pipeline (intent classifier → triage → parallel hypothesis-research agents → supervisor → healer over a runbook vector DB), surfaced in Slack/Airflow; being generalized toward Flink and Trino |
| `el-langgraph` | LangGraph / deep agents | framework | harness | LangChain's agent-orchestration framework; its deep-agent library gives each agent a dedicated prompt + MCP-tool subset plus built-in steering tools (to-do list, virtual file system) — mirroring what Claude Code/Codex do natively; its deterministic *workflow* mode proved brittle for diagnostics vs ReAct agents |

Element edges: `el-spark-medic` `DevelopedByCompany → co-pinterest`; `el-spark-medic` `UsesElement → el-langgraph`; `el-spark-medic` `UsesElement → el-mcp` (**[existing]** — all tool access is MCP); `el-langgraph` `DevelopedByCompany → co-langchain`; both `IdentifiedInArtifact → ia-aie-profirovic-spark-medic`.

## Signals (3 new)

All: domain `data-eng`, `SpottedInArtifact → ia-aie-profirovic-spark-medic`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-pinterest-spark-medic-arc` | Pinterest shipped Medic (2026) to replace human support-rotation triage of Spark failures; the arc — raw MCP tools + careful prompting → single ReAct agent → multi-agent — was forced by concrete failures: one prompt couldn't do everything (detail added in one area degraded another), response quality was inconsistent, and log-sized tool outputs blew the context window on production jobs | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-pinterest` |
| `sig-deterministic-workflows-brittle` | Pinterest trialed LangGraph's deterministic workflow mode to make Medic more predictable and found it *brittle* compared to the reasoning-and-acting agent paradigm — a practitioner datapoint against hard-coding agent control flow for diagnostic work | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-pinterest` |
| `sig-metrics-as-images-bounded-tokens` | Pinterest found rendering raw time-series metrics into annotated, collaged chart images (min/max callouts, Grafana-like) analyzed by a quarantined sub-agent beat feeding raw data: guaranteed-bounded input tokens per job regardless of duration, and reliable detection of executors-to-zero drops, plateaus, and unhealthy-progress shapes | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-pinterest` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-shape-context-not-prompts` | Medic's quality gains came from shaping what enters context, not from prompt tuning or bigger models: exceptions pre-classified (benign patterns learned from *successful* jobs, fingerprinted, clustered, ranked) and served as top-K tools instead of raw logs; metrics quarantined into a sub-agent returning summaries; one prompt decomposed into role agents with tool subsets. The harness is the product | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-spark-medic`, `ReliesOnElement → el-langgraph` |
| `ins-evals-before-architecture` | The record/playback eval harness was the unlock that made every later refactor safe: quality went from anecdote ("manual tests on production data that gets retentioned away") to a graded regression suite — without it you cannot know whether changes broke earlier wins | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-spark-medic` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-profirovic-spark-medic`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-record-playback-evals` | Build a record/playback eval harness for production agents | Record mode: agent calls real downstream systems, tool responses captured as fixtures and checked in as code; playback mode: agent runs against fixtures and produces the report; grade reports with authored offline evals (e.g. penalize >3 suggested fixes to control verbosity); tune prompts against scores; add OTel traces (→ LangFuse) and read the run as a waterfall to localize quality drops | `ReferencesElement → el-spark-medic` |
| `how-exception-classifier-pipeline` | Don't feed agents raw logs — classify exceptions first | Regex heuristics don't scale; instead learn which exceptions commonly appear in *successful* jobs and treat them as red herrings; fingerprint + cluster + rank surviving exceptions by content relevance and recency-to-termination; expose exactly two tools — top-K truncated exceptions, and full detail for one exception — to stop the LLM anchoring on a misleading stack trace | `ReferencesElement → el-spark-medic`, `ReferencesElement → el-mcp` |
| `how-quarantine-heavy-analysis` | Quarantine token-heavy analysis in sub-agents | Any input whose size scales with job duration (time series, logs) must not touch the parent context; convert to bounded artifacts (annotated image collages) and analyze in a dedicated sub-agent that returns only a findings summary; give each role agent its own prompt + tool subset — scope expansion then becomes "add a prompt" (how Medic gained Spark-SQL optimization) | `ReferencesElement → el-spark-medic`, `ReferencesElement → el-langgraph` |

## Dropped

- Apache Spark, Flink, Trino, Airflow, Slack, OpenTelemetry, LangFuse as Element nodes — substrate technologies, kept in prose.
- "Support rotation is a never-ending stream" / LLMs-scale-where-humans-must-prioritize framing — motivation, folded into `sig-pinterest-spark-medic-arc`.
- Current experiment (auto-improvement from user session feedback) — announced direction, no result yet; revisit when shipped.

## Review notes

1. `co-pinterest` type: enum has no "consumer internet"; `media` chosen (social platform). Flip to `bigtech` if you prefer.
2. `co-langchain`/`el-langgraph` promotion call: Medic is *built on* it and the brittleness finding is about it, so I promoted both; demote to prose if you want vendor frameworks out of the element set.
3. All three signals are single-company practitioner findings (no external dated facts in this talk) — same caveat as the Daga file.
4. No security angle anywhere in the talk; nothing links to `pat-verification-gap` except the eval insight, which I kept because "quantify quality instead of intuition" is the verification thesis verbatim.
