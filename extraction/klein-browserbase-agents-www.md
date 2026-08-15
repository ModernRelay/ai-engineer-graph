# SPIKE extraction — "Bringing agents onto the world wide web" (Paul Klein IV, Browserbase) — FOR REVIEW

Source transcript: `transcripts/klein-browserbase-agents-www.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/GqoNrUz8hEU — AI Engineer World's Fair, **Computer Use (CUA) track**, published 2026-08-14.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-14 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the track's state-of-the-category talk, opening on a half-empty room ("have we all given up at this point?") and arguing the despair is misplaced: the models stopped being the bottleneck, and what remains is a **capabilities overhang** closed by engineering — harness, infrastructure, and a web made agent-legible (accessibility, authentication, trust). Ends on the vendor's answer (Browserbase agents, launched the day before). Caption garbles: "Open Cloud" → **OpenClaw**, "Cloud code / Cloud in Chrome" → **Claude Code / Claude in Chrome**, "COA" → **CUA**, "Brokman" → **Brockman**, "web bot off" → **Web Bot Auth**, "OffMD" → ⚠ likely **auth.md** (WorkOS, see review note 4), "Docus says" → ⚠ unresolved attribution, "browser.sh" → **Browse.sh**, "bottom neck" → bottleneck.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-klein-agents-www` | Bringing agents onto the world wide web (Paul Klein IV, Browserbase — AI Engineer World's Fair) | youtube | https://youtu.be/GqoNrUz8hEU |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-paul-klein`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-paul-klein` | Paul Klein IV (founder, Browserbase; career started in web automation, "maintaining these scripts every single day") | `AffiliatedWithCompany → co-browserbase` |

Referenced without coining: Andrej Karpathy (the November-2023 LLM-OS tweet — code interpreter, multimodal input, browser, subagents — "if you're ever wondering what to build next, just go look at Karpathy's old talks"), Greg Brockman (the "whenever I don't use Codex, I ask myself why" overhang tweet).

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-browserbase` | Browserbase | developer | Browser infrastructure for agents — "millions and millions of sessions every single month"; ships **Browse.sh** (published skills for websites), **AutoBrowse** (self-improving browsing loops), and **Browserbase agents** (batteries-included browsing agent + harness, launched the day before the talk). Thesis: "solving computer use accelerates the diffusion of AI to the real economy" |

Reused **[registry]**, edge-only: `co-cursor` **[b3]** ("Cursor actually started this — harness engineering on top of the original LLMs"), `co-google` **[b2]** (Chrome shipping WebMCP). Referenced without coining: Factory (the harness-beats-same-model chart — an `el-` reference exists via prose only), WorkOS (auth.md).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-cua-capability-overhang` | The computer-use capability overhang | concept | harness | The central claim: "there is a massive capabilities overhang in computer use. The models are good enough, but we haven't done the engineering work to solve it." A year ago the models genuinely were the bottleneck (long-horizon tasks); RL-environment investment moved from coding to computer use in the last six months and the evals show it. Task-completion rates in coding far exceed CUA "because we haven't pushed the models far enough and given them the right tools" — and non-coding is called the bigger opportunity. "The wrong answer is to sit around and wait for the models to get better" |
| `el-browser-agent-triad` | Multimodal, harness-engineered, reliable infra | concept | harness | What working browser agents share. **Multimodal**: model-mix per page difficulty, and code alongside clicking — "the most reliable browser agents in production are often writing code alongside using the browser," e.g. intercepting network requests and replaying them by script (Claude Code emitting a script beats Claude-in-Chrome for repeatable tasks — context-efficient). **Harness-engineered**: memory and skills so nothing is discovered twice — Browse.sh publishes per-website skills an agent reads before visiting; token-optimized context, not whole-page dumps. **Reliable infrastructure**: environments that render identically every run — "if your infra renders mobile one time and desktop the next, you get inconsistent results"; the Mac-mini-under-the-desk OpenClaw setup named as the anti-pattern ("I've yet to see a SOC 2 compliant Mac mini setup at scale") |
| `el-agent-legible-web` | The agent-legible web | concept | infra | The other half of the problem: "we have to improve the web itself… be evangelists that you want agents coming to your website." Three fronts: **accessibility** — best-in-class agents consume the accessibility tree and ARIA tags, not raw DOM; **Chrome shipped WebMCP**, letting sites publish in-page MCP servers agents can call without pre-installation ("submit the registration form" as a blessed, context-efficient tool call); llms.txt / skills.md / agents.md published alongside sites. **Authentication** — passwords, service accounts, and WorkOS's auth.md (agent-first signup/login discovery); "agents are going to be using your software whether you like it or not — best to let them use it securely." **Trust** — CAPTCHAs don't work against agents; good agents need distinguishing from bad bots (Web Bot Auth), and "there needs to be a Verisign moment for web agents — who is the certificate issuer? Nobody's done that yet" |
| `el-browserbase-agents` | Browserbase agents | product | harness | The vendor answer: prompt in, and the platform stands up "the harness, the runtime, the sandbox, the code execution, the fetch, the search tools, and the models." Sessions feed observability (screen recordings, logs, network activity) back into the agent — "every agent you run should get better every single time" — with an optimization pass that reviews completed runs. Pitched as a subagent for larger agentic systems: "you should be focusing your time on solving customer problems, not rebuilding best-in-class browser agents" |
| `el-agent-identity-broker` | Agent identity brokering | concept | security | The infrastructure role the talk argues must exist: someone to "negotiate with the anti-bot providers of the world and say: we are the platform for trusted agents, and we can broker access for your agents as you use the web." Model-agnostic infrastructure plus brokered identity plus observability as the platform requirements for production browsing |

Element edges: all five `IdentifiedInArtifact → ia-aie-klein-agents-www`.
`el-browserbase-agents` `DevelopedByCompany → co-browserbase`, `UsesElement → el-browser-agent-triad`;
`el-browser-agent-triad` `UsesElement → el-cua-capability-overhang`;
`el-agent-legible-web` `UsesElement → el-mcp` **[registry, seed]**, `el-agents-md` **[registry, b6]**;
`el-agent-identity-broker` `EnablesElement → el-agent-legible-web`;
`el-cua-capability-overhang` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**.

Reused elements (no new nodes): `el-mcp` **[seed]**, `el-agents-md` **[b6]**, `el-claude-code` **[b5]**, `el-openclaw` **[registry]**, `el-agent-skills` **[batch1]** (Browse.sh is per-website skills — a genuinely new deployment surface for that node).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-klein-agents-www`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-browserbase`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-cua-overhang-is-engineering-debt` | harness | An infrastructure vendor's diagnosis of why browser agents stalled while coding agents soared: not models — "anything I believed 6 months ago I have to revisit every week" — but missing harness and tools. RL-environment investment shifted from coding to computer use in the last six months and capability followed; the gap between coding and CUA task completion is engineering debt, not model limitation. "Solving overhang is an engineering problem… the wrong answer is to sit around and wait for the models" | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-cua-capability-overhang` |
| `sig-domain-harness-beats-raw-model` | harness | The harness-engineering case restated for browsing, with the coding evidence: Factory outperforming Claude Code *on the same model* with a domain-optimized harness; "Cursor actually started this." The claim is scoped carefully — "it's not clear yet if custom harnesses will beat out durably RL'd models, but we're not debating that today; adding a harness on a model improves results" — and democratized: "you don't have to be a lab to build a good harness" | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-browser-agent-triad` |
| `sig-production-browsing-mixes-code-and-clicks` | harness | The production observation: reliable browser agents write code alongside clicking — intercepting network requests and generating replay scripts, using CLIs like Playwright with skills and memory so nothing is discovered twice, and compressing page context rather than dumping DOMs. Consistency of the rendering environment is the base layer ("same inputs and outputs, same page layout, every run"). A both/and answer to the pixels-versus-code question the track's thesis talk poses | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-browser-agent-triad`; `el-agent-skills` **[registry, batch1]** |
| `sig-web-must-become-agent-legible` | infra | The web-side shift, with named mechanisms landing now: Chrome shipping **WebMCP** (in-page MCP servers, no pre-install), accessibility trees and ARIA as the consumed surface, llms.txt/skills.md/agents.md alongside sites, WorkOS's auth.md for agent-first signup, and Web Bot Auth for declaring agent identity. Plus the unsolved half: secure delegated login, human-in-the-loop approval for the enterprise, and a missing "Verisign moment" — no certificate issuer for trusted agents exists. "Agents are going to be using your software whether you like it or not" | — **HELD PATTERN-LESS** (`pat-agent-economy` ledger — the infrastructure-side leg; see review note 1) | `OnElement → el-agent-legible-web`, `el-agent-identity-broker` |
| `sig-real-economy-runs-on-php-and-clicks` | infra | The market claim under the company: "the real economy is the logistics company in Singapore, the bank in South Africa, the lumber factory in Mexico — built on PHP websites with forms and human beings clicking buttons every single day." Computer use as the diffusion mechanism carrying AI past the San Francisco bubble into that economy; the plethora of small-company use cases reported as the surprise of building the business. Convergent with the Batra talk's long-tail argument, from the infrastructure seller's side | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-cua-capability-overhang`, `el-browserbase-agents` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-overhang-is-a-vendor-opportunity-map` | "Capabilities overhang" is doing precise work in this talk: it names the gap between what models can already do and what deployed systems extract, and locates the profit in closing it with engineering rather than waiting. That framing explains the whole batch's vendor lineup — harness sellers, infrastructure sellers, identity brokers all monetize the same overhang — and it makes a testable prediction: if the overhang is real, CUA deployment should inflect *without* a frontier-model release, purely on tooling. The half-empty room is the market mispricing that bet | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-cua-capability-overhang`, `el-browser-agent-triad` |
| `ins-trust-not-capability-gates-the-agent-web` | Of the three web-side fronts, accessibility and authentication have shipping mechanisms (WebMCP, auth.md) while trust has none — no issuer, no registry, no delineation between good agents and bad bots beyond CAPTCHAs that no longer work. That makes trust the binding constraint on the agent web: capability grows in the models, legibility grows in the standards, but until someone becomes the certificate authority for agents, every site's rational default is to block. The "Verisign moment" framing predicts the next infrastructure company, and notably the speaker positions his own as broker rather than issuer | `HighlightsPattern → pat-new-cyber-threats` **[registry]** | `ReliesOnElement → el-agent-identity-broker`, `el-agent-legible-web` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-klein-agents-www`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-production-browser-agents` | Build browser agents as harness + infra, not model wait-states | Stop waiting for better models — audit the overhang instead, comparing what frontier models achieve in your harness against baseline, and invest where the gap is engineering; mix modalities per task — cheaper models for simple pages, code generation for repeatable flows (intercept and replay network requests rather than re-clicking), CLIs like Playwright given skills and context; give agents **memory and per-website skills** so nothing is discovered twice, and compress page context rather than dumping raw DOM into the model; run on **consistent rendering infrastructure** — identical layout, viewport and environment every run — because inconsistent rendering produces inconsistent agents, and a Mac mini under a desk is not production; consume the accessibility tree and ARIA tags, and adopt WebMCP where sites publish it; plan authentication deliberately (scoped service accounts, agent-first signup flows, human-in-the-loop approval for sensitive actions) rather than handing agents passwords; feed observability — recordings, logs, network — back into the agent every run so it improves; and if browsing is not your core product, use a purpose-built browsing agent as a subagent instead of rebuilding one | `ReferencesElement → el-browser-agent-triad`, `el-agent-legible-web`, `el-browserbase-agents` |

## Dropped

- **The sleepy-room opener and closing attendance prediction** ("1 year from now this room is going to be overfilled") — framing; the substantive overhang claim is carried.
- **The Karpathy-LLM-OS retrospective** — folded into the Experts note.
- **The demo walkthrough** — product mechanics carried by `el-browserbase-agents`.

## Review notes

1. **⚑ Paired with the Batra talk deliberately.** Same track, same day, same conclusion (agents become the web's users), opposite emphasis: Batra says the *model* generalizes and scaffolds don't; Klein says the *models are already good enough* and scaffolds are exactly what's missing. Both signals feeding `pat-agent-economy` are held pattern-less; the harness disagreement is recorded as edges on the coined patterns (`sig-scaffolds-dont-generalize-pixels-do` contra vs `sig-domain-harness-beats-raw-model` pro). This is the b15 FINDING 1 claim-1/claim-2 split reproduced inside one conference track — flag for the re-scoping review.
2. **`sig-real-economy-runs-on-php-and-clicks` homed on `pat-saaspocalypse`** on the workflow-displacement reading (agents replacing human click-work across the real economy). Drop-option: rehome to the `pat-agent-economy` ledger on coin if review reads it as adoption rather than displacement.
3. **⚠ Verify before seeding:** the Factory-vs-Claude-Code chart (referenced, not quantified), Chrome's WebMCP ship status, "millions of sessions per month," and the launched-yesterday date for Browserbase agents.
4. **⚠ Garbles:** "OffMD" normalized to **auth.md** (WorkOS's announced agent-auth discovery file) with medium confidence; "Docus says if the models were good enough diffusion would just happen" — attribution unrecoverable, kept out of all nodes.
