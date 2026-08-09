# SPIKE extraction — "Structuring the Unstructured" (Cedric Clyburn, Red Hat) — FOR REVIEW

Source transcript: `transcripts/clyburn-redhat-structuring-unstructured.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/-x5GEVnkuRw — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact and all signals: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

Context: a Docling talk — extracting structure (layout, tables, images, captions) from enterprise documents locally, and using that structure downstream (RAG, chunkless/agentic RAG, docling-serve at scale, Docling MCP server for agents). `el-docling` already exists in the registry (batch 8) and is REUSED here, not redefined. ⚠ The transcript's second half garbles "Docling" as "DocQuery"/"Doc Lee" throughout — all read as Docling (Review note 1).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-clyburn-structuring-unstructured` | Structuring the Unstructured (Cedric Clyburn, Red Hat — AI Engineer World's Fair) | youtube | https://youtu.be/-x5GEVnkuRw |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-cedric-clyburn`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-cedric-clyburn` | Cedric Clyburn (open source engineer / developer advocate, Red Hat) | `AffiliatedWithCompany → co-red-hat` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-red-hat` | Red Hat | developer | open-source enterprise software company (IBM subsidiary); appears here both as speaker employer and as a Docling-at-scale user (thousands of product-documentation PDFs) |
| `co-hugging-face` | Hugging Face | developer | AI platform/community (models, datasets); appears via the public FinePDFs cost-comparison case (Review note 5) |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-chunkless-rag` | Chunkless RAG (outline-as-index agentic retrieval) | concept | context | RAG without a chunker, embedding model, or vector database: parse the document into a layout-aware structured object (Docling's Pydantic document), then use its markdown outline + per-section summaries as the *entire* retrieval index; an agentic loop (~5 iterations in the demo) picks candidate sections relevant to the question, pulls full section text from the structured document, judges sufficiency, and iterates; demonstrated on Docling's own 8-page paper (20 sections) and scaled to IBM's 2025 annual report (418 sections) |

Element edges: `el-chunkless-rag` `IdentifiedInArtifact → ia-aie-clyburn-structuring-unstructured`; `el-chunkless-rag` `UsesElement → el-docling` **[registry]**.

Registry element reuse (no new node, edge only): `el-docling` **[registry]** `IdentifiedInArtifact → ia-aie-clyburn-structuring-unstructured` — the talk's central element (local CLI/library, Linux Foundation project: OCR + layout-analysis + table/vision models → markdown/JSON/HTML/Pydantic, plus docling-serve REST scaling and a Docling MCP server; this talk adds operator-level detail worth folding into the central brief at reconciliation, Review note 2); `el-mcp` **[seed]** `IdentifiedInArtifact → ia-aie-clyburn-structuring-unstructured` — the Docling MCP server (conversion/generation/manipulation tools) is demoed as the agent integration path.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-clyburn-structuring-unstructured`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-unstructured-data-new-context-layer` | data-eng | Framing claim (citing Jensen Huang's NVIDIA keynote): unstructured data is becoming the new context layer for AI — the large majority of the world's data is unstructured (PDFs, presentations, contracts, technical docs, meeting notes, scans, diagrams, tables, images) and spread across dozens of systems; Red Hat's own reality: thousands of product-documentation PDFs; no matter the model or agent, this data must be transformed into something an LLM can use, and proprietary parsing services force sending private data to someone else's server | `FormsPattern → pat-context-graphs` **[registry]** | `RelevantCompany → co-nvidia` **[registry]**, `RelevantCompany → co-red-hat` |
| `sig-scanned-pdf-term-cascade` | data-eng | Viral cautionary case: ~20 scientific papers now feature a nonsensical term that doesn't exist because an AI misread an old scanned two-column PDF and merged words across columns; researchers using models to help write propagated the term, and the papers are now being cited by others — unverified machine extraction is compounding through the scientific record (a Docling-style layout parse shows the two words are far apart and should never have merged) | `FormsPattern → pat-verification-gap` **[registry]** | — |
| `sig-ingestion-determines-answer-quality` | data-eng | Practitioner claim: regardless of model choice (NVIDIA-accelerated, open-source, or proprietary), how you process source data is *the* key determining factor in whether the end user's answer is correct; naive PDF parsers truncate/merge text and spit tables out linearly into output indecipherable even to a human, while frontier-model parsing (~$30/M output tokens) is expensive at thousands-of-PDF scale and non-deterministic — structured output changes between model versions (a 5.1 deprecated into a 5.2), making consistency at scale tricky | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-red-hat` |
| `sig-local-structured-parsing-50x-cheaper` | data-eng | Public Hugging Face case (Leandro, FinePDFs): pre-extracting structure with OCR + Docling for common-crawl PDFs achieved ~50× cost savings versus naively running VLMs+OCR — on CPU, no GPU needed — producing training-grade text at web scale; specialized local pipelines beat frontier-model calls for document structure at scale (⚠ figures caption-read, Review note 6) | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-hugging-face` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-parsing-is-upstream-of-everything` | Document-parsing quality is upstream of every downstream AI property — RAG correctness, agent extraction/validation, fine-tuning data, even the future scientific record (the citation cascade shows one bad extraction compounding through papers that train tomorrow's models); engineering spend belongs there before model upgrades, because no model choice repairs garbled ingestion | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-docling` **[registry]** |
| `ins-structure-makes-the-index` | Once a document is parsed into a layout-aware structured object (sections, tables, images, captions, bounding boxes), its own outline can serve as the retrieval index — chunkers, embedding models, and vector databases become optional components rather than mandatory RAG plumbing; structure extraction upstream buys retrieval simplicity downstream | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-chunkless-rag` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-clyburn-structuring-unstructured`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-local-document-pipeline` | Run document structuring locally with Docling | `pip install docling`; convert PDFs/websites via DocumentConverter to markdown/JSON/HTML/dict with page layout preserved (works air-gapped, CPU-only, no data leaves the machine); export detected tables straight to dataframes; scale up image extraction via a PDF pipeline; enrich images/diagrams with a local VLM (demo: Granite via Ollama's OpenAI-compatible endpoint) so tribal knowledge survives the SME leaving; use the layout visualizer's bounding boxes to locate elements — e.g., strip PII regions before ingestion; scale out with docling-serve as a REST microservice (container/Kubernetes) with per-request options (OCR, backend, image annotation); wire agents in via the Docling MCP server (conversion/generation/manipulation tools) from Claude Code, Cursor, Continue, etc.; use structured output when you need only specific fields (bill number, total) from a document like an invoice | `ReferencesElement → el-docling` **[registry]**, `ReferencesElement → el-mcp` **[seed]** |
| `how-chunkless-rag-loop` | Answer questions over big documents without a vector DB | Parse the document with Docling; hand the agent the markdown outline with per-section summaries as the entire retrieval index; loop (~5 iterations): pick the sections most relevant to the query, pull their full text from the structured document, judge whether they answer the question, iterate if not; works from a 20-section paper to a 418-section annual report; skip the chunker/embedding/vector-database stack entirely for single-corpus Q&A | `ReferencesElement → el-chunkless-rag`, `ReferencesElement → el-docling` **[registry]** |

## Dropped

- "DocQuery" / "Doc Lee" — recurring caption garbles for Docling; no separate product exists (Review note 1).
- Hybrid Chunker ("Hybrid Chunkier") — Docling feature mention; explicitly NOT linked to `el-hybrid-search` **[registry]**, which is a different thing (Review note 3).
- Granite, Ollama, MLX, Qwen ("Quinn 3.6"), VS Code, Pydantic — demo-stack mentions, prose inside the knowhow.
- IBM 2025 annual report — demo corpus, prose (no `co-ibm` coined; IBM appears only as document subject).
- Linux Foundation governance — kept as prose in the registry-reuse line for `el-docling`.
- Session-slides link, LinkedIn outro, "open-source world looking bright" close — color.

## Review notes

1. Caption garble: from the chunkless-RAG demo onward the transcript renders Docling as "DocQuery" (and once "Doc Lee") — context (same pip package, same paper, same pipeline) makes clear it's Docling throughout; no separate DocQuery product coined.
2. `el-docling` **[registry, batch 8]** reused, not redefined. This talk is the richest Docling source in the corpus so far (docling-serve, MCP server, VLM enrichment, bounding-box/PII workflow, FinePDFs case) — consider enriching the central element brief at reconciliation.
3. "Hybrid Chunkier" = Docling's HybridChunker (a chunking utility). Despite the surface similarity it is NOT `el-hybrid-search` **[registry]** (retrieval technique from the MongoDB talk) — deliberately no link.
4. Jensen Huang's keynote claim is second-hand framing inside this talk — kept inside `sig-unstructured-data-new-context-layer` with `RelevantCompany → co-nvidia` rather than as a separate expert/artifact.
5. "Leandro at Hugging Face" is likely Leandro von Werra (surname not in captions) — company coined (`co-hugging-face`), person left in prose; verify against the FinePDFs writeup.
6. Numbers hygiene: the 50× savings, ~$30/M output tokens, 20 papers, 418 sections, and 8 pages are caption-read; the 50× figure should be verified against the public FinePDFs comparison before public-facing use.
7. `sig-scanned-pdf-term-cascade` is this batch's cleanest `pat-verification-gap` data point outside the security track — unverified machine reading entering (and self-reinforcing in) the scientific record.
8. `co-red-hat` type: `developer` chosen (open-source software vendor); flip to `bigtech` if you treat it as IBM's arm.
