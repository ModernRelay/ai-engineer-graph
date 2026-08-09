# SPIKE extraction — "Browser Agents Don't Need Better Models. They Need Better Eyes." (Kushan Raj, ARK) — FOR REVIEW

Source transcript: `transcripts/raj-ark-browser-agents-better-eyes.txt` (auto-captions — quotes are paraphrases, not verbatim). Very short talk (~940 words).
Video: https://youtu.be/JnubYCYunk8 — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact and all signals: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
NOTE (review 2026-07-22): `pat-html-native-medium` was demoted to element `el-html-native-medium`; the one flagged edge in this file is dropped per its own Review note 3 (input-side stretch).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-raj-better-eyes` | Browser Agents Don't Need Better Models. They Need Better Eyes. (Kushan Raj, ARK — AI Engineer World's Fair) | youtube | https://youtu.be/JnubYCYunk8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-kushan-raj`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-kushan-raj` | Kushan Raj (ARK; previously founding engineer at Seraphim for 2 years) | `AffiliatedWithCompany → co-ark` |

## Companies (1 new)

| slug | name | type | brief |
|---|---|---|---|
| `co-ark` | ARK | developer | Browser-agent infrastructure project by Kushan Raj — fast, cheap, reliable browser agents via a compressed full-page representation plus state-diff feedback; pre-launch (plans: open-source the code, expose "URL + intent → execution" as an API/plugin). ⚠ Name from the official talk listing only — the transcript never says "ARK" (see Review notes) |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-compressed-page-markdown` | Compressed markdown page representation | technology | harness | ARK's browser-agent perception layer (speaker never names it — descriptive name ours): renders the entire web page as ~1.8k tokens of markdown (vs ~20k tokens of raw DOM, or ~1.1k tokens for a screenshot that shows only one viewport snippet), paired with a screenshot and explicit state-diff feedback — what appeared, what's gone, that a blocking element was removed, that an attempted click didn't land — so a cheap model can see the whole page, diagnose failures, and plan long action sequences |

Element edges: `IdentifiedInArtifact → ia-aie-raj-better-eyes`; `DevelopedByCompany → co-ark`; `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

## Signals (3 new — very short talk)

All: domain `harness`, `SpottedInArtifact → ia-aie-raj-better-eyes`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | Pattern edges | RelevantCompany |
|---|---|---|---|
| `sig-browser-agents-adoption-gap` | Practitioner: browser agents are barely adopted despite the excitement — the speaker doesn't use them himself; on a 30-step browser-agent benchmark a mainstream agent burned 10–20 seconds just clicking the start button, and in his tests a frontier-model screenshot loop spent 2 minutes on a single-button download (screenshot → scroll → screenshot → stuck) without finishing. Title thesis verbatim-ish: "models are pretty smart, but it's the infra around them that sucks" | `FormsPattern → pat-model-not-bottleneck` **[registry]** | — |
| `sig-compressed-page-token-math` | The representation numbers: full DOM ≈ 20k tokens; a screenshot ≈ 1.1k tokens but shows only one snippet; ARK's markdown ≈ 1.8k tokens and covers the entire page — with it a much cheaper model completed tasks (downloading an Aadhaar ID document, booking a Canadian trekking date) fast, where Claude driving screenshots stalled or failed on the same sites | `FormsPattern → pat-harness-over-model` **[registry]** (html-native edge dropped at review; see Review note 3) | `RelevantCompany → co-ark` |
| `sig-page-state-diff-feedback` | Environment feedback as the fix for long sequences: the harness tracks page state end-to-end and tells the agent what just appeared, what disappeared, that the element blocking its target is gone, and that its click didn't happen — turning "agent debugging blind against a mute page" into an environment where it can locate failures and plan a long task sequence correctly | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-ark` |

## Insights (1 new — short talk)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-perception-is-the-bottleneck` | For browser agents the binding constraint is perception, not intelligence: a compressed full-page text view at ~1/10th the DOM's token cost beats frontier-model screenshot loops on speed, cost, and completion — upgrading the model cannot fix what its representation hides (a screenshot shows one viewport; the DOM drowns the signal). "Better eyes" beat "better brains" | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-compressed-page-markdown` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-raj-better-eyes`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-browser-agent-perception` | Give browser agents better eyes, not bigger models | Compress the page into a ~2k-token markdown representation covering the whole page (vs ~20k raw DOM) and pass it alongside a screenshot; keep end-to-end page-state tracking in the harness; feed explicit diffs each step — new elements, removed elements, cleared blockers, clicks that didn't land — so the agent can diagnose failure instead of blindly re-screenshotting; once the representation is right, downshift to cheaper models for speed and cost | `ReferencesElement → el-compressed-page-markdown` |

## Dropped

- "The browser challenge" — the 30-step benchmark he demos against; captions don't identify it well enough to node (see Review notes); prose inside `sig-browser-agents-adoption-gap`.
- Claude as the comparison agent in both failure demos — prose (no edge; which Claude product/harness is unstated).
- Seraphim — the speaker's *previous* employer, mentioned once as bio; not coined.
- Aadhaar (India's national ID) and the Canadian trekking-booking site — task examples, folded into `sig-compressed-page-token-math`.
- Open-sourcing / "URL + intent" API / plugin plans — intentions, not shipped artifacts; folded into the `co-ark` brief.

## Review notes

1. **Company identification:** the transcript only says "I worked at Seraphim as a founding engineer for 2 years" (past tense) and never names the current project; `co-ark` comes from the official talk listing. Verify ARK is a company vs a project name before public-facing use.
2. **Title-as-thesis:** the talk title is a direct `pat-model-not-bottleneck` statement and the content is textbook `pat-harness-over-model` (environment/representation engineering over model upgrades) — both linked, per the extraction brief.
3. **RESOLVED at review 2026-07-22 — edge dropped (pattern demoted centrally; this note's drop condition applied).** Original note: the representation is markdown (not HTML) and it's agent *input* (perception), not output. Included because the pattern (as defined in the russo file) covers "agent perception moves from pixels and raw DOM to compressed markup" — the shared claim is text-structured web medium over pixels. Drop this one edge if review reads the pattern output-only.
4. All numbers (token counts 20k/1.1k/1.8k, timings) are speaker-reported demo measurements via auto-captions — order-of-magnitude claims, not audited.
5. `el-compressed-page-markdown` is our descriptive name — the speaker never names the representation; rename freely at seeding.
6. Candidate patterns from the central ledger: no new evidence in this talk.
