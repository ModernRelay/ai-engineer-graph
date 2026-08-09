# SPIKE extraction — "GTM Is You" (Victoria Melnikova, Evil Martians) — FOR REVIEW

Source transcript: `transcripts/melnikova-evil-martians-gtm-is-you.txt` (auto-captions — quotes are paraphrases, not verbatim; talk embeds podcast interview clips).
Video: https://youtu.be/G6IlDzj8OjA — AI Engineer World's Fair, published 2026-07-07.
`stagingTimestamp` for the artifact and all signals: 2026-07-07 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-melnikova-gtm-is-you` | GTM Is You (Victoria Melnikova, Evil Martians — AI Engineer World's Fair) | youtube | https://youtu.be/G6IlDzj8OjA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-victoria-melnikova`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-victoria-melnikova` | Victoria Melnikova (head of new business, Evil Martians; hosts the Dev Propulsion Labs podcast on the business of developer tools) | `AffiliatedWithCompany → co-evil-martians` |

Quoted founders (interview clips) deliberately **not** coined as Experts — no artifact-contribution or affiliation edges would be load-bearing: Sam Lambert (PlanetScale CEO), David Cramer (Sentry founder — `co-sentry` **[registry]**), the Typesense founder, a Supabase voice, Zeno Rocha (garbled as "Zen Rocha"), and an unnamed founder who restarted from $300K ARR. Kept in signal/knowhow prose; see notes.

## Companies (3 new)

| slug | name | type | note |
|---|---|---|---|
| `co-evil-martians` | Evil Martians | developer | Consultancy for developer-tools companies; blog with ~500K technical readers/year; built the "PMF compass" from analyzing 37 successful devtools |
| `co-planetscale` | PlanetScale | developer | Database (MySQL-platform) company; appears via CEO Sam Lambert's founder-brand customer-acquisition anecdote |
| `co-typesense` | Typesense | developer | Open-source search engine company, bootstrapped/non-VC-backed; ran SF billboard campaigns as a credibility signal |

Also referenced: `co-sentry` **[registry]** (David Cramer's "SF is unfair" quote), `co-y-combinator` **[registry]** (post-YC stay-in-SF fundraising claim). Supabase (garbled "Superbase"; user-conference example) deliberately not coined — passing example.

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-pmf-compass` | Product-market-fit compass | concept | — | Evil Martians' diagnostic framework derived from analyzing 37 successful devtools: two axes, product signal vs revenue; signal > revenue → fix distribution; revenue > signal → fix product; equal → full speed ahead. Used to triage early-stage devtools GTM |
| `el-founder-led-gtm` | Founder-led GTM / personal brand as moat | concept | — | Go-to-market motion where the founder's personal brand and founder-led sales are the primary distribution channel: undelegatable authenticity, quirks as "genius zone", trust built by a real human behind the product; AI amplifies the founder's signal (text, video) but cannot replace it |

Element edges: both `IdentifiedInArtifact → ia-aie-melnikova-gtm-is-you`; `el-founder-led-gtm` `ExemplifiesPattern → pat-value-of-judgement` **[registry]**.

## Signals (4 new)

