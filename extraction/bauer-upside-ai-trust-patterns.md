# SPIKE extraction — "Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers" (Alex Bauer, Upside) — FOR REVIEW

Source transcript: `transcripts/bauer-upside-ai-trust-patterns.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/YZQsWVeN3rE — AI Engineer World's Fair, published 2026-07-11.
`stagingTimestamp` for the artifact and all signals: 2026-07-11 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-bauer-trust-patterns` | Design Patterns for AI Trust: Juries, Libraries, and Agent Tiers (Alex Bauer, Upside — AI Engineer World's Fair) | youtube | https://youtu.be/YZQsWVeN3rE |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-alex-bauer`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-alex-bauer` | Alex Bauer (Upside.tech; GTM/product-marketing leadership — previously led product marketing at a 600-person company; self-described "technical enough to be dangerous") | `AffiliatedWithCompany → co-upside` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-upside` | Upside | developer | upside.tech — "the data layer for the age of agentic go-to-market": GTM data foundation + dashboards, plus AI-native analysis (deep research, multi-touch attribution); founded to solve multi-touch attribution, built the data layer along the way. |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-jury-judge-workflow` | Jury-and-judge workflow | concept | harness | For questions with no empirically correct answer: spin up a jury of independent analyst agents that each examine the data separately and return an evidence-cited opinion; a consensus judge treats those opinions as input (not fact), weighs each analyst's reasoning quality, synthesizes the final answer, and escalates by expanding the jury when consensus is insufficient. Modeled explicitly on human trial-by-jury; shipped in Upside's multi-touch attribution product, enabled by Claude Opus-class models. |
| `el-upside-librarian` | Upside Librarian | product | context | Just-in-time context service inside Upside's product: before touching data, an agent consults the librarian — company documentation, a curated library of knowledge items (e.g., fiscal year runs Feb–Apr; "pipeline" means stage ≥ 2), and the schema of prior failed queries — then answers with citations. Prevents the confident-wrong default (assuming quarter = Jan–Mar on created-date). |
| `el-agent-tiers` | Agent tiers | concept | harness | Capability tiering of agent harnesses as a trust/procurement criterion: important work needs at least "tier 2" — a powerful reasoning model plus subagents, plan mode, full MCP support, and file editing. AI crowbarred into a pre-existing subscription price point can't afford intelligent reasoning models under its margin — "you can't fix stupid; friends don't let friends use really bad harnesses." |
| `el-commanders-intent` | Commander's intent prompting | concept | harness | Armed-forces doctrine applied to prompting: tell agents why you want something, not micromanaged steps — they perform markedly better (as do humans). Requires active counter-pressure: models trained on human material micromanage themselves, so pull them back to the why. |

Element edges: all four `IdentifiedInArtifact → ia-aie-bauer-trust-patterns`; `el-jury-judge-workflow` `ExemplifiesPattern → pat-verification-gap` **[registry]**; `el-upside-librarian` `DevelopedByCompany → co-upside`, `ExemplifiesPattern → pat-context-graphs` **[registry]**; `el-agent-tiers` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-bauer-trust-patterns`, `SourcedFromSource → source-aie-yt` **[registry]**. Domain per row.

| slug | name / brief | domain | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-gtm-teams-become-builders` | GTM teams — historically the lowest builder-density function, running on spreadsheets and slides — are becoming builders: "Claude does for building what the bicycle did for mobility," an "infinite supply of valedictorian interns with CS degrees" for the people closest to the problem. Concrete delta: a full website rebuild that took several product marketers, a designer, consulting PMs, and a web team ~2 months at his previous 600-person company is now one non-engineer + Claude | harness | `FormsPattern → pat-saaspocalypse` **[registry]** | `RelevantCompany → co-upside` |
| `sig-hallucination-becomes-trust-problem` | The "AI hallucination problem" discourse of a couple of years ago has faded and matured into its "older sibling," a trust problem: ask Claude to report revenue and it doesn't say "I'm not sure" — it gives a wrong answer that looks exactly like being right. Upside's countermeasures: citation track-records on every compiled fact and a data layer underneath the disagreeing systems "where the data finally agrees with itself" | context | `FormsPattern → pat-verification-gap` **[registry]** | `RelevantCompany → co-upside` |
| `sig-jury-judge-in-production` | Upside ships jury-and-judge attribution: independent analyst agents produce evidence-cited opinions on a deal's attribution credit; a consensus judge weighs reasoning quality (input, not fact) and expands the jury absent consensus — porting trial-by-jury to questions with no empirically correct answer. Multi-touch attribution, "the holy grail of go-to-market," became tractable ~2 years in, "enabled by Opus" | harness | `FormsPattern → pat-verification-gap` **[registry]** | `RelevantCompany → co-upside` |
| `sig-jit-librarian-in-production` | Upside ships a librarian agents must consult before querying: company docs, curated knowledge-item definitions (fiscal year Feb–Apr; pipeline = stage ≥ 2), and the schema of prior failed queries, injected as just-in-time memory with cited answers back — so definitions are discovered before the query, not after the wrong dashboard | context | `FormsPattern → pat-context-graphs` **[registry]** | `RelevantCompany → co-upside` |
| `sig-subscription-ai-cant-reason` | Slack shipped Slackbot MCP-client support ~2 weeks before the talk; the speaker wired it to his own librarian and found it "horrifically stupid" for real work — generalizing: any AI crowbarred into a pre-existing subscription price point lacks margin for an intelligent reasoning model, so harness tier (powerful model, subagents, plan mode, full MCP, file editing) is now a procurement criterion; don't let teams do important work in a chat web UI | harness | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-salesforce` **[registry]** (Slack's owner — see notes) |

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-manage-agents-like-humans` | When in doubt, manage agents like other humans: the trust mechanisms we already run for people — commander's intent instead of micromanagement, onboarding guides/librarians, second opinions, juries of peers — port directly to agent design and beat both bleeding-edge optimizations and prompt incantations in day-to-day practice. All three of the talk's shipped examples are org-design patterns, not model tricks | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-commanders-intent`, `ReliesOnElement → el-jury-judge-workflow`, `ReliesOnElement → el-upside-librarian` |
| `ins-deliberation-replaces-ground-truth` | Where no empirically correct answer exists (attribution credit), verification cannot be a truth-checker; it becomes structured deliberation — independent sampling by evidence-citing analysts plus a judge weighing reasoning quality, escalating by widening the jury. Extends the judge/verifier playbook beyond checkable outputs into judgment questions | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-jury-judge-workflow`, `ReliesOnElement → el-judge-as-classifier` **[registry]** |
| `ins-pricing-caps-harness-intelligence` | A product's pricing model caps its harness intelligence: AI bundled into existing subscription margins structurally can't afford reasoning models, so trustworthiness is decided at tool-selection time — pick by tier attributes (model power, subagents, plan mode, MCP, file editing), not by the convenience of a subscription you already pay for | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-agent-tiers` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-bauer-trust-patterns`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-commanders-intent-prompting` | Prompt with commander's intent | State the why and the desired outcome, not step-by-step instructions; expect self-micromanagement ("don't tell Claude to improve itself — you'll get micromanagement") and pull the agent back to intent; the same doctrine improves delegation to humans | `ReferencesElement → el-commanders-intent` |
| `how-scaffold-then-delegate` | Define structure first, then turn Claude loose | Don't YOLO large deliverables even with plan mode — it fails today. Maintain living "anchor assets" for the company: personas, and a product-capabilities reference compiled BY the AI with citations back to every connected system (so you can verify it didn't hallucinate the parts that matter); new work ladders up from those assets. Keep a bench of persona agents to review drafts on demand from each audience's perspective | `ReferencesElement → el-claude-code` **[registry]** |
| `how-jit-librarian-pattern` | Put a librarian between agents and data | Centralize documentation, curated definitions/knowledge items, and the schema of prior failed queries; make agents consult it before acting rather than embedding definitions per prompt; return answers with citations; every failed query enriches the library — tribal definitions become just-in-time memory instead of rediscovered mistakes | `ReferencesElement → el-upside-librarian` |

