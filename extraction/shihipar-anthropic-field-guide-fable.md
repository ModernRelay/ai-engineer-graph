# SPIKE extraction — "Field Guide to Fable" (Thariq Shihipar, Anthropic) — FOR REVIEW

Source transcript: `transcripts/shihipar-anthropic-field-guide-fable.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/9fubhllmsBU — AI Engineer World's Fair, published 2026-07-06.
`stagingTimestamp` for the artifact and all signals: 2026-07-06 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

Context: Shihipar's solo talk, delivered the day Fable rolled out ("Fable is back — rolling it out later today"); he plugs the 12:30 fireside with Cat Wu and Simon Willison, which is the batch-5 artifact `ia-aie-wu-shihipar-anthropic-culture`. Same speaker, so overlapping claims here are corroboration, not independent evidence (see Review notes).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-shihipar-field-guide-fable` | Field Guide to Fable (Thariq Shihipar, Anthropic — AI Engineer World's Fair) | youtube | https://youtu.be/9fubhllmsBU |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-thariq-shihipar` **[registry]**.

## Experts (0 new)

- `exp-thariq-shihipar` **[registry]** (batch 5, Claude Code team, Anthropic) — no new node.

## Companies (0 new)

- `co-anthropic` **[registry]** — `RelevantCompany` target for all signals below.

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-capability-overhang` | Capability overhang | concept | harness | Latent model capability exceeding what current prompts/harnesses extract — "models get smarter in spiky ways": a chat model cannot list the Pokémon whose names end in "-aw", but the same model with a code-execution tool fetches every name and filters (Croconaw, Drednaw). Models are "grown, not designed", so the harness encodes our *understanding* of the model; "unhobbling" = mapping and unlocking the overhang, and each frontier release (Fable) ships with a largely unmapped one |

Element edges: `el-capability-overhang` `IdentifiedInArtifact → ia-aie-shihipar-field-guide-fable`; `el-capability-overhang` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**.

Registry element reuse (no new nodes, edges only): `el-claude-fable` **[registry]**, `el-claude-code` **[registry]**, `el-claude-tag` **[registry]** — each `IdentifiedInArtifact → ia-aie-shihipar-field-guide-fable`. Fable is the talk's subject; Claude Code is the running example of overhang-unlocking (bash tool → model builds its own context, "the insight that led to Claude Code"); Claude Tag appears as the proactive-multiplayer unlock ("Claude waking itself up to do work is unlocking the new wave of agents").

## Signals (5 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-shihipar-field-guide-fable`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-anthropic` **[registry]**.

| slug | name / brief | FormsPattern |
|---|---|---|
| `sig-fable-capability-overhang` | Anthropic Claude Code staff frames Fable's launch as an unmapped capability overhang: the models' latent ability exceeds what harnesses currently extract (Pokémon "-aw" answerable only once a code-execution tool is present), and "what contains them is us" — the discovery work is on the harness/prompting side, not model-side | `FormsPattern → pat-model-not-bottleneck` **[registry]** |
| `sig-system-prompt-era-arc` | System-prompt best practice has moved in an arc across model generations: Sonnet-3.5-era = small prompt, few tools, many examples → mid-era = large prompts, many instructions, many tools → Fable-class = smaller prompts again, examples removed (they constrain a model more imaginative than the examples), "do not" constraints replaced with context; Claude Code's system prompt was cut ~80% | ContradictsPattern → `pat-harness-over-model` **[registry]** (counter-evidence: prescriptive scaffolding is being deleted as models improve) |
| `sig-question-tool-progression` | The "ask a question" tool traces the overhang across releases: Opus 4 could barely call it (tool needed heavy tweaking), Opus 4.5 could run a 40-question spec interview, Opus 4.8/Fable builds whole HTML reports with the questions embedded; model output similarly moved markdown → plan mode → in-depth HTML reports — the interaction surface jumps discontinuously with each generation | `FormsPattern → pat-model-not-bottleneck` **[registry]** |
| `sig-fable-bottleneck-is-operator` | Practitioner claim: "Fable is bottlenecked by my ability to match the map and the territory" — with Fable-class models the constraint moves to the operator's ability to surface unknowns (unspecified decision points the model will hit); Fable traverses so much territory that unfound unknowns dominate outcomes | `FormsPattern → pat-value-of-judgement` **[registry]** |
| `sig-tradeoffs-collapse` | Returning to his ~30-person YC startup's codebase: changes that took weeks now take hours; the "good, fast, cheap — pick two" tradeoff is reframed as "pick three"; Anthropic culture holds "tradeoffs are not real — force reality to show you the tradeoff"; the conference deck itself was made in ~4 hours with Fable | `FormsPattern → pat-accelerated-research` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-unhobbling-is-the-work` | Because models are grown, not designed, the harness and prompt are a function of our understanding of the model — so when a frontier model lands, the leverage is not waiting for a better model but "unhobbling": empirically mapping the capability overhang ("closer to biology than physics") and rebuilding harness assumptions per generation | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-capability-overhang`, `ReliesOnElement → el-claude-fable` **[registry]** |
| `ins-build-easy-value-hard` | Building is now easy but generating value is still hard — AI engineers over-index on process and setups when the point is value, which takes many swings to find; "the only way to prove agents work is to do the best work of our lives faster than ever" — the world is watching AI engineers for proof AI transforms productivity | `HighlightsPattern → pat-value-of-judgement` **[registry]** | — |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-shihipar-field-guide-fable`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-blind-spot-pass` | Use the model to find your unknowns before prompting big work | Run a "blind spot pass" first ("I know nothing about this auth provider — find my relevant unknown unknowns so I can prompt better"), pointing it at context stores (git diff/history, Slack); works for whole new fields (e.g. color grading). Then invert: have Claude interview you against the spec ("prioritize questions that would change the architecture"). For know-it-when-you-see-it preferences (design), ask for throwaway prototypes — one HTML page with four widely different design directions to react to | `ReferencesElement → el-claude-fable` **[registry]** |
| `how-reference-as-map` | Give Claude another map instead of writing a spec | Hand it reference code that represents what you want — even from a different system or language — or an HTML mock-up for a React component, with "read this, understand it, then start"; a working artifact encodes the unknown-knowns a prose spec misses | `ReferencesElement → el-claude-fable` **[registry]** |
| `how-deviation-log-and-quiz` | Log deviations mid-run, get quizzed after | Ask Fable to log every unknown it hits while running (implementation notes with context on why it deviated) so you can see where map diverged from territory; afterwards have it quiz you on what happened so you can genuinely represent the work at PR/merge time — the core "stay in the loop" practice for long-leash models | `ReferencesElement → el-claude-fable` **[registry]** |

## Dropped

- Fable launch logistics ("rolling out later today", fireside plug) — kept as artifact context prose, not a signal; the launch is already canonical in batch-5's `el-claude-fable`.
- Claude Tag proactive-multiplayer recap — already deeply covered in `wu-shihipar-anthropic-culture.md`; here it gets only the element reuse edge.
- "On the Biology of a Large Language Model" (favorite Anthropic paper) — reading recommendation, prose only.
- Opus 4.8 — mentioned jointly with Fable (question tool, HTML reports); kept in prose per batch-5 precedent (central reviewer may still want `el-claude-opus-48`).
- Known/unknown 2×2 matrix (Rumsfeld matrix) — folded into `sig-fable-bottleneck-is-operator` and the KnowHows, not coined.
- Selfie tradition, RPG "the map is opening up" metaphor, grief/loss reflection ("how can you not laugh, how can you not cry", "swimming in failure") — color; grief material partly informs `sig-tradeoffs-collapse`.

## Review notes

1. **Name garbles resolved from official title/registry**: "Tarik Shaupar" → Thariq Shihipar; "Kat Woo" → Cat Wu; "Simon Wilson" → Simon Willison; "3 sign of 3.5 new" → "Sonnet 3.5 new"; "agentle coding" → agentic coding. **Unresolved**: "the first time I used a Mithril class model, uh used Fable" — "Mithril" may be a garble of "Mythos" (batch-5 flagged Mythos as Fable's likely preview name, cf. `el-claude-mythos-preview`) or a real internal class name; flagged, not coined.
2. **Same-speaker overlap with batch 5**: the ~80% system-prompt cut and examples-constrain-frontier-models claims also appear in `wu-shihipar-anthropic-culture.md` (`sig-system-prompt-cut-80pct`, `how-prompt-frontier-models`). `sig-system-prompt-era-arc` is kept because the three-era *arc* (small→large→small) is this talk's distinct contribution — but treat the two signals as one speaker's claim twice, not independent evidence.
3. `sig-system-prompt-era-arc` uses **ContradictsPattern** against `pat-harness-over-model`, matching the batch-5/6 counter-evidence treatment (scaffolding shrinking as models improve).
4. Two signals form `pat-model-not-bottleneck` — deliberate: capability-overhang and the question-tool progression are distinct evidence lines (tool-affordance unlock vs generation-over-generation interaction jumps). Merge if the reviewer finds them redundant.
5. `sig-tradeoffs-collapse` timing facts (weeks→hours, 4-hour deck) are self-reported practitioner testimony, not measurements.
6. "AI-native organization" candidate (registry batch-3/5/6): "tradeoffs are not real" as stated Anthropic culture + "be unreasonable / do all of it" is soft further resonance; flagged only, no edges.
