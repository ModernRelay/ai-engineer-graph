# SPIKE extraction — "From Writing Code to Designing Systems: How the Developer Role is Changing" (Chris Noring, Microsoft) — FOR REVIEW

Source transcript: `transcripts/noring-microsoft-code-to-systems.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/GdvKNwMcfd0 — AI Engineer World's Fair, published 2026-07-11.
`stagingTimestamp` for the artifact and all signals: 2026-07-11 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-noring-code-to-systems` | From Writing Code to Designing Systems: How the Developer Role is Changing (Chris Noring, Microsoft — AI Engineer World's Fair) | youtube | https://youtu.be/GdvKNwMcfd0 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-chris-noring`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-chris-noring` | Chris Noring (AI engineering, Microsoft; 20 years in industry, ~19.5 of them editor-centric) | `AffiliatedWithCompany → co-microsoft` **[registry]** |

## Companies (0 new)

- `co-microsoft` **[registry]**, `co-github` **[registry]**, `co-anthropic` **[registry]** — all reused (Copilot tooling; cross-vendor guardrail convergence).

## Elements (3 new, 2 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agents-md` | AGENTS.md | concept | harness | Repo-level agent guidance file — the "absolute bare minimum" guardrail: high-level repository intent, application architecture, constraints, dos and don'ts (e.g. "never change the architecture unless told"); portable across repos and adoptable by existing codebases; cross-vendor convention |
| `el-custom-agents` | Custom agents (persona-scoped agent definitions) | concept | harness | The tier above skills: an agent definition with a persona and distinct role (security expert, back-end, researcher), able to reason, plan, orchestrate n skills, and use MCP servers, constrained by an explicit tool allowlist in its front matter (e.g. a researcher allowed web search but not file edits); lives in `.github/agents` for Copilot, with equivalents in Claude |
| `el-copilot-coding-agent` | GitHub Copilot coding agent (delegation) | product | harness | GitHub Copilot's asynchronous delegation surface: `/delegate` from the Copilot CLI sends the session to GitHub (starts a job, opens a draft PR), or assign-to-agent on any GitHub issue from the UI; agents run in sandboxes and can't escape, but can open draft PRs — the human-in-the-loop gate — while the developer keeps working |
| `el-agent-skills` **[registry]** | Agent skills | — | — | reused — skills as strict-contract, self-contained, intentionally constrained recipes (folder + SKILL.md with front matter); no new node |
| `el-mcp` **[registry]** | MCP | — | — | reused in prose only (custom agents use MCP servers; Playwright/GitHub MCP in demo); no new edges proposed |

Element edges: three new elements `IdentifiedInArtifact → ia-aie-noring-code-to-systems`; `el-agents-md` and `el-custom-agents` `ExemplifiesPattern → pat-harness-over-model` **[registry]**; `el-copilot-coding-agent` `DevelopedByCompany → co-github` **[registry]**; `el-custom-agents` `UsesElement → el-agent-skills` **[registry]** and `UsesElement → el-mcp` **[registry]**.

## Signals (5 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-noring-code-to-systems`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-devrole-shifted-2026` | Show of hands in a capacity AIE room (mid-2026): almost nobody still "codes like they used to" — the audience has shifted to a systems approach; Noring: "you are stuck with an AI tool — there's no longer an option not to use one"; devs still write code but are "very precious" about what they write by hand | `FormsPattern → pat-value-of-judgement` **[registry]** | `RelevantCompany → co-microsoft` **[registry]** |
| `sig-cli-displaces-editor` | A 20-year editor-native Microsoft engineer now starts the workday in the CLI — six-plus terminals of parallel agent runs ("build me an app", "fix this issue") while sipping coffee — and opens the editor only for fine adjustments, recast as a control board listening to CLI/repo streams | `FormsPattern → pat-value-of-judgement` **[registry]** | `RelevantCompany → co-microsoft` **[registry]** |
| `sig-guardrail-stack-convergence` | A tiered guardrail stack is presented as baseline practice: AGENTS.md in every repo → skills (strict-contract recipes) → custom agents (personas with tool allowlists + MCP); big vendors have converged on the same primitives — Anthropic and Microsoft/GitHub aligned on skills, near-identical layouts (`.claude/skills` vs Copilot's), "showing up at events together" | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-agents-md`, `OnElement → el-agent-skills` **[registry]**, `OnElement → el-custom-agents`; `RelevantCompany → co-microsoft` **[registry]**, `RelevantCompany → co-anthropic` **[registry]** |
| `sig-delegate-draft-pr-loop` | GitHub ships delegation as product: `/delegate` from Copilot CLI hands the session to GitHub (job + draft PR from sandboxed agents), and the GitHub UI assigns issues to the agent — "delegate, delegate, delegate, and go have a coffee"; whole product backlogs fanned out with draft PRs as the human review/merge gate | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-copilot-coding-agent`; `RelevantCompany → co-github` **[registry]** |
| `sig-demos-replace-decks` | Businesses report engineers no longer bring PowerPoints — they bring working demos; the MVP has become cheaper to produce than the slide deck about it | `FormsPattern → pat-value-of-judgement` **[registry]** | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-harness-not-vibes` | Agent leverage is gated on the guardrail stack, not model choice: agents are "toddlers" oscillating between genius and dumb, so constrain them like untrusted contractors — AGENTS.md intent, skill contracts ("do not improvise logic"), tool allowlists, sandboxes, and PR approval gates; 20× more code without guardrails is just 20× more slop | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-agents-md`, `ReliesOnElement → el-custom-agents` |
| `ins-devs-design-systems` | The developer job survives by moving up a level: from writing 100% of the code (linear, one-person progress) to designing the system the agents run within and applying judgment at review and merge — "scaling you, not replacing you"; the axe→chainsaw transition, and devs have always absorbed better tools | `HighlightsPattern → pat-value-of-judgement` **[registry]** | — |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-noring-code-to-systems`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-tiered-guardrails` | Set up the three-tier guardrail stack | Put an AGENTS.md in every repo (intent, architecture, constraints, dos/don'ts; copy a good one into fresh projects and tell the agent to adopt the codebase to it); when agents drift on repeatable multi-step tasks, write skills — one folder per skill + SKILL.md with name/description front matter and strict instructions; ask the AI itself to draft better skill instructions; when a task needs orchestration/reasoning across skills, define a custom agent with persona, argument hints, and a deliberately minimal tool allowlist (e.g. researcher: web yes, file edits no) | `ReferencesElement → el-agents-md`, `ReferencesElement → el-agent-skills` **[registry]**, `ReferencesElement → el-custom-agents` |
| `how-cli-first-delegation` | Run a CLI-first, delegate-to-PR workflow | Start in the CLI, not the editor; keep several terminals of agent runs in parallel; keep the editor for fine adjustments and as the control board; scale via `/delegate` (requires a proper GitHub repo) or assign-issues-to-agent from the GitHub UI; let sandboxed agents produce draft PRs and keep humans as the approval gate — review before merge, add more approval gates as needed | `ReferencesElement → el-copilot-coding-agent` |

## Dropped

- Claude Code / Claude Desktop and Copilot CLI/GitHub-UI/editor surface enumeration — passing product name-drops; `el-claude-code` **[registry]** not edged since the mention is non-load-bearing.
- Microsoft Agent Framework — single passing mention inside a demo prompt; no Element.
- Playwright MCP / GitHub MCP — demo details, folded into `el-copilot-coding-agent` prose.
- The finance-tracker demo app — demo apparatus.
- "Half the room Claude, half Copilot" audience poll — kept as color inside `sig-guardrail-stack-convergence` rather than its own signal.

## Review notes

1. **Caption garbles:** "AI slope" = *AI slop* (repeated); "a little finance tracker **by coded**" = likely *vibe-coded*; "IDs" = *IDEs*; "run a mock" = *run amok*; "whether you use code or IntelliJ" = *VS Code* or IntelliJ.
2. **Pattern candidate, NOT coined (per instructions):** this talk is a strong resonance point for the **"AI-native organization"** candidate (registry batches 3/5) — the developer role restructured around agent delegation, backlog-level fan-out. Signals were linked to existing `pat-value-of-judgement` / `pat-harness-over-model` / `pat-verification-gap` instead; add this file to the candidate's evidence list at central review.
3. `sig-delegate-draft-pr-loop` → `pat-verification-gap`: read as "trust re-architected outside the model" — sandbox + draft-PR + human merge as the verification surface for industrialized generation. Alternative home: `pat-value-of-judgement` (human as approval gate). Chose verification-gap to avoid four-of-five signals on one pattern.
4. `sig-devrole-shifted-2026` and `sig-demos-replace-decks` are anecdotal/secondhand observations (a show of hands; "I've heard some business…") — kept because they are dated, attributable claims of change from a named practitioner, but they are the weakest evidence tier in this file.
5. `el-custom-agents` is named generically (not "Copilot custom agents") because the speaker explicitly claims the concept exists across vendors ("I'm sure a similar concept exists in Claude"); flag if you want it vendor-scoped instead.
