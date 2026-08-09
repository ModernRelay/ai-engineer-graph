# SPIKE extraction — "Skills are the New SDKs" (Elvin Aghammadzada, DataRobot) — FOR REVIEW

Source transcript: `transcripts/aghammadzada-datarobot-skills-new-sdks.txt` (auto-captions — quotes are paraphrases; "open cloud"/"Open Agent" in captions read as OpenClaw, "Winix" as a mistranscribed repo name).
Video: https://youtu.be/LC3-P7v3yoI — AI Engineer World's Fair, published 2026-07-20.
`stagingTimestamp` for the artifact and all signals: 2026-07-20 (publish date).
Entities marked **[existing]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-aghammadzada-skills-sdks` | Skills are the New SDKs (Elvin Aghammadzada, DataRobot — AI Engineer World's Fair) | youtube | https://youtu.be/LC3-P7v3yoI |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-elvin-aghammadzada`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-elvin-aghammadzada` | Elvin Aghammadzada (DataRobot; builds customer enterprise agents, maintains DataRobot's open-source agent-skills repository) | `AffiliatedWithCompany → co-datarobot` |

## Companies (1 new; 1 existing reused)

| slug | name | type | note |
|---|---|---|---|
| `co-datarobot` | DataRobot | developer | enterprise AI platform; ships customer agents as one general-purpose engine + domain skills |
| **[existing]** `co-anthropic` | — | — | origin of both skills and MCP ("both are from Anthropic — they're not competing") |

## Elements (2 new; 3 existing reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-context-rot` | Context rot | concept | context | Empirical finding that LLM performance degrades long before the advertised context limit — measurably after ~25% of the window is used (e.g. 256K of 1M), with practitioners' "dumb zone" starting around 40%; falsifies the infinite-context-window framing behind dump-everything RAG/MCP designs |
| `el-progressive-disclosure` | Progressive disclosure | concept | context | Three-level loading of packaged capability: front matter (<~100 tokens, always in context, acts like a DB index) → markdown body (loaded on activation, <~5K tokens) → scripts/resources (executed or read on demand, only outputs return to context). The mechanism that makes skills ~10× cheaper in context than equivalent MCP tool definitions; also usable *in front of* an MCP server |
| **[existing]** `el-agent-skills` | Agent skills | — | — | the talk's core subject; reused for all edges |
| **[existing]** `el-mcp` | Model Context Protocol | — | — | contrast case: auth, isolation, remote horsepower |
| **[existing]** `el-openclaw` | OpenClaw | — | — | cited as most-starred GitHub repo; sub-agents for context hygiene; self-healing/self-writing skills |

Element edges: `el-progressive-disclosure` `EnablesElement → el-agent-skills`; `el-context-rot` `EnablesPattern → pat-context-graphs` (the constraint that motivates the pattern — review call below); both new elements `IdentifiedInArtifact → ia-aie-aghammadzada-skills-sdks`.

## Signals (5 new)

