# SPIKE extraction — "Notion's Token Town" (Sarah Sachs, Notion) — FOR REVIEW

Source transcript: `transcripts/sachs-notion-token-town.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/-I5W5QVAT8E — AI Engineer World's Fair, published 2026-07-23.
`stagingTimestamp` for the artifact and all signals: 2026-07-23 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node. `co-notion` exists (batch 6); the speaker is new.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-sachs-token-town` | Notion's Token Town (Sarah Sachs, Notion — AI Engineer World's Fair) | youtube | https://youtu.be/-I5W5QVAT8E |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-sarah-sachs`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-sarah-sachs` | Sarah Sachs (leads AI engineering teams at Notion; negotiates Notion's AI vendor contracts — the "Anna Wintour of AI contracts") | `AffiliatedWithCompany → co-notion` **[registry]** |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-parallel` | Parallel | developer | web-search API provider for AI products; Notion's announced web-search partner, chosen on whole-trajectory evals rather than per-call cost/latency |
| `co-decagon` | Decagon | developer | customer-support/voice agent vendor; Notion orchestration partner — tagged in where Claude Code isn't the best at customer voice |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-notion-auto-model` | Notion auto model | product | inference | Notion's model-agnostic router: state-of-the-art models always available, with an "auto" tier handling ~75% of traffic; switching between models inside the product and exposed to customers ("AI Switzerland") so neither Notion nor its customers are vendor-locked |
| `el-notion-workers` | Notion workers | product | infra | Recently launched CPU-based job runners on the "CPUs over GPUs" principle: discrete deterministic work — CSV→PDF, tool calls via a CLI, SQL queries — needs no LLM; routing it off GPUs is where products stop becoming token-poor |
| `el-cost-per-capability-per-second` | Cost per capability per second | concept | inference | Procurement/eval metric for model choice: judge whole task trajectories (not single calls or per-token price) on the joint trade-off of cost, capability, and latency — e.g., Parallel wins on full web-search trajectories while looking unremarkable on single-call cost or latency |

Element edges: all three `IdentifiedInArtifact → ia-aie-sachs-token-town`; `el-notion-auto-model` and `el-notion-workers` `DevelopedByCompany → co-notion` **[registry]**; `el-notion-auto-model` `EnablesPattern → pat-harness-over-model` **[registry]**; `el-notion-auto-model` `UsesElement → el-cost-per-capability-per-second`.

## Signals (6 new)

All: `SpottedInArtifact → ia-aie-sachs-token-town`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | domain | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-supplier-is-competitor` | Notion's AI lead states it plainly: your supplier is your competitor. Frontier labs sell tokens to applied companies while underpricing their own first-party products (the Dylan [Patel] chart of first-party vs API pricing); reselling surcharged tokens is not defensible value, and tying to one provider means no exit — "you are crossing your fingers and hoping you are a viable business" | inference | `FormsPattern → pat-saaspocalypse` **[registry]** | `RelevantCompany → co-notion` **[registry]** |
| `sig-token-cost-structural-barrier` | Cost, not capability, is the structural barrier: real recurring scenarios — a reasoning upgrade at the same per-token price that uses 3x the output tokens; a new model digit priced +40% with the predecessor deprecated in 4 months — now land "pretty much monthly," while revenue doesn't grow 40% in step; 88% of companies can't get past AI-as-assistant; a Citadel memo argues simpler models may be the most cost-effective productivity pathway (frontier/everyday bifurcation) | inference | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-notion` **[registry]** |
| `sig-notion-auto-model-75pct` | Notion's auto model handles ~75% of its AI traffic; the harness is built as model interoperability (multi-model, cache-kill and mid-transcript switching investment), routing by traffic pattern (Opus-class for large-scale data analysis, never for email triage — "we'd be ripping you off and ourselves"), with whole-trajectory evals (Parallel web search) driving choices | inference | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-notion` **[registry]**, `RelevantCompany → co-parallel` |
| `sig-openweight-negotiation-leverage` | Open-weight models are now strong enough for moderate tasks and RL-expandable upmarket — "Kimi [K2.6] was probably the first time an open model outperformed [GPT-5.2]; GLM [5.2] is another bombshell" — functioning as the credible alternative that lowers customers' cost barrier and puts downward pricing pressure on the frontier oligopoly; the gap to frontier gets covered in ~6 months, so be prepared now | inference | `FormsPattern → pat-sovereign-ai` **[registry]** (flagged — see notes) | `RelevantCompany → co-notion` **[registry]** |
| `sig-notion-software-factory` | Notion runs its own software factory in production: agents orchestrated inside live collaborative documents (not markdown files) — Claude agent scopes a spec via the new managed-agent capability, humans and PMs get tagged in, Decagon collects customer-voice data, Claude Code opens the PR, Codex reviews it; almost all polish/large-feedback work internally is coordinated this way, with >3 minutes saved per task at customer scale | harness | `FormsPattern → pat-ai-native-org` (coined 2026-08-16) | `RelevantCompany → co-notion` **[registry]**, `RelevantCompany → co-decagon` |
| `sig-durable-record-for-agents` | Notion's thesis on why AI-as-system fails (88% stuck at assistant): too much siloed data and no durable system of record at the point of collaboration — which is now human↔human, human↔agent, and agent↔agent; persistence of enterprise knowledge across agent work is "really not discussed enough" | context | `FormsPattern → pat-context-graphs` **[registry]** | `RelevantCompany → co-notion` **[registry]** |

