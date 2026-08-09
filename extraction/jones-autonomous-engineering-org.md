# SPIKE extraction — "Building an Autonomous Engineering Org" (Angie Jones, Agentic AI Foundation) — FOR REVIEW

Source transcript: `transcripts/jones-autonomous-engineering-org.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/whue9_YquGA — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact and all signals: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Speaker cross-file note: Angie Jones has a second talk in this batch (`jones-build-systems-not-code.md`). `exp-angie-jones` and her companies are defined HERE and only referenced there.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-jones-autonomous-org` | Building an Autonomous Engineering Org (Angie Jones, Agentic AI Foundation — AI Engineer World's Fair) | youtube | https://youtu.be/whue9_YquGA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-angie-jones`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-angie-jones` | Angie Jones (led Block's company-wide AI enablement — 12,000 employees — and built its agentic engineering org; conference listing: Agentic AI Foundation) | `AffiliatedWithCompany → co-agentic-ai-foundation`, `AffiliatedWithCompany → co-block` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-agentic-ai-foundation` | Agentic AI Foundation | developer | Foundation stewarding open agentic-AI tooling; Jones's affiliation per the official talk listing. Enum has no nonprofit/foundation type — `developer` chosen, flag if preferred otherwise |
| `co-block` | Block | bigtech | Fintech (Square, Cash App, Afterpay, Tidal); the 3,500-engineer org transformed in this talk; builder of Goose. Enum has no fintech/enterprise — `bigtech` chosen |

## Elements (4 new)

All new elements `IdentifiedInArtifact → ia-aie-jones-autonomous-org`.

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-goose` | Goose | product | harness | Block's coding agent, built before LLMs supported tool calling; Block design-partnered with Anthropic on MCP's initial release and Goose became the MCP client reference implementation; callable in Slack (`@goose`) for diagnose-and-fix flows |
| `el-builder-bot` | Builder Bot | product | harness | Block's internal orchestrator, built by engineers/AI champions to coordinate fleets of parallel agents; consumes the company world model to plan work spanning multiple codebases; any employee can invoke it from Slack to fix bugs or ship features — no GitHub account needed |
| `el-agent-maturity-model` | Agent-relationship maturity model | concept | harness | Six-stage model of an engineer's relationship with agents: 0 no AI → 1 autocomplete → 2 chatting, no PRs → 3 delegating + reviewing → 4 multiple agents in parallel → 5 delegating complete tasks with shippable results, no hand-holding. Jones reorganized her earlier model after Steve Yegge's "Gas Town" article |
| `el-company-world-model` | Company world model | concept | context | Machine-readable map of Block's entire 25,000-repo codebase — every service and what depends on what — that orchestrators and delegated agents pull context from as needed; enables agents to explore different parts of the system in parallel and reassemble cross-codebase plans |

Element edges: `el-goose` `DevelopedByCompany → co-block`, `UsesElement → el-mcp` **[registry]**; `el-builder-bot` `DevelopedByCompany → co-block`, `UsesElement → el-company-world-model`; `el-company-world-model` `EnablesPattern → pat-context-graphs` **[registry]**.

Registry elements referenced (edges only, no new nodes): `el-mcp`, `el-claude-code`, `el-codex`, `el-agents-md`, `el-agent-skills`.

## Signals (6 new)

