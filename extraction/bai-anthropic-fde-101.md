# SPIKE extraction — "Forward Deployed Engineering 101" (Kevin Bai, Anthropic) — FOR REVIEW

Source transcript: `transcripts/bai-anthropic-fde-101.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/KwhgfwOSToQ — AI Engineer World's Fair, published 2026-07-28.
`stagingTimestamp` for the artifact and all signals: 2026-07-28T00:00:00Z (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node. **[this batch]** = defined in another file of this 4-talk FDE set.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-bai-fde-101` | Forward Deployed Engineering 101 (Kevin Bai, Anthropic — AI Engineer World's Fair) | youtube | https://youtu.be/KwhgfwOSToQ |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-kevin-bai`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-kevin-bai` | Kevin Bai (member of technical staff, applied AI team, Anthropic — "technically we don't really have titles"; earlier the first hire on Rippling's FDE team, grown to ~25 in a year; before that Palantir) | `AffiliatedWithCompany → co-anthropic` **[registry]** |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-palantir` | Palantir | developer | Coined here: load-bearing subject of the talk (Foundry, the FDE origin story, the ACV numbers), not a passing reference. Reused by `reyes-factory-fde.md`. Founded ~2004–05 per the talk |

Also referenced, no node: Rippling, Jira, Slack, GitHub, Datadog, AWS/DynamoDB, ServiceNow, Workday — all named as quadrant or primitive-granularity examples only (`co-github` **[registry]** exists but the mention is illustrative; no edge).

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-palantir-foundry` | Palantir Foundry | product | data-eng | App-building data platform: centralizes an organization of arbitrary size's data in one place and builds an "ontology" — proper nouns out of data, so instead of table one/two/three there is a single source-of-truth `warehouses` table — then lets the company build applications on top. Because value is gated on the customer's ability to build with it (a licence cost *plus* a training tax), Foundry is sold with engineers attached rather than as software alone |
| `el-outcome-as-the-product` | Outcome as the product | concept | — | Selling products and services as one combined thing: the customer buys neither a software licence nor someone's time, they buy a business outcome (shelf placement, sales throughput). Industry buyers do not care how the data is organized — "that's an implementation detail" — so the vendor absorbs the implementation and is paid for the result |
| `el-shared-primitives-platform` | Shared-primitive platform (the FDE precondition) | concept | — | The line between an FDE function and a dev shop: FDEs assemble solutions from a shared set of platform primitives and never write software from scratch. Without it, per-customer bespoke code compounds into unmaintainable sprawl ("55 repos"), maintenance costs "eat your P&L alive", and the engineers quit. Primitive granularity is a function of customer breadth — some platforms ship apps 60% built with 40% customized, others (AWS/DynamoDB) offer extremely granular primitives to serve a broad swath |

Element edges: all three `IdentifiedInArtifact → ia-aie-bai-fde-101`; `el-palantir-foundry` `DevelopedByCompany → co-palantir`; `el-outcome-as-the-product` `ExemplifiesPattern → pat-saaspocalypse` **[registry]**; `el-shared-primitives-platform` `EnablesElement → el-forward-deployed-engineering` **[registry]**; `el-forward-deployed-engineering` **[registry]** `IdentifiedInArtifact → ia-aie-bai-fde-101` (this is the track's definitional talk — reused, not re-coined).

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-bai-fde-101`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-fde-quadrant-origin` | Anthropic applied-AI engineer (ex-Palantir, ex-Rippling) gives the track's definitional framing: FDE is not a general upgrade to go-to-market, it is the answer to one quadrant of {how technical is what you sell} × {how technical is who buys it}. Technical product + technical buyer (GitHub, Datadog) → DevRel/developer engagement; simple-or-configurable product + non-technical buyer (Rippling, Jira, Slack) → sales-led SaaS; **only** technical product + non-technical buyer (Foundry into a Fortune 500 oil-and-gas company whose "pipelines are not data pipelines") needs FDE | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-forward-deployed-engineering` **[registry]**, `el-palantir-foundry`; `RelevantCompany → co-palantir` |
| `sig-palantir-acv-outlier` | Numbers offered as evidence the motion works: among public SaaS companies in the Fortune 500 ranked by average contract value, Palantir is first at ~$4M ACV, ServiceNow next at ~$1.2M, Workday ~$600K, and no other public SaaS company cracks half a million — reached at only a few thousand headcount | `FormsPattern → pat-saaspocalypse` **[registry]** | `RelevantCompany → co-palantir`; `OnElement → el-outcome-as-the-product` |
| `sig-design-partnership-at-enterprise-scale` | FDE defined as the early-startup design partnership ("give me your context, I'll build you a really good solution" — how most B2B startups find PMF) scaled up into the enterprise, with one non-negotiable condition: if each FDE builds from scratch you do not have an FDE function, you have a dev shop. The differentiator is building on top of a platform of shared primitives | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-shared-primitives-platform`, `el-forward-deployed-engineering` **[registry]** |
| `sig-agentic-platforms-force-fde` | The 2026 thesis, stated as personal hypothesis: what changed since Palantir's 2004-era motion is not that the industry recognized it was a good idea — it is that **nearly every platform is now agentic, therefore nearly every platform is customizable**, therefore nearly every vendor now has customers who "have no idea what the heck it is that you actually do". Leaving success to the customer's ability to implement makes up-market, horizontal and vertical expansion fail | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-forward-deployed-engineering` **[registry]**, `el-outcome-as-the-product`; `RelevantCompany → co-anthropic` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-buy-the-outcome-not-the-tool` | Selling only technology fails at the last mile: you have organized the buyer's data, but the buyer asks "what does that do for my actual business?" Selling only services is a dev shop. The working configuration is both at once — smart engineers who learn the customer's business and assemble a solution on the vendor's platform — so what changes hands is an outcome, with the software as implementation detail. The fine-dining analogy: the waiter caters to your every need and figures out the problem for you | `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-outcome-as-the-product`, `el-palantir-foundry` |
| `ins-need-not-want-an-fde-function` | The advice Bai gives everyone considering FDE: ask whether you *need* one, not whether you want one — it is easy to want what is in vogue. Two qualifying questions: do you have to sell something technically complicated to a non-technical buyer, and do you have (or will you invest in) a platform of shared primitives for FDEs to build on? A "no" to either means DevRel or a sales-led motion instead; a "yes" to the first and "no" to the second guarantees a maintenance burden that outruns the revenue | `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-forward-deployed-engineering` **[registry]**, `el-shared-primitives-platform` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-bai-fde-101`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-qualify-fde-function` | Qualify (and platform-back) an FDE function before you build one | Need, not want: only build FDE if you must GTM a technically complicated product to a non-technical buyer — otherwise run DevRel (technical buyer) or sales-led SaaS (simple product). Second gate: have a platform, or commit to building one; FDEs must assemble from shared primitives, never write from scratch. Set primitive granularity by customer breadth — some domains tolerate apps that ship 60% built with 40% customization, others need extremely granular configuration and tooling (AWS is the reference point). Keep anything bespoke to a single customer with that customer; generalize anything generalizable over time. Expect thin primitives at the start — that is fine, FDE also scouts which products to build next | `ReferencesElement → el-forward-deployed-engineering` **[registry]**, `el-shared-primitives-platform` |
| `how-staff-fde` | Staff FDEs as customer-facing software engineers | The whole profile in one line: "an FDE is nothing more than a customer-facing software engineer" — someone you would hire as a software engineer on your team *and* trust in front of a customer; the rest is figured out as you go. Do not run one FDE per account: multiple FDEs on a project is an encouraged pattern because bespoke customer work otherwise creates a single point of failure (one person holds all the context, goes on vacation, you are stuck). Cross-company FDE collaboration works like any contractor relationship — establish who the contractor is | `ReferencesElement → el-forward-deployed-engineering` **[registry]** |

## Dropped

- "Ontology / proper nouns out of data" — kept inside the `el-palantir-foundry` brief rather than edged to `el-ontology-semantic-layer` **[registry]** (Neo4j, batch 10); Bai's usage is Palantir-specific product vocabulary, and asserting the equivalence would be our inference, not his claim. See review note 3.
- Rippling as a company node — appears twice (Bai's FDE build-out there, and as a "configurable tool sold to a non-technical buyer" example) but carries no signal of its own; kept in the expert brief and signal prose.
- ServiceNow / Workday / GitHub / Datadog / Jira / Slack / AWS — comparison points inside signals; no nodes.
- Q&A on "what goes on the platform vs the forward-deployed side" — folded into `how-qualify-fde-function`.

## Review notes

1. **Caption garbles.** "Palunteer"/"Palanteer"/"Palanteer" = **Palantir** throughout; "Ripling" = **Rippling**; "FTE" and "FDE" alternate freely in the captions and all mean **forward deployed engineer** (no full-time-equivalent reading fits any occurrence); "punit square" = **quadrant / 2×2**; "hurting a whole bunch of cats" = **herding cats**; "DynamoB" = **DynamoDB**; "Devril" = **DevRel**; "SAS" = **SaaS**; "balance is first at 4 million" = **Palantir is first**. The ACV figures are spoken from memory ("last I checked") — treat as approximate.
2. **Domain enum.** All four signals tagged `harness` following the `brunet-cursor-forward-deployed.md` precedent for FDE signals; the honest answer is that FDE is a go-to-market/delivery topic the enum has no slot for. `sig-palantir-acv-outlier` in particular is a business-model fact, not a harness fact — drop its domain to null if you would rather not overload the enum.
3. **`el-palantir-foundry` vs `el-ontology-semantic-layer` [registry].** Both describe a curated canonical layer over raw tables. Not edged (see Dropped); if you want the lineage, `el-palantir-foundry` `UsesElement → el-ontology-semantic-layer` is the edge to add at seeding.
4. **`el-outcome-as-the-product` merge-check** against `el-done-as-object` **[registry]** (batch 5, Paperclip) — related in spirit ("what changes hands is completed work") but Dotta's is about agent liveness/task objects and this is about a commercial sale. Kept distinct.
5. **`pat-saaspocalypse` load.** All four signals home there. This talk is the strongest single statement in the corpus of the seed pattern's "services is the new software" leg — Sequoia's thesis restated by an ex-Palantir practitioner with ACV numbers attached. If the registry brief reads `pat-saaspocalypse` narrowly as "SaaS businesses collapsing" rather than "the delivery model of software is changing", these edges need rehoming (same caveat the Brunet file raised at batch 5).
6. **FDE-thesis proposal for central reconciliation** — see the identical note carried in all four files of this set: *agentic products are customizable without limit, so implementation has moved from the buyer to the vendor; shipping software now means embedding engineers who co-build, measure and prove the outcome, which turns go-to-market into a delivery-and-product-feedback function.* This talk is its clearest statement ("nearly every platform is agentic ⇒ nearly every platform is customizable ⇒ your customers have no idea what you do") and supplies the economic proof point (Palantir's $4M ACV against a field where nobody else clears $500K). Not coined — central reconciliation sees all eight FDE talks.
