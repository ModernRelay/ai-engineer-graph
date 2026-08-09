# SPIKE extraction — "ReviewDebt: A Practical Framework for Scoring Every Pull Request" (Sachin Gupta) — FOR REVIEW

Source transcript: `transcripts/gupta-reviewdebt.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/TJPInBjhE4Q — AI Engineer World's Fair, published 2026-07-12.
`stagingTimestamp` for the artifact and all signals: 2026-07-12 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-gupta-reviewdebt` | ReviewDebt: A Practical Framework for Scoring Every Pull Request (Sachin Gupta — AI Engineer World's Fair) | youtube | https://youtu.be/TJPInBjhE4Q |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-sachin-gupta` **[registry]**.

## Experts (0 new)

**[registry]** reused: `exp-sachin-gupta` — same speaker as batch 3's "Agents Need Feature Flags" (`ia-aie-gupta-feature-flags`); NOT re-coined. Consistent with batch 3, he again states no company affiliation ("I'm a software engineer") — still no `AffiliatedWithCompany` edge.

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-faros-ai` | Faros AI | developer | engineering-intelligence platform; source of the 2026 AI-adoption-cohort benchmark and the April 2026 "acceleration whiplash" benchmark (22,000 developers, 4,000 teams) that this talk's headline numbers come from |

**[registry]** reused: `co-github` (October 2025 Octoverse-scale report cited).

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-reviewdebt` | ReviewDebt scoring framework | framework | harness | Deterministic (no-LLM-judge) PR scorer: 5 signal families / 10 checks — diff size & coupling, test-evidence gap (test lines ÷ production lines), directory & code-owner spread, AI-authorship indicators (co-authored footer, branch prefixes, body phrases; amplifier-only, "information only, not a penalty"), evidence & rationale gaps (does the PR body say *why*) — combined into a 0–100 score, four bands (low / normal / needs-evidence / high), plus structured reviewer-focus and author-next-action lists and estimated review minutes |

Element edges: `IdentifiedInArtifact → ia-aie-gupta-reviewdebt`; `ExemplifiesPattern → pat-verification-gap` **[registry]**.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-gupta-reviewdebt`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-github-commits-up-reviews-down` | GitHub's October 2025 report (covering nearly every public PR): commits +25% YoY while PR comments — the proxy for review activity — fell 27% in the same year; production volume and review attention moving in opposite directions | `FormsPattern → pat-verification-gap` **[registry]** | `RelevantCompany → co-github` |
| `sig-faros-review-time-blowup` | Faros AI 2026 benchmarks (AI-adoption cohort; April 2026 study = 22k developers, 4k teams): median PR review time up 441.5%, reviewed PRs take 5.4× longer than before, 31% more PRs merged with **no review at all**; DX 2026 study (400 orgs, 16 months): median PR size 44→72 lines (+63%) while PR throughput grew only ~8% against ~65% AI-usage growth — real gains, smaller than the hype | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-faros-ai` |
| `sig-review-debt-compounds` | Review debt is generative: (1) the agent learns from your codebase — code not deeply reviewed yesterday grounds tomorrow's PRs via fine-tuning/RAG/in-context; (2) reviewer attention contracts to syntax when most of a PR is generated — architectural calls move "from review time to never"; (3) leadership resets velocity expectations to the new throughput, leaving no slack to repay | `FormsPattern → pat-verification-gap` | — |
| `sig-524-pr-scan-volume-not-authorship` | 90-day scan of 524 PRs across 3 public repos: AI-authorship indicators steady at 5–20%/week, yet burden tracked *volume* — one repo accrued 186 senior-reviewer hours in 27 days (another 43 in the same window length); only 4 of 524 PRs hit needs-evidence/high bands and all 4 were structural (large migrations, SDK rewrites, multi-team refactors); one PR alone scored 5,036 estimated minutes (~84h) of review effort — complexity drives burden, AI-driven volume creates the conditions | `FormsPattern → pat-verification-gap` | — |

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-velocity-metrics-are-vanity` | Every celebrated AI-coding number — PR count, PR size, cycle time — is real and none is a lie, but all are vanity: PR count rises when one change splits into seven, size growth is bloat, cycle time falls when reviewers stop pushing back; they measure speed of production, not speed of trust | `HighlightsPattern → pat-verification-gap` | — |
| `ins-deterministic-scores-are-defensible` | A review-burden score must be deterministically computable from the PR + repo, never an LLM judge: judge-based scores are moving targets (same PR re-scores when the model changes) and indefensible in an engineering or leadership review — a number only changes behavior if it is traceable | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-reviewdebt` |
| `ins-2027-governance-shift` | 2026 is the adoption year; 2027 the conversation shifts to governance — can you trust shipped code, who is accountable when an AI-authored change causes an incident, where is the audit trail; a review-debt number is the bridge that lets teams have the governance conversation without abandoning the throughput gains | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-reviewdebt` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-gupta-reviewdebt`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-adopt-review-debt-scoring` | Adopt review-debt scoring bottom-up | Backfill: score your last 200 merged PRs and calibrate weights against reviewers' gut feel; threshold: PRs ≥ ~50 require an author evidence comment; surface: post the score as a non-blocking PR comment on every PR; aggregate: weekly per-team slope is the leading indicator EMs watch (slope matters more than level); talk: bring the number to retros/roadmap — "X% throughput added, Y points review debt over Z weeks ≈ N senior-engineer hours" moves the discussion from feeling to measurement; healthy PRs should produce near-zero noise | `ReferencesElement → el-reviewdebt` |
| `how-agent-era-pr-hygiene` | Shape agent-authored PRs for reviewability | One logical change per PR (not "small" in the abstract); tests ship with the change and the *human* author confirms they assert what the code *should* do, not lock in what it does (bugs included); stay in one code-owner territory — split cross-cutting work per team; the author, never the agent, writes the why in the PR body; same review standard for AI PRs as human PRs; anti-patterns: approve-with-comment merges, "we'll catch it in QA", "PRs are smaller now", LGTM stamps | `ReferencesElement → el-reviewdebt` |

## Dropped

- DX (the "DX 2026 study", 400 orgs) as a Company — cited once as a data source; kept in signal prose. Coin `co-dx` centrally if it recurs.
- The five signal families as separate Elements — they are internals of `el-reviewdebt`; folded into its brief.
- Reviewer fatigue / late-night 11pm merges / test theater / architectural drift / incident lag list — qualitative cost taxonomy, folded into insight-adjacent prose rather than dated signals.
- The A/B/C anonymized repo case (co-authored footer strongest signal; repo C at 0% because trailers were stripped) — folded into `el-reviewdebt` brief + `sig-524-pr-scan-volume-not-authorship`.
- LLM-as-judge critique as an Element — captured as `ins-deterministic-scores-are-defensible`; relates to batch-1 `el-generator-validator-separation` but no edge type fits Insight→Element beyond ReliesOn (kept on el-reviewdebt).

## Review notes

1. **Speaker reuse confirmed:** `exp-sachin-gupta` [registry, batch 3] — not re-coined; second AIE talk by the same expert, still no stated affiliation.
2. "Review debt" as a Pattern? Considered and **rejected**: it is a named mechanism/metric inside the existing seed-altitude thesis `pat-verification-gap` (generation industrialized, verification didn't). All four signals land there; the framework itself is `el-reviewdebt` with `ExemplifiesPattern`.
3. Numbers are read off auto-captions and slide narration: "441.5%", "5.4×", "31%", "44→72 lines", "8% vs 65%", "524 PRs", "186/43 hours", "5,036 minutes / score 73". The bands were narrated inconsistently ("52 74" ≈ 50–74). Verify against the video/slides before quoting publicly.
4. One caption stretch: the GitHub stat is described as "2025 October's report covering almost every public pull request" — presumably Octoverse 2025; not asserted as Octoverse in the node text.
5. `co-faros-ai` coined on two distinct cited benchmarks from the same vendor; DX left uncoined (one citation) — flip both or neither if you want symmetric treatment.
