# Omnigraph vs Markdown — agent benchmark — Technical Spec

**Author:** Roman Pronskiy · **Created:** 2026-09-23

> 📄 **This is a living document.** Status markers, decisions, and guardrail outcomes are meant to be updated as the work happens. See [How to Update This Document](#how-to-update-this-document) before editing.

### Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-09-23 | Initial spec created | Roman Pronskiy |
| 2026-09-23 | A1.1 done on the 0.11 seed; corpus is 337 talks; Sonar mis-link override and graph-fix gate added | Roman Pronskiy |
| 2026-09-23 | A1.2 done; Phase A1 guardrails passed | Roman Pronskiy |
| 2026-09-23 | A2.1 done; gate moved from `can_use_tool` to a PreToolUse hook; Omnigraph flag allowlist; clean-environment check added to A2.2 | Roman Pronskiy |
| 2026-09-23 | A2.2 done: `bench shim` + `bin/omnigraph` via `OMNIGRAPH_HOME`; secrets check implemented | Roman Pronskiy |
| 2026-09-23 | A2.3 done: contract + briefs, generated query catalog; D1.2 accepts chunk labels as talk ids | Roman Pronskiy |
| 2026-09-23 | A2.5 added and done: local 0.11 graph via `scripts/local-graph.sh`, OpenRouter for embeddings, agents and judge; Reader-only and Graph-live guardrails passed | Roman Pronskiy |
| 2026-09-23 | A2.4 done: live probe 8/8 on both arms via OpenRouter; Phase A2 guardrails passed; cost now from `model_usage` | Roman Pronskiy |
| 2026-09-23 | Agents switched to 1M context (`…[1m]`) | Roman Pronskiy |
| 2026-09-23 | B1.1 done: `questions.yaml` + validating loader | Roman Pronskiy |
| 2026-09-23 | Q05/Q08 swapped; B1.2 done; Epic B guardrails passed | Roman Pronskiy |
| 2026-09-23 | C1.1 done: `bench run` runner, shared trace helpers, answer-block parser | Roman Pronskiy |
| 2026-09-23 | C1.2 done: wall-clock cap, retries, spend limit | Roman Pronskiy |
| 2026-09-23 | Query docs: `@description` on every read query; brief names the verbatim-text queries; local cluster re-applied (rev 3) | Roman Pronskiy |
| 2026-09-23 | C1.3 pilot done (20/20 ok, $9.29); saved-output defect fixed; caps final | Roman Pronskiy |
| 2026-09-23 | Local graph re-linked (`bench relink-chunks`); mis-link guardrail passed for the local graph | Roman Pronskiy |
| 2026-09-23 | Sonar fix ported to `seed/chunks/part-03.jsonl`; override emptied; README notes the seed is ahead of the served graph | Roman Pronskiy |
| 2026-09-23 | C1.4 stopped at 34/60: `talk_semantic` failed on every real talk (0.11 T26 shape); query fixed (#36), og runs redone, md runs kept | Roman Pronskiy |
| 2026-09-23 | C1.4 done: 60/60 ok, $30.25 (md $12.99, og $17.26); Phase C1 guardrails passed; `results/run-meta.json`; focus moves to Epic D | Roman Pronskiy |
| 2026-09-23 | D1.1 normalisation rules pinned down from the C1.4 answers and implemented (`parse.normalise`); D1.2 resolves bare chunk labels | Roman Pronskiy |
| 2026-09-24 | D1.2 done: `verify.Corpus` quote check with a new `spliced` outcome (#37); C1.4 verbatim md 99.2%, og 97.2%; rapidfuzz added | Roman Pronskiy |
| 2026-09-24 | D1.3 support judge written with stubbed tests (`judge.py`, cached Opus 5.5 requests, `Corpus.context`, `prompts/judge_support.md`); `anthropic` SDK added; real pass pending | Roman Pronskiy |
| 2026-09-24 | `bench score` runner; D1.3 pilot 10/10 judged for $0.10; full pass about $7.10 | Roman Pronskiy |

### Status legend

🔲 Not started · 🔄 In progress · ✅ Done · ⏸️ Blocked · ❌ Cut

### Current focus

**Now on:** Epic D → Phase D1 → step D1.3 — the full support pass (`uv run bench score`, 685 requests, about $7.10) waits for your go; the 10-claim pilot is done. D1.4 (uncited statements) can be written with stubs meanwhile.

---

## 1. Executive summary

A small, repeatable benchmark that puts the same Claude agent in front of the
same questions about the AI Engineer World's Fair 2026 talks twice. One arm
answers from the Omnigraph graph through its stored read queries. The other
answers from the raw talk transcripts as markdown files. The transcripts come
to about 1.4–1.6M tokens, so they can't be pasted into context; the markdown
agent has to search them the way a coding agent would. The benchmark leans
toward aggregated questions ("what topics were discussed most", "which talks
argue X"), where a graph should help most. It measures answer quality, time,
cost and hallucination/grounding. The output is one two-column table, **Agent
+ Omnigraph** vs **Agent + Markdown files**, backed by per-question detail and a
few side-by-side traces for a demo.

---

## 2. Technical decisions

| Area | Decision | Rationale |
|------|----------|-----------|
| Location | `bench/` inside the graph repo | Keeps the benchmark next to the schema, queries and seed it measures. Corpus and raw runs stay gitignored. |
| Language / tooling | Python ≥ 3.12, `uv`, `ruff`, `pytest` | Matches the local corpus scripts; `uv run bench …` is the single entry point. |
| Agent harness | Claude Agent SDK (`claude-agent-sdk`) | The Claude Code harness as a library: same built-in Read/Grep/Glob/Bash tools, and a `ResultMessage` per run with `total_cost_usd`, `duration_ms`, `duration_api_ms`, `num_turns` and `usage`. |
| Agent isolation | `setting_sources=[]`, `strict_mcp_config=True`, `tools=[…]` per arm, a PreToolUse-hook gate on every call (with `can_use_tool` as a deny-all backstop), cwd in a temp dir outside the repo | The SDK loads user, project and local settings plus CLAUDE.md by default. Neither arm may see the repo's CLAUDE.md, user hooks or plugins, or the other arm's data. |
| Agent model | `anthropic/claude-sonnet-5[1m]` (Sonnet 5 with its full 1M context), `effort="high"`, both arms | Cheaper for 60 runs. The `[1m]` suffix makes the CLI use the whole 1M window: without it, it assumes 200k for OpenRouter ids, which would force the markdown arm to compact early. |
| Model access | OpenRouter's Anthropic-compatible API: `ANTHROPIC_BASE_URL=https://openrouter.ai/api`, `ANTHROPIC_AUTH_TOKEN` = `OPENROUTER_KEY` from `bench/.env`, `ANTHROPIC_API_KEY=""`; model ids `anthropic/claude-sonnet-5` (agents) and `anthropic/claude-opus-5.5` (judge) | You chose OpenRouter as the billing account. Both models are listed there at Anthropic list prices. |
| Cost | Computed per run as usage × a snapshot of OpenRouter prices, recorded with the results: Sonnet 5 $2 in / $10 out / $0.20 cache read / $2.50 cache write per Mtok; Opus 5.5 $4 / $20 / $0.20 / $5. The SDK's `total_cost_usd` is kept as a cross-check. | The SDK's cost comes from Claude Code's own price table, which may not recognise OpenRouter model ids. Tokens × a recorded price is exact and reproducible. |
| Local graph | File-backed copy under `bench/.graph/` (gitignored), built by `scripts/local-graph.sh`. Chunks are embedded with `google/gemini-embedding-2-preview` (the seed's model) through OpenRouter using Omnigraph's `openai-compatible` provider, and the server uses the same model for `nearest()`. | There was no S3 store or Gemini key here, and the tracked `cluster.yaml` stays untouched. The embedding model matches production's. |
| Subagents | None in either arm (no `Agent`/`Task` tool) | The comparison is about the data interface, not orchestration. |
| Judge model | `claude-opus-5-5` via the `anthropic` SDK, structured outputs, `effort` set explicitly to `high` | A stronger model than the agents, and a different one, to limit self-preference. Opus 5.5 defaults to `medium` effort, so it is set explicitly. |
| Corpus | 337 markdown files rebuilt from `seed/chunks` via `PartOfArtifact`, plus one documented override for a mis-linked talk | The original `transcripts/` folder isn't on this machine. Chunks join back together without overlap. |
| Correctness | No gold set, no human review: blind pairwise judge + pooled recall | User decision. Correctness is relative between the arms, not absolute. |
| Grounding | Every claim cites `talk slug + verbatim quote`. A mechanical quote check, then a judge check that the quote supports the claim. | The same contract for both arms, and checkable against the corpus without a gold set. |
| Cost scope | Per question only; graph build cost excluded | User decision. Stated as a footnote in the report. |
| Runs | 10 questions × 2 arms × 3 runs = 60 agent runs | 3 runs expose variance without making the pilot expensive. |

---

## 3. Architecture overview

```
 seed/chunks/*.jsonl ──build_corpus──▶ bench/corpus/talks/<ia-aie-slug>.md  (337 files, gitignored)
 seed/04-artifacts.jsonl ─(title, link, date header)─┘

 questions.yaml ──┐
                  ▼
            ┌─────────────┐   per (question, arm, run)    ┌──────────────────────────────┐
            │  bench run  │ ─────────────────────────────▶ │ Claude Agent SDK (Sonnet 5)  │
            └─────────────┘                                │  setting_sources=[]          │
                  ▲                                        ├──────────────┬───────────────┤
                  │ runs/<q>/<arm>/<n>/                    │ markdown arm │ omnigraph arm │
                  │  trace.jsonl, result.json              │ Read/Grep/   │ Bash gated to │
                  │  (answer + metrics)                    │ Glob over a  │ `omnigraph    │
                  │                                        │ temp copy of │  alias|query` │
                  │                                        │ the corpus   │ → server:8081 │
                  │                                        └──────────────┴───────────────┘
            ┌─────────────┐   claims + quotes   ┌─────────────────────────┐
            │ bench score │ ──────────────────▶ │ verify: quote in corpus │ (mechanical)
            └─────────────┘                     │ judge: Opus 5.5         │ (support, pairwise,
                  │                             └─────────────────────────┘  item clustering)
                  ▼
            ┌─────────────┐
            │ bench report│ ──▶ bench/results/results.md  (two-column table + per-question + traces)
            └─────────────┘
```

`bench run` runs each question through each arm three times and stores the
full trace and a metrics record for every run. `bench score` checks every
cited quote against the corpus, has the judge rate claim support and compare
the two arms blind, and pools list items across runs. `bench report` turns the
scores into the table.

---

## 4. Epics

All five epics below are MVP. The MVP is done when `results/results.md` holds
the two-column table for the 10-question shortlist at 3 runs per arm.

### Epic A — Corpus and arm sandboxes  ·  MVP

**Goal:** both agents can run, each sees only its own data source, and nothing else leaks in.
**Success metrics:** 337 corpus files with every chunk accounted for. An isolation probe passes for both arms.

#### Phase A1 — Markdown corpus

| Step | Description | Status | Notes |
|------|-------------|--------|-------|
| A1.1 | `bench corpus` builds 337 talk files from `seed/chunks` | ✅ | 337 files, 6.9 MB; 6 unit tests |
| A1.2 | Corpus integrity test against the real seed | ✅ | 7 tests; all 5 real-bug mutations caught |

**Steps (detail):**

- **A1.1 — Build the corpus.** Deliverable: `src/bench/corpus.py` and `bench corpus`, writing
  `corpus/talks/<artifact-slug>.md`.
  - Map each chunk to its talk through its `PartOfArtifact` edge. Order by `chunk_index`.
  - `CHUNK_TALK_OVERRIDES` corrects one known mis-link. The graph attaches all 24 chunks of
    Anirban Chatterjee's "Guide, Verify, Solve" (`chatterjee-sonar-guide-verify-solve`) to Tariq
    Shaukat's `ia-aie-shaukat-verifiers-king`. The override sends them to
    `ia-aie-chatterjee-guide-verify-solve`. The same mapping re-linked the local graph's chunk
    edges (`bench relink-chunks`, #34). Since #35 the seed itself is fixed and the mapping is empty;
    the mechanism stays for any future mis-link.
  - If any talk ends up with chunks from more than one transcript, the build fails, so a future
    mis-link can't silently merge two talks.
  - Strip the leading `[talk-slug] ` label from each chunk's text. Join chunks with a blank line
    and no chunk markers, so the file reads like a plain transcript.
  - The header comes only from `seed/04-artifacts.jsonl`: title (which already names the
    speaker and company), video link and publish date. Nothing else from the graph goes into
    the markdown arm.
  ```markdown
  # How Anthropic Builds: Lessons from Labs (Mike Krieger, Anthropic — AI Engineer World's Fair keynote)
  - talk: ia-aie-krieger-anthropic-how-anthropic-builds
  - video: https://youtu.be/…
  - published: 2026-…

  <transcript text, chunk 0>

  <transcript text, chunk 1>
  ```
- **A1.2 — Integrity test.** Deliverable: `tests/test_corpus_seed.py`, run against the real
  `../seed`. It checks:
  - 337 files
  - every chunk's text (without its label) appears verbatim in its talk's file, in
    `chunk_index` order
  - no `[talk-slug]` chunk label is left in any file
  - the two Sonar talks are split by speaker (literal opening lines)
  - transcript words (without headers) are within 1% of 1,192,360 (measured on 2026-09-23)
  - the corpus build is deterministic (same bytes on a rebuild)

**Exit guardrails — Phase A1 → A2**

| Guardrail | Criteria (pass/fail) | Status | Actual outcome |
|-----------|----------------------|--------|----------------|
| Complete | 337 files; 5,339/5,339 chunks found verbatim | ✅ | 337 files; 5,339/5,339 chunks found verbatim and in index order; 1,192,360 transcript words (exactly the measured count) |
| No graph leakage | Headers hold only title, video link and date; no pattern, signal or element text | ✅ | Every file's header is exactly title, talk slug (= file name), video and date, then the transcript. The slug is kept because citations need it. |
| Tests green | `uv run pytest` passes | ✅ | 13 passed (6 unit + 7 seed), ruff clean. A mutation check (reverse order, label kept, extra header line, override ignored, no separator) was caught every time. |

#### Phase A2 — Arm sandboxes

| Step | Description | Status | Notes |
|------|-------------|--------|-------|
| A2.1 | `arms.py`: SDK options and the PreToolUse gate for both arms | ✅ | 55 tests; 7 gate mutations all caught |
| A2.2 | Reader-only `omnigraph` shim | ✅ | `bench shim` + `bin/omnigraph`; 9 tests; real install waits on the reader token |
| A2.3 | Prompts: shared answer contract and one tool brief per arm | ✅ | `prompts/*.md` + `prompts.py`; 8 tests; catalog of all 89 read queries |
| A2.5 | Local 0.11 graph + server via `scripts/local-graph.sh` (needed before A2.4) | ✅ | 5,034 nodes, 17,942 edges, 5,339 embedded chunks, 2,619 evidence edges; serving on :8081 |
| A2.4 | `bench probe`: isolation probe for both arms | ✅ | 8/8 checks on both arms; about $0.09 per full probe |

**Steps (detail):**

- **A2.1 — Arm configs.** Deliverable: `src/bench/arms.py` (built against `claude-agent-sdk`
  0.2.158, bundled CLI 2.1.280). Both arms share the model, effort, caps and answer contract.
  They differ only in tools, working directory and system prompt.
  ```python
  markdown_options(talks_dir, system_prompt)             # tools=["Read", "Grep", "Glob"], cwd=talks_dir
  omnigraph_options(scratch_dir, system_prompt, shim_bin)  # tools=["Bash", "Read"], cwd=scratch_dir,
                                                         # env PATH = shim_bin first
  # shared: model="claude-sonnet-5", effort="high", max_turns=100, max_budget_usd=10.0,
  #         setting_sources=[], strict_mcp_config=True, allowed_tools=[],
  #         hooks={"PreToolUse": [gate_hook(gate)]}, can_use_tool=deny-all backstop
  ```
  - **The gate is a PreToolUse hook, not `can_use_tool`.** The SDK source shows `can_use_tool`
    only fires for calls that still need permission, so reads inside cwd never reach it. The hook
    runs on every call and returns an explicit `allow` or `deny` with a reason the agent can read.
    `can_use_tool` denies anything that still reaches the permission prompt.
  - `markdown_gate` allows Read, Grep and Glob only within the talks dir. It resolves symlinks,
    rejects `~` and absolute paths, and rejects `..` or absolute glob patterns. Every other tool
    is denied.
  - `omnigraph_gate` allows Bash only as `omnigraph alias …` or `omnigraph query …`, and only with
    the flags `--params`, `--format`, `--profile` and `--help`. It rejects shell operators
    (`; & | $ \` < >`, newlines), unbalanced quotes and background runs. Read is allowed only
    inside the arm's scratch dir.
    - A flag allowlist is needed because `omnigraph query` also accepts ad-hoc GQ
      (`-e`, `--query-string`, `--query <file>`), direct store access (`--direct`, `--store`),
      `--as <actor>` and `--params-file <path>`. Any of these would let the agent get around the
      stored-query interface.
  - Tested with allowed and denied cases for both gates, a symlink escape, the hook's output
    shape, arm symmetry, and the deny-all backstop.
  - Mutation check: removing the shell-operator check, symlink resolution, the flag allowlist, the
    verb check, glob-pattern checks or the background check, or making the hook always allow,
    fails at least one test every time.
- **A2.2 — Reader-only shim.** Deliverable: `bin/omnigraph`, `src/bench/omnigraph.py` and
  `bench shim`. The agent calls `omnigraph …` as normal and never sees the analyst login.
  - **`bench shim`** reads the **act-reader** token on stdin and writes `bench/.omnigraph-home/`
    (mode 0700, gitignored). Setup: `printf %s "$TOKEN_ACT_READER" | uv run bench shim`. The
    folder holds:
    - the repo's `omnigraph-config.example.yaml` as `config.yaml` (65 aliases, all stored reads)
    - the credential, stored by `omnigraph login intel-local`
    - the path of the real CLI
  - **`bin/omnigraph`** (first on the arm's PATH) drops every `OMNIGRAPH_*`, `AWS_*`,
    `TOKEN_ACT_*` and `GEMINI_API_KEY` variable. It sets `OMNIGRAPH_HOME` to the bench folder and
    `OMNIGRAPH_PROFILE=intel`, then runs the real CLI.
  - Verified against CLI 0.11.0:
    - `OMNIGRAPH_HOME` replaces `~/.omnigraph`, with `config.yaml` and `credentials` directly
      inside it.
    - A local echo server confirmed that the CLI sends the stored credential even when
      `OMNIGRAPH_BEARER_TOKEN` is set.
    - `OMNIGRAPH_PROFILE` lets a bare `omnigraph query <name>` reach
      `/graphs/spike/queries/<name>`.
  - The Bash tool inherits the harness environment, so `bench run` and `bench probe` refuse to
    start if `graph_secrets_in(os.environ)` finds anything. It checks for `AWS_*`, `TOKEN_ACT_*`,
    `GEMINI_API_KEY`, `OMNIGRAPH_BEARER_TOKEN`, `OMNIGRAPH_CONTROL_API` and
    `OMNIGRAPH_SERVER_BEARER_TOKENS_JSON`. The check is implemented now and gets wired into those
    commands when they're built (A2.4, C1.1). The server
    runs in its own shell with `.env.omni` sourced; the benchmark never does.
- **A2.3 — Prompts.** Deliverable: `prompts/answer_contract.md`, `prompts/markdown_arm.md`,
  `prompts/omnigraph_arm.md` and `src/bench/prompts.py::system_prompt(arm, workdir)`, which
  returns the contract followed by the arm's brief.
  - **Custom system prompt, not the Claude Code preset.** Both arms get only contract + brief. That
    keeps the framing identical and drops the coding-agent instructions and environment noise.
    The brief names the run's working directory, because Read needs absolute paths.
  - **Contract** (shared): work only from tool output, not prior knowledge. Transcripts are
    auto-captions, so garbles are quoted as they appear. The answer is prose, then one fenced
    `json` block with `items` (label, rank, talk_count) and `claims` (item, claim, talk, quote of
    8–40 verbatim words). If nothing is found, the block has empty lists and the agent doesn't
    guess.
  - **Markdown brief**: one `<talk-id>.md` per talk and the header format. Tools are Read, Grep and
    Glob only. `talk` is the file name without `.md`.
  - **Omnigraph brief**:
    - the two allowed command forms and flags
    - the node types, edges, domain enum and id prefixes (from the README model section, with no
      data)
    - a warning that everything except Chunk text is pipeline paraphrase, so quotes must come from
      Chunk text
    - `talk` may be the `ia-aie-…` id **or** the chunk's `[label]`, since `hybrid-search` and
      `related` return only chunk text and index
  - **Query catalog**: generated by `query_catalog()` from `queries/*.gq` (excluding
    `mutations.gq`) and the alias pack. It has one line per stored read query (89): the alias
    usage if there is one (65), else `omnigraph query <name> --params '{…}'`, plus the
    `@description` or the `//` comment directly above the query, plus the returned fields. It
    stays in step with the graph automatically.
  - **Size:** the Omnigraph prompt is about 16k characters (roughly 4k tokens) and the markdown
    prompt about 1.8k. The difference is the catalog, which is the Omnigraph interface's
    documentation. It is paid once per run and cached after the first turn.
  - **Tests:**
    - the exact catalog format on a fixture, including a comment separated by a blank line
    - every read query and alias present, no mutation
    - the shared contract prefix
    - no unfilled placeholders
    - each arm told only about its own tools
    - none of the 5,034 seed node ids in either prompt
  - **Mutation check:** mutations included, workdir not filled, a comment across a blank line
    attached, and `as` aliases ignored are all caught.
- **A2.5 — Local graph.** Deliverable: `scripts/local-graph.sh setup|load|serve|stop|status`.
  - **setup** copies `cluster.yaml` without its S3 `storage:` line, plus the schema, queries and
    policies, into `bench/.graph/`. It generates three random bearer tokens (`tokens.env`, 0600),
    then runs `cluster import` (0.11 needs an initial state before `apply`) and `cluster apply`.
  - **load** loads the seed in the order the README gives. Every file is loaded at most once
    (a marker per file) and must advance the commit head. Chunk parts are embedded through
    OpenRouter first (about $0.30 for all 5,339). Then it runs `omnigraph optimize`.
  - **serve** starts `omnigraph-server --cluster bench/.graph --bind 127.0.0.1:8081` with the
    tokens and the embedding env.
  - The act-reader token from `tokens.env` feeds `bench shim`:
    `grep '^TOKEN_ACT_READER=' bench/.graph/tokens.env | cut -d= -f2- | tr -d '\n' | uv run bench shim`.
  - Outcome (2026-09-23):
    - 13 × 800 + 278 chunk rows merged, plus 2,619 evidence edges, then `optimize`.
    - One transient embed failure on the first attempt; the retry succeeded. Parts now embed
      4 at a time (about 3 minutes per part), and each part keeps its own embed log.
    - The server runs outside the sandbox, which blocks listening on local ports.
- **A2.4 — Isolation probe.** Deliverable: `bench probe [--arm markdown|omnigraph|both]`
  (`src/bench/probe.py`, `src/bench/agent.py`, `src/bench/provider.py`).
  - **Pre-flight** refuses to start if `graph_secrets_in(os.environ)` finds anything. It then
    needs the OpenRouter key, the corpus (markdown arm), and the shim plus a live `/healthz`
    (Omnigraph arm).
  - **Each arm** runs in a fresh temp workdir with its own `CLAUDE_CONFIG_DIR`, using the real
    options and system prompt. It gets 6 scripted steps, 1 allowed control call and 5 escapes:
    - markdown: Glob `*.md`; Read the repo README, a seed file and `~/.claude/CLAUDE.md`; Grep
      the real corpus outside the workdir; Glob `../**`
    - omnigraph: `alias top-patterns`; `mutate`; `cat README`; `…; ls`; `--store file://…`;
      Read the README
  - **Verdict from the trace, not the agent's report:**
    - the init tool list is exact, with no MCP servers or non-built-in plugins, and the model
      is right
    - every step was attempted
    - replaying every call through the gate matches the live result: a denial carries the
      gate's reason, and an allowed call wasn't blocked
    - the control call returned data
    - no leak markers appear in any tool result
    - the session finished
  - **Output:** `trace.jsonl` + `summary.json` in `runs/_probe/<arm>/<stamp>/`, with the key
    redacted.
  - **Cost** is `session_cost(ResultMessage.model_usage)`. `ResultMessage.usage` misses part of
    the session (14 vs 1,533 input tokens in the probe). `model_usage` priced at OpenRouter
    rates equals the SDK's `total_cost_usd` exactly.
  - **Outcome (2026-09-23):**
    - markdown: 8/8 checks, 7 turns, 15.6 s, $0.028–0.031
    - omnigraph: 8/8 checks, 7 turns, 20.6 s, $0.062–0.065
    - The first markdown run failed `no_mcp_or_plugins` on the CLI's own `telemetry@builtin`
      plugin. The check now allows `@builtin` sources only; tested both ways.

**Exit guardrails — Phase A2 → Epic B**

| Guardrail | Criteria (pass/fail) | Status | Actual outcome |
|-----------|----------------------|--------|----------------|
| Tool surface | The SDK init `SystemMessage` lists exactly the arm's tools, no MCP servers and no skills or agents | ✅ | Markdown: exactly `Glob, Grep, Read`. Omnigraph: exactly `Bash, Read`. `mcp_servers: []`. `plugins` is only `telemetry@builtin`, which is part of the CLI; the check fails on any non-built-in plugin. The CLI still lists its built-in skills and agents, but without Skill or Agent tools the model can't invoke them. |
| Nothing inherited | Neither the repo nor the user CLAUDE.md shows up in the probe trace; no user hooks fire | ✅ | `setting_sources=[]` plus a per-run `CLAUDE_CONFIG_DIR`: `memory_paths` point into the run's own claude-home and `apiKeySource` is `none` (auth is the OpenRouter token). No hook messages besides ours. No README, repo or user CLAUDE.md, or seed text in any tool result. |
| Escapes denied | Every out-of-bounds read, non-omnigraph command and chained command is denied | ✅ | All 12 scripted attempts were made (6 per arm). Replaying each call through the gate matched the live result, and denials came back with the gate's exact reason, so the hook ran on every call. Blocked: repo README, seed, `~/.claude/CLAUDE.md`, the corpus outside the workdir, `../` globs, `mutate`, `cat`, `;` chaining and `--store`. |
| Reader only | `omnigraph mutate` through the shim is denied by the gate. Called directly with the shim's config, it returns 403. | ✅ | Called directly through `bin/omnigraph`, it returns `policy denied action 'change' on branch 'main' for actor 'act-reader'`. The gate half is unit-tested (A2.1); the live gate half is in the A2.4 probe. |
| Graph live | `omnigraph alias top-patterns` through the shim returns 18 patterns; `/healthz` is ok | ✅ | 18 patterns; healthz `{"status":"ok","version":"0.11.0","internal_schema_version":9}`. `hybrid-search` returns 10 chunks (query-time embedding via OpenRouter works). `talk-chunks ia-aie-shaukat-verifiers-king` returns 37, so the mis-link is present locally too. |

---

### Epic B — Question shortlist  ·  MVP

**Goal:** 10 questions, weighted toward aggregation, each with an answer shape the scorer can handle.
**Success metrics:** you approve the shortlist, and each question is answerable (or, for Q10, provably not) from the corpus.

#### Phase B1 — Shortlist

| Step | Description | Status | Notes |
|------|-------------|--------|-------|
| B1.1 | `questions.yaml` with the 10 questions below | ✅ | Loader + 12 tests; waiting on your approval (B guardrail) |
| B1.2 | Corpus sanity check per question | ✅ | `bench check-questions`: 10/10 pass on the markdown corpus |

**Steps (detail):**

- **B1.1 — Question file.** Deliverable: `questions.yaml`, with `id`, `category`, `shape` and
  `text` per question, and `src/bench/questions.py::load_questions`. The loader refuses:
  - malformed ids or duplicate ids
  - an unknown category or shape
  - empty text
  - graph vocabulary: id slugs such as `pat-…` or `co-…`, and the word "signal(s)"

  A test also checks that no question text appears in either system prompt. Questions use ordinary words, not graph vocabulary: no pattern slugs,
  no "signals".

  | ID | Category | Shape | Question |
  |----|----------|-------|----------|
  | Q01 | aggregate | ranked_list | What were the 10 most discussed topics at AI Engineer World's Fair 2026? Rank them by how many talks covered each, give an approximate talk count, and cite at least two talks per topic. |
  | Q02 | aggregate | ranked_list | What do speakers most often name as the biggest unsolved problems in building and shipping AI agents? Give the top 5, ranked, with supporting talks. |
  | Q03 | aggregate | ranked_list | Where do speakers disagree most? Name the three most contested claims, and for each, which talks argue for it and which push back. |
  | Q04 | aggregate | talk_set | Which talks argue that the engineering around the model (harness, tools, context, scaffolding) matters more than which model you pick? List every talk you can find, with speaker and company. |
  | Q05 | aggregate | ranked_list | Which five companies gave the most talks at the conference, and what did each company's talks focus on? |
  | Q06 | aggregate | company_set | Which companies described how they verify or review AI-generated code before it ships? Summarize each company's approach. |
  | Q07 | aggregate | ranked_list | Which tools, frameworks or products do speakers recommend most often for evaluating or observing LLM agents? Rank them by the number of talks that mention them favorably. |
  | Q08 | multi-hop | prose | How do the concerns raised in talks about voice or robotics agents differ from those raised in talks about coding agents? |
  | Q09 | lookup | prose | In Mike Krieger's talk on how Anthropic builds, how does Anthropic decide what to unship? |
  | Q10 | absence | absence | Which talks discuss running LLM inference on FPGAs or neuromorphic chips? |

- **B1.2 — Sanity check.** Deliverable: `bench check-questions` and `questions.py::check_questions`.
  Each question carries `check_terms` in `questions.yaml`; the agents never see them. A term
  counts the talks that contain it, case-insensitive.
  - For each non-absence question, it greps the corpus for a few seed terms and confirms at least
    one relevant talk.
  - For Q10, it confirms zero hits for `fpga`, `f p g a`, `field programmable`,
    `field-programmable`, `neuromorphic` and `spiking neural`. All were zero on 2026-09-23.
  - The check uses only the markdown corpus, never the graph.

**Exit guardrails — Epic B → Epic C**

| Guardrail | Criteria (pass/fail) | Status | Actual outcome |
|-----------|----------------------|--------|----------------|
| Approved | Roman signs off on the 10 questions | ✅ | Approved by Roman on 2026-09-23 with Q05 and Q08 swapped for pattern-neutral questions (decision #28). |
| Answerable | Q01–Q09 each have ≥1 relevant talk; Q10 has 0 hits | ✅ | Every term hits at least one talk for Q01–Q09 (e.g. Q08: voice agent 6, robot 20, coding agent 110; Q09: `unship` 1, Krieger's talk). Q10's six spellings (fpga, f p g a, field programmable, field-programmable, neuromorphic, spiking neural) hit 0. |

---

### Epic C — Runner  ·  MVP

**Goal:** every (question, arm, run) executes unattended and leaves a full trace plus a metrics record.
**Success metrics:** 60/60 runs recorded. The pilot shows no sandbox violations.

#### Phase C1 — Runner and pilot

| Step | Description | Status | Notes |
|------|-------------|--------|-------|
| C1.1 | `bench run`: resumable runner with metrics capture | ✅ | `run.py`, `trace.py`, `parse.py`; 17 tests with an injected fake agent |
| C1.2 | Caps, timeouts and failure statuses | ✅ | 30 min wall clock; 2 retries (30 s, 60 s) on exceptions and 429/5xx/529; `--max-spend`; 6 tests, 4 mutations caught |
| C1.3 | Pilot: 1 run per question per arm (20 runs) | ✅ | 20/20 ok, $9.29; md $4.11 / 21.8 min; og $5.18 / 32.6 min; see outcome below |
| C1.4 | Full run: 3 runs per question per arm (60 runs) | ✅ | 60/60 ok, $30.25; md $12.99 / 65.7 min; og $17.26 / 91.6 min. The first attempt was stopped at 34/60 when `talk-semantic` turned out never to have worked (#36); og was redone after the fix |

**Steps (detail):**

- **C1.1 — Runner.** Deliverable: `src/bench/run.py` (+ `trace.py`, `parse.py`) and
  `bench run [--pilot | --runs N] [--only Q01,Q09] [--arm markdown|omnigraph|both] [--concurrency 4]`.
  - **Order:** run-major, then question, then arm, so both arms meet each question at about the
    same time. Up to `--concurrency` runs go in parallel. A run whose `result.json` exists is
    skipped, so the command resumes.
  - **Isolation:** each run gets a fresh workdir under `$TMPDIR/aie-bench/runs/<q>/<arm>/<n>/`
    (a corpus copy, or an empty scratch dir) and its own claude-home. The prompt is the question
    text. The workdir is removed afterwards, except when the run errored.
  - **Output:** `runs/<q>/<arm>/<n>/trace.jsonl` (every SDK message) and `result.json`, with the
    OpenRouter key redacted from both.
    ```python
    {"qid", "arm", "run", "question", "started_at",
     "status": "ok|capped|error", "stop_reason",           # result subtype, or the exception
     "wall_s", "duration_ms", "duration_api_ms", "num_turns",
     "cost_usd",                                           # model_usage × OpenRouter prices
     "sdk_cost_usd",                                       # the SDK's own figure, a cross-check
     "input_tokens", "output_tokens", "cache_read_input_tokens", "cache_creation_input_tokens",
     "tool_calls", "tool_calls_by_name",
     "denied_tool_calls",                                  # the gate replayed on every call
     "answer_text", "answer_json",                         # parse.answer_block: last fenced json
     "model", "cli_version", "sdk_version", "graph_head", "corpus_sha"}
    ```
  - **Per invocation:** the local graph's head (`omnigraph commit list`) and a SHA-256 of the
    corpus are recorded once. Pre-flight is shared with `bench probe`: no graph secrets, the key,
    the corpus, the shim and `/healthz`. `--only` rejects unknown ids before anything runs.
  - **Checked:** graph head `01M37RTNV78NW2BA9M5BKK3G2X`; the pilot plan is 20 runs and the full
    plan 60.
- **C1.2 — Caps.** Deliverable: caps and failure handling in `run.py` (constants), plus
  `bench run --max-spend USD`.
  - **Caps per run:** `max_turns=300` and `max_budget_usd=10` (SDK-enforced, in `arms.py`), and a
    30-minute wall clock (`WALL_TIMEOUT_S`). Hitting any cap gives status `capped`
    (`error_max_turns`, `error_max_budget_usd` or `wall_timeout`), is scored as-is, counts against
    that arm, and is never retried.
  - **Timeouts keep the partial trace:** `run_agent` streams into a list the runner owns. The cost
    of a timed-out session comes from per-message usage, flagged `cost_complete: false` (it
    undercounts).
  - **Infrastructure failures** are retried twice (after 30 s, then 60 s), each time in a fresh
    sandbox. That covers exceptions (CLI or connection errors) and results with
    `api_error_status` 429/500/502/503/504/529. After the third failure the status is `error`.
    `result.json` records `attempts`, `retries` (the failure reasons) and `retry_cost_usd`, kept
    apart from the run's own `cost_usd`.
  - **`--max-spend`:** no new run starts once finished runs (including retry costs) have spent
    that much. Runs already going finish, so the total can overshoot by at most
    concurrency × per-run budget.
  - The spec's earlier `bench.toml` idea was dropped: the caps are constants next to the code that
    enforces them (decision #29).
- **C1.3 — Pilot.** Deliverable: `runs/` for 20 runs (`bench run --pilot --max-spend 20`).
  - **Q01 calibration first:** md $0.73 / 265 s / 82 turns; og $0.99 / 299 s / 76 turns. The
    graph agent pulled 19 whole transcripts with `talk-chunks`, which led to the query docs (#31).
    After them: og $0.60 / 224 s / 70 turns and 0 whole transcripts. The first og run is kept in
    `runs/_before-query-docs/`.
  - **Pilot outcome (2026-09-23):**

    | | markdown | omnigraph |
    |---|---|---|
    | cost | $4.11 | $5.18 |
    | total time | 21.8 min | 32.6 min |
    | turns per run | 3–82 | 14–124 |
    | parsed answers | 10/10 | 10/10 |
    | verbatim quotes (quick check) | 112/128 | 90/109 |

    The markdown arm is fast on lookups (Q09: 4 turns, $0.05; og: 22 turns, $0.22). Both arms
    handle Q10 (absence) correctly. The og arm answers "topics" (Q01) with the graph's patterns;
    the md arm counts topics bottom-up.
  - **Harness defect found:** the CLI saves oversized tool output under the run's claude-home
    (`…/tool-results/<id>.txt`) and tells the agent to Read it, but both gates only allowed Read in
    the workdir. That cost 9 og reads + 3 `ls` + 1 md read, and probably most of the 22 attempts to
    trim output with `| head`. Fixed by #32. The pilot ran under the defect, so it counts as
    calibration and the full run starts fresh.
  - **Found later (C1.4):** `talk-semantic` failed on every real talk throughout the pilot
    (29 errors). The pilot checks counted gate denials, not tool errors. See the C1.4 incident
    and #36.
- **C1.4 — Full run.** Deliverable: 60 `result.json` files. Record the graph commit head and the
  corpus hash in `results/run-meta.json`.
  - **Incident: `talk-semantic` never worked (found and fixed mid-run, #36).** The first launch
    (`bench run --max-spend 40`, 22:38) was stopped at 34/60: 18 markdown and 16 omnigraph runs,
    all `ok`, $17.62 recorded, plus 4 runs that were in flight when it was killed (no
    `result.json`, their spend unrecorded).
    - *Symptom.* Every `talk-semantic <talk> <q>` call with a real `ia-aie-…` id failed with
      `search-ordered query produced rows without its 'c._distance' ranking column`. Calls with a
      wrong id returned 0 rows, which is why a naive count showed some "successes": 24 non-errors
      vs 52 errors in this run, and 14 vs 29 in the pilot. None of them returned a passage: the
      non-errors were empty results for a wrong id, `--help` calls or gate denials.
    - *Root cause.* An Omnigraph 0.11.0 engine limit. A `nearest()` target must be the root scan
      of its match. `talk_semantic` declared `$a: InformationArtifact { slug: $talk }` first, so
      the plan scanned the artifact and reached `$c` by traversal. No scan ran the vector search,
      no `_distance` column existed, and the engine's guard (`exec/query.rs`) refused the rows
      rather than returning them unranked. Upstream this is rule T26, "search and rank targets
      must be scan-rooted" (omnigraph `361c2f02`), which turns the shape into a compile error. It
      sits on the `search-contracts-p0-p1` branch and is not in v0.11.0. That's why `omnigraph
      lint` passed: 0.11 has no T26 check.
    - *Why it was missed.* The pilot guardrail counted gate denials, not tool errors, so the
      pilot's 29 failures went unnoticed. They showed up here as 7 errors in one run
      (Q06 omnigraph #2).
    - *Impact.* 52 failed calls in 11 of the 16 omnigraph runs (Q04 18, Q06 12, Q03 10, Q10 5,
      Q08 3, Q07 2, Q02 1, Q09 1). The brief (#31) names `talk-semantic` as the in-talk source of
      verbatim text, so agents kept reaching for it and lost those calls and turns. Whole-transcript
      pulls were about the same with and without the fix (`talk-chunks`: 8.8 vs 8.2 calls per
      run), so the failure did not visibly push agents to `talk-chunks`. The markdown arm never touches the graph and was not
      affected. The C1.3 pilot's omnigraph numbers carry the same defect.
    - *Scope.* All 14 search-ordered stored queries were checked; `talk_semantic` is the only one
      whose search target is not the first-declared binding.
    - *Fix.* Declare `$c: Chunk` first (`queries/traversals.gq`). The results are unchanged in
      meaning. Checked on the local graph, directly and through the reader shim: 5 ranked
      passages, all from the requested talk, and still 5 from the right talk for a question
      unrelated to it. So it scopes first and then ranks, rather than taking a global top-k and
      filtering. The brief's generated catalog is byte-identical (signature and description
      unchanged), so neither arm's prompt changed. `local-graph.sh setup` re-applied the local
      cluster (state revision 3, converged) and the server was restarted. The graph head is
      unchanged at `01M37ZANGF3QTZH8WDE3J9ZEN9`.
    - *Re-run.* The 16 omnigraph results moved to `runs/_og-broken-talk-semantic/`, and the 18
      markdown results were kept. The resume (`bench run --max-spend 30`, 23:10) ran 30
      omnigraph + 12 markdown runs: 42 ok, 0 errors, $22.52.
    - *After the fix.* In the 30 new omnigraph runs `talk-semantic` returned passages 165 times,
      with 0 `_distance` errors. All 30 empty results were for ids that don't exist: 26 were
      bracketed labels (`chatterjee-sonar-…`) passed as-is, and 4 were `ia-aie-` ids the agent built
      from a label. The other 7 calls were gate denials (`| head`). `talk-chunks` use barely moved: 8.2 calls per run, against 8.8 in the discarded
      runs.
    - *Logging note.* `bench run` prints without flushing, so a redirected `runs/full.log` fills
      only at exit. The first attempt's log is empty because it was killed. Progress was
      followed through the `result.json` files instead.
  - **Outcome (2026-09-23):**

    | | markdown | omnigraph |
    |---|---|---|
    | runs | 30/30 `ok` | 30/30 `ok` |
    | cost | $12.99 | $17.26 |
    | total time | 65.7 min | 91.6 min |
    | mean / max per run | 131 s / 352 s | 183 s / 419 s |
    | max cost per run | $1.03 | $1.45 |
    | turns per run | 2–106 | 8–126 |
    | parsed answers | 30/30 | 30/30 |
    | gate denials | 0 | 70 |

    No `capped` or `error` runs and no retries; every cost is complete (`cost_complete`), and the
    SDK's cost matches ours on both arms. No cap came close: 126 turns (42% of 300), $1.45 (15% of
    $10), 419 s (23% of 30 min). All 60 runs share graph head `01M37ZANGF3QTZH8WDE3J9ZEN9`, corpus
    `63c73703…`, CLI 2.1.280 and SDK 0.2.158 (`results/run-meta.json`). C1.4 spent $40.14 as recorded:
    $30.25 in the kept runs and $9.89 in the 16 discarded omnigraph runs. The 4 runs killed
    mid-flight add an unrecorded amount on top.

**Exit guardrails — Phase C1 → Epic D**

| Guardrail | Criteria (pass/fail) | Status | Actual outcome |
|-----------|----------------------|--------|----------------|
| Pilot clean | 20/20 runs `ok` or `capped` with a clear reason; 0 sandbox escapes in the traces | ✅ | 20/20 `ok` (no capped runs, errors or retries). 0 sandbox escapes: replaying the gate against each run's real cwd matched every live result. 35 calls were denied: 22 shell operators and 12 reads of saved tool output (a harness defect, fixed by #32), plus 1 markdown read of saved output. |
| Contract followed | ≥ 90% of pilot answers carry a parseable JSON block (otherwise fix the prompt, not the scorer) | ✅ | 20/20 answers carry a parseable JSON block. Quick verbatim check: md 112/128 quotes (88%), og 90/109 (83%). Q10 correct on both arms (no claims). |
| Caps fixed | Final caps logged in §6 before the full run | ✅ | Observed maxima: 124 turns (Q07 og), $1.05 per run, 366 s. Caps kept at 300 turns (2.4×), $10 (9.5×), 30 min (4.9×); decision #33. |
| Graph mis-link fixed (before C1.4) | The local graph attributes Chatterjee's 24 chunks to `ia-aie-chatterjee-guide-verify-solve` (revised by #34; the tracked seed and production graph are a follow-up) | ✅ | Local graph rebuilt via `local-graph.sh load`, which now runs `bench relink-chunks` on the embedded parts. `talk-chunks` returns 13 for Shaukat and 24 for Chatterjee, each opening with the right speaker. `top-patterns` still returns 18; head `01M37ZANGF3QTZH8WDE3J9ZEN9`. The tracked seed is unchanged. |
| Full run | 60/60 `result.json` written; no `error` status left unexplained | ✅ | 60/60 `ok`: no `error` or `capped` runs, no retries, all 30 answers per arm parse. 0 sandbox escapes: in every run the replayed gate's denials match the calls denied live. The 70 og denials are 66 shell operators, 3 non-`omnigraph` commands (2 `grep`, 1 unknown verb) and 1 Read outside the scratch dir; md had none. The og arm was re-run in full after the `talk_semantic` fix (#36), so no counted run used the broken query (0 `_distance` errors across all 60 traces). |

---

### Epic D — Scorer  ·  MVP

**Goal:** turn the 60 answers into grounding, hallucination and correctness numbers without a gold set.
**Success metrics:** the scorer passes its own calibration checks. Every number in the report traces back to a stored judgment.

#### Phase D1 — Grounding and hallucination

| Step | Description | Status | Notes |
|------|-------------|--------|-------|
| D1.1 | Parse the contract block and claims | ✅ | `parse.normalise` → `Answer` / `Item` / `Claim`; 13 tests, 6 mutations caught; 60 C1.4 answers: 0 unparseable, 286 items, 710 claims |
| D1.2 | Mechanical quote check against the corpus | ✅ | `verify.Corpus` + `corpus.talk_labels`; `spliced` added (#37); 20 tests, 14 of 15 mutations caught (the 15th can't change a result); C1.4 verbatim: md 99.2%, og 97.2% |
| D1.3 | Judge: does the quote support the claim? | 🔄 | Judge + `bench score` runner done (stubbed tests). Pilot: 10/10 judged, $0.10 ($0.0104 a claim), 9 supported / 1 partial. The full pass (685 requests left, about $7.10) waits for your go |
| D1.4 | Judge: uncited factual statements in the prose | 🔲 | |
| D1.5 | Scorer calibration on planted claims | 🔲 | |

**Steps (detail):**

- **D1.1 — Parse.** Deliverable: `src/bench/parse.py`: `answer_block` (landed with C1.1) and
  `normalise(answer_json) -> Answer`, which turns a run's `answer_json` into fixed-shape items and
  claims for D1.2–D2.4. Normalising only fixes form: it never drops a claim for its content, and
  no flag changes a score by itself. Flags are counted per arm as contract deviations.
  - **Unparseable.** Takes the last fenced `json` block in the answer. If there is no block, or it
    isn't valid JSON or a JSON object, the run is `unparseable`: no items and no claims, so all
    claims count as zero.
  - **Lists.** A missing or non-list `items` or `claims` counts as empty and flags the answer
    (`bad_items`, `bad_claims`). List entries that aren't objects are dropped and counted
    (`dropped_items`, `dropped_claims`).
  - **Text fields** are trimmed. A number becomes its string; anything else that isn't a string
    becomes `""`.
  - **Items** keep their list order as `position` (1-based). `rank` and `talk_count` are kept as
    given when they are integers, otherwise `None`. Tied ranks (`1, 1, 3`) are fine: 10 of the 60
    C1.4 answers use them. D2.1's top-5 overlap uses `position`.
  - **Claims** keep their order and their `index` in the agent's list, which is how later steps
    refer to a claim (run + index). They are never deduplicated: the same quote backing two items
    counts as two claims (7 cases in C1.4).
    - `talk`: brackets around a chunk label are stripped, so `[label]` and `label` both become
      `label`. `talk_raw` keeps what the agent wrote. All 127 non-`ia-aie-` citations in C1.4 are
      bare labels, all from the Omnigraph arm (its brief shows them with brackets). An empty
      `talk` is flagged `missing_talk`.
    - `claim`: when missing or empty, it falls back to the claim's `item` label and is flagged
      `claim_from_item`. One C1.4 answer (Q01 markdown #2) wrote all 20 claims as item + talk +
      quote. With no item either, it is `""` and flagged `missing_claim`.
    - `item`: `""` means the claim supports no list entry. Otherwise it links to the first item
      whose label matches exactly after trimming (`item_position`). A label that matches no item
      keeps its text, gets `item_position: None` and is flagged `unknown_item` (1 case in C1.4:
      "AWS" against "AWS (Amazon Web Services)"). D2.1's clustering treats it as a label of its
      own.
    - `quote`: kept as written apart from trimming, with `quote_words`. Outside the contract's
      8–40 words it is flagged `short_quote` or `long_quote` (14 and 3 in C1.4) but is still
      checked. An empty quote is flagged `missing_quote`; D1.2 treats it as `not_found`.
  - **Checked** on the 60 C1.4 answers: 0 unparseable, nothing dropped, 286 items, 710 claims.
    Flags: markdown 20 `claim_from_item`, 11 `short_quote`, 3 `long_quote`; omnigraph 1
    `unknown_item`, 3 `short_quote`, and 127 label citations.
- **D1.2 — Quote check.** Deliverable: `src/bench/verify.py` (`Corpus.load`, `Corpus.check(talk,
  quote) -> QuoteCheck`), plus `corpus.talk_labels` for the label map.
  - Resolve `talk` first. It may be a talk id (`ia-aie-…`) or a chunk label (D1.1 has stripped
    any brackets); a label maps to its talk through `PartOfArtifact` in `seed/chunks` plus
    `CHUNK_TALK_OVERRIDES`.
  - Only the transcript counts: the talk file without its header, so quoting the title matches
    nothing.
  - Both sides are normalised the same way: lowercase, apostrophes dropped (`isn’t` = `isnt`),
    every other non-word character turned into a space, and whitespace collapsed. A quote may run
    across a chunk boundary.
  - Outcomes, in order:
    - `exact`: the normalised quote occurs in the cited talk on word boundaries
    - `fuzzy`: rapidfuzz `partial_ratio ≥ 90` against the cited talk. Short quotes get less
      slack: one wrong word in 12 words scores about 87, in 25 words about 96.
    - `spliced`: the quote joins passages with an ellipsis (`...` or `…`), and every piece of
      4+ words is `exact` or `fuzzy` in the cited talk. Shorter pieces are ignored, but at least
      one piece must qualify. `score` is the lowest piece's. Splices are only checked against the
      cited talk; one that isn't there goes on to the whole-quote search below (#37).
    - `wrong_talk`: not in the cited talk, but exact or fuzzy in another one (`found_in`: the
      first exact match by id, else the best fuzzy one)
    - `not_found`
  - A `talk` that resolves to nothing (empty, an invented id or an unknown label) has no text of
    its own, so its quote can only be `wrong_talk` or `not_found`, with `talk: None`. Both count as
    hallucinated, so this only makes the label more precise. An empty quote is `not_found`.
  - `score` is the best `partial_ratio` in the cited talk (100 for `exact`, 0 when unresolved).
  - No LLM involved. Checking a quote against all 337 talks takes about 0.02 s.
  - **Checked** on the 710 C1.4 claims (0.2 s for all of them):

    | | exact | fuzzy | spliced | wrong_talk | not_found | verbatim |
    |---|---|---|---|---|---|---|
    | markdown (386) | 342 | 16 | 25 | 0 | 3 | 99.2% |
    | omnigraph (324) | 258 | 15 | 42 | 1 | 8 | 97.2% |

    Before `spliced`, verbatim was 92.7% and 84.3%. What's left is real. Most misses are
    paraphrases (best score in the cited talk 52–89). The only `wrong_talk` is a real quote cited
    to an invented id close to the real one. Two omnigraph claims cite a pattern or signal slug
    (`pat-agent-supply-chain`, `sig-dependency-pr-70kloc`) and quote its brief: the
    paraphrased-brief risk in §5, seen twice in 324 claims.
- **D1.3 — Support judge.** Deliverable: `src/bench/judge.py::support` (plus the shared judge
  cache and OpenRouter client), `prompts/judge_support.md` and `verify.Corpus.context`.
  - Opus 5.5 gets the claim, the quote and the transcript around it (±1 chunk).
  - It returns `supported | partial | unsupported` with a one-line reason, via structured output.
  - Judgments are cached by hash of the inputs, so rescoring costs nothing.
  - **Which claims.** Only claims whose quote is `exact`, `fuzzy` or `spliced` in the cited talk.
    A `wrong_talk` or `not_found` claim is hallucinated whatever the judge says, so it isn't sent.
  - **What the judge sees.** The claim, the list entry it supports (if any), the quote, and the
    transcript around it: for each quoted piece (the whole quote, or each 4+ word piece of a
    splice), the chunk that matches it best plus one chunk either side, in talk order, with `[…]`
    between runs that don't touch. It never sees the arm, the run or the question, so it judges
    blind. A claim that is only a topic label (`claim_from_item`) is read as "the talk discusses
    this topic".
  - **Request.** `anthropic/claude-opus-5.5` through OpenRouter with the `anthropic` SDK:
    `output_config` with `effort: high` and a JSON schema (`verdict` enum, `reason`), no
    `thinking` parameter (Opus 5.5 always thinks adaptively), `max_tokens` 16000.
  - **Cache.** Each request is hashed (SHA-256 of its canonical JSON, prompt included) and saved
    with its response and token usage as `runs/_judge/<hash>.json`. A cached request is never sent
    again, and any change to the prompt changes every hash. Cost is usage × `provider.PRICES`.
  - **Failures.** A refusal, a `max_tokens` stop, or output outside the schema raises and is not
    cached. The SDK retries 429 and 5xx itself.
  - **Dry run** on the C1.4 claims (no API calls): 698 to judge (markdown 383, omnigraph 315).
    Requests are about 4.9k characters at the median, 9.5k at most. Contexts are 3 chunks at the
    median and 6 at most, and no splice needed a `[…]` gap. Graph words ("pattern", "signal",
    "graph") appear in the claims of both arms (18 md, 10 og), so they don't reveal the arm.
    Estimated cost is $7.5–31 depending on thinking length (300–2,000 output tokens per claim);
    a 10-claim pilot measures it first.
  - **Runner.** `bench score` (`score.py`) quote-checks every claim of `runs/Qnn/*/*`, asks the
    judge about the uncached ones (4 at a time, progress printed as it goes) and writes
    `results/scores.json` only once every claim has a verdict, so a pilot never leaves partial
    scores. Identical requests share one judgment: the 698 claims make 695 requests.
    `--dry-run` counts claims and estimates cost from the judgments already cached; `--limit N`
    asks about N claims spread evenly over the runs. A failed judgment is reported and skipped,
    so a re-run retries it.
  - **Pilot (2026-09-24):** `bench score --limit 10`: 10/10 judged, 0 errors, $0.10 ($0.0104 a
    claim; about 1,950 input and 70–390 output tokens). 9 supported, 1 partial. The partial was a
    real catch: the claim said Sonar acquired Gitar and that Gitar grades PRs, and the transcript
    says neither. Opus 5.5 served every call with the schema honoured. Adaptive thinking used 0–277
    tokens, so most claims need none even at `high` effort. Our computed cost matches OpenRouter's
    `upstream_inference_cost` exactly. The full pass is about $7.10 for the 685 requests left.
- **D1.4 — Uncited statements.** Deliverable: `judge.py::uncited`. The judge lists factual
  statements in the prose that no claim covers. The count goes into the report.
- **D1.5 — Calibration.** Deliverable: `tests/test_scorer_calibration.py`.
  - Plants 10 claims with known labels: 5 real quotes, 2 real quotes paired with the wrong
    claim, 2 invented quotes, and 1 real quote cited to the wrong talk.
  - Requires the scorer to get ≥ 9/10 right.
  - This checks the scorer, not the arms. It needs no human review of answers.

  A claim counts as **grounded** when its quote is `exact`, `fuzzy` or `spliced` **and** the judge rates it
  `supported`. It counts as **hallucinated** when its quote is `not_found` or `wrong_talk`, or
  the judge rates it `unsupported`. `partial` gets its own bucket.

**Exit guardrails — Phase D1 → D2**

| Guardrail | Criteria (pass/fail) | Status | Actual outcome |
|-----------|----------------------|--------|----------------|
| Calibrated | ≥ 9/10 planted claims classified correctly | 🔲 | |
| Deterministic | Rescoring from cache reproduces identical numbers | 🔲 | |

#### Phase D2 — Correctness without a gold set

| Step | Description | Status | Notes |
|------|-------------|--------|-------|
| D2.1 | Pooled recall for list questions | 🔲 | |
| D2.2 | Blind pairwise quality judge | 🔲 | |
| D2.3 | Run-to-run consistency | 🔲 | |
| D2.4 | Absence scoring (Q10) | 🔲 | |

**Steps (detail):**

- **D2.1 — Pooled recall.** Deliverable: `src/bench/score.py::pooled_recall`.
  - For `talk_set` questions, items are talk slugs.
  - For `company_set` and `ranked_list` questions, the judge clusters item labels from every run
    of both arms into canonical items (e.g. "evals" = "agent evaluation").
  - The **pool** is every canonical item with at least one grounded claim.
  - Recall for a run is the share of the pool it contains. For `ranked_list`, also report overlap
    within the top 5.
  - Items neither arm found are invisible to the pool; the report says so.
- **D2.2 — Pairwise judge.** Deliverable: `judge.py::pairwise`.
  - For each question, pair run *i* of one arm with run *i* of the other: 3 pairings × 10
    questions = 30.
  - The judge gets the question, both answers labelled A and B, and each answer's grounding
    annotations, so a confident but ungrounded answer can't win.
  - It rates coverage, specificity and correctness, and returns A, B or tie.
  - Each pairing is judged twice with the order swapped. An arm wins only if it wins both
    orders; anything else is a tie.
- **D2.3 — Consistency.** Deliverable: mean Jaccard similarity of each arm's item sets across
  its 3 runs, per list question.
- **D2.4 — Absence.** Deliverable: Q10 is correct when the answer says nothing relevant was found
  and makes no grounded claim of a talk. Any claim that a talk covers it is a hallucination.

**Exit guardrails — Phase D2 → Epic E**

| Guardrail | Criteria (pass/fail) | Status | Actual outcome |
|-----------|----------------------|--------|----------------|
| Position bias checked | Swapped-order agreement ≥ 80% (if lower, report it and treat those pairings as ties) | 🔲 | |
| All scored | Every run has grounding, recall (where applicable) and pairwise results | 🔲 | |

---

### Epic E — Report  ·  MVP

**Goal:** a single page that shows the comparison honestly and can go straight into a demo.
**Success metrics:** `results/results.md` regenerates from `runs/` with one command, with no hand-edited numbers.

#### Phase E1 — Results

| Step | Description | Status | Notes |
|------|-------------|--------|-------|
| E1.1 | Headline two-column table | 🔲 | |
| E1.2 | Per-question table | 🔲 | |
| E1.3 | Three side-by-side showcase traces | 🔲 | |
| E1.4 | Method notes and footnotes | 🔲 | |

**Steps (detail):**

- **E1.1 — Headline table.** Deliverable: `src/bench/report.py` and `bench report`, writing
  `results/results.md` and `results/scores.json`.

  | Metric | Agent + Omnigraph | Agent + Markdown files |
  |---|---|---|
  | Answer quality — pairwise wins / ties / losses (30 pairings) | | |
  | Pooled recall, list questions — mean | | |
  | Run-to-run consistency — mean item Jaccard | | |
  | Claims per answer — mean | | |
  | Grounded claims (verbatim quote + supported) | | |
  | Hallucinated claims (quote not found, wrong talk, or unsupported) | | |
  | Uncited factual statements per answer — mean | | |
  | Absence question (Q10) answered correctly | x / 3 | x / 3 |
  | Time per question — median / p90 | | |
  | Cost per question — mean (total for 30 runs) | | |
  | Tokens per question — input (incl. cache reads) / output | | |
  | Turns / tool calls per question — mean | | |
  | Capped or failed runs | | |

- **E1.2 — Per-question table.** Deliverable: one row per question with the winner, recall,
  grounded %, hallucinated %, median time and mean cost for each arm.
- **E1.3 — Showcase traces.** Deliverable: pick 3 questions (one aggregate win, one lookup, one
  loss or tie). Show them side by side: the tool calls in order (collapsed), an excerpt of the
  answer, and the metrics.
- **E1.4 — Method notes.** Deliverable: footnotes covering:
  - Sonnet 5, no subagents, 3 runs
  - the judge model and its cost, listed separately from the arms' cost
  - correctness is relative, with no gold set
  - graph build cost is excluded
  - `total_cost_usd` is the SDK's estimate
  - the graph commit and corpus hash
  - the run date

**Exit guardrails — Epic E → done**

| Guardrail | Criteria (pass/fail) | Status | Actual outcome |
|-----------|----------------------|--------|----------------|
| Reproducible | `uv run bench score && uv run bench report` rebuilds results.md byte-identical from cache | 🔲 | |
| Honest | Footnotes state n, the relative-correctness caveat and the build-cost exclusion | 🔲 | |

---

### Epic F — Extensions  ·  Post-MVP

**Goal:** widen the comparison once the MVP table exists.
**Success metrics:** each extension adds a column or rows to the same report without changing the MVP numbers.

#### Phase F1 — Candidates (unordered)

| Step | Description | Status | Notes |
|------|-------------|--------|-------|
| F1.1 | Grow the question set to ~40, still weighted to aggregation | 🔲 | |
| F1.2 | Re-run both arms on Opus 5.5 | 🔲 | Does a stronger model close the gap? |
| F1.3 | Subagent variant of the markdown arm (fan-out map-reduce) | 🔲 | Strongest raw baseline for aggregation |
| F1.4 | "No tools" floor, to measure what the model already knows | 🔲 | |
| F1.5 | Long-context arm on a subset of talks that fits in 1M tokens | 🔲 | |
| F1.6 | Publish the report as a shareable page | 🔲 | |
| F1.7 | Judge through the Batches API to halve scoring cost | 🔲 | |

---

## 5. Risk register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Arms inherit user/project settings, CLAUDE.md, hooks or plugins (the SDK loads them by default) | High | High | `setting_sources=[]`, `strict_mcp_config=True`, cwd outside the repo, A2.4 probe gate |
| The Omnigraph agent "quotes" paraphrased signal briefs rather than transcript text | High | Med | The contract requires verbatim transcript text, and the brief says quotes come from `talk-chunks` / `hybrid-search` / `talk-semantic`. If it persists, report it as a finding. |
| The markdown arm hits turn or budget caps on aggregate questions | Med | High | Generous pilot caps. Set final caps after the pilot and log them. Capped runs are visible in the table. |
| Large query output gets truncated or spilled to a file by the Bash tool | Med | Med | The Omnigraph arm gets `Read` limited to its own scratch dir. Check spill behaviour in the pilot. |
| No gold set: an item both arms miss can't be seen, and recall is relative | Certain | Med | Stated in the report. Absolute recall is a possible later extension (per-talk map pass). |
| Judge bias: position, or favoring longer answers | Med | Med | Both orders, win requires both, grounding annotations given to the judge, calibration test |
| 10 questions × 3 runs is a small sample | Certain | Med | Show per-question results next to the aggregates. Avoid claims stronger than the data supports. |
| Server-side `nearest()` needs Gemini; 429s during runs | Med | Low | Retry, then `error`; errors are listed in the report |
| Caption garbles make quotes look wrong | Low | Low | Garbled text is still verbatim; fuzzy matching tolerates punctuation |
| Graph data defects skew the Omnigraph arm (known: Chatterjee's chunks attached to Shaukat's talk) | Certain (one known) | Med | Fix the known one before C1.4. The corpus build fails on any other talk that mixes two transcripts. Report any others found in the traces. |
| Sonnet 5 already knows some talks (published Apr–Sep 2026) | Low | Med | Affects both arms equally; the F1.4 no-tools floor measures it |
| A stored query the brief recommends fails at runtime although it lints (happened: `talk_semantic`, #36) | Occurred | High | Check the traces for tool errors, not only gate denials. Call every query the brief names once with a real id before a paid run. The one found is fixed; the other 13 search queries have the safe shape. |

---

## 6. Decision log

| # | Date | Decision | Context | Decided by |
|---|------|----------|---------|------------|
| 1 | 2026-09-23 | Benchmark lives in `bench/` inside the graph repo | Exception to the "graph definition only" rule; corpus, runs and credentials stay gitignored | Roman Pronskiy |
| 2 | 2026-09-23 | Two arms only: Agent + Omnigraph vs Agent + Markdown files; the output is a two-column table | This is a demo of the graph's value against raw transcripts | Roman Pronskiy |
| 3 | 2026-09-23 | Both arms run on `claude-sonnet-5` | Cost for 60+ runs; the difference between arms shows up just as clearly | Roman Pronskiy |
| 4 | 2026-09-23 | No subagents in either arm | Isolates the data interface from orchestration | Roman Pronskiy |
| 5 | 2026-09-23 | No gold answers and no human review; correctness via pooled recall + blind pairwise judge | You chose to keep it a comparison table | Roman Pronskiy |
| 6 | 2026-09-23 | Hallucination/grounding measured by verbatim-quote check + judge support check | Works without a gold set and applies equally to both arms | Roman Pronskiy |
| 7 | 2026-09-23 | Time and cost measured per run from the SDK `ResultMessage` plus harness wall clock | Wanted time and cost as explicit metrics | Roman Pronskiy |
| 8 | 2026-09-23 | Graph build cost excluded; per-question numbers only | You chose per-question only | Roman Pronskiy |
| 9 | 2026-09-23 | Shortlist of 10 questions, 8 of them aggregate or multi-hop | A shortlist for now, with more aggregated questions | Roman Pronskiy |
| 10 | 2026-09-23 | 3 runs per question per arm | Shows variance while keeping the run count at 60 | Roman Pronskiy |
| 11 | 2026-09-23 | Harness is the Claude Agent SDK in Python, not `claude -p` | Needs isolation control and per-run metrics in code | Roman Pronskiy |
| 12 | 2026-09-23 | Corpus rebuilt from `seed/chunks` (336 talks), not the original transcripts | `transcripts/` isn't on this machine; chunks join back together without overlap | Roman Pronskiy |
| 13 | 2026-09-23 | Judge is `claude-opus-5-5` at explicit `high` effort | Stronger than and different from the agent model | Roman Pronskiy |
| 14 | 2026-09-23 | Omnigraph arm uses the act-reader token through a shim | Read-only access, without touching the analyst login | Roman Pronskiy |
| 15 | 2026-09-23 | Local `main` rebased onto `origin/graph-0.11-upgrade` (c97a0d2); the corpus reads the 0.11 seed format (top-level `id`) | The graph moved to Omnigraph 0.11 (storage v9, root `spike-intel-011`); the benchmark targets that graph | Roman Pronskiy |
| 16 | 2026-09-23 | Corpus has 337 talks, not 336; supersedes #12's count. Chatterjee's chunks are split from Shaukat's talk by a documented override, and the graph gets fixed before the full run (C1.4 gate). | The "two prefixes on one talk" was a graph mis-link from the 2026-09-08 audit backfill, not a joint session. Splitting now keeps the markdown arm true to the real talks. Fixing the graph before C1.4 keeps the Omnigraph arm from being scored "wrong talk" on Sonar quotes. | Roman Pronskiy |
| 17 | 2026-09-23 | Arm gates run as a PreToolUse hook on every tool call; `can_use_tool` is only a deny-all backstop. The Omnigraph arm is limited to `alias`/`query` with an allowlist of four flags. | Reading SDK 0.2.158 showed `can_use_tool` only fires for calls that need permission. `omnigraph query` also takes ad-hoc GQ, direct store access, `--as` and `--params-file`, all of which would bypass the stored-query interface. | Roman Pronskiy |
| 18 | 2026-09-23 | The reader-only CLI uses `OMNIGRAPH_HOME` + `OMNIGRAPH_PROFILE`, not a `HOME` override. `bench shim` takes the reader token on stdin only. | Found in the 0.11 binary, and resolves the open question on a config path. Overriding `HOME` would also move the agent's own config. Stdin keeps the token out of argv and shell history. The stored credential beats `OMNIGRAPH_BEARER_TOKEN` (checked against a local echo server). | Roman Pronskiy |
| 19 | 2026-09-23 | Both arms get a custom system prompt (contract + brief), not the Claude Code preset | The same framing for both arms, without coding-agent instructions or environment noise. The brief states the working directory because Read needs absolute paths. | Roman Pronskiy |
| 20 | 2026-09-23 | A claim's `talk` may be the `ia-aie-…` id or a chunk's `[label]`; the scorer maps labels to talks | `hybrid_chunks` and `related_chunks` return only chunk text and index. Requiring the `ia-aie-` id would penalize the graph arm for the shape of its query output rather than for its grounding. | Roman Pronskiy |
| 21 | 2026-09-23 | Agents and judge run through OpenRouter (`anthropic/claude-sonnet-5`, `anthropic/claude-opus-5.5`) | You added an OpenRouter key as the billing account. OpenRouter documents an Anthropic-compatible endpoint for Claude Code. | Roman Pronskiy |
| 22 | 2026-09-23 | Cost = usage × a recorded OpenRouter price snapshot; the SDK's `total_cost_usd` is only a cross-check | Exact and reproducible, and it doesn't depend on Claude Code knowing OpenRouter model ids | Roman Pronskiy |
| 23 | 2026-09-23 | The benchmark uses a local file-backed 0.11 graph under `bench/.graph/`, with chunks embedded by `google/gemini-embedding-2-preview` through OpenRouter (`openai-compatible` provider) | There's no S3 store or Gemini key here. The 0.11 binary supports `openai-compatible\|openai\|gemini\|mock`, and OpenRouter serves the seed's exact embedding model (3072-d, verified). | Roman Pronskiy |
| 24 | 2026-09-23 | Cost is priced from `ResultMessage.model_usage`, not `usage`; refines #22 | The probe showed `usage` misses part of the session. `model_usage` at OpenRouter prices reproduces the SDK's `total_cost_usd` exactly. | Roman Pronskiy |
| 25 | 2026-09-23 | Each run gets its own `CLAUDE_CONFIG_DIR` | This keeps the bundled CLI entirely off `~/.claude`: sessions, `.claude.json`, plugins, memory. It adds to `setting_sources=[]`. | Roman Pronskiy |
| 26 | 2026-09-23 | The CLI's own `…@builtin` plugins are allowed by the isolation check | `telemetry@builtin` ships with CLI 2.1.280 and doesn't come from any user setting. Any other plugin still fails the probe. | Roman Pronskiy |
| 27 | 2026-09-23 | Both arms run `anthropic/claude-sonnet-5[1m]` (1M context) | Through OpenRouter the CLI assumed 200k, and the markdown arm would compact early. A live probe confirmed `contextWindow: 1000000`, init model `…[1m]`, and cost matching the SDK. OpenRouter prices Sonnet 5 flat across the 1M window. | Roman Pronskiy |
| 28 | 2026-09-23 | Q05 and Q08 replaced with questions that no graph pattern covers (talks per company and what each focused on; voice/robotics vs coding-agent concerns) | Five of the ten drafts mapped almost one-to-one onto the graph's precomputed patterns (memory layer, agent supply chain, verification gap, harness over model, contradictions). Two neutral aggregations show whether the graph helps beyond its prepared themes. The other three pattern-aligned questions stay and are named in the report's method notes. | Roman Pronskiy |
| 29 | 2026-09-23 | Run caps are code constants (`arms.py`: 100 turns, $10 per run; `run.py`: 30 min, 2 retries); no `bench.toml` | Fewer moving parts; each cap sits next to what enforces it. Final values get revisited after the pilot (C1 guardrail "Caps fixed"). | Roman Pronskiy |
| 30 | 2026-09-23 | `max_turns` raised from 100 to 300 | 100 was a placeholder. A turn cap that binds on aggregate questions would cut the markdown arm off and distort both quality and cost. At 300 it only guards against a runaway loop, and $10 per run plus 30 minutes are the real limits. Final caps get set after the pilot from the observed maximum turns and cost (about 2× headroom). | Roman Pronskiy |
| 31 | 2026-09-23 | All 89 stored read queries get an explicit `@description` (49 added in `queries/*.gq`, docs only). The Omnigraph brief lists which queries return verbatim Chunk text. Q01 re-run on the Omnigraph arm. | In the Q01 calibration the graph agent used `signal-evidence` 24 times but also pulled 19 whole transcripts with `talk-chunks` ($0.99, 1.13M cache reads). 42 of 89 catalog entries had no description, `signal-evidence` among them: the queries' `//` comments sit one blank line above and the generator deliberately skips those. This is interface documentation, not a new capability. The first Q01 run is kept in `runs/_before-query-docs/` as a before/after point. A new `pattern-quotes` query (option 3) was deferred as a possible "graph v2" column. | Roman Pronskiy |
| 32 | 2026-09-23 | Both gates allow Read of the run's own saved tool output (`<claude-home>/…/tool-results/…`, nothing else in claude-home); both briefs carry the same one-line note | The pilot showed the CLI saves oversized output there and the gates blocked it. The og arm hit it 9×, and the md arm 1×. A harness defect, not a tuning of either arm. | Roman Pronskiy |
| 33 | 2026-09-23 | Final caps: 300 turns, $10 per run, 30 min per run | Pilot maxima were 124 turns, $1.05 and 366 s; every cap has at least 2× headroom, so none of them shaped a result. | Roman Pronskiy |
| 34 | 2026-09-23 | The mis-link is fixed in the benchmark's local graph only. `CHUNK_TALK_OVERRIDES` is the single mapping for both the corpus and the graph (`bench relink-chunks` on the embedded parts, run by `local-graph.sh load`). The tracked seed and production graph are a follow-up for the maintainer. | Fixing production needs production access and a delete path for key-less edges, which has no stored mutation. The benchmark only needs its own graph and corpus to agree, and they now share one mapping. Chatterjee's 5 signals still have no evidence passages (that needs the extraction pipeline), and one Shaukat signal keeps a Chatterjee passage as its evidence. | Roman Pronskiy |
| 35 | 2026-09-23 | The fix is ported to the tracked seed: `bench relink-chunks ../seed/chunks` re-points exactly 24 `PartOfArtifact` rows in `seed/chunks/part-03.jsonl` (same formatting, only `to` changes). `CHUNK_TALK_OVERRIDES` is emptied; README says chunks cover 337 talks and documents the seed being ahead of the served graph. | You asked to port the fix. This departs from the repo's "regenerate the seed from `omnigraph export`, never hand-edit" rule: the served production graph still has the mis-link, so the seed runs ahead of it until the graph maintainer re-points the 24 edges there. The corpus rebuilds byte-identical (same fingerprint), and the one evidence edge from Shaukat's `sig-cmu-velocity-fade` to Chatterjee #1 is left alone because both passages discuss the same Carnegie Mellon study. | Roman Pronskiy |
| 36 | 2026-09-23 | `talk_semantic` in `queries/traversals.gq` declares `$c: Chunk` first (was `$a: InformationArtifact { slug: $talk }` first), with a comment on why. The local cluster is re-applied and the server restarted. The C1.4 omnigraph runs made before the fix move to `runs/_og-broken-talk-semantic/` and are all re-run. The 18 markdown runs already finished are kept. | On 0.11.0 a `nearest()` whose target is reached by traversal fails at runtime; later engines reject it at compile time as T26. The query had never worked for a real talk id, in the pilot (29 errors) or in the first C1.4 attempt (52 errors in 11/16 runs), and the brief (#31) points agents at it. This fixes a broken tool; it adds no capability. Same results, same description, same brief text. The markdown arm doesn't read the graph and its prompt didn't change, so its runs stay valid. Full detail in the C1.4 incident note. | Roman Pronskiy |
| 37 | 2026-09-24 | D1.2 adds a `spliced` outcome: a quote that joins real passages of the cited talk with an ellipsis counts like `fuzzy` for grounding. It is reported separately as a contract deviation, and the support judge still checks it. | On the C1.4 answers, most `not_found` quotes were splices whose every piece is in the cited talk: markdown 25 of 28, omnigraph 42 of 50. Scoring them as hallucinations would make that metric mostly measure ellipsis use, and would hit the omnigraph arm harder. The contract asks for exact copies, so splices stay visible as their own status rather than being folded into `exact`. | Roman Pronskiy |

---

## 7. Open questions

- [x] ~~Billing: API key or Claude Code login?~~ OpenRouter (decision #21).
- [ ] Final caps (`max_turns`, `max_budget_usd`, wall clock) after the pilot. Do they stay the same for both arms?
- [x] ~~Does the `omnigraph` CLI accept a config path or profile env var?~~ Yes: `OMNIGRAPH_HOME` and `OMNIGRAPH_PROFILE` (decision #18).
- [x] ~~Does `HookMatcher(matcher=None)` match every tool?~~ Yes: the A2.4 probe saw our reason on every denial across Read, Grep, Glob and Bash.
- [x] ~~Context window: 200k or 1M?~~ 1M for both arms (decision #27). Verified live: `contextWindow: 1000000`.
- [x] ~~How does the CLI handle very large tool output?~~ It saves it to `<claude-home>/projects/<cwd>/<session>/tool-results/<id>.txt` and tells the agent to Read it (decision #32).
- [ ] Commit `runs/` traces for the demo, or only `results/`? Currently runs are gitignored.
- [ ] Follow-up (graph maintainer): re-point Chatterjee's 24 chunks in the production 0.11 graph so it matches the seed (#35), and derive evidence passages for his 5 signals. Then refresh the seed from an export as usual.
- [ ] Follow-up (graph maintainer): the production 0.11 server still serves the broken `talk_semantic`. `cluster apply` of the fixed `queries/traversals.gq` plus a server restart fixes it (#36). T26 in a later Omnigraph release will catch this shape at lint time.

---

## How to Update This Document

This spec is the source of truth for the build. Keep it current as work happens:

- **Status markers.** Update a step's status in its tracker table as you go: 🔲 → 🔄 → ✅. Use ⏸️ for blocked (note why in Notes) and ❌ for cut (leave the row; the strikethrough of history is useful).
- **Current focus.** Keep the pointer at the top aimed at the next actionable 🔲 step. Update it the moment you finish a step or cross a phase boundary. A stale pointer sends the next reader to the wrong place.
- **Guardrails.** When you hit a phase boundary, fill the **Actual outcome** column with what really happened and set the guardrail status. Don't advance to the next phase until its guardrails pass, or log a decision explaining why you're proceeding anyway.
- **Decisions.** Any non-trivial choice made during the build gets a new row in the Decision Log (§6). It's append-only: reversals are new rows, not edits. If the choice changes the architecture, also update the Technical Decisions snapshot (§2).
- **Spec changes.** Structural changes (new epic, re-scoped phase) get a Changelog row at the top. Keep the executive summary honest if the project's shape shifts.
- **Open questions.** When one resolves, strike it from §7 and log the decision in §6.
