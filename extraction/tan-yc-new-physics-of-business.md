# SPIKE extraction — "The New Physics of Business" (Garry Tan, Y Combinator) — FOR REVIEW

Source transcript: `transcripts/tan-yc-new-physics-of-business.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/eBUyTS7SzV4 — AI Engineer World's Fair, published 2026-07-17.
`stagingTimestamp` for the artifact and all signals: 2026-07-17 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-tan-new-physics` | The New Physics of Business (Garry Tan, Y Combinator — AI Engineer World's Fair) | youtube | https://youtu.be/eBUyTS7SzV4 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-garry-tan`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-garry-tan` | Garry Tan (President & CEO, Y Combinator; founder and investor; running YC's own AI-native transformation; builds G Brain in the open) | `AffiliatedWithCompany → co-y-combinator` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-y-combinator` | Y Combinator | investor | startup accelerator; appears both as investor (batch data) and as a 20-year-old institution converting itself to an AI-native org |

## Elements (2 new, 3 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-company-brain` | Company brain | concept | context | The library plus the librarian: a curated organizational memory (every email, meeting, decision + reasoning, customer conversation, postmortem) with an arbitration layer deciding which "three books" get loaded into an agent's ~1M-token context per task; retrieval is the primitive ("this is just RAG" the way Postgres is just B-trees) — curation, enrichment, hot-vs-cold promotion, and contradiction arbitration are the product |
| `el-gbrain` | G Brain | product | context | Tan's MIT-open-source company-brain / personal-AI retrieval layer ("Postgres for agents"); works with any harness, pairs with OpenClaw + Hermes agent; his personal instance: ~220,000 pages written mostly by his agents from 20 years of email, meetings, and notes |

Element edges: both `IdentifiedInArtifact → ia-aie-tan-new-physics`; `el-gbrain` `UsesElement → el-company-brain`; `el-gbrain` `UsesElement → el-hermes-agent` **[registry]**; `el-company-brain` `EnablesPattern → pat-context-graphs` **[registry]**.

