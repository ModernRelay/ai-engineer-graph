# SPIKE extraction — "We Cut 94% of AI Coding Tokens With a Local Code Index" (Rajkumar Sakthivel, Tesco) — FOR REVIEW

Source transcript: `transcripts/sakthivel-tesco-local-code-index.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/dRmWYHuIJxM — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact and all signals: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the shared registry — edges link to them, no new node defined here.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-sakthivel-local-code-index` | We Cut 94% of AI Coding Tokens With a Local Code Index (Rajkumar Sakthivel, Tesco — AI Engineer World's Fair) | youtube | https://youtu.be/dRmWYHuIJxM |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-rajkumar-sakthivel`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-rajkumar-sakthivel` | Rajkumar Sakthivel ("Raj"; engineer at Tesco; built the local code index as a personal open-source project with collaborator "Foss") | `AffiliatedWithCompany → co-tesco` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-tesco` | Tesco | — | UK grocery/retail enterprise; appears only as the speaker's employer — the indexing project is personal OSS, so no `DevelopedByCompany` edge from the element and no `RelevantCompany` on signals. Type left unset: no enum value fits a retailer (same gap daga flagged for Tesla) |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-local-code-index` | Local code index | concept | context | A local search layer between the codebase and AI coding tools, replacing whole-file context: semantic chunking into functions/classes/methods (not random windows); dual retrieval — meaning-based plus exact-word search fused (each alone misses ~1 in 4 relevant results, together ~1 in 10); result compression to signatures + descriptions (50-line function → 5 lines); call-graph links so one hit pulls connected code; sub-millisecond weighted relevance gating that drops low-scoring results (no bad context); runs entirely on-machine, with one shared index and persistent memory serving all coding tools (Claude Code, Cursor, Copilot, Codex) |

Element edges: `el-local-code-index` `IdentifiedInArtifact → ia-aie-sakthivel-local-code-index`; `el-local-code-index` `ExemplifiesPattern → pat-context-graphs` **[registry]** (structured, shared, persistent context infrastructure instead of raw text dumps).

## Signals (3 new)

All: domain `context`, `SpottedInArtifact → ia-aie-sakthivel-local-code-index`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-input-90-output-10` | Practitioner cost autopsy after a month-over-month AI-coding bill spike with unchanged usage: ~90% of spend was input tokens — a typical query shipped 45K tokens of context of which only ~5K mattered. Cutting output 75% (compression) saved only ~8% total, while cutting input 94% saved ~61%; prompt wording and model settings couldn't touch it because the context cost had already been paid before the model read the prompt | `FormsPattern → pat-model-not-bottleneck` **[registry]** | — |
| `sig-94pct-context-cut-benchmark` | Public benchmark of the local index on FastAPI (53 files, 20 real developer questions): 83K → 4.9K tokens per question (94% cut; 523 tokens with extra compression) while still finding the right code ~90% of the time. Honestly bounded by the speaker: the baseline is worst-case full-file reading (tools like Claude Code already do better, so real savings are lower), and recall collapsed to near zero on a 396-file mixed-responsibility codebase — single-purpose files work, tangled ones don't | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-local-code-index` |
| `sig-coding-tools-share-nothing` | Every AI coding tool re-learns the same codebase from scratch and shares nothing across tools or sessions (Claude Code for hard problems, Cursor for quick edits, Copilot for completions — "you explain the same codebase to three different tools", paraphrase). One shared local index + persistent memory fixed it: explain once, every tool remembers. Measured on a real project: 247 queries, 12.4M tokens saved (~$186), 84% of savings from the search layer vs compression — tracked per query as would-have-sent vs sent | `FormsPattern → pat-context-graphs` **[registry]** | `OnElement → el-local-code-index` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-fix-the-input` | Token-cost optimization has a 90/10 structure: output-side tricks (short answers, max-tokens settings) cap out at single-digit total savings; the real lever is input-side context selection. "We argue about which model is best, Opus or Sonnet — but the model may be 30% of the cost; the other 70% is what you feed it. Fix the input; the model choice matters less than you think" (paraphrase) | `HighlightsPattern → pat-model-not-bottleneck` | `ReliesOnElement → el-local-code-index` |
| `ins-simple-scoring-beats-llm-judging` | For relevance gating, a 0.4 ms weighted formula (50% semantic score + 30% keyword score + 20% code recency, with an adaptive threshold) beat both LLM-as-judge (2–3 s per query, too slow) and fixed cutoffs (punish short queries); bad context is worse than no context because it produces confident wrong answers. "Simple formula beats the complex model most of the time" (paraphrase) — same spirit at every layer: small DB over big infrastructure, two plain searches over one fancy one, local over cloud, small fast model for indexing (re-index <1 s) | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-local-code-index` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-sakthivel-local-code-index`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-local-code-index` | Build a local retrieval layer for AI coding tools | Chunk by code structure (functions/classes/methods), never arbitrary windows; run meaning-based and exact-word search together and fuse results — they patch each other's blind spots (semantic misses exact names; lexical misses synonyms like login vs sign-in); compress hits to name + description before sending; index call-graph edges so a hit brings its connected code; score-gate every result and send nothing below threshold — no bad context beats more context; keep everything local (privacy + speed) and prefer a small fast model for indexing — speed over perfection; share one index and persistent memory across all coding tools; instrument per-query would-have-sent vs sent × model price so savings are measured, not estimated | `ReferencesElement → el-local-code-index` |

## Dropped

- "CCE" (the tool's command, shown on screen) as a product Element — expansion and spelling unverifiable from captions; the concept is coined instead (`el-local-code-index`) and the tool name kept in prose with a flag.
- `el-claude-code` / `el-codex` **[registry]**, `co-cursor` / `co-github` (Copilot) **[registry]** — the tools are named as context consumers the index serves, not analyzed; prose only, no edges.
- Failed approaches inventory (shorter prompts, max-token/temperature settings, output compression alone) — folded into `sig-input-90-output-10` and `ins-fix-the-input`.
- The ten-pizzas analogy and Opus-vs-Sonnet debate — rhetoric.

## Review notes

1. **Affiliation nuance:** the conference listing credits Tesco, but the transcript frames everything as a personal project ("me and my friend Foss", "our AI bill", free open source) and never mentions Tesco. Coined `co-tesco` for the `AffiliatedWithCompany` edge only; deliberately NO `DevelopedByCompany → co-tesco` from `el-local-code-index` and no `RelevantCompany → co-tesco` on signals.
2. **`co-tesco` type left unset** — the enum (bigtech/developer/investor/research/hardware/media) has no fit for a grocery retailer; same gap the daga file flagged for Tesla.
3. **Caption garbles:** "Cloud code" = Claude Code, "code X" = Codex, "co-pilot" = Copilot. Collaborator "Foss" — first name/handle only, possibly itself a garble — not coined (precedent: unnamed "Maria", batch 5). Tool name "CCE" unresolved (command on screen; expansion unknown) — verify against the video before public-facing use. "$186" is read from "nearly 186 not spent"; currency assumed USD.
4. The 94% headline is explicitly caveated by the speaker (worst-case full-file baseline; recall collapse on large mixed codebases) — caveats preserved inside `sig-94pct-context-cut-benchmark` so downstream use doesn't overquote it.
5. No new pattern coined; nothing at candidate threshold. The shared-index/memory claim is the corpus's cleanest coding-tools instance of `pat-context-graphs`; the 90/10 cost split is a strong quantitative `pat-model-not-bottleneck` data point.
