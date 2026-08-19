# SPIKE extraction — "The Next Game Engine Won't Have a Manual" (Arturo Nunez, Nereu) — FOR REVIEW

Source transcript: `transcripts/nunez-nereu-game-engine-no-manual.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/VBCDhRrvlYo — AI Engineer World's Fair, **Generative Media track**, published 2026-08-18.
`stagingTimestamp`: 2026-08-18. Entities marked **[registry]** are already in the registry.
Shape of the talk: a 10-year Unity veteran builds Nereu, a game engine driven by **describing intent in game-player vocabulary** rather than coding. The key idea: flip the engine's context from engine-internals to **game design** via an **asset-tag system** (entity-component-system reframed as tags), an LLM assistant that applies/removes tags, and **level-of-detail context assembly** (feed the LLM high detail for nearby objects, low for far ones). Caption garbles: "Nereo/Nereu" → **Nereu**, "Bibi/Weeby" → **Weeby** (the assistant), "ATS" → **asset-tag system**, "Cloud Code" → **Claude Code**, "entity component system" kept.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-nunez-game-engine-no-manual` | The Next Game Engine Won't Have a Manual (Arturo Nunez, Nereu — AI Engineer World's Fair) | youtube | https://youtu.be/VBCDhRrvlYo |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-arturo-nunez`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-arturo-nunez` | Arturo Nunez (building Nereu; ~10 years at Unity, then MongoDB; game-asset version-control background) | `AffiliatedWithCompany → co-nereu`, `AffiliatedWithCompany → co-unity` |

## Companies (1 new; 1 reused-on-reference)

