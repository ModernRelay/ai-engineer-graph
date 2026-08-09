# SPIKE extraction — "Running a Chess YouTube Channel entirely by AI" (Stephan Steinfurt, TNG) — FOR REVIEW

Source transcript: `transcripts/steinfurt-tng-ai-chess-channel.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/BqZrTdgBaPw — AI Engineer World's Fair, published 2026-07-08.
`stagingTimestamp` for the artifact and all signals: 2026-07-08 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-steinfurt-chess-channel` | Running a Chess YouTube Channel entirely by AI (Stephan Steinfurt, TNG — AI Engineer World's Fair) | youtube | https://youtu.be/BqZrTdgBaPw |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-stephan-steinfurt`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-stephan-steinfurt` | Stephan Steinfurt (TNG Technology Consulting, Munich; builds the AI chess-explanation agent and runs its automated YouTube channel) | `AffiliatedWithCompany → co-tng` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-tng` | TNG Technology Consulting | developer | German tech consultancy (Munich) known for AI showcase projects; here operating a fully automated AI chess YouTube channel. |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-chess-explainer-agent` | TNG chess explainer agent | product | harness | TNG's automated chess-video pipeline: nightly Lichess game download → background analysis → tool-using agent that explores the game in depth (legal-move tool to bar illegal reasoning; an interactive board it can play/take back/branch on; chess-engine evaluation on demand; a checks-captures-threats saliency tool; human-move models; web search for historical context) → intermediate explanation format → rendered video with ElevenLabs V3 narration (audio tags for excitement). The agent itself decides which squares to highlight, which arrows to draw, and what counts as a brilliant move; videos upload automatically every night. |
| `el-gemini-31-pro` | Gemini 3.1 Pro | product | inference | Google's recently released frontier model (caption garble — see notes); per TNG the best chess model observed so far — reasoning traces show genuinely better positional understanding, suspected chess-specific post-training. Powers the chess explainer agent. |

Element edges: both `IdentifiedInArtifact → ia-aie-steinfurt-chess-channel`; `el-chess-explainer-agent` `DevelopedByCompany → co-tng`, `UsesElement → el-gemini-31-pro`, `ExemplifiesPattern → pat-harness-over-model` **[registry]**; `el-gemini-31-pro` `DevelopedByCompany → co-google-deepmind` **[registry]**.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-steinfurt-chess-channel`, `SourcedFromSource → source-aie-yt` **[registry]**. Domain per row.

| slug | name / brief | domain | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-chess-holy-grail-already-automated` | ~One week before the talk (early July 2026), one of Germany's biggest newspapers quoted chess trainer Wilhelm Weber calling AI that explains chess as well as a human trainer "the holy grail of chess programming" — possibly 5 more years away — while TNG in Munich was already auto-producing and auto-uploading such explainer videos nightly, no human in the loop | harness | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-tng` |
| `sig-engine-llm-tool-bridge` | Chess engines have been superhuman for decades but can't explain; LLMs explain but can't play. TNG bridges them with a tool harness: ground truth (legal moves, engine evals) plus deliberately diverse, even conflicting context (checks/captures/threats candidates, rating-conditioned human-likely moves, game history) fed to the model, which narrates for humans — covering instructive bad moves, not just the engine's best line | harness | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-tng` |
| `sig-reasoning-models-absorbed-pipeline` | The division of thinking flipped within about a year: the pre-reasoning-model pipeline was Python scripts assembling position analysis for an LLM to verbalize; since reasoning models arrived, the model explores variations and decides which tools to call itself (best chess model autumn 2025: Grok 4; now Gemini 3.1 Pro, visibly stronger in reasoning traces, suspected chess post-training) — hand-built scaffolding retired as capability moved into the model | inference | `ContradictsPattern → pat-harness-over-model` **[registry]** (see notes) | — |
| `sig-chess-video-unit-economics` | Auto-generated explainer videos cost ~€0.20–0.30 each (longer formats: a few euros) with ~1-in-20 having a defective description; the operator moved from pre-watching every video to publish-first / take-down-later. Channel at ~500k views and >4,000 subscribers, most gained in the final month; positioned for the long tail — videos of amateurs' own games, which human streamers like GothamChess would never cover; not yet monetized (net negative) | harness | — (pattern-less; see notes) | `RelevantCompany → co-tng` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-conflicting-context-yields-human-explanations` | The craft is context curation, not model choice: feeding the model the best move AND human-plausible alternatives (checks/captures/threats, rating-conditioned Maia-style moves, historical games) produces explanations of what a human would actually consider, instead of engine-line dumps. The harness decides what information exists; the model decides what matters and how to tell it | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-chess-explainer-agent` |
| `ins-cheap-generation-flips-qa-posthoc` | At ~30 cents per video and a ~5% defect rate, per-item human review costs more than it saves: QA flips from pre-publish gate to post-publish takedown, and each defect becomes diagnostic signal (e.g., a missed tool call at game end) rather than a reason to gate. Verification economics, not capability, now set the human's role | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-chess-explainer-agent` |

## KnowHow (1 new)

All `SourcedFromArtifact → ia-aie-steinfurt-chess-channel`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-domain-explainer-agent` | Build an explainer agent for an engine-solved domain | Constrain hallucination with a hard legality tool (never let the model reason about illegal moves); give it an interactive domain sandbox (board with play/undo/variations) rather than static pre-computed analysis; expose engine evaluation on demand, not as the only truth; add a candidate-saliency tool (checks/captures/threats) so coverage includes plausible-but-bad moves a human would consider; mix in human-move models (Maia-style, rating-conditioned) and web history to target the audience's level; let the agent drive presentation (square highlights, arrows, brilliancy labels, excitement tags in ElevenLabs V3 TTS); don't optimize cost early — err toward too-good analysis and tolerate redundant tool calls | `ReferencesElement → el-chess-explainer-agent`, `ReferencesElement → el-gemini-31-pro` |

## Dropped

- Maia engine (University of Toronto rating-conditioned human-move model; captions say "Maya") — supporting mention, kept in prose within signals/KnowHow rather than coined.
- ElevenLabs V3 TTS — production dependency, kept in briefs/prose rather than coined.
- GothamChess — color reference for the long-tail argument.
- Audience-Q&A details (monetization stage, per-video count decisions, other games "not yet") — folded into `sig-chess-video-unit-economics` or dropped.

## Review notes

1. **Model-name garble:** captions say "Gemini 3 but 1 Pro… which recently came out" — read as **Gemini 3.1 Pro** and slugged `el-gemini-31-pro`; verify before seeding. "Chess post-training" is the speaker's inference from reasoning traces, not a Google claim.
2. **Deliberate `ContradictsPattern` use:** `sig-reasoning-models-absorbed-pipeline` is counter-evidence to `pat-harness-over-model` — assembly/thinking scaffolding migrated INTO the model when reasoning models arrived, shrinking the harness's job to ground-truth tools. Flip to `FormsPattern` with a nuanced brief if ContradictsPattern is reserved for stronger refutations; the same talk's other two signals support the pattern, which is exactly the tension worth keeping.
3. **`sig-chess-video-unit-economics` left pattern-less:** no existing pattern covers content/media automation economics, and no candidate on the central do-not-coin list matches; nearest resonance is the general "generation cheap, attention/verification scarce" space already carried by the insight's `pat-verification-gap` link. Rehome if a media-automation pattern is ever coined.
4. **Names unverified:** "Wilhelm Weber" (quoted chess trainer) is plausible but caption-only; the newspaper is unnamed ("one of the biggest in Germany", article ~2026-07-01). Grok 4 as best chess model "autumn last year" = autumn 2025, kept as a dated fact inside the signal.
5. The channel itself is unnamed in the talk — element named "TNG chess explainer agent" after the system, not the channel.
