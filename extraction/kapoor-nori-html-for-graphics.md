# SPIKE extraction — "HTML is All You Need (for Agents to Make Graphics)" (Amol Kapoor, Nori) — FOR REVIEW

Source transcript: `transcripts/kapoor-nori-html-for-graphics.txt` (auto-captions — quotes are paraphrases, not verbatim). Short talk (~1.1k words).
Video: https://youtu.be/JRTAtZ5iBkU — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact and all signals: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
NOTE (review 2026-07-22): `pat-html-native-medium` was demoted to element `el-html-native-medium` (defined in `russo-heygen-html-all-agents-need.md`); this file's pattern edges are rehomed to `pat-model-not-bottleneck` per the pre-written fallback.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-kapoor-html-graphics` | HTML is All You Need (for Agents to Make Graphics) (Amol Kapoor, Nori — AI Engineer World's Fair) | youtube | https://youtu.be/JRTAtZ5iBkU |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-amol-kapoor`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-amol-kapoor` | Amol Kapoor (CEO of Nori) | `AffiliatedWithCompany → co-nori` |

## Companies (1 new)

| slug | name | type | brief |
|---|---|---|---|
| `co-nori` | Nori | developer | Deploys an "AI employee" that understands the company — code, docs, Slack, call transcripts, email — and produces work artifacts (decks, docs, videos) end to end; captions render the name as "Nori Atentic" (see Review notes) |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-nori-sessions` | Nori Sessions | product | harness | Nori's agent workspace for producing visual artifacts (board/sales decks, docs, videos) end to end: the agent reads company data for content and authors the artifact as HTML/CSS, rendering to the delivery format last; pitched as "build a board deck from your phone on the subway" |
| `el-pelican-bicycle-test` | Pelican-on-a-bicycle test | concept | harness | Simon Willison's (`exp-simon-willison` **[registry]**) informal spatial-reasoning gut check: ask every new model to draw a pelican riding a bicycle, but only in SVG; outputs are famously bad — used in this talk as the control case that the failure is the medium (handwritten coordinate soup) rather than model reasoning, since the same task in HTML produces a structured, readable, themeable result |

Element edges: both `IdentifiedInArtifact → ia-aie-kapoor-html-graphics`; `el-nori-sessions` `DevelopedByCompany → co-nori`; `el-nori-sessions` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]** (rehomed); `el-nori-sessions` `UsesElement → el-html-native-medium` [russo file].

## Signals (3 new — short talk)

All: domain `harness`, `SpottedInArtifact → ia-aie-kapoor-html-graphics`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | Pattern edges | RelevantCompany |
|---|---|---|---|
| `sig-nori-html-artifacts-production` | Nori runs its real artifacts as agent-written HTML in production: actual board decks, sales decks, docs, and marketing videos ("literally just divs all the way down") built end to end by coding agents from company data (call transcripts, email); claim: a 10-hour deck is really ~25 minutes of thinking once formatting/branding fiddling is removed — against a world pouring "~34,000 human years a day" into slides | `FormsPattern → pat-model-not-bottleneck` **[registry]** (rehomed) | `RelevantCompany → co-nori` |
| `sig-pelican-svg-vs-html` | Same model, same pelican, different medium: frontier models fail Willison's SVG pelican test (a wall of numbers no human could handwrite either), but asked for the same bird in HTML they succeed — structure the model can reason about, every line readable/theme-able/editable; presented as evidence against the "agents fundamentally can't reason about space" claim baked into benchmarks like ARC-AGI | `FormsPattern → pat-model-not-bottleneck` **[registry]** ("it's not the model, it's the medium"; carries the rehomed edge too) | — |
| `sig-canvas-tools-fail-agents` | Handing agents human canvas tools fails structurally: PowerPoint/Slides/Figma/Canva are built for human hands and eyes (click, drag, snap-to-grid) with data structures only the app can read; agent output through them — including Figma MCPs, PowerPoint CLIs, screenshot-and-replace loops — comes out as garbage (overlaps, invisible text, no alignment) because every such tool "approaches the problem like a human" | `FormsPattern → pat-model-not-bottleneck` **[registry]** (rehomed) | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-editing-format-arbitrary` | The audience only ever sees the presentation mode; the editing format is invisible and therefore arbitrary — "slide deck" and "PowerPoint" are not synonyms. So pick the editing format agents are natively fluent in (HTML) and render to the human delivery format (PDF, PPT, MP4) as the last step; the tool-for-making-X and X itself decouple | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** (rehomed) | `ReliesOnElement → el-nori-sessions`, `ReliesOnElement → el-html-native-medium` |
| `ins-medium-not-model` | Asking an AI to use a canvas is like asking a human to handwrite SVG — capability verdicts are artifacts of the medium: "think like the model" (tokens, language, structure) rather than "think like a user" (pixels, coordinates), and abilities that benchmarks score as absent (spatial layout) appear, with the browser doing the geometry so the model never places a coordinate | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-pelican-bicycle-test` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-kapoor-html-graphics`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-agent-visual-artifacts-html` | Make visual artifacts with coding agents via HTML | Don't hand agents canvas tools or screenshot-replace loops — have them author HTML/CSS so the browser does layout and the model never places coordinates; keep the artifact readable/theme-able as text; wire the agent into company data (transcripts, email, docs) so it populates content end to end — a beautiful empty deck is worth nothing; render/export to the delivery format (PDF, deck, video) last; treat plain text as a choice of convenience — add structure and color when the artifact matters | `ReferencesElement → el-nori-sessions` |

## Dropped

- ARC-AGI — one-line mention as the benchmark family built on "agents can't reason about space"; prose inside `sig-pelican-svg-vs-html`, no element.
- PowerPoint, Google Slides, Figma, Canva, Figma MCP, PowerPoint CLIs — named as the failing human-tool class; folded into `sig-canvas-tools-fail-agents` (no edge to `el-mcp` **[registry]** — passing mention).
- "Nori bot lives in the fabric of our company" — marketing framing, folded into company brief and Review note 4.

## Review notes

1. **Company-name garble:** captions open with "CEO of Nori Atentic" — official listing says just "Nori" (possibly "Nori Agentic" garbled). Coined `co-nori` per the official title; flag for verification before public-facing use.
2. **RESOLVED at review 2026-07-22 — coin rejected centrally; edges rehomed to `pat-model-not-bottleneck` as this note anticipated.** Original note: this talk independently states the same thesis as Russo/HeyGen (the two titles are near-identical); per the two-talk rule the pattern `pat-html-native-medium` is coined once, in `russo-heygen-html-all-agents-need.md`, and this file's signals evidence it. If review rejects the coin, these edges rehome to `pat-model-not-bottleneck`.
3. `el-pelican-bicycle-test` is a third-party informal benchmark (Simon Willison's; he's `exp-simon-willison` **[registry]** but there is no Element→Expert edge type — attribution lives in the brief). Coined because the HTML-vs-SVG contrast is the talk's load-bearing evidence.
4. **Candidate-pattern evidence (not coined, noted per central ledger):** soft resonance with `pat-ai-native-org` — an "AI employee" living in company data, CEO shipping real board decks from a phone; weak/one-liner, noted only, no edge.
5. The 34,000-human-years/day and 10-hours→25-minutes figures are speaker assertions with no cited source — treat as rhetoric-grade claims.
