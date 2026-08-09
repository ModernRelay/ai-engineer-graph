# SPIKE extraction — "Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer" (Emil Eifrem, Neo4j) — FOR REVIEW

Source transcript: `transcripts/eifrem-neo4j-ontology-semantic-layer.txt` (auto-captions — quotes are paraphrases, not verbatim; "Neo Forj" = Neo4j).
Video: https://youtu.be/VGN22pPpb-8 — AI Engineer World's Fair keynote, published 2026-07-22.
`stagingTimestamp` for the artifact and all signals: 2026-07-22 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node. `co-neo4j` is defined in `blumenfeld-neo4j-lakehouse-context-shapes.md` (this batch).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-eifrem-thin-agents-substrate` | Thinner Agents on a Smarter Substrate: The Ontology-based Semantic Layer (Emil Eifrem, Neo4j — AI Engineer World's Fair) | youtube | https://youtu.be/VGN22pPpb-8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-emil-eifrem`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-emil-eifrem` | Emil Eifrem (co-founder & CEO, Neo4j) | `AffiliatedWithCompany → co-neo4j` [defined in blumenfeld file] |

## Companies (0 new)

- `co-neo4j` — reused [defined in blumenfeld file].

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-ontology-semantic-layer` | Ontology-based semantic layer | concept | context | Three-pillar shared substrate for enterprise agents: (1) **business-facing ontology** — the org's key concepts and relations (customers, accounts, transactions; business processes for process-guided agents) expressed in terms every human in the company uses ("customer has first name", not `f_name`); (2) **technical ontology** — metadata of every data source and asset in the estate (the 14 Oracle DBs, Snowflake, Databricks, S3, schemas) plus the explicit mapping from business concept to system of record and column; (3) **execution traces** left by agents at runtime. One governed place mapping business intent to data sources — discovery, trust, DRY, and learning solved in the substrate instead of per agent |
| `el-agent-execution-traces` | Agent execution traces | concept | context | The runtime pillar: as agents walk the semantic-layer graph they record where they were, what they tried, their context, the outcome — rolled into a score that biases future data-source selection ("DMV lookup worked, prefer it in this context next time"). Trust established bottom-up from what actually worked, complementing top-down human curation; enables self-learning and cross-agent learning |

Element edges: both `IdentifiedInArtifact → ia-aie-eifrem-thin-agents-substrate`; `el-ontology-semantic-layer` `UsesElement → el-semantic-layer` **[registry]**, `UsesElement → el-agent-execution-traces`, `EnablesPattern → pat-context-graphs` **[registry]**; `el-agent-execution-traces` `EnablesPattern → pat-context-graphs` **[registry]**.

## Signals (4 new)

All: domain `context`, `SpottedInArtifact → ia-aie-eifrem-thin-agents-substrate`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-thin-agents-fortune20-pattern` | Neo4j CEO: from at-scale deployments over the last 6–9 months at a Fortune 20 global bank, a massive Bay Area tech-platform company, and a leading fintech, the emerging pattern is "thin agents on a smarter shared substrate" — per-agent manual data-source wiring means rediscovering sources from scratch, unverifiable trust/duplication, DRY violations cascading on every change, and zero cross-agent learning because the wiring lives in code and prompts | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-neo4j`; `OnElement → el-ontology-semantic-layer` |
| `sig-markdown-files-not-the-solution` | Verdict on the skills/markdown-file approach to agent-data grounding, from "a ton of teams" tried at scale: part of the solution, not the solution; quotes swyx a week earlier on the Latent Space podcast — "you've got to learn your databases; you cannot vibe-code with just markdown files" | `FormsPattern → pat-context-graphs` | `OnElement → el-agent-skills` **[registry]** |
| `sig-execution-traces-cross-agent-learning` | Agents leave scored execution traces in the shared substrate so tomorrow's invocation — and other teams' agents — choose data sources by what actually worked; "my agent that wakes up tomorrow is slightly smarter than it was today", across agents, not just per agent | `FormsPattern → pat-context-graphs` | `OnElement → el-agent-execution-traces` |
| `sig-ontology-goes-mainstream` | "Ontology" has moved from decades of academic niche to hype term — "probably thanks to Palantir" plus the rise of AI — and vendors are fighting the complexity creep: Neo4j's framing strips it to the key concepts of your organization and how they relate, expressed in human terms | `FormsPattern → pat-context-graphs` | `RelevantCompany → co-neo4j` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-thin-agents-smarter-substrate` | The intelligence about where data lives, whether it can be trusted, and what worked belongs in a shared governed substrate, not in each agent's code and prompts. Agents get thinner as the substrate gets smarter — so the Nth agent stops costing a re-engineering effort and change cascades once instead of per agent | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-ontology-semantic-layer` |
| `ins-trust-top-down-and-bottom-up` | Data-source trust needs both directions at once: top-down human curation (an administrator asserting what is authoritative in the ontology) and bottom-up execution traces (what empirically worked in practice). Either alone is incomplete; the combination is the governance win | `HighlightsPattern → pat-context-graphs` | `ReliesOnElement → el-agent-execution-traces` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-eifrem-thin-agents-substrate`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-three-pillar-semantic-layer` | Build the agent substrate as three pillars | Define the business-facing ontology in the vocabulary humans in the org actually use; catalogue every data source/schema as a technical ontology; maintain the explicit mapping (business concept → system of record → physical column); encode business processes in the ontology for process-guided agents; instrument agents to write execution traces (location, attempt, context, outcome → score) and route future source selection by those scores | `ReferencesElement → el-ontology-semantic-layer`, `ReferencesElement → el-agent-execution-traces` |

## Dropped

- The bank-account-opening agent walkthrough (DMV registry vs passport-verification source resolution) — illustration, folded into the element briefs.
- Graph-track namedrops (Gates Foundation, Monday.com, JP Morgan Chase, Berkeley, New York Times) and the Neo4j startup-program / booth pitch — marketing.
- "Three key ways to construct the technical ontology" — teased, explicitly not covered in the talk; nothing to extract.

## Review notes

1. Resolved garbles: "Switz" = swyx (Latent Space podcast); "Palunteer" = Palantir. Quotes are paraphrases.
2. Zero new patterns: this keynote is the most direct professional statement of `pat-context-graphs` in the batch — the thin-agents/smart-substrate framing maps onto the seed thesis rather than beside it.
3. `el-agent-execution-traces` is added evidence for the uncoined batch-9 candidate "persistent agent memory as a first-class stack layer" (shared, scored agent memory living in the substrate rather than in the agent) — noted only, no edge, per instructions.
4. Deployment evidence in `sig-thin-agents-fortune20-pattern` is vendor testimony with customers unnamed by the speaker (Fortune 20 bank etc.); treat as practitioner-class, not verifiable fact.
5. `el-ontology-semantic-layer` deliberately reuses registry `el-semantic-layer` via `UsesElement` (same precedent as `el-source-of-truth-hierarchy`, batch 2) rather than duplicating it; it also overlaps Blumenfeld's `el-neocarta` (the productized technical-ontology pillar) — no cross-file element edge added, flag if you want `el-neocarta UsesElement el-ontology-semantic-layer` at seeding.
