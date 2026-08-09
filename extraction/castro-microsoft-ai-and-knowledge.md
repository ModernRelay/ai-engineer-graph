# SPIKE extraction — "On AI and Knowledge (Intrinsic + Extrinsic + Learned)" (Pablo Castro, Microsoft) — FOR REVIEW

Source transcript: `transcripts/castro-microsoft-ai-and-knowledge.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/RGSFUqzqErE — AI Engineer World's Fair, published 2026-07-17.
`stagingTimestamp` for the artifact and all signals: 2026-07-17 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-castro-ai-and-knowledge` | On AI and Knowledge: Intrinsic + Extrinsic + Learned (Pablo Castro, Microsoft — AI Engineer World's Fair) | youtube | https://youtu.be/RGSFUqzqErE |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-pablo-castro`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-pablo-castro` | Pablo Castro (Distinguished Engineer & CVP, Microsoft; information-retrieval lead behind Azure AI Search / Foundry IQ) | `AffiliatedWithCompany → co-microsoft` **[registry]** |

## Companies (0 new)

Reused: `co-microsoft` **[registry]** (speaker + platform), `co-anthropic` **[registry]** (Claude-in-Foundry GA signal).

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-microsoft-foundry` | Microsoft Foundry | product | infra | Microsoft's agent platform: hosting, observability, management, a model catalog of thousands of models (now incl. Claude GA), knowledge bases, and the agent optimizer; the demoed hub for grounding and tuning agents (ai.azure.com) |
| `el-microsoft-iq` | Microsoft IQ | product | context | Family of grounding entry points into an organization's "ambient data": Work IQ (SharePoint docs, email, calendar, chats, people graph), Fabric IQ (warehouses, lakes, Power BI), Foundry IQ (bring-your-own data for agents, backed by Azure AI Search), Web IQ (public web grounding) — one entry point for agent grounding beyond agent-specific knowledge |
| `el-agentic-retrieval` | Agentic retrieval | concept | context | Retrieval as a reflective loop rather than single-shot search: the system inspects the dataset, decides whether the stated information need is satisfied, and iterates before returning; in Microsoft's evals it consistently beats individual simple methods on difficult cases (evidence recall, answer completeness), at a latency/quality trade-off |
| `el-foundry-agent-optimizer` | Foundry agent optimizer | product | harness | Foundry component materializing the "learned knowledge" loop: generates a task-adherence eval from an agent's traces and instructions if none exists, establishes a baseline, then hill-climbs candidate configurations (instructions/tools/skills) GEPA-style and applies the winner by swapping externalized config |

Element edges: all four `IdentifiedInArtifact → ia-aie-castro-ai-and-knowledge`; `el-microsoft-iq` and `el-foundry-agent-optimizer` `DevelopedByCompany → co-microsoft`; `el-microsoft-foundry` `DevelopedByCompany → co-microsoft`; `el-microsoft-iq` `EnablesPattern → pat-context-graphs` **[registry]**; `el-agentic-retrieval` `EnablesPattern → pat-context-graphs`.

## Signals (5 new)

All: domain `context` (except where noted), `SpottedInArtifact → ia-aie-castro-ai-and-knowledge`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-claude-in-foundry-ga` | Claude announced generally available in Microsoft Foundry the day before the talk (~2026-07-16) — Anthropic's models distributed inside Microsoft's unified enterprise agent platform ("best of both worlds") | — (distribution/partnership fact; no pattern fit — see notes) | `RelevantCompany → co-anthropic`, `co-microsoft` |
| `sig-grounding-goes-company-wide` | Microsoft's field observation: every agent needs its own curated knowledge plus the org's ambient data (documents, email, chat threads, warehouse) the moment it acts beyond its silo — grounding has evolved from simple isolated datasets to company-wide, productized as the IQ family | `FormsPattern → pat-context-graphs` | `OnElement → el-microsoft-iq`, `RelevantCompany → co-microsoft` |
| `sig-vector-only-retrieval-over` | The industry's "hot second" of believing cosine similarity was all retrieval needed is over: Microsoft's evals (Azure AI Search behind Foundry IQ) repeatedly show combined methods beating any individual method on real customer scenarios, and agentic retrieval beating simple retrieval on difficult cases across evidence-recall and answer-completeness metrics | `FormsPattern → pat-context-graphs` | `OnElement → el-agentic-retrieval` |
| `sig-knowledge-bases-ship-as-mcp` | Every knowledge base created in Foundry is exposed as an MCP server, connectable to any harness with no glue code — MCP as the default interop surface for enterprise knowledge grounding | `FormsPattern → pat-context-graphs` | `OnElement → el-mcp` **[registry]** |
| `sig-learning-loops-productized` | "Learned knowledge" is being productized: Foundry's agent optimizer auto-generates evals from agent traces and hill-climbs instructions/tools/skills configs (~45-min runs), materializing the compounding people+agents learning loop Satya Nadella recently wrote about — org-unique knowledge captured as tuned agent behavior | `FormsPattern → pat-context-graphs` | `OnElement → el-foundry-agent-optimizer`, `RelevantCompany → co-microsoft` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-knowledge-three-kinds` | Agent knowledge splits into three kinds with a historical arc: intrinsic (parametric — what powered the Copilot/ChatGPT inflection and the '96-IntelliSense-to-zero-handwritten-code exponential), extrinsic (RAG grown into context engineering and company-wide grounding), and learned (loops that observe agents doing the work and tune them from traces). The learned kind is the newest leg and the one that captures what's unique to each organization — its differentiation | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-foundry-agent-optimizer` |
| `ins-layered-retrieval-platform` | A knowledge platform must layer its complexity: turnkey at the top ("here are my PDFs, deal with them" — chunking, vectorization, ranking under the covers) with expert control at the bottom (index structure, vector quantization, lexical retrieval) in the same stack, so teams move up and down as needs change; plus token-efficiency as a first-class retrieval metric (most information-dense answer in fewest tokens) | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-microsoft-foundry`, `ReliesOnElement → el-agentic-retrieval` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-castro-ai-and-knowledge`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-ground-agents-owned-plus-ambient` | Ground agents on owned + ambient + web knowledge | Manage the agent-specific knowledge yourself, but plan for ambient org data (docs, email, chats, analytics) the moment the agent leaves its silo, and add web grounding to complete the world view. Combine retrieval methods rather than betting on vectors alone; reserve agentic retrieval for difficult cases and treat its extra effort as an explicit latency/quality dial; expose knowledge bases as MCP servers to plug into existing harnesses | `ReferencesElement → el-microsoft-iq`, `ReferencesElement → el-agentic-retrieval`, `ReferencesElement → el-mcp` **[registry]** |
| `how-externalize-config-for-learning-loops` | Externalize agent config so learning loops can tune it | Write agents however you like, but externalize instructions, tool definitions, and skills as configuration; if no eval exists, generate a task-adherence eval from traces + instructions; baseline, hill-climb candidates against the rubric, and promote by swapping config — non-handwritten instructions emerging from reflection on real usage traces | `ReferencesElement → el-foundry-agent-optimizer` |

## Dropped

- The 25-years-apart code anecdote and IntelliSense→Copilot timeline dates — folded into `ins-knowledge-three-kinds` as the intrinsic-knowledge arc; no separate signal since the events are historical, not new observations. The OpenClaw zero-handwritten-code milestone rides in that insight too (registry `el-openclaw` mentioned in prose only; no edge — it's an illustration here, not this talk's claim).
- "Opus 4.5 ships" late-2025 reference — historical marker in the timeline, prose only.
- The movies-dataset demo mechanics (blob storage, parquet, index inspection) — product walkthrough detail, folded into knowhow/element briefs.

## Review notes

1. `sig-claude-in-foundry-ga` carries no `FormsPattern`: it is a dated, concrete distribution fact but none of the registry patterns cover lab-to-platform distribution deals; per the pattern budget I did not coin one. If a partnership/consolidation pattern ever exists, this signal is evidence.
2. Caption garbles: "actually I search" read as **Azure AI Search** ("the search technology behind Foundry IQ" — high confidence); "a J power style kind of loop" read as **GEPA-style** (prompt-optimization method — medium-high confidence, kept in element brief); "Open Claw" = OpenClaw (registry `el-openclaw`).
3. Talk title in the supplied list ("Intrinsic + Extrinsic + Learned") used for the artifact name; the spoken framing matches.
4. Element granularity: Work/Fabric/Foundry/Web IQ kept as one `el-microsoft-iq` node (the speaker presents them as "not one feature, a set of capabilities" under one entry point). Split at reconciliation if per-product nodes are wanted; Foundry IQ is the one with independent technical content (Azure AI Search, knowledge bases).
5. Five signals is at the top of the band; `sig-knowledge-bases-ship-as-mcp` is the most droppable (single product fact) — fold into `how-ground-agents-owned-plus-ambient` if trimming.
6. All pattern links go to `pat-context-graphs`; `pat-model-not-bottleneck` was considered for `sig-grounding-goes-company-wide` ("an interesting model got us here, but it only gets you so far") but the talk's substance is knowledge infrastructure, so single-linked.
