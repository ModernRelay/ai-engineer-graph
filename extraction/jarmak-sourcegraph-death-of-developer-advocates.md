# SPIKE extraction — "The Death of Developer Advocates" (Stephanie Jarmak, Sourcegraph) — FOR REVIEW

Source transcript: `transcripts/jarmak-sourcegraph-death-of-developer-advocates.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/Lrw0jqBNaw0 — AI Engineer World's Fair (GTM/leadership track), published 2026-08-26.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-26 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a research scientist (an astronomer a year ago; zero GitHub commits then, 12,000 now, maintaining a multi-agent orchestration framework) who became Sourcegraph's **agent advocate**. DevRel's audience changed: the agent is both a **user** of your tool (reads docs, calls APIs, hits errors) and a **recommender** of it (installs libraries, answers "what should I use"). Two measurement programs: **CodeScaleBench** — hundreds of SDLC tasks run with and without Sourcegraph's code-navigation MCP, traces exposing tool friction — and **generative engine optimization** experiments showing the product recommended 65% of the time to comparison shoppers and 0% at the moment of pain, with old models pitching a retired product and compounding on the web. DevRel's core (enablement, community, feedback loop, credibility) survives with a new audience. Caption garbles: "Claude's slop" kept, "m dashes" → **em dashes**, "AEs" → account executives, "Cody" kept (Sourcegraph's older product), "LLMs at TXT" → **llms.txt**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-jarmak-sourcegraph-death-of-developer-advocates` | The Death of Developer Advocates (Stephanie Jarmak, Sourcegraph — AI Engineer World's Fair) | youtube | https://youtu.be/Lrw0jqBNaw0 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-stephanie-jarmak`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-stephanie-jarmak` | Stephanie Jarmak (Research Scientist / Agent Advocate, Sourcegraph; ex-astronomer) | `AffiliatedWithCompany → co-sourcegraph` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-sourcegraph` | Sourcegraph | developer | Code intelligence / code search; ships a code-navigation MCP tool for agents and a cross-repo observability layer; older product Cody still pitched by stale models; runs CodeScaleBench and GEO experiments; has replaced "developer advocate" with an agent-advocate role |

Referenced, not coined: the chatbots/agents used in the GEO study (Claude Sonnet 4 → 4.6), Discord communities, MCP registries.

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-advocate` | The agent advocate | concept | | DevRel's history: 1980s software evangelism (one-way) → 2010s developer advocacy (a feedback loop with developers as kingmakers, DX as GTM) → 2026, when developers "no longer work alone" and their job changes, so the advocate's must too. Other users appear: engineers as orchestrators of agent fleets expected to have AI fluency, and non-engineers who can now use dev tools through agents. The agent itself is a user (reads docs differently, calls the API, has its own frustrations recovering from errors) *and* a recommender, driving the bottom-up adoption DevRel exists to encourage — via ChatGPT/Claude Q&A or by installing the library directly into a workflow |
| `el-codescalebench` | CodeScaleBench | technology | harness | Hundreds of SDLC-representative tasks run by agents with and without Sourcegraph's code-navigation MCP tool, producing thousands of traces that show where the tool helps and where it breaks. Example: the model's training-data bias expected a `read_line` parameter where the tool offered `start_line`; the description didn't say otherwise, the call failed, the error explained why, the agent recovered — but burned a whole turn. Fix the description. Organizations will evaluate tools by tokens consumed and speed, not only success — "measure how these users are using it" |
| `el-generative-engine-optimization` | Generative engine optimization (GEO) | concept | | SEO for agents and chatbots: design prompts around what the ICP actually does. In a pilot, comparison-shopping prompts recommended the product ~65% of the time; a pain prompt ("we keep breaking downstream services when we change shared libraries because we can't see all the consumers") got **zero mentions** — the agent suggested a wiki page. Re-run on Sonnet 4.6, the model pitched the retired Cody product *more*, because old models' outputs compound on the internet. Tactics: llms.txt and authoritative sources with provenance; give agents something current to quote (examples, charts, FAQs); keep everything fresh; be in marketplaces and MCP registries; remove friction (an agent won't recommend a tool that needs three demos and a sales email); cover the pains in content; measure lift after content campaigns |
| `el-devrel-three-flavors` | DevRel's three flavors for the agent era | concept | | Engineering flavor: partner with engineering on the agent's interfaces to the product (MCP server), evals and instrumentation. Product flavor: own the end-to-end agentic experience, translate evals into agent-experience rubrics for the product team. Marketing flavor: own pipeline generation — how agents enter the funnel, find the product, and bring developers along. Roles across the org are fuzzier, which helps mix and match |
| `el-agent-experience-report` | The agent experience report | ops | | Quick start for DevRel: point a coding agent at your docs, read the transcript, and write up the agent's experience; for GTM, build the GEO prompt set and track mentions versus recommendations. Credibility differs by audience: humans "know what Claude's slop is and nobody likes it," while "Claude loves its own slop" — agent-facing content can be structured and em-dashed. The curb-cut argument: built for wheelchairs, used by everyone with wheels — serve the agent and the human path clears too |

Element edges: all five `IdentifiedInArtifact → ia-aie-jarmak-sourcegraph-death-of-developer-advocates`.
`el-codescalebench` `DevelopedByCompany → co-sourcegraph`;
`el-agent-advocate` `UsesElement → el-codescalebench`, `el-generative-engine-optimization`, `el-devrel-three-flavors`, `el-agent-experience-report`;
`el-generative-engine-optimization` `UsesElement → el-agent-legible-web` **[registry]**, `el-agent-capability-directory` **[registry]**, `el-mcp` **[seed]**;
`el-codescalebench` `UsesElement → el-agent-execution-traces` **[registry]**, `el-mcp` **[seed]**;
`el-agent-advocate` `ExemplifiesPattern → pat-agent-economy` **[registry]**;
`el-generative-engine-optimization` `ExemplifiesPattern → pat-agent-economy` **[registry]**;
`el-codescalebench` `EnablesPattern → pat-verification-gap` **[registry]**.

Reused elements (no new nodes): `el-agent-legible-web` **[registry]**, `el-agent-capability-directory` **[registry]** (MCP registries as where agents shop), `el-mcp` **[seed]**, `el-agent-execution-traces` **[registry]**, `el-slop-as-unread-code` **[registry]**.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-jarmak-sourcegraph-death-of-developer-advocates`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-sourcegraph`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-the-agent-is-the-new-developer-user` | | Developer relations' audience changed: the agent reads the docs, calls the API, recovers from errors and installs libraries into the workflow — a user and a recommender at once — while engineers become orchestrators of agent fleets and non-engineers gain dev-tool access through agents. Sourcegraph replaced the developer-advocate role with an **agent advocate**, and the speaker — an astronomer a year ago — now maintains a multi-agent framework with 12,000 commits | `FormsPattern → pat-agent-economy` **[registry]**; `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-agent-advocate`, `el-devrel-three-flavors` |
| `sig-agents-recommend-at-the-moment-of-need-zero-percent` | | A GEO pilot: when prompts modeled comparison shopping, agents recommended the product ~65% of the time; when they modeled the actual pain the product solves, zero mentions — the agent proposed a wiki. Tooling adoption is increasingly driven by what the agent recommends or silently installs, so vendors must measure mentions vs recommendations at the moment of need and rewrite content around pains, llms.txt and registries. The supply chain of tools now runs through the agent's suggestions | `FormsPattern → pat-agent-economy` **[registry]**; `FormsPattern → pat-agent-supply-chain` **[registry]** | `OnElement → el-generative-engine-optimization`, `el-agent-legible-web` **[registry]** |
| `sig-stale-models-compound-old-product-mentions` | | Re-running the GEO study on a newer model made it pitch Sourcegraph's retired product *more*: training data is always stale, and old models' outputs about a product accumulate on the web, so the noise compounds. The remedy is provenance — authoritative, current, quotable sources agents fetch at answer time — not waiting for the next model | `FormsPattern → pat-agent-economy` **[registry]** | `OnElement → el-generative-engine-optimization` |
| `sig-tool-friction-costs-agents-whole-turns` | harness | CodeScaleBench traces show an agent guessing a parameter name from training-data bias, failing, and recovering — at the cost of a full turn — because the tool description didn't pre-empt it. Organizations will judge tools on the tokens and time an agent spends to use them; the agent-experience report (point an agent at your docs, read the transcript) is the new DX audit | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-codescalebench`, `el-agent-experience-report` |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-serve-the-agent-and-the-human-path-clears` | The durable reframing is the curb cut: the agent is one more user in the room — one that reads docs, hits errors, spends tokens, and recommends — and designing docs, tool descriptions, content and distribution for it (measured by traces and GEO experiments) clears the path for the human on the other end. DevRel's functions survive; its instrumentation changes from surveys of developers to thousands of agent traces and recommendation experiments you can run at will | `HighlightsPattern → pat-agent-economy` **[registry]** | `ReliesOnElement → el-agent-advocate`, `el-codescalebench`, `el-generative-engine-optimization`, `el-agent-experience-report` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-jarmak-sourcegraph-death-of-developer-advocates`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-advocate-to-agents` | Measure the agent's experience and the agent's recommendations | Treat the agent as a user and a recommender: point a coding agent at your docs and write up the transcript as an agent experience report; build a benchmark of real SDLC tasks run with and without your tool and mine the traces for friction (parameter-name expectations, error messages, wasted turns), then fix descriptions and errors; judge success by tokens and speed as well as outcomes; run **GEO** experiments — prompts modeled on your ICP's real pains, not just comparison shopping — and track mentions vs recommendations, then rewrite content around the pains; publish llms.txt and authoritative, current, quotable sources (examples, charts, FAQs) since old models' outputs compound online; be present in marketplaces and MCP registries; remove friction between discovery and use (no demos and sales emails in the agent's path); keep human-facing content slop-free while structuring agent-facing content for machines; and staff the role across engineering, product and marketing flavors | `ReferencesElement → el-agent-experience-report`, `el-codescalebench`, `el-generative-engine-optimization`, `el-devrel-three-flavors`, `el-agent-advocate` |

## Dropped

- **The vacationing-manager / robot-mauling bit** — color.
- **Community-with-agents privacy remarks** (people bringing their Claudes into Discord) — one clause in the agent-advocate element.

## Review notes

1. **A GTM-track talk on the engineering side of the line** — kept in this batch for its measurement content (CodeScaleBench, GEO). The GTM track proper (8 talks) is still queued; its domain-enum gap (b22 flag) applies here too — signals carry no `domain` except the trace one.
2. **`pat-agent-economy` (machine-web / agents-as-customers leg):** agents as buyers and recommenders of developer tools with a measured 65%/0% recommendation split. Pairs with Garvin/Stripe (agent as buyer) this batch.
3. **⚠ Verify before seeding:** the 65% / 0% pilot figures, "12,000 commits," Sonnet 4 → 4.6 as the models compared, and that the multi-agent framework she maintains is Sourcegraph's.
