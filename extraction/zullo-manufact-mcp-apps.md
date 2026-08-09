# SPIKE extraction — "MCP Apps: Primitives, discovery, and the Future of Software" (Pietro Zullo, Manufact Inc) — FOR REVIEW

Source transcript: `transcripts/zullo-manufact-mcp-apps.txt` (auto-captions — quotes are paraphrases, not verbatim; heavy name garbling, see Review notes).
Video: https://youtu.be/sAOBXCDiDOs — AI Engineer World's Fair, published 2026-07-05.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-07-05 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-zullo-mcp-apps` | MCP Apps: Primitives, Discovery, and the Future of Software (Pietro Zullo, Manufact — AI Engineer World's Fair) | youtube | https://youtu.be/sAOBXCDiDOs |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-pietro-zullo`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-pietro-zullo` | Pietro Zullo (co-founder, Manufact; builds open-source MCP SDKs and MCP cloud tooling) | `AffiliatedWithCompany → co-manufact` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-manufact` | Manufact Inc | developer | open-source MCP SDKs (mcp-use, 8M+ downloads), an open-source MCP inspector, and an MCP-vertical cloud (deploy from GitHub, test, pre-vet and package store submissions) |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-mcp-apps` | MCP Apps | technology | harness | Official MCP extension (January 2026; formerly MCP-UI, started May 2025 by the MCP-UI creator — captions: "Idel Solomon", likely Ido Salomon) letting tools return sandboxed-iframe widgets instead of just JSON, with bidirectional host communication: set-state (sync widget state into model context), send-follow-up-message, widget-initiated tool calls, streaming partial tool-args into a live-updating UI, dual UI-vs-model outputs, display modes (inline / fullscreen / picture-in-picture), OS theme sync. Rendered today by Claude (Desktop, Cowork), ChatGPT, Codex, Cursor, VS Code |
| `el-mcp-app-stores` | MCP app stores | concept | harness | First-party MCP directories — ChatGPT apps (chatgpt.com/apps), Claude connectors directory, Cursor directory — with self-serve submission, automated + partly manual vetting (tool-annotation scan, auth declaration checks, test prompts/cases), and one-click install URLs replacing hand-shared JSON config. On Claude, extends to dynamic task-time connector discovery from the MCP registry |
| `el-mcp-use` | mcp-use | framework | harness | Manufact's open-source SDK family (8M+ downloads, ~10K GitHub stars) abstracting over the official MCP SDKs to build servers, clients, and agents; for MCP apps: React widget files in a resources folder auto-register as UI resources returnable from tools (compiled to HTML/CSS), plus client-capability detection primitives; `npx create-mcp-app` template |

