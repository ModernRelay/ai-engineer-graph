# SPIKE extraction — "Active Graph Agent Runtime (BabyAGI 4)" (Yohei Nakajima, Untapped Capital) — FOR REVIEW

Source transcript: `transcripts/nakajima-babyagi4-active-graph-runtime.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/khVX_BUnEwU — AI Engineer World's Fair, published 2026-07-22.
`stagingTimestamp` for the artifact and all signals: 2026-07-22 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-nakajima-active-graph` | Active Graph Agent Runtime — BabyAGI 4 (Yohei Nakajima, Untapped Capital — AI Engineer World's Fair) | youtube | https://youtu.be/khVX_BUnEwU |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-yohei-nakajima`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-yohei-nakajima` | Yohei Nakajima (creator of BabyAGI, March 2023; nine iterations since; GP at Untapped Capital plus a dedicated agent fund — "VC by day, builder by night"; investor in multiple agentic companies) | `AffiliatedWithCompany → co-untapped-capital` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-untapped-capital` | Untapped Capital | investor | Nakajima's VC fund; ActiveGraph itself is his personal open-source research project, so no DevelopedByCompany edge from the elements |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-activegraph` | ActiveGraph | framework | harness | Open-source, event-sourced graph runtime for auditable agents (BabyAGI 4). A single immutable typed event log — recording both what the agent does AND every change to the agent — is the ground truth; agent state is a graph projected from it. Behaviors subscribe to graph changes (subscriptions can be graph queries, e.g. claim-contradicts-claim) and emit events; LLMs never talk to each other, only through shared state; views = graph queries as context management; policies gate what may change autonomously vs via proposed patch vs human-in-the-loop; packs bundle object schemas, tools, behaviors, and pack policies into modular harnesses (core/tool/secret/memory/identity/communication/chat), loadable across repos. Replay, rollback, and forks come natively. Explicitly "not a harness — a runtime": common harnesses (e.g. ReAct) can be rebuilt on top |
| `el-babyagi` | BabyAGI | framework | harness | Nakajima's March-2023 autonomous-agent experiment that went viral ("people thought it was going to work; it didn't work at all"); nine lower-fanfare iterations over three-plus years, usually themed on self-improvement — "build the simplest thing that can build itself." ActiveGraph is the fourth major generation |
| `el-experiential-world-model` | Experiential world model | concept | context | Nakajima's hypothesis: long-running agents need not just a predictive world model (the priors) but an experiential one — an immutable event log of lived experience that projects current state and feeds back into the priors via replays/dreaming/sleep (hippocampus analogy). The agent's identity — beliefs, knowledge, behaviors — derives from its own log, not from its reasoning capability |
| `el-blackboard-architecture` | Blackboard architecture | concept | harness | Classic 1970s–80s AI architecture (Kafka its modern descendant): many slim workers communicating only through shared state, never directly. Historically limited because it was unintuitive for humans to write and workers had to stay slim/deterministic — both constraints lifted now that AI writes the code and workers have reasoning capability |

Element edges: `el-activegraph` `UsesElement → el-blackboard-architecture`, `UsesElement → el-agent-session-log` **[registry]**, `ExemplifiesPattern → pat-context-graphs` **[registry]**; all four `IdentifiedInArtifact → ia-aie-nakajima-active-graph`.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-nakajima-active-graph`, `SourcedFromSource → source-aie-yt` **[registry]**. Domain `harness` except where noted.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-babyagi4-activegraph-runtime` | BabyAGI's creator ships ActiveGraph, inverting agent construction: instead of building around the LLM (responses API + tools + memory + logging bolted on), build around the log — what the agent does and how the agent changes, flattened into one immutable typed event log that projects the agent's state as a graph; replay/rollback/fork native; paper title: "the log is the agent" | `FormsPattern → pat-context-graphs` **[registry]** | `OnElement → el-activegraph`, `el-agent-session-log` **[registry]** |
| `sig-activegraph-longrun-resume` | Durability came free: an API key died ~question 350 of a 500-question LongMemEval run; on restart ActiveGraph rolled back one event and resumed at 353 — vs. the usual experience of rerunning long agents from the beginning. "No more starting long runs over" listed among the pleasant surprises | `FormsPattern → pat-harness-over-model` **[registry]** (parked — see note 3) | `OnElement → el-activegraph` |
| `sig-log-as-memory-longmemeval` | Experiment: the structured event log itself as memory — embed the query, find relevant messages, grab neighbors before/after; no semantic ingestion, no fact or entity extraction — did "pretty well" on LongMemEval. Much of what memory stores overlaps the log anyway; keeping them the same structure prevents divergence (semantic-ingestion add-ons improved the score only modestly). Domain: `context` | `FormsPattern → pat-context-graphs` **[registry]** | `OnElement → el-activegraph`, `el-agent-session-log` **[registry]** |
| `sig-gated-self-modification-works` | Controlled self-modification produced measured gains: the Regimes project classified each failure type and only unlocked the matching part of the agent for editing; the agent forks itself, proposes a patch, passes a static gate, a sandbox gate, and an eval-delta check on held-out questions, and only improving patches land (4–5 accepted of 8–13 proposed; statistically significant LongMemEval improvement). Same loop on a Pokémon TCG Kaggle competition: ~80 passes, ~20–30 accepted, each justified by ~200 simulated games + win-rate/Wilson-score criteria, Elo slowly climbing — and the policy forces a durable record of what did NOT work | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-activegraph` |
| `sig-activegraph-lab-self-research` | ActiveGraph Lab — an agent that reads all the project's blog posts and repos, proposes new experiments, asks permission, runs them, and writes them up — found an error in its own code, asked to fix it, wrote the PR (merged), and independently discovered that packs are modular between repos ("I didn't know that") — early but self-improving | `FormsPattern → pat-accelerated-research` **[registry seed]** | `OnElement → el-activegraph` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-harness-wont-disappear-experiential` | Against "as models get better, the harness disappears": predictive world model (priors) and experiential world model (the event log) are complements, not stages — like humans, an agent is not its reasoning capability but the beliefs, knowledge, and behaviors derived from lived experience, with the log feeding priors through replay/sleep. The agent's identity lives in its own log; we need both | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-experiential-world-model`, `el-agent-session-log` **[registry]** |
| `ins-training-data-favors-blackboard` | AI seems better at architecting event-sourced/blackboard-style agents than LLM-centric ones — hypothesis: decades of Kafka/blackboard shared-state distributed-systems literature sit in the training data vs. ~3 years of LLM-agent lore. Corollary: architectures too unintuitive for humans to hand-write ("I would never write code myself with ActiveGraph") become viable when AI writes the code and the micro-workers can reason | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-blackboard-architecture` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-nakajima-active-graph`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-around-the-log` | Build the agent around the log, not the LLM | Flatten what-the-agent-does and every change-to-the-agent into one immutable typed event log; never edit the graph — only emit events; project state (e.g. the current master prompt) from the log; implement logic as behaviors subscribed to graph changes, including graph-query subscriptions (on object created, if type is claim and it contradicts another claim → trigger contradiction detector) and relation behaviors on edges (research done → unblock write-memo); do context management as views — a graph query selecting the subset visible to a behavior; encode change control as policies (auto-add research sources; proposed-patch for prompt edits; contradiction checks or human-in-the-loop for facts); ship capabilities as packs and compose them into agents | `ReferencesElement → el-activegraph`, `ReferencesElement → el-agent-session-log` **[registry]** |
| `how-gate-agent-self-modification` | Let agents self-modify only through gated, measured proposals | Classify the failure type first and scope which part of the agent that class may edit; fork the agent → propose the patch → static gate check → sandbox gate check → measure eval delta on a held-out set; accept only statistically supported improvements (e.g. win-rate lift with Wilson score above threshold across ~200 simulations); record rejected experiments so the agent retains negative knowledge — the difference from YOLO self-modification is that failed attempts stay queryable | `ReferencesElement → el-activegraph` |

## Dropped

- Instagraph and Mindgraph — named only as pre-GraphRAG lineage ("code graphs, function graphs, log graphs"); prose in expert framing, no nodes (see note 1 re: `el-nanograph`).
- Replit and Claude Code as the coding agents used to build on ActiveGraph (also "Claude Code called it Régime de Cène" — spelling unverifiable); tool mentions, kept as prose. `co-replit` / `el-claude-code` **[registry]** not edged — incidental.
- OpenClaw / Hermes name-drops ("how do we get this closer to an OpenClaw or Hermes") — the aspiration behind ActiveGraph packs; `el-openclaw` / `el-hermes-agent` **[registry seed]** not edged; noted for central cross-linking.
- LangSmith comparison ("you can do this with LangSmith — thing is, I didn't have to think about it") — prose only.
- Kaggle Pokémon competition mechanics beyond what the self-modification signal needs.

## Review notes

1. **`el-nanograph` [seed] check (per task instruction):** the talk does NOT mention nanograph. Nakajima names his earlier graph projects as **Instagraph and Mindgraph**. The seed brief for `el-nanograph` (schema-first embedded property graph, Rust, SPIKE ontology, "SQLite for graphs") does not look like a Nakajima project — no edge added; confirm centrally whether the seed node is his or an unrelated project.
2. **"The log is the agent" convergence:** Nakajima says his first arxiv paper carries that exact title — which is also the title/thesis of the batch-9 Sehgal/Omnara talk (`ia-aie-sehgal-log-is-agent`, `el-agent-session-log`). ActiveGraph is a runtime embodiment of the same thesis, so `el-agent-session-log` is REUSED rather than coining a duplicate log-centric concept. Citation direction between Nakajima's paper and Omnara unknown from the transcripts — flag for central cross-linking (possible `el-omnara-managed-agents` ↔ `el-activegraph` relation).
3. `pat-durable-execution` candidate (NOT coined): `sig-activegraph-longrun-resume` is another clean data point (rollback-one-event-and-resume on a 500-question run). Parked on `pat-harness-over-model` per registry convention; rehome if the pattern is coined.
4. `pat-adaptive-harness` / `pat-adaptive-software` candidate (NOT coined): the task brief flagged that BabyAGI 4's "active graph runtime" may resonate — it does, twice: (a) harnesses are rebuilt as packs ON a runtime, i.e. harness as composition rather than fixed artifact; (b) `sig-gated-self-modification-works` is agents rewriting themselves under policy gates. Both noted as candidate evidence; `sig-gated-self-modification-works` rehomes if coined (currently on `pat-verification-gap`, which is also genuinely load-bearing — the gates ARE verification).
5. **Candidate "persistent agent memory as a first-class stack layer" (NOT coined):** this talk adds an inverse-variant data point — `sig-log-as-memory-longmemeval` argues memory should be UNIFIED with the runtime log rather than built as a separate store, and `el-experiential-world-model` gives the layer a cognitive-science framing (log → replay/sleep → priors; resonates with `el-agent-sleep-cycle` **[registry, batch 6]**, no edge). Left for central decision.
6. Both insights highlight `pat-harness-over-model`: deliberate — this talk is a direct pro-harness engagement ("some discussions suggest the harness disappears as models get better; I'm starting to think that's not true"), a counterweight to the three ContradictsPattern edges from batches 6–7.
7. Caption garbles resolved: "AI engineer warfare" = World's Fair; "ActoGraph"/"Auto graph"/"Actigraph"/"active graph" = ActiveGraph; "Pox" = packs; "no cloud code" read as "Claude Code" (with Replit) per surrounding context; "Regime de Scene" left unresolved (Claude Code's nickname for the Regimes project). Whether the official project spelling is "ActiveGraph" or "Active Graph" — verify against the repo before seeding.
8. Untapped Capital plus "an agent fund" — the second fund is unnamed in the talk; only `co-untapped-capital` coined.
