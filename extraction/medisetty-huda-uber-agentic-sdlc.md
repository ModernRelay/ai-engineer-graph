# SPIKE extraction — "Agentic SDLC at Uber" (Uday Kiran Medisetty & Adam Huda, Uber) — FOR REVIEW

Source transcript: `transcripts/medisetty-huda-uber-agentic-sdlc.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/17-YSUHo6Lk — AI Engineer World's Fair, published 2026-08-21.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-21 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: Uber's "managed software factory" at scale — a few thousand engineers across 12 sites, **70%+ of PRs now by local or cloud agents**, 2× lines of code per engineer year over year, 250+ automated migrations (9M lines). Six building blocks: a model gateway (PII redaction, AI guard, attribution; 800 projects, 100M requests/day), an MCP gateway with token optimization (Omni MCP → CLI projection → code-mode skill; 40% fleet-wide savings; 1,000+ tools), agent devpods (pre-provisioned balloon pods), a managed skills marketplace (2,500 skills, 20K executions/day), a **context graph** (150 node/edge types, 40M entries), and the Cortana assistant (300 personas, 20K sessions/day). Then a feature end to end: Cortana → Minion → inner-loop validation → self-healing CI → tiered review → maintenance loops. Caption garbles: "Udai"/"Ud" → **Uday**, "basil" → **Bazel**, "dev port"/"devots" → **devpod**, "Cortana" kept, "aensified" → **agentified**, "interloop" → **inner loop**, "Spire" → **SPIRE**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-medisetty-huda-uber-agentic-sdlc` | Agentic SDLC at Uber (Uday Kiran Medisetty & Adam Huda, Uber — AI Engineer World's Fair) | youtube | https://youtu.be/17-YSUHo6Lk |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-uday-kiran-medisetty`, `exp-adam-huda`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-uday-kiran-medisetty` | Uday Kiran Medisetty (Uber) | `AffiliatedWithCompany → co-uber` **[registry]** |
| `exp-adam-huda` | Adam Huda (Uber) | `AffiliatedWithCompany → co-uber` **[registry]** |

## Companies (0 new)

Reused **[registry]**, edge-only: `co-uber` — new facts: a few thousand engineers across 12 global tech sites; 70%+ of PRs by local or cloud agents; 2× LOC per engineer YoY; 250+ automated migrations covering 9M lines; six years of monorepo + Bazel investment as the foundation; runs Minion (cloud coding agent) and Cortana (assistant on Slack/CLI/web). Referenced, not coined: Google/Slack/Jira (SaaS MCPs), Figma (design specs compared to simulator screenshots).

## Elements (6 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-uber-model-gateway` | Uber's model gateway | technology | infra | One OpenAI/Anthropic-compatible endpoint for every internal use case, coding harness and external use case: SPIRE identity/auth, a data anonymizer redacting 20+ PII types (no PII leaves the perimeter by default), an AI guard of five specialized safety/policy models — all under 100 ms — plus caching and token optimization. Every request is attributed to a catalog project, caller, user and team, in real time and in the data lake, enabling spend guardrails across the portfolio; audit logs and session traces feed benchmarking and self-improvement loops. 800+ projects, 100M+ model requests/day, frontier and self-hosted open models |
| `el-mcp-gateway-token-optimization` | MCP gateway and the token tax | technology | harness | Thousands of internal APIs were not agent-accessible; SaaS tools each had their own auth. An automated crawler projects internal APIs into MCPs with one config change; SaaS MCPs (Google, Slack, Jira) are hosted with token exchange — one entry point, one install path. Enough MCPs add up to "a massive token tax," so: direct MCP → **Omni MCP** (one MCP that discovers and invokes any other) → **CLI projection** (responses don't eat context) → an auto-installed **code-mode skill** that writes Python on the fly for the top token-consuming uses. 1,000+ tools; 40%+ fleet-wide savings |
| `el-agent-devpods` | Agent devpods | technology | infra | Uber's cloud dev environments for million-line monorepos, agentified: pre-provisioned Kubernetes **balloon pods** with all repositories snapshotted and the search index built, so an agent starts in seconds; isolated, globally available, any number. Roles blur, so a **mega devpod** holds all repos for autonomous cross-repo agents; non-engineers get any harness in seconds |
| `el-managed-skills-marketplace` | Managed skills marketplace | technology | harness | Engineers built skills everywhere — duplication, painful discovery/configuration, "superpar" quality — so Uber built a lifecycle: core and domain skills in a marketplace (2,500 skills), lint checks and automated reviews for a quality baseline, one command to discover/install, persona-based auto-install so agents pick the right skill without installation, and now traces/comments captured as continuous evals fed back to skill authors. 20,000+ skill executions/day |
| `el-uber-context-graph` | Uber's context graph | technology | context | Execution traces showed agents burning time and tokens finding basic context in the monorepo — where a service lives, its dependencies, owners, patterns — scattered across 20–30 systems each needing its own skill or MCP. One context graph of "how Uber runs": 150 unique node and edge types, 40 million entries, from mobile app builds to backend to the data lake, design docs, Jira, incidents and bugs. Plugged into skills for on-call RCAs, planning, data analysis, security scans; example (cash trips in India → SQL) shows "massive improvement in tokens, turns and latency" with the graph |
| `el-managed-software-factory` | The managed software factory | concept | harness | A feature end to end: idea in Slack → **Cortana** (assistant on Slack/CLI/web with skills, MCPs and the context graph; 300 personas, 20K sessions/day, personalizable per team channel) researches the opportunity, drafts requirements, Figma mock-ups and A/B variants → **Minion** (cloud coding agent on a devpod, interactive or autonomous, cross-repo) builds to a *draft* PR and does not push to CI until validated → **inner-loop validation** shifts left: static analysis, visual validation (simulator screenshot vs Figma spec via a skill), staging integration → outer loop: **self-healing CI**, tiered review (small fast model inner, powerful reasoning model + skill outer), and a table on the PR listing every check and screenshot so a human trusts the autonomous diff → **maintenance skills** (e.g. feature-flag cleanup) enrolled on a managed loop surface (runs Sunday for CI capacity, throttled so Monday isn't flooded); landed/not-landed diffs are label data to improve the skill; monthly, incident reviews become new maintenance skills. Bottlenecks now: CI capacity, experiment slots, and "should we build it" |

Element edges: all six `IdentifiedInArtifact → ia-aie-medisetty-huda-uber-agentic-sdlc`.
`el-uber-model-gateway` `DevelopedByCompany → co-uber` **[registry]**;
`el-uber-context-graph` `DevelopedByCompany → co-uber` **[registry]**;
`el-managed-software-factory` `UsesElement → el-uber-model-gateway`, `el-mcp-gateway-token-optimization`, `el-agent-devpods`, `el-managed-skills-marketplace`, `el-uber-context-graph`, `el-software-factory` **[registry]**;
`el-mcp-gateway-token-optimization` `UsesElement → el-mcp` **[seed]**, `el-code-mode` **[registry]**;
`el-managed-skills-marketplace` `UsesElement → el-agent-skills` **[registry]**, `el-skills-registry-platform` **[registry]**;
`el-uber-context-graph` `UsesElement → el-company-brain` **[registry]**;
`el-uber-model-gateway` `UsesElement → el-model-routing` **[registry]**;
`el-uber-context-graph` `ExemplifiesPattern → pat-context-graphs` **[registry]**;
`el-managed-software-factory` `ExemplifiesPattern → pat-ai-native-org` **[registry]**;
`el-managed-skills-marketplace` `ExemplifiesPattern → pat-agent-supply-chain` **[registry]**;
`el-mcp-gateway-token-optimization` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

Reused elements (no new nodes): `el-software-factory` **[registry]**, `el-mcp` **[seed]**, `el-code-mode` **[registry]**, `el-agent-skills` **[registry]**, `el-skills-registry-platform` **[registry, b22]** (QuantumBlack's blueprint, here in production at 2,500 skills), `el-company-brain` **[registry]**, `el-model-routing` **[registry]**, `el-kubernetes` **[registry]**.

## Signals (6 new)

All: `SpottedInArtifact → ia-aie-medisetty-huda-uber-agentic-sdlc`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-uber` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-seventy-percent-of-uber-prs-by-agents` | | A few thousand engineers across 12 sites: over 70% of PRs now come from local or cloud agents, lines of code per engineer doubled year over year, and 250+ automated migrations rewrote 9M lines — on a foundation of six years of monorepo and Bazel investment. The most quantified AI-native engineering org in the corpus | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-managed-software-factory` |
| `sig-token-tax-fixed-at-the-gateway` | harness | With thousands of internal APIs projected into MCPs and every SaaS tool hosted behind one gateway, "enough MCPs add up to a massive token tax" — so Uber moved from direct MCP to an Omni MCP, to CLI projection so responses don't consume context, to a code-mode skill writing Python for the heaviest uses: 40%+ fleet-wide savings across 1,000+ tools. The model gateway attributes every one of 100M daily requests to a project, user and team for spend guardrails | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-mcp-gateway-token-optimization`, `el-uber-model-gateway`, `el-code-mode` **[registry]** |
| `sig-uber-context-graph-40m-entries` | context | Agents were burning tokens, latency and predictability finding basic context across 20–30 systems, each needing its own skill or MCP. Uber built one context graph of how the company runs — 150 node/edge types, 40M entries spanning mobile builds, backend, data lake, design docs, Jira and incidents — and plugs every skill into it: RCAs, planning, data analysis, security scans, with "massive improvement in tokens, turns and latency" on internal evals. A production-scale instance of the company brain | `FormsPattern → pat-context-graphs` **[registry]** | `OnElement → el-uber-context-graph`, `el-company-brain` **[registry]** |
| `sig-skills-marketplace-2500-with-continuous-evals` | harness | Duplication, hard discovery and poor quality in engineer-built skills led to a managed marketplace: 2,500 skills through lint and automated review, one-command install, persona-based auto-install so agents pick skills without installation, and traces/comments captured as continuous evals fed back to authors — 20,000+ executions a day. QuantumBlack's registry blueprint (b22) exists in production at Uber | `FormsPattern → pat-agent-supply-chain` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-managed-skills-marketplace`, `el-skills-registry-platform` **[registry]** |
| `sig-validation-shifts-into-the-inner-loop` | harness | Autonomous diffs stop at a draft PR and don't touch CI until validated: static analysis, visual validation (simulator screenshot vs the Figma spec), staging integration — then self-healing CI, a two-tier review (small model inside the loop, reasoning model plus skill outside), and a table on the PR listing every check and screenshot so a human trusts the diff. Verification moved earlier and got cheaper to protect CI capacity and reviewer attention | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-managed-software-factory` |
| `sig-bottleneck-moves-to-ci-experiments-and-should-we` | | With generation industrialized, Uber names the next constraints: CI capacity ("anticipate where our CI capacity needs to be"), the number of experiments that can feasibly run, and decision-making — "it's not can we build it; we know we can. It's should we build it." Maintenance loops are throttled to Sunday CI capacity and Monday reviewer attention for the same reason | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-value-of-judgement` **[registry]** | `OnElement → el-managed-software-factory` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-the-factory-is-gateways-plus-a-graph` | The durable architecture claim: a managed software factory at thousands-of-engineers scale is six shared blocks — model gateway (identity, PII, guard, attribution), MCP gateway with token optimization, agent environments, a governed skills marketplace, one context graph, and an assistant surface — and the factory is what you get when every SDLC step is a skill plugged into them. The token tax and the context-finding tax are the two costs the blocks exist to pay down | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-uber-context-graph`, `el-mcp-gateway-token-optimization`, `el-uber-model-gateway`, `el-managed-software-factory` |
| `ins-generation-solved-capacity-and-judgement-remain` | At 70% agent-written PRs the remaining bottlenecks are physical and human: CI capacity, experiment slots, reviewer attention (hence inner-loop validation, tiered review, throttled maintenance loops) and the decision of what to build. Uber's factory is the corpus's verification-gap and judgement theses observed as operating constraints rather than predictions | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-managed-software-factory`, `el-managed-skills-marketplace` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-medisetty-huda-uber-agentic-sdlc`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-a-managed-software-factory` | Six building blocks, then plug the SDLC into them | Route every model call through one **gateway** with identity, PII redaction, a safety guard under a latency bound, and per-project/user/team attribution for spend guardrails and traces; put an **MCP gateway** in front of internal APIs (auto-projected) and SaaS tools (hosted, token exchange), then fight the token tax — one omni-MCP, CLI projection, code-mode scripts for heavy uses; pre-provision **agent environments** with repos snapshotted and indexes built so agents start in seconds, cross-repo; run skills through a **managed marketplace** with lint, automated review, one-command install, persona auto-install and continuous evals back to authors; build **one context graph** of how the company runs and plug every skill into it; expose it all through one assistant on every surface; keep autonomous diffs at draft-PR until inner-loop validation (static, visual vs design spec, staging) passes, add self-healing CI and tiered review, and attach the check table to the PR; enroll services in **managed maintenance loops** throttled to CI capacity and reviewer attention, use landed/not-landed as label data, and turn incident reviews into new skills monthly; and plan for the real bottlenecks — CI, experiments, and deciding what to build | `ReferencesElement → el-uber-model-gateway`, `el-mcp-gateway-token-optimization`, `el-agent-devpods`, `el-managed-skills-marketplace`, `el-uber-context-graph`, `el-managed-software-factory` |

## Dropped

- **The World Cup pickup-location feature narrative** — the worked example; its mechanics are in `el-managed-software-factory`.
- **Pointer to the following Uber talk (uReview)** — that talk is queued for this batch.

## Review notes

1. **⚑ Strongest `pat-context-graphs` support in the corpus** (40M-entry production graph with measured token/turn/latency gains) — arriving one batch after Box's counter (b22). Both should sit in the pattern brief.
2. **`pat-ai-native-org`** gets its most quantified data point (70% agent PRs, 2× LOC/engineer, 9M migrated lines); `pat-agent-supply-chain` its second governance-side instance (2,500-skill marketplace with continuous evals).
3. **"Agent spend governance" ledger (b22):** gateway attribution + 40% token savings are the platform-side entries.
4. **⚠ Verify before seeding:** every figure above is from a garbled caption track (70%, 2×, 250/9M, 800/100M, 1,000+/40%, 2,500/20K, 150/40M, 300/20K).
