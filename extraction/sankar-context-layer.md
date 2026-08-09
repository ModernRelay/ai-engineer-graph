# SPIKE extraction — "WTF Is the Context Layer? The Missing Infrastructure for Production Agents" (Prukalpa Sankar, Atlan) — FOR REVIEW

Source transcript: `transcripts/sankar-context-layer.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/8G_1-3IO4ZQ — AI Engineer World's Fair, published 2026-07-14.
`stagingTimestamp` for the artifact and all signals: 2026-07-14 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-sankar-context-layer` | WTF Is the Context Layer? The Missing Infrastructure for Production Agents (Prukalpa Sankar, Atlan — AI Engineer World's Fair) | youtube | https://youtu.be/8G_1-3IO4ZQ |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-prukalpa-sankar`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-prukalpa-sankar` | Prukalpa Sankar (co-founder, Atlan; captions render the name as "Prakalpa"/"Prokalpa") | `AffiliatedWithCompany → co-atlan` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-atlan` | Atlan | developer | Data-catalog / metadata company ("AI doesn't know your business, we fix that"); customers named in talk: GitLab, Zoom, Discord, Affirm, MasterCard, General Motors. Now positioning around the "context layer" / company brains |

## Elements (1 new, 2 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-context-layer` | Context layer | concept | context | A system that turns a company's knowledge, expertise, and norms into machine-usable context for AI: continuously mines context from business systems, feeds one shared company brain, manages skills/context through development lifecycles (versioning, dependency management, quality ownership, security posture), exposes multiple retrieval paths (MCP, SQL, vector, hybrid), and closes a compounding learning loop from agent traces |
| **[registry]** `el-company-brain` | — | — | — | reused; Sankar's "one company brain" that all domain skills feed into (near-synonym of her context layer — see review notes) |
| **[registry]** `el-agent-skills` | — | — | — | reused; Atlan's 300 marketing skills are skills in this sense |

Element edges: `el-context-layer` `IdentifiedInArtifact → ia-aie-sankar-context-layer`; `el-context-layer` `EnablesPattern → pat-context-graphs`; `el-context-layer` `UsesElement → el-company-brain`.

## Signals (4 new)

All: domain `context`, `SpottedInArtifact → ia-aie-sankar-context-layer`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany | OnElement |
|---|---|---|---|---|
| `sig-intelligence-context-divergence` | Model intelligence 1,000x'd in a decade (2x in the last 6 months alone: two years ago models couldn't pass the bar, now top-1% scorers) while situated business context "barely moved" — and usefulness shows it: 1 in 5 AI use cases reaches production, 56% of CEOs report zero financial benefit from AI (figures as cited by speaker) | `pat-model-not-bottleneck`, `pat-context-graphs` | — | `el-context-layer` |
| `sig-atlan-bootstrapped-agent-limits` | Atlan's era-1 (per-job bootstrapped agents, started ~18 months ago): building an agent took ~5 minutes but context engineering "took forever"; agents lived on islands with separate memory systems — marketing changed positioning and the SDR agent on the website kept pitching the old version; failures untraceable (model? agent? context?) | `pat-context-graphs` | `co-atlan` | — |
| `sig-atlan-agent-stack-churn` | In 12 months Atlan cycled its agent layer: Relevance (no-code) → Google ADK → Glean → Claude Code → now 50/50 Claude Code and Codex — and at every migration accumulated context got trapped in the abandoned tool; context portability across agent harnesses is a live, unsolved cost | `pat-context-graphs` | `co-atlan` | — |
| `sig-atlan-skill-sprawl` | Atlan's marketing team built ~300 skills and 40 agents in 6 months around a shared context layer and hit code-scale problems: skill dependency chains (competitive intel → positioning → battle cards) break downstream when upstream skills self-improve; skills drift stale; no owner of skill quality; secrets hardcoded in .env files; people downloading public skill repos — "a nightmare" of security and governance | `pat-context-graphs`, `pat-agent-supply-chain` | `co-atlan` | `el-agent-skills` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-context-managed-like-code` | Company context needs what code got: lifecycle management, versioning, dependency graphs ("this skill impacts these others"), named approvers/maintainers/contributors, quality gates, and security posture — the open question is "what does the GitHub for context look like?"; hardcoding context into individual agents does not scale and gets dangerous as autonomous systems multiply (the sales-vs-finance two-revenue-numbers joke, now executed by agents) | `pat-context-graphs` | `el-context-layer` |
| `ins-context-is-ip` | In a world where you and your competitor buy the same models and the same intelligence, encoded context — how you do business, your norms and culture — is the differentiator; context is not just king but IP, the thing that distinguishes an American Express support agent from an Amazon one | `pat-context-graphs`, `pat-model-not-bottleneck` | `el-context-layer` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-sankar-context-layer`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-mine-context-from-business-systems` | Bootstrap the company brain by reverse-constructing business systems | Don't start by hand-writing context: context is hidden in existing business systems and quality compounds across connections; connect Salesforce/HubSpot/warehouse/application layer, reverse-construct how they relate (context is lost at every hop otherwise), then deploy AI on top — Atlan reports "incredible accuracy" for a first-version company brain built this way | `el-context-layer`, `el-company-brain` |
| `how-trace-maintainer-loop` | Harvest agent traces into a human-approved learning loop | Every AI interaction creates more context — harness it: deploy a specialized harness that reads all agent traces, reverse-constructs candidate context/skill improvements, and routes them to a human maintainer as approve/reject decisions; this is the compounding learning loop that keeps skills from drifting | `el-context-layer` |

## Dropped

- Named agent-layer tools (Relevance, Google ADK, Glean, Claude Code, Codex, Qualified, Artisan, "Co-work"/claw) — kept as prose inside `sig-atlan-agent-stack-churn`; none is load-bearing enough here to coin.
- The Maya / "Mac Context Burgers" analyst narrative (knowledge/expertise/norms taxonomy) — folded into the `el-context-layer` brief.
- Bill Gates "content is king" framing and the "context is king" slogan — rhetorical device.
- MCP/SQL/vector/hybrid retrieval list — prose inside the element brief; `el-mcp` edge not warranted (passing mention).

## Review notes

1. `el-context-layer` vs registry `el-company-brain` (batch 3): Sankar uses "company brain" for the store and "context layer" for the full system (mining + lifecycle + retrieval + learning loop). I kept both with `UsesElement`, but a reviewer may prefer merging them into one node — flag for central decision.
2. This talk is the clearest single-vendor articulation of the `pat-context-graphs` thesis in the batch (she name-checks "context graphs, anyone?" directly); all four signals link it. If that feels over-weighted, `sig-intelligence-context-divergence` stands fine on `pat-model-not-bottleneck` alone.
3. Statistics (1-in-5 production rate, 56% of CEOs, 10% of job performance variance from IQ, 1,000x intelligence) are speaker-cited without sources — kept attributed as claims, not facts.
4. `pat-agent-supply-chain` on `sig-atlan-skill-sprawl` is an interpretive stretch worth checking: her governance complaints (public skill repos, hardcoded secrets) are exactly that pattern's territory, but she frames them as internal ops pain, not supply-chain attack surface.
5. Twitter handle garbled ("Prokalpa") — actual handle is @prukalpa; name spelled per official talk listing.
