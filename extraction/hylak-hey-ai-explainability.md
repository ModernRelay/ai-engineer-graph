# SPIKE extraction — "Your AI Product Will Fail Unless You Can Explain It" (Veronica Hylak, Hey AI) — FOR REVIEW

Source transcript: `transcripts/hylak-hey-ai-explainability.txt` (auto-captions — quotes are paraphrases, not verbatim; speaker renders as "Veronica Hylick").
Video: https://youtu.be/d_Ftrl3vfV0 — AI Engineer World's Fair, published 2026-07-05.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-07-05 (publish date).
Entities marked **[registry]** already exist — edges link to them, no new node.

Very short talk (~960 words) — extraction kept deliberately lean: 2 signals, 1 knowhow, 0 insights, 0 elements.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-hylak-explain-it` | Your AI Product Will Fail Unless You Can Explain It (Veronica Hylak, Hey AI — AI Engineer World's Fair) | youtube | https://youtu.be/d_Ftrl3vfV0 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-veronica-hylak`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-veronica-hylak` | Veronica Hylak (Hey AI; AI explainer videos with 8M+ views; has helped YC startups, safety orgs, and AI teams with product storytelling) | `AffiliatedWithCompany → co-hey-ai` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-hey-ai` | Hey AI | media | Veronica Hylak's AI-explainer / product-storytelling outfit; named only in the official talk listing, never in-transcript — brief inferred from her self-description (see notes) |

## Elements (0 new)

None — "Devin, the AI software engineer" and "smoke alarm for AI behavior" are cited as exemplars of picturable naming, not discussed as products.

## Signals (2 new)

All: `SpottedInArtifact → ia-aie-hylak-explain-it`, `SourcedFromSource → source-aie-yt` **[registry]**. Domain: unset (go-to-market topic; no enum fit).

| slug | domain | name / brief | pattern edge | RelevantCompany |
|---|---|---|---|---|
| `sig-ai-pitch-attention-collapse` | — | Buyer attention for AI pitches has collapsed to roughly an elevator ride, and the category vocabulary is spent: "agentic AI orchestration platform for enterprise knowledge retrieval" — a real pitch she recently heard from a series-B startup — no longer registers at all; layering qualifiers ("agents talking to agents in a multi-agent workflow") makes it worse; AI products are failing on explanation, not technology | — (see notes) | — |
| `sig-clearest-story-gets-funded` | — | Distribution-shift claim from an AI-storytelling practitioner: 15 years ago a great product might be found organically; in the crowded 2026 AI market the clearest-story products are the ones getting funded, bought, and talked about — "great tech that nobody understands dies quietly" (paraphrase) | — (see notes) | — |

## Insights (0 new)

None coined — the talk's substance is method (captured as KnowHow); no registry pattern covers go-to-market storytelling, and a mandatory `HighlightsPattern` edge would have to be forced.

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-hylak-explain-it`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-wound-click-transformation` | Explain an AI product in an elevator: wound → click → transformation | (1) **Wound** — never open with what you built; immerse the buyer in their day-to-day pain moment ("alerts in one system, tickets in another, the real investigation buried in Slack threads and screenshots"), then "we fix that", then how — all in ~20 seconds. (2) **Click** — pass the 17-year-old test; anchor to viral stories the buyer already knows (the McDonald's AI drive-thru putting bacon on ice cream → "if McDonald's had used us, that clip never makes TikTok: we catch agents going off script before it's a PR nightmare"); ban words nobody can picture; hand them a mental image instead ("Devin, the AI software engineer", "a smoke alarm for AI behavior") — imperfect technical definitions are fine as front doors, precision comes later in the sale. (3) **Transformation** — prove value as concrete before/after ("support spends 30 minutes digging through docs and tickets → asks one question, gets the answer in 10 seconds with sources"), never abstract benefit claims ("we improve code quality with AI") | — |

## Dropped

- The opening buyer skit / elevator framing device and closing audience CTA.
- The McDonald's drive-thru fiasco as a *signal* — it's referenced as years-old shared cultural shorthand, not reported; kept inside the knowhow.
- "Devin" — exemplar mention only; no element or company node coined.

## Review notes

1. **Both signals left pattern-less** (allowed per corpus precedent, e.g. the raskar file): no registry pattern covers GTM/product-storytelling. They read as a second soft data point for the batch-3 "AI adoption/UX gap" candidate (nanz) — the buyer-side comprehension gap as the adoption bottleneck, here at the pitch/funding layer. Noted, not coined, no edges.
2. **Company thinness:** "Hey AI" appears only in the official talk title; the transcript self-description is "built products, made AI explainers that have hit 8 million views, helped YC startups, safety orgs, and AI teams". Type `media` chosen; verify the company's site before seeding, or fall back to affiliation-less expert if reviewers prefer.
3. **Garble:** captions render the speaker "Veronica Hylick"; official listing "Veronica Hylak" used.
4. Signals are practitioner testimony from a marketing vantage, with the series-B pitch anonymized. If that fails the signal bar, fallback is 1 signal (`sig-clearest-story-gets-funded`) + the knowhow.
