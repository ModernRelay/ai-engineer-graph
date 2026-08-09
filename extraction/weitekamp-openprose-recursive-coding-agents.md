# SPIKE extraction — "Recursive Coding Agents" (Raymond Weitekamp, OpenProse) — FOR REVIEW

Source transcript: `transcripts/weitekamp-openprose-recursive-coding-agents.txt` (auto-captions — quotes are paraphrases, not verbatim; captions garble the speaker as "Raymond Whitcomb" — official listing: Weitekamp).
Video: https://youtu.be/3hXJI2q0Jz8 — AI Engineer World's Fair, published 2026-06-25.
`stagingTimestamp` for the artifact and all signals: 2026-06-25 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-weitekamp-recursive-agents` | Recursive Coding Agents (Raymond Weitekamp, OpenProse — AI Engineer World's Fair) | youtube | https://youtu.be/3hXJI2q0Jz8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-raymond-weitekamp`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-raymond-weitekamp` | Raymond Weitekamp (OpenProse; independent RLM research under "raw works"; benchmark results applying RLMs to long-reasoning tasks) | `AffiliatedWithCompany → co-openprose` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-openprose` | OpenProse | developer | Company behind the OpenProse language and its coding-agent harness (open source) |
| `co-symbolica` | Symbolica | research | Team behind the Agentica RLM harness that upended ARC-AGI-3. ⚠ Name per auto-captions — plausibly Symbolica AI, unverified; check before seeding |

## Elements (6 new)

All new elements `IdentifiedInArtifact → ia-aie-weitekamp-recursive-agents`.

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-recursive-coding-agents` | Recursive coding agents | concept | harness | Applying RLM principles to coding agents: the harness can invoke itself/sub-agents to a settable depth, with the model choosing the decomposition. Rubric for "is it an RLM": executable environment; prompt externalized as a variable (file/files); code is the thing calling the model; the model picks the decomposition into sub-calls; state stays symbolic. Hard-coded map-reduces (e.g., lambda-RLM) fail the rubric — decomposition isn't model-chosen |
| `el-openprose` | OpenProse | framework | harness | Open-source "programming language" compiled by your coding agent rather than your computer — a markdown / logical-English spec (`.prose.md`); explicitly declares sub-agent work, wires skills and CLI tools in as dependencies so sub-agents are provably equipped, and verifies sub-agent output in the parent session; turns any coding agent with a filesystem + sub-agents into an RLM; `prose write` has the agent author the program; harness executes over Codex SDK or Claude Code |
| `el-claude-dynamic-workflows` | Claude Code dynamic workflows | technology | harness | Claude Code capability (released weeks before the talk; Anthropic's "A Harness for Every Task" post shows six workflow patterns) that lets the agent generate and run recursive, model-chosen workflows — the change that made RLM co-author Omar Khattab publicly declare Claude Code "finally an RLM" |
| `el-agentica` | Agentica | product | harness | Symbolica's RLM agent harness; scored ~30% on ARC-AGI-3 within hours of the benchmark's release while frontier models sat at 2–3%. ⚠ Both product and company names per auto-captions — verify |
| `el-dspy` | DSPy | framework | harness | Declarative LM-programming framework; its `dspy.RLM` implementation is the reference home of recursive language models and the speaker's go-to for benchmarking (source of his state-of-the-art long-reasoning results) |
| `el-pi-coding-agent` | Pi coding agent | product | harness | Minimal, deliberately extension-first open-source coding agent (creator captioned only as "Mario" — Mario Zechner per public record, ⚠ verify); its evolved extension API now supports full self-recursion as a pure extension (pi-recursive, with the Y-pi convenience wrapper): "pi calls pi calls pi," depth settable |

Element edges: `el-recursive-coding-agents` `UsesElement → el-recursive-language-models` **[registry]**; `el-openprose` `DevelopedByCompany → co-openprose`, `EnablesElement → el-recursive-coding-agents`; `el-claude-dynamic-workflows` `DevelopedByCompany → co-anthropic` **[registry]**, `EnablesElement → el-recursive-coding-agents`; `el-agentica` `DevelopedByCompany → co-symbolica`, `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