Additional signal edges: `sig-notion-auto-model-75pct` `OnElement → el-notion-auto-model`; `sig-openweight-negotiation-leverage` `OnElement → el-glm-52` **[registry]**; `sig-notion-software-factory` `OnElement → el-claude-code` **[registry]**, `OnElement → el-codex` **[registry]**.

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-value-transcends-tokens` | An applied-AI company cannot win on token economics against its own supplier; the durable value is everything around the tokens — product expertise, data flywheels, knowing your customers' traffic (when they need capability vs price vs latency), and compelling UI/orchestration. "Bet on the frontier, not on the lab": stop trying to train, build the best product that uses many models | `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-cost-per-capability-per-second` |
| `ins-optionality-is-leverage` | Model optionality is the negotiating leverage: oligopoly pricing follows gas-station dynamics (the #2 model only needs to be $1/M-tokens cheaper), so price does not correlate with capability, leaders rotate monthly, and a lab-exclusive discount that removes your ability to walk is the most expensive decision you can make — worse than the engineering cost of interoperability | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-notion-auto-model` |
| `ins-security-over-capability` | The challenge of the next six months is security, not capability: any system combining private-data access, exposure to untrusted content (ingestion/MCP/email/web payloads), and external communication — the lethal trifecta — is exposed, and the more autonomous the system, the more unsupervised the risk; sandboxing, visibility, and governance of what agents see/do/persist is what builds valuable product and better token economics | `HighlightsPattern → pat-new-cyber-threats` **[registry]** | `ReliesOnElement → el-lethal-trifecta` **[registry]** |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-sachs-token-town`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-model-agnostic-playbook` | The model-agnostic playbook ("this is the slide") | Build for multi-model from the start: invest in killing the cache and switching models mid-transcript (doesn't have to be per-thread) — treat the harness as model interoperability. Evaluate cost per capability per second on entire trajectories, not single calls or token price. Switch fast and often. Give labs something back: eval-program partnerships are exchangeable value in negotiations — better than extraordinarily large commits, and no discount is worth the loss of optionality | `ReferencesElement → el-notion-auto-model`, `ReferencesElement → el-cost-per-capability-per-second` |
| `how-route-traffic-by-complexity` | Route traffic by complexity; be the expert on what complexity is | Not all traffic is equal — sending everything to the latest Opus-class model is a huge miss; define frontier-vs-everyday for YOUR product. For moderate tasks, assess open weights first without RL, on your own evals (your tool errors, your actual latency) rather than external benchmarks. Push deterministic work to CPUs — no LLM for CSV→PDF, CLI tool calls, or SQL. Layer governance on top: visibility into who uses what data, maintainability, control — model optionality is also a governance offering to customers | `ReferencesElement → el-notion-workers`, `ReferencesElement → el-notion-auto-model` |

## Dropped

- The AI-transformation journey ladder (thought partner → assistant → teammates → AI-as-system) — framing device; folded into `sig-durable-record-for-agents` / `sig-token-cost-structural-barrier`.
- Citadel as a Company node and its memo as an artifact — second-hand mention; kept as prose in `sig-token-cost-structural-barrier`.
- Kimi K2.6 as a new Element — version mention atop seed `el-kimi-k25`; prose only (see notes).
- Vercel staging-to-shipping factory mention — prose; `co-vercel` **[registry]** not edged.
- Notion's "managed agent capability" (launched day-of) as an Element — kept as prose in `sig-notion-software-factory`; see note 3.
- The stale published benchmark slide and "Philip at BE 10" attribution — unresolvable (see notes).

## Review notes

1. **Caption garbles:** "Kimmy 26" → read as Kimi K2.6 (NOT coined; seed `el-kimi-k25` is the family's registry node); "52, GPT 52, GLM 52" → read as GPT-5.2 / GLM-5.2 (`el-glm-52` reused **[registry]**; a GPT-5.2 node doesn't exist — registry has `el-gpt-56` — left un-edged); "Philip at BE 10" (source of the gap-gets-covered slide) — unresolved, possibly Philipp Schmid (batch 5), no edge; "Dylan in some analysis" → Dylan Patel / SemiAnalysis, prose; "Verscell" → Vercel; "Rejieve" → internal Notion engineer, unresolved; "Anna Winter" → Anna Wintour; "Tay" → internal agent name, unresolved.
2. **Pattern candidates (NOT coined, no edges):** `sig-notion-software-factory` held pattern-less for rehoming onto `pat-ai-native-org` if coined at review — it's another strong data point (production software factory coordinating most internal polish work, plus the 88%-stuck framing). Weak add to `pat-agent-economy`: token economics as viability/structural barrier ("cost as the reason systems don't happen at scale") echoes batch-8's cost-as-SLA evidence.
3. Notion's "managed agent capability" possibly relates to seed `el-anthropic-managed-agents` (Claude agents managed from inside Notion docs) — check at seeding before coining anything.
4. `sig-openweight-negotiation-leverage → pat-sovereign-ai` reads open weights as control/leverage evidence. Note batch-8's counter-edge (`sig-2026-openweight-augments-closed` ContradictsPattern → pat-sovereign-ai): Sachs is actually closer to the augments-closed reading (leverage, not replacement) — downgrade to pattern-less if you want sovereign-ai reserved for self-hosting/national-control claims.
5. Notion "AI Switzerland" positioning and the 75% auto-model figure are self-reported vendor claims from a keynote — treat marketing-adjacent numbers accordingly.
