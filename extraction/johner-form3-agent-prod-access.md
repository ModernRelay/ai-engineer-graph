# SPIKE extraction — "We Gave an Agent Production Code Access and Then Tried to Sleep at Night" (Moritz Johner, Form3) — FOR REVIEW

Source transcript: `transcripts/johner-form3-agent-prod-access.txt` (auto-captions — quotes are paraphrases, not verbatim).
Published 2026-07-20 on the AI Engineer channel (World's Fair). `stagingTimestamp`: 2026-07-20.
Registry reuse marked **[registry]**; everything else is new in this file.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-johner-agent-prod-access` | We Gave an Agent Production Code Access and Then Tried to Sleep at Night (Moritz Johner, AI Engineer World's Fair security track) | youtube | https://youtu.be/LqLoYksJ6do |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-moritz-johner`.

## Experts (1 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-moritz-johner` | Moritz Johner (Form3; built Patch Pilot) | `co-form3` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-form3` | Form3 | developer | UK payments-infrastructure fintech; thousands of repositories, regulated environment — the case-study operator of Patch Pilot |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-patch-pilot` | Patch Pilot | product | security | Form3's in-production CVE-remediation system: a boring deterministic Go orchestrator (scan OCI images, map image→repo, commit/push/PR/watch-CI) that spawns agents only for reasoning steps (smallest-effective-change remediation, CI-failure triage); agents touch the filesystem only |
| `el-deterministic-agentic-split` | Deterministic/agentic credential split | concept | security | Partition an agentic system into a deterministic layer that holds the dangerous credentials (git write, PR creation, CI trigger) and an agentic layer whose only effect is file edits; the placement of that boundary *is* the security model and bounds prompt-injection blast radius |
| `el-firecracker` | Firecracker | technology | infra | AWS's microVM monitor; gives an agent + its own Docker daemon a private kernel, solving the Docker-socket-escape problem that userland sandboxes (landlock, bubblewrap, seccomp, gVisor-style) can't compose around |
| `el-microsandbox` | microsandbox | framework | infra | Young (~3-4 months) YC-funded open-source agent-sandboxing project with batteries included (network access controls etc.); Johner's pick if rebuilding Patch Pilot today |

Element edges: `el-patch-pilot` `DevelopedByCompany → co-form3`, `UsesElement → el-deterministic-agentic-split`, `UsesElement → el-firecracker`; `el-firecracker` `DevelopedByCompany → co-amazon` (defined in `korshakov-bee-privacy-intelligence.md`); `el-deterministic-agentic-split` `EnablesPattern → pat-verification-gap` **[registry]**.

## Signals (4 new)

All: SpottedInArtifact → `ia-aie-johner-agent-prod-access`, SourcedFromSource → `source-aie-yt`.

| slug | name / brief | domain | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-patchpilot-agent-in-prod` | Form3 (regulated payments) runs an agentic CVE-remediation system in production across thousands of repos; Infosec's framing — "is this automation or a supply-chain incident waiting to happen?" — reshaped the architecture (credentials pulled out of the agent) | security | pat-agent-supply-chain **[registry]**, pat-verification-gap **[registry]** | co-form3 |
| `sig-dependency-pr-70kloc` | A routine dependency-bump PR from the agent changed ~70,000 lines — an attack/review surface far beyond human verification, produced by "just bumping a couple of dependencies" | security | pat-verification-gap, pat-agent-supply-chain | co-form3 |
| `sig-docker-socket-game-over` | Form3 ran an agent with host Docker-socket access in production and backed off: privileged-container escape makes it "game over" (env vars, process memory, SSH keys); the built-in sandboxes of Codex/Claude-class agents can't contain a Docker socket, and Linux sandbox primitives don't compose with containers | infra | pat-verification-gap | co-form3 |
| `sig-agent-sandbox-market-beta` | The agent-sandboxing ecosystem is real but beta (mid-2026): sandbox-as-a-service vendors mostly lack Docker-socket containment and network policy controls; orchestration is forming in the Kubernetes agent-sandbox SIG, open sandbox efforts, and microsandbox — no enterprise-grade default yet | infra | pat-verification-gap | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-agent-is-supply-chain-actor` | A useful coding agent IS a supply-chain actor — the moment it holds production credentials it must get the same guardrails as a human engineer; the question is never "are agents dangerous" but "what can this actor reach" | pat-agent-supply-chain | el-deterministic-agentic-split |
| `ins-blast-radius-is-architecture` | Prompt injection can't be solved, only bounded — so the deterministic-vs-agentic partition (who holds git-write and CI-trigger credentials) is the actual security model, not the sandbox drawing | pat-verification-gap | el-deterministic-agentic-split |

## KnowHow (3 new)

All SourcedFromArtifact → `ia-aie-johner-agent-prod-access`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-partition-agent-blast-radius` | Partition agent blast radius by architecture | Keep dangerous credentials (git write, PR creation, CI trigger, registry write) in a deterministic orchestrator; agent output = file edits only; vet the diff for nonsense (empty files, stray binaries) before the deterministic layer commits; prompt-steer the agent away from known-untrusted context (vendor/ dirs, CI logs); maintain an injection-eval honeypot repo (deprecated functions + migration guides that try to recruit the agent) and run the agent against it | el-deterministic-agentic-split, el-patch-pilot |
| `how-microvm-agent-sandbox` | Sandbox Docker-needing agents in a microVM | If the agent must build/run containers, put agent + Docker daemon inside a Firecracker-class microVM with its own kernel; cut the VM off from the host network and route all egress through a vsock to a host process enforcing DNS/hostname/port/CIDR policies; apply separate network policies to the deterministic layer (known egress) vs the agentic layer (ecosystem-dependent egress) | el-firecracker, el-microsandbox |
| `how-agent-retrospectives` | End every agent invocation with a retrospective | Ask the agent: what went well, what went wrong, what tools were missing, what context would help next time; aggregate across runs to separate infra failures (network, permissions) from repo-complexity failures; feed fixes back as system-prompt changes or per-repository instruction files | el-patch-pilot |

## Dropped

- Dependabot/Renovate limitations (manifest-only visibility, no cross-cutting reasoning) — framing/setup, not a graph-worthy fact; carried inside `el-patch-pilot` description.
- The libcrypto3/libssl3 diff walkthrough and Slack-notification plumbing — implementation color.
- "Agent observability is an open community problem" — too vague to stand as a signal; the retrospective knowhow carries the actionable part.
- Vendor-booth sandbox-as-a-service comparison details — folded into `sig-agent-sandbox-market-beta`.

## Review notes

1. `el-patch-pilot` kind: chose `product` to mirror `el-snappy` (internal tool) from batch1; `ops` also defensible.
2. `el-firecracker`'s DevelopedByCompany depends on `co-amazon`, coined in the Korshakov file — reconcile if that file's companies change.
3. `sig-docker-socket-game-over` names Codex/Claude sandboxes as unable to contain a socket — speaker opinion + operational experience; kept because it's grounded in Form3 having run and abandoned the setup.
4. microsandbox promoted to an Element (named, adoptable project) rather than staying prose inside the market signal — demote if too thin.
