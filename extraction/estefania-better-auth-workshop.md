# SPIKE extraction — "Full Workshop: Better Agent Auth" (Paola Estefania, Better Auth) — FOR REVIEW

Source transcript: `transcripts/estefania-better-auth-workshop.txt` (auto-captions — quotes are paraphrases, not verbatim; **heavy garbling**: "Asian"/"Asians"/"nations"/"ancient" → **agent(s)** throughout; "Asian health protocol"/"agent out protocol" → **Agent Auth protocol**; "Asian D"/"Agent D" → the demo MCP/tool name; "Burgett" → co-author Bereket).
Video: https://youtu.be/JvKO40CFq-s · published 2026-07-21 (AI Engineer, World's Fair — full workshop).
`stagingTimestamp` for the artifact and all signals: 2026-07-21 (publish date).
Entities marked **[registry]** already exist — edges link, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-estefania-better-agent-auth` | Better Agent Auth (Paola Estefania, Better Auth — AI Engineer World's Fair full workshop) | youtube | https://youtu.be/JvKO40CFq-s |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-paola-estefania`, `ContributedByExpert → exp-bereket-habtemeskel`.

## Experts (2 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-paola-estefania` | Paola Estefania (Better Auth; presenter — built the workshop with Bereket) | `co-better-auth` |
| `exp-bereket-habtemeskel` | Bereket Habtemeskel (Better Auth; co-author, could not attend — did not present) | `co-better-auth` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-better-auth` | Better Auth | developer | Ships an open-source agent-as-principal auth protocol (agent plugin + SDK/MCP + directory); company name from the talk listing, not cleanly stated in captions (see Review note 2) |

## Elements (2 new; 3 registry reuse)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-auth-protocol` | Agent Auth protocol | framework | security | Open protocol making the agent a first-class principal: each agent gets its own cryptographic identity (private key) permanently bound to a user and a "host," so it can sign/mint its own tokens and every action is attributable, auditable, and independently revocable; solves discovery + authorization + identity + traceability; ships as three layers — an agent plugin (server-side: verify agent, issue grants, enforce constraints), an SDK (mints keys, assigns agent identity, exposes an MCP), and a directory |
| `el-agent-capability-directory` | Agent capability directory | concept | security | A "phone book for agents": a well-known agent-configuration endpoint (OIDC `.well-known` analog) where an agent discovers a service's capabilities; in the interim (before services adopt), built by translating a service's OpenAPI spec into fine-grained capabilities and matching user intent → capability(ies) → tool call; a directory (not a data-carrying proxy — "a proxy uses data, not scalable"), with logs cut down per provider |

| slug | reuse | note |
|---|---|---|
| **[registry]** `el-agent-scoped-authorization` | Agent-scoped authorization | the core model — capabilities (not coarse OAuth scopes), least privilege, per-agent identity bound to the principal (Scalekit/Madabhushi batch 3) |
| **[registry]** `el-oauth-token-exchange` | OAuth 2 Token Exchange | the baseline being extended: "mint a token for the agent, not the user" — switching the principal (Keycard/Maida batch 2) |
| **[registry]** `el-mcp` | Model Context Protocol | the protocol ships as an MCP + SDK; the demo connects the MCP to Claude/Cursor |

Element edges: `el-agent-auth-protocol` `DevelopedByCompany → co-better-auth`; `el-agent-auth-protocol` `UsesElement → el-agent-scoped-authorization` **[registry]**, `UsesElement → el-oauth-token-exchange` **[registry]**, `UsesElement → el-agent-capability-directory`, `UsesElement → el-mcp` **[registry]**; `el-agent-capability-directory` `UsesElement → el-mcp` **[registry]**; `el-agent-auth-protocol` `EnablesPattern → pat-verification-gap` **[registry]**; both new elements `IdentifiedInArtifact → ia-aie-estefania-better-agent-auth`.

## Signals (4 new)