| slug | name | type | note |
|---|---|---|---|
| `co-nereu` | Nereu | developer | Browser-based game engine (closed alpha) where you build games by **describing intent** in game-player vocabulary rather than coding; assets pre-tagged (via a vision model over ~6–7k assets), an LLM assistant ("Weeby") applies tags. JavaScript under the hood, extensible but scripting-free by default |
| `co-unity` | Unity | developer | Game-engine company; coined on reference (the speaker's ~10-year employer, the incumbent-workflow contrast). Passing corpus entry |

Reused **[registry]**, edge-only: `co-mongodb` **[b2]** (the speaker's later employer). Referenced: Claude Code (how the engine itself is built).

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-intent-over-engine-vocabulary` | Intent in player vocabulary, not engine vocabulary | concept | harness | The core flip: "by default the context is on the game engine — we should flip that to game design." Instead of learning meshes, renderers, animators, rigid bodies, colliders and hundreds of sliders, you describe intent in **the language players already know** ("make this robot move with WASD," "double jump," "when you collect a coin, increase the score"). The LLM otherwise "reinvents the wheel every time" (a camera-follow reimplemented differently each run) because it lacks the right vocabulary layer — so the fix is a domain-intent layer above the engine, not a better prompt |
| `el-asset-tag-system` | Asset-tag system (ATS) | technology | harness | The mechanism: reframe the game-dev **entity-component-system / data-oriented design** as **tags** describing intent — "everything is an asset, everything renders, everything has physics; you add tags to describe intent." Systems query for assets by tag ("move everything tagged vehicle+player+drivable"). Recyclable across games (tag a building vehicle+drivable and it's a Mario-Kart obstacle). The LLM assistant applies/removes tags via tool calls; tags and systems are built into the engine, no scripting layer by design |
| `el-lod-context-assembly` | Level-of-detail context assembly | concept | context | The context-engineering technique, borrowed from game rendering's **level-of-detail**: just as you render nearby objects in high fidelity and distant ones as a cube, **assemble the LLM's context by proximity** — feed full tag/setting detail for objects near what the user is editing, minimal info for far ones, ignore filler (grass). As the user moves, update what's fed. A domain-native answer to context bloat: relevance by spatial proximity to the edit |
| `el-vision-tagged-assets` | Vision-model asset tagging | technology | harness | The bootstrapping step: ~6–7k assets couldn't be hand-tagged, so a **vision model screenshots and describes each** (astronaut, knight, castle) to seed the tag/description index the assistant searches. Vision models as the mechanism for making a large asset library agent-navigable |

Element edges: all four `IdentifiedInArtifact → ia-aie-nunez-game-engine-no-manual`.
`el-asset-tag-system` `UsesElement → el-intent-over-engine-vocabulary`, `el-vision-tagged-assets`;
`el-lod-context-assembly` `EnablesElement → el-asset-tag-system`;
`el-asset-tag-system` `DevelopedByCompany → co-nereu`, `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-intent-over-engine-vocabulary` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**.

Reused elements (no new nodes): `el-progressive-disclosure` **[registry]** (LOD context assembly is a spatial form of it), `el-agents-md`/`el-code-mode` adjacency (none). The talk contrasts its approach with **world-model game generation** (referenced, said to be "a different medium," 60fps/4K real-time still far off) — no edge.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-nunez-game-engine-no-manual`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-nereu`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-flip-context-to-domain-intent` | harness | The design claim from a Unity veteran: the LLM "reinvents the wheel every time" (a camera-follow reimplemented differently each run) because the context is on engine internals, not game design — so **flip the context to domain intent** and let people describe games in player vocabulary (WASD, double-jump, collect-a-coin). A general harness lesson: give the model a domain-intent vocabulary layer above the tool, rather than a better prompt over raw primitives | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-intent-over-engine-vocabulary`, `el-asset-tag-system` |
| `sig-tags-as-intent-layer` | harness | The mechanism: reframe entity-component-system as **tags describing intent** that systems query over, recyclable across games, applied/removed by an LLM assistant — a declarative intent layer that the engine executes deterministically. The "intent, not code" thread (Dailey b17, Jain b21) realized in a game engine via a tag substrate | `FormsPattern → pat-value-of-judgement` **[registry]** | `OnElement → el-asset-tag-system`, `el-vision-tagged-assets` |
| `sig-lod-context-assembly` | context | A domain-native context-engineering technique: assemble the LLM's context by **spatial level-of-detail** — high fidelity for objects near the edit, minimal for far ones, ignore filler — updated as the user moves. Game rendering's LOD borrowed for context management, a concrete instance of relevance-by-proximity progressive disclosure. Convergent with the corpus's broader context-engineering thread (Bouchard b21) from a spatial angle | `FormsPattern → pat-context-graphs` **[registry]** | `OnElement → el-lod-context-assembly`, `el-progressive-disclosure` **[registry]** |
| `sig-game-making-as-creative-outlet` | harness | The product thesis: most people want game-*making* as a creative outlet (like Legos), not to ship a competitive title, and shouldn't need to be professional developers — "the same as AI assistants for code, now you don't need to be a programmer to build what you want." Democratization of creation via an intent layer; a media-side echo of the AI-native-org "non-devs ship" thread. **HELD PATTERN-LESS** — media-as-medium ledger | — (held pattern-less) | `OnElement → el-intent-over-engine-vocabulary` |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-give-the-model-a-domain-vocabulary` | The durable lesson is that the fix for an LLM that "reinvents the wheel every time" is not a better prompt but a **domain-intent vocabulary layer** the model applies over deterministic systems — tags the engine executes, described in the language the user already thinks in. That is the harness-over-model thesis in a specific form: the reliability comes from the tag substrate and the LOD context assembly, not the model's intelligence, and it generalizes to any tool where users have a rich domain vocabulary (game design, video editing, music) that the raw engine primitives don't expose | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-intent-over-engine-vocabulary`, `el-asset-tag-system` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-nunez-game-engine-no-manual`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-an-intent-driven-engine` | Build tools around domain intent, not primitives | When an LLM "reinvents the wheel every time," give it a **domain-intent vocabulary layer** rather than a better prompt — let users describe intent in the language they already know (for games: WASD, double-jump, collect-a-coin) and map it to deterministic systems the engine executes; reframe your primitives as **tags describing intent** (an entity-component-system as tags) that systems query over and that an LLM assistant applies/removes via tool calls, so behavior is declarative and recyclable across projects; manage context with **spatial level-of-detail** — feed the model full detail for what's near the user's focus and minimal detail for the rest, updating as they move, so context stays small and relevant; and make a large asset library agent-navigable by **tagging it with a vision model** (screenshot + describe) rather than by hand | `ReferencesElement → el-intent-over-engine-vocabulary`, `el-asset-tag-system`, `el-lod-context-assembly`, `el-vision-tagged-assets` |

## Dropped

- **The live build demo** (robot + WASD + buildings + rain + camera-follow) — illustration folded into `el-intent-over-engine-vocabulary`.
- **The Unity-career reminiscence** — kept as one clause in the expert node.
- **The world-model-game-generation aside** — referenced as "a different medium" (60fps/4K real-time far off); no edge.

## Review notes

1. **The media talk with the best context-engineering contribution.** `el-lod-context-assembly` (relevance-by-spatial-proximity) is a genuinely novel framing of progressive disclosure, and the "flip context to domain intent" lesson lands on `pat-harness-over-model` (claim-1). Convergent with Bouchard's b21 context-engineering workshop from a spatial angle, and with the "intent not code" thread (Dailey b17, Jain b21).
2. **`co-unity` coined on reference** (b2 precedent) to carry the speaker's dual affiliation and the incumbent-workflow contrast — a passing entry, no facts beyond being a game engine.
3. **⚠ Verify before seeding:** assistant name ("Weeby"/"Bibi"); ~6–7k asset count; the closed-alpha status. All caption-sourced.
