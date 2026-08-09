# SPIKE extraction — "From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization" (May Walter, Hud) — FOR REVIEW

Source transcript: `transcripts/walter-hud-agentic-perf-optimization.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/JJGbw4ggaFs — AI Engineer World's Fair, published 2026-07-19.
`stagingTimestamp` for the artifact and all signals: 2026-07-19 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-walter-agentic-perf` | From Blind Spots to Merged PRs: Continuous Agentic Performance Optimization (May Walter, Hud — AI Engineer World's Fair) | youtube | https://youtu.be/JJGbw4ggaFs |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-may-walter`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-may-walter` | May Walter (co-founder & CTO, Hud) | `AffiliatedWithCompany → co-hud` |

## Companies (1 new, 1 registry)

| slug | name | type | note |
|---|---|---|---|
| `co-hud` | Hud | developer | runtime intelligence layer for coding agents — captures function-level and forensic production context so coding agents can fix what is going on in production; the product name references the "heads-up display" over code |
| `co-github` **[registry]** | GitHub | — | reused: GitHub agent(ic) workflows are the trigger/orchestration substrate for Hud's automation (prose; no new node) |

## Elements (1 new, 2 registry)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-prod-to-code` | Prod-to-code runtime context | concept | harness | Translating production observability into the level coding agents actually reason at: function/file-level context (invocations, callers, timings, outbound calls) connected back to the endpoint/consumer/cron that triggered it, plus forensic evidence captured only for anomalous requests (beyond P99) — instead of service/endpoint-level metrics that "don't speak the agent's language" |
| `el-agent-skills` **[registry]** | Agent skills | — | — | reused: skills over the query language (500-tracing, memory-spike-vs-baseline diffs) cut eval variance and encode senior-engineer playbooks |
| `el-mcp` **[registry]** | Model Context Protocol | — | — | reused: runtime intelligence is served to the coding agent via MCP in the weekly workflow |

Element edges: `el-prod-to-code` `IdentifiedInArtifact → ia-aie-walter-agentic-perf`; `el-prod-to-code` `EnablesPattern → pat-verification-gap` (grounding agent claims in runtime evidence); `el-prod-to-code` `UsesElement → el-mcp`.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-walter-agentic-perf`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-dora-2026-ai-instability` | Google's DORA 2026 metrics: the biggest impact of AI adoption on engineering is individual effectiveness, the second is software delivery *instability*; team throughput is barely moved — individuals feel faster, teams ship the same, software breaks more often | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-google` **[registry]** |
| `sig-hud-automated-perf-sprint` | Hud runs a weekly autonomous agentic workflow (GitHub agent workflows + Claude Code + runtime context via MCP) that investigates production performance, scores high-ROI opportunities, fixes, re-runs and verifies impact, and reports to Slack — automating the "performance sprint" investigation phase that never happened in engineers' day-to-day | `FormsPattern → pat-model-not-bottleneck` | `RelevantCompany → co-hud` |
| `sig-plausible-unverified-fixes` | First failure mode encountered: the "plausible unverified" — agent-suggested fixes that sound right and look real but fail once verified; theoretically-possible root causes rather than what actually happens in production. Fix required grounding on production runtime data plus a verify-by-rerun step | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-hud` |
| `sig-pr-flood-rejected-by-humans` | Auto-opening a "rain of 80 pull requests" failed socially — no one wants to review them; Hud switched to one prioritized, human-readable gist at a time (hot-path frequency x business impact x risk), effectively pitching each fix to the human as worth their attention | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-hud` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-autonomous-agents-need-90-trust` | Agentic engineering (autonomous automation) is categorically different from coding with an agent in your IDE: 80% success is fine when you're in the loop steering, but an automation running without you must cross ~80–90% trust — with issues verified worth-fixing and fixes verified in runtime — or its output is slop humans learn to ignore | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-prod-to-code` |
| `ins-agents-unlock-never-done-work` | The bigger win is not doing existing work faster but automating work that never happened at all: nobody proactively investigated performance because the research phase was an unpriceable black box (an hour or weeks); models are already good enough for this — the leverage is context, scoring and guardrails ("context over cleverness") | `HighlightsPattern → pat-model-not-bottleneck` | `ReliesOnElement → el-prod-to-code` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-walter-agentic-perf`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-agentic-perf-loop` | Automate the performance investigation, gate on ROI | Run scheduled (weekly) + webhook-triggered (SLO breach) investigations on real production context; keep infrastructure vendor-neutral in compute, harness and model; score opportunities by hot-path frequency, business criticality (payments, sign-up) and risk (migrations) — surface highest-ROI, not highest-impact; agent must fix, re-run and verify measured impact before a human sees it; deliver one human-friendly report at a time to build appetite, not a PR flood | `ReferencesElement → el-prod-to-code`, `ReferencesElement → el-agent-skills` |
| `how-skills-over-raw-queries` | Encode the senior-engineer playbook as skills, not raw querying | Letting the agent free-form query runtime data created high eval variance; add skills per investigation type (HTTP 500 → trace error origin; memory spike → what ran on those pods vs baseline; look for artificial delays, N+1 queries, missing indexes, sequential awaits, dead code); methodology matters as much as data access | `ReferencesElement → el-agent-skills`, `ReferencesElement → el-prod-to-code` |

## Dropped

- ClickHouse — the underlying columnar DB and its query-pattern quirks; prose inside `how-skills-over-raw-queries` context, not load-bearing enough for an Element.
- Claude Code / Cursor / Copilot / Slack / Teams — named explicitly as swappable choices ("could have been Cursor or Copilot"); kept as prose, no Element nodes.
- GitHub agent workflows as an Element — orchestration substrate mention; kept as prose + `co-github` reference.
- The Jenny/Dave opening skit — illustration of unpriceable investigation debt; folded into `ins-agents-unlock-never-done-work`.

## Review notes

1. Speaker garble: captions introduce the speaker as "Mike, co-founder and CTO at **Thundra**"; the official listing says **May Walter, Hud** — and the talk itself later explains "the HUD, the heads-up display." Extracted under the official name/company; if "Thundra" was a real earlier name for the product, resolve at reconciliation (Thundra is also an unrelated real observability company — likely caption mis-hear).
2. `sig-dora-2026-ai-instability` is the strongest externally-dated fact in the batch (Google DORA 2026 report); consider promoting the report itself to an InformationArtifact centrally if other talks cite it too.
3. `sig-pr-flood-rejected-by-humans` → `pat-verification-gap` reads the human-review-bandwidth bottleneck as part of the verification gap; an alternate home is `pat-model-not-bottleneck` (value migrated to the delivery/attention layer).
4. "80-90% trust" threshold and "7,000 times a week" flow frequency are caption-paraphrase numbers; treat as approximate.
