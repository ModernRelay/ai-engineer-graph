# SPIKE extraction — "The Factory That Dreams: 39 AI Agents, No Framework" (Rushabh Doshi, Machinecraft) — FOR REVIEW

Source transcript: `transcripts/doshi-machinecraft-39-agents-no-framework.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/jtzh-GBXBWc — AI Engineer World's Fair, published 2026-07-11.
`stagingTimestamp` for the artifact and all signals: 2026-07-11 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-doshi-39-agents-factory` | The Factory That Dreams: 39 AI Agents, No Framework (Rushabh Doshi, Machinecraft — AI Engineer World's Fair) | youtube | https://youtu.be/jtzh-GBXBWc |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-rushabh-doshi`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-rushabh-doshi` | Rushabh Doshi (third-generation owner-operator of Machinecraft, a ~100-person thermoforming-machine factory in India; built its multi-agent GTM "brain" himself) | `AffiliatedWithCompany → co-machinecraft` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-machinecraft` | Machinecraft | hardware | Indian thermoforming-machine manufacturer (~100 people, three-generation family business; machines serve seven verticals from hydroponic trays to EV panels). Appears as a non-tech SMB that built its own agent system — not an AI vendor. |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-brain-os` | Brain OS | framework | harness | Machinecraft's forkable "company brain" architecture, shipped as an empty nervous system (forkmybrain.org): ~39 single-job specialist agents (orchestrator, sales, pricing, machine specs, fact-checking, corrections-guarding) that hold moderated "meetings"; layered engineered memory (working memory / pinned facts / episode stories / relationship warmth) behind a salience gate, with corrections always beating conflicting facts; a nightly sleep cycle; and a values "soul file" (Jain family-business principles compiled to engineering rules: cross-check before speaking, cite document + date, never speak in absolutes). Built on off-the-shelf models from three providers — no fine-tuning — over vector + relationship-graph + CRM databases, with ~213 tools exposed over one protocol. Golden rule: agents draft, humans send. |
| `el-agent-sleep-cycle` | Agent sleep cycle | concept | context | Nightly offline consolidation pass for an agent system: replay the day, lock in useful facts, hunt contradictions, decay stale junk, distill the day's work into reusable skills, and emit a morning "dream report" for the operator. The system measurably "gets smarter overnight" without any training run. |

Element edges: `el-brain-os` `DevelopedByCompany → co-machinecraft`, `UsesElement → el-agent-sleep-cycle`, `ExemplifiesPattern → pat-context-graphs` **[registry]**; both `IdentifiedInArtifact → ia-aie-doshi-39-agents-factory`.

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-doshi-39-agents-factory`, `SourcedFromSource → source-aie-yt` **[registry]**. Domain per row.

| slug | name / brief | domain | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-factory-grows-company-brain` | A 100-person Indian factory with no data-science team or ML budget turned "three generations in three brains" into a company brain: hundreds of GB of private history (quotes back to 2019, drawings, payment schedules, email threads) chunked and fact-extracted by off-the-shelf models, stored as vectors plus a who-connects-to-what relationship graph — no fine-tuning, no GPUs, zero training bill | context | `FormsPattern → pat-context-graphs` **[registry]** | `RelevantCompany → co-machinecraft` |
| `sig-39-agent-gtm-pantheon` | Machinecraft's entire front-of-funnel GTM — nine daily jobs (outbound referencing real history, account briefs from cross-checked facts, quotations, outreach triage, dead-lead revival, inbound replies, fit-screening) — runs on ~39 single-job specialist agents that argue in moderated meetings, because "one prompt that's supposed to do everything ends up doing everything badly"; operated from a single Cursor tab, draft-only with a human send | harness | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-machinecraft` |
| `sig-agent-build-cost-collapse` | An agency quoted ~$230k to build the system; the owner built it for ~$30k ("cheaper than a nice watch") and runs it for a couple thousand dollars/month — then open-sourced the architecture as forkable Brain OS: "we are not selling ours to you, we are helping you build your own" | harness | `FormsPattern → pat-saaspocalypse` **[registry]** | `RelevantCompany → co-machinecraft` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-memory-not-model` | The differentiating asset was never a smarter model — "the brain isn't a smarter model, it's a really well-organized memory." Off-the-shelf models reading structured private history (vectors + graph + corrections-win + salience gating) beat the fine-tuning reflex; "the expensive part was never compute, it was teaching a company to remember itself" | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-company-brain` **[registry]**, `ReliesOnElement → el-brain-os` |
| `ins-company-brain-not-outsourceable` | A company brain cannot be bought or outsourced — only the company can pour its own truth in; the sellable artifact is the empty architecture (Brain OS), not the filled brain. Moat shifts from the software to the buyer's own curated memory — uncomfortable news for agencies and vendors selling "AI transformation" | `HighlightsPattern → pat-context-graphs` **[registry]**, `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-brain-os` |

## KnowHow (1 new)

All `SourcedFromArtifact → ia-aie-doshi-39-agents-factory`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-grow-company-brain` | Grow a company brain from private history instead of training a model | Feed everything (quotes, drawings, emails, payment schedules — your internet, not the public one); chunk and fact-extract with off-the-shelf models; store meaning as vectors and relationships as a graph. One agent, one job — never a mega-prompt; let a moderator agent convene specialists. Corrections beat conflicting facts and stay fixed forever; gate memory writes with a salience filter so the brain doesn't fill with junk. Run a nightly sleep cycle (replay, consolidate, contradiction-hunt, forget, skill-extraction) with a morning report. Encode house values as engineering guardrails (cross-check before speaking; cite document and date; never absolute claims; report ugly truths). Agents draft, humans send | `ReferencesElement → el-brain-os`, `ReferencesElement → el-agent-sleep-cycle` |

## Dropped

- The Greek-pantheon agent names (Athena, Prometheus, Plutus, Hephaestus, Vera, Memnon) — flavor; folded into the `el-brain-os` brief.
- "213 tools over one protocol" — almost certainly MCP but never named on stage; no edge to `el-mcp` **[registry]**, kept as prose.
- "Three different model providers, each picked for the job" — unnamed; prose only.
- The biology framing (senses/gut/immune system) — metaphor layer over the same architecture; kept only where it maps to mechanisms (sleep cycle, salience gate).

## Review notes

1. **Agent count mismatch:** title says 39 agents; captions consistently say "36" ("a 36 AI agent", "why 36 agents"). Kept 39 per the official title; verify.
2. **System name garbled** across captions as "Era" / "Eira" / "Ira" — rendered "Eira" where needed in prose; actual spelling unverified (possibly "AIRA"). Kept out of slugs deliberately.
3. **Currency assumption:** "230 grand" / "built for around 30" read as USD (speaker later says "a couple of thousand dollars a month"); flag if you want it hedged.
4. **"One cursor tab"** read as the Cursor IDE (`co-cursor` **[registry]**) but lowercase in captions — left as prose, no company edge.
5. **"AI-native organization" candidate (do-not-coin list):** this talk is a resonance point — a 100-person manufacturer whose GTM is agents end-to-end. Noted, no edge.
6. **`el-company-brain` reuse:** coined in batch 3 (Schillings). This talk is a full concrete instance of the concept; if the batch-3 brief is narrower than this use, rehome the `ins-memory-not-model` edge at review.
7. `ins-company-brain-not-outsourceable` carries two HighlightsPattern edges (context-graphs + saaspocalypse) — trim to one if you enforce single-pattern insights.
