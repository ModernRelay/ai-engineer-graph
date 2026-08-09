# SPIKE extraction — "Stop Writing Tone Instructions. Layer Them." (Isadora Martin-Dye, Isadora & Co) — FOR REVIEW

Source transcript: `transcripts/martin-dye-tone-layering.txt` (auto-captions — quotes are paraphrases, not verbatim; captions are rough — "layer" is consistently rendered "lad", see Review notes).
Video: https://youtu.be/ij-AU9dpJjc — AI Engineer World's Fair, published 2026-06-26.
`stagingTimestamp` for the artifact and all signals: 2026-06-26 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-martin-dye-tone-layering` | Stop Writing Tone Instructions. Layer Them. (Isadora Martin-Dye, Isadora & Co — AI Engineer World's Fair) | youtube | https://youtu.be/ij-AU9dpJjc |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-isadora-martin-dye`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-isadora-martin-dye` | Isadora Martin-Dye (owner-operator of a 225-year-old Virginia wedding venue; builds voice-critical AI products — venue agents, a companion app, a missing-persons family tool) | `AffiliatedWithCompany → co-isadora-and-co` |

## Companies (1 new)

| slug | name | type | brief |
|---|---|---|---|
| `co-isadora-and-co` | Isadora & Co | developer | Studio of wedding-venue operator Isadora Martin-Dye building AI products where voice is the product: Bloom (multi-tenant AI agent for wedding venues), Thread Light (public utility for families of missing people), and a personal AI companion app. ⚠ Company name from the official talk listing — never stated in the transcript |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-layered-voice-architecture` | Four-layer voice architecture | concept | harness | Splits brand voice into four separated jobs assembled in one place, in a fixed, load-bearing order: (1) immutable identity — hard rules and forbidden vocabulary nothing below can override; (2) situational mode — real-time conditions: who the user is (customer vs staff) and what they're going through (soft context notes used for tone, never quoted); (3) example-anchored voice — the tone guide/dials/phrase lists where most teams start and stop, trainable from staff edits; (4) post-generation veto. Replaced 24 ad-hoc system prompts scattered across one codebase with a single composition entry point; layer 1 is identical across tenants, 2–3 load per tenant |
| `el-post-generation-veto` | Post-generation veto | concept | harness | The only layer that reads what the model actually produced and can refuse to ship it — automated, cheap, and the only deterministic part of the stack. Two grades: soft flag (a regex "honesty inspector" — did it answer? did it hedge?) and hard reject (a numbers guard that blocks any date/figure/fact not in an allow-list). "Instructions are probabilistic; permission is deterministic." ⚠ merge candidates: `el-generator-validator-separation` **[registry, batch 1]**, `el-constrain-effects-not-expression` **[registry, batch 7]** |
| `el-bloom` | Bloom | product | harness | Multi-tenant AI agent for wedding venues (talks to couples, briefs coordinators) built on the four-layer stack; discloses that it is an AI in its very first response — before being asked; hard physical-presence boundary ("you are software; you do not have a body"); adjusts narration to engagement heat-maps read through soft human context. Product name inferred from "Every AI in Bloom discloses…" (see Review notes) |
| `el-thread-light` | Thread Light | product | harness | Public utility for families of missing people running the identical four-layer architecture with wildly different stakes: layer 1 forbids the words confirmed / identified / matched / proven / linked / solved — the statistically natural word ("match") said to a grieving family is the single most damaging output the product could emit. ⚠ name garbled in captions ("Thread Light" / "thread line") |

