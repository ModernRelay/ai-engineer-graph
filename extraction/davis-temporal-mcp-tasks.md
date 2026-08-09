# SPIKE extraction — "MCP Tasks (async): Why Aren't Any Agents Supporting Them?" (Cornelia Davis, Temporal) — FOR REVIEW

Source transcript: `transcripts/davis-temporal-mcp-tasks.txt` (auto-captions — quotes are paraphrases, not verbatim; "Agoric AI Foundation" and "MCPC task specification" garbles resolved, see review note 2).
Video: https://youtu.be/s4r6nk5WsZw — AI Engineer World's Fair, published 2026-08-02.
`stagingTimestamp` for the artifact and all dated nodes (signals, knowhows): 2026-08-02 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the canonical durable-execution vendor explains why **no agent client supports async MCP Tasks** — a spec whose central requirement is durability — walks the V1 protocol's failures, previews the stateless V2, and demos her own client implementation (built as a Temporal workflow). **Extraction brief honored: ALL durable-execution-candidate evidence is HELD PATTERN-LESS** (review note 1); vendor framing was not allowed to inflate claims.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-davis-mcp-tasks` | MCP Tasks (async): Why Aren't Any Agents Supporting Them? (Cornelia Davis, Temporal — AI Engineer World's Fair) | youtube | https://youtu.be/s4r6nk5WsZw |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-cornelia-davis`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-cornelia-davis` | Cornelia Davis (technologist at Temporal; distributed-systems veteran — Cloud Foundry, Kubernetes, GitOps, Weaveworks — and book author; building the missing client side of MCP Tasks, previously presented the server side at MCP Dev Summit, March 2026) | `AffiliatedWithCompany → co-temporal` |

Mentioned but NOT coined here: **Angie Jones** = `exp-angie-jones` **[registry, batch 9]** — author of the May 2026 blog announcing the stateless MCP restructure, named as "responsible for developer experience at the A~gentic~ AI Foundation, which is where MCP now lives" (caption "Agoric" — see review notes 2–3). No `ContributedByExpert` edge (cited, not a contributor to this artifact).

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-temporal` | Temporal | developer | Durable-execution platform (workflows, signals, retries) — the candidate ledger's canonical durable-execution vendor, appearing in the corpus in person for the first time. In-talk role: supplies the durable server side of the demo *and* the speaker's MCP-client implementation ("task tracker workflow") |

Reused: `co-agentic-ai-foundation` **[registry, batch 9]** (where MCP now lives; source of the V2 restructure).

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-mcp-tasks` | MCP Tasks (async MCP extension) | technology | infra | MCP extension for asynchronous, long-running tools: `tools/call` returns a **handle** instead of a response, with a spec-defined lifecycle (working → input_required → working → completed / cancelled / failed) and a hard durability requirement — per the spec, once launched a task **must survive** client crashes, server crashes, dropped connections and humans-gone-on-vacation. V1 (November 2025, marked experimental) was a **stateful** protocol: `task/list` for server-side enumeration (no filter — a million-task scan at scale) and input_required tunneled through a held-open connection with server-driven elicitation. V2 (announced May, spec "coming out in July") rebuilds it as an **extension on a stateless core**: `task/list` removed, a client-initiated update endpoint replaces the elicitation session (effectively a *signal* into the running task), clients are told to persist task IDs ("should", though an unpersisted ID is unrecoverable), and the lifecycle model is unchanged. A notifications protocol (one "did anything change?" endpoint replacing per-task polling) is the sketched path to million-task scale |
| `el-fastmcp` | FastMCP | framework | infra | Widely used MCP framework; already carries server-side MCP Tasks support (and some client pieces) and is what both demo processes run on. Davis's stated plan: land a full client-side tasks implementation **in FastMCP** within a month or two, "so you can use the same framework you're using probably for your MCP servers today" |
| `el-temporal` | Temporal (durable-execution platform) | product | infra | Workflow engine used on both sides of the demo: the invoice-processing MCP server is a workflow (ERP validation, human-in-the-loop approval via **signals**, programmed retries, survives being down at submission time), and — the talk's novelty — the **MCP client itself** is implemented as a "task tracker" workflow so the client-side protocol handling (long-lived connections, reconnect/resume, multiplexing concurrent input_required) is durable too |

Element edges: all three `IdentifiedInArtifact → ia-aie-davis-mcp-tasks`; `el-mcp-tasks` `UsesElement → el-mcp` **[registry, seed]**; `el-fastmcp` `UsesElement → el-mcp` **[registry, seed]**; `el-temporal` `DevelopedByCompany → co-temporal`. Deliberately **no** `ExemplifiesPattern`/`EnablesPattern` edges from `el-temporal` — the only fitting pattern is the uncoined `pat-durable-execution` candidate (review note 1).

Reused elements (no new nodes): `el-mcp` **[registry, seed]**. `el-mcp-apps` **[registry, batch 8]** is referenced in prose only ("they talked about MCP-UI two talks ago… that's what's happening in V2 — extensions"); the extension-model corroboration is captured in `sig-mcp-v2-stateless-core-extensions`.

## Signals (3 new)

All: `SpottedInArtifact → ia-aie-davis-mcp-tasks`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-temporal`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-mcp-tasks-zero-client-adoption` | infra | The durable-execution vendor's own talk title concedes the adoption gap: **no agent clients support MCP Tasks**, and Davis's explanation is that the holdouts are being *smart* — the November spec was marked experimental, the protocol is "super involved," and V1's core mechanics (a stateful, unfilterable `task/list`; input_required tunneled through a held-open elicitation session) were bad enough that "radical changes" landed within ~8 months. The V1 reference implementation's client couldn't even multiplex: with several tasks in input_required, responses were FIFO — you could only answer the first. She had to build her own client implementation to demo the spec at all | — **HELD PATTERN-LESS** (durable-execution candidate; counter-flavoured — see review note 1) | `OnElement → el-mcp-tasks` |
| `sig-mcp-spec-mandates-task-durability` | infra | Durability is being standardized at the **protocol layer**: the MCP Tasks spec's own verbage says a launched task can't disappear — it must survive network blips, client and server crashes, disconnections, and approvers who leave on vacation — and V2 shifts part of that burden to the client ("should persist task IDs"; Davis: unclear why not an all-caps MUST, since an unpersisted ID is unrecoverable). Her demo makes the requirement concrete: a purchase order submitted **while both servers were down** was captured and completed once they returned, and the client side survives because the protocol handler itself runs as a Temporal workflow — her argument for why the client half stayed unbuilt is precisely that this recovery/resume machinery "has all sorts of complexity in it" | — **HELD PATTERN-LESS** (durable-execution candidate; support-flavoured with a convention-shaped tail — see review note 1) | `OnElement → el-mcp-tasks`, `el-temporal`, `el-fastmcp` |
| `sig-mcp-v2-stateless-core-extensions` | infra | MCP is being restructured ~8 months after the tasks spec shipped: per the May announcement from the Agentic AI Foundation (where MCP now lives), the protocol gets a **stateless core with extensions** — tasks become an extension, `task/list` is deleted ("just because you can doesn't mean you should"), and server-driven elicitation over a long session is replaced by a client-initiated update endpoint that Davis maps directly onto Temporal's *signal* primitive. Her distsys reading: "stateful protocols are the absolute worst thing in large-scale distributed systems," and even V2 doesn't yet scale — a million tasks means a million polling clients until the spec's notifications protocol matures. The agent ecosystem's core protocol is churning through 30-year-old distributed-systems lessons in public, with breaking rewrites inside a year | `FormsPattern → pat-agent-supply-chain` **[registry]** | `OnElement → el-mcp-tasks`, `el-mcp` **[registry]**; `RelevantCompany → co-agentic-ai-foundation` **[registry]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-async-agent-protocols-are-distsys-again` | Nothing in this 20-minute frontier-conference talk is a model problem. The hard parts of long-horizon agent work — handles, lifecycles, durable state, signaling into running work, reconnect/resume, notification fan-in versus polling — are the classical distributed-systems curriculum, being relearned at the MCP layer by an engineer who lived it once already at Cloud Foundry/Kubernetes scale. The engineering frontier of "async agents" sits entirely in the periphery around the model, and the periphery is where the industry's protocol effort is going | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-mcp-tasks`, `el-temporal` |
| `ins-non-adoption-as-competence` | In a fast-churning extension ecosystem, refusing to adopt is information, not lag: the agent clients that skipped experimental MCP Tasks V1 dodged a stateful protocol that is being discarded within a year, while any early implementer would now be rewriting. When the spec surface itself is unstable, adoption timing is a risk decision — and the vendor most invested in the capability is the one telling you the holdouts were right | `HighlightsPattern → pat-agent-supply-chain` **[registry]** | `ReliesOnElement → el-mcp-tasks` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-davis-mcp-tasks`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-implement-async-mcp-tasks` | Implement MCP Tasks without getting burned | Target the V2 extension model, not V1 — the stateful protocol is going away; **persist task IDs on the client and treat the spec's "should" as MUST** (an unpersisted ID is unrecoverable); don't build on `task/list` (unfilterable, deleted in V2); on the server, map the spec's task lifecycle (working / input_required / completed / cancelled / failed) onto your own domain state machine rather than replacing it; expect **multiple concurrent** input_required tasks and multiplex them (the V1 reference client was FIFO-blocked); make the client protocol handler itself durable — Davis runs hers as a workflow so reconnect/resume survives process death; at scale, replace per-task polling with the spec's notifications endpoint ("did anything change?" then fetch); and build on FastMCP, which already has server-side task support and is where the client implementation is headed | `ReferencesElement → el-mcp-tasks`, `el-fastmcp`, `el-temporal` |

## Dropped

- **The purchase-order / invoice demo mechanics** (dashboards, buttons, cold-start hiccup, ERP retries) — illustrations; the durable-while-down submission and the signal-based approval are kept inside `sig-mcp-spec-mandates-task-durability` and the `el-temporal` brief.
- **The MCP Dev Summit talk (March 2026, server-side durability)** — referenced with a QR code; a prior artifact by the same speaker, not coined as an InformationArtifact (corpus convention: referenced talks stay prose).
- **Her book and CV detail** (Cloud Foundry, Kubernetes, GitOps, Weaveworks) — folded into the Expert brief; the book is unnamed in the transcript.
- **V1 tool-semantics enumeration** (`task/get`/`cancel`/`list`/`result` RPC table) — spec detail, superseded by V2; the two load-bearing failures (stateful list, tunneled elicitation) are in the signals.
- **Git repo / slides pointers** — logistics.

## Review notes

1. **`pat-durable-execution` ledger note — the core deliverable of this extraction.** Per the brief, nothing was coined and no signal was homed on the candidate; here is what the vendor's actual argument adds to the ledger:
   - **Support-shaped point:** durability is now a **spec requirement, vendor-neutral** — the MCP Tasks spec itself mandates that launched tasks survive crashes and disconnects on both sides. That is the first corpus evidence of the durability requirement being standardized at the *protocol* layer rather than argued by a runtime vendor. And her answer to "why is an engine necessary?" is concrete: the client half of the protocol (long-lived connection recovery, resume, input_required multiplexing) is hard enough that **nobody has built it** — she only got a working client by implementing the protocol handler as a Temporal workflow. Note also the convergence she points out: MCP Tasks V2's client-update endpoint is the same primitive as Temporal's *signal* — the spec is independently reinventing the engine's vocabulary.
   - **Counter-shaped point, from the vendor itself:** the title concedes **zero client adoption**, her explanation endorses the non-adopters ("they're smart"), and her go-forward plan is to ship the capability **inside FastMCP** — the commodity OSS framework people already use — rather than as "buy a durable-execution product." That delivery path rhymes with the ledger's three-practitioner meta-observation (HumanLayer/Netflix/FlyersSoft: proposed infra layers land as conventions over stock tooling). Caveat honestly: the durable substrate under her demo *is* the vendor's product, and whether the FastMCP client work embeds Temporal or is framework-native is not stated in the talk.
   - **Net:** one support point (protocol-level durability mandate + hard-client argument), one counter point (vendor-acknowledged non-adoption + convention-shaped delivery). This file deliberately leaves both pattern-less for the coin decision.
2. **Garbles.** "Agoric AI Foundation" → **Agentic AI Foundation** (`co-agentic-ai-foundation`, batch 9 — where MCP governance lives; corroborated by Angie Jones being named as its DevEx lead, matching her batch-9 affiliation). "MCPC task specification" → MCP Tasks specification; "fast MCP" → FastMCP; "Weave Works" → Weaveworks; "MCPUI" → MCP-UI; "locked launched" → launched; "dam demo gods" → demo gods. None affect entity identity.
3. **Cross-registry corroboration.** `exp-angie-jones` (batch 9, dual-affiliated co-agentic-ai-foundation + co-block) is independently confirmed here in the foundation role; the May stateless-restructure blog is hers. Also same-session adjacency: "they talked about MCP-UI two talks ago… they mentioned extensions" places this talk in the same block as the Salomon/Yosef MCP Apps talk (`ia-aie-salomon-yosef-mcp-apps`, published the same day) and corroborates the core+extensions restructure from a second, independent speaker set.
4. **Timing caveat on V2 claims.** At recording, the V2 spec was *forthcoming* ("a new one coming out in July") and Davis's account of it is second-hand via the May announcement plus her own prototype. The V1 failures are demonstrated; the V2 fixes are previewed. Weight accordingly before citing V2 details externally.
5. **Signal-bar caveat.** Single-vendor testimony plus a self-built demo; the strongest externally-checkable claims are the spec-text durability requirement and the V1→V2 protocol diff, both verifiable against the public spec and the foundation blog. The "million tasks" scale framing is a thought experiment, not a deployment report.
6. **No pattern coined; no new-pattern candidate proposed** beyond the standing `pat-durable-execution` ledger movement in note 1.
