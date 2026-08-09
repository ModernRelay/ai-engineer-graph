# SPIKE extraction — "Claude Fable, Claude Tag, and Anthropic's Culture" (Cat Wu & Thariq Shihipar, ft. Simon Willison) — FOR REVIEW

Source transcript: `transcripts/wu-shihipar-anthropic-culture.txt` (auto-captions — quotes are paraphrases, not verbatim; interview/panel format, ~10.4k words — speaker attribution per captions where possible, see Review notes).
Video: https://youtu.be/uU5Gv2h8-9g — AI Engineer World's Fair, published 2026-07-15.
`stagingTimestamp` for the artifact and all signals: 2026-07-15 (publish date).
Entities marked **[registry]** are already in the registry; **[this batch]** are defined in another file of this 5-talk batch.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-wu-shihipar-anthropic-culture` | Claude Fable, Claude Tag, and Anthropic's Culture (Cat Wu & Thariq Shihipar, interviewed by Simon Willison — AI Engineer World's Fair) | youtube | https://youtu.be/uU5Gv2h8-9g |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-cat-wu`, `ContributedByExpert → exp-thariq-shihipar`, `ContributedByExpert → exp-simon-willison`.

## Experts (3 new)

| slug | name | edges |
|---|---|---|
| `exp-cat-wu` | Cat Wu (product, Claude Code / Claude Tag / Cowork, Anthropic) | `AffiliatedWithCompany → co-anthropic` **[registry]** |
| `exp-thariq-shihipar` | Thariq Shihipar (Claude Code team, Anthropic) | `AffiliatedWithCompany → co-anthropic` **[registry]** |
| `exp-simon-willison` | Simon Willison (independent researcher/blogger; interviewer here; notable individual — also cited in Meijer's talk for the "lethal trifecta") | — (independent; no affiliation edge) |

## Companies (0 new)

- `co-anthropic` **[registry]** — `RelevantCompany` target for all signals below.

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-claude-code` | Claude Code | product | harness | Anthropic's terminal coding agent; launched February 2025 as a bullet point on the Sonnet 3.7 launch, now the center of an agentic product family (Claude Tag, Cowork, workflows, remote control, sub-agents); built and maintained using itself | 
| `el-claude-tag` | Claude Tag | product | harness | Claude living in team collaboration tools (launched publicly in Slack the week before this talk): multiplayer by default (whole channel steers one session), proactive rather than reactive (standing instructions like "monitor bug reports in this channel, put up a PR, tag the last-touching engineer"), with channel-scoped team memory (markdown file per channel); positioned internally as "the evolution of Claude Code" |
| `el-claude-fable` | Claude Fable | product | inference | Anthropic frontier model released around this conference; described as a step change: one-shots many product features, enables ~80% system-prompt reduction, does long-horizon multimodal work (autonomous video editing incl. dynamic cropping, transcript sync, HTML-slide substitution). Related registry node: `el-claude-mythos-preview` **[registry]** — captions have the speaker start to say "mythos" then self-correct to "fable", suggesting Mythos was the preview name (flagged, not merged) |
| `el-claude-auto-mode` | Claude Code auto mode | technology | security | Permission layer replacing manual prompts: a Sonnet classifier judges every tool/bash call against conversation context and the user's own dynamic instructions ("don't push"), and adjudicates sandbox escapes (e.g. network requests); internal-only since January 2026, hardened via commissioned red teams and thousands of evals before public rollout; the layer that makes Claude Tag's exposure to whole-channel input viable |

Element edges: all four `IdentifiedInArtifact → ia-aie-wu-shihipar-anthropic-culture`; all four `DevelopedByCompany → co-anthropic`; `el-claude-tag` `UsesElement → el-claude-auto-mode`; `el-claude-tag` `UsesElement → el-claude-code`; `el-claude-auto-mode` `EnablesPattern → pat-new-cyber-threats` **[registry]** (as a defense productized against them).

## Signals (6 new)

All: `SpottedInArtifact → ia-aie-wu-shihipar-anthropic-culture`, `SourcedFromSource → source-aie-yt`, `RelevantCompany → co-anthropic`.

| slug | domain | name / brief | FormsPattern |
|---|---|---|---|
| `sig-claude-tag-65pct-product-prs` | harness | Anthropic's internal Claude Tag lands 65% of the product engineering team's PRs; work splits into Claude Code for complex interactive tasks vs Tag for proactive background work; a large share of sessions are multiplayer (PM tags in Claude, then design, then eng to take it to prod) | `FormsPattern → pat-accelerated-research` **[registry]** |
| `sig-anthropic-removing-humans-from-review` | harness | Anthropic is deliberately moving humans out of the code-review loop: code owners still manually review core paths (e.g. the system prompt), but outer-layer changes are now fully reviewed by automated Claude code review — reached via a 6+-month trust ladder (measure categories where automation catches 100% of issues, then remove the human; incident-causing PRs become permanent review-eval regressions) | `FormsPattern → pat-verification-gap` **[registry]** |
| `sig-system-prompt-cut-80pct` | harness | With Opus 4.8 and Fable, the Claude Code system prompt shrank ~80%: examples removed (frontier models are more creative without them), "do not" constraints replaced with context, and system prompts are now per-model — older models keep the full prompt while frontier models run on judgment instead of instruction | ContradictsPattern → `pat-harness-over-model` **[registry]** (counter-evidence: as models improve, deterministic scaffolding is being deleted, not added) |
| `sig-auto-mode-mitigation-claim` | security | Anthropic claims auto mode has mitigated every attack its commissioned red teams found (adversarial environments, prompt injection, data exfiltration) with risk "far lower than the average human reviewer" (paraphrase); nearly everyone inside Anthropic runs auto mode; supporting evals promised for publication in the coming weeks | `FormsPattern → pat-new-cyber-threats` **[registry]** |
| `sig-idea-to-ship-one-week` | harness | The PRD-first process (6 months of customer interviews → spec → code) has inverted; idea→ship is down from 6–12 months to ~a week, so Anthropic pushes engineers to develop business and product sense — value shifts to taste about what is worth building, execution weight drops (infra excepted) | `FormsPattern → pat-value-of-judgement` **[this batch]** (defined in `osmani-engineer-of-the-future.md`) |
| `sig-rewrites-now-good` | harness | The "never rewrite" law of the mythical-man-month era is inverted at Anthropic: with a good test suite, rewrites and parallel candidate implementations are cheap and beneficial — Bun has been rewritten in Rust and Claude Code runs on it internally; the codebase is treated as the only complete spec, distillable into other versions | `FormsPattern → pat-accelerated-research` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-codebase-is-the-spec` | A codebase is a spec — often the only complete copy of the spec you have; once verification lives in the test suite rather than in humans reading code, you can regenerate implementations (full rewrites, three parallel candidates, ports to other languages) and select by evidence | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-claude-code` |
| `ins-multiplayer-ai-raises-the-bar` | Making AI use visible and multiplayer (public channels, shared sessions) creates social accountability that levels up how everyone uses the tool and suppresses slop — "you want to do work you're proud to do in public"; team norms transmit by observation rather than policy | `HighlightsPattern → pat-value-of-judgement` **[this batch]** | `ReliesOnElement → el-claude-tag` |

## KnowHow (4 new)

All `SourcedFromArtifact → ia-aie-wu-shihipar-anthropic-culture`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-prompt-frontier-models` | Prompt frontier models with context, not constraints | Remove examples — frontier models (Opus 4.8/Fable-class) are more creative without them; prefer context over "do not X" (hard constraints collide confusingly with later user/skill instructions); audit every instruction for the 10% of cases where it's wrong and soften until it's 100% accurate ("always verify" → when/why verification helps), because the model receives it 100% of the time; maintain per-model system prompts — weaker models still need the verbose version | `ReferencesElement → el-claude-fable` |
| `how-earn-automated-code-review` | Earn your way out of human code review | Start with human review of everything + automated review on every PR; measure per-file-category whether automation catches 100% of issues and remove humans only there; keep code owners on critical cores; on every incident, update the reviewer to catch that class and add the offending PRs to a review eval set so it never regresses; expect ~6 months of investment, not an overnight switch | `ReferencesElement → el-claude-code` |
| `how-credential-injection-for-agents` | Make credentials usable but not accessible to agents | Don't hand the agent the Datadog (etc.) token: a credential-management proxy injects the real secret on the fly when the agent calls the API, so the credential is usable by but never readable from the agent; provision Claude its own identity/credentials rather than acting as the user, which also gives clean audit trails | — |
| `how-dogfood-ship-bar` | Gate launches on internal usage, not roadmap | Dogfood daily and fix your own product rather than route around it; roll out to the whole company + brutally honest early customers first; hold features to an explicit internal bar of active users and retention before public ship — unpolished features churn and thereby self-block; keep behavioral evals (not just capability evals) for how the product feels, fed by ranked user complaints | — |

## Dropped

- Remote control (couch-driven mobile control of a local Claude Code session, trusted devices) and workflows (orchestrated sub-agent prompting; also used for climbing-trip research) — product-feature color; kept as prose in element/signal briefs, no nodes.
- Cowork mention ("implement this new feature in co-work") — registry `el-claude-cowork` exists; passing reference only, no edge.
- Opus 4.8 — load-bearing only jointly with Fable for the prompt-cut signal; kept in prose, not coined (registry pattern: `el-claude-opus-47` exists from batch 2; central reviewer may want an `el-claude-opus-48`).
- Street Fighter game / climbing app closing anecdotes, Gemini image generation, "sea dance" video model (garble, likely Seedance) — color.
- Eval-tooling audience Q&A ("skill of building evals, not tooling, is the constraint") — folded nowhere; could be promoted to an insight if reviewer wants a third.

## Review notes

1. **Name garbles resolved from official title**: "Theik Shihipa" → Thariq Shihipar; "Cat Woo" → Cat Wu; "claw tag / quad tag / quag" → Claude Tag; "quad code / cloud code" → Claude Code. "Opusport" (the model that prompted "I need to work at Anthropic") is likely "Opus 4"; unresolved. "Dell was working on a post" — unknown Anthropic person, unresolved. "Ken and Boris" — Boris Cherny + likely Cat ("Kat")/Ken, unresolved. "Jared ... rewrote all of Bun into Rust" = Jarred Sumner (Bun creator).
2. **Attribution**: captions mark speaker turns with ">>" but not names. The 65%-PRs, code-review ladder, auto-mode claims, dogfooding bar, and remote-control story read as Cat Wu; system-prompt/tools/video-editing material reads as Thariq Shihipar; framing questions and the "models write my prompts now" observations are Willison. Signals are attributed to "Anthropic (Wu/Shihipar)" jointly to stay safe.
3. `sig-system-prompt-cut-80pct` uses **ContradictsPattern** against `pat-harness-over-model` — deliberate: it's the strongest counter-evidence yet recorded for that pattern (scaffolding shrinking as models improve). Swap to a FormsPattern on `pat-model-not-bottleneck` if the reviewer prefers positive edges — that reading also fits.
4. Mythos/Fable: kept `el-claude-fable` separate from registry `el-claude-mythos-preview`; the caption self-correction ("with like mythos and uh sorry with fable") hints they are preview/release names of the same line — merge decision is central.
5. `sig-auto-mode-mitigation-claim` records a vendor claim ("mitigated every attack") explicitly as a claim; the promised eval publication is the verifiable follow-up.
6. "AI-native organization" (un-coined batch-3 candidate, Tan): this talk is further resonance — 65% agent PRs, multiplayer sessions, automated launch calendars, humans-out-of-review. Flagged only; no edges.
