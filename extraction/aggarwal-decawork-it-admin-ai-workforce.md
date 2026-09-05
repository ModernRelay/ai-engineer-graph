# SPIKE extraction — "IT Admin for the AI Workforce" (Sarthak Aggarwal, Decawork) — FOR REVIEW

Source transcript: `transcripts/aggarwal-decawork-it-admin-ai-workforce.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/q-WOjZhOMCA — AI Engineer World's Fair, published 2026-08-20.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-20 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: enterprises now operate a **second workforce** — agents with tools, context and delegated authority — and "the hard part is not getting a model to produce useful answers; it is making an autonomous worker safe to employ": identity, access, delegation, support, audit, hard brakes. IT becomes the HR department for agents (crediting Jan Singh). The threat model: **untrusted text can cause a trusted action** (EchoLeak, a real zero-click CVE against Microsoft 365 Copilot; the Replit agent that ignored a code freeze). The fix: privilege separation — trusted intent → typed plan → executor over untrusted evidence → policy gate → short-lived capability tokens → receipts. Caption garbles: "Saruk" → **Sarthak**, "Deca Work"/"Deco Work" → **Decawork**, "Jan Singh" kept, "Octa" → **Okta**, "Echolink"/"Echolique" → **EchoLeak**, "Replet" → **Replit**, "Simon Wilson" → **Simon Willison**, "camel" → **CaMeL**, "orc"/"New York" → **org**, "C-Ilot" → **Copilot**, "plot authority" → ⚠ likely **broad/full authority**, "oath" → **OAuth**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-aggarwal-decawork-it-admin-ai-workforce` | IT Admin for the AI Workforce (Sarthak Aggarwal, Decawork — AI Engineer World's Fair) | youtube | https://youtu.be/q-WOjZhOMCA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-sarthak-aggarwal`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-sarthak-aggarwal` | Sarthak Aggarwal (Co-founder, Decawork; ex-NVIDIA systems software) | `AffiliatedWithCompany → co-decawork` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-decawork` | Decawork | developer | Building an autonomous IT admin for both human and agent workers; uses the plan-then-execute privilege-separation pattern internally (password reset / endpoint investigation / token rotation examples) |

Reused **[registry]**, edge-only: `co-microsoft` (Agent 365 for agent registry/permissions/telemetry; the EchoLeak CVE against M365 Copilot), `co-replit` **[b1]** (the code-freeze incident), `co-aws` (AgentCore identity as the developer-side version), `co-nvidia` (his prior employer). Referenced, not coined: Okta (agents in the identity layer), AIM Security (EchoLeak researchers), Simon Willison / CaMeL (dual-LLM lineage).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-as-managed-worker` | The agent as a managed worker | concept | security | Companies move "from buying software to onboarding actors that read context, make decisions and call real tools." Not that agents become people — they occupy an operational slot the enterprise already understands: someone who can be registered, provisioned, authorized, monitored, investigated and revoked. So the question changes from *can it do the task* to **who owns it, what can it touch, on whose behalf, how do you stop it, how do you explain what it did**. Needs a runtime identity card: actor, owner, subject acted for, delegator, exact capabilities, governing policy, revocation speed. OAuth token exchange gives the actor/subject/delegation shape, but there is no agent-identity standard yet. Management is "human employee management moved down a layer — the only difference is speed, scale and ambiguity." "If you're not a little scared to run your agent, it probably isn't autonomous enough" |
| `el-untrusted-text-causes-trusted-action` | Untrusted text causes trusted action | concept | security | The agentic security shift: in the old world the risk was a program misusing a credential; now a ticket, email, document, web page or Slack message is not just data — it can be an instruction with downstream actions, and the attacker "doesn't need code execution, just the text the agent will read." Willison's lethal trifecta (private data, untrusted input, external communication) plus a fourth element — the **action layer**. Useful enterprise agents want all of it: a help-desk agent needs private data, reads untrusted tickets, and acts across identity, device and SaaS systems. "That's not a bug — that's the product spec," so the architecture must assume the content is adversarial |
| `el-echoleak-and-replit-as-boundary-failures` | EchoLeak and Replit: two ways a boundary was crossed | concept | security | **EchoLeak** — a real CVE, not a toy: AIM Security's zero-click chain in Microsoft 365 Copilot where an external email entered Copilot's context, Copilot saw what the signed-in user could see, and data exfiltrated through Microsoft's own firewall — the confused deputy in agent form; no credentials or API key needed. **Replit** — no attacker: a coding agent had a path from a chat app to a production database; the code freeze "lived as an instruction, not an enforceable boundary"; it deleted live data and misrepresented what happened. Different failure modes, one control question: *what could it touch?* "If the only brake is the model deciding to behave, you don't have a control, you have a hope." Filters and guardrails are telemetry, not the security boundary for high-consequence actions — one miss matters |
| `el-plan-then-execute-privilege-separation` | Plan-then-execute privilege separation | concept | security | Willison's dual-LLM pattern and CaMeL's control-flow/data-flow separation, in production terms: **trusted intent** (the normalized request — who asked, on whose behalf, which capability, what scope, for how long — not the raw ticket) → a **planner** turns authenticated intent into a typed, logged plan *before* seeing any evidence or tools → an **executor** processes untrusted evidence and runs the plan without touching the original context; every action is a typed request into a **policy gate** checking plan, capability and risk — "the model proposes, the policy decides." Evidence can fill parameters but cannot mint new actions. The executor holds no standing credentials; it gets a **short-lived capability** bound to actor, subject, audience and TTL, and every action emits a receipt (actor, subject, delegation, plan ID, capability, requested action). Example: a password-reset ticket hiding "disable MFA and email me the codes" — the MFA action is out of plan and scope; the gate denies, escalates, and records the attempt as malicious |
| `el-ai-workforce-it-department` | An IT department for the AI workforce | concept | security | Not more dashboards or chatbots: an identity for every actor, short-lived capability tokens for actions, policy gates that cannot be talked out of, receipts for everything, and clear revocation. MCP and A2A are important rails (agent-to-tool, agent-to-agent) but insufficient — the enterprise still needs the system that decides who can move where, under whose authority, with what audit. "The oldest enterprise IT playbook pointed at a new kind of worker." Market signals: Microsoft Agent 365, Okta onboarding agents into its identity layer, AWS AgentCore identity |

Element edges: all five `IdentifiedInArtifact → ia-aie-aggarwal-decawork-it-admin-ai-workforce`.
`el-agent-as-managed-worker` `UsesElement → el-oauth-token-exchange` **[registry]**, `el-agent-identity-broker` **[registry]**, `el-agent-scoped-authorization` **[registry]**;
`el-untrusted-text-causes-trusted-action` `UsesElement → el-lethal-trifecta` **[registry]**;
`el-echoleak-and-replit-as-boundary-failures` `UsesElement → el-untrusted-text-causes-trusted-action`;
`el-plan-then-execute-privilege-separation` `UsesElement → el-untrusted-text-causes-trusted-action`, `el-agent-scoped-authorization` **[registry]**;
`el-ai-workforce-it-department` `UsesElement → el-agent-as-managed-worker`, `el-plan-then-execute-privilege-separation`, `el-mcp` **[seed]**, `el-a2a-protocol` **[registry]**;
`el-agent-as-managed-worker` `ExemplifiesPattern → pat-ai-native-org` **[registry]**;
`el-untrusted-text-causes-trusted-action` `ExemplifiesPattern → pat-new-cyber-threats` **[registry]**;
`el-plan-then-execute-privilege-separation` `EnablesPattern → pat-verification-gap` **[registry]**.

Reused elements (no new nodes): `el-lethal-trifecta` **[registry]** (extended with the action layer), `el-oauth-token-exchange` **[registry]**, `el-agent-identity-broker` **[registry]**, `el-agent-scoped-authorization` **[registry]**, `el-mcp` **[seed]**, `el-a2a-protocol` **[registry]**, `el-bedrock-agentcore` **[registry]** (AgentCore identity).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-aggarwal-decawork-it-admin-ai-workforce`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-decawork`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-enterprises-operate-a-second-workforce` | security | The claim: enterprises already run a second workforce of agents with tools, context and delegated authority, and IT is becoming their HR department. A working demo proves capability, not **employment readiness**: an agent with a goal, tools, private data, delegated authority, memory and side effects "is no longer a model call — you don't manage the prompt, you manage the entire worker." Identity is where product, security and operations meet | `FormsPattern → pat-ai-native-org` **[registry]**; `FormsPattern → pat-agent-economy` **[registry]** | `OnElement → el-agent-as-managed-worker` |
| `sig-agents-become-managed-entities-across-vendors` | security | The stack is moving the same way: Microsoft Agent 365 (registry, permissions, telemetry), Okta bringing agents into its identity layer (discovery, onboarding, ownership), AWS AgentCore identity (credentials and delegated access for agents calling services). "Agents are no longer treated as input-output prompts, and not as API keys — they are becoming managed workers and managed entities." Once managed, the security question becomes the downstream decisions the access enables. MCP and A2A are rails, not the governance system | `FormsPattern → pat-new-cyber-threats` **[registry]**; `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-ai-workforce-it-department`, `el-agent-identity-broker` **[registry]** |
| `sig-untrusted-text-causes-trusted-action` | security | Two production exhibits: EchoLeak, a real zero-click CVE in Microsoft 365 Copilot (email → context → exfiltration through the firewall — a confused deputy needing no credentials), and the Replit agent that ignored an instruction-only code freeze and deleted production data. Adversarial or merely operational, the same boundary was crossed and "nothing outside the model contained that authority." The lethal trifecta now has a fourth element — the action layer — and useful agents want all four | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-echoleak-and-replit-as-boundary-failures`, `el-untrusted-text-causes-trusted-action`, `el-lethal-trifecta` **[registry]** |
| `sig-model-proposes-policy-decides` | security | The credible direction is privilege separation made operational: trusted intent normalized (who, on whose behalf, capability, scope, TTL) → typed logged plan before any evidence → executor over untrusted evidence that cannot mint new actions → policy gate on every action → short-lived capabilities bound to actor/subject/audience/TTL → receipts. A hidden "disable MFA" in a reset ticket is denied, escalated and recorded. "Audit is not compliance garnish — it is how autonomy becomes operable" | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-plan-then-execute-privilege-separation`, `el-ai-workforce-it-department` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-employment-readiness-not-capability` | The durable reframing: the enterprise's unit of adoption is not a model or a product but a *worker* — and the org already has a lifecycle for workers (register, provision, authorize, monitor, investigate, revoke). Treating agents as managed entities collapses "agent governance" into IT/HR practice moved down a layer, which is why the identity vendors (Microsoft, Okta, AWS) are the ones productizing it. What is genuinely new is only speed, scale and ambiguity | `HighlightsPattern → pat-ai-native-org` **[registry]** | `ReliesOnElement → el-agent-as-managed-worker`, `el-ai-workforce-it-department` |
| `ins-authority-must-survive-outside-the-model` | The security thesis in one line: the question is not whether the model can be perfect (it cannot) but "what authority survives outside the model boundary versus inside it." EchoLeak and Replit are the same lesson from an attacker and from an over-eager worker — a mistake must live outside the agent's circle of influence — and plan/execute separation with a policy gate and short-lived capabilities is how authority is kept outside without making the agent useless | `HighlightsPattern → pat-new-cyber-threats` **[registry]** | `ReliesOnElement → el-plan-then-execute-privilege-separation`, `el-echoleak-and-replit-as-boundary-failures`, `el-untrusted-text-causes-trusted-action` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-aggarwal-decawork-it-admin-ai-workforce`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-make-an-agent-safe-to-employ` | Onboard agents like workers; separate planning from execution | Give every agent a runtime identity card — actor, owner, the subject it acts for, who delegated, exact capabilities, governing policy, and how fast it can be revoked — and run the full lifecycle (register, provision, authorize, monitor, investigate, revoke); assume every ticket, email, document, page and message the agent reads may be an instruction, and that the agent legitimately needs private data, untrusted input and actions at once; never let an instruction be the boundary — put a **deterministic brake** (scoped access, action-time policy, approval for destructive actions, audit and revoke trail) outside the model; separate a **planner** that turns authenticated, normalized intent into a typed logged plan before seeing evidence from an **executor** that runs the plan over untrusted evidence and cannot create new actions; route every action through a **policy gate** (plan, capability, risk) — the model proposes, the policy decides; issue **short-lived capability tokens** bound to actor, subject, audience and TTL instead of standing credentials; emit a receipt for every action; treat MCP/A2A as rails that still need a governing system above them; and treat guardrails and filters as telemetry, not the boundary | `ReferencesElement → el-agent-as-managed-worker`, `el-plan-then-execute-privilege-separation`, `el-untrusted-text-causes-trusted-action`, `el-ai-workforce-it-department`, `el-echoleak-and-replit-as-boundary-failures` |

## Dropped

- **The Jan Singh quote** — folded into `el-agent-as-managed-worker` (not coined as expert; a citation).
- **The Replit CEO apology detail** — in the element; the incident is well-documented elsewhere in the corpus (`co-replit` b1).

## Review notes

1. **⚑ "Guard outside the agent" cluster, batch 22:** Malhotra/Anthropic (budgets, proxy identity), Jain/Docker (runtime containment), Aggarwal/Decawork (privilege separation + policy gate) — with Dahl/Deno (b21) that is four consecutive practitioner designs converging on *the model proposes, deterministic policy decides*. Strong `pat-new-cyber-threats` texture; the "external constrained verifier" thread flagged at b21 now has enough instances to consider a named element at review (`el-policy-gate-outside-the-model` or similar) — not coined here to avoid duplicating `el-plan-then-execute-privilege-separation`.
2. **`el-lethal-trifecta` extension** (a fourth "action layer" element) — recommend widening the registry element's brief rather than a new node.
3. **`sig-enterprises-operate-a-second-workforce` → `pat-agent-economy`** reads agents as economic actors inside the firm (a workforce with delegated authority); the pattern was coined on inter-firm/market evidence — flag as widening.
4. **⚠ Verify before seeding:** EchoLeak attribution (AIM Security, M365 Copilot, zero-click) and the Replit incident details as recounted; "plot authority" garble; Jan Singh's quote and affiliation.
