# SPIKE extraction — "Which AI startups actually land enterprise contracts?" (Brian Lewis, Millennium) — FOR REVIEW

Source transcript: `transcripts/lewis-millennium-startups-enterprise-contracts.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/7A65O-0lvKE — AI Engineer World's Fair (AI-native enterprise / leadership track), published 2026-08-29.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-29 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the buyer's side, from a product lead at an 8,000-person hedge fund (speaking as an individual): the real enterprise-readiness bar (efficacy, security, reliability, legal) and the anti-patterns that kill pilots, plus the buyer-side thesis that **half or more of becoming AI-native is unsexy and has nothing to do with AI** — data hygiene, architecture, integration, enablement, change management. "AI is a flashlight, not a band-aid." Caption garbles: "Fable" → **Claude Fable** (mentioned in the ZDR/data-retention context), "Emil" → the morning keynote speaker (thinner agents / smarter substrate), "ZDR" = zero data retention, "CMEK" = customer-managed encryption keys, "SCIM" kept.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-lewis-millennium-enterprise-contracts` | Which AI startups actually land enterprise contracts? (Brian Lewis, Millennium — AI Engineer World's Fair) | youtube | https://youtu.be/7A65O-0lvKE |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-brian-lewis`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-brian-lewis` | Brian Lewis (Product, Millennium — speaking as an individual) | `AffiliatedWithCompany → co-millennium` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-millennium` | Millennium | investor | Multi-strategy hedge fund (~8,000 people; "trading billions of dollars"); coerced hedge fund → investor. An enterprise **buyer** in this talk: evaluates 10–15 startups per pain point, runs non-production pilots with weekly check-ins, converts ~5% of demo calls to contracts |

Reused **[registry]**, edge-only: `co-anthropic` **[seed]** (Fable named in the data-retention context), `co-openai` **[registry]** (ChatGPT "out for 43 months"). Referenced, not coined: the unnamed vendors in the anti-pattern list ("not naming and shaming — just shaming").

## Elements (6 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-enterprise-ready-from-the-inside` | Enterprise-ready, from the inside | concept | security | The bar as the buyer states it. **Efficacy**: the product actually solves the problem; pricing reflects real value; integrations demonstrated on day one, not hypothetical; the buyer defines success criteria. **Security**: zero data retention (ZDR) or customer-managed encryption keys that don't break the product; bring-your-own LLM gateway and bring-your-own infrastructure (deployable in the buyer's cloud); SCIM-tied RBAC configurable via API; at least one real security hire. **Reliability**: a control plane that works — every admin setting via API, audit logs on config changes, controlled rollouts, real SLAs, a reachable support engineer, a status page. **Legal**: no training on our data; sub-processor transparency (fourth-party risk is our risk); IP indemnification with reasonable caps |
| `el-enterprise-funnel-five-percent` | The 5% funnel | concept | | Per pain point: 10–15 interesting startups → 2–3 demo calls → 0–1 pilots → one in four pilots signs. About 5% of demo calls end in a contract — which "tracks with the industry." Where deals die: ~40% efficacy/commercial, then security, then reliability, then legal. Meanwhile the **pilot window collapsed** from ~6 months to ~3 months to ~2 weeks in two years |
| `el-vendor-anti-pattern-catalog` | The vendor anti-pattern catalog | concept | security | Real examples: vaporware the platform team could rebuild in six weeks; **upside-down pricing** (a wrapper asking the buyer to report its own gateway telemetry so the vendor can margin on it); demo promises with no ETA after two months; re-pitching declined features; data sent to the vendor's cloud against instructions; **read-write-all default scopes**; beta features on by default each release; "we'll get you the security architecture diagram next week"; "we haven't had a breach yet" as the breach plan; auto-updating clients across 3,000 people with no version control; support-page terms not in the contract; core APIs down for hours on a trading day; features shipped only as "beta" with a **permissive data-retention clause**; claimed ZDR that quietly retained data |
| `el-boring-sixty-percent` | The boring 60% | concept | | The buyer-side thesis: ~40% of getting to AI-native is models and products; ~60% is data hygiene, clean architecture, good integration, strong enablement and change management — "the stuff no one likes talking about anymore." A new frontier model every ~11 days versus architecture a decade old; ChatGPT is 43 months old while companies are still finishing five-year-old ERP migrations. "AI is a flashlight, not a band-aid: it accelerates what works and breaks down quickly where things don't." Fix the technology estate before plugging AI in |
| `el-agents-inherit-your-entitlements` | Agents inherit your entitlements | concept | security | What the flashlight showed internally: entitlements need a new paradigm — large enterprises are full of over- and under-entitled people, and the model breaks when agents need to act fast, on many things, with judgment. "Agents inherit your foundations; when processes or people go rogue, agents will 100× that problem." Companion lessons: cross-platform integration moved up the stack (AI is only as good as what it reaches); centralized, consumable knowledge for "thinner agents and a smarter substrate"; possibly a separate ecosystem for experimentation when the legacy gap is too vast |
| `el-buyer-written-success-criteria` | Buyer-written success criteria | ops | | The best startups arrive with security architecture that works, a responsive support engineer, an admin API from the beginning, a 90-day plan that deploys into the buyer's cloud, and let the buyer write the success criteria. The worst bring salesmanship, no diagrams, no deployment control or audit logs, no ETAs. Weekly pilot check-ins on non-production data surface the difference fast |

Element edges: all six `IdentifiedInArtifact → ia-aie-lewis-millennium-enterprise-contracts`.
`el-enterprise-ready-from-the-inside` `UsesElement → el-buyer-written-success-criteria`, `el-agent-scoped-authorization` **[registry]**;
`el-agents-inherit-your-entitlements` `UsesElement → el-agent-scoped-authorization` **[registry]**, `el-company-brain` **[registry]**;
`el-boring-sixty-percent` `UsesElement → el-agents-inherit-your-entitlements`;
`el-vendor-anti-pattern-catalog` `UsesElement → el-enterprise-ready-from-the-inside`;
`el-boring-sixty-percent` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**;
`el-agents-inherit-your-entitlements` `ExemplifiesPattern → pat-new-cyber-threats` **[registry]**;
`el-vendor-anti-pattern-catalog` `ExemplifiesPattern → pat-agent-supply-chain` **[registry]**.

Reused elements (no new nodes): `el-agent-scoped-authorization` **[registry]** (entitlements/RBAC), `el-company-brain` **[registry]** (the "centralized knowledge, smarter substrate" ask).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-lewis-millennium-enterprise-contracts`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-millennium`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-value-left-on-the-table-at-current-intelligence` | | The buyer's hypothesis, stated up front: "at current model intelligence, most of the value available is already being left on the table" — not a hot take inside enterprises, where the "how much are these tools actually doing?" stat gets a knowing laugh. Only ~5% of demo calls become contracts, and the reasons are efficacy, security, reliability and legal — none of them model capability | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-enterprise-funnel-five-percent`, `el-enterprise-ready-from-the-inside` |
| `sig-becoming-ai-native-is-sixty-percent-not-ai` | | "Half or more of getting to AI-native is unsexy and has absolutely nothing to do with AI." Models can't fix a legacy architecture or run change management; a frontier model ships every ~11 days while the estate is a decade old and ERP migrations from five years ago are still running. Start with the boring 60% — data hygiene, architecture, integration, enablement, change management — because AI is a flashlight that exposes and accelerates whatever is already there | `FormsPattern → pat-model-not-bottleneck` **[registry]**; `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-boring-sixty-percent` |
| `sig-platform-team-rebuilds-the-pitch-in-six-weeks` | | The efficacy failure mode from the buyer's chair: startups pitch ideas the buyer's platform team can rebuild in about six weeks — "not a knock, this is what's going on in the industry everywhere." Plus upside-down pricing (a wrapper wanting margin on traffic through the buyer's own gateway) and re-pitching declined features. Sometimes buying still wins, but the wrapper's moat is visibly thin from inside a capable enterprise | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-vendor-anti-pattern-catalog`, `el-enterprise-funnel-five-percent` |
| `sig-enterprise-security-bar-zdr-cmek-byo-everything` | security | The security bar and how vendors fail it: ZDR first, CMEK that don't break the product, bring-your-own gateway and infrastructure, SCIM-tied RBAC via API, a real security hire — against pilots that shipped data to the vendor's cloud, demanded read-write-all scopes, turned betas on by default, deferred the architecture diagram weekly, and answered "what if there's a breach?" with "we haven't had one yet." Legal side: betas with permissive retention clauses and fourth-party risk hidden on a web page — supply-chain risk in the contract, not the code | `FormsPattern → pat-new-cyber-threats` **[registry]**; `FormsPattern → pat-agent-supply-chain` **[registry]** | `OnElement → el-enterprise-ready-from-the-inside`, `el-vendor-anti-pattern-catalog` |
| `sig-agents-100x-the-entitlements-problem` | security | What the flashlight showed inside the fund: the entitlements model breaks under agents that act fast, broadly, and with judgment; enterprises are full of over- and under-entitled people, and "agents are going to 100× that problem." Recommendation: fix entitlements, governance and audit logging now, centralize knowledge for thinner agents on a smarter substrate, and consider a separate experimentation ecosystem when the legacy gap is too wide | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-agents-inherit-your-entitlements`, `el-agent-scoped-authorization` **[registry]**, `el-company-brain` **[registry]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-ai-is-a-flashlight-not-a-bandaid` | The durable framing: AI doesn't add capability to an enterprise so much as reveal and amplify what is already there — accelerating working systems and breaking quickly on broken ones. That makes the boring 60% (data, architecture, integration, enablement, change management) the actual critical path to AI-native, and explains from the buyer's side why value is "left on the table" at current model intelligence: the bottleneck is the estate, not the model | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-boring-sixty-percent`, `el-agents-inherit-your-entitlements` |
| `ins-enterprise-readiness-is-a-control-plane` | Strip the checklist to its structure and enterprise readiness is a control plane: identity (SCIM-tied RBAC, entitlements), configuration (every admin setting via API, audited, rolled out deliberately), data boundaries (ZDR/CMEK, BYO gateway and infra, no training, transparent sub-processors) and a human on call. Vendors that ship this "from the beginning" clear an 8,000-person regulated fund and therefore "basically everybody else"; the same control plane is what the buyer must build internally before agents 100× its entitlement debt | `HighlightsPattern → pat-ai-native-org` **[registry]** | `ReliesOnElement → el-enterprise-ready-from-the-inside`, `el-buyer-written-success-criteria`, `el-vendor-anti-pattern-catalog` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-lewis-millennium-enterprise-contracts`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-clear-the-enterprise-bar` | Sell into — and prepare — a regulated enterprise | **Seller side:** solve a real problem the platform team can't rebuild in six weeks; price on value, never on the buyer's own gateway telemetry; show integrations on day one; let the buyer write success criteria; offer ZDR (and mean it) or CMEK that doesn't break the product; support BYO gateway and deployment into the buyer's cloud with a 90-day plan; ship SCIM-tied RBAC and every admin setting via API with audit logs and controlled rollouts; never default to read-write-all scopes or betas-on; hire a security person and have a breach plan and an architecture diagram before the pilot; keep a status page, real SLAs and a reachable support engineer; keep contract terms out of support pages and never hide data retention in a beta clause. **Buyer side:** start with the boring 60% — fix entitlements, governance and audit logging before agents 100× the problem; move integration up the stack; centralize knowledge so agents can be thin; and spin up a separate experimentation ecosystem when the legacy gap is too vast | `ReferencesElement → el-enterprise-ready-from-the-inside`, `el-vendor-anti-pattern-catalog`, `el-boring-sixty-percent`, `el-agents-inherit-your-entitlements`, `el-buyer-written-success-criteria` |

## Dropped

- **The "my mom asked why" / economics-degree intro and the missing Coinbase speaker** — color only.
- **The compliance disclaimer** — recorded in the expert row (speaking as an individual).
- **The QR/LinkedIn close** — nothing to extract.

## Review notes

1. **⚑ Buyer-side calibration for `pat-model-not-bottleneck`.** Most corpus evidence for the pattern is builder-side (harness, verification). Lewis supplies the demand-side version with a funnel number (~5% demo-to-contract) and a breakdown that never mentions model capability. Consider citing in the pattern's brief.
2. **`co-millennium` typed `investor`** is a coercion (hedge fund). If review prefers the buyer role to dominate, `developer` is the alternative; the node's brief records the buyer stance either way.
3. **`sig-enterprise-security-bar-zdr-cmek-byo-everything` double-edges** to `pat-new-cyber-threats` (vendor-side data/scope failures) and `pat-agent-supply-chain` (beta retention clauses, fourth-party risk as contract-level supply chain). The supply-chain reading is a widening — flag for review.
4. **⚠ Verify before seeding:** the "5% of demo calls" figure and its industry benchmark; "a frontier model every 11 days"; "ChatGPT out for 43 months"; the 40/60 split is explicitly "unscientific."
5. **Domain empty for the two thesis signals** (leadership track); security signals carry `security`.
