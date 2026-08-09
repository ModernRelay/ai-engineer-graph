# SPIKE extraction — "You Didn't Ship a Bug. You Just Wrote It for a Human." (Ravi Madabhushi, Scalekit) — FOR REVIEW

Source transcript: `transcripts/madabhushi-scalekit-bug-for-human.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/lMCxVorb9wM — AI Engineer World's Fair, published 2026-07-19.
`stagingTimestamp` for the artifact and all signals: 2026-07-19 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-madabhushi-bug-for-human` | You Didn't Ship a Bug. You Just Wrote It for a Human. (Ravi Madabhushi, Scalekit — AI Engineer World's Fair) | youtube | https://youtu.be/lMCxVorb9wM |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-ravi-madabhushi`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-ravi-madabhushi` | Ravi Madabhushi (co-founder, Scalekit; 10 years identity/auth operations, previously built the identity platform at Freshworks) | `AffiliatedWithCompany → co-scalekit` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-scalekit` | Scalekit | developer | identity and authentication infrastructure platform, now focused on auth for AI agents; customers include ref.tools (agent-only actors) |

## Elements (1 new, 1 registry)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-scoped-authorization` | Agent-scoped authorization | concept | security | Authorization model for non-deterministic agent actors: agent has its own identity permanently bound to the principal it acts for, least-privileged by default, with fine-grained scopes at attribute/context/principal level (which senders, which recipients, which hours), time-boxed credentials, and just-in-time elevation — explicitly beyond today's coarse OAuth scopes |
| `el-mcp` **[registry]** | Model Context Protocol | — | — | reused: MCP servers' tool-surface behavior is load-bearing in `sig-mcp-tool-surface-ignores-principal` |

Element edges: `el-agent-scoped-authorization` `IdentifiedInArtifact → ia-aie-madabhushi-bug-for-human`; `el-agent-scoped-authorization` `EnablesPattern → pat-verification-gap` (deterministic trust controls built outside the model).

## Signals (4 new)

All: domain `security`, `SpottedInArtifact → ia-aie-madabhushi-bug-for-human`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-agent-api-traffic-breaks-human-assumptions` | Scalekit saw rhythmic 15-minute latency spikes traced to a "last seen" timestamp being written ~60x faster once agents started hitting their APIs (past ~12 months) — a harmless bug, but evidence that infrastructure assumptions sized for human actors quietly break under agent traffic | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-scalekit` |
| `sig-agent-overpermissioning-default` | Across Scalekit's customer base, most agents are provisioned with far more permissions and scopes than their job requires — not developer carelessness but the default pattern, because existing auth primitives (API keys, service accounts, OAuth scopes) cannot express fine-grained agent permissions | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-scalekit` |
| `sig-mcp-tool-surface-ignores-principal` | Most MCP servers Scalekit has worked with do not limit the tool surface based on which user authorized the agent — they expose all tools the application supports and let the agent decide, so the agent sees the same surface regardless of whom it acts for and picks wrong tools | `FormsPattern → pat-agent-supply-chain`; `OnElement → el-mcp` | — |
| `sig-agent-rogue-incidents-today` | Rogue-agent incidents (e.g. agents deleting production databases) are already occurring — "a problem of today, not tomorrow"; agent-native companies like Scalekit customer ref.tools (no human actors at all, context for coding agents) are already building full OAuth scoping from scratch | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-scalekit` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-auth-determinism-assumption-broken` | Decades of auth (passwords, API keys, service accounts, OAuth) rest on two assumptions: whoever authenticates is who acts, and the actor is a deterministic program a human wrote that can be security-reviewed. Agents break both — the principal is not the actor, and no code review can bound what a probabilistic agent will do next run — so registration-time permissions no longer constrain behavior | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-agent-scoped-authorization` |
| `ins-visibility-or-prayer` | Without full visibility (every action: who took it, on behalf of whom, who authorized it, when, what scope, for how long) plus deterministic control of what an agent can do, operators are "just praying the agent doesn't do what it's not supposed to — and praying is not a strategy" | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-agent-scoped-authorization` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-madabhushi-bug-for-human`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-agent-least-privilege-authz` | Rethink authorization for agent actors | Give every agent its own identity, always bound to the principal it acts on behalf of; default to least privilege with just-in-time elevation for higher scopes; scope at attribute/context/principal level (allowed senders/recipients/hours), time-boxed to the operating window; limit MCP tool surface per authorizing user rather than exposing everything; log every action with actor, principal, authorizer, grant time and duration; start from OAuth but expect to go beyond it | `ReferencesElement → el-agent-scoped-authorization`, `ReferencesElement → el-mcp`, `ReferencesElement → el-oauth-token-exchange` **[registry]** |

## Dropped

- Freshworks — speaker's prior employer, biography only; no Company node.
- ref.tools — single-mention customer example; kept as prose inside `sig-agent-rogue-incidents-today`, no Company node.
- Salesforce / Databricks / HubSpot / Notion / Gmail — named only as example data sources agents access; no edges (co-salesforce exists in seed but the mention is not load-bearing).
- SPIFFE — passing mention in the service-account history; prose only.

## Review notes

1. Company name garble: the captions say "Scale Grid" but the official talk title/speaker listing says **Scalekit**; extracted as Scalekit. (ScaleGrid is a different, real database-hosting company — captions likely mis-heard.)
2. Pattern candidate NOT coined: "built-for-humans infrastructure breaks under agent actors" (the talk's framing thesis — auth, APIs, MCP all designed for human/deterministic actors). Evidence here is one talk; `sig-agent-api-traffic-breaks-human-assumptions` and the overpermissioning signal are parked on `pat-verification-gap` (trust re-architected outside the model) instead. If other batches surface the same thesis, consider coining and re-homing.
3. `sig-mcp-tool-surface-ignores-principal` → `pat-agent-supply-chain` is a judgment call (MCP ecosystem immaturity as attack/failure surface); flip to `pat-verification-gap` if you read supply-chain as strictly about distribution of skills/packages.
4. This talk overlaps thematically with batch1's Maida/Keycard agent-identity talk; `el-oauth-token-exchange` **[registry]** referenced rather than redefining any OAuth element. `el-agent-scoped-authorization` is coined because the fine-grained/JIT/principal-binding bundle here is broader than token exchange.
