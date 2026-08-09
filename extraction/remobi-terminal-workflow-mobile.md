# SPIKE extraction — "remobi.app: Don't Change Your Terminal Workflow for Mobile" (Connor Adams) — FOR REVIEW

Source transcript: `transcripts/remobi-terminal-workflow-mobile.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/5192csoTkVo — AI Engineer World's Fair, published 2026-07-12.
`stagingTimestamp` for the artifact and all signals: 2026-07-12 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Short demo-style talk — thin by design; 3 signals.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-adams-remobi-mobile` | remobi.app: Don't Change Your Terminal Workflow for Mobile (Connor Adams — AI Engineer World's Fair) | youtube | https://youtu.be/5192csoTkVo |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-connor-adams`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-connor-adams` | Connor Adams (indie builder; author of Remobi, an open-source mobile front end for tmux-based agent workflows) | — (no company stated; Remobi is a personal open-source project — no `AffiliatedWithCompany` edge) |

## Companies (0 new)

- none coined; Happy, Conductor, Tailscale mentioned in passing only (see Dropped).

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-remobi` | Remobi | product | harness | Open-source progressive web app (iOS/Android) that attaches to your existing tmux sessions over a private tunnel (Tailscale by default; Cloudflare Tunnel/ngrok possible): agent-agnostic mobile monitoring and steering of Claude Code, Codex, Pi, etc. — pane zoom, touch gestures, plan-mode toggles, and an install skill that turns your tmux config into touch keybindings |

Element edges: `el-remobi` `IdentifiedInArtifact → ia-aie-adams-remobi-mobile`; `el-remobi` `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

## Signals (3 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-adams-remobi-mobile`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-mobile-agent-supervision-demand` | Agents now run long enough that builders feel a "compulsion to check on them" from their phones (audience hands went up), and a niche app ecosystem has formed to serve it — Happy (Claude Code only, third-party relay server of uncertain trust), Claude's built-in manual session handoff to mobile, generic SSH terminal apps — each locked to one agent or high-friction | `FormsPattern → pat-harness-over-model` **[registry]** | — |
| `sig-terminal-multiagent-control-plane` | Practitioners are running 4+ coding agents in parallel tmux panes with vibe-coded custom keybindings and status tooling ("spawn N agents" bound to a keypress; the agent itself wrote the tmux config); the speaker moved off VS Code — the terminal re-emerging as the multi-agent control plane | `FormsPattern → pat-harness-over-model` | — |
| `sig-remobi-attach-not-replace` | Remobi's design bet: don't replace the workflow, attach to it — a PWA over a Tailscale tunnel into existing tmux sessions gives agent-agnostic (Claude Code / Codex / Pi) mobile control with zero workflow change; security is explicitly delegated to the private tunnel ("put it on the public internet and you've pwned your computer", paraphrase) | `FormsPattern → pat-harness-over-model` | `OnElement → el-remobi` |

## Insights (1 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-own-your-workflow-stage` | At the current "find out" stage of agent tooling, practitioners prefer owning a composable terminal workflow (tmux + vibe-coded glue: lazygit, critique, port-killers) over polished vertical apps (Conductor, Happy) that lock them to one agent or someone else's relay — the durable asset is the workflow, and mobile access should wrap it, not replace it | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-remobi` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-adams-remobi-mobile`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-mobile-terminal-access` | Get mobile access to agent sessions without changing your workflow | Run agents inside tmux on a persistent dev machine (SSH-reachable, portable setup); expose the session to your phone via a PWA server over a private tunnel — Tailscale default, Cloudflare Tunnel/ngrok work; never expose it on the public internet; use an install skill to bootstrap tmux (or convert an existing tmux config into touch keybindings) rather than hand-configuring | `ReferencesElement → el-remobi` |

## Dropped

- tmux as an Element — decades-old generic tool; load-bearing but kept as prose (coin `el-tmux` at review only if it keeps recurring as agent-control infrastructure).
- Happy, Conductor, Tailscale, lazygit, critique — competitor/dependency name-drops, prose only; no Company nodes (Tailscale is a real company but appears purely as a transport choice).
- "Pi" agent mention — kept as prose in `el-remobi` brief; unclear which product this is (see note 2).
- Audience Q&A mechanics and the demo walkthrough.

## Review notes

1. **Thin-signal talk as expected**: demo-style; all three signals are practitioner-testimony/ecosystem observations. `sig-mobile-agent-supervision-demand` is the strongest (dated ecosystem inventory of a new app niche).
2. **Garbles/uncertain names**: "Pi" as a supported agent (possibly Poe/pi.ai/a CLI named pi — unresolved); "critique" diff tool spelling unverified; "Mari" (referenced speaker) unresolved. Speaker name "Connor Adams" is clear in captions.
3. Pattern fit: all signals parked on `pat-harness-over-model` (workflow/scaffolding around agents as the durable layer). Weak resonance with the flagged "durable runtime as stack layer" candidate (agents as persistent processes needing supervision anywhere) — noted, not coined, no edges.
4. `el-remobi` is a solo open-source project, not a company product — hence Element without `DevelopedByCompany`.