All: no domain set (GTM/business observations — none of the domain enum values apply), `SpottedInArtifact → ia-aie-melnikova-gtm-is-you`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-planetscale-founder-account` | Summer 2026, PlanetScale's new SF office: CEO Sam Lambert tells Melnikova "you would be shocked if I told you how many customers we get from my own [Twitter] account" — and refuses to delegate it ("my literal favorite thing to do"); founder distribution as measurable pipeline at a scaled devtools company | `FormsPattern → pat-value-of-judgement` **[registry]** (resonance read — see notes) | `RelevantCompany → co-planetscale` |
| `sig-distribution-is-bottleneck` | Evil Martians' PMF-compass data (37 successful devtools analyzed; early-stage client base): 9 of 10 early-stage devtools show product signal stronger than revenue — distribution, not product, is the binding constraint in 2026; "building software has never been easier, which means the bottleneck has moved" (and technical founders hate marketing) | `FormsPattern → pat-value-of-judgement` **[registry]** | `OnElement → el-pmf-compass`; `RelevantCompany → co-evil-martians` |
| `sig-slop-saturated-channels` | 2026: AI has made inboxes and feeds nearly unusable for GTM — "so much annoying outreach and generated slop that it's really hard to tell the real deal" — and cutting through the noise now drives founders to re-anchor trust in humans: personal brands, artisanal craft, beautiful design/text, as the pendulum swings back from automation | `FormsPattern → pat-verification-gap` **[registry]** (resonance read — see notes) | — |
| `sig-costly-signaling-returns` | Expensive physical GTM signals are back for devtools: Typesense (bootstrapped, no funding milestones to announce) ran hundreds of SF billboards explicitly as a credibility proxy ("I didn't realize you were this big"); SF banner culture (Muni buses, buildings, highways) plus a rising norm of early-stage startups hosting their own user conferences (Supabase's, year two, cited as the model) | — (pattern-less; see notes) | `RelevantCompany → co-typesense` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-personal-brand-moat` | "It's not your model, not your team, not your funding — it's you": as AI amplification compounds through 2026→2030, the founder's personal brand is the moat — AI can amplify your signal but cannot replace your authenticity; people want to buy from a real human, which is why founder-led sales remains the main early-stage motion and why it cannot be delegated | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-founder-led-gtm` |
| `ins-artisanal-premium` | Slop saturation inverts marketing economics: precisely because generated content is free, the artisanal carries the trust premium — craft, beautiful design and text, physical presence (SF, billboards, events), and even public failure with an elegant recovery all work because they are hard to fake and audiences can no longer tell the real deal in cheap channels | `HighlightsPattern → pat-verification-gap` **[registry]** | — |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-melnikova-gtm-is-you`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-devtools-gtm-foundation` | Lay the devtools GTM foundation (six hygiene steps + compass triage) | Crystallize the value proposition around a painful problem and validate it with *paying* customers; understand your shelf space in the developer's life; derive channels from that shelf space and become the authority on the problem; friend the ecosystem and cross-pollinate; know your foes so you can differentiate; distribute early — sometimes before the product is ready. Triage with the PMF compass: product signal > revenue → work distribution; revenue > signal → work product; equal → full speed | `ReferencesElement → el-pmf-compass` |
| `how-founder-brand-playbook` | Build the founder-brand distribution engine | Get to SF — clients, friends, and VCs in person ("SF is unfair — just do it," per Sentry's David Cramer; post-YC stayers claimed to fundraise ~2× as much, ~2× as fast); get loud: banners/billboards as signaling + subconscious mindshare (and, for bootstrapped companies, credibility proxy); run the events ladder — paddle/poker/breakfast/boba → meetups → launch parties → your own user conference; do memorable stunts (open a café, brand coffee, name an ice cream) — fun marketing shows; share failures openly, people love a fail story with an elegant recovery; be unapologetically you — turn quirks into your genius zone and use AI to amplify your personal signal (text, video) at personal and brand level; lean on founder-led sales, because that is how trust is built | `ReferencesElement → el-founder-led-gtm` |

## Dropped

- Dev Propulsion Labs podcast as a SourceEntity — the talk quotes its interviews, but the artifact here is the AIE talk; podcast kept in the expert brief.
- "Come to San Francisco" as its own Signal — advice, not an observation of change; folded into `how-founder-brand-playbook` (the YC 2×-fundraising stat is an unverified community claim).
- The $300K-ARR restart interview clip — founder unnamed in captions; folded into the playbook's fail-story guideline.
- Supabase user conference, PlanetScale office party details — prose color.

## Review notes

1. **Pattern mapping is the judgment call of this file (flagged per instructions, nothing coined):** the talk's thesis — execution commoditized ("building software has never been easier"), durable edge migrates to the undelegatable human (brand, taste, authenticity) — *resonates with* `pat-value-of-judgement` but stretches it from judgment/verification to authenticity/distribution. I linked the two strongest-fit signals and both thesis insights there rather than coining anything ("AI-native GTM" / "authenticity premium" would be one-talk patterns). If the central view is that this over-broadens the pattern, cut `FormsPattern` from `sig-planetscale-founder-account` and re-home `ins-personal-brand-moat`.
2. `sig-slop-saturated-channels` → `pat-verification-gap` is likewise a resonance read: generation industrialized (outreach slop), verification didn't (buyers can't tell the real deal), trust re-architected outside the generated channel (onto humans/costly signals). Same shape, new arena (GTM rather than code). Flag if verification-gap should stay artifact/code-scoped.
3. `sig-costly-signaling-returns` left pattern-less — closest existing home would also be verification-gap (costly signaling as trust restoration), but one resonance-stretch per file felt like the limit; reviewer may add the edge.
4. **Caption garbles:** "unpairable" = *unbearable*; "founders here in **NASSCOM**" — unresolved (context suggests "in the last year" or a venue name; NASSCOM the Indian trade body makes no sense here); "**Superbase** Select" = *Supabase* (their user-conference name as captioned — verify "Select"); "**Type Sense**" = *Typesense*; "**Zen Rocha**" = *Zeno Rocha*; "fly a banner over **a sub** / I love **a sub**" = likely *over SF / I love SF*.
5. Quoted founders not coined as Experts (schema has no Signal→Expert edge, so nodes would be orphan-ish); if the reviewer wants Sam Lambert as an Expert given the anecdote's weight, add `exp-sam-lambert` + `AffiliatedWithCompany → co-planetscale`.
6. The "37 successful devtools" PMF-compass analysis is Evil Martians' proprietary claim ("a mathematical formula") — not externally verifiable.
