# SPIKE extraction — "Turn 10,994 Notes Into Memory" (Paul Iusztin, Decoding AI & Louis-François Bouchard, Towards AI) — FOR REVIEW

Source transcript: `transcripts/iusztin-bouchard-notes-into-memory.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/ZRM_TfEZcIo — AI Engineer World's Fair, published 2026-06-26.
`stagingTimestamp` for the artifact and all signals: 2026-06-26 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

Context: two speakers — Paul Iusztin (captions: "Paul Yushin"; founder/CEO of Decoding AI, co-author of the LLM Engineer's Handbook) and Louis-François Bouchard (captions: "Luis François"; co-founder/CTO of Towards AI, creator of the What's AI YouTube channel). They present "AI Research OS", an open workshop repo that turns a personal second brain (10k+ notes) into agent-usable research memory.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-iusztin-bouchard-notes-memory` | Turn 10,994 Notes Into Memory (Paul Iusztin & Louis-François Bouchard — AI Engineer World's Fair) | youtube | https://youtu.be/ZRM_TfEZcIo |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-paul-iusztin`, `ContributedByExpert → exp-louis-francois-bouchard`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-paul-iusztin` | Paul Iusztin (founder/CEO, Decoding AI; co-author, LLM Engineer's Handbook) | `AffiliatedWithCompany → co-decoding-ai` |
| `exp-louis-francois-bouchard` | Louis-François Bouchard (co-founder/CTO, Towards AI; creator of the What's AI YouTube channel; author, Building AI Systems for Production; ex-AI PhD student) | `AffiliatedWithCompany → co-towards-ai` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-decoding-ai` | Decoding AI | media | AI-education company (content + courses on shipping AI products), founded by Paul Iusztin |
| `co-towards-ai` | Towards AI | media | AI-education company (courses, trainings for companies, publication); co-founded by Louis-François Bouchard; also builds for clients |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-ai-research-os` | AI Research OS | framework | context | Open workshop repo by Decoding AI + Towards AI: a set of Claude Code / Codex skills (packaged as a Claude Code plugin) that runs personal deep research over your second brain (Obsidian, Readwise, NotebookLM, GitHub repos, YouTube transcripts, web links/documents) and materializes the results as a three-layer file system — immutable `raw/` sources, an `index.yaml` reference catalog (per-source link, origin, title, authors, date, summary), and an LLM-maintained `wiki/` of derivatives (concepts, entities, comparisons, notes, open questions). No vector DB, no knowledge-graph infra — plain markdown + references. Wikis are scoped per project (article, video, book, course, codebase), and the wiki keeps evolving from the questions you ask, not just from ingestion |
| `el-deep-research` | Deep research loop (orchestrator + query rounds) | technology | context | Multi-round research algorithm: an orchestrator agent frames N queries per round from the topic + scraped seed context ("golden links"); per-question sub-agents search (in the talk: Gemini grounded in Google search) and return links + executive summaries; the orchestrator aggregates compactly; ~3 rounds × ~6 queries yields 40–50 links, then a ranking pass scores each source against the topic, fully scrapes only the top-K, and keeps summaries for the rest. Generic technique (public deep-research products exist); the talk's move is retargeting it from the public web to your own sources |
| `el-second-brain` | Second brain (personal knowledge base) | concept | context | Accumulated personal notes/highlights/meeting recaps/saved links across tools (Obsidian, Readwise, Notion, Apple Notes, Granola, Google Drive), typically organized PARA-style (projects/areas/resources/archive, Tiago Forte); in the talk it is the immutable, human-curated substrate agents read from via research skills — and never write to |
| `el-obsidian` | Obsidian | product | context | Local-first markdown note tool; used as both the second-brain store (a vault on the file system, syncable across devices) and the inspection UI for generated wikis — its graph view renders the index's references as a navigable subgraph of concepts/entities |

Element edges: all four `IdentifiedInArtifact → ia-aie-iusztin-bouchard-notes-memory`; `el-ai-research-os` `DevelopedByCompany → co-decoding-ai` and `DevelopedByCompany → co-towards-ai`; `el-ai-research-os` `UsesElement → el-deep-research`, `UsesElement → el-second-brain`, `UsesElement → el-obsidian`; `el-ai-research-os` `ExemplifiesPattern → pat-context-graphs` **[registry]**.

Registry element reuse (no new node, edge only): `el-progressive-disclosure` **[registry]** `IdentifiedInArtifact → ia-aie-iusztin-bouchard-notes-memory` — the wiki's query path (index summaries → source wiki page → derivative pages → full raw source, stop as early as possible) is progressive disclosure applied to personal memory; `el-claude-code` **[registry]** and `el-codex` **[registry]** `IdentifiedInArtifact → ia-aie-iusztin-bouchard-notes-memory` — the harnesses the skills plug into (system is deliberately harness-agnostic).

## Signals (4 new)

All: domain `context`, `SpottedInArtifact → ia-aie-iusztin-bouchard-notes-memory`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-second-brain-harness-gap` | Two AI-education practitioners with 10k+ notes (5k Obsidian + 5k Readwise + Notion/Drive, growing ~250 files/month) find stock tools can't durably leverage a personal second brain: reading lists become graveyards, Codex/Claude Code sessions require re-pasting the same links/PDFs every time, on-the-fly structures and scripts are lost when the session ends, and NotebookLM is closed (you don't own it, can't personalize it, not agent-native, weak for coding). Their fix is a system that "sits between those harnesses and your second brain". Bouchard's framing (paraphrase): the information you give the model is not the bottleneck — the bottleneck is how you leverage it in the future; the context window is forced to be database, file system, memory, and reasoning space at once, and loses everything when the conversation stops | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-decoding-ai`, `RelevantCompany → co-towards-ai` |
| `sig-files-over-retrieval-infra` | Deliberate architecture rejection for personal-scale memory: they dropped vector databases, knowledge graphs, semantic search, and text search ("all that is beautiful, but adds a lot of complexity") in favor of plain markdown files plus an `index.yaml` of references — a mechanism "rooted into how your computer works" that stays human-inspectable and agent-navigable; retrieval-infra RAG is acknowledged as right for products at scale but wrong for a daily-driver personal research OS | `FormsPattern → pat-context-graphs` **[registry]** (see Review note 4) | — |
| `sig-wiki-living-memory` | The wiki layer is alive: every question leaves a trace (the LLM can create new concept/note/comparison files; every question is logged), so the wiki evolves from conversation, not only from ingestion — "a true reflection of yourself, of what you haven't understood, of all your questions from the past". This layer exists because V2's static `research.md` output forced full, token-expensive re-runs whenever a follow-up question arrived or information went stale | `FormsPattern → pat-context-graphs` **[registry]** | — |
| `sig-deep-research-aimed-inward` | System progression V1→V2: the deep research loop was retargeted from the public web (which required manually handpicked "golden links" and produced generic results) to the second brain, which supplies golden links organically because its contents are already filtered by the owner; V1 (web-only) still generated 35 course lessons "really quick", but the inward-aimed version anchors research in personal notes, values, and prior work | `FormsPattern → pat-context-graphs` **[registry]** | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-memory-layer-between-harness-and-brain` | The durable asset is a harness-agnostic memory layer of plain files + references sitting between whichever agent harness you use and your accumulated knowledge: harnesses are swappable (Claude Code, Codex), per-session context is disposable, but the wiki compounds — the answer to "why not just use Codex Cloud or NotebookLM" is that you are, and you still need the layer in between | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-ai-research-os` |
| `ins-hierarchy-buys-token-efficiency` | A reference hierarchy (index summaries → per-source executive summary → wiki derivative → full raw source) means the agent usually stops early and reads the expensive full source only as a last resort — token efficiency achieved through file structure and referencing instead of retrieval infrastructure; executive summaries are computed once at ingestion and amortized forever | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-progressive-disclosure` **[registry]** |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-iusztin-bouchard-notes-memory`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-file-based-research-wiki` | Build research memory as raw/index/wiki file layers | Keep `raw/` sources immutable — never edited; maintain `index.yaml` as the single agent entry point (per-source link + origin/title/authors/date/summary metadata, plus pointers to all wiki pages); let the LLM own only the `wiki/` derivatives (concepts, entities, comparisons, notes, open questions); log every question and let answers create/update wiki files; never let the LLM write to your personal notes — the second brain is an immutable snapshot; scope one wiki per project (article, video, course, codebase) and treat the project as the work, the second brain as the research; pipe saves into a PARA-style flat resources list and reference them into projects | `ReferencesElement → el-ai-research-os`, `ReferencesElement → el-second-brain` |
| `how-scope-deep-research-cost` | Budget deep-research rounds — the loop burns tokens | Default to light (1 round × 3 queries) or fast (2 × 3); reserve full deep mode for genuinely large surveys over "tons and tons of notes"; seed the loop by scraping known golden links first so question-framing starts informed; after query rounds, rank every source against the topic and fully scrape only the top-K (keep executive summaries for the rest); expect 10–20 minutes per run across Obsidian/Readwise/NotebookLM connectors | `ReferencesElement → el-deep-research` |

## Dropped

- Readwise, NotebookLM, Granola, Notion, Apple Notes, Google Drive, Bright Data, Gemini-grounded-search — connector/tool mentions kept as prose inside element briefs and signals; not coined (NotebookLM's ownership critique lives inside `sig-second-brain-harness-gap`).
- PARA method / Tiago Forte — prose inside `el-second-brain` and the knowhow; method-altitude, not coined.
- Demo 2's ingested harnesses — "open code, Pi, and Hermes" (opencode + two others; see Review note 7) — demo material, prose only.
- Wiki-generated comparison examples ("agentic RAG vs file systems", "compaction versus recursive language models") — incidental mentions; no edges to `el-context-compaction`/`el-recursive-language-models` **[registry]**.
- LLM Engineer's Handbook / Building AI Systems for Production — expert-bio prose.
- Towards AI Academy / Agent Engineering course pitch (~60h, final project = this system) — closing promo, color.
- Named next-improvements list (stronger linting, memory compaction, source provenance/ranking) — roadmap prose, folded into Review note 6.

## Review notes

1. Name garbles: captions render the speakers "Paul Yushin" and "Luis François" — resolved to Paul Iusztin and Louis-François Bouchard from the official talk listing. Iusztin's brand is historically "Decoding ML"; both the listing and the transcript say "Decoding AI", so `co-decoding-ai` follows the talk.
2. The title's "10,994 notes" matches the transcript's "over 5,000 in Obsidian and another 5,000 in Readwise, and some scattered in Notion and Google Drive".
3. `sig-second-brain-harness-gap` → `pat-model-not-bottleneck` is near-verbatim: Bouchard says the information given to the model "is not the bottleneck — the bottleneck is how can you leverage it in the future".
4. `sig-files-over-retrieval-infra` nuance: they explicitly reject knowledge-graph *infrastructure* yet converge on graph-shaped context (typed derivative notes, entity/concept links, an index of references rendered as an Obsidian subgraph). Read as supporting `pat-context-graphs` at concept altitude; flip to `ContradictsPattern` only if you read the pattern as graph-database infra specifically.
5. `el-karpathy-llm-wiki` **[seed]** resonance: the wiki layer is a working instance of the LLM-maintained-wiki idea ("a personalized research assistant that builds some sort of Wikipedia that compounds over time"). No Element→Element edge type fits cleanly; flagged for central cross-linking instead of forcing `UsesElement`.
6. Candidate pattern (NOT coined, no edges): "persistent agent memory as a first-class stack layer" — this talk, `savkin-nx-genius-with-amnesia`, and `pankaj-starlight-retrieval-boundary` (all this batch) independently argue for a session-transcending memory layer between harness and knowledge; prior registry echoes: `el-semantic-episodic-memory` (batch 2), `el-agent-sleep-cycle` (batch 6), mem0 mentions (daga). Left for central decision.
7. "Pi" and "Hermes" in demo 2 are plausibly the badlogic "pi" coding agent and Nous Research's Hermes agent (`el-hermes-agent` **[seed]**) but captions are too thin to confirm — left as prose, no edge.
8. `el-obsidian` is a borderline coin (the talk says "you don't have to use that") — kept because the memory/context talk set keeps hitting it as the de-facto local-notes substrate; no `DevelopedByCompany` edge (vendor not load-bearing).
9. The AI Research OS repo is named only as "the AI research OS workshop repository"; no URL in captions — `repository` field left empty, verify before seeding.
