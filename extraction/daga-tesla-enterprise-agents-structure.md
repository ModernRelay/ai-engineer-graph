# SPIKE extraction — "Enterprise Agents Have a Structure Problem" (Ishita Daga, Tesla) — FOR REVIEW

Source transcript: `transcripts/daga-tesla-enterprise-agents-structure.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/B8l81jhvHbI — AI Engineer World's Fair, published 2026-07-20.
`stagingTimestamp` for the artifact and all signals: 2026-07-20 (publish date).
Entities marked **[existing]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-daga-structure-problem` | Enterprise Agents Have a Structure Problem (Ishita Daga, Tesla — AI Engineer World's Fair) | youtube | https://youtu.be/B8l81jhvHbI |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-ishita-daga`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-ishita-daga` | Ishita Daga (ML engineer, Tesla; builds enterprise data agents) | `AffiliatedWithCompany → co-tesla` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-tesla` | Tesla | hardware | appears here as an enterprise deploying internal data agents, not as an AI vendor |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-source-of-truth-hierarchy` | Source-of-truth hierarchy | concept | context | Ranked ordering of an enterprise agent's knowledge sources from cleanest/least flexible to messiest/most dynamic: semantic layer → canonical parametric queries → full database graph; agent answers by descending the hierarchy instead of weighting all knowledge bases equally |
| `el-semantic-layer` | Semantic layer | concept | data-eng | Curated single layer of KPI definitions, metric calculations, canonical queries, and business definitions that a data agent references first; the cleanest source of truth and the first thing an enterprise should build |

Element edges: `el-source-of-truth-hierarchy` `UsesElement → el-semantic-layer`; both `IdentifiedInArtifact → ia-aie-daga-structure-problem`; `el-source-of-truth-hierarchy` `EnablesPattern → pat-context-graphs`.

## Signals (3 new)

All: domain `context`, `SpottedInArtifact → ia-aie-daga-structure-problem`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-tesla-agent-failures-structural` | Tesla enterprise-agent practitioner: data-agent failures trace to structure — source-of-truth ambiguity, stale context, uncaptured preference — not model capability; bigger/latest models, longer context, and more .md/MCP knowledge bases don't fix them | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-tesla` |
| `sig-enterprise-context-staleness` | KPI definitions, processes, and decisions inside the enterprise change faster than .md files and skills get updated; without a context lifecycle (live mandatory sources like GitHub/CRM/dbt + logged correction events + evals) agent context rots | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-tesla` |
| `sig-preference-routing-unsolved` | Metric preference remains industry-unsolved: two teams compute the same "average milestone time" differently, both correctly; semantic layers and agent memory (mem0, memory.md) store but cannot route between valid competing definitions; frontier labs actively researching | `FormsPattern → pat-context-graphs` | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-structure-over-scale` | When an enterprise agent gives bad answers the reflex is a bigger model or more knowledge bases; the actual failure is unstructured context — undifferentiated sources of truth, no update lifecycle, no preference capture. Structure, not scale, is the lever | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-source-of-truth-hierarchy` |
| `ins-preference-is-the-open-frontier` | Ambiguity and staleness have engineering answers (hierarchy, lifecycle); preference does not — routing an agent to the right metric based on who is asking amounts to building a "hive mind" per team/individual and is the open research frontier of enterprise agents | `HighlightsPattern → pat-context-graphs` | — |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-daga-structure-problem`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-source-of-truth-hierarchy` | Build sources of truth as a ranked hierarchy | Rank knowledge sources cleanest→most flexible; answer by descending; build semantic layer + canonical parametric queries first (~80% of questions, cheap to set up); add the full database graph last for the remaining 20% (expensive to build and maintain) | `ReferencesElement → el-source-of-truth-hierarchy`, `ReferencesElement → el-semantic-layer` |
| `how-context-lifecycle` | Run a context lifecycle, not static context | Embed live, mandatory, frequently-updated data sources (GitHub, CRM, Tableau/dbt semantic layers) rather than hand-maintained .md files; log every correction event ("this definition is wrong/updated"); evaluate continuously — human-annotated suite or automated regression against recent Q&A — and update context on a cadence | `ReferencesElement → el-semantic-layer` |

## Dropped

- mem0 / memory.md as Element nodes — named only as inadequate options for preference storage; kept as prose inside `sig-preference-routing-unsolved`.
- MCP mention — passing reference ("plugins, MCP servers"), no load-bearing content; no edge to `el-mcp`.
- The team-A/team-B milestone example — illustration, folded into the preference signal.

## Review notes

1. Thin-signal talk: it is a framework talk with no external dated facts, so all three signals are practitioner-testimony observations from inside Tesla. If that fails your signal bar, the fallback is 1 signal (`sig-preference-routing-unsolved`) + the two insights.
2. `co-tesla` type: schema enum has no "enterprise/automotive"; `hardware` chosen. Flip to `bigtech` if you prefer.
3. `el-semantic-layer` is a decades-old BI concept — kept as an Element because two talks in this batch and the preference discussion lean on it; drop to prose if you want only AI-native elements.
