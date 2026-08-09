# SPIKE extraction — "Forward Deployed Engineering at Cursor" (Pauline Brunet, Cursor) — FOR REVIEW

Source transcript: `transcripts/brunet-cursor-forward-deployed.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/APqXGyCoGW4 — AI Engineer World's Fair, published 2026-07-14.
`stagingTimestamp` for the artifact and all signals: 2026-07-14 (publish date).
Entities marked **[registry]** are already in the registry; **[this batch]** are defined in another file of this 5-talk batch.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-brunet-forward-deployed` | Forward Deployed Engineering at Cursor (Pauline Brunet — AI Engineer World's Fair) | youtube | https://youtu.be/APqXGyCoGW4 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-pauline-brunet`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-pauline-brunet` | Pauline Brunet (global lead, forward deployed engineering, Cursor; 10 years of enterprise AI deployments) | `AffiliatedWithCompany → co-cursor` **[registry]** |

## Companies (0 new)

- `co-cursor` **[registry]** — `RelevantCompany` target for all signals below. Spotify / Rippling / Palantir (FDE hiring sources) named only in passing — no nodes.

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-forward-deployed-engineering` | Forward deployed engineering (FDE) | concept | — | Vendor function embedding senior engineers ("magical unicorns": deeply technical + high EQ) inside customer organizations to co-design and co-build strategic AI deployments in the customer's codebase — distinct from professional services and staff augmentation; fit is a 2×2 of customer digital maturity × product customizability, with FDE value concentrated in the middle band (accelerate the mature, embedded transformation for the less mature); doubles as the tightest product-feedback loop the vendor has |

Element edges: `IdentifiedInArtifact → ia-aie-brunet-forward-deployed`; `ExemplifiesPattern → pat-saaspocalypse` **[registry]** (software increasingly sold as co-built agentic transformation rather than out-of-the-box SaaS).

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-brunet-forward-deployed`, `SourcedFromSource → source-aie-yt`, `RelevantCompany → co-cursor`.

| slug | domain | name / brief | FormsPattern |
|---|---|---|---|
| `sig-fde-breakout-ai-job` | harness | FDE framed as the breakout AI job of 2026 ("waiting for the Forbes article: 2026's hottest job"); Cursor is building a global FDE org hiring only 5+-year engineers with customer-facing experience (from Palantir, Spotify, Rippling), organized geo-first → industry-verticals later, with roles expected to be redefined every ~6 months | `FormsPattern → pat-saaspocalypse` **[registry]** |
| `sig-cursor-agents-beyond-sdlc` | harness | Cursor FDEs are deploying long-running cloud agents and Cursor-SDK applications beyond the software development lifecycle — HR, finance, supply chain, e-commerce, call-center ticketing, asset management at retailers and banks — as the "tip of the spear" testing edge use cases before productization | `FormsPattern → pat-saaspocalypse` **[registry]** |
| `sig-org-redesign-demand` | harness | Repeated unprompted enterprise demand (heard "six or seven times") for a new offering: not deployment help but organizational redesign — whom to hire, what job descriptions, how to rearrange teams and processes to capture value from AI tooling; Cursor is now standing up an offering for it | — (see Review notes: "AI-native organization" candidate resonance; deliberately un-coined) |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-fde-fit-matrix` | FDE creates value only in the band between the extremes of customer digital maturity × product customizability: high-maturity/low-customization → self-serve docs; low/low → traditional SaaS rollout; high/high → advisers who accelerate. Misplaced FDE degenerates into staff augmentation, bores away your 10x engineers, and they leave | `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-forward-deployed-engineering` |
| `ins-agent-roi-is-the-unit-of-account` | Enterprise agent value must be denominated in the customer's three currencies — increase revenue, decrease cost, mitigate risk: a $2,000/day agent read as expensive until reframed as dispatch-cost reduction ("absolutely worth it, but I never measured it this way"); ROI framing, not model capability, decides whether deployments survive after the vendor leaves | `HighlightsPattern → pat-value-of-judgement` **[this batch]** (defined in `osmani-engineer-of-the-future.md`) | `ReliesOnElement → el-forward-deployed-engineering` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-brunet-forward-deployed`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-scope-fde-engagements` | Scope FDE engagements as directional problem-solving, never bodies | Anchor with the economic buyer/senior champion on a strategic objective; refuse "we're understaffed, do X" (staff-augmentation red flag) — ask "who is the working team?"; define success upfront as a measured baseline delta (3 hours → 20 minutes); keep scope directional (problem + phases + ~6 weeks + KPIs) not fixed-deliverable, because you haven't seen their data/systems and learnings force pivots; involve the customer at every step so nothing is switched off when you leave; over-communicate ROI (revenue / cost / risk) and leave documentation artifacts behind | `ReferencesElement → el-forward-deployed-engineering` |
| `how-build-an-fde-team` | Build the FDE function to fit your buyer | Map your customers' maturity and your product's customizability before hiring; first hires are senior "unicorns" (5+ yrs, technical + customer-facing) — split into specialized roles only at scale; designate SMEs per product area (e.g. long-running cloud agents, SDK) that others pull into projects; hand change management and broad rollouts to SIs/consultancies who know the accounts; say no to wrong-fit use cases — honesty compounds into trust; expect to re-plan profiles and structure every ~6 months | `ReferencesElement → el-forward-deployed-engineering` |

## Dropped

- "AI software factory" mission language — overlaps batch-3 software-factory material; kept in prose only.
- "A players hire A players, B players hire C players" and war-for-talent commentary — general management advice, no node.
- Cursor SDK — mentioned as a delivery surface; not coined (would be load-bearing only in a product-focused talk).

## Review notes

1. "Pauline Brane" in captions = Pauline Brunet (per official title). Captions oscillate between "FDE" and "FTE" — all read as FDE (forward deployed engineer); no full-time-equivalent meaning anywhere in context.
2. `sig-org-redesign-demand` intentionally carries no FormsPattern: it is fresh independent resonance for the un-coined batch-3 candidate **"AI-native organization"** (Tan; also echoed by the Wu/Shihipar talk in this batch). If that pattern gets coined centrally, this signal is a natural FormsPattern source.
3. Thin-signal talk: it's an operating-manual talk, so signals are practitioner testimony about the function's emergence rather than dated external facts; the two KnowHows carry most of the value. If the signal bar fails, fallback is 2 signals (drop `sig-fde-breakout-ai-job` into prose).
4. `pat-saaspocalypse` linkage assumes the registry brief covers "software delivery model disruption" broadly (out-of-box SaaS → co-built agents). If its brief is strictly "SaaS businesses collapsing", rehome these edges to `pat-value-of-judgement` or leave the signals pattern-less.
