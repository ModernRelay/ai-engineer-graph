# SPIKE extraction — "Build AI Systems for Discernment, Not Approval" (Angel Ortmann Lee, Duolingo) — FOR REVIEW

Source transcript: `transcripts/ortmann-lee-duolingo-discernment.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/CDqzWpwkSls — AI Engineer World's Fair, published 2026-07-07.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-07-07 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-ortmann-lee-discernment` | Build AI Systems for Discernment, Not Approval (Angel Ortmann Lee, Duolingo — AI Engineer World's Fair) | youtube | https://youtu.be/CDqzWpwkSls |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-angel-ortmann-lee`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-angel-ortmann-lee` | Angel Ortmann Lee (software engineer, Duolingo; security for the Duolingo English Test) | `AffiliatedWithCompany → co-duolingo` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-duolingo` | Duolingo | developer | language-learning company; operates the Duolingo English Test (DET) — fully online, remotely proctored, high-stakes English proficiency exam trusted by ~6,000 programs; combines AI cheating-detection models with human proctor review |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-automation-bias` | Automation bias | concept | harness | Human tendency to defer to an automated/AI signal instead of exercising independent judgment — the reviewer becomes a rubber stamp. The failure mode human-in-the-loop systems must be designed against; Wharton's "cognitive surrender" (adopting AI output as one's own with minimal scrutiny) is the same phenomenon |
| `el-interactions-as-labels` | Interactions as labels | concept | harness | Treating every human-AI interaction (approve / reject / modify / override / follow-up question) as a label: intentionally structured interactions are a system property that yields high-quality training and eval data — a compounding flywheel. Unstructured rubber-stamp UIs log false positives as truth, making the model more confident and the human more deferent |

Element edges: both `IdentifiedInArtifact → ia-aie-ortmann-lee-discernment`; `el-automation-bias` `ExemplifiesPattern → pat-verification-gap` **[registry]**.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-ortmann-lee-discernment`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-duolingo-proctor-rubber-stamp` | Duolingo English Test injected fake AI copy-typing flags into clean historical sessions inside proctors' normal workflow: reviewers who consistently score >90% on accuracy calibration upheld ~50% of the fake flags — coin-flip automation bias inside the human verification layer of a high-stakes exam feeding college-admission and visa decisions | `FormsPattern → pat-verification-gap` **[registry]** | `RelevantCompany → co-duolingo` |
| `sig-duolingo-guideline-copy-fix` | Changing only the proctor guideline copy (the AI signal is a preliminary alert; you are the final decision-maker; find independent evidence in the video before upholding) moved fake-flag rejection from ~50% to ~71% — a 21-point improvement with zero model changes and zero UI changes (the model was already at ~1% false-positive rate; the people were already skilled) | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-duolingo` |
| `sig-wharton-cognitive-surrender` | Wharton study on AI-assisted reasoning exams: ~80% of participants accepted AI answers even when wrong; when the AI was right human performance rose ~25 points, when wrong it fell ~15 — "cognitive surrender": AI supplants rather than supplements thinking, and the human may not notice it happening | `FormsPattern → pat-verification-gap` | — |
| `sig-coding-agent-rubber-stamp-uis` | Practitioner observation: out-of-the-box coding agents converge on two interaction patterns — one giant end-to-end diff, or approve-pings on every file change — and both reduce the developer to a rubber stamp, logging accept-skewed binary labels on code blocks instead of rich structured decisions (bad assumptions, trade-offs, stylistic preferences) that could actually improve the system | `FormsPattern → pat-verification-gap` | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-design-for-discernment` | Sometimes the fix is neither a better model nor more oversight but the interaction itself: reframe the human as investigator rather than validator, require independent evidence, surface assumptions and trade-offs early, split compound questions (was the detection correct? vs. should we penalize? — headphones detected may be a hearing aid). Discernment is a designable property of the interface | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-automation-bias` |
| `ins-interface-determines-labels` | Human-in-the-loop is a cycle, not a line: model → interaction → human behavior → data → next model. The interface determines which labels get logged — rubber-stamp UIs breed a vicious cycle (confident model, deferent human, false positives logged as truth), while structured, friction-matched interactions surface honest disagreement that compounds into targeted model improvement | `HighlightsPattern → pat-model-not-bottleneck` | `ReliesOnElement → el-interactions-as-labels` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-ortmann-lee-discernment`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-design-for-discernment` | Design human-AI review for discernment, not approval | State in guidelines that the AI signal is preliminary and the human is the final decision-maker; require independent evidence before upholding a flag; split compound CTAs into "was the detection correct?" and "is this a violation?"; match friction to stakes — deliberate review gates and speed bumps where stakes are high, seamless frictionless flow where oversight is low; prefer structured inputs/outputs (inline markup like the writing-tutor UI, forms, tables) over walls of text; make agents plan, ask good questions, and ship reviewable increments like a good junior developer | `ReferencesElement → el-automation-bias` |
| `how-instrument-interactions-as-labels` | Instrument the interaction as your labeling system | Stop asking "how do I evaluate the model" after building — define success, concrete metrics, and the data needed to improve before designing the interaction; capture the diff when a human modifies or overrides output (a bare "yes" followed by manual edits logs a false positive that pollutes the dataset); log explanation/follow-up questions and their sentiment as low-trust indicators; collect explicit feedback at the right touchpoints with nuance, not thumbs up/down | `ReferencesElement → el-interactions-as-labels` |

## Dropped

- "When Machines Mislead" (Duolingo's published case study) — kept as prose context of the proctor experiment, not a separate artifact node (the talk is the artifact; the paper wasn't linked).
- The Duolingo-style writing tutor and headphone-detection screenshots — product illustrations, folded into insight/knowhow prose.
- GPS / phone-contacts / Gemini-search-summary trust anecdotes — scene-setting only.
- Wharton (UPenn) as a Company node — study attribution only, no org activity claimed.

## Review notes

1. Speaker name garbled as "Angel Ermanlee" in captions; used the official listing "Angel Ortmann Lee" (`exp-angel-ortmann-lee`).
2. All study numbers (50%→71%, +25/−15 points, 80% acceptance, 1% FPR, 6,000 programs) are auto-caption paraphrases — verify against Duolingo's published "When Machines Mislead" before public-facing use.
3. Per the batch hint, checked against `pat-value-of-judgement`: confirmed — the talk's thesis (engineer interfaces so human judgment survives AI assistance) is linked via `ins-design-for-discernment`. The empirical signals mostly evidence `pat-verification-gap` (the human verification layer itself failing); both patterns used, no tension.
4. `sig-duolingo-guideline-copy-fix` → `pat-model-not-bottleneck` follows the speaker's own framing ("the problem was not the model, not the people — the interface"). Re-home to `pat-harness-over-model` if you read guideline copy as harness scaffolding.
5. `el-automation-bias` is a long-standing HCI term, not AI-native — kept as an Element because two signals and a KnowHow lean on it (same call as batch-2's `el-semantic-layer`); drop to prose if too generic.
