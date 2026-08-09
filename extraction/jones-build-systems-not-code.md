# SPIKE extraction — "Build Systems, Not Code" (Angie Jones, Agentic AI Foundation) — FOR REVIEW

Source transcript: `transcripts/jones-build-systems-not-code.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/ZD9-4fW2HhM — AI Engineer World's Fair, published 2026-06-25.
`stagingTimestamp` for the artifact and all signals: 2026-06-25 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Speaker cross-file note: `exp-angie-jones`, `co-agentic-ai-foundation`, and `co-block` are defined in `jones-autonomous-engineering-org.md` — referenced here by slug only.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-jones-build-systems` | Build Systems, Not Code (Angie Jones, Agentic AI Foundation — AI Engineer World's Fair) | youtube | https://youtu.be/ZD9-4fW2HhM |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-angie-jones` (defined in `jones-autonomous-engineering-org.md`).

## Experts (0 new)

Reuses `exp-angie-jones` (defined in `jones-autonomous-engineering-org.md`).

## Companies (0 new)

None needed — the talk is a personal-project framework talk (Relocation Scout house-hunting agent).

## Elements (2 new)

All new elements `IdentifiedInArtifact → ia-aie-jones-build-systems`.

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-output-contracts` | Agent output contracts | concept | harness | Schema-defined structured outputs (decision, score, reason) written to a queryable agent-memory layer instead of free-form session text; makes one agent/step's output another's input without a human in the loop, makes memory queryable ("every house rated 4+ with commute ≤ 15 min"), and defining the shape forces clarity about what you're asking the agent to produce |
| `el-agent-idempotency` | Agent idempotency | concept | harness | Designing agent runs to be safely retryable in messy realities (double-fired webhooks, crashed sessions): log every side-effecting action to memory, resume half-done runs by checking what the system wrote down and completing only what's missing, and run periodic lint passes over agent state; the agent-specific trap — a retried model may reword the request enough to look like a new task — means idempotency must be enforced by the system, not the model |

Registry elements referenced (edges only, no new nodes): `el-agent-skills`, `el-agents-md`, `el-deterministic-agentic-split`.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-jones-build-systems`, `SourcedFromSource → source-aie-yt` **[registry]**, domain `harness`. Framework talk — signals are practitioner testimony, not dated external facts.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-agent-design-is-swe` | Practitioner thesis: designing agentic systems exercises the same pre-genAI engineering disciplines — systems thinking, workflow design (every run ends stop/retry/escalate), decomposition, separation of concerns, modularity, contracts, state, threat modeling; the primitives changed, the discipline didn't — "we're still building, we just moved up a layer" | `FormsPattern → pat-harness-over-model` **[registry]** | — |
| `sig-giant-prompt-code-smell` | The giant prompt is the agentic code smell: her Relocation Scout instructions accreted four distinct jobs (listing normalization, shortlist format, commute calculation, neighborhood research) into one blob — the cause of agent drift ("the script is too long"); the fix is decomposition into skill / schema / script / sub-agent | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-agent-skills` **[registry]** |
| `sig-dont-let-agents-design-agents` | She deliberately does NOT let her coding agent design her other agents: the output "technically works" but is unmaintainable (a giant prompt, concerns poorly separated); the human architect bakes maintainability into the system, after which any harness can be told "update this agent to do XYZ" and succeed | `FormsPattern → pat-value-of-judgement` **[registry]** | — |
| `sig-retry-rewording-trap` | Agent retries carry a model-specific trap absent from classical systems: on retry, the model can reword the request just enough to register as a brand-new task; idempotency must therefore live in the system (memory-logged actions checked before acting — email sent, calendar never blocked → finish only the missing part), never delegated to the model | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-agent-idempotency` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-discipline-transfers-up-a-layer` | Agentic systems have direct analogues for every classic engineering structure — skills ≈ packages, sub-agents ≈ functions ("good in any hood" because they don't carry session context), schemas ≈ API contracts, agents.md ≈ architecture docs — so engineers should apply existing instincts (code smells included) rather than treat agent design as alien | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-agent-skills` **[registry]** |
| `ins-contracts-unlock-systems` | Free-form agent output is a dead end for systems: buried in a session, nothing downstream can reliably find it; schema-bound output written to queryable memory is what turns a one-shot prompt into a reusable agentic system with safe agent-to-step handoffs | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-agent-output-contracts` |

## KnowHow (5 new)

All `SourcedFromArtifact → ia-aie-jones-build-systems`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-decompose-agent-prompts` | Decompose the blob prompt by responsibility | Spot the distinct jobs hiding in one prompt and rehome each: reusable process → agent skill (write once, load in every market); fixed output format → schema; exact computation → plain boring script; meaty research subtask → sub-agent. Don't abstract instructions local to one workflow — modularity sometimes costs more than it saves | `ReferencesElement → el-agent-skills` **[registry]**, `el-deterministic-agentic-split` **[registry]** |
| `how-code-agent-human-split` | Assign work by actor strength | If a task has an exact answer, reach for code — cheaper, more reliable ("AI did not invent automation"); if it needs interpretation, judgment, or reasoning over messy input, give it to the agent; keep authority with humans — the human approves booking the tour | `ReferencesElement → el-deterministic-agentic-split` **[registry]** |
| `how-agent-threat-model` | Threat-model the agent like a service | Treat all third-party content (listing copy, forum threads, anonymous reviews) as untrusted input — tell the agent explicitly it is evidence, not instructions; grant least privilege; wall side-effecting actions (emailing sellers, booking tours, submitting offers) behind human approval to shrink blast radius | — |
| `how-idempotent-agent-runs` | Design for crash-and-retry from day one | Log side-effecting actions to memory as they happen; on retry, check what the system wrote down and complete only what's missing; schedule lint passes to catch half-done runs; assume webhooks fire twice and sessions crash — "this is not an exception, this happens all the time" | `ReferencesElement → el-agent-idempotency`, `el-agent-output-contracts` |
| `how-cold-start-maintainability` | Build for the fresh-context cold start | Put an agents.md at every level of the system explaining the workflow, where policy lives, supporting resources (skills, scripts, sub-agents), and how to keep memory up to date; the test: a fresh-context human or agent can orient and act without reverse-engineering prompts; if a harness fails when asked to update the system, treat that as a maintainability bug | `ReferencesElement → el-agents-md` **[registry]** |

## Dropped

- "Compendium Wiki" — the product she names as her agent-memory layer ("I use Compendium Wiki for my agent memory layer on most of my agents"); single mention, name unverified and plausibly caption-garbled — kept as prose, NOT coined as an Element. Flag for verification; if real, it belongs as a product element under `el-agent-output-contracts`'s orbit.
- Relocation Scout — the demo agent; illustration, not a product.
- "/goal" slash command — generic mention.
- Sub-agents as a standalone Element — covered by the functions analogy in `ins-discipline-transfers-up-a-layer` and by existing harness elements.

## Review notes

1. **`pat-durable-execution` candidate (NOT coined, per instruction):** the idempotency/retry/lint-pass material (`sig-retry-rewording-trap`, `how-idempotent-agent-runs`) is application-level evidence for the durable-execution thesis — state outliving the run, resumability by checking durable records — alongside Sehgal's log-is-the-agent talk in this same batch. Ledger note only, no edges.
2. **Adaptive-harness counter-note:** `sig-dont-let-agents-design-agents` is mild counter-evidence to the `pat-adaptive-harness` candidate and sits in direct tension with Graziano's agents-building-agents talk (same batch, where a coding agent successfully rewrites production agents). Good dialectic to preserve at review.
3. Heavy reuse of `pat-harness-over-model` (3 signals + both insights) is honest for a talk whose entire thesis is the engineering-of-the-scaffolding claim; `sig-dont-let-agents-design-agents` rehomed to `pat-value-of-judgement` where it genuinely fits (architecture judgment stays human).
4. `el-agent-output-contracts` vs `el-agent-handoff-gates` [registry, batch 6]: related — both make agent→agent handoffs safe. Kept separate: contracts are schema-on-output written to memory; handoff-gates are quality gates between fleet stages. Merge call is central's.
5. Note the "use code for determinism, agents for judgment, humans for authority" formula assigns judgment to *agents* and authority to humans — subtly different altitude from `pat-value-of-judgement` (human career edge); did not edge the formula to that pattern.
6. Framework talk with no external dated facts — same caveat as `daga-tesla-enterprise-agents-structure.md`: all signals are practitioner testimony.
7. Garbles: "agent's in D file" = agents.md file; "Compendium Wiki" unverified (see Dropped).
