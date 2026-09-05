# SPIKE extraction — "AI-Native Organisations Run on Skills: How to Structure and Scale Them" (Imad Touil, QuantumBlack) — FOR REVIEW

Source transcript: `transcripts/touil-quantumblack-ai-native-orgs-skills.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/M05vON8i0aI — AI Engineer World's Fair (AI-native enterprise / leadership track), published 2026-08-28.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a distinguished engineer at QuantumBlack (McKinsey's AI arm) argues that in an agentic stack "all of your know-how is at the skills level" — skills make organizational know-how executable, portable and cheap — and that **ungoverned skills are a new class of technical debt** (duplication, decay against new models, undiscoverable, ownerless, insecure). The answer is a governed skills registry platform run like an internal developer portal, with the same design principles as microservices. Caption garbles: "Imatel" → **Imad Touil**, "Quantum Black" → **QuantumBlack**, "entropic"/"Intropic" → **Anthropic**, "cloud code MD" → **CLAUDE.md**, "skills bench" → **SkillsBench**, "sub aents" → **sub-agents**, "vip coding" → **vibe coding**, "technical depths" → **technical debt**, "DLC" → **SDLC**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-touil-quantumblack-ai-native-orgs-skills` | AI-Native Organisations Run on Skills: How to Structure and Scale Them (Imad Touil, QuantumBlack — AI Engineer World's Fair) | youtube | https://youtu.be/M05vON8i0aI |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-imad-touil`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-imad-touil` | Imad Touil (Distinguished Engineer, QuantumBlack) | `AffiliatedWithCompany → co-quantumblack` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-quantumblack` | QuantumBlack | developer | McKinsey's AI/analytics arm (coerced consultancy → developer). Touil's 18 years serving enterprise organizations inform the "no single workflow builds everything" view; the talk's skills-governance simulation (15 teams, six months) is his own |

Reused **[registry]**, edge-only: `co-anthropic` **[seed]** (published the first skills article ~8 months ago; its best practices are the de-facto skills lint). Referenced, not coined: Backstage / IDP vendors (starting to centralize skills registries), Cursor (skills portability example).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-two-loop-agentic-stack` | The two-loop agentic stack | concept | harness | **Inner loop** — the coding-agent harness: context manager, tools/MCP, memory and state, skills loader. **Outer loop** — the workflows: skills, sub-agents, MCP servers, hooks — "harness blueprints that shape the behavior of your coding harness at runtime." **Enablement** beneath both: environment sandbox, an MCP gateway, a model gateway (open and frontier), a knowledge graph abstracting IT core systems / codebase / skills registry, a workflow marketplace. **Context layer** on top: project instructions (the CLAUDE.md), tool and MCP schemas, memory/conversation history, retrieved content |
| `el-enterprise-sdlc-is-not-four-steps` | The enterprise SDLC is not four steps | concept | | Specify → plan → tasks → implement is how coding agents are shaped today, but it is one product increment. The real lifecycle: product strategy and success metrics, market research and competitive analysis, discovery (problem statements, solution validation, experiments, user stories), **data product delivery** (pipelines, data-quality validation, catalog), the increment across many differently-shaped SDLCs (mobile, internal platform, customer-facing), platform engineering ops (infrastructure as code, provisioning), launch, performance optimization and incidents — and what's shown "is probably 10–20% of it," different in every organization |
| `el-skills-as-executable-knowhow` | Skills as executable know-how | concept | harness | Hooks trigger events, MCP tools are mostly someone else's, sub-agents just minimize context — "at the end of the day all of your know-how is at the skills level," and without well-structured skills there is no deterministic workflow. Skills are "a new unit that makes your know-how executable, portable and cheap." Design principles are the microservices principles: reusable, modular, discoverable, portable across workflows *and harnesses* (a Claude Code skill moves to Cursor), specialized (one task, not a monolith), composable (no duplication or conflicts), consistent/deterministic, cost-efficient via progressive disclosure. Example: a data-retention-policy skill composed with disclosure standards, GDPR rules and templates, pulled at runtime by a regulatory-disclosure-review workflow that emits an audit report |
| `el-skills-technical-debt` | Skills technical debt | concept | harness | Ungoverned skills create a new class of debt: **duplication** (teams on the same stack rebuild the same skills), **quality decay** (skills not re-validated against each new model degrade), **undiscoverability**, **no ownership** (no one maintains what no one owns), **non-composability** (needs a domain-driven catalog shape), **security** (public skills can carry prompt injection and executable scripts), and **permissions** (some skills embed sensitive business logic). A six-month, 15-team simulation shows ungoverned teams burning tokens re-deriving what a skill would have given in one shot, with uneven quality and security |
| `el-skills-registry-platform` | The skills registry platform | technology | harness | The centralized platform: a catalog with metadata, searchable, an MCP plugged into the catalog, a CLI that pulls skills into an IDE or a factory sandbox; dependency tracking; versioning and lifecycle (the agent detects a newer version and pulls it); access control; evaluation and observability — all under governance where architects, engineering leads, infra leads and cyber leads own domains and keep skills aligned with policy. Adoption path: individual create/test/improve → team sharing → centralized platform; the same treatment extends to whole workflows. IDP vendors are beginning to centralize this capability |

Element edges: all five `IdentifiedInArtifact → ia-aie-touil-quantumblack-ai-native-orgs-skills`.
`el-two-loop-agentic-stack` `UsesElement → el-agent-skills` **[registry]**, `el-agent-hooks` **[registry]**, `el-mcp` **[seed]**, `el-agents-md` **[registry]**;
`el-skills-as-executable-knowhow` `UsesElement → el-agent-skills` **[registry]**, `el-progressive-disclosure` **[registry]**, `el-skillsbench` **[registry]**;
`el-skills-registry-platform` `UsesElement → el-skills-as-executable-knowhow`, `el-skills-technical-debt`;
`el-skills-technical-debt` `UsesElement → el-skills-as-executable-knowhow`;
`el-skills-as-executable-knowhow` `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-skills-registry-platform` `ExemplifiesPattern → pat-ai-native-org` **[registry]**;
`el-skills-technical-debt` `ExemplifiesPattern → pat-agent-supply-chain` **[registry]**.

Reused elements (no new nodes): `el-agent-skills` **[registry]** (recommend widening its brief with the governance dimension), `el-skillsbench` **[registry]** (cited: with skills, outcomes "clearly higher" than the model alone on the same tasks), `el-progressive-disclosure` **[registry]**, `el-agent-hooks` **[registry]**, `el-agents-md` **[registry]**, `el-mcp` **[seed]**.

## Signals (6 new)

All: `SpottedInArtifact → ia-aie-touil-quantumblack-ai-native-orgs-skills`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-quantumblack`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-skills-standard-adopted-in-eight-months` | harness | The adoption curve as the speaker charts it: Anthropic's first skills article ~8 months ago → an open standard two months later → most agent harnesses adopting it by around February → an exploding count of skills across public GitHub repos and registries, "way more than this publicly and within your organizations." Show of hands in the room: many create and use skills, fewer share them, very few govern them across the organization — the ecosystem formed faster than its governance | `FormsPattern → pat-agent-supply-chain` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-agent-skills` **[registry]**, `el-skillsbench` **[registry]** |
| `sig-knowhow-lives-at-the-skills-level` | harness | The structural claim: hooks, MCP servers and sub-agents "don't bring structured value" — hooks fire events, MCP tools are mostly provided by others, sub-agents exist to save context — so organizational know-how ends up entirely in skills, and without well-structured skills "you're not really having a deterministic workflow." Skills are the unit that makes know-how executable, portable across harnesses, and cheap (progressive disclosure keeps tokens down) | `FormsPattern → pat-harness-over-model` **[registry]**; `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-skills-as-executable-knowhow`, `el-two-loop-agentic-stack` |
| `sig-ungoverned-skills-are-new-technical-debt` | harness | "If we don't govern skills, we start creating a new class of technical debt": duplication across teams on the same stack, quality decaying as new models land, undiscoverable and ownerless skills, non-composable catalogs, prompt injection and scripts in public skills, and sensitive business logic without access control. A six-month simulation over 15 teams shows the ungoverned state burning tokens and time re-deriving what a skill gives in one shot | `FormsPattern → pat-agent-supply-chain` **[registry]** | `OnElement → el-skills-technical-debt` |
| `sig-skills-registry-is-the-new-internal-developer-portal` | harness | The organizational answer recapitulates the microservices era: a governed skills registry (catalog, metadata, search, MCP + CLI access, dependencies, versioning, access control, evals, observability) owned by architects / engineering / infra / cyber leads — "the Backstage IDP moment for skills," and IDP vendors are already centralizing it. When governed, the next engineer's harness discovers and pulls the existing skill instead of rebuilding it; the same platform then centralizes whole workflows | `FormsPattern → pat-ai-native-org` **[registry]**; `FormsPattern → pat-agent-supply-chain` **[registry]** | `OnElement → el-skills-registry-platform` |
| `sig-enterprise-sdlc-is-mostly-outside-the-coding-loop` | | The four-step coding-agent workflow (specify/plan/tasks/implement) is a single product increment inside a lifecycle that runs from product strategy and market research through discovery, data-product delivery, many differently-shaped SDLCs, platform engineering and incident response — "what you're looking at is 10–20% of it." The enterprise value of agents is gated by the 80–90% no coding agent currently touches | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-enterprise-sdlc-is-not-four-steps`, `el-two-loop-agentic-stack` |
| `sig-auto-evolving-skills-need-governance-first` | harness | The forward look: skills registries (have one), skills evals (static-test skills against Anthropic's best practices — badly structured or wrongly invoked skills are usually low quality), and **auto-evolving skills** — the closed loop that improves skills automatically, "the next hype." His caution: switching that machine on without governance in place multiplies today's debt; the guardrails must precede the self-improvement loop | `FormsPattern → pat-continual-learning-turn` **[registry]** | `OnElement → el-skills-registry-platform`, `el-skills-technical-debt` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-skills-are-the-unit-of-organizational-knowhow` | The durable claim is where know-how *lives* in an AI-native organization: not in the model, not in the tools, but in a governed catalog of executable skills that any harness can pull — which makes the skills registry (ownership, versioning, evals, access control) the organizational substrate, and its governance the actual restructuring. It is the corpus's `pat-ai-native-org` "org-as-markdown" thesis taken to its logistics: markdown at scale needs a registry, owners, and a lifecycle | `HighlightsPattern → pat-ai-native-org` **[registry]** | `ReliesOnElement → el-skills-as-executable-knowhow`, `el-skills-registry-platform`, `el-two-loop-agentic-stack` |
| `ins-skills-recapitulate-the-microservices-governance-curve` | Skills are following microservices: the same design principles (reusable, modular, discoverable, composable), the same sprawl failure (duplication, ownerless services, undiscoverability), and the same institutional fix (a catalog/IDP with owners). The new twists are security (skills carry prompts and scripts — a supply-chain surface) and decay against a moving model. Governance arriving *after* adoption is the supply-chain pattern's recurring shape | `HighlightsPattern → pat-agent-supply-chain` **[registry]** | `ReliesOnElement → el-skills-technical-debt`, `el-skills-registry-platform` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-touil-quantumblack-ai-native-orgs-skills`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-govern-skills-across-an-organization` | Structure and scale skills like microservices with an IDP | Design each skill by the microservices principles — reusable, modular, discoverable, portable across harnesses, specialized to one task, composable without conflicts, deterministic, cost-efficient via progressive disclosure; adopt in three stages — individuals create/test/improve with one agreed tool, teams share and evolve, then a **centralized registry platform**: catalog with metadata and search, an MCP plugged into the catalog plus a CLI to pull skills into IDEs and sandboxes, dependency tracking, versioning and lifecycle so agents pull the latest, access control for sensitive business logic, evals and observability; assign **domain owners** (architects, engineering, infra and cyber leads) to keep skills aligned with policy; scan public skills for prompt injection and scripts before use; re-validate skills against each new model; static-test skills against Anthropic's best practices as a first eval; extend the same platform to whole workflows; and put governance in place *before* enabling any auto-evolving skills loop | `ReferencesElement → el-skills-as-executable-knowhow`, `el-skills-registry-platform`, `el-skills-technical-debt`, `el-two-loop-agentic-stack` |

## Dropped

- **The show-of-hands opening** — folded into `sig-skills-standard-adopted-in-eight-months`.
- **The simulation dashboard walkthrough** (per-team productivity/quality/cost bars) — summarized inside `el-skills-technical-debt`; figures are illustrative, not measured.
- **The regulatory-disclosure worked example** — folded into `el-skills-as-executable-knowhow`.

## Review notes

1. **⚑ Third same-batch skills-centric harness talk** (Navan: skills as the unit of context; Box: recursive agent + skills as the current rung; here: skills as the unit of organizational know-how with governance). Recommend widening `el-agent-skills` (b1) at review with the governance/registry dimension rather than coining a skills pattern.
2. **`pat-agent-supply-chain` gets its governance-side evidence.** The pattern was coined on the exploitation side (slopsquatting, malicious skills); Touil supplies the institutional response (registry, owners, security scanning, permissions). Three edges deliberately.
3. **`sig-auto-evolving-skills-need-governance-first` → `pat-continual-learning-turn`** is a cautious support: the self-improving-skills loop is named as the next wave, with governance as the precondition. Review may prefer to hold it.
4. **⚠ Verify before seeding:** the skills adoption timeline (8 months / 2 months / February), the SkillsBench comparison claim, and the simulation's parameters (15 teams, 5–12 per team, six months) — the simulation is the speaker's own model, not field data.
