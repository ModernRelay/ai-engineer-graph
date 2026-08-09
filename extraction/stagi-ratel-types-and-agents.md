# SPIKE extraction — "A Song of Types and Agents" (Roberto Stagi, Ratel) — FOR REVIEW

Source transcript: `transcripts/stagi-ratel-types-and-agents.txt` (auto-captions — quotes are paraphrases, not verbatim; "Reto" in captions = **Ratel** per the official talk title).
Video: https://youtu.be/UlFB6efYN5Q — AI Engineer World's Fair, published 2026-07-12.
`stagingTimestamp` for the artifact and all signals: 2026-07-12 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-stagi-types-and-agents` | A Song of Types and Agents (Roberto Stagi, Ratel — AI Engineer World's Fair) | youtube | https://youtu.be/UlFB6efYN5Q |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-roberto-stagi`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-roberto-stagi` | Roberto Stagi (CTO & co-founder, Ratel; EU ambassador for a global AI-builders community; long-time JavaScript→TypeScript developer) | `AffiliatedWithCompany → co-ratel` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-ratel` | Ratel | developer | Context layer for AI agents (captions render it "Reto"; spelling taken from official talk title — verify site/spelling before seeding) |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-typescript` | TypeScript | technology | harness | Typed superset of JavaScript; per the talk, the default output language of coding agents and the emerging language of the agentic application layer — one language and one type system (e.g. Zod schemas) from UI through backend to agent loop, on top of NPM |
| `el-vercel-ai-sdk` | Vercel AI SDK | framework | harness | TypeScript SDK for building AI/agent features in web applications; cited as the marker of the TS AI-ecosystem surge (1.6M → 15.1M weekly downloads in one year) |

Element edges: both `IdentifiedInArtifact → ia-aie-stagi-types-and-agents`; `el-typescript` `EnablesPattern → pat-model-not-bottleneck` **[registry]** (the application layer around models is where the language war is being fought).

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-stagi-types-and-agents`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-typescript-passes-python-github` | In August 2025 TypeScript passed Python as the most-used language on GitHub — and GitHub's own reports attributed both moves to AI ("AI leads Python to the top" in 2024, "AI leads TypeScript to first" in 2025), amid one new developer joining GitHub every second | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-typescript`; `RelevantCompany → co-github` **[registry]** |
| `sig-coding-agents-default-typescript` | What changed between 2024 and 2025 was coding agents (Claude Code, Cursor, Codex) becoming the default way to build applications — and their default output is TypeScript; a self-reinforcing flywheel: more TS apps → more TS training data + deeper native integrations → better agent output in TS | `FormsPattern → pat-model-not-bottleneck` | `OnElement → el-typescript`; `RelevantCompany → co-cursor` **[registry]** |
| `sig-anthropic-acquires-bun` | December 2025: Anthropic acquired Bun, a JavaScript runtime — an AI lab buying JS infrastructure, read as confirmation that the agentic application layer runs on the JS/TS stack | `FormsPattern → pat-model-not-bottleneck` | `RelevantCompany → co-anthropic` **[registry]** |
| `sig-vercel-ai-sdk-10x` | The Vercel AI SDK went from 1.6M to 15.1M weekly downloads in one year (~9–10x) — the TS-native AI ecosystem is surging as AI features move into ordinary applications | `FormsPattern → pat-model-not-bottleneck` | `OnElement → el-vercel-ai-sdk` |

## Insights (1 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-python-brain-typescript-body` | An emerging language split: training, research, and GPU serving stay Python ("the model ships on pip"), but agents — the new application layer — ship on NPM in TypeScript; the practical edge is one codebase and one consistent type system (a Zod schema defined once, used in agent loop, backend, and UI) versus a Python service + separate typed frontend with a contract to hand-synchronize — Atwood's law extended to agents | `HighlightsPattern → pat-model-not-bottleneck` | `ReliesOnElement → el-typescript` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-stagi-types-and-agents`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-choose-typescript-for-agents` | Build application-layer agents in TypeScript, keep training in Python | If the agent lives inside a product: use TypeScript for agent loop, tools, backend, and UI (one language, one repo, one type system via Zod); tap NPM for auth/payments/UI/infra integrations; expect coding-agent output quality in TS to keep improving with the flywheel; keep Python for training, research, and model serving — don't split the app into FastAPI + React unless you must | `ReferencesElement → el-typescript` |

## Dropped

- Zod, FastAPI, Pydantic AI, React/Vue — prose inside the insight/knowhow, not load-bearing elements here.
- Bun as an Element — the acquisition is the signal; the runtime itself carries no further edges in this talk.
- "AI's Pratic" community and speaker's ambassador role — bio detail (garble, likely "AI Sprint"/"AI Practice" — unresolved).
- Jeff Atwood quote — kept as prose in `ins-python-brain-typescript-body`.

## Review notes

1. **Advocacy talk, weight accordingly**: this is an opinion/positioning talk by a TypeScript partisan; the three dated external facts (GitHub Aug 2025 ranking, Anthropic–Bun Dec 2025, Vercel AI SDK download growth) are the hard signals — verify all three independently before public-facing use. The Bun acquisition in particular I could not cross-check from the transcript alone.
2. **Garbles**: "Reto" → Ratel (per title); "Lava Cloud Code, Cursor, Codex" — "Lava" unresolved (possibly "the likes of" or a fourth agent name); "Versatile AI SDK" → Vercel AI SDK; "AI's Pratic" unresolved.
3. All four signals land on `pat-model-not-bottleneck` — the talk is a single-thesis argument (value moved from the model/training layer to the application layer, and the application layer's language is winning). A "TypeScript eats the agentic layer" pattern was considered and NOT coined (one-talk evidence, and it reads as a mechanism of `pat-model-not-bottleneck` rather than a seed-altitude thesis).
4. `co-github` reuse: registry lists it under batch1 companies; used for `RelevantCompany` on the ranking signal.