All: domain `security`, `SpottedInArtifact → ia-aie-estefania-better-agent-auth`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-better-auth`.

| slug | name / brief | FormsPattern | OnElement |
|---|---|---|---|
| `sig-agents-use-human-credentials-risk` | Status quo: users hand agents their own credentials (an MCP server + personal tokens), so the agent acts "pretending to be you" with full access — like giving a new hire the CEO's credentials; in the room, most agent users declined to grant agents Gmail/calendar access because the blast radius (misuse, data exposure, no way to revoke without disconnecting everything) is unacceptable | `pat-new-cyber-threats` **[registry]** | `el-agent-scoped-authorization` **[registry]** |
| `sig-agent-as-principal-shift` | Better Auth's core move: reframe the agent from hiding behind the user to a first-class principal — give it *authority* (scoped capabilities), not your credentials; "act for me within these limits," not "pretend to be me"; each agent gets its own private-key identity bound to a user and a host, making every action attributable and revocable | `pat-verification-gap` **[registry]** | `el-agent-auth-protocol`, `el-agent-scoped-authorization` **[registry]** |
| `sig-agent-capability-discovery` | Three problems structure agent auth — discovery (how an agent learns what a service allows), authorization (scope to capabilities, not coarse scopes), identity (who the agent is) — addressed by a well-known agent-config endpoint (OIDC `.well-known` analog) plus, in the interim, a directory that translates a service's OpenAPI spec into capabilities and matches intent → capability → tool call | `pat-verification-gap` **[registry]** | `el-agent-capability-directory` |
| `sig-capabilities-over-scopes` | Argument + live demo: coarse OAuth scopes ("read") are too broad to delegate to a non-deterministic agent; capabilities name specific permitted actions, so you grant per-tool and revoke instantly — an email-reader agent with only read capability must request approval (device / client-initiated back-channel flow) to gain send, and revoking its identity forces a fresh, capability-limited agent | `pat-verification-gap` **[registry]** | `el-agent-scoped-authorization` **[registry]**, `el-oauth-token-exchange` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-authority-not-credentials` | Stop giving agents our credentials; give them authority. The shift is from "pretend to be me" (agent impersonates the user with full access) to "act for me within these limits" (agent is a scoped principal with its own identity) — which is precisely what makes tracing, firing, and revoking an agent possible | `pat-verification-gap` **[registry]** | `el-agent-scoped-authorization` **[registry]** |
| `ins-identity-enables-traceability` | Only per-agent identity makes the full lifecycle work: audit logs (which agent did what, for which user, via which host), the ability to revoke/fire a misbehaving agent, and enterprise policy (per-user or per-host) — none possible when the agent hides behind the user, where the only recourse is disconnecting everything | `pat-verification-gap` **[registry]** | `el-agent-auth-protocol` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-estefania-better-agent-auth`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-agent-auth-protocol-adopt` | Adopt agent-as-principal auth | Give each agent its own identity (private key) permanently bound to a user and a host; grant capabilities (specific actions), not broad scopes; discover capabilities via a well-known agent-config endpoint, or in the interim a directory that translates a service's OpenAPI spec into capabilities and matches intent → capability; default hosts to read-only so an agent can't mutate (e.g. send email) without an explicit approval flow (device / client-initiated back-channel authorization); log every action for attribution; support instant revoke (and delete the residual access token, not just the grant) | `el-agent-auth-protocol`, `el-agent-scoped-authorization` **[registry]**, `el-oauth-token-exchange` **[registry]**, `el-agent-capability-directory`, `el-mcp` **[registry]** |
| `how-directory-not-proxy` | Prefer a directory over a proxy for agent capability routing | Don't put a data-carrying proxy in the path (not scalable — it moves all the traffic); use a directory that only matches intent ↔ capabilities and logs per provider; ship the protocol as three layers — an agent plugin (server-side: verify agent, issue grants, enforce constraints), an SDK (mints keys, assigns agent identity, exposes an MCP so hosts like Claude/Cursor connect), and the directory; constrain the agent so its only path to external services is through the protocol | `el-agent-auth-protocol`, `el-agent-capability-directory`, `el-mcp` **[registry]** |

## Dropped

- Internet-history and phone-book analogies, "hire your agent" / CEO-credentials framing — rhetorical devices; folded into signal prose.
- AI-gateway comparison ("an AI gateway doesn't give agents their own identity") — competitor contrast; kept in prose, no node.
- V1→V2 roadmap (long-lived/enterprise agents, agent policies, next draft) — forward-looking; noted in Review, no signal.
- `el-keycard` **[registry]** — **not attached**: Keycard the product is never mentioned; the task flagged it as "same space," and the conceptual overlap is captured by reusing `el-oauth-token-exchange` + `el-agent-scoped-authorization` instead (see Review note 3).
- Discord/contribution CTA, device-flow UI mechanics — logistics.

## Review notes

1. **Speaker credit.** The listing credited "Bereket Habtemeskel & Paola Estefania." The transcript confirms **Paola presented solo** ("you were expecting Burgett also — he couldn't come, but we made this workshop together"). Both credited `ContributedByExpert` (co-authors); Bereket did not speak — drop his edge if you credit delivered talks only.
2. **`co-better-auth` name flagged.** The captions never cleanly state the company; "Better Auth" comes from the talk listing. The protocol/tool is rendered as "Agent Auth protocol" / "Agent D" (the demo MCP) — all caption-garbled. Verify before public-facing use.
3. **Registry-reuse decision (per task).** The task named `el-oauth-token-exchange` + `el-keycard` + `el-agent-scoped-authorization` as the batch-2/3 security-cluster reuses. I reused `el-oauth-token-exchange` (token-for-the-agent) and `el-agent-scoped-authorization` (capabilities/least-privilege/agent-as-principal — the single closest match) but **did not** attach `el-keycard` (a specific competitor product not referenced here). Only two new elements coined: `el-agent-auth-protocol` (the umbrella + three-layer architecture + cryptographic identity) and `el-agent-capability-directory` (discovery). Capability-vs-scope and per-agent-identity deliberately fold into `el-agent-scoped-authorization` rather than duplicating it.
4. Pattern split mirrors the security cluster: the risk/attack-surface signal → `pat-new-cyber-threats` **[registry]** (seed brief: "agentic enterprise attack surfaces"); the solution signals (trust/attribution re-architected outside the model) → `pat-verification-gap` **[registry]**, consistent with Maida/Keycard and Madabhushi/Scalekit.
