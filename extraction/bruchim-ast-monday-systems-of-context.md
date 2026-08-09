# SPIKE extraction — "From Systems of Record to Systems of Context" (Omri Bruchim & Tomer Ast, monday.com) — FOR REVIEW

Source transcript: `transcripts/bruchim-ast-monday-systems-of-context.txt` (auto-captions — quotes are paraphrases, not verbatim; speaker names heavily garbled, see notes).
Video: https://youtu.be/Btk8wDUVs74 — AI Engineer World's Fair, published 2026-07-22.
`stagingTimestamp` for the artifact and all signals: 2026-07-22 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-bruchim-ast-systems-of-context` | From Systems of Record to Systems of Context (Omri Bruchim & Tomer Ast, monday.com — AI Engineer World's Fair) | youtube | https://youtu.be/Btk8wDUVs74 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-omri-bruchim`, `ContributedByExpert → exp-tomer-ast`.

## Experts (2 new)

| slug | name | edges |
|---|---|---|
| `exp-omri-bruchim` | Omri Bruchim (engineering manager, monday.com; works on Sidekick / the Monday world model) | `AffiliatedWithCompany → co-monday` |
| `exp-tomer-ast` | Tomer Ast (engineering manager, monday.com; presented the data-model / dual-engine architecture) | `AffiliatedWithCompany → co-monday` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-monday` | monday.com | developer | global work-platform SaaS (hundreds of thousands of teams) repositioning itself as a system of context; four AI bets: Sidekick, Vibe (build-your-own software), custom agents, workflows |

## Elements (3 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-monday-sidekick` | Monday Sidekick | product | context | monday.com's AI personal work assistant ("a bird on your shoulder"): knows the user and their business, thinks and executes with them, keeps the user in control; the consumer of the Monday world model |
| `el-monday-world-model` | Monday world model | technology | context | Precomputed per-user work-context model built from cross-tool "breadcrumbs" (boards, tasks, emails, Slack, calendar, meeting transcripts): (1) how the user's work is structured — entities, dependencies, who blocks whom; (2) a live-signal snapshot — what's overdue/urgent, active collaborators; (3) a durable learned profile — persona, routines, goals. Explicitly "not a bigger prompt, not a longer context window" |
| `el-fast-slow-context-engines` | Fast/slow context engines | concept | context | Dual-timescale context construction: a slow engine mines weeks of activity into a durable, reinforcement-updated user profile ("knows you"); a fast engine recomputes live signals over a short recent window ("knows your day"); merged into one served view. Deliberate analog of complementary learning systems (hippocampus/neocortex) in neuroscience and lambda architecture (speed/batch layers) in data infrastructure |

Element edges: all three `IdentifiedInArtifact → ia-aie-bruchim-ast-systems-of-context`; `el-monday-sidekick` and `el-monday-world-model` `DevelopedByCompany → co-monday`; `el-monday-sidekick` `UsesElement → el-monday-world-model`; `el-monday-world-model` `UsesElement → el-fast-slow-context-engines`; `el-monday-world-model` `EnablesPattern → pat-context-graphs` **[registry]**.

## Signals (4 new)

