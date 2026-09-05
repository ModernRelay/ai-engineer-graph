# SPIKE extraction — "Agentic Sites: Building Hyper Personalized Websites" (Carlos Sanchez, Adobe) — FOR REVIEW

Source transcript: `transcripts/sanchez-adobe-agentic-sites.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/jebp4V0vh30 — AI Engineer World's Fair, published 2026-08-29.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-29 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a principal scientist on Adobe Experience Manager demos **agentic sites** — pages assembled per user in real time from browsing intent (pages visited, dwell time, queries), personalizing *blocks* (hero, products, feeds, navigation, CTAs) rather than generating whole sites, grounded by RAG over the site itself so brand guidelines hold. The engineering point is **speed as the selection criterion**: per-site continuous evaluation of models and providers with Promptfoo on accuracy *and* latency; Gemma 4 on Cerebras assembles a page in ~1 s at ~2,300 tokens/s where the next option takes 4.6 s — "you don't need a huge LLM for this." "Audience of one": the marketing dream of per-person personalization, extended to a voice query rendering a personalized page on a TV. Caption garbles: "Agility Sites" → **Agentic Sites**, "AMH delivery" → **AEM (Adobe Experience Manager) edge delivery**, "rack" → **RAG**, "Prompt Full" → **Promptfoo**, "164 seconds" → **1.64 seconds** (total page time), "Arco" → the demo coffee site, "OfOneLabs" kept (⚠ name uncertain), "nano banana light" → a fast Google image model (⚠ name uncertain).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-sanchez-adobe-agentic-sites` | Agentic Sites: Building Hyper Personalized Websites (Carlos Sanchez, Adobe — AI Engineer World's Fair) | youtube | https://youtu.be/jebp4V0vh30 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-carlos-sanchez`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-carlos-sanchez` | Carlos Sanchez (Principal Scientist, Adobe Experience Manager; open-source foundations contributor) | `AffiliatedWithCompany → co-adobe` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-adobe` | Adobe | bigtech | Adobe Experience Manager (content management running "a lot of website properties for big brands") is building agentic sites on its edge-delivery stack; backend on Google and Cloudflare; inference via Cerebras (also tried Bedrock) |

Reused **[registry]**, edge-only: `co-cerebras` (Gemma 4 at ~2,300 tokens/s — the reason the demo is on Cerebras), `co-google` (Gemma 4; backend hosting; a fast image model for on-the-fly media), `co-cloudflare` (backend hosting), `co-aws` (Bedrock evaluated). Referenced, not coined: Google TV (the voice-to-page demo target).

## Elements (6 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agentic-sites` | Agentic sites | product | context | Sites that read the browsing user's intent and personalize pages in real time to drive engagement or conversion. Not whole-site generation — marketers "have very strict brand guidelines, you don't want hallucinations" — but per-**block** personalization (hero, product cards, blog feeds, navigation, calls to action, comparisons), with the whole site as a RAG corpus so every generation is grounded. Modes: instant persona adaptation, query-generated result pages, "for you" recommendation pages built from accumulated signals (pre-generatable and pre-fetchable, with cost implications per generation). Marketers define the strategy in natural language and close the loop with analytics |
| `el-audience-of-one` | Audience of one | concept | | The marketing dream of personalizing for each individual, now operational: users bucketed into intent groups (exploring / buying / informing — marketers decide the groups), pages assembled per query ("a coffee machine for camping" → rewritten copy, camping-suitable products, tips). Beyond the browser: a voice query to an assistant rendering a fully personalized page on a Google TV — "no phone, no computer, just my voice." "Is the web still the future? Nobody knows — but we can do this with generative sites" |
| `el-site-dependent-model-eval` | Site-dependent, speed-first model evaluation | ops | inference | Model/provider choice "is very dependent on the site" (size, vertical, commerce type), so evaluation runs continuously per site: a prompt set (15 for the demo site) across many models and providers, scored on **accuracy and speed** — a page must generate in 1–2 s because faster sites convert better. Result: Gemma 4 on Cerebras averages 1.1 s per page; the next option 4.6 s. "Some don't need to be perfect — they're good enough if they're fast enough," and "you don't need a huge LLM — you're generating text and deciding where to put blocks" |
| `el-promptfoo` | Promptfoo | technology | harness | The open-source evaluation tool used for the per-site model matrix: run prompts against multiple models and providers (local models and any OpenAI-compatible endpoint), compare accuracy and latency continuously; complemented by a manual in-site model/temperature/token switcher for customer demos |
| `el-edge-blocks-plus-llm-backend` | Edge-delivered blocks with an LLM backend | technology | infra | Dynamic front end composed of blocks on AEM edge delivery, updated in real time; browser-side signals (pages visited, dwell time, queries, intent bucket) recorded and fed to the model; a backend (Google/Cloudflare) that calls the LLM with the site RAG (vector database + inference) and returns the assembled page; static content still served at the edge. Demo timing: ~1.6 s total round trip, ~1 s LLM time, 2,200–2,300 tokens/s |
| `el-ofonelabs-site-generator` | Agentic site from any URL in under an hour | product | | An internal tool that turns any site into an agentic site "in less than an hour" for customer demos — the AI Engineer site became a search box with AI-generated suggestions, query-focused pages ("Europe AI conferences") and side-by-side comparison pages assembled on the fly |

Element edges: all six `IdentifiedInArtifact → ia-aie-sanchez-adobe-agentic-sites`.
`el-agentic-sites` `DevelopedByCompany → co-adobe`;
`el-ofonelabs-site-generator` `DevelopedByCompany → co-adobe`;
`el-agentic-sites` `UsesElement → el-edge-blocks-plus-llm-backend`, `el-site-dependent-model-eval`, `el-audience-of-one`;
`el-site-dependent-model-eval` `UsesElement → el-promptfoo`, `el-gemma-open-models` **[registry]**;
`el-ofonelabs-site-generator` `UsesElement → el-agentic-sites`;
`el-site-dependent-model-eval` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**;
`el-agentic-sites` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

Reused elements (no new nodes): `el-gemma-open-models` **[registry]** (Gemma 4, "announced last week"), `el-model-routing` **[registry]** (per-site provider selection as a routing decision).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-sanchez-adobe-agentic-sites`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-adobe`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-pages-assembled-per-user-in-one-second` | inference | Adobe's content-management product assembling a personalized page per query in ~1 s of LLM time (~1.6 s round trip) at 2,200–2,300 tokens/s — Gemma 4 on Cerebras — "something we only dreamed about before." Blocks, copy, products and navigation re-composed for one user's intent; the "for you" page pre-generated from accumulated browsing signals. Enterprise web personalization moving from pre-authored variants to on-demand generation | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-agentic-sites`, `el-edge-blocks-plus-llm-backend` |
| `sig-speed-not-size-selects-the-model` | inference | The selection criterion is latency at acceptable accuracy: a continuous per-site Promptfoo matrix over models and providers found 1.1 s (Gemma 4 / Cerebras) versus 4.6 s for the runner-up, and "you don't need a huge LLM" to place blocks and write copy. Public benchmarks don't settle it — "this is very dependent on the site," so each site re-runs its own evaluation. A small fast model plus fast inference beats a big one for a latency-bound product | `FormsPattern → pat-model-not-bottleneck` **[registry]**; `FormsPattern → pat-benchmark-trust-crisis` **[registry]** | `OnElement → el-site-dependent-model-eval`, `el-promptfoo`, `el-gemma-open-models` **[registry]** |
| `sig-personalize-blocks-not-the-site` | context | The constraint that makes generation shippable to brands: never generate the whole site; personalize blocks inside brand guidelines, ground every generation in a RAG over the site's own content, let marketers define the strategy in natural language and decide the intent groups, and close the loop with analytics. Generation is boxed by the harness — corpus, blocks, groups, brand — rather than trusted to the model | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-agentic-sites`, `el-audience-of-one` |
| `sig-audience-of-one-beyond-the-browser` | | The marketer's "audience of one" reaches past the web page: a voice query to an assistant renders a personalized page on a TV; any site can become an agentic site in under an hour; "is the web still the future — nobody knows." Web surfaces dissolving into per-person, per-query generated pages — a data point for the corpus's uncoined liquid-software framing, held pattern-less | | `OnElement → el-audience-of-one`, `el-ofonelabs-site-generator` |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-personalization-became-a-latency-problem` | The durable claim is where the difficulty moved: once a small open model can write on-brand copy and place blocks, per-user page generation is gated by inference latency (the 1–2 s conversion budget) and by grounding (RAG over the site, blocks not sites), not by model quality — so the engineering is continuous per-site evaluation of provider speed and a harness that boxes the generation. Personalization, the oldest unsolved promise in marketing, becomes an infrastructure and evaluation problem | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-site-dependent-model-eval`, `el-agentic-sites`, `el-edge-blocks-plus-llm-backend` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-sanchez-adobe-agentic-sites`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-an-agentic-site` | Per-user pages: blocks, grounding, and a speed-first model matrix | Personalize **blocks** (hero, products, feeds, navigation, CTAs, comparisons), never the whole site, so brand guidelines hold; build a RAG over the site's own content and ground every generation in it; record browsing signals (pages, dwell time, queries) and bucket users into marketer-defined **intent groups**; let marketers state the strategy in natural language and feed analytics back into it; set a hard **1–2 s page budget** and evaluate models *and providers* continuously per site (Promptfoo) on accuracy and latency — expect the answer to differ by site, and prefer a small fast model on fast inference over a large one; pre-generate and pre-fetch "for you" pages from accumulated signals, watching the cost of repeated generations; serve static content and blocks at the edge with the LLM backend behind them; and keep a manual model/temperature switcher for demos and debugging | `ReferencesElement → el-agentic-sites`, `el-site-dependent-model-eval`, `el-promptfoo`, `el-edge-blocks-plus-llm-backend`, `el-audience-of-one` |

## Dropped

- **The coffee-site demo walkthrough** (product browsing, debug panel, camping query) — folded into `el-agentic-sites` and `el-audience-of-one`.
- **Image generation on the fly** — mentioned as possible with a fast image model but "depends on whether it's on brand"; not coined.

## Review notes

1. **A product-side `pat-model-not-bottleneck` point with numbers**: 1.1 s vs 4.6 s per page, small open model on fast inference, per-site evaluation. Pairs with the corpus's `el-model-routing` (speed-first routing) — recommend widening that element's brief.
2. **`sig-audience-of-one-beyond-the-browser` is held pattern-less** for the uncoined `pat-liquid-software` ledger (with Kus's half-life thesis and Louf's interface ladder in this batch): web pages as per-person generated surfaces.
3. **Track note:** this was the one talk of the 18 held back by YouTube's caption rate limit; it landed after the batch loaded and was added as the 18th in a second load.
4. **⚠ Verify before seeding:** "OfOneLabs" (tool name), the fast image model's name, "Gemma 4," the 2,200–2,300 tokens/s and 1.1 s / 4.6 s figures, and that the backend runs on Google and Cloudflare.
