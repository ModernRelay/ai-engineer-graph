# SPIKE extraction — "The Era of Compound Engineering" (Kieran Klaassen, Every / Cora) — FOR REVIEW

Source transcript: `transcripts/klaassen-every-compound-engineering.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/_ehJyfHg1Vk — AI Engineer World's Fair, published 2026-08-20.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-20 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: "I haven't written a single line of code this year" — the solo engineer behind Cora (an agent-native email client used by thousands, rebuilt as v2 since January) on **compound engineering**: extracting thinking and taste into a system that compounds. The bottleneck moved from code → plans → deciding what to build → memory → judgement and taste. The loop: brainstorm → plan → work → review → polish → **compound** → repeat, with the human as "the bread" at both ends; 50% of time on the feature, 50% teaching the system; solutions documented in the repo. The open-source compound-engineering plugin (`/ce ideate`, `/ce brainstorm`, `/lfg`, `/ce polish`, `/ce compound`) is used by hundreds of thousands daily. Caption garbles: "Kiran" → **Kieran**, "core as"/"Kora" → **Cora**, "cloth MD" → **CLAUDE.md**, "codeexcloud code" → Codex / Claude Code, "reals" → **Rails**, "Trevan Chowo" → ⚠ co-contributor name uncertain, "CE ID8" → **/ce ideate**, "SL LFG" → **/lfg**, "vip coding" → vibe coding.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-klaassen-every-compound-engineering` | The Era of Compound Engineering (Kieran Klaassen, Every / Cora — AI Engineer World's Fair) | youtube | https://youtu.be/_ehJyfHg1Vk |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-kieran-klaassen`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-kieran-klaassen` | Kieran Klaassen (Every / Cora; ex-VP Engineering and founder) | `AffiliatedWithCompany → co-every` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-every` | Every | media | "An AI lab for the future of work" that writes, teaches and builds; a studio of mostly single-engineer teams shipping products (Cora, an agent-native AI email client rebuilt as v2 by one engineer with support). Coerced publisher + product studio → media. Author of the open-source compound-engineering plugin |

Reused **[registry]**, edge-only: `co-anthropic` **[seed]** (Sonnet 3.5 as the moment "something new was unlocked"; Claude Code / Cowork as hosts), `co-openai` (Codex host), `co-cursor` (host).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-compound-engineering` | Compound engineering | concept | harness | Extract your thinking and taste into a system that compounds, so the next feature is easier to build than the last — flipping the usual accrual of complexity. The loop: brainstorm → plan → work → review → polish → **compound** → repeat, a "human–AI sandwich" with the brain on at both ends (deciding what and why; raising the bar on taste) and a middle that must run without you, overnight, in parallel. Rule: 50% of time on the feature, 50% teaching the system what it got wrong. "One engineer with a compounding system beats full teams that use AI without one" |
| `el-moving-bottleneck` | The moving bottleneck | concept | | Two years of solo building traced where the constraint sat: bad code and hallucination → (agents, skills, review) plans → (good plans do bigger things) deciding what to build → repeating yourself → a memory system (CLAUDE.md grew too large) → **judgement and taste**. "Implementation is mostly solved… the thing that doesn't work is our judgement and our taste" — where you turn your brain on versus leverage the model |
| `el-solution-documents-in-repo` | Document the thinking, not the code | concept | context | Learnings are stored in the repository as solution documents — reasoning, decisions, postmortems ("what decision by whom or what agent led to this, and what do we change") — so the next brainstorm already includes them. Counter-intuitively **more token-efficient**: with the answers already in context there is no re-research, review or correction. "My brain is fixed and AI isn't — keep extracting until the middle runs itself and surprises you" |
| `el-compound-engineering-plugin` | The compound-engineering plugin | product | harness | Open-source plugin for Claude Code, Codex, Cursor and ~10 other harnesses, used by hundreds of thousands daily. `/ce ideate` — structure open tickets/issues/Slack/Intercom into scored ideas (against OKRs, a `/ce strategy` doc, past experiments) as a shareable HTML page; `/ce doc-review` — sharp questions on a PRD, answers compounded; `/ce brainstorm` — the brain-on command that pulls compound knowledge and personas and asks just enough questions; `/lfg` — the overnight loop: plan, work, review, test, dogfood, fix, open a PR with before/after video; `/ce polish` — raise the bar on the result, not QA; `/ce compound` — extract the learning so it never repeats. Grew into "compound product" for PMs, designers and knowledge workers |
| `el-brain-at-the-ends` | Brain at the ends | concept | | Don't offload the thinking: at the start truly understand the problem and decide what to work on; let the machine rip in the middle; at the end raise the bar ("we're not shipping shitty code"). If you're still needed in the middle, spend time on the middle until a three-hour run is always good. "Implementation is only getting cheaper and judgement is not" |

Element edges: all five `IdentifiedInArtifact → ia-aie-klaassen-every-compound-engineering`.
`el-compound-engineering-plugin` `DevelopedByCompany → co-every`;
`el-compound-engineering` `UsesElement → el-moving-bottleneck`, `el-solution-documents-in-repo`, `el-brain-at-the-ends`, `el-background-agents` **[registry]**;
`el-compound-engineering-plugin` `UsesElement → el-compound-engineering`, `el-agent-skills` **[registry]**, `el-claude-code` **[registry]**, `el-codex` **[registry]**;
`el-solution-documents-in-repo` `UsesElement → el-agents-md` **[registry]**, `el-karpathy-llm-wiki` **[registry]**;
`el-compound-engineering` `ExemplifiesPattern → pat-continual-learning-turn` **[registry]**;
`el-solution-documents-in-repo` `ExemplifiesPattern → pat-agent-memory-layer` **[registry]**;
`el-brain-at-the-ends` `EnablesPattern → pat-value-of-judgement` **[registry]**.

Reused elements (no new nodes): `el-background-agents` **[registry]**, `el-agent-skills` **[registry]**, `el-claude-code` **[registry]**, `el-codex` **[registry]**, `el-agents-md` **[registry]** (outgrown as the memory), `el-karpathy-llm-wiki` **[registry]** (solution docs as the wiki), `el-ralph-loop` **[registry]** (the `/lfg` loop's ancestor).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-klaassen-every-compound-engineering`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-every`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-implementation-solved-judgement-is-the-bottleneck` | | Two years of solo product-building traced the bottleneck from code to plans to deciding what to build to memory to judgement and taste: "implementation is mostly solved… the thing that doesn't work is our judgement." The bet: implementation keeps getting cheaper, judgement does not, so systems must be set up to have access to the human's judgement | `FormsPattern → pat-value-of-judgement` **[registry]**; `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-moving-bottleneck`, `el-brain-at-the-ends` |
| `sig-one-engineer-with-a-compounding-system-beats-teams` | | A former VP of Engineering deliberately stayed solo (with design/DB support) to see how far AI goes before hiring, and rebuilt a full agent-native email client alone since January without writing code. Claim: one engineer with a compounding system beats full teams that use AI without one — the thin-team thesis stated as a lived experiment | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-compound-engineering` |
| `sig-extract-until-the-middle-runs-itself` | context | The mechanism: every repetition is extracted into repository solution documents (reasoning, postmortems, taste rules), 50% of time goes to teaching the system, and the loop runs overnight in parallel — more token-efficient over time because the answers are already in context. When CLAUDE.md grew too large, a memory system replaced it. Learning that compounds outside the weights, in the repo | `FormsPattern → pat-continual-learning-turn` **[registry]**; `FormsPattern → pat-agent-memory-layer` **[registry]** | `OnElement → el-solution-documents-in-repo`, `el-compound-engineering`, `el-agents-md` **[registry]** |
| `sig-compound-plugin-used-by-hundreds-of-thousands-daily` | harness | A personal plugin shipped while building Cora — ideate, brainstorm, overnight loop with before/after video, polish, compound — is now used by hundreds of thousands of people daily across a dozen harnesses and has spread to PMs, designers and knowledge workers. A practitioner's loop became a de facto harness standard without a launch | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-compound-engineering-plugin` |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-compounding-is-judgement-made-reusable` | The durable claim is what the compounding system stores: not code but the human's reasoning and taste, extracted each time they would otherwise be repeated, so that the next brainstorm starts from them. That makes the repository the memory layer, the human's judgement the appreciating asset, and "the next feature should be easier" the test of whether learning is actually accumulating | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-compound-engineering`, `el-solution-documents-in-repo`, `el-brain-at-the-ends` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-klaassen-every-compound-engineering`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-practice-compound-engineering` | Extract, never repeat; brain at the ends; make the middle boring | Run the loop brainstorm → plan → work → review → polish → compound → repeat; keep your brain on at the ends — decide the problem yourself at the start (block time, don't multitask) and raise the bar at the end; whenever you repeat yourself, **extract** it into repository solution documents (reasoning, decisions, postmortems, taste rules) so it never happens again; spend **50% of time teaching the system** what it got wrong; work the middle manually until an overnight or three-hour run is always good, then let it rip in parallel; document the thinking, not the code; use or build the tooling — ideation against OKRs, doc review, brainstorm, an overnight loop with before/after evidence, polish, compound; and hold the standard that the next feature should be easier because you shipped this one | `ReferencesElement → el-compound-engineering`, `el-solution-documents-in-repo`, `el-brain-at-the-ends`, `el-compound-engineering-plugin`, `el-moving-bottleneck` |

## Dropped

- **The Rails/React stack detail and beta-access pitch** — in the company row.
- **The PowerPoint-from-ideation anecdote** — folded into the plugin element.

## Review notes

1. **⚑ A clean `pat-value-of-judgement` + `pat-continual-learning-turn` pairing from a solo builder**: the loop lives in repo documents (memory layer), and what it stores is judgement. Pairs with Hall (b22) on judgement as the non-trainable input.
2. **`co-every` coined `media`** (publisher + studio); Bhagwat's earlier Every talk did not coin the company — if review prefers `developer`, retype.
3. **⚠ Verify before seeding:** "hundreds of thousands daily," the plugin's command names, "haven't written a line of code this year," the co-contributor's name.