All: `SpottedInArtifact → ia-aie-jones-autonomous-org`, `SourcedFromSource → source-aie-yt` **[registry]**, domain `harness` unless noted.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-block-90pct-adoption-no-impact` | ~90% of Block's 3,500 engineers used Goose/Claude Code regularly, yet the CEO saw no faster shipping — IDE-level adoption (questions, boilerplate) didn't move delivery; impact required integrating agents into how software is built and shipped | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-block`; `OnElement → el-goose`, `el-claude-code` **[registry]** |
| `sig-goose-mcp-reference-client` | Block built Goose before LLMs supported tool calling, design-partnered with Anthropic on the initial MCP release, and Goose became the MCP client reference implementation — enterprise co-development at the very start of the agent-protocol era | — (pattern-less; historical ecosystem fact) | `OnElement → el-goose`, `el-mcp` **[registry]**; `RelevantCompany → co-block`, `co-anthropic` **[registry]** |
| `sig-block-champions-metrics` | Three months after the 50-engineer AI-champions program made critical repos AI-ready (context/rules files, workflows, reviewers): AI-authored code +69%, reported time savings +37%, automated PRs ×21; sprint teams ran out of tickets and pulled more in twice | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-block`; `OnElement → el-agents-md` **[registry]** |
| `sig-block-review-bottleneck` | Multi-agent parallelism tripled/quadrupled PR volume and code review became the binding constraint; Block enabled Codex review on all repos plus an auto-fix loop (a second agent commits fixes for reviewer-flagged issues before humans look) — explicitly "not a totally solved problem" | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-codex` **[registry]**; `RelevantCompany → co-block` |
| `sig-block-world-model-autonomy` (domain: context) | Block built a machine-readable world model over its 25,000 repos; Builder Bot and its delegated agents pull context from it, explore in parallel, and produce plans spanning multiple codebases — reaching stage 5, where anyone at the company gets bugs fixed or features built from Slack | `FormsPattern → pat-context-graphs` **[registry]** | `OnElement → el-company-world-model`, `el-builder-bot`; `RelevantCompany → co-block` |
| `sig-block-autonomy-then-layoffs` | The transformation arc ends in layoffs immediately after reaching stage-5 autonomy; the speaker asks openly whether enabling employees "to do the most incredible work of their careers" ultimately contributed to their dismissal — "what are we doing? where are we heading?" | — (pattern-less; see review notes) | `RelevantCompany → co-block` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-adoption-is-not-impact` | AI enablement has three phases — experimentation, adoption, impact — and near-total adoption can coexist with zero delivery improvement; the jump to impact comes from integrating agents into build-and-ship workflows (delegation, decomposition, verification), not from more usage or newer models | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-agent-maturity-model` |
| `ins-one-percent-lifts-org` | Per the 1/9/90 rule, transformation fails if it depends on every engineer leveling up; invest a handpicked 1% (champions) in the shared substrate — the repos — so agents work well for everyone, then delegation surfaces where work already arrives make agent use native for the other 99% | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-agents-md` **[registry]** |

## KnowHow (4 new)

All `SourcedFromArtifact → ia-aie-jones-autonomous-org`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-repo-ai-readiness` | Make repos AI-ready before demanding delegation | Add context files (agents.md / claude.md); rules files as guardrails; repeatable workflows (slash commands, later agent skills); an AI code reviewer with instructions on what matters; AI attribution on PRs. For monorepos, set shared context/rules at the root and layer service-level overlays (inheritance). Don't force one-size-fits-all — web ≠ mobile; let similar-shaped teams converge on tools | `ReferencesElement → el-agents-md` **[registry]**, `el-agent-skills` **[registry]** |
| `how-ai-champions-program` | Scale transformation through a handpicked 1% | Handpick ~50 engineers covering the most critical repos (not a call for volunteers); require ~30% dedicated time; select for tolerance of non-determinism ("it often did not work out of the box"); span every corner — front end, back end, mobile, data, infra, nasty legacy monorepos to small services — to pressure-test what actually scales | `ReferencesElement → el-agent-maturity-model` |
| `how-native-delegation-surfaces` | Wire delegation into where work already arrives | Implement agent delegation from all three intake surfaces: issue trackers (Jira/Linear), GitHub issues, and Slack; let tickets be assigned to agents like sprint members; keep the flow native so engineers outside the champions program need no new skill | `ReferencesElement → el-goose` |
| `how-stage4-scaling` | Solve the two stage-4 walls: review and compute | Enable an AI reviewer on every repo and pair it with an auto-fix loop so a second agent commits fixes before humans review; move agents off laptops (memory/CPU choke) into dedicated cloud workspaces — one isolated environment per agent — so parallel fleets run from anywhere | `ReferencesElement → el-codex` **[registry]** |

## Dropped

- Square, Cash App, Afterpay, Tidal as Company nodes — Block subsidiaries; prose only.
- "AI or die" top-down pressure and AI fatigue — kept as context inside signals.
- Steve Yegge / "Gas Town" article — attribution kept in `el-agent-maturity-model` brief; `exp-steve-yegge` **[registry]** exists but no edge type fits a citation (he didn't contribute to this artifact).
- Cloud workspaces as an Element — captured in `how-stage4-scaling`; no reusable named product given.

## Review notes

1. **`pat-ai-native-org` candidate (NOT coined, per instruction):** this talk is arguably the strongest single narrative data point yet — a 3,500-person org restructured around agent delegation, non-engineers shipping via Builder Bot without GitHub, quantitative gains (+69% AI-authored code, ×21 automated PRs), PLUS the labor-market dark side (layoffs at stage 5). Signals 1, 3, 5, 6 all bear on it; `sig-block-autonomy-then-layoffs` deliberately left pattern-less rather than force-fit, ready to rehome if the pattern is coined. The layoffs signal also softly resonates with `pat-value-of-judgement` (execution industrialized, headcount followed) — noted, not edged.
2. **`exp-angie-jones` affiliation:** official listing says Agentic AI Foundation; all the described work happened at Block (the closing layoff twist suggests the transition). Both `AffiliatedWithCompany` edges kept — trim at review if one-affiliation convention is preferred.
3. Company enum stretches: `co-block` → bigtech, `co-agentic-ai-foundation` → developer; neither fits cleanly.
4. `el-company-world-model` vs `el-company-brain` [registry, batch 3] and `el-brain-os` [registry, batch 6]: possible merge targets. Kept separate because this one is specifically a machine-readable service/dependency map over the codebase for orchestrators, not an org-knowledge brain.
5. Builder Bot's orchestration resembles `el-agent-org-hierarchy` [registry, batch 6] (KRAFTON fleet); different org, similar shape — noted for the ledger, no edge.
6. Garbles: "1990 rule" = 1/9/90 rule; "act Build-A-Bot in Slack" ≈ "ask Builder Bot in Slack" (product name rendered both "Builder Bot" and "Build-A-Bot" in captions — "Builder Bot" chosen); "contacts and rules files" = context and rules files. Layoff timing/scale never stated — kept vague as in the talk.
7. Timeline: the narrated events are 2025 (champions program ~June 2025; metrics ~3 months later); publish date 2026-06-28 used as stagingTimestamp per convention.
