# SPIKE extraction — "Claws Out: Securing and Building with OpenClaw" (Nick Taylor, Pomerium) — FOR REVIEW

Source transcript: `transcripts/taylor-pomerium-claws-out-openclaw.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/xg1zNlzw7Jk — AI Engineer World's Fair, published 2026-07-11.
`stagingTimestamp` for the artifact and all signals: 2026-07-11 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-taylor-claws-out` | Claws Out: Securing and Building with OpenClaw (Nick Taylor, Pomerium — AI Engineer World's Fair) | youtube | https://youtu.be/xg1zNlzw7Jk |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-nick-taylor`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-nick-taylor` | Nick Taylor (developer advocate, Pomerium; GitHub Star, Microsoft MVP, AWS Community Builder; OpenClaw contributor — trusted proxy auth mode) | `AffiliatedWithCompany → co-pomerium` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-pomerium` | Pomerium | developer | open-core identity-aware proxy (identity provider + policy engine + reverse proxy) for securing internal apps; the proxy Taylor uses to gate his OpenClaw gateway and MCP endpoints |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-identity-aware-proxy` | Identity-aware proxy | concept | security | Google-originated pattern (GCP IAP): identity provider + policy engine + reverse proxy in front of an internal app, so policy — not tokens pasted into UIs — dictates access; implementations include Pomerium (open core) and Caddy+OAuth; now applied to agent control planes |

Element edges: `IdentifiedInArtifact → ia-aie-taylor-claws-out`; `el-identity-aware-proxy` `EnablesElement → el-openclaw` **[registry]** (secures its control plane).

**[registry]** reused: `el-openclaw` (the talk's subject — self-hosted agent gateway; trusted proxy auth mode is an OpenClaw feature, kept as prose, see Review notes), `el-mcp` (demo builds an MCP server with UI per the now-in-spec MCP apps additions, live inside ChatGPT), `co-replit` (passing nod — no edge).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-taylor-claws-out`, `SourcedFromSource → source-aie-yt`. Domain per row.

| slug | name / brief | domain | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-openclaw-control-plane-hardening` | OpenClaw shipped a community-contributed "trusted proxy auth" mode (Taylor's Feb 2026 contribution, maintainer-specced): an identity-aware proxy now gates the gateway/control plane, replacing an auth token in the websocket query string + per-device pairing — security hardening for a self-hosted agent that is also a UX win | security | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-openclaw`, `OnElement → el-identity-aware-proxy`, `RelevantCompany → co-pomerium` |
| `sig-openclaw-issue-velocity` | OpenClaw's growth measured in issue numbers: Taylor's issue was #1560; two weeks later numbering was near 16,000 — contributors must rebase constantly to keep PRs mergeable; his stale PR was auto-closed during a vacation | harness | `FormsPattern → pat-agent-supply-chain` **[registry]** | `OnElement → el-openclaw` |
| `sig-agent-full-gh-access-premature-pr` | First-hand over-permissioning incident: Taylor gave OpenClaw full GitHub CLI access while using it to write his own contribution; it opened the PR before he finished reviewing — plus community incidents of exposed instances and users' emails being mass-deleted | security | `FormsPattern → pat-new-cyber-threats` | `OnElement → el-openclaw` |
| `sig-personal-software-from-phone` | "Age of personal software" in practice: Taylor builds his own tools (Claw Space workspace-file browser, MCP apps) by chatting with his self-hosted agent from his phone over Discord — Telegram rejected because channels aren't encrypted (his security-company CEO vetoed it) | harness | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-openclaw` |
| `sig-mcp-apps-ui-in-chatgpt` | MCP servers with UI are now in the MCP spec ("MCP apps"): live demo registers an OAuth'd MCP server in ChatGPT, renders React-based widgets in-chat (echo tool, conference-speaker search over the AIE speakers.json), hot-reloads via Vite while the agent edits it, and calls back into the LLM via send-message | harness | `FormsPattern → pat-agent-supply-chain` | `OnElement → el-mcp` |

## Insights (1 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-proxy-gated-agent-exposure` | Self-hosted agents are only safely useful when you can expose them: gating the control plane (and anything the agent serves, like MCP endpoints) behind an identity-aware proxy lets local agent workspaces be reached from ChatGPT, phones, and chat apps without tokens in query strings or device pairing — hardening and usability stop being a trade-off | `HighlightsPattern → pat-new-cyber-threats` | `ReliesOnElement → el-identity-aware-proxy`, `ReliesOnElement → el-openclaw` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-taylor-claws-out`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-harden-openclaw-access` | Harden access to a self-hosted agent's control plane | Put an identity-aware proxy (Pomerium, Caddy+OAuth) in front of the gateway; switch OpenClaw to trusted-proxy auth mode: list `trusted_proxies` IPs, set the user header (e.g. a JWT) + required headers, optional allowed-users (or let proxy policy decide); this removes the websocket token-in-query-string and device pairing; run the agent on encrypted channels only (not Telegram); scope tool access — full GitHub CLI access means PRs go up before you've reviewed them | `ReferencesElement → el-identity-aware-proxy`, `ReferencesElement → el-openclaw` |

## Dropped

- Claw Space (Taylor's personal workspace-file web UI) as an Element — a one-person side project; kept as prose evidence in `sig-personal-software-from-phone`.
- "Trusted proxy auth mode" as its own Element — it is an OpenClaw feature/config surface, below Element altitude; captured in the hardening signal + KnowHow. Promote if other talks reference it.
- Contributor names (Peter Stipe as maintainer, Anthony/Sid bugfix) — community color; no Expert nodes.
- nginx/Caddy/GCP IAP mentions — folded into `el-identity-aware-proxy` prose.
- co-openai — ChatGPT is the demo surface, but no OpenAI-specific claim; no edge.

## Review notes

1. Per the brief, this talk links registry entities heavily: `el-openclaw` carries 4 of 5 signals; no new agent-gateway element was coined.
2. Pattern fit judgment calls: `sig-openclaw-issue-velocity` and `sig-mcp-apps-ui-in-chatgpt` → `pat-agent-supply-chain` reads the pattern broadly (explosive community ecosystem + MCP surface expansion = growing supply-chain exposure). If you read that pattern strictly as *exploitation*, drop those two edges — the hardening and over-permissioning signals on `pat-new-cyber-threats` are the safe core.
3. `sig-personal-software-from-phone` → `pat-saaspocalypse`: build-your-own-tools replacing bought software is the resonance; cut if the pattern is strictly about the SaaS vendor market.
4. Caption garbles: "McClaw" (Taylor's pet name for his OpenClaw instance — kept as color only), "Clawzette" (talk-title riff), "jot" = JWT, "wath"/"oauth" = OAuth, "V" = Vite, "engine X" = nginx. "Peter uh Stipe" may be garbled; not coined.
5. Dates: the contribution "back in February" (2026, from the July talk). The maintainer criteria + merge sequence is paraphrased from captions.