All: domain `context`, `SpottedInArtifact → ia-aie-aghammadzada-skills-sdks`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-context-rot-25pct` | "Context Rot" paper: performance starts degrading after ~25% of the context window is used; practitioner heuristic puts the "dumb zone" past ~40% — an agent loaded with instructions + many MCPs can start its first user turn already dumb | `FormsPattern → pat-context-graphs` | — |
| `sig-docs-traffic-50pct-agents` | Traffic to documentation websites coming from coding agents jumped from ~10% to ~50% in one year — docs' primary reader is becoming the agent, but docs are still written for humans (intuition, follow-ups, "just Google it") | `FormsPattern → pat-context-graphs`, `FormsPattern → pat-saaspocalypse` | — |
| `sig-mcp-token-overhead-100k` | An agent connected to 15 MCP servers burns >100K tokens per session on tool definitions alone, before the conversation starts; skills' progressive disclosure makes the same surface ~10× smaller; Codex/Claude Code themselves run on only a handful of tools | `FormsPattern → pat-context-graphs` | — |
| `sig-skills-ecosystem-scale` | Skills ecosystem snapshot (mid-2026): 26+ platforms support skills (Claude Code, Codex, Copilot, Gemini CLI…), ~100Ks of published skills, paid skill marketplaces, a skills registry; OpenClaw became the most-starred GitHub repository — while marketplaces still lack verification controls ("like npm 10 years ago") | `FormsPattern → pat-agent-supply-chain`, `FormsPattern → pat-saaspocalypse` | `RelevantCompany → co-anthropic` |
| `sig-llm-written-skills-hurt` | Recently published research: LLM-generated skills *hurt* performance — more tokens and more reasoning time than no skill — versus human-authored ones; "a skill is only as good as the human who wrote it" | `FormsPattern → pat-context-graphs`, `FormsPattern → pat-verification-gap` | — |

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-fluency-moat` | Agents dissolve SaaS-era friction moats (integrations, switching costs — gone when an agent rewrites 100K–1M lines Python→Rust in days); the replacement moat is *fluency*: how fast an arriving agent picks up your platform's operational knowledge. "Teachability" joins security/compliance/SLA on the enterprise evaluation checklist, and skills are the commoditization vehicle for that experience layer | `HighlightsPattern → pat-saaspocalypse` | `ReliesOnElement → el-agent-skills` |
| `ins-one-agent-many-skills` | The unit of enterprise delivery is inverting: not a bespoke agent per domain, but one good general-purpose coding agent (~10 tools) as the engine, with domain skills layered on top — switching industries becomes writing skills, not building agents | `HighlightsPattern → pat-saaspocalypse`, `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-agent-skills`, `ReliesOnElement → el-openclaw` |
| `ins-skills-mcp-complementary` | Skills and MCP solve different halves: skills carry how-to-think (reasoning, self-modification, can even template/expose/spawn MCP servers); MCP carries auth, process isolation, and remote horsepower (GPUs, 400TB corpora) — with skills doing progressive disclosure in front of heavyweight MCP servers | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-agent-skills`, `ReliesOnElement → el-mcp`, `ReliesOnElement → el-progressive-disclosure` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-aghammadzada-skills-sdks`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-context-as-budget` | Treat context as a budget with a 40% ceiling | Longer context ≠ better — every irrelevant file/web result/error drags attention; keep pre-conversation load (system prompt + tools + MCPs) under ~40% of the window or you start in the dumb zone; prefer progressive disclosure over dumping tool definitions and documents | `ReferencesElement → el-context-rot`, `ReferencesElement → el-progressive-disclosure` |
| `how-skills-vs-mcp-choice` | Pick skills vs MCP by what's actually hard | Skills when the hard part is reasoning/approach (they run on the agent's machine, self-modify, cost ~100 tokens idle); MCP when you need authentication, process isolation, or resources the agent's machine lacks (GPU fleets, huge restricted corpora); front heavy MCP servers with a skill for progressive disclosure | `ReferencesElement → el-agent-skills`, `ReferencesElement → el-mcp` |
| `how-treat-skills-as-software` | Treat skills as versioned, tested software | Skills take weeks to build well — version, evaluate, and test them; prefer human-authored (LLM-generated skills measurably hurt); vet third-party skills like early npm packages (author, adoption) because marketplaces lack verification; assume prompt-injection risk and remember skills run unisolated on your machine | `ReferencesElement → el-agent-skills` |

## Dropped

- Co-presenter "Carson" (audience/panel voice, surname never captured) — no Expert node; his MCP-inside-skills points are folded into `ins-skills-mcp-complementary`.
- "Devin Jensen talked about the Claude Agent registry" — passing shout-out, likely mistranscribed names; kept as prose in `sig-skills-ecosystem-scale`.
- React/npm history analogies, mode/moat definitional slides — framing, not facts.
- "Bad stuff on the news with OpenClaw" — too vague to be an incident signal (batch1 already carries the concrete skills-audit signals).

## Review notes

1. `sig-llm-written-skills-hurt` → `pat-verification-gap` is the stretchiest edge (human curation as the verification layer for generated context); drop if too clever.
2. `sig-docs-traffic-50pct-agents` and `sig-skills-ecosystem-scale` each carry a `pat-saaspocalypse` edge — software's consumers and distribution shifting to agents. Confirm that reading of the pattern's scope.
3. The context-rot paper is real published research (Chroma, 2025) but the talk cites it loosely; numbers in `sig-context-rot-25pct` are the speaker's paraphrase.
4. `el-openclaw` reuse assumes the registry entry covers the "most-starred repo, beat React" claim; if the registry brief says otherwise, keep the claim only in the signal here.
