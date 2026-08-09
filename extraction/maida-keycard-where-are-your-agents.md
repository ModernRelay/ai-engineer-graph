# SPIKE extraction — "It's 10pm. Do You Know Where Your Agents Are?" (Kim Maida, Keycard) — FOR REVIEW

Source transcript: `transcripts/maida-keycard-where-are-your-agents.txt` (auto-captions — quotes are paraphrases, not verbatim).
Published 2026-07-20 on the AI Engineer channel (World's Fair). `stagingTimestamp`: 2026-07-20.
Registry reuse marked **[registry]**. Talk is mostly a live demo + standards walkthrough — signal yield is deliberately low; the durable value is in the elements and knowhows.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-maida-agent-identity` | It's 10pm. Do You Know Where Your Agents Are? (Kim Maida, AI Engineer World's Fair security track) | youtube | https://youtu.be/I3znWC3MEXM |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-kim-maida`.

## Experts (1 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-kim-maida` | Kim Maida (founding GTM engineer & Head of DevRel, Keycard) | `co-keycard` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-keycard` | Keycard | developer | Standards-based platform providing a security token service + policy governance for agent access |

## Elements (2 new; 1 registry reuse)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-oauth-token-exchange` | OAuth 2 Token Exchange (RFC 8693) | technology | security | Pre-existing OAuth 2 extension (2020) repurposed as the backbone of agent access: a security token service takes a user's subject token + the runtime's workload identity, evaluates governance policy, and mints an audience-bound, task-scoped, short-lived (minutes), ephemeral (never stored) token per tool call |
| `el-keycard` | Keycard platform | product | security | Keycard's security-token-service + policy-governance product; works with off-the-shelf and custom agents, CLIs, third-party/proprietary MCP servers, MCP gateways, A2A, any OAuth IdP |
| **[registry]** `el-mcp` | Model Context Protocol | — | — | reused for edges (the demo's enforcement point sits between MCP client and server) |

Element edges: `el-keycard` `DevelopedByCompany → co-keycard`, `UsesElement → el-oauth-token-exchange`; `el-oauth-token-exchange` `EnablesPattern → pat-verification-gap` **[registry]**.

## Signals (2 new)

All: domain `security`, SpottedInArtifact → `ia-aie-maida-agent-identity`, SourcedFromSource → `source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-agent-api-key-status-quo` | The 2026 default for deployed agents is still env-file API keys: kitchen-sink scopes, no attribution of calls to a user or agent identity, free rein even under supervision — the pattern behind the publicized agent DB-deletion incidents | pat-verification-gap **[registry]** | — |
| `sig-agent-auth-spec-convergence` | Agent-identity standards churn (new specs "almost daily", mid-2026) is converging on composition with the existing RFC 8693 token exchange rather than a new protocol — enterprises adopt it without new-spec fear | pat-verification-gap | co-keycard |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-policy-before-credential` | Evaluate policy before the credential exists: a denied request means the token was never minted — nothing to leak, replay, or steal. This inverts the detect-and-revoke posture of API-key security | pat-verification-gap | el-oauth-token-exchange |
| `ins-hitl-needs-policy-backing` | Human-in-the-loop is only a control if the approval itself is policy-gated: the approver must hold the role for the action, so a consent-fatigued 2am "approve" from the wrong human is rejected by the same policy engine | pat-verification-gap | el-oauth-token-exchange |

## KnowHow (2 new)

All SourcedFromArtifact → `ia-aie-maida-agent-identity`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-token-exchange-agent-access` | Replace agent API keys with token exchange | Authenticate the operator via an IdP and delegate only a subset of their permissions as a subject token; put an OAuth-capable client (gateway before third-party MCP servers, custom agent app, or CLI wrapper) in the execution path; per proposed tool call, have the runtime authenticate to the STS with client credentials/workload identity + subject token and request access for that tool call only; enforce governance policy pre-mint; issued tokens are audience-bound to the target MCP server, minutes-lived, never stored, discarded after the call | el-oauth-token-exchange, el-mcp |
| `how-bootstrap-oauth-scopes` | Bootstrap scope definitions from the resource server | Don't invent an agent-scope taxonomy from scratch: the user's resource-server scopes are the baseline (they're what the subject token carries); layer additional tool-call-governance scopes on top only for custom MCP servers, or pass the baseline through | el-oauth-token-exchange, el-mcp |

## Dropped

- The full incident-management demo narrative (cert renewal, DB drop, prod restart, scale-up) — illustration, not fact; its one real-world echo ("this has really happened to high-profile companies") is already carried by `sig-replit-db-deletion` [batch1].
- "Works with OpenClaw and whatever ships next week" — compatibility marketing; `el-openclaw` **[registry]** left unlinked.
- Keycard workshop/booth logistics.

## Review notes

1. Two signals is below the 3-6 bar on purpose — the talk is a demo + spec explainer; both retained signals are observations about the industry, not the demo.
2. `sig-agent-api-key-status-quo` is an industry-state observation without a hard dataset behind it; kept because it's the premise the whole security track argues from — cut if you want dataset-grade signals only.
3. `ins-hitl-needs-policy-backing` is adjacent to batch1's `ins-steer-beats-ask` but distinct: that one says asks don't scale; this one says asks themselves need access control. Merge if you disagree.
4. Cross-check: batch1 pattern description for `pat-verification-gap` mentions "runtime policy enforcement at the tool-call boundary" — this talk is primary evidence for that clause; the identity/credential angle could be worth a sentence in the pattern description at reconciliation.
