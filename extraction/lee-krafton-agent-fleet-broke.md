# SPIKE extraction — "I Run a Fleet of AI Agents Across Three Machines. Here's What Broke." (Kyle Jaejun Lee, KRAFTON) — FOR REVIEW

Source transcript: `transcripts/lee-krafton-agent-fleet-broke.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/4kYl2_mqmnQ — AI Engineer World's Fair, published 2026-07-08.
`stagingTimestamp` for the artifact and all signals: 2026-07-08 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-lee-agent-fleet` | I Run a Fleet of AI Agents Across Three Machines. Here's What Broke. (Kyle Jaejun Lee, KRAFTON — AI Engineer World's Fair) | youtube | https://youtu.be/4kYl2_mqmnQ |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-kyle-jaejun-lee`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-kyle-jaejun-lee` | Kyle Jaejun Lee (engineer at KRAFTON; runs a daily-driver fleet of AI coding agents across a MacBook and two headless Linux boxes) | `AffiliatedWithCompany → co-krafton` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-krafton` | KRAFTON | developer | South Korean game company (PUBG). Appears via an engineer's multi-machine agent fleet practice, not as an AI vendor. |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-org-hierarchy` | Agent org hierarchy | concept | harness | Multi-agent fleet structured as a corporate hierarchy — CEO / VP / manager / worker as real entity types (not metaphor), each an agent with its own scoped context and its own approval boundary. Context flows down in slices ("each layer only gets the slice it needs"), results flow back up; the human reviews only what reaches the top. Includes a review gateway: any layer's plan blocks until approved, then a hook fires execution automatically. |
| `el-filesystem-agent-state` | Filesystem as agent state | concept | harness | Agent state moved out of the context window onto disk: every entity gets a workspace (mission, current status, handoff folder with the actual work product); shared context all agents must honor lives in a shared dir; machine-bound state under machines/. Enables "reset, don't compact" — wipe the context entirely and let the agent re-read its own handoff/history files to resume — plus crash recovery, one-command fleet reboot, and cross-machine migration via git. |
| `el-kubernetes` | Kubernetes | technology | infra | Container-orchestration substrate (declare needs, a scheduler places workloads; compute, secrets, tools abstracted beneath). Invoked here as the layer that already answers an agent fleet's unsolved problems — the plan is to stack it underneath and build only the agent-native orchestration (task routing, review flow, context management) on top. |

