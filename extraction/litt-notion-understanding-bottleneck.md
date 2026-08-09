# SPIKE extraction — "Understanding is the new bottleneck" (Geoffrey Litt, Notion) — FOR REVIEW

Source transcript: `transcripts/litt-notion-understanding-bottleneck.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/WkBPX-oDMnA — AI Engineer World's Fair (design engineering track), published 2026-07-10.
`stagingTimestamp` for the artifact and all dated nodes (signals, knowhows): 2026-07-10 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-litt-understanding-bottleneck` | Understanding is the new bottleneck (Geoffrey Litt, Notion — AI Engineer World's Fair) | youtube | https://youtu.be/WkBPX-oDMnA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-geoffrey-litt`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-geoffrey-litt` | Geoffrey Litt (design engineer at Notion; long-time malleable-software / end-user-programming researcher) | `AffiliatedWithCompany → co-notion` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-notion` | Notion | developer | Collaborative workspace company; appears here shipping agent-native primitives (HTML blocks in pages, coding agents living in docs, multiplayer human+agent threads) and as the shared-understanding thesis owner |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-explain-diff` | ExplainDiff (code-explainer skill) | product | harness | Litt's agent skill (published free at the talk, HTML and Notion variants) that turns a code change into a personalized explainer doc: background/system context first, intuition before details ("the goal of this commit is…"), interactive figures where tasteful, literate code diffs in narrated order — ending in a 5-question spaced-repetition-style quiz that gates whether you understood; used daily by Litt and coworkers at Notion |
| `el-microworlds` | Microworlds (agent-built learning environments) | concept | harness | Seymour Papert's "living in Mathland" applied to codebases: have agents build ephemeral, throwaway UIs whose purpose is your understanding, not shipping — e.g., a scrubber-timeline debugger visualizing every step of a Prolog interpreter's state, or a click-through "video game" that replays a website migration file-by-file so you do the port manually without the pain; the software is disposable, the changed human is the output |

Element edges: both `IdentifiedInArtifact → ia-aie-litt-understanding-bottleneck`.

Reused: `el-cognitive-debt` **[registry]** (Litt cites the term directly — Margaret-Anne Storey's coinage, Simon Willison's blogging of it), `el-claude-code` **[registry]** (prose: "Claude, make me a microworld"; Claude/Cursor in Notion).

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-litt-understanding-bottleneck`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | domain | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-agent-code-outpaces-review` | Whether humans still need to understand code is now a live, debated question: agents land 50,000-line PRs, "code review is the new bottleneck" is common parlance, and the human share of correctness-checking is shrinking as agents get verification loops and check their own work — Litt (pro-understanding) accepts that trend rather than fighting it | harness | `FormsPattern → pat-verification-gap` **[registry]** | — |
| `sig-notion-agent-workspace-launches` | Dated product moves toward shared human+agent workspaces: Notion launched HTML blocks in pages the morning of the talk (agents can embed interactive simulations in docs); the week before, it launched coding agents living inside Notion (Claude and Cursor); Notion's team now builds much of its own code inside Notion for the shared-space benefits — plus multiplayer chat threads where multiple humans and multiple agents converse in one visible space ("one-on-one conversations → Slack channels") and agent-written plan docs that teammates comment on in place | context | — (see review note 3) | `RelevantCompany → co-notion`, `OnElement → el-claude-code` **[registry]** |
| `sig-education-techniques-for-agent-code` | Practitioners are importing education science to keep up with agent-written code: Litt's ExplainDiff (background-first explainer docs + gate-keeping quizzes — his rule: don't send a PR for review unless you can pass the quiz on what your agents wrote; "shocking the number of times this caught me"), Matuschak/Nielsen-style spaced-repetition embedded in essays, and Papert microworlds built by agents on demand; he prints explainer docs and reads them at the cafe "like a textbook about this PR" | harness | `FormsPattern → pat-value-of-judgement` **[registry]** | `RelevantCompany → co-notion`, `OnElement → el-explain-diff`, `OnElement → el-microworlds` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-understand-to-participate` | The reason humans must keep understanding isn't verification — agents are absorbing thumbs-up/thumbs-down correctness checking, and that's fine. It's participation: each loop you actually understand changes you, and that accumulated conceptual structure is what generates the *next* idea; a few layers removed, you can't take creative leaps. Skipping this builds cognitive debt — like tech debt, you get away with it until you suddenly can't participate in your own project | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-cognitive-debt` **[registry]** |
| `ins-understanding-bottleneck-not-generation` | With generation industrialized, the scarce resource is human comprehension speed — so spend the free code *on* comprehension: ephemeral UIs, dynamic simulations, debuggers, and playgrounds built solely to make one person understand one thing. This is Alan Kay's 50-year-old vision (computers to level humans up, kids modifying a game's code to learn physics) finally practical; the optimistic frame is AI putting us more deeply in the loop, not out of it — moving at "the speed of understanding," not just the speed of correctness | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-microworlds` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-litt-understanding-bottleneck`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-explain-diff-workflow` | Generate explainer docs, then gate on a quiz | For every substantial agent change, generate an explainer: background/system context first; intuition before details (essence and examples before code); interactive figures only where they beat static ones (interactivity can be slop); literate code diffs — prose narration in reading order, not a file list. End with a ~5-question medium-difficulty quiz and adopt the rule: you don't send the PR to human reviewers until you pass the quiz on what your agents wrote. Use it as a speed regulator — a system that keeps understanding-speed coupled to shipping-speed; put docs somewhere collaborative (Notion/HTML) so the team can comment | `ReferencesElement → el-explain-diff` |
| `how-agent-built-microworlds` | Have agents build throwaway worlds, not just fixes | When you don't have a feel for a system, don't ask the agent to just fix/do it — ask it to build you a microworld: a bespoke debugger or step-through visualizer of internal state (with a timeline you scrub and annotate), or a game-ified manual walkthrough (old system left, new system right, one step per click, files visibly moving) so you get the peripheral vision of doing it iteratively without the pain; treat the artifact as disposable — the understanding is the deliverable | `ReferencesElement → el-microworlds` |

## Dropped

- The Zen-garden video game and Prolog interpreter specifics — kept only as illustrations inside element/knowhow briefs.
- Andy Matuschak / Michael Nielsen ("Books don't work"), Seymour Papert, Alan Kay, Margaret-Anne Storey, Simon Willison — cited thinkers, prose only (no Expert nodes: not contributors to this artifact; Willison already exists as `exp-simon-willison` **[registry]**).
- Opening room poll (nearly unanimous pro-understanding; "maybe selection bias") — color.

## Review notes

1. **Resonances (per extraction brief):** the talk is a direct complement to `pat-value-of-judgement` — it supplies the *mechanism* (understanding → participation → judgment) for why judgment stays human. It also continues the cognitive-debt thread flagged in batch 3 and coined as `el-cognitive-debt` in batch 5 (Osmani) — Litt cites the exact term and lineage (Storey, Willison), independent of Osmani's talk. Third resonance: `pat-verification-gap` — but Litt's twist is that verification is the *wrong* justification for human review; understanding-to-participate is the durable one.
2. **Pattern candidate flagged, NOT coined (no edges):** "understanding/comprehension as the industry bottleneck" (title thesis) could be read as its own claim, but on one-talk evidence it decomposes cleanly into `pat-model-not-bottleneck` (bottleneck moved out of generation) + `pat-value-of-judgement` (what humans are still for) — filed under those.
3. `sig-notion-agent-workspace-launches` left pattern-less: the launches are concrete/dated but the closest patterns (`pat-context-graphs`? `pat-harness-over-model`?) both feel like stretches for collaborative-workspace features. Reconciler may attach one.
4. "Margaret Stories" in captions = Margaret-Anne Storey (corrected); "explainedif" = ExplainDiff; both confident. No other material garbles.
5. `el-explain-diff` has no `DevelopedByCompany` edge — it's Litt's personal skill (published via QR at the talk), used at Notion but not presented as a Notion product.
