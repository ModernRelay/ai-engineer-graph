# SPIKE extraction — "What if the harness mattered more than the model?" (Aditya Bhargava, Etsy) — FOR REVIEW

Source transcript: `transcripts/bhargava-etsy-harness-over-model.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/2e9ANoOEn28 — AI Engineer World's Fair, published 2026-07-07.
`stagingTimestamp` for the artifact and all signals: 2026-07-07 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

Context: the talk title is, verbatim, the registry pattern `pat-harness-over-model` — this file treats that as direct titular evidence (see Review notes 1). Live-coded talk: seven iterations of one coding agent in the speaker's own agent language, Agency.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-bhargava-harness-over-model` | What if the harness mattered more than the model? (Aditya Bhargava, Etsy — AI Engineer World's Fair) | youtube | https://youtu.be/2e9ANoOEn28 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-aditya-bhargava`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-aditya-bhargava` | Aditya Bhargava (staff engineer at Etsy; Etsy's IC initiative lead for agentic commerce; author of *Grokking Algorithms*; illustrated posts at ducktyped.org; creator of the Agency language) | `AffiliatedWithCompany → co-etsy` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-etsy` | Etsy | developer | e-commerce marketplace; appears here as the speaker's employer (agentic-commerce initiative), not as the builder of Agency — enum has no commerce/enterprise type, `developer` chosen |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agency-lang` | Agency (agent language) | framework | harness | TypeScript-like language for building agents (agencylang.com; ~6 months old, built by Bhargava as personal research): every function is automatically a tool (JSON schema from the signature, docstring as description); interrupts are first-class pausable/resumable execution — raise one inside a for-loop/tool-call/sub-agent, serialize the run, resume a week later at that exact point; partial function application locks tool arguments away from the LLM; sub-agents are plain functions; built-in prompt optimizers (mark variables `optimize`, give a goal, measure against a baseline); stdlib includes read/write/search tools where every mutating or sensitive action throws an interrupt by default |
| `el-harness-bench` | HarnessBench | technology | harness | Benchmark for harnesses cited by Bhargava from a recent paper: 106 tasks, same model + same evaluation, only the harness varies; reported scores range 52.4%–76.2% — a >20-point spread from harness choice alone — and the harness effect is larger for weaker models (name per captions; verify paper identity before public use) |

Element edges: both `IdentifiedInArtifact → ia-aie-bhargava-harness-over-model`; both `ExemplifiesPattern → pat-harness-over-model` **[registry]**. `el-agency-lang` deliberately has **no** `DevelopedByCompany` edge — it is Bhargava's personal project, not Etsy's.

