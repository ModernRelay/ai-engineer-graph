# SPIKE extraction — "The Rise of CaaS: Context-as-a-Service for Agentic AI" (Omer Primor, Bright Data) — FOR REVIEW

Source transcript: `transcripts/primor-brightdata-context-as-a-service.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/Ot4OPrPH4xY — AI Engineer World's Fair, **Computer Use (CUA) track**, published 2026-08-14.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-14 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the track's data-infrastructure talk. The web is shifting from a source of *data* to a source of *context* for knowledge-work agents; a new vendor category, **CaaS (context-as-a-service)**, structures web data into knowledge graphs agents tap via MCP/CLI/API. A live test (enrich a company across 25 fields, 100 companies, Opus 4.8 loop) compares AI-search vs CaaS vs DIY scraping, landing on the thesis: **rented context decays and repeats cost the same every time; owned context compounds** — there's a tipping-point volume above which building your own beats renting. Caption garbles: "bright air/brighta" → **Bright Data**, "casts/cast/Cass/CAS" → **CaaS**, "Om" → **Omer**, "LLN" → LLM, "zoom info" → **ZoomInfo**, "gtm.ai" → GTM.ai, "unlocker" → **Web Unlocker** (Bright Data product), "SER/SERP" → SERP/search, "stainless data" → **stale data**, "crunchbas" → Crunchbase.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-primor-context-as-a-service` | The Rise of CaaS: Context-as-a-Service for Agentic AI (Omer Primor, Bright Data — AI Engineer World's Fair) | youtube | https://youtu.be/Ot4OPrPH4xY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-omer-primor`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-omer-primor` | Omer Primor (leads product marketing, Bright Data; ~3 years at the company — "front row seats at everything around AI and the web") | `AffiliatedWithCompany → co-bright-data` |

Referenced without coining: Will (CEO of Exa, cited from a prior-day talk covering Exa, Parallel, you.com, Tavily — AI-search companies "indexing the web especially for agents, not even looking at humans anymore").

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-bright-data` | Bright Data | developer | Web-data company: 20,000+ teams and "more than 70% of the world's biggest AI labs" extract web data through it — "well over 50 billion pages/HTMLs every day, 20+ petabytes of video/audio/media." Products named: Web Unlocker, SERP API, Scraper Studio (build a self-healing scraper for any site in <5 min, AI-powered), and a startup program (up to $20k credits) |

Reused **[registry]**, edge-only: `co-amazon` **[b2]** ("last week, Amazon developed their own index and started allowing agents to retrieve web data on AgentCore"), `co-microsoft` **[b2]** ("two weeks before, Microsoft repackaged its search as part of web-BYOQ for agentic development"), `co-google` **[b2]** (the search-dominance-being-shaken framing; SERP baseline), `co-anthropic` **[seed]** (Opus 4.8 as the test harness), `co-parallel` **[b?]** (named among AI-search companies). Referenced without coining: Exa, you.com, Tavily, ZoomInfo (GTM.ai), LinkedIn/Crunchbase (structured entity sources).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-context-as-a-service` | Context-as-a-service (CaaS) | concept | context | The named emerging category: companies that let agents tap web-derived **context** (not just data) via MCP, CLI, or API. They don't only crawl/search/extract/index — they build **knowledge graphs**, dedup entities, and enrich from many sources, behaving "like vertical search engines: a very very good search engine for something very specific." Live across e-commerce, travel, finance, market research, HR, real estate, sales intelligence. Framed as an evolution of DaaS (data-as-a-service, e.g. ZoomInfo's GTM.ai rebrand) but built for agent knowledge work rather than human lookup |
| `el-web-as-context-not-data` | Web as context, not just data | concept | context | The reframing under the category: historically the web was the world's greatest *data* source; with knowledge-work agents it becomes a *context* source — "the data itself is only a step for something bigger: the actions I take, the conclusions I draw, every downstream application." And search only tells part of the story — you can search a sneaker's price this morning but not how it changed over six months, or a company's open roles but not its headcount over time. There is far more context in the web than search extracts |
| `el-data-decay` | Data decay | concept | data-eng | The property that makes context a subscription rather than a snapshot: a Bright Data analysis of how quickly new content stops being relevant — social media far under a day; news, finance, retail mostly irrelevant ~30 days out. "Extracting context from the web is not a snapshot, not a one-time effort, not even monthly — it's an ongoing process." The decay curve is what forces the owned-vs-rented economics later in the talk |
| `el-rented-vs-owned-context` | Rented vs owned context | concept | infra | The talk's central economic argument, from a 100-company × 25-field enrichment test (Opus 4.8 loop, budget-guarded). Coverage: AI-search, one major CaaS, and DIY-scraping-plus-Google all converge well; the two pure CaaS providers underperformed counterintuitively **because "they know what they have about an entity — ask beyond it and the data is never there,"** while a searcher can keep exploring. Cost: search solutions need heavy token burn to *structure* results, CaaS charges its service fee; per-record costs spread widely. The killer is **frequency** — "every repeated query costs the same as the first even if nothing changed" — so renting makes teams cut corners (query weekly not daily, take 10 results not all). Owned context (build the scrapers, merge into entities, store) is upfront cost then near-free retrieval — "owned context compounds while rented decays" — with a computed **tipping point** (~15,000 entities/queries in the test, use-case-dependent) above which building beats renting |
| `el-web-context-engineering` | Web context engineering | concept | context | The discipline the talk proposes: optimizing *how* an agent sources web context per task and per team, mixing AI-search (ad hoc, always-changing needs) and CaaS/owned pipelines (persistent, consistent, escalating needs) rather than throwing AI-search at everything. "As an AI engineer I need to serve different teams with different needs — it's tempting to throw AI search at all of them, but maybe that's not optimal." Frequency is "the cost killer," and the tipping point "is much lower than you think" |

