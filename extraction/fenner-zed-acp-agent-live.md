# SPIKE extraction — "Building an ACP-Compatible Agent Live" (Bennet Fenner, Zed) — FOR REVIEW

Source transcript: `transcripts/fenner-zed-acp-agent-live.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/HsxQICTLF84 — AI Engineer World's Fair, published 2026-07-08.
`stagingTimestamp` for the artifact and all signals: 2026-07-08 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-fenner-acp-live` | Building an ACP-Compatible Agent Live (Bennet Fenner, Zed — AI Engineer World's Fair) | youtube | https://youtu.be/HsxQICTLF84 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-bennet-fenner`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-bennet-fenner` | Bennet Fenner (engineer at Zed; works on the Agent Client Protocol; live-built an ACP agent on stage) | `AffiliatedWithCompany → co-zed` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-zed` | Zed | developer | AI code editor written in Rust; created and open-sourced the Agent Client Protocol (ACP) so users can bring any coding agent into the editor |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-acp` | Agent Client Protocol (ACP) | technology | harness | Open JSON-RPC protocol from Zed standardizing agent↔client communication, LSP/MCP-style: initialize/authenticate/session/prompt lifecycle; streamed session updates (agent message chunks, tool-call → tool-call-update status); diff content type (agent sends old/new text, client renders the diff); client-advertised capabilities the agent can call back into (buffer-aware file-system proxy, managed terminals). Transport is stdio today; remote transport in progress (JetBrains). website: https://agentclientprotocol.com |

Element edges: `el-acp` `DevelopedByCompany → co-zed`; `IdentifiedInArtifact → ia-aie-fenner-acp-live`; `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**.
Reused without new edges: `el-mcp` **[registry]** (named only as an analogy for ACP).

## Signals (3 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-fenner-acp-live`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-acp-forty-clients` | ACP reaches ~40 clients within roughly a year: JetBrains, Obsidian, and OpenClaw implement the client side (OpenClaw is simultaneously an ACP client and an agent); agents join natively (OpenCode and Cursor ship ACP modes in their CLI agents) or via adapters that translate an agent's native protocol — agent↔editor interop is standardizing the way LSP did for language tooling | `FormsPattern → pat-model-not-bottleneck` | `OnElement → el-acp`; `OnElement → el-openclaw` **[registry]**; `RelevantCompany → co-zed`; `RelevantCompany → co-cursor` **[registry]** |
| `sig-tui-agent-wave-editor-response` | Speaker dates 2025 as the rise of terminal coding agents from every major model provider (Claude Code, Codex, Gemini CLI); Zed's strategic response was not to compete on an in-house agent but to let users "bring the agent of choice" behind one unified interface — the editor's job becomes hosting agents, not owning them | `FormsPattern → pat-model-not-bottleneck` | `OnElement → el-claude-code` **[registry]**; `RelevantCompany → co-zed` |
| `sig-minimal-agent-live-bootstrap` | Live on stage: a bare coding agent is two tools (read file, edit file) plus a stateless model-API loop; retrofitting full ACP (streaming, tool-call status, client FS proxy) took ~15 minutes, after which the agent added a terminal tool to its own source, compiled, and ran it. The agent loop is commodity boilerplate (the demo code was itself agent-generated); the leverage sits in client-side capabilities the protocol exposes | `FormsPattern → pat-harness-over-model` | `OnElement → el-acp` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-protocol-decouples-agent-from-editor` | An LSP moment for agents: once agents speak a shared protocol they become swappable backends, and clients compete on rendering and capabilities — integration value accrues at the protocol layer, not in whose model powers the loop | `HighlightsPattern → pat-model-not-bottleneck` | `ReliesOnElement → el-acp` |
| `ins-client-mediated-perception` | Editor-embedded agents shouldn't read the raw file system: ACP proxies FS and terminals through the client so the agent sees what the user sees (unsaved buffer state, live terminals) — perception mediation by the harness, not extra model capability, is what makes embedded agents trustworthy | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-acp` |

## KnowHow (1 new)

All `SourcedFromArtifact → ia-aie-fenner-acp-live`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-acp-agent-integration` | Make an existing agent ACP-compatible | Implement the four minimum methods: initialize (respond with protocol version + advertised capabilities), authenticate (no-op if the key comes from an env var), session/new (generate ID, bind agent to client-supplied cwd), prompt (look up session, run the tool loop); stream model output as session-update `agent_message_chunk` notifications; wrap each tool as a `tool_call` update (title, status=in_progress, locations) followed by a `tool_call_update` (final status + content); prefer client capabilities (readTextFile, terminals) over native FS calls so unsaved buffer edits are visible; send edits as diff content (old/new text — the client does the diffing); transport is stdio | `ReferencesElement → el-acp` |

## Dropped

- LSP — named only as an analogy for ACP; no node.
- Codex / Gemini CLI — members of the 2025 TUI wave; prose inside `sig-tui-agent-wave-editor-response`.
- JetBrains / Obsidian / OpenCode — adopter mentions, prose inside `sig-acp-forty-clients`; not coined (passing).
- The duplicated-output demo bug, Wi-Fi trouble, and unpublished demo repo — stage noise, explicitly "don't use in production".

## Review notes

1. Caption garble: "open code and co- uh and cursor having ACP mode built into their CLI agents" — read as OpenCode and Cursor; the dangling "co-" could be Codex. The `co-cursor` edge is kept; verify against the video before seeding.
2. Speaker name: captions say "Bennett"; the official listing spells it "Bennet Fenner" — official spelling used.
3. Tempted pattern, NOT coined (one-talk evidence): "agent interop standardization" — the protocol layer as the new competitive surface. Filed under `pat-model-not-bottleneck`; flag if it recurs in later batches.
4. The ~40-clients figure and the adoption roster are speaker-claimed and unverified.
5. `el-openclaw` reuse: the claim that OpenClaw is both an ACP client and an agent lives in `sig-acp-forty-clients`'s brief; interesting for the OpenClaw node if reconciled.
