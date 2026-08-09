# SPIKE extraction — "Think You Can Build a Game with AI? Think Again!" (Danielle An & David Hoe, Meta) — FOR REVIEW

Source transcript: `transcripts/an-hoe-meta-game-with-ai.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/grdoOC1BT1s — AI Engineer World's Fair, published 2026-07-08.
`stagingTimestamp` for the artifact and all signals: 2026-07-08 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-an-hoe-game-with-ai` | Think You Can Build a Game with AI? Think Again! (Danielle An & David Hoe, Meta — AI Engineer World's Fair) | youtube | https://youtu.be/grdoOC1BT1s |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-danielle-an`; `ContributedByExpert → exp-david-hoe`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-danielle-an` | Danielle An (principal engineer, Meta; co-leads AI-driven game creation) | `AffiliatedWithCompany → co-meta` **[registry]** |
| `exp-david-hoe` | David Hoe (Meta; co-leads AI-driven game creation — exact team name garbled in captions) | `AffiliatedWithCompany → co-meta` **[registry]** |

## Companies (0 new)

- `co-meta` **[registry]** — reused; appears here as both game-creation tooling builder and platform anticipating millions of pieces of AI-created gaming content.

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-runtime-llm-gameplay` | Runtime-LLM gameplay | technology | inference | LLMs running *during* play as a living entity that modifies and directs the game: unscripted NPC decision-making from assigned personalities, game-master-style per-player adjustment (e.g. difficulty for a coordination-challenged player). Distinct from build-time generation; became feasible ~2025–2026 as inference got fast and cheap enough; every session is unique/non-repeatable |

Element edges: `el-runtime-llm-gameplay` `IdentifiedInArtifact → ia-aie-an-hoe-game-with-ai`. (No `DevelopedByCompany` — Meta demoed it but the technology is general; Meta's association is carried by the signals' `RelevantCompany` edges.)

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-an-hoe-game-with-ai`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | domain | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-llm-npcs-now-feasible` | Meta's AI-gaming team demoed a multiplayer game — built in a couple of days — where every NPC is entirely runtime-LLM-driven: assigned personalities (thief, honorable, fast) making unscripted decisions to steal, block, kick; a genre "the industry just could not make" before, unlocked in the last ~18 months by inference speed and model cost drops | inference | — (pattern-less; see notes) | `OnElement → el-runtime-llm-gameplay`; `RelevantCompany → co-meta` **[registry]** |
| `sig-game-prompting-commoditized` | By 2026 anyone — kids, moms, friends — can prompt a working basic game (platformer/Tetris) on consumer models; the novelty wears off and outputs converge ("everyone's Mario platformer looks the same"); skill gates fell (coders without art use image/3D generation tools — names garbled), so differentiation collapses to taste: aesthetics, one-universe cohesion, playtests, knowing which humans will have fun and why | harness | `FormsPattern → pat-value-of-judgement` **[registry]** | — |
| `sig-game-waterfall-parallel` | After ~12 months directing cross-discipline AI game teams at Meta: production flipped from linear waterfall (design→art→modeling→animation→code; upstream decisions prohibitively costly to revisit; months per iteration) to parallel AI-assisted teams iterating in hours/days — more playtests per idea, structurally more fun games | harness | — (pattern-less; AI-native-org resonance, see notes) | `RelevantCompany → co-meta` **[registry]** |
| `sig-agentic-stack-nondeterminism` | Meta platform engineers report non-determinism now spans the whole stack — user prompting at the frontend, runtime LLMs inside the game, agentic serving/ranking/delivery behind it; model upgrades or prompt changes can throw off the entire system, and the write-code/write-tests/debug-against-known-codebase notion of stability and scalability no longer applies; "how do you even debug that?" is open at scale | harness | `FormsPattern → pat-verification-gap` **[registry]** | `RelevantCompany → co-meta` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-runtime-llm-taste` | Runtime LLMs turn the model from a build-time asset generator into a live game director — but the technology itself does not make the product better; with polish democratized and every studio exploring the same tech, the scarce input is taste: the feel for which subset of humans will find a game fun and why. How to use runtime LLMs to differentiate is still unsolved, industry-wide, at day zero | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-runtime-llm-gameplay` |
| `ins-nondeterminism-is-the-price` | The same runtime LLMs that make every play session unique dissolve the known-codebase stability contract; a platform expecting millions of pieces of AI-created gaming content must re-solve verification from scratch — debugging non-deterministic stacks, content safety for content generated *at runtime*, and a token economy that keeps creators, players, and platform simultaneously profitable | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-runtime-llm-gameplay` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-an-hoe-game-with-ai`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-key-art-anchoring` | Anchor generative pipelines on a single key-art image | Iterate until you hit a concept you love (like classic game development), then use that one key-art image as the anchor for all models; filter it down into asset generation and even gameplay direction — a single image carries enough information to keep art style, UI, story, and gameplay cohesive across LLM sessions (workflow from a Meta art director) | — |
| `how-stand-out-prompted-games` | Escape prompted-game sameness | Upgrade beyond the prompt: invest in aesthetics and one-universe cohesion between UI, story, and art; run playtests with real people and real feedback; then differentiate with runtime-LLM dynamics (NPC personalities, game-master personalization); at platform scale, design the token economy (creators/players/platform all profitable) and content safety for runtime-generated images and content | `ReferencesElement → el-runtime-llm-gameplay` |

## Dropped

- The interactive QR-code slide game (NPCs revealing slides, audience voting) — demo apparatus, folded into artifact context.
- Gemini / "Manas" (likely Manus) / image- and 3D-gen tool mentions — passing name-drops as prompting/asset tools; no Element nodes, garbles flagged below.
- Ready Player One / Oasis "day zero" framing and the Labubu personalization moment — rhetoric/demo color, kept out of signals.
- "Game master" as a separate Element — folded into `el-runtime-llm-gameplay` brief.

## Review notes

1. **Caption garbles, unresolved:** (a) "David from our AI for Meta" — David Hoe's exact team/title is garbled; official listing just says Meta. (b) "you can just use **Meta Banana or Mesh you**" — plausibly "Nano Banana" (Google image model) and "Meshy" (3D asset generation); left unnamed in the signal since neither reading is certain and one would be a competitor's product named by Meta employees. (c) "Gemini **Manas**" — plausibly "Manus". (d) "Lububu" = Labubu (Pop Mart character). (e) Art director "Dale" — first name only.
2. `sig-llm-npcs-now-feasible` left pattern-less deliberately: it is a capability-unlock observation (cheap fast inference → new genre) and none of the registry patterns claim that shape; closest is `pat-model-not-bottleneck` but this signal argues the opposite direction (model/inference progress *was* the unlock). Flagged rather than force-fit.
3. `sig-game-waterfall-parallel` is an **"AI-native organization" resonance point** (team structure/process transformed by AI) — candidate noted in registry batches 3/5; per instructions, NOT coined, no edge. Add it to that candidate's evidence list at central review.
4. `sig-game-prompting-commoditized` → `pat-value-of-judgement` extends that pattern beyond careers to product differentiation ("taste is what separates the best game") — flag if you want the pattern kept career-scoped.
5. The "18 months" and "built in a couple days / 12 hours" figures are speaker statements; the talk demos were live and not externally verifiable from captions.