Element edges: all five `IdentifiedInArtifact → ia-aie-primor-context-as-a-service`.
`el-context-as-a-service` `DevelopedByCompany → co-bright-data`, `UsesElement → el-web-as-context-not-data`;
`el-web-as-context-not-data` `EnablesElement → el-context-as-a-service`;
`el-data-decay` `EnablesElement → el-rented-vs-owned-context`;
`el-rented-vs-owned-context` `UsesElement → el-web-context-engineering`;
`el-context-as-a-service` `ExemplifiesPattern → pat-agent-memory-layer` **[registry]** — *see review note 1*.

Reused elements (no new nodes): `el-mcp` **[seed]** (CaaS access surface), `el-knowledge-graph-control-plane` **[b11]** adjacency (CaaS providers build knowledge graphs), `el-company-brain` **[b3, Tan]** (the owned-context-compounds argument is the supply-side of Tan's company-brain thesis) — edge left to review, note 4.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-primor-context-as-a-service`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-bright-data`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-caas-category-emerging` | context | A web-data vendor names a new category — **context-as-a-service** — of companies structuring web data into knowledge graphs (dedup, entity enrichment, multi-source merge) that agents tap via MCP/CLI/API, "behaving like vertical search engines." Live across finance, market research, retail, e-commerce, GTM, sales intelligence, and pursued by incumbents too (ZoomInfo's GTM.ai). Framed as the successor to data-as-a-service, built for agent knowledge work rather than human lookup. The supply side of the agent-memory/context thesis, from the vendor layer | `FormsPattern → pat-agent-memory-layer` **[registry]** | `OnElement → el-context-as-a-service`, `el-web-as-context-not-data` |
| `sig-search-index-land-grab` | infra | The competitive signal: three years ago web search was "complete and total Google dominance"; now search runs inside chatbots (blurring human vs agent — "the same LLMs have the same access through API for the bot"), and a breed of AI-search companies (Exa, Parallel, you.com, Tavily) index the web *for agents, not humans*. Then the incumbents moved — "last week Amazon developed their own index and started letting agents retrieve web data on AgentCore; two weeks before, Microsoft repackaged its search as web-BYOQ for agentic development." Google's search synonymity "is very much shaking" — a live restructuring of the web's retrieval layer around agents | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-web-as-context-not-data`; `RelevantCompany → co-amazon`, `co-microsoft`, `co-google` **[registry]** |
| `sig-owned-context-compounds` | infra | The economic thesis, from a 100-company/25-field enrichment test: **rented context decays and every repeated query costs the same even if nothing changed**, so renting forces corner-cutting (query less often, take fewer results, skip fields), leaving value unextracted; **owned context is upfront cost then near-free retrieval** and compounds as the web keeps changing. A computed **tipping point** (~15k entities in the test, use-case-dependent) above which building your own beats renting — driven by *frequency*, "the cost killer," which "is much lower than you think." A build-vs-buy inflection for agent context infrastructure | `FormsPattern → pat-agent-memory-layer` **[registry]** | `OnElement → el-rented-vs-owned-context`, `el-data-decay` |
| `sig-caas-limited-to-what-it-holds` | context | The counterintuitive test result: the two pure CaaS providers **underperformed** on coverage — expected to dominate entity enrichment, they were limited because "they know what they have about an entity; ask a question beyond that and the data is never there," whereas a searcher keeps exploring. A structural limit of pre-indexed context products: they answer within their index and go silent outside it, which for open-ended knowledge work is a real ceiling. A vendor publicly naming its own category's limitation | `ContradictsPattern → pat-agent-memory-layer` **[registry]** | `OnElement → el-rented-vs-owned-context`, `el-context-as-a-service` |
| `sig-web-context-needs-engineering` | context | The discipline claim: sourcing web context is itself a context-engineering problem — mix AI-search (ad hoc, changing needs) with CaaS or owned pipelines (persistent, consistent, escalating needs) per task and per team, rather than defaulting to AI-search everywhere. Data decay (social <1 day; news/finance/retail ~30 days) makes it an ongoing process, and frequency dominates cost, so the sourcing choice is an engineering decision with real cost-efficiency stakes. The knowledge-work counterpart to prompt/context engineering | `FormsPattern → pat-context-graphs` **[registry]** | `OnElement → el-web-context-engineering`, `el-data-decay` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-context-supply-mirrors-memory-demand` | The memory-layer thesis coined from the product side (b19) has a supply side, and this is it: agents that accumulate context need somewhere to source it, and a vendor category — CaaS — is forming to structure the web into agent-consumable knowledge graphs. The two are the same market from opposite ends: memory products own the *retention* loop, CaaS/owned pipelines own the *acquisition* loop, and the data-decay curve is why acquisition is a subscription rather than a purchase. Reading them together is what makes the build-vs-buy tipping point legible | `HighlightsPattern → pat-agent-memory-layer` **[registry]** | `ReliesOnElement → el-context-as-a-service`, `el-rented-vs-owned-context` |
| `ins-frequency-is-the-hidden-cost-axis` | The talk's durable lesson is that context economics are governed by *frequency*, not volume: a rented query costs the same on the thousandth ask as the first even when the answer is unchanged, so any workload that revisits the same entities repeatedly (due diligence, monitoring, market research) crosses a build-beats-rent tipping point far sooner than intuition suggests. That reframes agent-context procurement as an amortization decision, and it generalizes past web data to any external context an agent queries on a cadence — the same owned-vs-rented calculus the memory-compute-budget talks reached (Khemani, b19) | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-rented-vs-owned-context`, `el-data-decay` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-primor-context-as-a-service`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-source-agent-web-context` | Source web context by frequency, not by default | Treat sourcing web context as an engineering decision, not a reflex to throw AI-search at everything — match the tool to the need: AI-search and CaaS for ad hoc, always-changing questions; owned pipelines for persistent, consistent, escalating needs across the org; remember the web **decays** (social under a day; news, finance, retail ~30 days), so context is an ongoing subscription, not a snapshot; know that **rented context costs the same on every repeat even when nothing changed**, which quietly pushes teams to cut corners (query weekly not daily, take 10 results not all, skip fields) and leave value unextracted; watch for the structural limit of pre-indexed CaaS — it answers within its index and goes silent outside it, so a searcher that keeps exploring can out-cover it on open-ended questions; compute your **tipping point** — the volume/frequency above which building your own scrapers and merging into owned entities beats renting (it is usually lower than you think), noting owned context is upfront cost then near-free retrieval that compounds; and where sources are already structured as entities (LinkedIn, Crunchbase) the ontology is partly built for you | `ReferencesElement → el-rented-vs-owned-context`, `el-context-as-a-service`, `el-data-decay`, `el-web-context-engineering` |