Element edges: all four `IdentifiedInArtifact → ia-aie-martin-dye-tone-layering`; `el-layered-voice-architecture` `UsesElement → el-post-generation-veto`; `el-bloom` and `el-thread-light` `UsesElement → el-layered-voice-architecture` and `DevelopedByCompany → co-isadora-and-co`; `el-layered-voice-architecture` `ExemplifiesPattern → pat-harness-over-model` **[registry]**; `el-post-generation-veto` `ExemplifiesPattern → pat-verification-gap` **[registry]**.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-martin-dye-tone-layering`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | Pattern edges | RelevantCompany |
|---|---|---|---|
| `sig-tone-prompt-fails-turn-21` | Voice-is-the-product operator (wedding venues; same class as luxury hotels, high-end real estate): the standard advice — a detailed brand-voice system prompt with examples — holds only on the happy path; on "turn 21", the first question the examples never covered, the model says something technically correct the brand would never say; where users pay for a relationship, one wrong sentence costs more than a refund, and one prompt is being asked to do four different jobs (situational, inviolable, expressive, self-checking) | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-isadora-and-co` |
| `sig-warm-voice-invented-dates` | The failure that forced a deterministic layer: the venue AI kept warmly offering wedding dates that were already booked — identity, mode, and voice layers all did their jobs; the voice, trained on what good service sounds like, confidently invented availability it was never given. Fix: a post-generation numbers guard that rejects any date/figure not in an allow-list, added because "a prompt will eventually lose" — a warm, confident voice offering something unreal is worse than a cold one (the couple believes they have a date; disappointment ships with a 48-hour delay) | `FormsPattern → pat-verification-gap` **[registry]** | `RelevantCompany → co-isadora-and-co` |
| `sig-multitenant-default-identity-leak` | Shipped multi-tenant bug: silently defaulted brand-identity fields made every venue's agent email as sage@[the flagship venue's domain] — a white-label leak where venues spoke in a stranger's voice and users just felt something was off. Resulting principle: in a multi-tenant agent system identity must never have a default — a missing brand identity is a crash (fail loud), not a fallback | — (no FormsPattern; see Review notes) | `RelevantCompany → co-isadora-and-co` |
| `sig-ai-disclosure-first-message` | Product bet on disclosure: every Bloom agent states it is an AI in its very first response — before being asked, as a product decision rather than a legal one — wagering that a couple who knows from the start trusts more than one who finds out on turn 7; paired with the physical-presence boundary (never "I'd love to show you around", always "the team would love to host you for a tour") because embodied warmth from a bodiless system is a lie, and when users notice, trust doesn't dip — it inverts | — (no FormsPattern; see Review notes) | `RelevantCompany → co-isadora-and-co` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-instructions-vs-permission` | The first three layers (identity, conditions, voice) are instructions — probabilistic requests to a system that usually complies; the fourth reads what actually came out and decides whether it may leave the business. Instructions are prompt engineering (asking nicely and hoping); permission is systems engineering (checking and being sure). One mechanism cannot simultaneously be inviolable, situational, expressive, and self-checking — pull the jobs apart and give each a layer built for it, and "turn 21" stops breaking | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-layered-voice-architecture` |
| `ins-veto-asymmetry` | The veto is the cheapest layer to build and the only deterministic one, and its error economics are asymmetric: a false positive costs someone double-checking a fine response; a false negative ships a hallucinated number or a privacy violation to a client. Prevention is the prompt, the veto is the check — you need both; stakes scale from mildly embarrassing (a venue AI implying it has a body) to catastrophic (a missing-persons tool saying "match" to a parent) | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-post-generation-veto` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-martin-dye-tone-layering`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-four-layer-voice-stack` | Compose agent voice as four ordered layers through one assembler | One entry point composes every surface's system prompt — kill scattered per-surface prompts (she found 24); order is load-bearing: hard identity rules first, task last; put brand-impossible statements and forbidden vocabulary in layer 1 where no voice warmth can reach them; layer 2 adapts to who the user is (customer vs coordinator get different candor on the same facts) and what they're going through (soft context notes shape tone — gentleness for grief, slack for a sick parent — and are never quoted verbatim); render human soft context *before* numeric constraints or the prose feels mechanically slotted; keep layer 1 universal across tenants, layers 2–3 per tenant; identity must never default — crash loudly on missing brand config | `ReferencesElement → el-layered-voice-architecture` |
| `how-post-generation-veto` | Gate output with a deterministic post-generation veto | Run a check that reads the actual output after generation, with power to block shipping; soft-flag via regex honesty inspector (did it answer the question? did it hedge?) — regexes are fast, cheap, deterministic; choosing determinism over a small classifier's coverage is a real trade-off to make consciously; hard-reject any number, date, or fact not present in an allow-list of known-true values; build the veto as one shared service every surface passes through by default (per-surface wiring is a checklist waiting to be forgotten); centralize condition/mode resolution in one resolver rather than per-surface knowledge | `ReferencesElement → el-post-generation-veto` |

## Dropped

- The Google Maps routing analogy (destination fixed, route conditional, rules vs conditions vs preferences vs pre-departure check) — the talk's teaching scaffold, folded into element/knowhow briefs.
- The 24 scattered prompts "named Sage, Less, Venue" — folded into `el-layered-voice-architecture` brief.
- The engagement heat-map + "mom in chemo" narration example — folded into `el-bloom` brief and `how-four-layer-voice-stack`.
- The personal AI companion app — mentioned once in the bio list; nothing extractable.
- Voice-training-from-coordinator-edits (layer 3 tooling) — folded into the architecture brief; not load-bearing enough for its own node.

## Review notes

1. **Heavy caption garbling, resolutions applied:** "four lad / lad one" → four layers / layer one; "the soft flag is rejects not a model… rejects is fast and cheap and deterministic. It either matches or it doesn't" → **regexes** (resolved from context); "numbers God / numbers guide us" → numbers guard; "munching in grief" → likely "navigating grief"; "catch-all error" → likely "category error"; "corn walk from the coordinator rules" → unresolved (likely "coordinator walkthrough/config"); "sage@hawthornemanner.com" → presumably hawthornemanor.com (the flagship venue's domain — venue name not coined, inferred only from this leaked-email example).
2. **Company & product names:** `co-isadora-and-co` from the official listing (never spoken); "Bloom" inferred from "Every AI in Bloom discloses that it is AI"; "Thread Light" also appears as "thread line" — picked Thread Light. All three flagged for verification.
3. **Two pattern-less signals** (`sig-multitenant-default-identity-leak`, `sig-ai-disclosure-first-message`): concrete, high-quality practitioner observations with no seed-altitude home in the registry — the first is a multi-tenancy ops lesson, the second a trust-UX product bet. If a trust/disclosure-UX pattern ever reaches coin threshold, both are ready to rehome; forcing them onto `pat-harness-over-model` felt like altitude abuse.
4. **`el-post-generation-veto` merge decision:** same family as `el-generator-validator-separation` **[batch 1]** and `el-constrain-effects-not-expression` **[batch 7]** (deterministic checks outside the generator). Coined anyway because the soft-flag/hard-reject taxonomy and the instructions-vs-permission framing are this talk's load-bearing contribution and get referenced by insight + knowhow; collapse into one node at seeding if preferred (batch-7 already flagged this cluster).
5. `pat-verification-gap` edges: the invented-dates story is a textbook verification-gap case (generation confident, verification bolted on outside the model) — chosen over a second `pat-harness-over-model` edge for signal diversity; swap if review disagrees.
6. Candidate patterns from the central ledger (`pat-durable-execution`, `pat-benchmark-trust-crisis`, `pat-agent-economy`, `pat-ai-native-org`, `pat-adaptive-*`): no new evidence in this talk. (A solo non-engineer operator shipping multi-tenant AI products is at most the faintest `pat-ai-native-org` resonance — not counted.)
