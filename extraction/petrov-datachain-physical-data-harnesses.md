# SPIKE extraction — "When Agents Meet Physical Data: The Other Physics of Agent Harnesses" (Dmitry Petrov, DataChain) — FOR REVIEW

Source transcript: `transcripts/petrov-datachain-physical-data-harnesses.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/bUJgirn4_yc — AI Engineer World's Fair, published 2026-07-20.
`stagingTimestamp` for the artifact and all signals: 2026-07-20 (publish date).
Entities marked **[existing]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-petrov-physical-data` | When Agents Meet Physical Data: The Other Physics of Agent Harnesses (Dmitry Petrov, DataChain — AI Engineer World's Fair) | youtube | https://youtu.be/bUJgirn4_yc |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-dmitry-petrov`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-dmitry-petrov` | Dmitry Petrov (creator of DVC "Git for data"; ~10 years in data tooling; now DataChain) | `AffiliatedWithCompany → co-datachain` |

## Companies (2 new; 1 existing reused)

| slug | name | type | note |
|---|---|---|---|
| `co-datachain` | DataChain | developer | open-source data harness for coding agents over unstructured/physical data; lineage from the DVC project |
| `co-openai` | OpenAI | research | frontier lab; referenced here for its data-agent context-layers blog post. Surprisingly absent from the registry until now — expect heavy reuse |
| **[existing]** `co-anthropic` | — | — | 21%-accuracy data-agent finding |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-data-harness` | Data harness | concept | harness | Harness layer that lets a coding agent operate on physical/unstructured data: see it (schemas over binary internals), act on it (execution engine, distributed compute), verify it (fast tests via metadata layers), and remember it (shared dataset knowledge base). Counterpart to code harnesses; needed because agents' code-world intuition "pushes them in the wrong direction — the laws of physics change" |
| `el-datachain` | DataChain | product | data-eng | Open-source data harness for coding agents (Claude Code + 3 others): Pydantic as the single language for data/schema/code transpiled to SQL, execution engine with parallel/distributed mappers and generators, incremental updates + data checkpoints, and an MD-file dataset knowledge base (description, session context, deps, preview, stats, source code) giving full lineage |

Element edges: `el-datachain` `DevelopedByCompany → co-datachain`; `el-datachain` `UsesElement → el-data-harness` — review: arguably `ExemplifiesPattern`-style, but Element→Element only offers Enables/Uses; kept `UsesElement`. `el-data-harness` `EnablesPattern → pat-context-graphs`. Both `IdentifiedInArtifact → ia-aie-petrov-physical-data`.

## Signals (3 new)

All: domain `data-eng`, `SpottedInArtifact → ia-aie-petrov-physical-data`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-anthropic-data-agent-21pct` | Anthropic published (2026) that agent accuracy on data projects is only ~21% until dedicated data harnesses and context are added | `FormsPattern → pat-context-graphs`, `FormsPattern → pat-verification-gap` | `RelevantCompany → co-anthropic` |
| `sig-openai-data-agent-context-layers` | OpenAI's data-agent blog post: six layers of context required to make a data agent work on (structured) warehouse data; key conclusion — the dataset's **source code** is the most important context to preserve | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-openai` |
| `sig-physical-data-metadata-explosion` | The "neutron star" scaling law of physical data: 90 dashcam videos → ~100k detection records (24 min compute); 2,000 video files → millions of nested objects (clips→frames→objects→labels), ×10–100 going deeper. Both standard coping patterns fail — millions of JSONs on S3 (latency, no consistency) or a second database stack researchers won't touch | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-datachain` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-data-harness-over-model` | Model choice is not the lever for physical-data work — everyone already uses frontier models and they still fail, because coding-agent intuition (grep the files, run scripts on raw data) is wrong physics for binary data at scale. The harness that understands data's laws — schemas, execution engine, checkpoints, shared memory — is where capability comes from | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-data-harness` |
| `ins-data-answers-are-singular` | Verification is harder in data than software: a software task has many acceptable solutions, a data question usually has exactly one correct answer — and tests over raw binary data are the slowest, most expensive kind. Cheap verification must be manufactured (precomputed metadata layers) before agents can self-check | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-data-harness` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-petrov-physical-data`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-metadata-layer-over-raw` | Answer data questions from metadata layers, not raw binaries | Never run analysis scripts over raw object storage — slowest and most expensive path; maintain queryable metadata tables (classic dimensional modeling: star schema / one-big-table) over the raw data; teach the agent to ask "do I have a dataset to answer this in one SQL-ish query?" and, if not, build a layer general enough for the *family* of questions, not just the one asked | `ReferencesElement → el-data-harness`, `ReferencesElement → el-datachain` |
| `how-incremental-checkpoints` | Make incremental updates and data checkpoints non-negotiable | Heavy file processing (often LLM-per-file) fails mid-run from bugs/API errors; checkpoint so a rerun catches up on already-processed results instead of recomputing; new files in the bucket trigger delta-only compute; one schema language end-to-end (Pydantic → SQL, no SQL islands) keeps the engine able to distribute work by file/schema | `ReferencesElement → el-datachain` |
| `how-dataset-knowledge-base` | Share computed datasets as an agent-readable knowledge base | Every expensive dataset gets an MD record: LLM-enriched description, session context (why it was built), storage dependency, data preview, stats, and — most important — the generating source code; source data + code + warehouse result = lineage, so teammates' agents reuse results instead of paying double/triple recompute | `ReferencesElement → el-datachain` |

## Dropped

- Pydantic, Dask, Ray, Spark, YOLO, Copilot/Codex/Claude Code as Element nodes — supporting-cast technology mentions; Pydantic-as-single-language is captured inside `el-datachain` and `how-incremental-checkpoints`.
- The live demo mechanics (skill install, permission skipping, per-frame velocity options) — product walkthrough, not graph-worthy.
- "82 of 91 clips contain people" — demo output, not a signal.

## Review notes

1. `co-openai` is a new registry-level company — coined here (type `research`; flip to `bigtech` if you prefer). The 21%/six-layers figures are the speaker's characterization of Anthropic/OpenAI blog posts via auto-captions; treat numbers as paraphrase until the posts are cited directly.
2. `sig-anthropic-data-agent-21pct` double-links to `pat-verification-gap` — the 21%-without-harness number is as much about unverified agent output as about context. Cut that edge if you want it purely context-graphs.
3. `el-data-harness` vs the existing harness-domain elements from batch1 (`el-agent-hooks` etc.): no overlap found — this is a data-plane concept, they are lifecycle/security mechanisms.
