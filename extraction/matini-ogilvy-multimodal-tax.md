# SPIKE extraction — "Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry" (Abed Matini, Ogilvy) — FOR REVIEW

Source transcript: `transcripts/matini-ogilvy-multimodal-tax.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/Akm1sqvWG4A — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact, signals, and knowhows: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-matini-multimodal-tax` | Bypassing the Multimodal Tax: Hybrid RAG, SQL RRF & UI Telemetry (Abed Matini, Ogilvy — AI Engineer World's Fair) | youtube | https://youtu.be/Akm1sqvWG4A |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-abed-matini`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-abed-matini` | Abed Matini (senior backend developer, Ogilvy; builds framework-free local RAG systems) | `AffiliatedWithCompany → co-ogilvy` |

## Companies (1 new)

| slug | name | type | brief |
|---|---|---|---|
| `co-ogilvy` | Ogilvy | media | Global advertising/marketing agency (WPP); appears here as the speaker's employer, not as an AI vendor (captions garble it as "OGOV") |

## Elements (4 new + 2 registry reuse)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-multimodal-tax` | The multimodal tax | concept | context | The hidden cost of dragging raw PDFs/images/decks into a cloud LLM: tokens are burned parsing the document before any question is asked, and the chunking is opaque — you can't see how the model read a table, so quality failures are undebuggable. Bypassed by structure-first local preprocessing: convert to markdown on local CPU, chunk deliberately, then feed only clean text |
| `el-docling` | Docling | framework | data-eng | Open-source document-conversion pipeline used to turn raw enterprise documents (PDF, Word, PowerPoint, images) into markdown on a local CPU before chunking/embedding; the heavy-lifting front end of a structure-first RAG ingestion flow (captions garble it as "Doc Link") |
| `el-hybrid-search` | Hybrid search (BM25 + vector + rank fusion) | concept | context | Retrieval combining BM25 keyword search (exact matches: SKUs, IDs, medication names, product names) with vector/cosine semantic search, fused via reciprocal-rank-style scoring (in plain PostgreSQL here) and optionally reranked; top-k is a product decision — retrieve more for catalogs, fewer for high-liability domains like medical |
| `el-langfuse` | Langfuse | product | harness | Open-source LLM observability/telemetry platform: per-conversation traces, model + latency + retrieved-chunk visibility, session/user tracking, cost estimation for external models; runs fully locally in this stack (captions garble it as "LangChain Fuse"/"length fuse") |

Registry reuse: `el-deterministic-agentic-split` **[registry]** (the talk's "agents" are plain Python functions — deterministic code wherever code can do the job); `co-langfuse` **[registry]** as developer of Langfuse.

Element edges: all four `IdentifiedInArtifact → ia-aie-matini-multimodal-tax`; `el-langfuse` `DevelopedByCompany → co-langfuse` **[registry]**; `el-docling` `EnablesElement → el-hybrid-search` (clean markdown chunks are what get indexed).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-matini-multimodal-tax`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-multimodal-tax-structure-first` | data-eng | Practitioner: uploading raw documents to cloud LLMs taxes you tokens before the first question and hides how the document was chunked (28-page handbook → meaningless chunks like "signature date" → slower answers, more hallucination); converting to markdown locally on CPU via Docling and chunking deliberately eliminates the cost and makes every answer traceable to its chunk | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-multimodal-tax`, `OnElement → el-docling` |
| `sig-smallest-model-vetted-data` | inference | Production finding: with vetted, structured data, the smallest available chat model — Qwen 2.5 0.5B instruct, ~400MB, CPU-only via Ollama — answers an FAQ RAG correctly; bigger models were slower and wordier with no accuracy gain, and the small model hallucinates less ("if it doesn't have the information it simply says so" — paraphrase). Two tiny local models (chat + embedding) are the whole model footprint | `FormsPattern → pat-model-not-bottleneck` **[registry]** | — |
| `sig-guardrails-in-code-not-prompts` | harness | Practitioner moves guardrails out of prompts into deterministic pre-LLM code: intent regex, term dictionaries, and an LLM classifier block prompt injection and out-of-scope queries (e.g. medical questions) **before** anything reaches the model; the system prompt stays a few sentences because "the prompting happens in the code" — and unlike prompts, code guardrails carry a rigid test suite ("this is what I'm blocking and why") | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-deterministic-agentic-split` **[registry]** |
| `sig-framework-free-rag-stack` | harness | A single backend dev shipped a production-shaped hybrid-RAG FAQ chatbot with zero paid components and no agent/RAG framework — Python/FastAPI, React widget, PostgreSQL (vectors + BM25), Docker, Ollama local models, Langfuse telemetry — reproducible with one command in GitHub Codespaces; the RAG stack has commoditized to plain code | `FormsPattern → pat-saaspocalypse` **[registry]** (⚠ weakest edge in file, see Review notes) | `OnElement → el-hybrid-search`, `OnElement → el-langfuse` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-preprocessing-beats-model-size` | In RAG systems the ingestion layer — conversion to structured markdown plus a chunking strategy matched to each document's shape — determines answer quality, cost, and debuggability more than model choice does; vet the data before the LLM and the smallest model suffices, skip it and no model saves you | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-multimodal-tax`, `ReliesOnElement → el-docling` |
| `ins-code-is-the-testable-guardrail` | Guardrails belong in deterministic code upstream of the LLM, where they are cheap (no tokens spent on blocked queries), fast, and testable — a prompt is an instruction the model sometimes ignores; a pre-LLM function is a contract with a test suite. Same logic replaces LLM sub-agents with Python functions for anything code can do (dates, lookups, calculations) | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-deterministic-agentic-split` **[registry]** |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-matini-multimodal-tax`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-structure-first-ingestion` | Structure-first document ingestion for RAG | Convert every raw document (PDF/Word/PPT/image) to markdown locally on CPU (Docling) before anything touches an LLM. Pick the chunking strategy per document shape: heading-based for FAQ/handbook content (best: rewrite the corpus as explicit Q&A so each chunk is one question + answer, cleanly referenceable); paragraph-based for prose; fixed 512-char with 64-char overlap for messy/unstructured data; sentence-group for screenshots/emails run through image-to-text. Clean and split large documents instead of uploading 28 pages raw. Keep chunk→answer references visible so failures are debuggable ("why wasn't the right chunk retrieved?"). Name files meaningfully — filenames surface in citations | `ReferencesElement → el-docling`, `ReferencesElement → el-multimodal-tax` |
| `how-hybrid-retrieval-tuning` | Tune hybrid retrieval per use case | Combine semantic vector search (cosine over embedded chunks) with BM25 keyword search — semantic for meaning-adjacent matches, keyword for exact SKUs/IDs/product/medication names — and fuse the rankings before returning top-k. Size top-k to the domain: more results for product catalogs (or items never surface), fewer for medical/high-liability answers (precision over coverage); add exact-match filters (language, ID, brand). Rerank before display; showing top-20 confuses users | `ReferencesElement → el-hybrid-search` |
| `how-deterministic-functions-and-code-guardrails` | Replace agents with functions; block before the LLM | If a Python function can do it (current date, product info, calculations), don't spend an LLM call — looping 3–4 agents on local models adds 20–30s and users leave; functions are fully controlled, hallucination-free, and unit-testable. Put guardrails before the model: intent regex + term dictionaries + an LLM classifier reject prompt injection and out-of-scope/medical queries pre-LLM with canned escalation responses. Keep the system prompt tiny by encoding do's/don'ts in code. Instrument everything with local telemetry (Langfuse): per-conversation traces, retrieved chunks, latency, model used, cost estimates, session/user tracking — plus a consent gate on the chat widget | `ReferencesElement → el-deterministic-agentic-split` **[registry]**, `ReferencesElement → el-langfuse` |

## Dropped

- Ollama, FastAPI, PostgreSQL/pgvector, React, Docker, GitHub Codespaces as Element nodes — commodity stack components, kept in signal/knowhow prose.
- Qwen 2.5 0.5B and the BGE(?) embedding model as Elements — load-bearing *finding* captured in `sig-smallest-model-vetted-data`; model names stay prose (and "BGM embedding" is an unresolved garble).
- The Coca-Cola premium example, maintenance-screenshot walkthrough, consent-widget demo details — illustrations folded into knowhows.
- "Agent mode vs direct RAG" toggle — captured inside `how-deterministic-functions-and-code-guardrails` and `sig-guardrails-in-code-not-prompts`.

## Review notes

1. **Garbles resolved against official title**: "OGOV" = Ogilvy; "Abid Matini" = Abed Matini; "Doc Link" = Docling; "LangChain Fuse"/"length fuse" = Langfuse; "quant 2.5" = Qwen 2.5. Unresolved: "BGM embedding models" (likely BGE — flagged, kept prose); "how our F in the Python going to work" (unclear, skipped).
2. The title promises **SQL RRF**, but the transcript describes rank-fusing BM25 + vector results without ever naming reciprocal rank fusion; `el-hybrid-search`'s brief says "reciprocal-rank-style scoring" on the strength of the title. Verify before public-facing use.
3. `sig-framework-free-rag-stack → pat-saaspocalypse` is a judgment call (one dev + zero paid components as DIY-over-vendor evidence). It's the weakest edge in the file — drop to pattern-less if the bar isn't met; the signal stands on its own.
4. `el-deterministic-agentic-split` **[registry]** reused for functions-not-agents + code-guardrails; note the registry already flags batch-7 `el-constrain-effects-not-expression` as a merge candidate in this cluster — this talk is further evidence they describe one practice.
5. Docling's developer (IBM) not coined — tool mention doesn't warrant a company node; add `DevelopedByCompany` at reconciliation if IBM enters the registry.
6. `co-ogilvy` typed `media` (advertising agency — closest enum fit).
