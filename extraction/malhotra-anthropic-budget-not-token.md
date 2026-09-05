# SPIKE extraction — "Give the Agent a Budget, Not a Token" (Sachin Malhotra, Anthropic) — FOR REVIEW

Source transcript: `transcripts/malhotra-anthropic-budget-not-token.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/rbjWzZK2LU0 — AI Engineer World's Fair, published 2026-08-22.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-22 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: an engineer on Anthropic's CI team (test quarantining, merge queues, CI autoscaling for "a few thousand engineers") on what happens after the demo ships: an agent tidying up deleted **200 workloads in 90 seconds** because one pipeline stage evaluated to nothing. The failure "wasn't the model — it was giving the agent unbounded power under my token." A token is a boolean; a **budget** has four dimensions (how much, how fast, what it can undo, who's noticing). Three primitives — **asymmetric verbs**, **refilling rate limits**, **tripwires over allowlists** — sized by the **undo test**, with identity stamped by a per-session proxy, never by the request. Caption garbles: "Entropic" → **Anthropic**, "cla tag" → **Claude Tag** (in Slack), "cloud code" → **Claude Code**, "postmortm" → **postmortem**, "kotaas" → **quotas**, "right"/"rights" → **write(s)**, "trip fire" → **tripwire**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-malhotra-anthropic-budget-not-token` | Give the Agent a Budget, Not a Token (Sachin Malhotra, Anthropic — AI Engineer World's Fair) | youtube | https://youtu.be/rbjWzZK2LU0 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-sachin-malhotra`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-sachin-malhotra` | Sachin Malhotra (CI team, Anthropic) | `AffiliatedWithCompany → co-anthropic` **[seed]** |

## Companies (0 new)

Reused **[seed]**, edge-only: `co-anthropic` — new facts: internal CI machinery (test quarantining, merge automation, merge queues, CI autoscaling) serves a few thousand engineers; agents run with per-session proxies that stamp identity; a Kubernetes admission webhook caps deletes per hour per resource kind per namespace after the 200-workload incident; Claude Tag owns feature-flag rollout loops in Slack with a canary-only key.

## Elements (6 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-token-is-a-boolean-budget-is-a-shape` | A token is a boolean; a budget is a shape | concept | security | The standard incident fix — narrow the token, take the delete verb away — is what you'd never do to a new hire, and it fails for agents too: within a week or two you're pressing Enter by hand. A token is yes/no over a static scope list: too tight and the agent is useless, too wide and you write the postmortem. A budget has four dimensions: **how much** can it do, **how fast**, **what can it undo on its own**, and **who's noticing** — each primitive replaces a boolean with a budget. It's the onboarding checklist for junior engineers, written as policy |
| `el-asymmetric-verbs` | Asymmetric verbs | concept | security | Same-size actions have different blast radius by direction. Some verbs **fail out loud** (unskip a test → CI goes red; page a human → a nuisance) and some **fail silently** (skip a test → a real bug walks into production under green checks). Give agents the loud-failing verbs; keep a human on the silent ones. In Anthropic's CI the agent may re-enable quarantined tests (cheaply reversible) but skipping is a break-glass verb needing a human and an audit row — written by the proxy, "the agent never holds the pen on its own provenance" |
| `el-refilling-rate-limits-for-writes` | Refilling rate limits on every write | technology | security | The most concrete budget: a ceiling that refills per caller per time window; spend it freely, no approvals, and past the line the request bounces with a count. Every write is rate-limited, only the size varies (own namespace higher than shared). After the incident an admission webhook caps deletes per hour per resource kind per namespace; the bypass flag exists for on-call, but **inside an agent session it refuses and tells the agent to ask the human** — the agent gets the limit, the human keeps the override, nobody files a ticket |
| `el-tripwires-over-allowlists` | Tripwires over allowlists | concept | security | An allowlist is a guess written before you have data on agent behavior; it gets stale and never improves. A tripwire is how you get the data: for cheap actions let the agent act, record every action with the actor's stamp, watch the **aggregate** and page when it crosses a line — "the smoke detector, not the lock." Fixes are usually one or two lines of agent context. Example: investigation threads per hour spiked because dozens of jobs failed with the same signature; the fix was one sentence — correlate failures before launching threads — and next time it did |
| `el-undo-test` | The undo test | concept | security | The lens for sizing the other primitives: *can the agent put it back by itself?* and *how bad if it's wrong?* Verbs ask whether you'd notice the failure; undo asks whether you can recover. If both answers are fine, log it and let it go; if either is no, a **second key** held by someone other than the agent plus an audit record. Feature flags: the agent's key has the full dial on canary (ramp 0→100, toggle on bug reports) but only *proposes* production promotion — the second key is a scoped production key, not a new auth system |
| `el-identity-from-the-proxy-not-the-request` | Identity from the infrastructure, not the request | concept | security | Policy lives in two places: **text** (context files explain the why; works ~80% of the time, cheap, but "just advice — no enforcement, and prompt injection can talk it around") and **infrastructure** — a per-session proxy that doesn't read the prompt, sees a delete or a crossed budget and returns 403. The proxy holds the real credentials and stamps every outbound call with the identity it *knows*, not the one the agent claims; the cluster writes the stamp as a label, child jobs inherit it, and every safeguard (ownership, quotas, rate limits, approvals, tripwires) keys on it. Without this an agent hitting a limit can just change the header and "you don't have a rate limit, you have a suggestion" |

Element edges: all six `IdentifiedInArtifact → ia-aie-malhotra-anthropic-budget-not-token`.
`el-token-is-a-boolean-budget-is-a-shape` `UsesElement → el-asymmetric-verbs`, `el-refilling-rate-limits-for-writes`, `el-tripwires-over-allowlists`, `el-undo-test`;
`el-identity-from-the-proxy-not-the-request` `UsesElement → el-identity-aware-proxy` **[registry]**, `el-agent-identity-broker` **[registry]**, `el-agent-scoped-authorization` **[registry]**, `el-kubernetes` **[registry]**;
`el-refilling-rate-limits-for-writes` `UsesElement → el-identity-from-the-proxy-not-the-request`;
`el-tripwires-over-allowlists` `UsesElement → el-identity-from-the-proxy-not-the-request`;
`el-undo-test` `UsesElement → el-claude-tag` **[registry]**;
`el-token-is-a-boolean-budget-is-a-shape` `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-identity-from-the-proxy-not-the-request` `ExemplifiesPattern → pat-new-cyber-threats` **[registry]**;
`el-tripwires-over-allowlists` `EnablesPattern → pat-verification-gap` **[registry]**.

Reused elements (no new nodes): `el-identity-aware-proxy` **[registry]**, `el-agent-identity-broker` **[registry]**, `el-agent-scoped-authorization` **[registry]**, `el-kubernetes` **[registry]**, `el-claude-tag` **[registry]** (owns the flag-rollout loop in Slack), `el-claude-code` **[registry]** (the session in which the bypass flag refuses).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-malhotra-anthropic-budget-not-token`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-anthropic` **[seed]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-200-workloads-gone-in-90-seconds` | security | The post-demo incident at Anthropic: a cleanup agent listed stale workloads and deleted them; one pipeline stage evaluated to nothing, the filter dropped, the selector matched everything — ~200 workloads, ~20 engineers' work, some un-checkpointed training jobs, gone in 90 seconds. "Nobody was malicious; the agent genuinely thought it was tidying." The failure wasn't the model; it was "here's a token and a tool list" at production scale | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-token-is-a-boolean-budget-is-a-shape` |
| `sig-give-the-agent-a-budget-not-a-token` | security | Narrowing scope fails within weeks (you end up pressing Enter for the agent); a token is a boolean over static scopes. Replace it with a budget along four dimensions — how much, how fast, what it can undo, who's noticing — enforced by primitives, "your onboarding checklist for engineers written down as policy for agents." Agents differ from new hires only in that they never tire and are "every so often very confidently wrong" | `FormsPattern → pat-harness-over-model` **[registry]**; `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-token-is-a-boolean-budget-is-a-shape`, `el-undo-test` |
| `sig-asymmetric-verbs-loud-and-silent-failures` | security | Sort verbs by how they fail: unskipping a test or paging a human fails loudly on a dashboard and a human fixes it cheaply; skipping a test fails silently and ships a bug under green checks. Hand agents the loud verbs, keep humans on the silent ones, and let a proxy — not the agent — write the audit row. Verification relocated to "which failures would show up" | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-asymmetric-verbs` |
| `sig-tripwires-and-refilling-limits-over-allowlists` | security | Allowlists are stale guesses; refilling rate limits give full autonomy inside a ceiling with a hard cap on how bad one loop gets (a delete-cap admission webhook whose bypass refuses inside agent sessions), and tripwires on aggregates page a human *after* the line is crossed so the fix — usually one sentence of context — is grounded in what actually happened. The limit would have capped the incident at a few dozen workloads; the undo test says the rest needed a second key | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-refilling-rate-limits-for-writes`, `el-tripwires-over-allowlists`, `el-undo-test` |
| `sig-identity-must-come-from-infrastructure` | security | The one rule: identity comes from the infrastructure, not the request. Text shapes intent (~80%) but is advice; a per-session proxy that holds the credentials stamps every call with the identity it knows, the cluster labels jobs with it, children inherit it, and every safeguard keys on it — otherwise an agent at its limit simply changes the header and starts a fresh budget. "Get that one rule right and everything else is tuning." Fifth independent lab/lab-adjacent arrival at *the model never holds its own credentials* | `FormsPattern → pat-new-cyber-threats` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-identity-from-the-proxy-not-the-request`, `el-identity-aware-proxy` **[registry]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-budgets-replace-booleans` | The durable idea is a type change in agent authorization: from a boolean scope to a multi-dimensional budget (volume, rate, reversibility, observation), each dimension carried by a deterministic primitive outside the model — rate limits that refill, verbs sorted by failure mode, tripwires on aggregates, a second key for the irreversible. It preserves autonomy (no approvals inside the ceiling) while bounding the worst loop, which is exactly what scope-narrowing cannot do | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-token-is-a-boolean-budget-is-a-shape`, `el-refilling-rate-limits-for-writes`, `el-asymmetric-verbs`, `el-undo-test` |
| `ins-the-onboarding-checklist-is-the-policy` | The organizational reading: the primitives are the questions every engineering org already asks about a new hire — what can they touch, how much rope, who signs off, how do we know it's working — now written as enforceable policy for a worker that never sleeps. The text layer explains the why to the agent; the infrastructure layer bounds how wrong it can go; identity from the proxy ties the two. Agents get onboarded, not permissioned | `HighlightsPattern → pat-ai-native-org` **[registry]** | `ReliesOnElement → el-tripwires-over-allowlists`, `el-identity-from-the-proxy-not-the-request` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-malhotra-anthropic-budget-not-token`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-budget-an-agents-writes` | Four primitives and one rule for agents with production access | Give the agent verbs that **fail out loud** on a dashboard and keep a human on verbs that fail quietly; put a **refilling ceiling on every write** (size by namespace: own higher, shared lower) so the agent has full autonomy inside the limit and a loop can only get so bad — and make any bypass flag refuse inside agent sessions and ask the human; **watch aggregates, not calls**: record every action with the actor's stamp, page when a tripwire crosses, and fix with a sentence of context rather than a code change; size all of it with the **undo test** — if the agent can put it back and the blast radius is acceptable, log and let it go, otherwise require a second key held by someone else with an audit record (e.g. full canary dial, production promotion only proposed); keep policy in two places — text for intent, infrastructure for enforcement; and above all **stamp identity from a proxy that holds the credentials**, never from a header the agent controls, so every quota, approval and tripwire keys on an identity the agent can't change | `ReferencesElement → el-asymmetric-verbs`, `el-refilling-rate-limits-for-writes`, `el-tripwires-over-allowlists`, `el-undo-test`, `el-identity-from-the-proxy-not-the-request` |

## Dropped

- **The espresso / mountains intro** — color.
- **The coffee-website demo** — the "god token + tool list" setup, folded into `sig-200-workloads-gone-in-90-seconds`.

## Review notes

1. **⚑ Anthropic's own production-security practice, first-person.** Pairs with Dahl/Deno (b21, proxy below HTTP parsing bytes) and Docker/Jain (this batch, runtime containment): three independent "guard outside the agent" designs in two batches, now including the lab. `sig-identity-must-come-from-infrastructure` is the fifth "model never holds its own credentials" arrival (OpenAI vaults b18, Anthropic credential-away-from-model b19, Agent Vault, Deno b21).
2. **`el-tripwires-over-allowlists`** is a small but sharp claim — enforcement that *improves with data* versus policy that only goes stale — and the correction loop ("one sentence of context; next time it did it right") is `pat-continual-learning-turn`-adjacent; not edged, noted.
3. **Same-batch "agent spend governance" ledger:** budgets-for-writes here, TokenOps for tokens (Chawla/Koul), token ROI (Hong). Recorded in the registry section.
4. **⚠ Verify before seeding:** "200 workloads / 20 engineers / 90 seconds," "a few thousand engineers," the "~80%" text-compliance figure, and that the flag service key is canary-scoped in production practice.
