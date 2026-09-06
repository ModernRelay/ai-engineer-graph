# SPIKE extraction — "Building the Engine While Flying the Plane: Launching the Figma MCP Server" (Jesse Lumarie, Figma) — FOR REVIEW

Source transcript: `transcripts/lumarie-figma-mcp-server-launch.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/ZIYYsAzaLlA — AI Engineer World's Fair, published 2026-08-28.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: how a one-day-a-week side project became the Figma MCP server — "one of the fastest-growing products Figma has ever had" — built while the MCP spec and its clients moved under it (SSE deprecated, OAuth added March 2025, clients implementing subsets, VS Code the "golden client"). The engineering: which serialization of Figma's C++ scene graph an agent converts best (React-Tailwind + an image beat sparse XML and images alone), **Code Connect pointers** so agents use the enterprise's accessible components instead of pixel-perfect Tailwind blobs, evals that went from a two-hour spreadsheet to hundreds of LLM-judged runs a week, and elicitation + sampling mimicked with tools when clients lacked them. Caption garbles: "MC Peeps" kept (team name), "D2R" kept, "B 64" → **base64**, "OOTH" → **OAuth**, "HMR" → ⚠ unclear, "fig jam"/"make" → FigJam / Figma Make, "cloud" → Claude.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-lumarie-figma-mcp-server-launch` | Building the Engine While Flying the Plane: Launching the Figma MCP Server (Jesse Lumarie, Figma — AI Engineer World's Fair) | youtube | https://youtu.be/ZIYYsAzaLlA |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-jesse-lumarie`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-jesse-lumarie` | Jesse Lumarie (Software Engineer, Figma; ~3 years) | `AffiliatedWithCompany → co-figma` **[registry]** |

## Companies (0 new)

Reused **[registry]**, edge-only: `co-figma` — new facts: shipped a local MCP server (~mid-2025) then a remote one (September 2025), GA'd both in October 2025, added read and write capabilities — "one of the fastest-growing products Figma has ever had"; **Make in your local codebase** is Figma's agent for GitHub/local code, born from designers wanting to write production code; engineers are given leeway to build unstaffed. Reused `co-anthropic` **[seed]** (released the MCP spec November 2024; the server-instructions blog post), `co-openai`, `co-microsoft` (VS Code as the golden client), `co-cursor` (first client Figma could ideate on).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-figma-mcp-server` | The Figma MCP server | product | context | Sends context between design and production code both ways so AI tools need no dedicated integration. Local first (Electron desktop app → IPC bridge → node process → SSE server; enterprises liked that data stayed local) as the fastest path to product-market fit; then remote (streamable HTTP + OAuth); GA October 2025; read tools for Dev Mode data (components, spacing, variables), FigJam, Make, then write capabilities. Resources expose help articles and usage guidance so the agent doesn't burn inference discovering how to use the server |
| `el-scene-graph-serialization-for-agents` | Which serialization an agent converts best | concept | context | Figma is a C++ scene graph (like the DOM). Candidates: a sparse JSX/XML-like internal form (abstract, low fidelity); **React-Tailwind** (from the Sites product — pixel-perfect if pasted into a server); a plain image (early-2025 agents were poor at image → code). Winner: React-Tailwind *plus* an image of the node — code context and image together gave better agentic output. Never inline base64 images in code ("blew up the context window"); hoist images to the top level |
| `el-code-connect-pointers` | Code Connect pointers | technology | context | Pixel-perfect is half the story: enterprises want their battle-tested, accessible, internationalized components used. Code Connect links design components to codebase components, so the server sends a **pointer** ("use Button component") instead of a Tailwind blob — higher-fidelity output and far less context. When a component isn't linked, the server prompts the user (mimicking elicitation) and has the agent scan the codebase for matches (mimicking sampling), then bulk-creates the links |
| `el-mcp-client-compatibility-drift` | MCP spec vs client drift | concept | harness | The spec moved while they built (SSE deprecated weeks in; OAuth in March 2025) and clients implemented subsets at different paces — Claude Desktop early, Claude Code incomplete, OpenAI and VS Code only after the spec update, VS Code GA in July and the eventual golden client; often only tools were supported. Server instructions were in the spec but unimplemented until Anthropic's blog post, so instructions were injected into every tool call; elicitation and sampling (now deprecated) were hacked via tools and prompts. The MCP Inspector is essential. "The spec is only two years old; we're still figuring it out" |
| `el-hand-eval-to-judged-runs` | From a two-hour spreadsheet to hundreds of judged runs | ops | harness | The first eval — quantitative (used variables? theming? right spot?) plus qualitative (looks good? good decisions with incomplete information?) — was two hours of hand-grading in Excel: "never again." Then toy repos, then a web app, now an eval engineers kick off that runs hundreds of times a week against prompt changes with LLM judges. Complication: little open-source code has Figma files attached, so eval assets had to be made. Optional tool arguments (language, framework) added as telemetry — "agents lie, but it's a signal" |

Element edges: all five `IdentifiedInArtifact → ia-aie-lumarie-figma-mcp-server-launch`.
`el-figma-mcp-server` `DevelopedByCompany → co-figma` **[registry]**;
`el-figma-mcp-server` `UsesElement → el-mcp` **[seed]**, `el-scene-graph-serialization-for-agents`, `el-code-connect-pointers`, `el-mcp-client-compatibility-drift`;
`el-hand-eval-to-judged-runs` `UsesElement → el-judge-as-classifier` **[registry]**, `el-golden-dataset` **[registry]**;
`el-code-connect-pointers` `UsesElement → el-scene-graph-serialization-for-agents`;
`el-figma-mcp-server` `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-mcp-client-compatibility-drift` `ExemplifiesPattern → pat-agent-supply-chain` **[registry]**;
`el-hand-eval-to-judged-runs` `EnablesPattern → pat-verification-gap` **[registry]**.

Reused elements (no new nodes): `el-mcp` **[seed]**, `el-judge-as-classifier` **[registry]**, `el-golden-dataset` **[registry]**, `el-mcp-apps` **[registry]**, `el-progressive-disclosure` **[registry]** (the pointer-over-blob move is context-budget discipline).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-lumarie-figma-mcp-server-launch`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-figma` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-figma-mcp-became-a-fastest-growing-product` | context | A one-day-a-week side project (a Figma plugin-based MCP server, started when only Cursor exposed the feature) shipped local ~mid-2025, remote in September, GA in October 2025, added writes — and became one of Figma's fastest-growing products ever, "not something we expected." Design context delivered to agents wherever they are turned out to be a product, not an integration | `FormsPattern → pat-harness-over-model` **[registry]**; `FormsPattern → pat-agent-economy` **[registry]** | `OnElement → el-figma-mcp-server`, `el-mcp` **[seed]** |
| `sig-representation-beats-the-model-for-design-to-code` | context | The output quality lever was serialization, not the model: React-Tailwind (which the models were "RL'd on") plus an image beat sparse XML and images alone; base64 in code blew up context; and enterprise fidelity came from **Code Connect pointers** — "use Button component" instead of a Tailwind blob — which also cut context. What the agent is handed decided the result | `FormsPattern → pat-model-not-bottleneck` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-scene-graph-serialization-for-agents`, `el-code-connect-pointers` |
| `sig-mcp-spec-outran-its-clients` | harness | Building on MCP in 2025 meant building against a moving spec (SSE deprecated, OAuth added) and clients that implemented different subsets — server instructions unimplemented, elicitation and sampling absent or later deprecated, VS Code the only complete client by July. Figma injected instructions per tool call and mimicked elicitation/sampling with tools. Two years in, the protocol ecosystem is still settling | `FormsPattern → pat-agent-supply-chain` **[registry]** | `OnElement → el-mcp-client-compatibility-drift`, `el-mcp` **[seed]** |
| `sig-hand-graded-evals-to-hundreds-a-week` | harness | Two hours grading an eval into a spreadsheet — "never doing that again" — became toy repos, a web app, and now hundreds of LLM-judged runs a week that any engineer triggers on a prompt change, with the human removed "where we don't need it." The eval asset problem (no open-source code with Figma files) had to be solved by making the data | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-hand-eval-to-judged-runs`, `el-judge-as-classifier` **[registry]** |
| `sig-unstaffed-engineers-built-figma-mcp-and-make` | | "I wasn't staffed on MCP. I wasn't staffed on our Make product" — both were built because engineers were given leeway to run with what they saw; Make-in-your-local-codebase came out of hacking with the MCP team at an offsite after research showed designers wanted to write production code. Org slack as the mechanism for the company's fastest-growing product | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-figma-mcp-server` |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-context-delivery-is-the-product` | The durable lesson is that the valuable artifact was never the model's conversion ability but the *representation and pointers* handed to it — a serialization the model was trained on, an image alongside, and a pointer to the enterprise's own component — and that packaging this as an MCP server made design context a product with its own growth curve. It is the corpus's harness thesis in the design domain, with the protocol churn as the cost of being early | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-scene-graph-serialization-for-agents`, `el-code-connect-pointers`, `el-figma-mcp-server`, `el-mcp-client-compatibility-drift` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-lumarie-figma-mcp-server-launch`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-ship-an-mcp-server-on-a-moving-spec` | Representation, pointers, evals, and client hacks | Test which serialization of your data the agent converts best — prefer one the models were trained on (React-Tailwind), add an image as *additional* context, never inline base64; send **pointers to the customer's own components** instead of generated blobs for fidelity and context economy; start with a **local** server when it's the fastest path to product-market fit and enterprises prefer data staying local, then go remote (streamable HTTP + OAuth); expect clients to implement subsets — put instructions in every tool call, expose resources so agents don't burn inference learning your server, mimic elicitation/sampling with tools when needed, and live in the MCP Inspector; replace hand-graded spreadsheets with an automated eval (toy repos → web app → hundreds of LLM-judged runs per week) and build the eval assets you can't find; add optional tool arguments as telemetry, knowing agents lie; and give engineers leeway to build unstaffed | `ReferencesElement → el-scene-graph-serialization-for-agents`, `el-code-connect-pointers`, `el-figma-mcp-server`, `el-mcp-client-compatibility-drift`, `el-hand-eval-to-judged-runs` |

## Dropped

- **The "MC Peeps" / candy aside** and demo-restart hiccups — color.
- **The exact client compatibility matrix (March 2025)** — summarized in `el-mcp-client-compatibility-drift`.

## Review notes

1. **A b16 "MCP unlock" follow-up with a product outcome** — the corpus's MCP evidence was mostly protocol-side; this is a vendor reporting MCP as its fastest-growing product, plus a grounded account of client drift (`pat-agent-supply-chain` texture: ecosystem before governance).
2. **`sig-representation-beats-the-model-for-design-to-code`** joins b22's Adobe talk as a second design-domain `pat-model-not-bottleneck` point.
3. **⚠ Verify before seeding:** launch dates (local ~mid-2025, remote September, GA October 2025), "fastest-growing product," the deprecation of sampling, and the product name "Make in your local codebase."