## Dropped

- **The startup-program plug** (up to $20k credits) and Scraper Studio demo specifics — logistics/product; Scraper Studio's self-healing detail folded into `co-bright-data`.
- **The test's per-provider cost breakdown** ("native obscenely expensive"; the unnamed most-expensive CaaS) — the shape is in `el-rented-vs-owned-context`; the anonymized vendor rankings carry no node.
- **The "won't name and shame" asides** — colour.

## Review notes

1. **⚑ The supply-side counterpart to `pat-agent-memory-layer` — and it arrives already contested.** Three signals home on the pattern: `sig-caas-category-emerging` and `sig-owned-context-compounds` support it (a vendor category forming to feed agent context; owned context compounds), while `sig-caas-limited-to-what-it-holds` **contradicts** it (pre-indexed context products answer within their index and go silent outside it). That the same talk supplies both a support and a counter mirrors the healthy-from-birth shape the pattern was coined with (b19). The `el-context-as-a-service` `ExemplifiesPattern` edge is emitted; recommend the brief note that the memory layer has an acquisition side (CaaS) and a retention side (memory products).
2. **Fifth-plus corroboration of the "search layer restructuring around agents" thread.** Amazon (AgentCore index), Microsoft (web-BYOQ), the AI-search cohort (Exa/Parallel/you.com/Tavily) — a live land-grab, homed on `pat-model-not-bottleneck` (value moving to the retrieval layer around the model). Convergent with the Oxylabs and Batra talks in this same batch on the infrastructure-around-the-model theme.
3. **⚠ Verify before seeding:** Bright Data's scale figures (20k teams, "70% of biggest AI labs," 50B pages/day, 20PB media); the 100-company/25-field/Opus-4.8 test setup and its ~15k tipping point; the data-decay curve (social <1 day, news/finance/retail ~30 days); the Amazon-AgentCore and Microsoft-web-BYOQ launches ("last week" / "two weeks before"). All vendor-stated.
4. **Proposed cross-file edge, left to review:** `el-rented-vs-owned-context` → `el-company-brain` **[b3, Tan]** — Primor's owned-context-compounds argument is the data-supply mechanics under Tan's "your company is a library" company-brain thesis. Not emitted; both are concepts and the link is thematic.
