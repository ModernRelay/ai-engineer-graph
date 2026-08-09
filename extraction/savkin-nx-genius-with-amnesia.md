# SPIKE extraction — "A Genius With Amnesia" (Victor Savkin, Nx) — FOR REVIEW

Source transcript: `transcripts/savkin-nx-genius-with-amnesia.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/jVjt-2g8NMY — AI Engineer World's Fair, published 2026-06-26.
`stagingTimestamp` for the artifact and all signals: 2026-06-26 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

Context: the "genius with amnesia" framing — a genie grants you John Carmack, but he can only see 1/1000 of your codebase and remembers nothing between conversations. That's an agent: constrained in space (repo-bound) and time (session amnesia). Nx's answer is Polygraph, an agent-agnostic meta-harness.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-savkin-genius-amnesia` | A Genius With Amnesia (Victor Savkin, Nx — AI Engineer World's Fair) | youtube | https://youtu.be/jVjt-2g8NMY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-victor-savkin`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-victor-savkin` | Victor Savkin (co-founder, Nx/Nrwl; presents Polygraph) ⚠ transcript says only "my name is Victor"; role from public record — verify | `AffiliatedWithCompany → co-nx` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-nx` | Nx | developer | monorepo/build-tooling company (Nx, by Nrwl); now shipping Polygraph, an agent-agnostic meta-harness for multi-repo agent work |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-polygraph` | Polygraph (Nx) | product | harness | Agent-agnostic meta-harness: analyzes every repo a GitHub user can reach (~300 owned + thousands of open-source dependencies in Savkin's own graph) without changing a line of code in them, extracting metadata into a unified dependency graph (what each project produces/consumes package-wise and API-wise); creates multi-repo sessions — one agent per repo, wired together, presented as "an illusion of one big code base" — with CI across the repos treated as one vector (routes a failure to whichever side needs the patch); captures intent, repos, PRs, and full agent traces per session so any session can be restored on any machine or referenced from anywhere; installed agents are interchangeable (Claude in the original session, Codex on resume, or swapped mid-session). Spoken URL: "try.poligraph.com" (⚠ spelling, Review note 2) |
| `el-org-work-graph` | Organizational work graph (repos × sessions) | concept | context | Savkin's mental model: at the bottom, the repository graph — every artifact your org produces plus every open-source repo you depend on (maybe 1,000 owned, tens of thousands OSS); at the top, all agentic sessions that create and modify that code; sessions relate to sessions, repos relate to repos, sessions attach to repos — "a faithful picture of the work in your organization: what's there at the bottom and how it came to be at the top". What agents actually see today is one session × one repo fraction × no memory |

Element edges: both `IdentifiedInArtifact → ia-aie-savkin-genius-amnesia`; `el-polygraph` `DevelopedByCompany → co-nx`; `el-polygraph` `UsesElement → el-org-work-graph`; `el-polygraph` `ExemplifiesPattern → pat-harness-over-model` **[registry]**; `el-org-work-graph` `EnablesPattern → pat-context-graphs` **[registry]**.