Registry elements referenced (edges only, no new nodes): `el-recursive-language-models` (defined in batch 5, `shashi-rlm-codebases`), `el-claude-code`, `el-codex`.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-weitekamp-recursive-agents`, `SourcedFromSource → source-aie-yt` **[registry]**, domain `harness`.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-rlm-small-beats-frontier` | On the LongCoT long-reasoning benchmark, a small laptop-runnable open model (captioned "Qwen 3.59B") run as an RLM beats Opus and GPT-5.4 run as plain LLMs; RLMs also process inputs orders of magnitude beyond their context window (tens of millions of tokens), and the unmodified RLM harness ranks around top-10 as a memory system against purpose-built (billion-dollar-funded) memory products | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-recursive-language-models` **[registry]**, `el-dspy` |
| `sig-arc-agi3-too-hot-to-benchmark` | Within hours of ARC-AGI-3's release, Symbolica's Agentica RLM harness posted ~30% vs ~2–3% for all frontier models; the ARC Prize team declined to run the full private evaluation (a "consolation tweet" — "you didn't solve the problem the right way"), and LongCoT maintainers were pushed by the speaker and the RLM first author to stand up a separate open-harness leaderboard — harness results are outrunning benchmark governance | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-agentica`; `RelevantCompany → co-symbolica` |
| `sig-mismanaged-geniuses` | Thesis signal: today's agents are "mismanaged geniuses" (framing from Alex Zhang / Omar Khattab, MIT — the RLM authors): intelligence is sufficient, and the missing layer is how work is specified, managed, reused, and verified. Lived whiplash as evidence: a near-working SaaS app from a single prompt one day; Claude Code emptying his Solana wallet the next | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-claude-code` **[registry]** |
| `sig-claude-code-becomes-rlm` | Claude Code's dynamic workflows made the most-used coding agent capable of recursive, model-chosen decomposition; RLM co-author Omar Khattab publicly conceded Claude Code is "finally an RLM" — frontier harnesses are converging on recursion as a first-class primitive | — (pattern-less; see review notes) | `OnElement → el-claude-dynamic-workflows`, `el-claude-code` **[registry]**; `RelevantCompany → co-anthropic` **[registry]** |
| `sig-golden-session-capture` | OpenProse can take a "golden session" (an unusually good agent run) from Claude Code, Codex, or Pi and have the agent deconstruct it into a reusable `.prose.md` workflow — converting a lucky great run into a repeatable program, recursive sub-agent structure included | — (pattern-less; see review notes) | `OnElement → el-openprose` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-recursion-unifies-tools-and-reasoning` | RLMs are the next test-time-compute paradigm because they merge the two prior scaling moves — chain-of-thought/reasoning tokens and (parallel) tool calling — into one mechanism: reasoning BY executing code whose calls include sub-agents/sub-RLMs; whether cognition lives in latent space, reasoning tokens, or code execution is irrelevant next to results | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-recursive-language-models` **[registry]** |
| `ins-trust-is-reliability-not-iq` | Trust in agents is gated by reliability, not intelligence: the next capability step is behavioral — orchestration, specification, reuse, verification — which is why recursive structure (model-chosen decomposition + declared dependencies + parent-session verification) matters more than a smarter base model | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-recursive-coding-agents` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-weitekamp-recursive-agents`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-rlmify-coding-agent` | Three routes to make a coding agent recursive | (1) Cheapest: wrap an RLM as a CLI tool the agent can call when a task exceeds context (e.g., sifting a 100M-token corpus). (2) On Claude Code: use dynamic workflows — study the six patterns in "A Harness for Every Task," and know the difference between a hard-coded map-reduce workflow and a true RLM workflow where the model picks the decomposition. (3) Harness-agnostic: write a `.prose.md` program — declare the sub-agent decomposition, wire skills/CLI tools in as explicit dependencies so each sub-agent is provably equipped, verify sub-agent output in the parent session. Set recursion depth deliberately — "recurse responsibly" | `ReferencesElement → el-openprose`, `el-claude-dynamic-workflows`, `el-recursive-coding-agents` |
| `how-golden-session-to-program` | Turn golden sessions into reusable programs | When an agent has a great run, have the agent deconstruct that session into a Prose workflow that reproduces the golden path on demand, portable across harnesses (Claude Code, Codex, Pi); apply the same recursive patterns to repo-scale swarm migrations (fan out, then merge), recursive deep research/analysis over directories, audits and bug sweeps, and adversarial sets (skeptical or red-team agents improving the system) | `ReferencesElement → el-openprose` |

## Dropped

- Unix RLM (by "Dan at OpenProse" — pure bash; the REPL/environment is just the Linux filesystem) and AXE (TypeScript DSPy variation whose agents write TypeScript interfaces to other AXE agents — possibly the real "Ax" library, ⚠ garble) — single-mention showcases; prose only.
- lambda-RLM — named only as the close-but-no-cigar hard-coded map-reduce example; folded into `el-recursive-coding-agents` brief.
- Y-pi / pi-recursive package names — folded into `el-pi-coding-agent` brief.
- recursivecodingagents.com (the slides are a website), the companion GitHub repo, and his Turing Post articles — kept as prose; no separate artifact nodes.
- MIT RLM authors (Omar Khattab, Alex Zhang) as Expert nodes — see review note 4.
- "OOLONG"-like benchmark name from the original paper (captioned "U Long") — unresolved; not an entity.

## Review notes

1. **`pat-adaptive-harness` / `pat-adaptive-software` candidate (NOT coined, per instruction) — specifics for the ledger:** three mechanism-level data points here: (a) dynamic workflows make the harness a *runtime output* — the agent writes and runs its own workflow; (b) `prose write` is the agent authoring its own program spec; (c) golden-session deconstruction extracts harness structure from observed behavior after the fact. Together with Chandegra's "harness as runtime output, not input" (batch 7) this is the clearest mechanism evidence yet for `pat-adaptive-harness`. `sig-claude-code-becomes-rlm` and `sig-golden-session-capture` were deliberately left pattern-less so they can be rehomed if the pattern is coined.
2. **`pat-benchmark-trust-crisis` candidate (NOT coined):** `sig-arc-agi3-too-hot-to-benchmark` adds a new flavor to the ledger — not reward hacking but *governance strain*: leaderboards refusing or segregating harness-based results (ARC Prize private-eval refusal; LongCoT open-harness split). Sits alongside the Han/Vidal/Robinson/Desai data points.
3. **`pat-durable-execution`: deliberately NOT counted** — recursion here is about decomposition and reuse, not durable state; excluded from that ledger.
4. Omar Khattab and Alex Zhang (MIT; captions garble them as "Alex Zeng, Z Li, and Omar Khattab") are the intellectual source of RLMs and recur throughout, but no edge type fits a citation (they didn't contribute to this artifact) — not coined. Precedent either way: `exp-karpathy` exists as a cited-researcher node; coin centrally if wanted.
5. Garbles: speaker "Whitcomb" → Weitekamp (official listing); "Cloud Code" → Claude Code throughout; "Qwen 3.59B" unresolved (Qwen 3.5-9B? Qwen3 ~4B/9B?) — kept as-captioned in the signal with flag; "GPT-5.4" as captioned; "ArcadeGI" → ARC-AGI; "pie"/"Y pie" → Pi/Y-pi; "AI engineer code, November 2025" ≈ AI Engineer CODE conference (the "meditate while agents manifest" progression is from the event t-shirt).
6. `el-dspy` coined without a `DevelopedByCompany` edge — open-source with academic lineage (Khattab); add centrally if a lab/university node is preferred. `el-agentica`/`co-symbolica` both carry verification flags — if Symbolica can't be confirmed, fold both into prose inside `sig-arc-agi3-too-hot-to-benchmark`.
7. Same-batch resonance: this talk and Graziano's `agents-building-agents` independently argue the orchestration/management layer (not intelligence) is the frontier — both feed `pat-model-not-bottleneck` and `pat-harness-over-model` rather than any new pattern.