## Signals (3 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-bhargava-harness-over-model`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-harnessbench-20pt-spread` | HarnessBench evidence: same model, same 106-task evaluation, only the harness changed → resolution ranges 52.4% to 76.2% (>20 points), with the harness mattering more the weaker the model — quantitative support that harness choice moves agent performance as much as a model-generation jump | `FormsPattern → pat-harness-over-model` **[registry]** | — |
| `sig-harness-for-local-models` | Etsy staff engineer pushes back on the emerging industry wisdom "models are so good, keep the harness simple, give it a few tools" — arguing it deepens dependence on fancy proprietary hosted models; the counter-program: build harnesses good enough that local open-source models reach cutting-edge task performance, which "any of us can do" without depending on paid models | `FormsPattern → pat-harness-over-model` **[registry]**, `FormsPattern → pat-sovereign-ai` **[registry]** | `RelevantCompany → co-etsy` |
| `sig-agency-language-level-harness` | Claim: building a really good harness requires *language-level* support — existing tools/frameworks couldn't do it, so Bhargava spent 6 months building Agency, whose load-bearing features (functions-as-tools, serializable pause/resume interrupts, partial function application, sub-agents as functions, built-in optimizers) are all harness primitives, not model features | `FormsPattern → pat-harness-over-model` **[registry]** | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-harness-quality-is-sovereignty` | If harness quality can substitute for model quality (HarnessBench's 20-point spread, largest for weak models), the industry's dependency structure flips: cutting-edge agent performance stops being gated on a handful of frontier labs, and local/open-source models become viable for serious agent work — harness expertise is the sovereignty lever | `HighlightsPattern → pat-harness-over-model` **[registry]**, `HighlightsPattern → pat-sovereign-ai` **[registry]** | `ReliesOnElement → el-harness-bench` |
| `ins-safety-is-a-harness-property` | Agent capability and agent safety are the same design problem, solved in the harness: the goal is *just enough* capability to act autonomously without destructive reach — approval handlers where humans must stay in the loop, argument-locking (partial function application) where they shouldn't have to be; none of it lives in the model | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-agency-lang` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-bhargava-harness-over-model`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-harness-improvement-ladder` | Climb the harness ladder, one rung at a time | Model alone (can't touch files) → add tools (functions-as-tools) → add safety (interrupt handlers; human approves destructive/sensitive calls) → trade approval for constraint (partial function application: safe *and* autonomous) → add reasoning (ReAct loop: read files, run tests, observe failure, edit, re-run to green — the stage where the agent first actually fixes the bug) → add sub-agents for more capability without context bloat → finish with self-optimization (optimizer + goal, e.g. "fix the bug in median.py using TDD") so improvement is measured, not guess-and-check | `ReferencesElement → el-agency-lang` |
| `how-pfa-tool-constraint` | Lock dangerous tool arguments with partial function application | Partially apply the risky parameter (e.g. lock `read`/`write` to one directory) before passing the function as a tool: the LLM never sees the locked argument in the schema, so the agent physically cannot escape the boundary — autonomy without approval fatigue, capability without blast radius | `ReferencesElement → el-agency-lang` |
| `how-subagents-for-context-isolation` | Group tools under sub-agents to fix tool-choice failures | Agents with many unrelated tools/concepts in context mis-pick tools and fail; wrap related tools in sub-agents exposed as plain functions so the top-level agent only picks a sub-agent (which runs with its own LLM call, system message, and tool set, in parallel where possible) — new capability with a cleaner decision at every level | `ReferencesElement → el-agency-lang` |

## Dropped

- Claude Code / Opus as the agent-definition example ("Claude Code is an agent; Opus is the model; everything else is the harness") — definitional aid only; no edge to `el-claude-code` **[registry]**.
- ReAct — named pattern inside the ladder; kept in prose (adjacent to registry `el-agent-loops`, not linked).
- Wikipedia sub-agent demo, "Jensen's inequality for medians" limerick prompt, Alan Kay quote ("simple things should be simple, complex things should be possible"), median-function bug fixture — demo color.
- *Grokking Algorithms* / ducktyped.org — expert-bio prose.

## Review notes

1. **Direct titular evidence for `pat-harness-over-model`**: the talk title is the pattern's thesis verbatim, argued as the talk's whole program (and extended: harness as the route to *local/open* models). Strongest single-artifact evidence for the batch-2 coin to date; also the first time the pattern is stated as a strategic direction (independence from frontier labs) rather than an engineering observation — hence the double link to `pat-sovereign-ai`.
2. **Speaker name garbles**: captions render him "Audit, pronounced Audit like a tax audit" (he goes by *Adit*) and the sign-off says "Aditya Parikh" — both resolved to **Aditya Bhargava** from the official talk title and his *Grokking Algorithms* authorship. "agent of commerce" → *agentic commerce*.
3. **"Japa optimizer"** is almost certainly a caption garble of **GEPA** (the prompt-optimization method); unresolved, kept as "built-in optimizers" in briefs. "PM install" → `npm install`; "Blue Sky" → Bluesky.
4. **HarnessBench** name/numbers are as-captioned from a paper the speaker cites; verify the paper before seeding public-facing claims.
5. **`pat-durable-execution` candidate — added evidence (not coined, per instructions)**: Agency's interrupts do true pause/resume — serialize a run mid-loop/mid-sub-agent and resume a week later at the exact point, "very few languages allow this". That is durable execution surfacing as a *language-level* requirement for agents, a new data-point shape alongside ZenML Kitaru (batch 3), Inngest (batch 4), OpenAI sandbox-cloud and KRAFTON state-in-files (batches 5–6). Evidence noted here; the signal stays parked on `pat-harness-over-model`.
6. `co-etsy` is coined because the speaker's affiliation and agentic-commerce role are stated, but note Agency is explicitly a personal research project; Etsy claims in this talk are limited to his bio.
