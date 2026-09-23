# CLAUDE.md

Project instructions for Claude Code working on the **Omnigraph vs Markdown agent benchmark** (`bench/`).

## Overview

`bench/` is a small benchmark that runs the same Claude agent (Sonnet 5, no
subagents) on a 10-question shortlist about the AI Engineer World's Fair 2026
talks. It runs twice: once with only Omnigraph read queries, once with only the
raw transcripts as markdown files. It measures quality, time, cost and
grounding/hallucination, and produces a two-column table in
`results/results.md`. Epic A is done: the corpus, both sandboxed arms, the prompts,
a local 0.11 graph and a passing live isolation probe. Epic B (the question file) is next.

**`SPEC.md` is the task list and source of truth.** Start at the **Current focus** pointer near the top of the spec; it names the next actionable step so you don't have to scan the whole file. Work the spec: implement that step's deliverable, update its status (🔲 → 🔄 → ✅) in the phase tracker, and advance the Current focus pointer. Don't skip ahead past a phase's exit guardrails. When you reach a phase boundary, verify the guardrail criteria, fill in the **Actual outcome** column, and only then move on.

The repo root `CLAUDE.md` still applies to everything outside `bench/`. Benchmark
work doesn't change `schema.pg`, `queries/`, `policies/` or `seed/` unless the user
explicitly approves it, and every such change gets a Decision Log row (e.g. #31,
the query descriptions). Prefer documentation over new capability. The benchmark
reads the seed and the running server; it never writes data to either.

## Code conventions

- **Directory structure:**
  ```
  bench/
  ├── SPEC.md, CLAUDE.md
  ├── pyproject.toml        # uv project; console script `bench`
  ├── questions.yaml        # the shortlist (Epic B)
  ├── prompts/              # answer contract, per-arm tool briefs, judge prompts
  ├── bin/omnigraph         # reader-only shim put first on the Omnigraph arm's PATH
  ├── scripts/local-graph.sh  # the local file-backed 0.11 graph + server
  ├── src/bench/            # cli, corpus, arms, omnigraph, prompts, provider, agent, trace,
  │                         #   probe, questions, run, parse (next: verify, judge, score, report)
  ├── tests/
  ├── corpus/               # generated talk markdown — gitignored
  ├── runs/                 # per-run traces and result.json — gitignored
  ├── .omnigraph-home/      # shim config + act-reader credentials — gitignored
  └── results/              # results.md, scores.json, run-meta.json — committed
  ```
- **Style:** `uv run ruff check . && uv run ruff format .`
- **Testing:** `uv run pytest`. Every step with a code deliverable ships a test. The sandbox
  gates (`markdown_gate`, `omnigraph_gate`) and the quote verifier need both allowed and
  denied/negative cases. Tests never call the Claude API. Judge and agent calls are
  stubbed; the real calls happen only in `bench probe | run | score`.
- **Commits:** short, plain, human-sounding messages (e.g. "bench: build markdown corpus from
  chunks"). No co-author trailers. Mention the spec step in the body only when it helps.

## Commands

```bash
cd bench
uv sync
uv run bench corpus                 # A1 — build corpus/talks/*.md from ../seed
printf %s "$TOKEN_ACT_READER" | uv run bench shim   # A2.2 — once; reader-only omnigraph config
uv run bench probe                  # A2.4 — live isolation probe, both arms (~$0.09; needs the
                                    #   local server: scripts/local-graph.sh serve)
uv run bench check-questions        # B1.2
uv run bench run --pilot --max-spend 25   # C1.3 — 1 run per question per arm (20 runs)
uv run bench run                    # C1.4 — 3 runs per question per arm (resumable)
uv run bench score --dry-run        # D — claims to judge, cost estimate; no API calls
uv run bench score --limit 10       # D — judge 10 claims (pilot); scores.json waits for all
uv run bench score                  # D — quote checks + judge (cached), results/scores.json
uv run bench report                 # E — results/results.md
```

The Omnigraph arm needs the local graph server up:
`scripts/local-graph.sh status | serve | stop`. It is file-backed under
`bench/.graph/` (gitignored), with its own bearer tokens in `bench/.graph/tokens.env`.
The first build is `scripts/local-graph.sh setup && scripts/local-graph.sh load`.
Models (agents, judge, chunk embeddings) go through OpenRouter using `OPENROUTER_KEY`
in `bench/.env` (gitignored). Never print it or write it into a trace; `bench probe`
redacts it.

## Rules that protect the measurement

- **Arm isolation is the whole point.** Every `ClaudeAgentOptions` comes from `bench.arms` and has:
  - `setting_sources=[]` and `strict_mcp_config=True`
  - an explicit `tools=[…]` list
  - the PreToolUse gate hook, with `can_use_tool` as a deny-all backstop
  - a cwd in a temp dir outside the repo

  Never add `allowed_tools`: the gate must be the only thing that approves a call. A change to a
  gate needs a test for each new allowed or denied case.
- **Run the benchmark in a clean shell.** Never source `.env.omni` for `bench run` or `bench probe`.
  The Omnigraph agent's Bash inherits the environment, and the server runs in its own shell.
- **Keep the arms symmetric.** Same model, effort, caps and answer contract. Only the tools, cwd
  and tool brief differ. Any asymmetry is a Decision Log row.
- **No graph in the markdown arm, no transcripts in the Omnigraph arm.** Corpus headers carry only
  title, video link and date. Prompts never mention a question's expected answer or a pattern slug.
- **Never tune prompts on the results.** Change prompts only after the pilot, record why in §6,
  and then re-run both arms in full.
- **Numbers come from code.** `results.md` is generated. Never hand-edit a number in it.

## Workflow

- **Autonomous:** code steps with clear deliverables and tests (A1, A2.1–A2.3, C1.1–C1.2, D1.1,
  D1.2, D2.1, D2.3, E1.1–E1.2), run with stubbed model calls.
- **Needs human input:**
  - anything that spends money: `bench probe`, `bench run`, `bench score` against the real API.
    Confirm first and state the expected run count.
  - approving `questions.yaml` (B guardrail)
  - setting final caps after the pilot
  - showcase trace selection
  - every Decision Log row
  - starting or restarting the Omnigraph server
- **The loop:** pick the next 🔲 step → implement the deliverable → `ruff` + `pytest` → update the
  status table → commit. At a phase boundary, stop and confirm the guardrail before continuing.
- **When blocked or ambiguous:** mark the step ⏸️ with a note, add an Open Question to the spec,
  and surface it rather than guessing.

## Goals

Get Epics A–C through the pilot (C1.3): 20 clean runs with no sandbox escapes.
The caps and prompts can then be fixed before the full 60-run benchmark and
the scoring pass.
