# SPIKE extraction — "Security Firewall for Agents" (Ryan Dahl, Deno) — FOR REVIEW

Source transcript: `transcripts/dahl-deno-security-firewall-agents.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/MkRYPFIMCSA — AI Engineer World's Fair, published 2026-08-17.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-17 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the creator of Node.js (and Deno) on running incident-response agents (OpenClaw) with rewrite access to production systems — Postgres, Kubernetes, ClickHouse, AWS, GitHub, Slack — and the security stance that follows: **the agent is untrusted software; the guard cannot live inside the agent.** Deno's answer is **Claw Patrol**, an MIT-licensed proxy that parses every byte an agent emits at the protocol level (not just HTTP), injects credentials the agent never sees, and enforces a rule file. Caption garbles: "Dino"/"Dino Deploy" → **Deno / Deno Deploy**, "OpenClaw"/"open clock"/"open clause" → **OpenClaw**, "claw patrol" kept, "cubecuddle" → **kubectl**, "Codeex"/"codeex" → **Codex**, "yellow mode" → likely **YOLO mode**, "Crabt Trap" → **Crabtrap** (Brex), "OpenShell" (NVIDIA) → ⚠ likely **NeMo Guardrails / an NVIDIA sandbox** (see review note 3), "SIG v4" → **AWS SigV4**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-dahl-security-firewall-agents` | Security Firewall for Agents (Ryan Dahl, Deno — AI Engineer World's Fair) | youtube | https://youtu.be/MkRYPFIMCSA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-ryan-dahl`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-ryan-dahl` | Ryan Dahl (CEO, Deno; creator of Node.js) | `AffiliatedWithCompany → co-deno` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-deno` | Deno | developer | JavaScript/TypeScript runtime company; runs **Deno Deploy** (website hosting). Author of **Claw Patrol** (MIT). Uses OpenClaw agents for incident response with rewrite access to production Postgres, Kubernetes, ClickHouse, AWS, GitHub, Slack |

Reused **[registry]**, edge-only: `co-anthropic` **[seed]** (Opus, "remarkably well aligned" but insufficient), `co-nvidia` **[b2]** (a process-sandbox reference), `co-brex` — *not coined* (Crabtrap author, passing reference). Not coined: Open Router, LiteLLM, HTTPjail, Agent Vault, Tailscale, WireGuard — tools named in the landscape survey.

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-as-untrusted-software` | The agent is untrusted software | concept | security | The stance the whole talk rests on: "you can't rely on the agent itself to guard what it's doing — you can't put the guard inside the agent." Opus refuses `delete users table` "over and over," but security "can't just be wishful thinking that Opus will always obey"; support-connected agents are **prompt-injectable from outside**, so any string could push the model into a bad state. Alignment is good but not a security boundary — the boundary has to be elsewhere. As models get smarter the problem shrinks but "we're always going to have to have backstop security mechanisms" |
| `el-byte-level-egress-control` | Byte-level egress control | concept | security | The core insight: every nefarious and every good action an agent takes "comes in the form of some network communication — some bytes over the wire," whether via MCP or a spawned subprocess. ACLs, read-only credentials, and MCP-tool scoping all help "up to a point" but break down because **access composes into holes** (reach one system, tunnel to another — e.g. through an EKS endpoint into a VPC Postgres to `DROP TABLE`) and because "as soon as OpenClaw spawns psql you've broken through the MCP boundary." So the guard must understand the actual bytes, at the protocol level, not just HTTP |
| `el-claw-patrol` | Claw Patrol | product | security | Deno's MIT-licensed proxy that sits in front of agents. Operates **below HTTP** — parses every byte of each protocol (Postgres wire protocol included), with a plug-in system for unknown protocols. Holds credentials like Agent Vault and **injects them so the agent never sees secret values**. A dashboard shows every "action" (more general than an HTTP request) per device/agent — allowed, denied, or pending approval — with analytics. Treats the agent software as a **black box requiring no modification**. Runs over Tailscale/WireGuard; Claw Patrol acts as a Tailscale exit node and reuses Tailscale identity for dashboard auth |
| `el-hcl-egress-rules` | HCL egress rule file | technology | security | The key piece: permissions written in **HCL** (the Terraform config language), checked into git, "a big long file — like a thousand lines," every change managed in precise detail. Rules can block specific Postgres functions and apply **even when tunneling through other systems**. Ships with a **test system**: fixture requests flow through the rules so you can unit-test that a given request is always blocked — "an outbound path the agent's host can't reach, on a protocol that isn't HTTP, gated by a rule that understands SQL" |
| `el-egress-approval-routing` | Egress approval routing | technology | security | Rules don't only allow/deny — they can **route an action for approval**: ask a human in a Slack channel, run an LLM-as-judge over the request, or any combination (LLM judge first, then Slack). Precise control over what agents do, entirely outside the agent software. Credential injection supports many forms — bearer headers, cookies, Postgres, ClickHouse, OAuth, AWS SigV4 |

Element edges: all five `IdentifiedInArtifact → ia-aie-dahl-security-firewall-agents`.
`el-claw-patrol` `DevelopedByCompany → co-deno`, `UsesElement → el-byte-level-egress-control`, `el-hcl-egress-rules`, `el-egress-approval-routing`;
`el-byte-level-egress-control` `UsesElement → el-agent-as-untrusted-software`;
`el-agent-as-untrusted-software` `EnablesElement → el-byte-level-egress-control`;
`el-claw-patrol` `ExemplifiesPattern → pat-new-cyber-threats` **[registry]**, `EnablesPattern → pat-verification-gap` **[registry]**;
`el-egress-approval-routing` `UsesElement → el-claw-patrol`.

Reused elements (no new nodes): `el-openclaw` **[registry]** (the incident-response agent), `el-mcp` **[seed]** (one egress path among several — the talk's argument is that MCP scoping is insufficient because subprocesses bypass it), `el-agent-vault`-adjacent (Agent Vault named as prior art for credential injection; not coined).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-dahl-security-firewall-agents`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-deno`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-agent-is-a-security-boundary-problem` | security | The creator of Node.js states the thesis plainly: agents given production rewrite access "have to be untrusted software — you can't put the guard inside the agent." Opus refusing to drop the users table "over and over" is not security, because support-connected agents are prompt-injectable from outside; alignment "is a good thing" but the security boundary "has to be elsewhere." A frontier-adjacent practitioner arguing that model alignment and in-agent guardrails are categorically the wrong layer for production security | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-agent-as-untrusted-software` |
| `sig-egress-must-be-parsed-at-protocol-layer` | security | Why HTTP-level and MCP-level controls are insufficient: every agent action is bytes over the wire, but a subprocess (psql on the Postgres wire protocol) escapes MCP scoping, and access composes into holes — tunnel through an EKS endpoint into a VPC Postgres and `DROP TABLE`. So the guard must parse each protocol's bytes, understand SQL, and enforce rules that hold even through tunnels. Security relocated from the agent to a byte-level egress proxy | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-byte-level-egress-control`, `el-mcp` **[registry, seed]** |
| `sig-security-as-external-proxy-with-rules` | security | The product answer: Claw Patrol, an MIT proxy below HTTP that parses every byte, injects credentials the agent never sees, and enforces a git-managed **1,000-line HCL rule file** with a fixture-based test system — treating the agent as an unmodifiable black box. A demo: Codex in YOLO mode obeys "delete the users table," spawns psql, and the proxy rejects the destructive action mid-protocol. Verification of agent behaviour moved into an independent, testable, deterministic layer outside the model | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-claw-patrol`, `el-hcl-egress-rules` |
| `sig-credentials-injected-agent-never-sees` | security | The credential-handling pattern (echoing Agent Vault as prior art but extended): the proxy holds all production credentials and injects them at egress, so "the agent doesn't ever actually see secret values" — supporting bearer headers, cookies, Postgres, ClickHouse, OAuth, and AWS SigV4. Runs off the public internet inside Tailscale/WireGuard, with Claw Patrol as the exit node and Tailscale identity gating the dashboard. Convergent with OpenAI's b18 vaults and Anthropic's b19 credential-away-from-model — a third independent lab-adjacent arrival at "the model never sees secrets" | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-egress-approval-routing`, `el-claw-patrol` |
| `sig-approval-routing-human-or-judge` | security | Rules can route an action to a human in Slack or an LLM-as-judge (or both in sequence) rather than just allow/deny — precise, external, per-action control. Same constrained-verifier shape as OpenAI's auto-review (b18) and Anthropic's outcomes grader (b19), here at the network-egress layer: the judge sits outside the agent and gates the bytes, not the reasoning | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-egress-approval-routing` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-alignment-is-not-a-boundary` | The talk's durable claim is a categorical one: alignment reduces the probability of bad action but cannot bound it, because a prompt-injectable agent can be driven into a state where it believes the bad action is correct — so any security argument that terminates in "the model will refuse" has no boundary at all. That reframes agent security as a network-egress problem with a testable deterministic gate, and it is the same move the corpus keeps making elsewhere (verifier outside the model) applied to the wire. As models improve the residual risk shrinks but never reaches zero, so the backstop is permanent | `HighlightsPattern → pat-new-cyber-threats` **[registry]** | `ReliesOnElement → el-agent-as-untrusted-software`, `el-byte-level-egress-control` |
| `ins-the-boundary-is-the-bytes` | Locating the guard at the byte/protocol layer rather than at MCP or HTTP is what makes it complete: subprocesses, tunnels and composed access all reduce to bytes leaving the host, so a proxy that parses every protocol and injects credentials is the only place that sees everything an agent actually does. The cost is operational — a thousand lines of hand-managed HCL, a proxy holding every production credential — but it is the layer where "give the agent human-level access safely" becomes a testable rule rather than a hope | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-byte-level-egress-control`, `el-hcl-egress-rules` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-dahl-security-firewall-agents`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-firewall-a-production-agent` | Put the security boundary outside the agent | Treat any agent with production access as **untrusted software** and never place the guard inside it — alignment lowers risk but cannot bound it, and support-connected agents are prompt-injectable, so "the model will refuse" is not a security argument; recognize that every agent action is **bytes over the wire**, and that MCP scoping and read-only credentials break down because subprocesses bypass MCP and access **composes into holes** (one system tunnels into another); put a **proxy below HTTP** that parses each protocol's bytes (including non-HTTP ones like the Postgres wire protocol) and enforces rules that hold even through tunnels; **hold credentials in the proxy and inject them at egress** so the agent never sees secret values, across bearer/cookie/OAuth/Postgres/SigV4 forms; write permissions as a **version-controlled rule file with unit tests** (fixture requests that must always be blocked) so security changes are reviewable and testable; **route risky actions for approval** to a human channel or an LLM judge rather than only allow/deny; keep everything **off the public internet** (Tailscale/WireGuard) and reuse that identity for dashboard auth; and log every action, since the proxy is the one place that sees everything the agent does | `ReferencesElement → el-agent-as-untrusted-software`, `el-byte-level-egress-control`, `el-claw-patrol`, `el-hcl-egress-rules`, `el-egress-approval-routing` |

## Dropped

- **The pager-duty / incident-response framing** — motivation; folded into `co-deno` and the elements.
- **The landscape survey** (LLM gateways / Open Router / LiteLLM guardrails; HTTPjail; Crabtrap's LLM-judge-over-HTTP; Agent Vault credential injection; NVIDIA process sandbox) — named as partial solutions Claw Patrol supersedes; kept in prose, not coined, since each is a passing reference.
- **The two audience Q&A exchanges** (rule-file testing; does the problem shrink as agents get smarter) — the substantive answers are folded into `el-hcl-egress-rules` and `el-agent-as-untrusted-software`.

## Review notes

1. **⚑ A strong `pat-new-cyber-threats` data point from a load-bearing source** — the creator of Node.js arguing that in-agent guardrails and alignment are the wrong security layer, with a shipped MIT proxy as the alternative. Pairs with Gallon's b20 CAPTCHA-defeat exhibit (agents *are* the threat surface) as its defensive counterpart: bot defense and agent-egress defense both move outside the model. Also a fourth independent "the model never sees secrets" arrival after OpenAI vaults (b18), Anthropic credential-away-from-model (b19), and Agent Vault (prior art).
2. **Cross-pattern convergence worth carrying to review.** Approval-routing-to-a-constrained-judge (human or LLM) is now the same architecture in four talks across three batches: OpenAI auto-review (b18), Anthropic outcomes (b19), and here at the egress layer. Candidate texture for a "verifier is a boxed external agent" thread; none proposed (mechanism, not thesis).
3. **⚠ Verify before seeding:** "Claw Patrol" MIT status and repo; the "1,000-line HCL file"; "OpenShell" attributed to NVIDIA (likely a garble — possibly NeMo Guardrails or an NVIDIA container sandbox); "yellow mode" for Codex (likely YOLO mode); Crabtrap's Brex attribution. `co-brex` referenced but not coined (no facts beyond authorship of Crabtrap).
4. **`el-claw-patrol` carries `EnablesPattern → pat-verification-gap`** (deterministic external verification of agent actions) alongside its `ExemplifiesPattern → pat-new-cyber-threats` — appropriate; the tool is both a threat response and a verification mechanism.