All: domain `context`, `SpottedInArtifact → ia-aie-bruchim-ast-systems-of-context`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-monday-systems-of-context` | monday.com — a work-platform incumbent — is publicly repositioning from system of record to system of context: software that understands connections between records rather than just storing them, with four platform bets (Sidekick assistant, Vibe app-building, custom agents, deterministic workflows) | `FormsPattern → pat-saaspocalypse` **[registry]** | `RelevantCompany → co-monday` |
| `sig-agent-gap-what-to-focus` | The "what should I focus on right now?" test: agents (Gemini/GPT/Claude) with access to all boards, emails, Slack, and memory still return disconnected generic bullets — sharp at executing a known task (draft the escalation reply), lost at finding the problem; "all the data, zero understanding"; memory doesn't fix it — the speakers call this the agent gap | `FormsPattern → pat-context-graphs` **[registry]** | — |
| `sig-world-model-precomputed-offline` | Monday builds the world model offline, ahead of any question — meaning "can't be built at runtime the moment someone asks"; serve-time recomputes only a thin slice over recent activity and verifies part of the context against live data, falling back to last-verified context (degrades gracefully); sources are isolated so a bad feed can't break the rest; adding a source is deliberately cheap and additive, so the model compounds daily | `FormsPattern → pat-context-graphs` **[registry]** | `RelevantCompany → co-monday` |
| `sig-dual-engine-convergence` | The fast/slow engine split was independently arrived at by two unrelated fields — complementary learning systems in neuroscience (hippocampus captures instantly, neocortex distills durable lessons) and lambda architecture in data processing (speed layer + recomputed batch layer merged into one served view) — and monday.com applies the same split to an agent's data model | `FormsPattern → pat-context-graphs` **[registry]** | `RelevantCompany → co-monday` |

Additional signal edges: `sig-agent-gap-what-to-focus` `OnElement → el-monday-world-model`; `sig-dual-engine-convergence` `OnElement → el-fast-slow-context-engines`.

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-understanding-not-retrieval` | The bottleneck was never data access or retrieval — assistants already have every board, message, and email. Retrieval and understanding are two different problems almost everyone conflates; the missing piece is how entities connect to each other, and no amount of connectors, MCPs, or context-window growth supplies it | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-monday-world-model` |
| `ins-context-precomputed-ahead` | Understanding has to be built ahead of time: by the moment a user asks the question, it is too late to construct meaning at runtime. The architecture consequence is precomputation on two timescales, with only a thin verification slice at serve time — the opposite of query-time RAG | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-fast-slow-context-engines` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-bruchim-ast-systems-of-context`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-dual-engine-context-model` | Build agent context as two engines on different clocks | Collect breadcrumbs from everywhere the user works (boards, email, Slack, calendar, meeting transcripts). Slow engine: mine weeks of activity for persona, routines, collaborators, goals; distill into a durable profile; reinforce it every time it holds. Fast engine: recompute live signals (overdue, suddenly urgent, active collaborators) over a short recent window, updated frequently. Precompute both offline; at serve time recompute only a thin slice and verify part of the context against live data, falling back to last-verified. Isolate sources so a bad feed can't break the rest; make adding a source cheap and purely additive | `ReferencesElement → el-fast-slow-context-engines`, `ReferencesElement → el-monday-world-model` |

## Dropped

- "SDR agent that calls your prospects", finance/marketing research agents — product-vision listing, no load-bearing content; prose only.
- Monday Vibe / Monday agents / Monday workflows as Element nodes — named once as the other three bets; kept inside `sig-monday-systems-of-context`.
- The git-blame → PR → Monday-board provenance analogy — illustration of records-without-meaning; folded into prose.
- Speakers' own caveats (model trails the live world, cold-start users, signal bias, important-vs-noise is hardest) — kept as description material, not separate nodes.

## Review notes

1. **Caption garbles (resolved):** "Tormer / Tor / Thomas" → Tomer Ast; "psychic / Psyche" → Sidekick (official product name); "Monday word model" → Monday world model; "NSDR agent" → read as "an SDR agent". Unresolved: the demo profile line "combin is an engineering manager" (garbled first name). Speaker attribution between Bruchim and Ast is approximate — Ast presents the data-model/engines mid-section.
2. **Merge-check at seeding:** `el-monday-world-model` vs batch-9 `el-company-world-model` and batch-3 `el-company-brain` / batch-6 `el-brain-os`. Kept distinct: Monday's is per-user work context (persona + live day), not an org-level brain.
3. **Pattern candidate evidence (NOT coined, no edges):** "persistent agent memory as a first-class stack layer" (batch-9 three-talk candidate) gains a fourth, vendor-productized data point — the durable reinforced profile plus compounding precomputed context layer is exactly that thesis. Soft resonance with `pat-harness-over-model` ("not a bigger prompt... a totally different thing") left as prose.
4. `sig-monday-systems-of-context → pat-saaspocalypse` reads the pivot as incumbent-response evidence (record-keeping SaaS rebuilding as a context platform to stay relevant). If you want saaspocalypse reserved for disruption-side signals, rehome to `pat-context-graphs`.
