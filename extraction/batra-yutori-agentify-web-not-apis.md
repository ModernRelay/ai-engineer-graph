# SPIKE extraction — "Computer-use models will agentify the web, not APIs" (Dhruv Batra, Yutori) — FOR REVIEW

Source transcript: `transcripts/batra-yutori-agentify-web-not-apis.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/Ki980nV0__0 — AI Engineer World's Fair, **Computer Use (CUA) track**, published 2026-08-14.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-14 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the track's thesis talk, built as a single sustained argument. Agents will drive most web actions (agreed); the web will be "agentified" (agreed); *via APIs and protocols* (rejected as "delusional"). The long tail of the web — restaurant menus as JPEG galleries, school-district procurement behind FOIA scans — will never publish MCP servers, and even reading HTML fails because **the browser is a rendering engine and pixels are the source of truth**. Conclusion: general pixels-in models are the bitter lesson for web agents, and the web gets agentified by piling a layer of button-clicking browsers on top of the mess until "at some point you will say: yeah, that's an API." ⚠ Heavy caption garbles: "Dadra" → **Batra**, **"identified/identify the web" → "API-fied / agentify the web"** (systematic, load-bearing), "Palma de Mayorca" → Mallorca, "online mind to web" → **Online-Mind2Web**, "navigator N 1.5" → **Navigator N1.5**, "GBD 5.5" → GPT-5.5, "paralyze" → parallelize, "multi- aent" → multi-agent.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-batra-agentify-web` | Computer-use models will agentify the web, not APIs (Dhruv Batra, Yutori — AI Engineer World's Fair) | youtube | https://youtu.be/Ki980nV0__0 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-dhruv-batra`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-dhruv-batra` | Dhruv Batra (Yutori; AI-research background — "people coming from an AI background like me didn't always understand this" about browser internals) | `AffiliatedWithCompany → co-yutori` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-yutori` | Yutori | developer | Builds **Navigator**, a computer-use model (first version November 2025: screenshots in, button clicks and scrolls out; N1.5 current). Positioning is model-first: small-footprint CUA models competitive with frontier models at a fraction of latency and cost |

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-long-tail-web` | The long tail of the web | concept | infra | The empirical core: ~200M active websites (~1B total), and infrastructure that "changes very slowly — there are still places faxing each other." The head of the distribution may publish APIs; the long tail never will. Worked exhibits: restaurant menus ranging from plain German text (easy) to a menu-button-opens-PDF (medium) to **JPEGs of PDF pages embedded in a gallery** (hard); school-district procurement ranging from a portal to scanned PDFs to a district that answers FOIA requests by scanning your emailed request onto a Google Drive. "These are the people you're telling me will give you an MCP server. The amount of delusion here is off the chart" |
| `el-pixels-are-source-of-truth` | Pixels as the source of truth | concept | harness | Why coding agents reading HTML also fail: the browser is a **rendering engine** — "think of it as a game engine." An NBA score is absent from the initially-loaded HTML (fetched asynchronously); a product's sold-out state exists nowhere as text — a quantity JSON plus a rendering script grays the option out. "The information you are seeing on screen is not written somewhere as pure text. It is calculated. It is rendered." The web was built for human eyes, so machines need vision — "the bitter lesson for web agents": scaffolds around existing websites don't generalize to the long tail; the most general solution is pixels in |
| `el-yutori-navigator` | Navigator (Yutori) | product | harness | Yutori's computer-use model. V1 (Nov 2025) acted purely human — screenshot in, clicks/scrolls out. The next version **writes JavaScript on demand** (a Chrome extension filling multiple form fields via a generated function): "click buttons when you have to, write code when you have to, and look at the result through pixels, because that is the source of truth" — the screenshot acting as a built-in verification system. N1.5 reported at **97% human eval on Online-Mind2Web** (8/300 trajectories incorrect — "retire the benchmark, build something harder"), competitive with Opus 4.7/GPT-5.5 on browser-use benchmarks but at far lower latency (smaller footprint) and **~$0.80 per 20–30-step task versus ~$2.30** (⚠ figures caption-sourced, see review note 3). Orchestratable: one orchestrator launching parallel Navigators in cloud sandboxes, "superhuman because no human can parallelize that many instances" |
| `el-agentification-by-accretion` | Agentification by accretion | concept | infra | The closing prediction of *how* the web actually gets agentified: not by rebuilding 30 years of human-built infrastructure in "two, five, ten years" (a "fantasy") but by extrapolating current trends — accuracies rising, benchmarks falling, latencies and costs dropping — until "we just pile on another layer of mess on top of the mess that the web is": hundreds of browsers clicking buttons like humans behind a task endpoint, returning structured results for under a penny in sometimes <100ms. "At some point you will say: yeah, that's an API. Why do I care?" |
| `el-cua-progress-rate` | Computer-use progress rate | concept | training | Against the "has CUA progress stalled?" perception: "that's not the reality I'm seeing and not the reality the numbers back up." Online-Mind2Web (human-evaluated, 30–50 interaction steps) is saturated by release-time plotting; the next step is larger tasks. Offered explicitly as benchmark-with-caveats ("no benchmark is perfect — the point isn't that this is the right solution") |

Element edges: all five `IdentifiedInArtifact → ia-aie-batra-agentify-web`.
`el-yutori-navigator` `DevelopedByCompany → co-yutori`, `UsesElement → el-pixels-are-source-of-truth`;
`el-agentification-by-accretion` `UsesElement → el-long-tail-web`, `el-yutori-navigator`;
`el-pixels-are-source-of-truth` `EnablesElement → el-yutori-navigator`;
`el-long-tail-web` `EnablesElement → el-pixels-are-source-of-truth`.

Reused elements (no new nodes): `el-mcp` **[seed]** — the protocol whose universalization the talk denies ("initially supposed to be MCP servers, then WebMCP, and for payments there are 20 different competing protocols"); edge via signals. `el-code-mode` **[b6]** adjacency (write-code-when-you-have-to) kept in prose.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-batra-agentify-web`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-yutori`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-long-tail-will-never-publish-apis` | infra | The negative claim, argued from exhibits rather than theory: the institutions of the long-tail web — restaurants whose menus are JPEG galleries, school districts that answer FOIA by scanning emails onto Google Drive — will not publish APIs or MCP servers on any relevant timescale, because "you're not going to get unfettered access to these institutions and these institutions change very slowly." Aggregators cover the head (flights deserve tool calls, not button clicks — "I find this example bizarre"); the tail is unreachable by protocol. A direct dissent from the protocol-proliferation thread (MCP → WebMCP → 20 payment protocols) running through the corpus since batch 8 | — **HELD PATTERN-LESS** (`pat-agent-economy` ledger, counter-flavoured — see review note 1) | `OnElement → el-long-tail-web`, `el-mcp` **[registry, seed]** |
| `sig-html-is-not-the-page` | harness | The technical argument that eliminates the middle position ("fine, no APIs, but coding agents can read the HTML"): modern pages load empty placeholders and fetch content asynchronously; visible states like sold-out exist only as rendered consequences of JSON quantities plus rendering scripts. The browser is a rendering engine — asking to read the source and predict the pixels "is asking for an exact inversion of that process." Machines therefore need **vision**, because the web's consumers were human eyes and pixels are the ground truth | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-pixels-are-source-of-truth` |
| `sig-scaffolds-dont-generalize-pixels-do` | training | The bitter-lesson claim for web agents: "the more you end up writing scaffolds around existing websites, the less it generalizes to the long tail. The thing that generalizes is what the web was designed for — the most general solution, just pixels in." Backed by Navigator's arc: pure-human V1, then a version that also writes JavaScript on demand *with the screenshot as verifier*. Capability moves into the model; the scaffold is the part that doesn't transfer | `ContradictsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-yutori-navigator`, `el-pixels-are-source-of-truth` |
| `sig-cua-cost-collapse` | inference | Against "CUA agents are slow and expensive": a small-footprint CUA model matches Opus 4.7/GPT-5.5 accuracy on browser-use benchmarks (differences "within statistical noise" — the speaker declines to claim the accuracy win) while charging **~$0.80 per task versus ~$2.30** on 20–30-step tasks, with much lower per-step latency. Cost and latency, not capability, presented as the axis where CUA is being won | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-yutori-navigator`, `el-cua-progress-rate` |
| `sig-web-agentified-by-browser-layer` | infra | The synthesis prediction: the web gets its "API" not from rebuilt infrastructure but from an accreted layer of button-clicking browsers — task in, hundreds of parallel human-mimicking browsers behind the scenes, structured result out, sub-penny, sometimes sub-100ms — until the distinction from an API dissolves. Explicitly framed as "in some sense depressing, but true." **HELD PATTERN-LESS** — with the Klein, Gallon and Primor talks in this batch, the machine-web ledger entry for `pat-agent-economy` (see registry § Batch-20) | `FormsPattern → pat-agent-economy` (coined 2026-08-16) | `OnElement → el-agentification-by-accretion`, `el-long-tail-web` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-protocol-adoption-is-gated-by-institutions` | The MCP/WebMCP debate keeps being argued as a technology question when the binding constraint is institutional: an API exists only where an organization can and will maintain one, and the long tail of the web is precisely the set of organizations that cannot. That makes protocol coverage a function of institutional capacity, not spec quality — and means the addressable-by-protocol web is permanently the head of the distribution. Any agent strategy that assumes protocol reach beyond it inherits the delusion, however good the spec | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-long-tail-web` |
| `ins-vision-with-code-as-escape-hatch` | The stable design point Navigator lands on inverts the corpus's usual code-mode argument: code is not the general interface with vision as fallback — **vision is the general interface with code as the optimization**, because the screenshot doubles as a formal verifier ("it knows whether it succeeded"). Write code when the page permits, click when it doesn't, and always confirm through pixels. That combination is what lets one model span easy-mode HTML and JPEG-gallery hard mode without per-site scaffolds | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-yutori-navigator`, `el-pixels-are-source-of-truth` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-batra-agentify-web`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-decide-api-vs-computer-use` | Decide when a task needs computer use rather than an API | Use aggregator APIs and tool calls wherever they exist — clicking buttons on flights.google.com when aggregators return JSON is theater; reserve computer use for the long tail, and audit whether your target sites are head or tail before choosing an architecture (does the institution behind the page have the capacity to ever publish an interface?); do not trust initially-loaded HTML as the page — content arrives asynchronously and visible states are often rendered consequences with no textual representation, so verify through pixels; prefer a model that can both click and write code, using the screenshot as the success check for either path; expect per-site scaffolds not to transfer, and treat rising accuracy plus falling latency and cost — not protocol adoption — as the trend line that decides when to move a workflow onto agents; and parallelize across cloud browser instances for workloads no human could span | `ReferencesElement → el-pixels-are-source-of-truth`, `el-yutori-navigator`, `el-long-tail-web`, `el-agentification-by-accretion` |

## Dropped

- **The "does anybody speak Spanish?" audience moment and the gluten-free walkthrough details** — exhibit colour; the exhibits themselves are in `el-long-tail-web`.
- **The discount-code demo** (validate a code against natural-language constraints by adding to cart and checking the total — "there is no API for this") — a good concrete instance, folded into `el-yutori-navigator`'s brief logic.
- **The e-commerce Osmium-cube specifics** — carried by `el-pixels-are-source-of-truth`.

## Review notes

1. **⚑ This is the batch's thesis talk, and its main weight lands on an UNCOINED ledger.** The claim "the web will be agentified by computer-use models, not APIs" is the strongest counter yet to the protocol-optimist side of `pat-agent-economy` (Raskar's bazaar, b8/b16's MCP-apps thread, Davis's protocol-layer durability) — while simultaneously *supporting* that candidate's core (agents becoming the web's primary actors). Two signals held pattern-less. Batch 20 as a whole is that ledger's biggest single-batch haul; see registry § "Batch-20 additions" before the next coin review.
2. **The `ContradictsPattern → pat-harness-over-model` edge is deliberate** — "scaffolds don't generalize, pixels do" is a capability-side (claim-2) counter in b15 FINDING 1 terms, same family as Kundel's b18 counter, and would resolve under the recommended claim-1 re-scoping. Recorded so the re-scoping decision sees it.
3. **⚠ Verify before seeding:** all numbers are caption-sourced and vendor-stated — 97% human eval on Online-Mind2Web (8/300), $0.80 vs $2.30 per task, ~200M active / ~1B total websites, 15–20k US school districts, model names "Opus 4.7"/"GPT-5.5", "Navigator N1.5", November-2025 V1 date.
4. **Garble note.** The transcript systematically renders "API-fied"/"agentify" as "identified/identify" — the *title's own verb* is garbled throughout. Normalized on the video title's authority.
