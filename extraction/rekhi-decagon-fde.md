# SPIKE extraction — "How Forward Deployed Engineering is done at Decagon" (Sunny Rekhi, Decagon) — FOR REVIEW

Source transcript: `transcripts/rekhi-decagon-fde.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/7wu2hsRfvV0 — AI Engineer World's Fair, published 2026-07-28.
`stagingTimestamp` for the artifact and all signals: `2026-07-28T00:00:00Z` (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node. **[this batch]** = defined in another file of this 4-talk FDE set.

Context: the **operating-model** talk of the FDE cluster — how a 24/7 AI customer-service agent vendor runs its forward deployed motion through 10× headcount growth (50 → 500 people in a year). Delivered immediately after the Sierra talk and explicitly building on it ("the previous speaker alluded to this as well"). ⚠ The company name is garbled in nearly every occurrence — see Review note 1.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-rekhi-decagon-fde` | How Forward Deployed Engineering is done at Decagon (Sunny Rekhi — AI Engineer World's Fair) | youtube | https://youtu.be/7wu2hsRfvV0 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-sunny-rekhi`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-sunny-rekhi` | Sunny Rekhi (CTO of Forward Deployed Engineering, Decagon — owns both the agent-builder and agent-software-engineer lanes through the company's 50 → 500 growth year) | `AffiliatedWithCompany → co-decagon` **[registry]** |

## Companies (0 new)

