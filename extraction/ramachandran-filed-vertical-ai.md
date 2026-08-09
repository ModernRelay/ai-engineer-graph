# SPIKE extraction — "Chat and citations won't save your vertical AI" (Atul Ramachandran, Filed Inc) — FOR REVIEW

Source transcript: `transcripts/ramachandran-filed-vertical-ai.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/RGiXcVxSD3s — AI Engineer World's Fair, published 2026-07-11.
`stagingTimestamp` for the artifact and all signals: 2026-07-11 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-ramachandran-vertical-ai` | Chat and citations won't save your vertical AI (Atul Ramachandran, Filed — AI Engineer World's Fair) | youtube | https://youtu.be/RGiXcVxSD3s |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-atul-ramachandran`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-atul-ramachandran` | Atul Ramachandran (CTO & co-founder, Filed; 10+ years building products) | `AffiliatedWithCompany → co-filed` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-filed` | Filed Inc | developer | Vertical-AI agents for US tax professionals; raised $17M+; ~2 years old at talk time |

## Elements (2 new, 1 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-conveyor-belt-agent-product` | Conveyor-belt agentic product model | concept | harness | Product model for agentic delegation: the product is a conveyor belt, AI agents are the workers, users are supervisors. Four pillars: delegate (find repeatable >1-hour tasks → long-running background agents), teach (skills capture how each user works), monitor (task lists + per-value traces), control (pause-fix-resume, plan approval before irreversible actions) |
| `el-weekly-active-sessions` | Weekly active sessions (WAS) | concept | — | Proposed success metric for delegation-era products: a task completed by a human or an agent, counted whether or not the user is on the platform; replaces weekly active users — the target is WAU down while WAS up |
| `el-agent-skills` **[registry]** | Agent skills | — | — | reused for Filed's skills-as-product-feature discussion; no new node |

Element edges: both new elements `IdentifiedInArtifact → ia-aie-ramachandran-vertical-ai`; `el-conveyor-belt-agent-product` `ExemplifiesPattern → pat-saaspocalypse` **[registry]**.

## Signals (5 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-ramachandran-vertical-ai`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-filed-revenue-inflection` | Filed (AI agents for US tax pros, $17M+ raised) closed more revenue in a single month (mid-2026) than in the entire preceding year, two years into building — demand inflection for vertical AI agents in tax | `FormsPattern → pat-saaspocalypse` **[registry]** | `RelevantCompany → co-filed` |
| `sig-chat-citations-insufficient` | Practitioner verdict after 2 years of vertical tax agents: chat is synchronous (user must sit and wait) and citations push the verification burden onto the customer (reviewing agent work item by item) — together they break the sold promise of "agents do the work while you sleep"; customers in healthcare/legal/tax complain the promise is not kept | `FormsPattern → pat-verification-gap` **[registry]** | `RelevantCompany → co-filed` |
| `sig-agentic-delegation-abstraction` | Third product-abstraction level claimed live: physical presence (value bottlenecked on employee count) → digital self-serve (bottlenecked on user count) → agentic delegation, where users hand off long-running work and leave — value generation decouples from user visits entirely | `FormsPattern → pat-saaspocalypse` **[registry]** | — |
| `sig-wau-obsolete` | Filed argues weekly active users is now the wrong north-star for agentic products and tracks weekly active sessions instead; explicit goal: WAU goes down (not to zero) while WAS goes up — users trusting the platform enough to delegate and walk away | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-weekly-active-sessions`; `RelevantCompany → co-filed` |
| `sig-automatic-skill-capture` | Filed captures agent skills automatically from product usage — a separate skill-authoring interface "won't work" — to encode each firm's conventions, the last 20% of work where the real value sits; cites an unnamed well-known product doing the same (name garbled in captions) | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-agent-skills` **[registry]**; `RelevantCompany → co-filed` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-design-for-delegation` | Design vertical AI for delegation, not participation: chat and citations are participation-era interfaces; the value unlock is long-running background agents wrapped in supervision surfaces (teach/monitor/control) — ask of every feature "what would delegating this look like?" rather than "how does the user do this here?" | `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-conveyor-belt-agent-product` |
| `ins-reversibility-builds-delegation-trust` | Users only delegate what they believe they can take back: keep level-2 self-serve features alongside agents, let users pause the belt, fix, and restart ("take the wheel, not abandon the car"), and present approvable plans before irreversible actions (e.g. data entry that can erase tax-software records) — reversibility is the trust substrate that makes delegation happen at all | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-conveyor-belt-agent-product` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-ramachandran-vertical-ai`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-delegation-conveyor` | Build the four pillars of a delegation product | Find user tasks that take >1 hour and are (roughly) repeatable — Filed found three in the tax workflow — and build them as long-running background agents; capture skills automatically from product usage to encode the user's way of working (the last 20%); expose a task list plus per-value traces so every agent-produced value is traceable (this is where trust is built and complaints die); pause automatically when the agent would make an assumption and let users resolve conflicts by tagging the agent chat-style; present plans for approval before irreversible/dangerous actions | `ReferencesElement → el-conveyor-belt-agent-product`, `ReferencesElement → el-agent-skills` **[registry]** |
| `how-measure-agentic-value` | Measure delegation, not presence | Replace weekly active users with weekly active sessions (tasks completed by human or agent, user present or not); aim for WAU declining while WAS climbs; treat rising WAS with falling WAU as evidence users trust the platform enough to delegate and leave | `ReferencesElement → el-weekly-active-sessions` |

## Dropped

- The bank-branch → mobile-banking → agentic-delegation story — framing device; folded into `sig-agentic-delegation-abstraction`.
- "Save you money or save you cost" vertical-AI sales pitch — context, not an entity.
- Chat/citations as Elements — deliberately not coined; they are generic interface primitives, load-bearing only as the foil in `sig-chat-citations-insufficient`.

## Review notes

1. **Caption garble, unresolved:** "a prime example you would have used a product called this before. They also have like automatic skills" — the referenced product name is lost in captions (plausibly Cursor or Claude; unverifiable). Kept unnamed in `sig-automatic-skill-capture`.
2. `sig-filed-revenue-inflection` → `pat-saaspocalypse` is a judgment call: read as evidence that delegation-model vertical agents are commercially displacing seat-based software economics in tax. If reviewers want saaspocalypse reserved for incumbent-SaaS disruption evidence, drop the edge and leave the signal pattern-less.
3. Three of five signals land on `pat-saaspocalypse` — this talk is essentially a saaspocalypse playbook from inside a vertical; flagging the concentration rather than spreading edges artificially.
4. `el-weekly-active-sessions` is a metric, thinner than most Elements; kept because the KnowHow and a signal both lean on it. Demote to prose if below the element bar.
5. Revenue claim ("more revenue last month than the whole prior year") and "$17M raised" are speaker statements, not externally verified.