Element edges: `el-mcp-apps` `UsesElement → el-mcp` **[registry]**; `el-mcp-app-stores` `EnablesPattern → pat-saaspocalypse` **[registry]**; `el-mcp-use` `DevelopedByCompany → co-manufact`; all three `IdentifiedInArtifact → ia-aie-zullo-mcp-apps`.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-zullo-mcp-apps`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|
| `sig-mcp-apps-official-extension` | MCP-UI became MCP Apps, an official Model Context Protocol extension, in January 2026: MCP servers now return interactive sandboxed UI, not just JSON — the ChatGPT Apps SDK, Claude, Cursor, Codex, and VS Code all render them. Speaker frames this as one of the two structural shifts in the MCP ecosystem this year | `FormsPattern → pat-saaspocalypse` | `OnElement → el-mcp-apps` | — |
| `sig-mcp-stores-open-self-serve` | The second structural shift: MCP stores moved from design-partner gating to self-serve submission — ChatGPT first, Claude for team/enterprise accounts ~2 weeks before the talk, Cursor as well — with vetting pipelines (tool-annotation scans, auth checks, test prompts, partial manual review) and one-click installs; acceptance volumes rising | `FormsPattern → pat-saaspocalypse` | `OnElement → el-mcp-app-stores` | `co-openai` **[registry]**, `co-anthropic` **[registry]**, `co-cursor` **[registry]** |
| `sig-claude-dynamic-connector-discovery` | Claude is today the only client that, given a task with no matching tool, searches the MCP registry and selects the best store-listed connector dynamically; ChatGPT expected to follow soon. With 1B+ active users expressing intent in chat, model-mediated connector selection becomes an organic, high-intent acquisition channel | `FormsPattern → pat-saaspocalypse` | `OnElement → el-mcp-app-stores` | `co-anthropic` **[registry]**, `co-openai` **[registry]** |
| `sig-mcp-server-buying-decision` | Practitioner adoption testimony: "does this product have an MCP server" is now a basic buying criterion; the speaker runs day-to-day work in Claude Cowork / Claude Code chaining connectors (Granola meeting notes → Linear tickets → agent opens PR and closes the ticket); cites Paul Graham days earlier — "AI apps are the new browsers" (paraphrase) | `FormsPattern → pat-saaspocalypse` | — | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-chat-clients-new-distribution` | If AI apps (Claude, ChatGPT, Codex, Cursor) are the new browsers, MCP servers/apps are the new websites: software distribution shifts from web + search to store placement and model-mediated selection, and product UI moves into widgets rendered inside the chat surface ("I don't want to look at your dashboard anymore — I want it in Claude") | `HighlightsPattern → pat-saaspocalypse` | `ReliesOnElement → el-mcp-apps`, `ReliesOnElement → el-mcp-app-stores` |
| `ins-connector-selection-new-seo` | When the model chooses which connector serves an intent, being selectable by the model — store presence, clean tool annotations, passing vetting, quality signal — becomes the new SEO; high-intent traffic routes to whichever vendor the model picks, before the user ever searches | `HighlightsPattern → pat-saaspocalypse` | `ReliesOnElement → el-mcp-app-stores` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-zullo-mcp-apps`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-mcp-dual-output-privacy` | Partition tool outputs between widget and model | Return rich/private data only into the sandboxed widget (structured output → UI); send the model a separate minimal text output — possibly just "the user is seeing their private information in the widget above"; use this to keep regulated/private data out of model-provider context while still shipping AI-mediated UX | `ReferencesElement → el-mcp-apps` |
| `how-mcp-store-submission` | Make an MCP server/app store-ready | Annotate every tool correctly (arguments included) — stores scan them; declare and verify authentication; supply test prompts/cases and screenshots for the partly-manual review; a UI is not required for eligibility (plain servers submit too); pre-run the clients' checks yourself before submitting; expect per-store differences in process and review speed (ChatGPT fastest-moving at talk time) | `ReferencesElement → el-mcp-app-stores` |
| `how-mcp-app-client-fallback` | Degrade gracefully on non-app clients | Detect from initialization metadata whether the connected client renders MCP apps; return widgets only to hosts that can show them; when the widget is suppressed, return its information as an alternate model-visible output so nothing load-bearing is lost | `ReferencesElement → el-mcp-apps`, `ReferencesElement → el-mcp-use` |

## Dropped

- Excalidraw MCP demo (mermaid-into-canvas token streaming) and the Remotion MCP app — demo color; `el-remotion` **[registry]** exists but the mention is illustrative only, no edge.
- "Pulsar MCP" analytics workflow — likely garbled product name, unresolved; kept out.
- Granola/Linear workflow details — folded into `sig-mcp-server-buying-decision`.
- MCP-UI creator ("Idel Solomon", likely Ido Salomon) — kept as prose in `el-mcp-apps`; not coined as Expert (see Review notes).

## Review notes

1. Caption garbles normalized against the official title: speaker rendered "Pedro" → Pietro Zullo; company rendered "Manufact"/"Manifold Cloud"/"manifester.com" → Manufact; "MCPUs"/"MCP use" → mcp-use; "Cloud"/"called" → Claude throughout; "Character AI" → ChatGPT (context: apps-store pairing, "chadigpt.com/apps" → chatgpt.com/apps). Verify all before public-facing use.
2. "Idel Solomon, the other co-founder, started working on MCP-UI (May 2025)" — almost certainly Ido Salomon (MCP-UI creator), but whether he is a *Manufact* co-founder is ambiguous in the captions; left as prose, not coined.
3. All four signals form `pat-saaspocalypse` — this is a single-thesis distribution talk; if that reads as monotone, `sig-mcp-apps-official-extension` is the one to demote to prose (it is protocol history more than an industry-change observation).
4. The store-vetting mechanics could also be read as `pat-agent-supply-chain` evidence (curated first-party distribution as the trust answer to the connector supply chain); noted, no edge added.
5. "More than a billion active users" is the speaker's round number — paraphrase, not a sourced figure.
6. Claude self-serve submission timing ("since a couple weeks") is relative to recording; publish date used for staging as instructed.