- `co-decagon` **[registry, batch 10]** — `RelevantCompany` target for every signal below. The batch-10 node was coined on reference (Notion's multi-agent partner); this is its **primary-source talk**, so its brief can be widened at seeding: 24/7 multilingual omni-channel AI customer-service agent, hypergrowth from 50 to 500 people in a year, land-on-deflection / expand-into-revenue motion.
- **Hertz** named as a customer with a concrete expansion story, and "financial institutions / your favourite tech brand" as logo categories — no nodes (customer name-drops; same treatment as the customer lists in `brunet-cursor-forward-deployed.md`). See Dropped.
- **Codex / Claude Code** referenced as the coding agents an FDE is tempted to reach for — carried by registry elements, not company edges.

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-decagon-agent` | Decagon agent | product | harness | 24/7 AI customer-service agent replacing IVR trees and multi-day email queues with human-like phone and email response; multilingual and omni-channel (phone, email, text, WhatsApp). Deployment shape: **land** on the complex inbound support workflows that today must go to humans, then **expand** into revenue-generating outbound once the back-end integrations exist (stated example: Hertz, where the same integrations now drive proactive lease renewal/extension outreach). Design constraint that governs the whole FDE motion: the agent is **configured in natural language and owned by the customer**, so it must never become "a black box of prompts and patches" — brittle for the vendor and worse for the customer |
| `el-fde-role-specialization` | FDE role specialization (agent builder / agent software engineer) | concept | harness | The org split that hypergrowth forced: the original generalist "agent software engineer" — who configured the agent brain beside the customer, built back-end integrations *and* upstreamed platform work — divides into two lanes. **Agent builders** are product experts with intuition for the models underneath, working in the UI wherever possible and flagging what must go off-UI; **agent software engineers** are the front line for customer product asks, responsible for getting them into the platform. Staffed on top with **vertical expert pools** — the people who ran financial-services customers A, B and C get staffed on D — so domain lingo, credibility and success criteria compound instead of being relearned per logo |
| `el-custom-to-self-serve` | Custom becomes self-serve | concept | harness | Decagon's stated guiding ethos for the field-to-product funnel: every manual or bespoke thing an FDE does is a defect to be upstreamed until the customer (or the agent-building team) can do it themselves. Canonical instance: custom CRM integrations were hand-built one at a time until roughly the 25th, when "enough is enough" produced a self-serve integration builder, moving work that required an engineer writing custom code to configuration. Generalized rule: solve enterprise A's ask so that B, C, D and E inherit the solution before they ask — which happens "with stunning regularity" |

Element edges: all three `IdentifiedInArtifact → ia-aie-rekhi-decagon-fde`. `el-decagon-agent` `DevelopedByCompany → co-decagon` **[registry]**; `el-fde-role-specialization` `UsesElement → el-forward-deployed-engineering` **[registry, batch 5]**; `el-custom-to-self-serve` `UsesElement → el-forward-deployed-engineering` **[registry]**, `ExemplifiesPattern → pat-saaspocalypse` **[registry]** (the mechanism by which co-built services work is converted back into product surface — the vendor-side of "services is the new software"); `el-forward-deployed-engineering` **[registry]** also `IdentifiedInArtifact → ia-aie-rekhi-decagon-fde`.

Registry element reuse (edges only, no new nodes): `el-claude-code` **[registry, batch 5]** and `el-codex` **[registry, batch 6]** — named as the two agents an FDE reaches for when a customer wants a one-off now ("maybe I'll just go prompt Codex and Claude Code to do it for me"), i.e. the specific capability that makes restraint scarce.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-rekhi-decagon-fde`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-decagon` **[registry]**.

| slug | domain | name / brief | FormsPattern | extra edges |
|---|---|---|---|---|
| `sig-decagon-fde-equals-product-eng` | harness | Stated as the talk's most important point ("so important I wish I had a slide for it"): at Decagon **forward deployed engineering is identical to product engineering** — same hiring bar, same reporting structure, often the same team, reflected in the org chart. Rationale: when a Fortune 20 customer expresses a pain point in a call, that *is* a product feature that has to be built and prioritized, so the delineation between "forward deployed person" and "person who works on the product" is "gone". Independent corroboration of the Sierra observation that the lines are blurring, from a vendor that has already restructured around it | — (**held pattern-less** — second of the three cluster signals stating the un-coined FDE thesis; see Review note 2) | `OnElement → el-forward-deployed-engineering` **[registry]**, `el-fde-role-specialization` |
| `sig-decagon-hypergrowth-role-split` | harness | Org-scaling data point with dates: **50 → 500 people in a year** (and not slowing) forced the generalist agent-software-engineer role to split into two specialized lanes — agent builder (configures the agent brain in the UI: tonality, literal voice, user intents to hand off to a human, back-end actions like password resets) and agent software engineer (upstreams customer asks into the platform) — plus vertical expert staffing so knowledge compounds across logos in a vertical and **every deployment is faster than the last** | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-fde-role-specialization`, `el-decagon-agent` |
| `sig-restraint-is-the-scarce-skill` | harness | Direct claim about what coding agents changed: **"the scarce skill now that AI coding is so good is exercising restraint."** The temptation is to prompt Codex or Claude Code to satisfy an important customer's ASAP request; the FDE's job is to refuse the one-off and architect the fix so future customers benefit — reinforced by the product ethos that agents are owned by the customer, so a pile of one-off prompts and patches is "far too brittle" for both sides | `FormsPattern → pat-value-of-judgement` **[registry]** | `OnElement → el-claude-code` **[registry]**, `el-codex` **[registry]**, `el-custom-to-self-serve` |
| `sig-requirements-gathering-returns` | harness | Counterintuitive second-order effect of cheap code, offered as a "really good learning": because starting is now nearly free, **more effort has to move up front into requirements gathering** — narrowing what success means (which metrics, which channels, which pain point, what the ideal outcome is), **ideally in writing at deal-scoping time** so there is no miscommunication later. Paired with a fast time-to-value discipline: a Fortune 500 will hand you the entire kitchen sink, so prove value immediately and expand within what is expected to be a multi-year partnership | `FormsPattern → pat-value-of-judgement` **[registry]** | `OnElement → el-forward-deployed-engineering` **[registry]** |
| `sig-fde-as-cross-customer-advisor` | harness | The vendor-side information asymmetry, stated as a deliberate practice: Decagon **ingests a customer's historical support data and tells them which workflows to automate first for the highest ROI** — "and sometimes that's not actually what the customer had reached out about". Because an FDE sees the same problems repeat across every customer in a vertical, the role is "an advisor rather than just an executor" (it is both), and that earned advisory position is named as one of three reasons the company won its market position | `FormsPattern → pat-value-of-judgement` **[registry]** | `OnElement → el-decagon-agent`, `el-fde-role-specialization` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-productize-or-drown` | An embedded delivery motion only scales if the field is a funnel into the product, not a queue of bespoke work: every manual FDE action is a defect, repeats are the signal (25 hand-built CRM integrations → build the integration builder), and the destination is configuration in natural language by the customer or the agent-building team. Measured this way, the health of an FDE org is the rate at which custom becomes self-serve — and the compounding runs in both directions, since knowledge shared across deployments improves the agent for customer B every time it meets customer A | `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-custom-to-self-serve`, `el-decagon-agent` |
| `ins-restraint-over-velocity` | When coding agents make the one-off fix nearly free, the binding constraint moves from *writing* the code to *deciding whether it should exist*. Seniority in a forward deployed org is therefore measured in refusals and in generalization — architecting one customer's ask so the next four inherit it — and in front-loaded requirements work that would have been wasted effort when implementation was the expensive step. The failure mode is not slowness but a brittle per-customer black box that neither side can own | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-forward-deployed-engineering` **[registry]**, `el-custom-to-self-serve` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-rekhi-decagon-fde`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-scope-enterprise-agent-deployment` | Scope on written success criteria, then prove value before you expand | Define success in the *first* conversations, not after kickoff: which metrics, which channels (phone, email, text, WhatsApp), what the pain point is, what the ideal outcome looks like — and get it in writing so there is no miscommunication later. Resist the urge to start building; with cheap code the up-front alignment is now the expensive, valuable part. Assume a Fortune 500 will hand you the whole kitchen sink, so pick the narrowest thing that demonstrates value fast rather than accepting a multi-month time-to-value; land on deflecting the complex inbound work humans do today, then expand into revenue-generating workflows once your integrations are in place. Staff industry experts who have already delivered in that vertical so the customer hears their own lingo and the ramp is short; target every deployment being faster than the last | `ReferencesElement → el-decagon-agent`, `el-fde-role-specialization`, `el-forward-deployed-engineering` **[registry]** |
| `how-upstream-field-work` | Run the field as a funnel into the product, and exercise restraint at its mouth | Treat every manual action an FDE takes as something that must be upstreamed; count repeats and act on them (after ~25 hand-built CRM integrations, build the self-serve integration builder instead of the 26th). When a customer asks for something now, do **not** hand it to a coding agent as a one-off — ask how it scales to the customers who will ask in two weeks, and architect so they inherit it; a black box of prompts and patches is too brittle for a product the customer is supposed to own. Push the endpoint toward configuration in natural language so the rest of the business, not only engineers, can serve the ask. Share knowledge across deployments rigorously so the agent compounds with every customer interaction, and use the cross-customer vantage to advise (ingest historical support data, tell them what to automate first for ROI) rather than only execute | `ReferencesElement → el-custom-to-self-serve`, `el-decagon-agent`, `el-claude-code` **[registry]**, `el-codex` **[registry]** |

## Dropped

- **Hertz** — the land-and-expand exemplar (inbound support deflection first, then proactive lease-renewal outreach on the same integrations). Retained inside `el-decagon-agent`'s brief; no company node, consistent with how customer logos are handled elsewhere in the corpus.
- **Founder-age colour** ("started by folks in their late 20s, now early 30s") and the two hiring plugs with the speaker's email — no nodes.
- The **three reasons Decagon won** framing (move fast deal-by-deal; earned advisor trust; productize custom work) — split across `sig-fde-as-cross-customer-advisor` and `ins-productize-or-drown` rather than coined as its own element.
- **Natural-language agent configuration** as a standalone element — it is a property of `el-decagon-agent` and the endpoint of `el-custom-to-self-serve`; a separate node would duplicate both.
- The password-reset / back-end-action example and the brand-tonality/voice configuration list — illustrations folded into `el-fde-role-specialization`.

## Review notes

1. **Caption garbles (heavy, company name).** "Decagon" survives correctly only twice; elsewhere it is rendered **Degagon, Deckagon, Deck, Decky on, deciagon, Akkio gone** — all one company, resolved from the correctly-spelled instances and the talk title. The speaker's contact address is garbled in both renderings (`sunny@degagon.ai`, `sunny@deciagon.ai`) and is deliberately not recorded. "forward deployment engineering" and "forward deployed engineering" alternate; FDE/FTE alternate as in every talk of this batch. No other names are at risk in this file.
2. **`sig-decagon-fde-equals-product-eng` held pattern-less on purpose.** "FDE is identical to product engineering, same bar, same reporting structure" is the operational form of the cluster's un-coined thesis, and it sits *between* the two framings this batch disagrees about — Meurer's convergence claim and Ganesh's product-strategy claim. Rehome it if an FDE pattern is coined; do not force it onto `pat-saaspocalypse`, which would read it as a pricing/market claim it does not make.
3. **Title check.** "CTO of Forward Deployed Engineering" is what the transcript says and is an unusual construction (a functional CTO rather than the company CTO); worth verifying against the official listing before public-facing use, though it is stated clearly and is not a caption artifact.
4. **`pat-saaspocalypse` fit for `sig-decagon-hypergrowth-role-split`.** The link assumes the pattern covers the delivery-model shift (software sold as co-built, staffed outcomes) and not only the market-value collapse. Same caveat the Brunet file raised in batch 5; if you read the pattern strictly, this signal is the second candidate to hold pattern-less alongside note 2.
5. **Cross-file convergence worth noting at reconciliation.** `el-custom-to-self-serve` (here) and `el-fde-as-product-strategy` (`ganesh-kepler-fde.md` **[this batch]**) are the same mechanism argued from opposite ends — Decagon productizes *after* the field work as a scaling discipline, Kepler insists the field work exists *only* to produce product. They are not duplicates (one is an ops discipline, one is a strategic claim about what the function is for) but a `UsesElement` edge between them would be defensible at seeding.
6. **Signal bar.** The 50 → 500 headcount figure and the ~25-integrations threshold are the only hard numbers; the rest is named-practitioner testimony about an operating model, the standard this corpus has accepted for operator talks. If tightening, `sig-requirements-gathering-returns` is the first to demote — its content survives in `how-scope-enterprise-agent-deployment`.
