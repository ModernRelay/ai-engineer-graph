# SPIKE extraction — "How we taught agents to use good retrieval" (Hanna Lichtenberg, Mixedbread AI) — FOR REVIEW

Source transcript: `transcripts/lichtenberg-mixedbread-agent-retrieval.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/1IdzkRVmWAA — AI Engineer World's Fair, published 2026-07-07.
`stagingTimestamp` for the artifact and all signals: 2026-07-07 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

Context: two speakers — "Hannah" (Hanna Lichtenberg, AI engineer leading agentic search at Mixedbread) and "Amir", introduced as Mixedbread's co-founder (identified as Aamir Shakir from public record, ⚠ see Review notes 1). Internal framing: "closing the Oracle gap with knowledge agents".

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-lichtenberg-agent-retrieval` | How we taught agents to use good retrieval (Hanna Lichtenberg & Aamir Shakir, Mixedbread AI — AI Engineer World's Fair) | youtube | https://youtu.be/1IdzkRVmWAA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-hanna-lichtenberg`, `ContributedByExpert → exp-aamir-shakir`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-hanna-lichtenberg` | Hanna Lichtenberg (AI engineer, leads agentic search at Mixedbread) | `AffiliatedWithCompany → co-mixedbread` |
| `exp-aamir-shakir` | Aamir Shakir (co-founder, Mixedbread) ⚠ transcript says only "Amir, co-founder of Mixedbread"; surname from public record — verify | `AffiliatedWithCompany → co-mixedbread` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-mixedbread` | Mixedbread AI | developer | search/retrieval company (embeddings, rerankers, and now a trained agentic-search product); captions render it "Mix bread" throughout |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-knowledge-gap` | The knowledge gap (Oracle gap) | concept | context | Mixedbread's name for the widening gap between exponentially improving LLM reasoning and barely-improving retrieval (~20 years of slow search progress); operationalized as Oracle performance (model score when handed the right documents alongside the question) minus actual performance with real search tools over a noisy corpus — positioning knowledge *access*, not reasoning, as the binding constraint for agents beyond code (legal, finance) |
| `el-mixedbread-agentic-search` | Mixedbread agentic search | product | context | Mixedbread's trained search agent (beta in production; trained version unreleased at talk time): four-tool harness (overview search — up to 50 chunks as summaries only; semantic search — full payload of top-10; metadata-facet chunk filter; grep for exact keyword match), ≤4 search rounds with parallel searches per round, upfront corpus preview (initial semantic results + metadata hints), chunk dedup across rounds, final output = evidence ranking; the trained agent is a deliberately small LLM — SFT from a larger teacher, then on-policy RL on a composite search reward; production beta tops Snowflake's MatchQA at 93.4% accuracy (as the search tool under Gemini 3.5 Flash) at markedly lower cost than comparable setups |
| `el-browsecomp-plus` | BrowseComp Plus | technology | context | Fixed-corpus variant of OpenAI's BrowseComp deep-search benchmark: complex browsing questions answered over a fixed 100k-document corpus instead of the open web, which makes Oracle-vs-tools comparisons possible; Oracle ceiling ~93% for frontier models per the talk |

Element edges: all three `IdentifiedInArtifact → ia-aie-lichtenberg-agent-retrieval`; `el-mixedbread-agentic-search` `DevelopedByCompany → co-mixedbread`; `el-knowledge-gap` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**; `el-mixedbread-agentic-search` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

Registry element reuse (no new node, edge only): `el-codex` **[registry]** `IdentifiedInArtifact → ia-aie-lichtenberg-agent-retrieval` — Codex-with-default-tools is the talk's baseline for how far agent search falls below Oracle.

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-lichtenberg-agent-retrieval`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-mixedbread`.

| slug | domain | name / brief | FormsPattern |
|---|---|---|---|
| `sig-knowledge-gap-oracle-benchmarks` | context | On BrowseComp Plus (100k-doc corpus) and OfficeQA Pro (Databricks; ~100 years of US treasury documents), frontier models score near the Oracle ceiling (93% / 64%) when handed the right documents, but Codex with default tools drops sharply (captions: "nine points" / "eight points" — ambiguous whether drop-*by* or drop-*to*, ⚠ Review notes 3); swapping in Mixedbread search (late-interaction retrieval as a plain search tool) recovers to within ~3 points of Oracle on BrowseComp Plus and nearly closes OfficeQA Pro — "the bottleneck here is not the reasoning, it's access to the right knowledge" | `FormsPattern → pat-model-not-bottleneck` **[registry]** |
| `sig-agents-write-caveman-queries` | context | Agents issue gibberish keyword-soup search queries (real benchmark example: "senator woman questions billionaires not a company then okay thank you staff will check hearing") for three trained-in reasons: coding-agent training optimizes for grep/regex codebase exploration, web-tool training mimics human keyword-query patterns, and benchmark bias — BEIR/NanoBEIR-style "caveman" entity queries structurally favor BM25 — so models guess keyword overlap and cannot drive powerful semantic search unaided | `FormsPattern → pat-harness-over-model` **[registry]** |
| `sig-small-model-rl-search-wins` | training | Mixedbread trained a *small* LLM (for speed/cost) into a search agent — SFT from a larger teacher, then on-policy RL on a composite reward — and reports NDCG@10 of 0.40 on a long-rambling-query congressional benchmark (⚠ garbled name, Review notes 2) vs 0.18 for the best agent in that benchmark's paper (a GPT multi-hop agent); the production beta is top-1 on Snowflake MatchQA (93.4% acc with Gemini 3.5 Flash as the reasoning model) at far lower cost than comparable LLM search agents | `FormsPattern → pat-harness-over-model` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-oracle-gap-is-tooling-work` | Oracle-vs-actual deltas prove model capability is already sufficient for deep knowledge work — the recoverable gap lives in the search tool and harness (tool separation by intent, context budgeting via summaries/dedup, query framing), so closing it is retrieval engineering, not bigger models | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-knowledge-gap` |
| `ins-query-habits-trained-in` | An agent's search behavior is an artifact of its training distribution (code-grep + human-web + BM25-shaped benchmarks), so you cannot fully prompt it away — you reframe the task so the old pattern can't fire ("write one concise sentence describing what you want to find", never "write a search query") and ultimately retrain with rewards that grade query quality itself | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-mixedbread-agentic-search` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-lichtenberg-agent-retrieval`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-agent-search-tool-suite` | Give search agents intent-separated tools, not one search box | Split retrieval into: overview search (wide semantic, up to ~50 chunks, summaries only — corpus orientation without context blowup), semantic search (full payload, top ~10), metadata-facet filter, and grep (exact keyword match only); cap search rounds (~4) but allow parallel searches within a round; seed the first turn with initial semantic results + available metadata facets so planning starts informed; dedupe chunks across rounds; end with an explicit evidence ranking, not prose | `ReferencesElement → el-mixedbread-agentic-search` |
| `how-elicit-semantic-queries` | Trick the model out of keyword-soup queries | Force goal framing (articulate what evidence is needed before writing anything); never instruct "write a search query" — instruct "write one concise sentence describing what you want to find", so the trained BM25 reflex can't fire; show a few good example queries and how to split an input into separate aspects (≤4 sub-queries); reserve grep for genuinely exact-match needs | `ReferencesElement → el-mixedbread-agentic-search` |
| `how-composite-search-reward` | Train small search agents with a two-part reward | SFT the small model from a larger teacher first, then on-policy RL with: retrieval reward = ranking metric (NDCG on the final list) + LLM retrieval judge over rubrics (results relevant to query? all chunks relevant? ranking plausible?), and trajectory reward = LLM judge over the *process* (is each query a natural sentence? is exploration sufficient — neither too much nor too little? is the run efficient?) — rewarding the search behavior, not just the end answer | `ReferencesElement → el-mixedbread-agentic-search` |

## Dropped

- OfficeQA Pro as an Element — load-bearing numbers but the benchmark name is likely garbled (see Review notes 2); kept in signal prose with flags rather than coined under a possibly-wrong name.
- BEIR / NanoBEIR, BM25, NDCG, GPT-3.5→GPT-5.5 reasoning-curve framing — named in signal/knowhow prose; standard-technique altitude, not coined.
- Benchmark creators OpenAI (BrowseComp), Databricks (OfficeQA Pro), Snowflake (MatchQA) — prose credits only; no `RelevantCompany` edges (`co-openai` **[registry]** not linked).
- Closing hiring pitch — color.

## Review notes

1. **Second speaker ⚠**: transcript has only "I'm Amir, co-founder of Mix bread"; the official listing credits Hanna Lichtenberg alone. Coined `exp-aamir-shakir` because Mixedbread's co-founder by that name is well documented publicly (batch-6 `exp-nader-khalil` precedent: coin with verify-flag). If the reviewer prefers the batch-5 "Maria" precedent (don't coin without surname in-source), drop the expert and its two edges.
2. **Garbled benchmark names**: "BroSque Plus" → BrowseComp Plus (resolved from context: "BrowseComp was created by OpenAI... Plus is a version with a fixed-size corpus"). "Office QA Pro" — as-captioned, attributed to Databricks, corpus described as ~100 years of US treasury documents; plausibly a garble, unresolved. "Oblique Congress benchmark" (long rambling congressional-hearing queries) — clearly garbled, unresolved; NDCG numbers kept with the flag. "snowflakes match QA" → Snowflake MatchQA (partially resolved; verify). "Gemini 3.5 flash" as-captioned. "latent interaction" → almost certainly **late interaction** (ColBERT-style retrieval) — resolved in prose with flag.
3. **Score ambiguity ⚠**: "For BrowseComp it's nine points and for Office QA Pro it's eight points" — could mean Codex-default *drops by* 9/8 points from Oracle, or *drops to* 9/8 points. The surrounding rhetoric ("sharp drop", "performance drops sharply") suggests drop-*to*; the parallel later phrasing ("the difference between the Oracle and GPT-5 with Mixedbread is just three points") suggests drop-*by*. Left ambiguous in the signal; verify against the talk's slides before seeding numbers.
4. The recovery numbers name "GPT-5 with Mixedbread" while the baseline is "Codex with its default tools" — model and harness both differ from baseline to treatment; the signal reports it as the talk frames it (search-tool swap) but the confound is worth noting.
5. Both training-side signals park on `pat-harness-over-model` even though the fix spans harness *and* training — the talk's own causal story is that tool design + task framing + trained behavior around an unchanged reasoning model closes the gap. Weak added evidence for the `pat-benchmark-trust-crisis` candidate (benchmark bias actively mis-training agent query behavior) — noted only, no edge.
