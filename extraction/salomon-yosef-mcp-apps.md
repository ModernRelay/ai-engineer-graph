# SPIKE extraction — "MCP Apps: Extending the Frontier" (Ido Salomon & Liad Yosef) — FOR REVIEW

Source transcript: `transcripts/salomon-yosef-mcp-apps.txt` (auto-captions — quotes are paraphrases, not verbatim; both speaker names garbled, "MCPY"/"MCPUI" → MCP-UI throughout, see review note 2).
Video: https://youtu.be/-jY2T2PiJBE — AI Engineer World's Fair, published 2026-08-02.
`stagingTimestamp` for the artifact and all dated nodes (signals, knowhows): 2026-08-02 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the **spec authors themselves** — creator and co-creator/maintainers of MCP-UI and the official MCP Apps extension — narrate its arc from one-person side project (May 2025) to a cross-vendor standard co-created with Anthropic and OpenAI, demo the mechanics, and lay out the "agentic web" thesis: websites decompose into branded UI atoms composed inside personal assistants, with the host owning the user journey. This talk also **resolves a batch-8 identity flag** (review note 3).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-salomon-yosef-mcp-apps` | MCP Apps: Extending the Frontier (Ido Salomon & Liad Yosef — AI Engineer World's Fair) | youtube | https://youtu.be/-jY2T2PiJBE |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-ido-salomon`; `ContributedByExpert → exp-liad-yosef`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-ido-salomon` | Ido Salomon (creator of MCP-UI, May 2025; co-creator and maintainer of the MCP Apps spec; member of the MCP steering committee) | — (no employer stated in the talk; see review note 1) |
| `exp-liad-yosef` | Liad Yosef (works with Salomon on MCP-UI; co-creator and maintainer of the MCP Apps spec; recently co-founded Aura, a research lab for the agentic web) | `AffiliatedWithCompany → co-aura` |

Per the extraction brief, no employer was guessed for Salomon: the transcript states his spec roles but no company. (Batch 8's ambiguous "Manufact co-founder?" reading was **not** adopted — see review note 3.)

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-aura` | Aura | research | "A research lab for the agentic web," recently co-founded by Liad Yosef — stated in the talk, which is why it is coined despite thinness. ⚠ Name is caption-only ("Aura"); the promised "more about it later" never arrives in the transcript. Verify spelling/existence before public-facing use |