## Dropped

- The bedtime-story allegory (dragon = the data pile, first guardian = security review defeated "with paperwork", many-headed monster = conflicting metric definitions) — framing device; its referents are captured in the signals.
- The unnamed "best book on product capabilities reference" + "general D Sloop scale" — slide-only / garbled beyond recovery (see notes).
- "Persona Bench" — kept as prose inside `how-scaffold-then-delegate`, not coined (unclear if product or internal practice).
- "Jeff from XAI is coming up later… basically created Upside for all the rest of the world's data" — teaser for another talk, not this talk's content.
- Audience-poll results (engineers vs. "technical enough to be dangerous" vs. non-coders) — color supporting `sig-gtm-teams-become-builders`.

## Review notes

1. **"Radiant librarian" garble:** captions say "our radiant librarian," later "the Upside Librarian." Element named Upside Librarian; "radiant" may be a real product adjective (Radiant Librarian?) — verify before public-facing use.
2. **Unresolved garble:** "Two other important things are general D Sloop scale, there are a ton of these floating around" — possibly "general de-slop skills/scale"; unrecoverable from audio, dropped. The recommended book on product-capability references is shown on a slide, never spoken — unrecoverable from transcript.
3. **"Enabled by Opus"** — no version stated; deliberately did NOT link registry `el-claude-opus-47`. Kept as prose in `sig-jury-judge-in-production` and the `el-jury-judge-workflow` brief.
4. `sig-subscription-ai-cant-reason` carries `RelevantCompany → co-salesforce` because Slack is Salesforce-owned and the registry has no Slack node; swap to a new `co-slack` if you'd rather not conflate. Dated fact inside: Slackbot MCP client shipped ~2 weeks pre-talk (~late June 2026).
5. **Speaker bio inferred:** role at Upside not stated; "previously led product marketing at a 600-person company" is explicit — expert brief hedged to GTM/product-marketing leadership.
6. **`el-judge-as-classifier` reuse (batch 3):** the jury-judge pattern extends it — from classifying outputs to weighing reasoning quality across independent analysts; kept both nodes, cross-linked via `ins-deliberation-replaces-ground-truth`. Merge-flag if the reviewer reads them as one concept.
7. Zero new patterns from this talk: "manage agents like humans" reads as an application of `pat-harness-over-model` + `pat-verification-gap`, not a seed-altitude thesis of its own.
