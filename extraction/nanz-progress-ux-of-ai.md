# SPIKE extraction — "The UX of AI: Making AI-Powered Apps Your Users Don't Hate" (Kathryn Grayson Nanz, Progress Software) — FOR REVIEW

Source transcript: `transcripts/nanz-progress-ux-of-ai.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/L3RuP_q8Bwc — AI Engineer World's Fair, published 2026-07-18.
`stagingTimestamp` for the artifact and all signals: 2026-07-18 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-nanz-ux-of-ai` | The UX of AI: Making AI-Powered Apps Your Users Don't Hate (Kathryn Grayson Nanz, Progress Software — AI Engineer World's Fair) | youtube | https://youtu.be/L3RuP_q8Bwc |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-kathryn-grayson-nanz`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-kathryn-grayson-nanz` | Kathryn Grayson Nanz (senior design & developer advocate, Progress Software; does user research on AI features) | `AffiliatedWithCompany → co-progress-software` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-progress-software` | Progress Software | developer | developer-tools/software company (Telerik/Kendo UI lineage); appears here via its design-advocacy user research on AI features, not as an AI vendor |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-ai-ux-pillars` | Five pillars of AI UX (trust, clarity, control, transparency, meaningful benefit) | concept | harness | User-research-derived framework grouping the main challenges users have with AI features into five categories, each with concrete interface patterns: trust (citations, plan approval, AI-content labeling), clarity (streaming, think-out-loud, change highlighting), control (emergency stop, undo/version history, granular revert), transparency (granular revocable permissions, cost/time estimates, agent-driving indicators), meaningful benefit (suggested prompts, next-step actions, workflow integrations) |

Element edges: `el-ai-ux-pillars` `IdentifiedInArtifact → ia-aie-nanz-ux-of-ai`; `EnablesPattern → pat-model-not-bottleneck` **[registry]** (the experience layer is where differentiation now happens).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-nanz-ux-of-ai`, `SourcedFromSource → source-aie-yt` **[registry]**. Domain `harness`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-ai-knowledge-gap-widest` | Practitioner user research: the developer–user knowledge gap around AI (prompting, hallucinations, RAG, iteration) is the widest the speaker has seen for any technology; users face AI bolted onto everything, and each sub-par AI-feature experience lowers their willingness to try again — builders get a limited number of chances before users disengage entirely | `FormsPattern → pat-model-not-bottleneck` **[registry]** (adoption, not capability, is the constraint) | `co-progress-software` |
| `sig-ux-is-the-differentiator` | Explicit industry claim from a mainstream software vendor: "the models are already really good and keep getting better — the differentiator for AI-powered software isn't performance anymore, it's the quality of the experience built around it"; the design/development line is blurring and UX questions now fall on developers regardless of title | `FormsPattern → pat-model-not-bottleneck` | `co-progress-software` |
| `sig-ai-interface-patterns-unsettled` | Standardized, familiar AI interaction patterns don't exist yet and can't be delegated to AI itself: models only remix existing patterns, so AI-generated UI trends toward the average and there's no long history of AI-native interfaces to reference — inventing these patterns is, for now, a human design problem | `FormsPattern → pat-model-not-bottleneck` | — |
| `sig-verification-affordances-required` | Because no tool can claim to be hallucination-free, product teams are building verification affordances instead of trust claims: citations with tooltips/inline links/side panels linking back to sources, plan-approval gates before agentic action (now a common flow in Claude/ChatGPT), and explicit AI-generated-content labeling — "trust, but verify" designed into the interface | `FormsPattern → pat-verification-gap` **[registry]** | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-ai-ux-at-system-3` | Macintosh analogy: the GUI succeeded by meeting unfamiliar users with borrowed real-life vocabulary and literal icons, then shed abstractions (System 1 → System 6) as literacy grew. AI UX today is "around System 3": users have transferable mental models (chat ≈ messaging) but interfaces must adapt them (sources, stop/pause, agentic tools) and graduate users gradually rather than assume expertise | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-ai-ux-pillars` |
| `ins-trust-is-engineered-not-claimed` | Where you cannot promise truth, you must engineer verifiability: honesty about limitations plus patterns that let users see, check, and correct AI output (citations, visible chain of thought, undo/version history) earns more trust than positioning your tool as the exception to hallucination — and uncited output simply doesn't get reused in users' real work | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-ai-ux-pillars` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-nanz-ux-of-ai`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-earn-ai-feature-trust` | Earn trust through verifiability and honesty | Cite sources (tooltips for quotes, links for external, side panels for research work); show agentic action plans and get approval before execution (with always-allow settings for repeat flows); label AI-generated content (disclaimer, watermark, asterisk) instead of letting users feel it was snuck in; indicate which parts of output need manual verification; stream output and have the model think out loud so users can assess mid-generation and pinpoint where things went wrong | `ReferencesElement → el-ai-ux-pillars` |
| `how-keep-user-in-control` | Keep the user in the driver's seat | Provide a prominent "emergency brake" to halt any AI process (never buried in a menu or behind a remembered command); make version history non-negotiable for non-deterministic output — scale it to the task (rephrase-and-retry → undo/redo of ~10 steps → checkpoints/save states) with granular, targeted revert; make permissions granular, contextual, and revocable (read vs write vs delete; once vs always; per-folder), with a visible history of what was granted when; give rough time/token/cost estimates before users commit; show a clear visual signal (banner/outline) whenever an agent is driving | `ReferencesElement → el-ai-ux-pillars` |

## Dropped

- Copilot research-agent vs Teams chat comparison, Macintosh System 1/6 control panels, XKCD "my code's compiling", Nielsen's safe-exploration heuristic, sparkle-icon critique, Jurassic Park quote — illustrations; folded into signal/insight prose or omitted.
- "AI-generated UI looks average" as its own Element — kept as prose in `sig-ai-interface-patterns-unsettled` (adjacent to batch2 `el-generative-ui` but a critique, not the mechanism; no edge forced).
- Data-collection/memory-forgetting discussion — folded into the permissions guidelines of `how-keep-user-in-control`.

## Review notes

1. This is a patterns-and-practice talk with almost no external dated facts; signals are practitioner-research observations and explicit industry claims. If that fails your signal bar, keep `sig-ux-is-the-differentiator` + `sig-verification-affordances-required` and demote the other two to insight prose.
2. Pattern candidate NOT coined: a recurring "AI adoption/UX gap" thesis (users' AI literacy lags builders'; adoption—not capability—is the constraint) shows up here strongly but in this batch only in this talk — flagged without coining, no edges. Its evidence is meanwhile routed to `pat-model-not-bottleneck`, which absorbs the "value moved to the experience layer" half cleanly.
3. Speaker name is not spoken in full in the captions ("Hi, my name is Kat"); expert node uses the official title's Kathryn Grayson Nanz.
4. `el-ai-ux-pillars` has no clean schema domain (no "ux" enum value); `harness` chosen as the layer-around-the-model. Leave null if you disagree.