Reused: `co-anthropic` **[registry, seed]**, `co-openai` **[registry, b2]**, `co-block` **[registry, b9]**, `co-shopify` **[registry, b11]**, `co-hugging-face` **[registry, b9]**, `co-monday` **[registry, b10]**, `co-google` **[registry, b2]** (WebMCP; Gemini as A2UI target). Kept in prose (no nodes, adopter/demo name-drops): ElevenLabs ("11 Labs"), Postman, PostHog (the funnel-widget demo), Autodesk (heavy-app reusable-views motivation), Cursor, GitHub Copilot / VS Code, LibreChat, Spotify (mechanics example), Google Calendar / Amazon / Booking.com (anniversary vignette).

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-view-tools` | View tools (host→app channel) | technology | harness | The reverse direction of MCP Apps interactivity, in the spec now and "released very soon": until this, the flow was app→host (user clicks, app raises an event, host decides); view tools ("app tools" — both names used in-talk) let the **chat drive the app** — "fill out this form for me" and the host operates the embedded UI on the user's behalf. Explicitly framed as MCP Apps standardizing what WebMCP (Google's standard for agent↔web-view interaction) addresses |
| `el-webmcp` | WebMCP | technology | harness | Google's standard for how agents interact with web views; named in the talk only as the thing MCP Apps absorbs into view/app tools — the two standardization efforts converging on one host-mediated channel |
| `el-generative-ui-spectrum` | Generative-UI spectrum | concept | harness | The speakers' map of UI-production strategies for agent hosts: **predefined** UI (MCP Apps' sandboxed iframe — the app ships finished UI) ↔ **declarative** UI (JSON-render, A2UI — the app returns build instructions, the chat builds the UI) ↔ **fully generative** UI (the model writes the UI; Claude's ask-for-a-UI feature "is actually based on MCP Apps" underneath). MCP Apps positions itself as agnostic to where UI comes from, plus the interop layer: a just-released guide shows one server shipping A2UI to Gemini and the same payload wrapped as an MCP App to ChatGPT, and one codebase running in LibreChat and ChatGPT unchanged |
| `el-ui-atomization` | UI atomization (the agentic web) | concept | harness | The thesis under the spec: websites stop being destinations and decompose into **branded, interactive UI atoms** that a personal assistant composes with the user's own context — the calendar chunk, the storefront chunk, the map chunk — so the user never leaves the assistant. The three-way payoff as the speakers state it: the user keeps a brand they recognize and trust, the brand keeps its identity instead of being reduced to text, and the host gains capabilities it didn't build. The structural consequence: **no application controls the user journey anymore** — every interaction routes through the chat, which is also what makes the journey auditable |

Element edges: all four `IdentifiedInArtifact → ia-aie-salomon-yosef-mcp-apps`; `el-view-tools` `UsesElement → el-mcp-apps` **[registry]**, `UsesElement → el-webmcp`; `el-webmcp` `DevelopedByCompany → co-google` **[registry]**; `el-generative-ui-spectrum` `UsesElement → el-mcp-apps` **[registry]**, `UsesElement → el-a2ui` **[registry]**, `UsesElement → el-generative-ui` **[registry]**; `el-ui-atomization` `UsesElement → el-mcp-apps` **[registry]**, `EnablesPattern → pat-saaspocalypse` **[registry]**.

Reused elements (no new nodes): `el-mcp-apps` **[registry, batch 8]** — deliberately NOT re-coined and NOT split into a separate `el-mcp-ui` node (review note 4); `el-mcp` **[registry, seed]**; `el-a2ui`, `el-generative-ui` **[registry, batch 2]**; `el-mcp-app-stores` **[registry, batch 8]**; `el-goose` **[registry, batch 9]**.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-salomon-yosef-mcp-apps`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-mcp-apps-cross-vendor-consolidation` | harness | An interactive-UI-over-MCP protocol went from one person's project (MCP-UI, May 2025) to the **official MCP extension co-created with Anthropic and OpenAI** in months: launched with Claude and VS Code; ChatGPT Apps "are actually based on MCP Apps" and OpenAI *recommends* it as the protocol for building them; clients now include Cursor, GitHub Copilot, LibreChat, and Goose — which was the first MCP-UI client a year ago and now underlies Block's just-shipped agentic-commerce product. Governance matured with it: an open working group in the MCP committee convening every three weeks with Anthropic, OpenAI and partners, plus a community of plugins, integrations and courses | `FormsPattern → pat-agent-supply-chain` **[registry]** | `OnElement → el-mcp-apps` **[registry]**, `el-mcp` **[registry]**, `el-goose` **[registry]**; `RelevantCompany → co-anthropic`, `co-openai`, `co-block` **[all registry]** |
| `sig-brand-loss-blocked-mcp-servers` | harness | The spec authors' origin story names the adoption blocker for the whole MCP server ecosystem: companies refused to build servers because chat "reduces them to a textual database" — losing brand identity and the UX they invested in. MCP Apps exists to reverse that: services ship their own branded, interactive UI chunks into the chat (the demo: a PostHog funnel widget rendering inside Claude, "the PostHog experience within ChatGPT or Claude"), so a service can live inside the assistant without dissolving into text | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-mcp-apps` **[registry]**, `el-ui-atomization`; `RelevantCompany → co-shopify`, `co-hugging-face`, `co-monday` **[all registry]** |
| `sig-host-owns-the-user-journey` | harness | The architecture transfers journey control from apps to hosts, by construction: the app's UI renders in a sandbox, and when the user clicks, the app cannot call its own backend — it raises an event to the **host** ("I recommend calling this tool") and *the host decides*. The spec defines three levels of app control — notify the chat, ask the chat to run a prompt, or release the flow entirely — and the speakers draw the consequence explicitly: "no application will control the user journey anymore… Amazon won't be able to see my flow; everything goes through the chat for auditability" | `FormsPattern → pat-saaspocalypse` **[registry]**; `FormsPattern → pat-agent-supply-chain` **[registry]** | `OnElement → el-mcp-apps` **[registry]**, `el-ui-atomization` |
| `sig-generative-ui-approaches-converge` | harness | The competing UI-for-agents strands are converging on one interop surface: MCP Apps declares itself agnostic across the predefined ↔ declarative ↔ fully-generative spectrum; a days-old guide shows the same server shipping A2UI to Gemini and the wrapped MCP App to ChatGPT; Claude's generate-me-a-UI feature is MCP Apps underneath; WebMCP-style host-drives-the-view interaction is being standardized in as view/app tools; and "write once, run everywhere" is demonstrated with one codebase running in open-source LibreChat and ChatGPT | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-generative-ui-spectrum`, `el-a2ui` **[registry]**, `el-generative-ui` **[registry]**, `el-view-tools`, `el-webmcp`; `RelevantCompany → co-google` **[registry]** |
| `sig-chat-hosts-reach-app-store-scale` | harness | The distribution claim: ChatGPT alone was cited months ago at **800M weekly users — ~10% of world population** — a number the web took ~13 years to reach, making the assistant surface ~"170 times the total addressable market of the Apple App Store when it launched." The speakers' conclusion is categorical: MCP Apps "isn't just a technology… this is an entirely new way to distribute applications," with 2026 called as the year it becomes "a global standard for UI" | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-mcp-apps` **[registry]**, `el-mcp-app-stores` **[registry]**; `RelevantCompany → co-openai` **[registry]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-chat-host-is-the-new-app-platform` | The assistant host is accreting every property that historically defined a platform: distribution (app-store-scale reach inside ChatGPT/Claude), the interaction contract (three spec-defined levels of journey control), trust and auditability (everything routes through the chat), and the customer relationship itself (the app no longer sees the user's flow). SaaS frontends don't get destroyed in this shift — they get **demoted to branded atoms** whose composition, context and journey belong to the host. The spec authors present this as the win-win that unblocks adoption; it is also a one-way transfer of power to whoever owns the chat surface | `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-mcp-apps` **[registry]**, `el-ui-atomization`, `el-mcp-app-stores` **[registry]** |
| `ins-standardize-the-channel-not-the-ui` | MCP Apps won cross-vendor convergence by standardizing the *channel* — how UI is transmitted, sandboxed, and how it communicates with the host — while staying agnostic about how the UI is produced (shipped iframe, declarative A2UI/JSON instructions, or model-generated). That neutrality is what let Anthropic, OpenAI and Google-adjacent standards converge on it rather than fight it, and it means the predefined-vs-generative UI question can be settled later, per use case, without re-litigating the protocol | `HighlightsPattern → pat-agent-supply-chain` **[registry]** | `ReliesOnElement → el-generative-ui-spectrum`, `el-mcp-apps` **[registry]**, `el-view-tools` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-salomon-yosef-mcp-apps`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-ship-ui-over-mcp` | Ship interactive branded UI through MCP Apps | Link the tool to a prefixed UI resource returning HTML — "pretty simple code"; on the host side use the MCP-UI SDK (a React/web component taking the resource plus a callback) and render in the sandbox; **never let the app call its own backend** — raise events to the host recommending tool calls and let the host keep flow control; choose the journey-control level deliberately (notify / run-a-prompt / release to chat); expect resources to be preloaded rather than fetched at click time; for heavy views (3D renders), plan for reusable-view identifiers rather than re-rendering per turn; for multi-host reach, author declarative payloads (A2UI) and wrap them as MCP Apps where needed — one codebase can serve Gemini, ChatGPT and LibreChat; and build against the official ext-apps repo SDK, where spec changes land immediately | `ReferencesElement → el-mcp-apps` **[registry]**, `el-generative-ui-spectrum`, `el-view-tools`, `el-a2ui` **[registry]** |

