# SPIKE extraction — "The Agentic Web and the Bazaar Era of AI" (Ramesh Raskar, MIT Media Lab) — FOR REVIEW

Source transcript: `transcripts/raskar-mit-agentic-web-bazaar.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/sum9DgexFRQ — AI Engineer World's Fair, published 2026-07-12.
`stagingTimestamp` for the artifact and all signals: 2026-07-12 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-raskar-agentic-web` | The Agentic Web and the Bazaar Era of AI (Ramesh Raskar, MIT Media Lab — AI Engineer World's Fair) | youtube | https://youtu.be/sum9DgexFRQ |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-ramesh-raskar`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-ramesh-raskar` | Ramesh Raskar (professor, MIT Media Lab; director of Project Nanda — open infrastructure for an internet of AI agents) | `AffiliatedWithCompany → co-mit-media-lab` |

Co-presenter "Maria" (core contributor, Project Nanda) delivers roughly half the talk but no surname is ever given in captions — **not coined**; see Review notes.

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-mit-media-lab` | MIT Media Lab | research | home of Project Nanda ("Networked AI Agents in a Decentralized Architecture"), the open research effort behind the Nanda index and Nanda Town |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-nanda-index` | Nanda index | technology | infra | Discovery layer for the agentic web ("DNS for agents, plus more"): maps an agent identity (e.g. agent@domain) to an agent card; signed "agent facts" records state who built the agent, what it can do/touch, and how to reach it; a message-box layer handles auth/spam/buffering; resolution is adaptive — endpoints returned vary by requester, location, and permissions |
| `el-nanda-town` | Nanda Town | product | infra | Open-source discrete-event simulation sandbox for the agentic web from Project Nanda; models the whole agent economy across 12 layers (transport, communication, identity, registry, auth, trust, payments, coordination, negotiation, memory, privacy, data effects); scenario-in-YAML; tier 1 scripted agents, tier 2 real AI models; runs on a laptop |
| `el-maritime` | Maritime | product | infra | Agent-hosting platform positioned as a cheap cloud default for running OpenClaw and other agents; sleep/wake architecture so idle agents don't burn compute — targets per-agent cost at fleet scale |

Element edges: all three `IdentifiedInArtifact → ia-aie-raskar-agentic-web`; `el-nanda-town` `UsesElement → el-nanda-index` (the registry layer inside the sim); `el-maritime` `EnablesElement → el-openclaw` **[registry]**.

**[registry]** reused: `el-openclaw` (used twice: as the talk's example of "a model that uses tools in a loop" packaged as a self-hosted agent gateway, and as the workload Maritime hosts).

## Signals (5 new)

All: domain `infra`, `SpottedInArtifact → ia-aie-raskar-agentic-web`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-agent-walled-gardens-aol-era` | MIT's diagnosis of the present: agent builders are forced inside walled gardens — closed platforms, proprietary agent stores, orchestration that only talks to itself — explicitly analogized to the late-'90s AOL era, with an open-web-style transition predicted; Nanda ships the open alternative (index, registries, protocol) | — (see Review notes: `pat-agent-economy` candidate) | `RelevantCompany → co-mit-media-lab` |
| `sig-trillions-of-agents-strain-dns` | Premise driving the build-out: the internet will eventually host trillions of autonomous agents that negotiate, delegate, and migrate between hosts in milliseconds — a load the human web's identity/discovery stack (DNS included) was never designed for | — (same candidate) | — |
| `sig-nanda-index-live` | The Nanda index is shipped and onboarding now: identity → signed agent-facts card → message box, with adaptive resolution; onboarding tiers for enterprises (own catalog/domain), existing websites (DNS records), and individuals (hosted agent URL via host39.org) | — | `OnElement → el-nanda-index` |
| `sig-self-hosted-agents-as-control` | Because real agents need access to real tools/apps, the talk argues who controls the agent, where it runs, and what you can see now matter — open-source self-hosted agents (OpenClaw the named example) framed as how people keep control of their own agents | `FormsPattern → pat-sovereign-ai` **[registry]** | `OnElement → el-openclaw` |
| `sig-nanda-town-experiments` | Nanda Town is already running real coordination experiments — marketplace price negotiation, auctions, agent voting/ballot counting, consensus, supply chains — to find where agentic-web protocols break before they become load-bearing on the real internet | — | `OnElement → el-nanda-town` |

Per-agent hosting economics (idle agents burning compute; Maritime's sleep/wake answer) kept as prose in the Maritime element rather than a sixth signal — it is a product pitch, not an observed change.

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-agents-need-dns-plus` | Agents need more than DNS-style name→address resolution: capabilities, rules, trust, and adaptive routing must resolve too, and if that layer is owned by a single platform the walled garden wins by default — open, portable identity/discovery is the load-bearing piece of an open agentic web | `HighlightsPattern → pat-sovereign-ai` | `ReliesOnElement → el-nanda-index` |
| `ins-simulate-before-load-bearing` | You cannot assume agent-web protocols hold up under load — you have to run them and watch where they break; simulation (a full modeled agent economy) is how an open agent web gets verified before real commerce depends on it | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-nanda-town` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-raskar-agentic-web`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-publish-agent-to-open-web` | Put your own agent on the open agentic web | Fill out the agent-facts form (host39.org for individuals/small businesses) → get an agent card → publish to the Nanda index; enterprises: run your own catalog and register your gateway from your own domain; existing websites: attach agents to domains via DNS records; ensure the agent stays reachable — self-host for control or use cloud/agent-hosting (sleep/wake platforms cut idle cost) | `ReferencesElement → el-nanda-index`, `ReferencesElement → el-maritime` |

## Dropped

- "Agent = a model that uses tools in a loop" definition — pedagogical framing, standard by now; no Element.
- Agent-facts record / message box / agent card as separate Elements — folded into `el-nanda-index` prose (they are its components).
- AWS mention (generic "enterprise-ready cloud") — no edge to `co-aws`.
- The three-layer "discovery / commerce / bazaar" framing — rhetorical structure of the talk; captured across signals rather than as a concept Element.

## Review notes

1. **`pat-agent-economy` resonance (do not coin unilaterally — central decision):** this talk is the strongest evidence yet for the uncoined candidate from `povilionis-alithea-agents-need-receipts.md` (batch 2). `sig-agent-walled-gardens-aol-era` and `sig-trillions-of-agents-strain-dns` — plus Nanda's explicit commerce layer (portable identity, trust, payments, negotiation; Town's marketplace/auction experiments) — describe agents discovering, paying, and transacting with each other across org boundaries. That is two independent talks (Povilionis's Froglet transaction protocol `el-froglet` **[registry]**, now Nanda). Per the recurrence rule this may be at coin threshold; the two pattern-less signals above are the ones to rehome onto `FormsPattern → pat-agent-economy` if coined.
2. **Caption garbles:** "Agoric platform/economy/web" (multiple occurrences) is almost certainly "agentic" mis-captioned — treated as such throughout. "host39.org" and "DNS AID" are suspect (possibly "host39"/"DNS TXT" or a project name garble); "Project Nondo" = Project Nanda; "Open Clo" = OpenClaw. Verify host39.org before seeding a URL anywhere.
3. **Co-presenter "Maria":** delivers the index/town half of the talk; surname never given. Not coined to avoid a half-identified Expert node. If reviewers can resolve her from the video description, add `exp-maria-<surname>` + `ContributedByExpert`.
4. `ins-simulate-before-load-bearing` → `pat-verification-gap` is a mild stretch (the pattern was coined for code/agent-output verification; here it's protocol/infrastructure verification). Cut the edge if you read the pattern narrowly.
5. Maritime is presented product-first; it is unclear whether "Maritime" is also a company. Element only, no `DevelopedByCompany` edge.
