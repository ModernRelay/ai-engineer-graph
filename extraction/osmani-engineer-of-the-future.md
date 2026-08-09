# SPIKE extraction — "The engineer of the future is the person who is able to choose what is worth doing" (Addy Osmani) — FOR REVIEW

Source transcript: `transcripts/osmani-engineer-of-the-future.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/n97BCfyFIvw — AI Engineer World's Fair, published 2026-07-14.
`stagingTimestamp` for the artifact and all signals: 2026-07-14 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node. Entities marked **[this batch]** are defined in another file of this 5-talk batch.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-osmani-engineer-of-future` | The engineer of the future is the person who is able to choose what is worth doing (Addy Osmani — AI Engineer World's Fair) | youtube | https://youtu.be/n97BCfyFIvw |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-addy-osmani`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-addy-osmani` | Addy Osmani (engineering leader and author; notable individual) | — (no affiliation stated in the talk; publicly associated with Google, but the transcript never claims it — no `AffiliatedWithCompany` edge) |

## Companies (0 new)

- `co-sonar` **[registry]** — referenced twice for its 2026 survey/research data; `RelevantCompany` edges from signals below.

## Patterns (1 new — the single pattern coined across this 5-talk batch)

| slug | name | kind | brief |
|---|---|---|---|
| `pat-value-of-judgement` | Value of Judgement | dynamic | As AI industrializes execution (code, content, analysis), the durable human edge shifts to judgment: choosing what is worth doing, verifying evidence, and owning outcomes. Capability edges (speed, recall, verification, even taste) decay at roughly one model release; the signature — who stands behind the shipped work — decays far slower. Roles and careers re-bundle around answerability and taste rather than titles and keystrokes. |

Evidence altitude check: this is a labor/industry-change thesis, not a mechanism. It is evidenced independently by three talks in this batch — Osmani (this talk, the full thesis: verdict/answerability, alpha & decay, agency ladder), Wu & Shihipar/Willison (`wu-shihipar-anthropic-culture.md`: product taste and business sense now outrank execution as idea→ship falls to ~a week; visible-AI accountability), and Brunet (`brunet-cursor-forward-deployed.md`: enterprises buying judgment about what is worth automating). Cross-link suggestion for central reconciliation: `pat-value-of-judgement` `ReliesOnPattern → pat-verification-gap` (judgment is exercised over the evidence the verification layer produces).

## Elements (2 new, 1 registry reuse)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-cognitive-debt` | Cognitive debt | concept | — | Erosion of a team's understanding and memory of how its own system works as delegation to agents grows; for code, the gap between how much code exists in the repo and how much any human on the team genuinely understands. Related failure modes named in the talk: cognitive surrender (adopting AI's answer before forming your own) and orchestration tax (parallel agent loops multiplying routing/merge/verify decisions while human bandwidth does not parallelize) |
| `el-alpha-decay` | Alpha and decay (career math) | concept | — | Alpha = the gap between what you can do and what current models can do; decay = the clock on that gap. Half-life of a capability edge ≈ one model release (speed and recall already decayed; verification is moving into harnesses; taste decays slower but still resets); half-life of a signature — credibility, expertise, the name behind shipped work — is much longer |

Reused: `el-harness-engineering` **[registry]** — the talk explicitly recounts the harness engineering → loop engineering → software factory progression as the backdrop for the human-role shift.

Element edges: both new elements `IdentifiedInArtifact → ia-aie-osmani-engineer-of-future`; `el-alpha-decay` `ExemplifiesPattern → pat-value-of-judgement`.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-osmani-engineer-of-future`, `SourcedFromSource → source-aie-yt`.

| slug | domain | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-ai-code-normalized-distrust-gap` | harness | Sonar 2026 survey (as cited by Osmani): AI-assisted code is no longer marginal in codebases; ~96% of engineers are skeptical of AI code but only about half always verify before committing — distrust without verification bandwidth | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-sonar` |
| `sig-clean-code-agent-economics` | harness | Sonar research (as cited): clean and messy repos show roughly the same agent pass rates, but clean code uses fewer tokens and causes fewer revisits — code maintainability has become a line item in agent operating cost | `FormsPattern → pat-harness-over-model` | `RelevantCompany → co-sonar` |
| `sig-borrowed-confidence-wharton` | harness | Wharton study (as cited): when the AI was wrong, 73% of people still went with it and felt MORE sure — the failure mode of AI use is borrowed confidence (cognitive surrender), not non-use | `FormsPattern → pat-verification-gap` | — |
| `sig-roles-rebundling` | harness | Boris Cherny (Anthropic) has put language on what teams are feeling: old craft boundaries are blurring and roles are re-bundling around the work itself (prototype/build/sweep/grow/maintain modes); the question shifts from "what is your title" to "what part of the system can you own" | `FormsPattern → pat-value-of-judgement` | — |

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-inner-loop-capability-outer-loop-agency` | Agents can run the inner execution loop (investigate, implement, test, report); the outer loop — decide, verify, approve, own — is still engineering. The boundary is not "human looks at AI output"; it is evidence and responsibility. Inner loop is capability, outer loop is agency | `HighlightsPattern → pat-value-of-judgement` | `ReliesOnElement → el-harness-engineering` **[registry]** |
| `ins-explain-it-or-dont-ship-it` | Operational rule for AI-era shipping: explain it or don't ship it — not because humans type or read every line, but because someone must understand the work well enough to defend it; the owners-file model (named humans on the hook per subsystem) generalizes to agent output | `HighlightsPattern → pat-value-of-judgement` | `ReliesOnElement → el-cognitive-debt` |
| `ins-latent-demand-moves-the-bottleneck` | Every time writing software got cheaper (high-level languages, frameworks, cloud, low-code) demand expanded rather than shrank; agents repeat the pattern — the bottleneck moves from "can we build this" to "should this exist and can we answer for it" | `HighlightsPattern → pat-value-of-judgement` | — |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-osmani-engineer-of-future`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-avoid-agent-cognitive-traps` | Avoid the three cognitive traps of agent-heavy work | Avoid cognitive debt: keep team understanding in step with what agents ship. Avoid cognitive surrender: delegate ("do the work, show me evidence I can judge") but never adopt an answer before forming your own. Avoid orchestration tax: your attention does not parallelize — design it like a system (where you enter, what you require, what you reuse); treat hour/day-scale runs as work streams with control-system review, not glance-at-the-end review | `ReferencesElement → el-cognitive-debt` |
| `how-run-the-decay-test` | Run the decay test on your own edge | Periodically ask which of your edges the frontier has already absorbed (speed and recall: gone; verification: moving into harnesses/evals/static checks; taste: slower but resets as models learn from examples); don't cling to a capability — move your edge up a level toward loop design, evidence design, brownfield stewardship, and ownership | `ReferencesElement → el-alpha-decay` |

## Dropped

- "Taste" discussion (Paul Graham, Mitchell Hashimoto's definition: high-quality qualitative judgments where no objective metric exists yet) — folded into `pat-value-of-judgement` brief and `el-alpha-decay`; Hashimoto and Graham not coined as experts (cited, not contributing).
- The agency ladder (flag → execute → diagnose → propose → resolve → discernment) — prose within the pattern/insights, not its own element.
- "Software factory" and Dex Horthy reference — covered by registry (`exp-dex-horthy`, batch 3); no new node.

## Review notes

1. **This file coins the batch's single new pattern** (`pat-value-of-judgement`). Three-talk independent evidence within this batch (Osmani + Wu/Shihipar + Brunet) plus resonance with batch-3's un-coined "imagination as the new bottleneck" (bouffard). If you judge it too close to `pat-verification-gap`, the fallback is to rehome its 5 edges (2 signals, 4 insights across 3 files) onto `pat-verification-gap` — but note it claims a labor/career shift, not a trust-infrastructure shift; I read them as distinct and complementary.
2. Survey numbers (96%, ~50%, 73%) are read off auto-captions of a spoken summary of Sonar/Wharton studies — treat as paraphrases; verify against the original reports before public-facing use.
3. "Boris Cherney" in captions = Boris Cherny (Anthropic). "re-bumbling" = re-bundling.
4. Osmani's affiliation is never stated in the talk — no `AffiliatedWithCompany` edge on purpose.
5. `el-cognitive-debt` bundles cognitive surrender and orchestration tax as related failure modes rather than three separate concept elements — split if you want finer grain.
