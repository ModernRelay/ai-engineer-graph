# SPIKE extraction — "Build the AI GTM Agent That Knows the Buyer" (Dr. Sajjan Kanukolanu, Position2) — FOR REVIEW

Source transcript: `transcripts/kanukolanu-position2-gtm-agent.txt` (auto-captions — quotes are paraphrases; speaker name garbled as "Sajjan Khan Akolanu", company as "Position Squared").
Video: https://youtu.be/ltv-L5oMPIs — AI Engineer World's Fair, published 2026-07-20.
`stagingTimestamp` for the artifact and all signals: 2026-07-20 (publish date).
Entities marked **[existing]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-kanukolanu-gtm-agent` | Build the AI GTM Agent That Knows the Buyer (Dr. Sajjan Kanukolanu, Position2 — AI Engineer World's Fair) | youtube | https://youtu.be/ltv-L5oMPIs |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-sajjan-kanukolanu`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-sajjan-kanukolanu` | Dr. Sajjan Kanukolanu (VP Global Operations & Strategy, Position2; 20+ years product/technology/marketing) | `AffiliatedWithCompany → co-position2` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-position2` | Position2 | developer | growth-marketing firm running an AI-native transformation; builds GTM agents for clients (75+ agents live) |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-buyer-context-graph` | Buyer context graph | concept | context | Per-buyer connected record rolling every signal into persona ↔ account ↔ deal: individual touchpoints link to their account, accounts surface the buying committee, deal-level state records what sales/marketing already did — the structure that makes account prioritization and alert throttling possible at all |
| `el-position2-intelligence` | Position2 Intelligence | product | context | Position2's internal GTM system: identification job (multiple de-anonymization sources, consolidated + deduped) → enrichment → ICP-filter agent screening against the knowledge base → CRM match agent (warm/hot) → action agent (Slack alerts with drafted emails, direct outreach, LinkedIn touches); dashboards for anonymous visitors and LinkedIn engagement; personalized chat that resumes a returning visitor's last conversation |

Element edges: `el-position2-intelligence` `DevelopedByCompany → co-position2`; `el-position2-intelligence` `UsesElement → el-buyer-context-graph`; `el-buyer-context-graph` `ExemplifiesPattern → pat-context-graphs`; both `IdentifiedInArtifact → ia-aie-kanukolanu-gtm-agent`.

## Signals (3 new)

All: domain `context`, `SpottedInArtifact → ia-aie-kanukolanu-gtm-agent`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-buyers-genai-primary-research` | B2B buying moved behind a GenAI black box (Forrester 2026 per speaker): 94% of buyers use GenAI as primary research, 67% prefer a rep-free experience, 80% of deals go to vendors on the buyer's pre-contact shortlist, only 17% of total buying time is spent with vendors — the decision is mostly made before first contact, and sellers can't see what the GenAI platforms told the buyer | `FormsPattern → pat-saaspocalypse`, `FormsPattern → pat-context-graphs` | — |
| `sig-identity-ceiling` | Structural limit of visitor de-anonymization tooling (2026): ~70% accuracy at company identification but only ~15–20% at individual identification — a ceiling every GTM-AI architecture must plan around rather than engineer away | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-position2` |
| `sig-position2-gtm-agent-fleet` | Agentic GTM at production scale (month-to-date June 2026): Position2 runs 75+ client AI agents powered by 18+ vertical knowledge bases at 800+ runs/month, with growth expected by year-end | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-position2` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-gtm-bolt-on-fails` | Bolting AI onto a SaaS-era GTM stack cannot scale: stand-alone AI can't infer buyer role/history/intent, old stacks can't capture the signals AI generates, and the architecture itself must be rebuilt with a per-buyer context graph at the core — solving identity and integration without the architecture still fails. The greeting test makes it visible: a bolted-on chat asks "how can I help you?" to a late-stage buyer who already decided, and they walk | `HighlightsPattern → pat-context-graphs`, `HighlightsPattern → pat-saaspocalypse` | `ReliesOnElement → el-buyer-context-graph` |
| `ins-human-trust-budget` | Agentic GTM systems die at human trust boundaries, not model quality: flag everything hot and reps stop acting (alert fatigue); let AI-drafted emails need >30 seconds of editing and reps go back to writing their own. Survival = context-graph-throttled alerts + near-send-ready drafts + a policy engine the GTM operator (not a developer) can audit and fix | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-buyer-context-graph` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-kanukolanu-gtm-agent`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-separate-fit-from-intent` | Score ICP fit and buying intent separately | Conflating fit (right industry/geo/size/persona) with intent (buying stage vs research mode) sends the wrong message to the wrong person; define both scores explicitly in the knowledge base; weed non-fit contacts out before they reach the CRM-match and action layers; start with identity — if you can't identify visitors, the GTM project is dead | `ReferencesElement → el-buyer-context-graph` |
| `how-gtm-flywheel-retraining` | Retrain the GTM knowledge base on closed outcomes | ICPs drift (close a $100M-vertical deal and your target profile just changed); retrain agents quarterly on closed-won/closed-lost; feed every send, reply, win, loss, and deferral back into the knowledge base so the flywheel compounds — otherwise agents keep pointing at yesterday's accounts | `ReferencesElement → el-position2-intelligence` |
| `how-30-second-friction-budget` | Keep human touchpoints inside a friction budget | AI-drafted rep emails must be sendable with one click after ≤30 seconds of edits or reps abandon the system; throttle alerts through the context graph so only accounts that matter fire; make the policy engine auditable and adjustable by GTM operators so broken workflow steps get fixed without a developer | `ReferencesElement → el-position2-intelligence`, `ReferencesElement → el-buyer-context-graph` |

## Dropped

- HubSpot, LinkedIn, and the unnamed de-anonymization vendors as Company/Element nodes — interchangeable plumbing ("these tools change all the time for us, but not the architecture").
- The exec-sponsor-changes-jobs LinkedIn play — good tactic but folded into `el-position2-intelligence`'s brief rather than a standalone KnowHow (it's one routing rule, not a transferable practice framework).
- Demo walkthrough details (3,000 visitors / 280 accounts, 100 LinkedIn visitors / 73 companies / 8 posts) — dashboard-of-the-day numbers, not durable signals.

## Review notes

1. `sig-buyers-genai-primary-research` bundles four stats; only the 94% figure is explicitly attributed (Forrester 2026), the rest are unattributed speaker stats — split the signal if provenance granularity matters. Its `pat-saaspocalypse` edge reads the buyer-research shift into GenAI platforms as part of the SaaS-era-distribution collapse; cut if you scope that pattern to software delivery only.
2. `ins-human-trust-budget` → `pat-verification-gap`: the 30-second rule is "human verification cost kills agent systems" — same thesis as batch1's `ins-steer-beats-ask`, different domain. Confirm the cross-domain reuse.
3. `sig-position2-gtm-agent-fleet` is a vendor adoption stat of exactly the kind batch1 dropped ($1M cloud-code rollouts); kept because it's one of the few dated, quantified agentic-GTM production datapoints in the graph. Drop without argument if you disagree.
4. `co-position2` type: enum has no "services/agency"; `developer` chosen since they build and operate agents.