Registry element reuse (no new node, edge only): `el-meta-harness` **[registry]** `IdentifiedInArtifact → ia-aie-savkin-genius-amnesia` — Savkin independently describes Polygraph with the exact batch-7 term, "an agent-agnostic meta harness"; `el-semantic-episodic-memory` **[registry]** `IdentifiedInArtifact → ia-aie-savkin-genius-amnesia` — "the agent has no episodic memory; every session is a blank slate; the human becomes the memory"; `el-agent-checkpoint-replay` **[registry]** `IdentifiedInArtifact → ia-aie-savkin-genius-amnesia` — full session state materialized on another machine ("close to the transporter in Star Trek"); `el-claude-code` **[registry]** and `el-codex` **[registry]** `IdentifiedInArtifact → ia-aie-savkin-genius-amnesia` — the interchangeable agents in the demos (captions garble them "Cloat"/"Cortex", Review note 3).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-savkin-genius-amnesia`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-agents-space-time-constrained` | harness | Agents are constrained in space and time: repo-bound (see and change ~one repo at a time out of hundreds or thousands, never the whole system) and amnesiac (every session starts blank, so the human becomes the memory). Worked example: one logical UI change propagating through UI → module1 → module2 → platform → a week-later prod bugfix took seven re-explanations, often by different people; a 20-repo change means re-explaining 20 times — developer time and tokens burned. The capability is genius-level; the scaffolding is "deeply deficient" — equivalent to an engineer who can see one file and five messages back | `FormsPattern → pat-model-not-bottleneck` **[registry]** | — |
| `sig-nx-polygraph-multi-repo-sessions` | harness | Nx built Polygraph: metadata analysis over thousands of repos → unified dependency graph → multi-repo sessions that read/write anywhere, with per-repo agents wired together and cross-repo CI treated as one vector (when module1's CI fails, it works out whether module1 needs a patch or the upstream UI lib is broken and everyone needs one). Savkin notes other organizations he's talked to have converged on similar solutions — "look at the problem and the solution conceptually, not the specific tool" | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-nx` |
| `sig-session-transfer-cross-agent` | harness | Captured sessions are portable across machines, people, and agents: a coworker resumes the full session (same repos, same SHAs, agents primed with the captured traces) on a different machine with a *different* agent — Claude in the original, Codex on resume — because the state, not the agent, carries the memory; Savkin's own PR-review workflow is to resume the author's session and interrogate his agent about the decisions instead of asking the person; the same mechanism enables mid-session agent swaps and "reference this session, it's broken, fix it" bug reports that need zero extra explanation | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-nx` |
| `sig-org-hive-mind-memory` | context | Because session capture crosses developer boundaries, every developer's agent taps the whole organization's session history: ask "did anyone ever add a vector index to the PR collection?" and load the relevant prior sessions; replicate the approach of an engineer you respect so cross-repo code stays consistent instead of every implementation being bespoke; a thousand engineers' sessions are accessible to each of them — "almost like the Borg… one big hive mind", giving the agent more context than any single developer holds | `FormsPattern → pat-context-graphs` **[registry]** | `RelevantCompany → co-nx` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-space-time-are-harness-properties` | The two defining agent deficits — scope (repo boundary) and memory (session amnesia) — are properties of today's harness layer, not of the model, and both are liftable: a dependency graph lifts the space constraint, captured/replayable sessions lift the time constraint; the "genius" needs no upgrade, the lamp does | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-polygraph` |
| `ins-org-memory-beats-individual-memory` | Once agent memory is org-scoped rather than per-developer, the agent's usable context exceeds any individual's: prior sessions become retrievable precedent, best practices propagate by replaying respected engineers' work, and consistency emerges as a side effect — a company-brain effect assembled from work artifacts (repos + sessions) rather than from documents | `HighlightsPattern → pat-context-graphs` **[registry]** | `ReliesOnElement → el-org-work-graph`, `ReliesOnElement → el-company-brain` **[registry]** |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-savkin-genius-amnesia`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-multi-repo-change-as-one` | Treat a multi-repo change as one session | State the intent once; select repos by hand or let the dependency graph select them ("find every repo that depends on version X of this library and update it" — the graph knows); let the harness set up source, dependencies, and a correctly-wired agent per repo at the right SHAs; treat the resulting PRs + CI across repos as a single vector and route failures to whichever side actually needs the patch; capture traces so the session is resumable by anyone | `ReferencesElement → el-polygraph`, `ReferencesElement → el-org-work-graph` |
| `how-ingest-real-repo-not-docs` | Give agents the real dependency repo, not a docs lookup | When the agent must understand a dependency (e.g., writing a Vitest plugin inside the Nx repo), add the dependency's actual open-source repository to the session rather than querying a docs service (Savkin: "I much prefer this to Context7 — if I have the real code, the agent can go really deep; the deep problems are discovered this way") | `ReferencesElement → el-polygraph` |

## Dropped

- The genie / John Carmack framing and the Star Trek transporter and Borg analogies — rhetoric; kept only where they carry the claim (signals 3–4 prose).
- Context7 — named once as the docs-lookup foil in the knowhow; prose, not coined.
- Vitest / the three-repo demo workspace — demo material, prose.
- GUI/animation details of the Polygraph session view — product color.
- "One file at a time, five messages back" thought experiment — folded into `sig-agents-space-time-constrained`.

## Review notes

1. Savkin's role: the transcript only says "my name is Victor. You can follow me on Twitter"; co-founder of Nx (Nrwl) is from public record — verify before seeding.
2. Product URL spoken as "try.poligraph.com" — spelling unverified (Poligraph vs Polygraph; captions render the product "Polygraph" throughout). Verify the domain before public-facing use.
3. Caption garbles "Cloat" and "Cortex" resolved to Claude and Codex — confirmed by the later explicit "switch from say Claude to Codex mid-session".
4. `el-meta-harness` **[registry, batch 7]**: Savkin's own words ("agent-agnostic meta harness") independently reproduce the Chandegra-batch concept — second independent data point for that element; edge added `IdentifiedInArtifact` only, no redefinition.
5. Candidate pattern (NOT coined, no edges): "persistent agent memory as a first-class stack layer" — this talk is the second same-batch data point alongside `iusztin-bouchard-notes-into-memory` and `pankaj-starlight-retrieval-boundary` (see note 6 in the iusztin-bouchard file). Savkin adds the org-scale variant (cross-developer session memory).
6. `sig-agents-space-time-constrained` double-reads: it also supports `pat-harness-over-model`; parked on `pat-model-not-bottleneck` per the registry's industry-vs-engineering split — the signal states where the deficit lives (around a capable model), while signals 2–3 carry the engineering-solution reading.
7. Scale figures (1/1000 of the codebase, ~300 owned repos, "maybe a thousand repos you own") are Savkin's illustrative magnitudes, not measurements — kept as prose inside briefs.
8. `sig-org-hive-mind-memory` is adjacent to `el-company-brain` **[registry, batch 3]**; the insight edge records the connection rather than coining a duplicate concept.