## Dropped

- **The anniversary-planning vignette** (20 browser tabs vs. assistant-composed atoms from Google Calendar / Amazon / Booking) — the thesis illustration; folded into `el-ui-atomization`'s brief.
- **The PostHog funnel walk-through and the Spotify favorite-button example** — demo mechanics; the load-bearing parts (branding inside Claude, host-mediated tool calls) live in the signals.
- **"Adam Craft"** — Salomon says he "also created Adam Craft, if you were in the talk yesterday"; unresolvable caption garble (review note 2), no node.
- **Community texture** (plugins, courses, GitHub issue screenshots, tri-weekly meeting logistics beyond the fact of the working group) — kept as prose inside `sig-mcp-apps-cross-vendor-consolidation`.
- **"Not quite Jarvis, but… we're close"** closer — rhetoric (caption "Travis"); noted only for the garble list.

## Review notes

1. **Affiliations handled per the brief.** Salomon: spec roles only, no employer stated → Expert with no `AffiliatedWithCompany` edge (corpus precedent: exp-sachin-gupta b3, exp-rallabandi b15). Yosef: the talk states he "recently co-founded Aura, a research lab for the agentic web" → edge to the new `co-aura`, with the name flagged caption-only. If review can't verify Aura, the fallback is dropping the company node and the edge — one-node change.
2. **Garbles.** "Ido Sadan" → **Ido Salomon** (matches byline and his stated MCP-UI/MCP Apps roles); "I'm the Adi" → **Liad** (Yosef, from byline); "MCPY"/"MCPUI" → **MCP-UI**; "photo call" → protocol; "open eye" → OpenAI; "Cloud"/"cloud" → Claude throughout (incl. "cloud apps" → Claude's apps/generated-UI feature); "11 Labs" → ElevenLabs; "Libra Chat" → LibreChat; "X app(s)" → the official extension repo (plausibly `ext-apps` under the modelcontextprotocol org — verify before citing); "combon" not present in this talk; "Adam Craft" → unresolved (possibly a project shown in a previous-day talk); "Travis" → **Jarvis**. Speaker-name resolutions are high-confidence; repo name is medium.
3. **Batch-8 identity flag RESOLVED.** `zullo-manufact-mcp-apps.md` (b8) carried "'Idel Solomon', likely Ido Salomon (MCP-UI creator)" as prose with a Manufact-co-founder ambiguity. This talk confirms the person and the role (MCP-UI creator, May 2025; MCP Apps co-creator) from the primary source — and states **no** Manufact affiliation, so the b8 co-founder reading should stay unadopted. The b8 `el-mcp-apps` brief ("formerly MCP-UI… partnered with Anthropic and OpenAI") is corroborated in every checkable detail; its prose mention can now be linked to `exp-ido-salomon` at seeding.
4. **`el-mcp-ui` deliberately not coined.** The talk distinguishes MCP-UI (the origin project/SDK) from MCP Apps (the official extension), but the registry's `el-mcp-apps` brief already folds the lineage into one node ("formerly MCP-UI, started May 2025"). Splitting now would strand b8's edges on the merged node. Kept as one element with the lineage in prose; if review wants the split, coin `el-mcp-ui` at seeding and move the May-2025 material there.
5. **Pattern homing rationale.** The two `pat-saaspocalypse` support signals are the strongest in this file — but note the *flavour*: this is not "SaaS dies," it is "SaaS survives by ceding journey, context and distribution to the host." Worth carrying into the pattern's `evolution` field if it accretes more evidence of this negotiated-surrender shape (it pairs with b2's `el-headless-saas` seed thesis). `sig-generative-ui-approaches-converge` homed on `pat-model-not-bottleneck` per the corpus precedent for rendering/delivery-layer material (Ramdoss b2, Russo/Kapoor b9 rehome).
6. **Numbers caveat.** The 800M-weekly, "10% of world population," "growth of over 1 billion," and "170× App Store TAM" figures are conference-stage claims, second-hand ("someone said"), and the 1-billion sentence is visibly caption-mangled. `sig-chat-hosts-reach-app-store-scale` records them as the speakers' stated claims; verify independently before external citation.
7. **Cross-file adjacency.** Cornelia Davis (`ia-aie-davis-mcp-tasks`, same publish day, same session block) independently confirms the MCP core+extensions restructure and cites "MCP-UI two talks ago" — the two files corroborate each other on the extension model. The three-level journey-control design is also a corpus rhyme with `el-constrain-effects-not-expression` (b7) — host-side control of *effects* while expression stays free — noted here, no edge.