Reused: `el-agent-skills` **[registry]** (skill files as employees), `el-openclaw` **[registry]** (YC's internal harness; "OpenClaw is the Ferrari... Codex is a really good Honda"), `el-hermes-agent` **[registry]**.

## Signals (4 new)

All: domain `harness` unless noted, `SpottedInArtifact → ia-aie-tan-new-physics`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-y-combinator`.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-tan-400x-not-the-model` | Tan's self-measured output: ~14 usable logical lines/day as a near-full-time engineer YC partner in 2013 (median for the era) vs ~400x that today running YC full-time on fewer hours — 8x at the most pathological verbosity discount, ~80x mid. His tattoo-worthy point: the 2x and 100x people use the exact same Claude, same weights, same context window — "the leverage is not in the weights, it's in how you wire the work" | `FormsPattern → pat-model-not-bottleneck` **[registry]**, `FormsPattern → pat-harness-over-model` **[registry]** | — |
| `sig-w25-batch-95pct-ai-code` | Winter 2025 YC batch: a quarter of companies had codebases 95% AI-generated — a year before this talk — and that batch became the fastest-growing, most profitable in YC history (94 YC companies all-time have crossed $100M revenue from a seed check); the fastest-growing founders treat AI as a workforce, not autocomplete | `FormsPattern → pat-saaspocalypse` **[registry]** | — |
| `sig-ai-native-revenue-per-head` | Revenue-per-head records that "did not exist before — not in software, not in oil, not in railroads": Emergence (S24 AI app builder) public launch → nine-figure ARR in 8 months, 15 people at $15M ARR; Retail (W24) $60M with ~40 people; the AI-native operating model: encode sales/support/ops/finance as skills agents execute, hire engineers to maintain the skills (domain: infra) | `FormsPattern → pat-saaspocalypse` | — |
| `sig-nontechnical-staff-manage-agents` | Inside YC's own transformation the shift crossed the technical line: media, events, and finance staff who never opened a terminal are writing skill files and cron jobs; one finance person collapsed ~100 Excel workbooks into an app she built with internal OpenClaw + the company brain — "she's not a programmer, she's a manager of agents now, and everyone at YC is" | `FormsPattern → pat-saaspocalypse` | `OnElement → el-openclaw` **[registry]** |

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-org-as-markdown` | Every organizational primitive maps onto harness constructs: a skill file is an employee (one capability, written clearly enough to execute), a resolver table is the org chart (routes each task to who handles it), filing rules are internal process, trigger evals are performance reviews. Companies were always "organizations of written procedure" — what was missing was a management layer for executing them, and that's what a harness is: sitting down with Claude Code/Codex is hiring, training, and managing a workforce made of markdown | `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-agent-skills` **[registry]** |
| `ins-latent-vs-deterministic-placement` | Most AI-engineering bugs come from computation living on the wrong side of one boundary: latent space (the LLM — taste, judgment, decoding vague human intent, steered by markdown) vs deterministic space (code — state, storage, exact computation). His example: seating 800 people optimally at Startup School must keep the seat-assignment array out of the context window; the LLM does the human-judgment part. Getting placement right turns a month of work into ~10 minutes and a few hundred dollars of tokens | `HighlightsPattern → pat-harness-over-model` **[registry]** | — |
| `ins-owned-memory-beats-rented-models` | Every institution humans built — checklists, org charts, filing cabinets — is a prosthetic for the 7±2-item working memory; agents hold ~1M tokens ("three Harry Potter books open at once"), yet a company is a library, not three books, so the librarian deciding which three books open per task (context engineering) determines whether agents are geniuses or goldfish. Model quality is rented; a curated brain is owned and compounds — "retrieval is easy; being worth retrieving from is the product." Tan's greenfield call: every company on earth is about to need a brain; the memory layer should be open the way Linux is open | `HighlightsPattern → pat-context-graphs` **[registry]**, `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-company-brain`, `ReliesOnElement → el-gbrain` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-tan-new-physics`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-skillify-everything` | Never do one-off work — skillify it | After any agent task whose output you're happy with, convert the session into a reusable skill before moving on ("if you have to ask for something twice, you failed"); the org that captures what it learns gets smarter daily, the one that doesn't wakes up every morning with amnesia regardless of model quality; concepts travel with any stack — the tools don't matter | `ReferencesElement → el-agent-skills` **[registry]** |
| `how-brain-hygiene` | Treat the brain like production infrastructure | Failure modes: an uncurated brain is a garbage dump with great search — retrieval surfaces stale facts with total confidence, and a bad skill file encodes a bad process forever. The primitive is memory **plus hygiene**: provenance on every fact, contradiction checks when new information collides with old, and a librarian (human + agent) whose actual job is pruning; dumped-in memory yields a very confident agent that is wrong in ways nobody can trace | `ReferencesElement → el-company-brain` |

## Dropped

- The epilepsy-father story (80,000-markdown-file company brain for one child) — moving instantiation of the same architecture; prose only.
- "Is that AGI? Maybe not" aside, abundance/jobs closing, battlefield exhortation — rhetoric.
- Emergence and Retail as Company nodes — cited only as revenue datapoints inside `sig-ai-native-revenue-per-head`; coin them if the graph starts tracking YC portfolio companies.

## Review notes

1. **Pattern candidate flagged, NOT coined (no edges):** "the AI-native organization" — org-as-markdown, thin teams, agents-as-workforce, non-technical staff as agent managers — is arguably a distinct thesis about how companies are structured, not just SaaS economics. Evidence here is one talk (plus soft echoes in the loops debate), so per the one-talk rule it's filed under `pat-saaspocalypse` and flagged for the reconciler. If a later batch surfaces the same thesis, coin something like `pat-ai-native-org` and rehome the three `pat-saaspocalypse` links above.
2. "G brain" is consistently garbled lowercase in captions ("G brain", "gbrain"); official spelling unverified — likely "GBrain" or "Garry's Brain". Verify before public-facing use. Same for "Retail" (W24 company — possibly "Ret AI l"-style garble of another name) and "Emergence" (S24).
3. `sig-tan-400x-not-the-model` carries the talk's own caveats in the brief (8x floor under adversarial assumptions) — self-measured, contested-on-the-internet number, but Tan restates it deliberately on the record.
4. The 7±2 working-memory framing independently anchors Schillings' talk in this batch (see `schillings-deepmind-not-about-writing-code.md` review notes) — a genuine cross-speaker convergence worth an edge only if the reconciler wants Insight↔Insight linkage (schema has none; noted as prose).
5. "Open Claw" mapped to `el-openclaw` **[seed registry]** and "Hermes agent" to `el-hermes-agent` **[seed registry]** — both consistent with seed usage.