Element edges: all three `IdentifiedInArtifact → ia-aie-lee-agent-fleet`; `el-agent-org-hierarchy` and `el-filesystem-agent-state` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-lee-agent-fleet`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-fleet-operator-is-bottleneck` | KRAFTON engineer running 4–6 concurrent agent contexts in tmux found the human silently becomes the scheduler (who does what), the memory (what each is doing), and the reviewer — "I'm not running agents anymore… my own attention was the bottleneck." Flat piles of agents stop scaling at a handful of live contexts, well before model capability does | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-krafton` |
| `sig-agent-fleet-as-org-chart` | Fleet rebuilt as an organization — CEO/VP/manager/worker as real entity types with scoped context and approval boundaries — so the operator holds one context instead of six; plans block at a single web-inbox review gateway until approved, and the gateway itself was built by an infra team of agents inside the fleet ("agents building the tools that run the agents") | `FormsPattern → pat-harness-over-model` **[registry]** | — |
| `sig-reset-over-compact` | Practitioner abandoned context compaction entirely — slow, unselectable, lossy ("whatever it throws away is just gone"). Instead state lives in files (mission/status/handoff); he clears Claude's context outright and the agent re-reads its own handoff files and resumes. After a MacBook power loss killed everything in flight, a single boot command brought the whole fleet back because all state was in files | `FormsPattern → pat-harness-over-model` **[registry]** | — |
| `sig-multi-machine-five-failures` | Scaling from one machine to three (MacBook + two always-on headless Linux boxes, one control plane) broke five ways: orchestrators doing the work themselves instead of dispatching (fixed by a CLI harness + skills making dispatch the only available path); managers spawning tmux panes until capture-pane couldn't read them; OOM with swap full under stacked Claude Code + MCP processes; git credentials colliding across workspaces (fixed with fully separated per-workspace environments); laptop sleep/power loss killing in-flight jobs. Context moves between machines by committing files + git push, then tmux send-keys over SSH to pull; per-machine dirs for machine state, shared state changed only via pull request; per-machine review gateways collapsed into one on an always-on box ("your one point of control can't be a thing that falls asleep"); Discord bots (one per machine) became the single router, phone as fleet remote | `FormsPattern → pat-harness-over-model` **[registry]** | — |

Additional: `sig-reset-over-compact` `OnElement → el-claude-code` **[registry]**; `sig-multi-machine-five-failures` `OnElement → el-claude-code` **[registry]**, `OnElement → el-mcp` **[registry]**.

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-fleet-ops-is-distributed-systems` | A multi-machine agent fleet re-derives classic distributed systems one outage at a time: state sync, credential isolation, scheduling, node failure, a single control plane. The four problems still open (cross-machine consistency, local-only tools like MCP servers/browser, secure credential handoff, resource placement) are exactly the questions Kubernetes already answers — so the emerging shape is Kubernetes-style infra underneath, agent-native orchestration (task routing, review flow, context management) on top, rather than reinventing compute/secrets/tools | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-kubernetes`, `ReliesOnElement → el-agent-org-hierarchy` |
| `ins-state-outside-model-durability` | Keeping the source of truth in files instead of the context window turns agent sessions into resumable, crash-tolerant, machine-portable processes — the context window becomes a disposable cache. Durability comes from the harness (files + git + a boot script), not from model memory; compaction is a lossy, uncontrollable substitute | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-filesystem-agent-state` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-lee-agent-fleet`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-run-agent-fleet-as-org` | Structure an agent fleet as an org, not a flat pile | Make hierarchy levels real entity types with scoped context and their own approval boundaries; flow context down in slices, results up, and review only the top. Force delegation: give orchestrators a CLI harness + skills where dispatching is the only path, or they'll do the work themselves. Route every plan through one blocking review gateway (approve → hook fires the work); host it on an always-on machine, never a laptop that sleeps. Collapse per-machine inboxes into one main gateway; add a single router (e.g., one Discord bot per machine) so the fleet is drivable from a phone | `ReferencesElement → el-agent-org-hierarchy` |
| `how-file-based-fleet-state` | Reset, don't compact — keep fleet state in files | Give every entity a disk workspace: mission, current status, handoff folder (the work product that gets passed along). Instead of compacting, wipe the context and have the agent re-read its handoff + history files to resume exactly where it left off. Keep machine-bound state in per-machine directories; change shared context only via pull request so machines can't silently diverge. Move work across machines by committing context files + git push, then poking the target over SSH (tmux send-keys) to pull. Maintain a one-command fleet boot so a crashed or restarted machine resumes from files | `ReferencesElement → el-filesystem-agent-state` |

## Dropped

- Machine role split (Linux A long-running coding, Linux B short-lived side projects) — operational detail, folded into signal prose.
- The boot command's name ("one overlord boot" in captions) — likely a literal command name; kept as paraphrase only.
- Live-demo screen tour ("a normal Tuesday") — color.

## Review notes

1. **Personal vs. employer infra:** the fleet is presented as personal daily infrastructure ("my personal projects", "what I actually use all day"); KRAFTON is the speaker's employer from the title. `RelevantCompany → co-krafton` kept only on the practitioner-context signal — drop it if you read the fleet as fully personal.
2. **`pat-durable-execution` added evidence (candidate — NOT coined, no edges; strongest data point in this 5-talk set):** reset-not-compact, state-in-files, crash recovery via boot command, cross-machine resumption over git is a hand-rolled durable-execution layer. If coined at review, rehome `sig-reset-over-compact` (and arguably `sig-multi-machine-five-failures`) from `pat-harness-over-model`.
3. **"AI-native organization" candidate resonance:** agents organized as literal org-chart entity types with approval boundaries; plus "an infra team inside the fleet built the gateway." Noted, no edge.
4. `sig-fleet-operator-is-bottleneck` → `pat-model-not-bottleneck`: the named bottleneck is human attention/orchestration, not the model — an on-thesis reading (failure lives in the layer around the model); move to `pat-harness-over-model` if you read the pattern more narrowly as product/value migration.
5. **Adjacent registry elements, deliberately not edged:** `el-ralph-loop` **[registry]** (fresh-context loop re-reading durable files) is a sibling of reset-not-compact; `el-paperclip` / `el-liveness-model` **[registry]** (batch 5) cover the same control-plane territory his home-grown gateway occupies; `el-agent-checkpoint-replay` (batch 3) may overlap `el-filesystem-agent-state`. Flagging for reconciliation rather than edging on uncertain briefs.
6. Kubernetes direction is stated intent ("that's where I'm headed"), not shipped — insight phrased as the emerging answer, not a deployment.
