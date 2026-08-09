# SPIKE extraction — "Imagination Engineering" (Eve Bouffard, Head of Design, Y Combinator) — FOR REVIEW

Source transcript: `transcripts/bouffard-yc-imagination-engineering.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/Z2Erdirpudo — AI Engineer World's Fair, published 2026-07-16.
`stagingTimestamp` for the artifact and all signals: 2026-07-16 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-bouffard-imagination-engineering` | Imagination Engineering (Eve Bouffard, Head of Design, Y Combinator — AI Engineer World's Fair) | youtube | https://youtu.be/Z2Erdirpudo |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-eve-bouffard`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-eve-bouffard` | Eve Bouffard (Head of Design, Y Combinator) | `AffiliatedWithCompany → co-y-combinator` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-y-combinator` | Y Combinator | investor | startup accelerator; appears here via its head of design demoing frontier-model personal-software workflows. (Slug chosen to collide cleanly with any parallel coinage from the Garry Tan talk, per batch convention) |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-thinking-in-public` | Thinking in public (thought-stream → agent-compiled artifacts) | concept | context | Practice of streaming one's raw thinking into a shared channel (e.g. a personal Slack "thoughts" channel, in the lineage of PG's essays) so that a frontier model can compile the accumulated stream into working artifacts — a personal website, tools, reports — plus self-maintaining context files (voice.md distilled from one's public writing, an auto-updating design-language md, an agent-readable glossary md instead of having agents parse rendered pages) |

Element edges: `el-thinking-in-public` `IdentifiedInArtifact → ia-aie-bouffard-imagination-engineering`; `EnablesPattern → pat-context-graphs` **[registry]** (personal context corpus as the substrate agents build from — loose fit, see review note 3).

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-bouffard-imagination-engineering`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | domain | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-imagination-new-bottleneck` | YC's head of design, on Fable 5's launch week: with current models "it's going to be really easy to one-shot absolutely everything and anything very soon" — the new bottleneck is coming up with ideas worth building ("imagination engineering"), not building them; echoes Garry Tan's reframe of Jobs' bicycle-for-the-mind as "a rocket ship for the mind" | harness | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `co-y-combinator` |
| `sig-week-of-thoughts-to-website` | Concrete demo: after one week of brain-dumping into a personal Slack thoughts channel, a single ask to Opus 4.8 produced a full personal website (evebouffard.com) synthesizing her projects, books, quotes, tools, media — with per-viewer customization (backgrounds, shaders, typography, dark mode, full translation into any language), a self-updating design system, voice.md, and a public changelog; speaker: "it kind of felt like AGI" | harness | `FormsPattern → pat-saaspocalypse` **[registry]** (software on demand from a thought stream) | `co-y-combinator` |
| `sig-personal-software-in-hours` | Same-day software: the "Shape of Minds" interactive tool (commonalities across history's great minds over dimensions like thinking, obsessions, routines) was built in one morning before the talk, alongside a personal Slack-emoji search tool and on-demand learning reports — "it's all software on demand: whatever stream of consciousness you have, just ask an agent to do it for you" | harness | `FormsPattern → pat-saaspocalypse` | `co-y-combinator` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-imagination-is-the-scarce-input` | When one-shotting software approaches free, the scarce input inverts from engineering capacity to imagination — the valuable skill becomes stretching what you think is possible (PG's "live in the future, then build what's missing" as an operating prompt); design converges on taste-expression via sliders and generated variation rather than hand-built artifacts | `HighlightsPattern → pat-model-not-bottleneck`, `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-thinking-in-public` |
| `ins-thought-streams-are-agent-fuel` | "Building in public" extends to "thinking in public": a raw, continuous thought stream is a context asset agents can compile into artifacts on demand — the stream of consciousness effectively becomes the spec, and curated context files (voice.md, design-language md, glossary md) make the person herself agent-readable | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-thinking-in-public` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-bouffard-imagination-engineering`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-thought-stream-workflow` | Turn a thought stream into agent-built software | Keep a running public/semi-public thoughts channel and brain-dump continuously; periodically ask a frontier model to compile the stream into artifacts (site, tools, digest reports); distill your public writing into a voice.md and keep an auto-updating design-language md so outputs stay on-voice and on-style; publish an agent-readable glossary/md of your project instead of making agents parse rendered pages; build personal skills you can invoke; when you want to learn something, ask for a short digestible report rather than researching manually | `ReferencesElement → el-thinking-in-public` |

## Dropped

- Conductor (Lewis's "Lewis Thoughts" channel; Conductor Cloud for spinning agents on the go) — origin credit and a forward-looking aside; kept as prose, `co-conductor` not coined (single-mention, not load-bearing).
- Paper (design tool with Claude Code–compatible shaders) — enthusiast product mention; prose only.
- Opus 4.8 / Fable 5 as Elements — model-version mentions (registry has `el-claude-opus-47`, an earlier version); kept as prose to avoid version-node sprawl.
- Paul Graham / Garry Tan / Steve Jobs as Expert nodes — quoted inspirations, not contributors; prose only.

## Review notes

1. Auto-caption garbles: "evebufar.com" → evebouffard.com (inferred); "paper sheeters" → almost certainly Paper "shaders"; "cloud code" → Claude Code; "Cloud Workspaces ... with Conductor Cloud" is ambiguous between Claude Workspaces and a Conductor product — left as prose, unresolved; "Gary" → Garry Tan.
2. This is a demo/inspiration talk: all three signals are first-person demonstrations, not third-party dated facts. The two builds are precisely dated (the week before / the morning of the talk) and attributable, which is why they clear the signal bar.
3. `el-thinking-in-public` → `pat-context-graphs` is the loosest edge in this file (personal thought-corpus as context substrate vs enterprise context graphs); cut the `EnablesPattern` edge if you read the pattern more narrowly.
4. No new pattern coined; "imagination as the new bottleneck" is treated as evidence for `pat-model-not-bottleneck` rather than a distinct thesis (single-talk evidence).
