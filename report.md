# Intel-Graph Report — AI Engineer World's Fair 2026

**Corpus:** 136 talks extracted from the [AI Engineer](https://www.youtube.com/@aiDotEngineer)
channel (uploads 2026-06-25 → 07-21), processed in 9 batches into per-talk SPIKE
extraction files (`extraction/`), all entities slug-linked against `seed.jsonl` +
[registry.md](extraction/registry.md). ~1,800 entities defined. Markdown only —
nothing seeded yet. Not covered: 6 scheduled premieres (unlock Jul 22–24) and one
pulled video (Lance Martin, Anthropic). AIE Europe 2026 (243 talks): untouched.

All quotes are auto-caption paraphrases. ⚠-flagged names in the registry need
verification before anything public-facing.

---

## 1. The pattern layer

### The big three (dominate the corpus)

| Pattern | Files | One-line thesis |
|---|---|---|
| `pat-verification-gap` | 76 | Generation industrialized, verification didn't; trust is being re-architected outside the model |
| `pat-harness-over-model` | 74 | Production reliability/latency/control come from deterministic scaffolding around the model, not the model |
| `pat-model-not-bottleneck` | 68 | Models are good enough; failure and value migrated to the layers around them, and the industry is productizing that periphery |

More than half of all 136 talks link at least one of these three. They are one
thesis family seen from three angles (trust / engineering / economics) — the
batch-2 registry note discusses the keep-vs-merge decision.

### Also coined during extraction

| Pattern | Files | Origin |
|---|---|---|
| `pat-value-of-judgement` | 23 | batch 5 (Osmani + Anthropic culture + Cursor FDE) — as AI industrializes execution, the durable human edge shifts to judgment |
| `pat-agent-supply-chain` | 13 | batch 1 (Yegge) — skills/MCP/extensions as a worse package ecosystem; exploitation begun |

Rejected at review (2026-07-22): `pat-html-native-medium` (batch-9 coin —
demoted to element `el-html-native-medium`, edges rehomed to
`pat-model-not-bottleneck`) and the `pat-provider-blind-ai` candidate (design
property, not a thesis) — both mechanisms, not industry-change claims.

Seed patterns held up in the wild: `pat-context-graphs` (26 files),
`pat-accelerated-research` (20), `pat-saaspocalypse` (19), `pat-sovereign-ai` (14),
`pat-new-cyber-threats` (13).

### Candidates at coin threshold (your review decisions)

Ranked by evidence weight; details in the registry batch sections.

1. **`pat-durable-execution`** (18 files despite being uncoined) — durable
   runtime / checkpoint-replay / log-as-state as an emerging stack layer.
   Evidence: ZenML Kitaru, Inngest, OpenAI sandbox cloud, Paperclip, KRAFTON
   fleet, Chronicle (Microsoft), Resonate/Synadia, Agency lang pause/resume,
   Omnara's "log is the agent" (purest statement). **Recommend coining.**
2. **`pat-ai-native-org`** (9) — org structure rebuilt around agents.
   Qualitative: Garry Tan, Anthropic (65% of PRs), Cursor FDE, Machinecraft,
   Automattic's 500-person month, Block's 3,500-engineer restructure (+ its
   layoffs dark side, held pattern-less). Quantitative: Yaron survey — 81%
   role-blur, >⅓ of teams with non-devs shipping. **Recommend coining.**
3. **`pat-benchmark-trust-crisis`** (12) — Unsloth reward hacking, Vidal
   psychometrics, Cursor RSI reward hacking, SWE-Marathon hardening arms race
   (12.8%→9%→0), Miranda persona-eval contamination (strongest), ARC-AGI-3
   governance split. **Recommend coining.**
4. **`pat-adaptive-harness` / `pat-adaptive-software`** (8/7, paired) — the
   frozen artifact dissolves: Sky Valley stem+divergences, Annicha emergent
   harnesses, Resonate spec-is-product, RELAI, Mutagent, AutoAgent, Claude Code
   dynamic workflows. Decide one-vs-two patterns at review; mild counter
   ("don't let agents design agents", Jones).
5. **`pat-agent-economy`** (8) — Alithea receipts/Froglet, MIT Nanda bazaar,
   agents provisioning GPUs (Local AI panel). Two strong + scattered weak.
6. **"Persistent agent memory as a first-class stack layer"** — newest; three
   data points in one batch (second-brain OS, Nx Polygraph, StarlightSearch
   outcome-weighted memory). Watch one more batch or coin now.

### Contested patterns (counter-evidence exists — a feature, not a bug)

- `pat-harness-over-model` — 3 ContradictsPattern edges: TNG (reasoning models
  re-absorbed pipeline steps), Shihipar (Claude Code's system prompt halved as
  models improved), Chandegra (fixed harnesses obsolete themselves). The thesis
  and its erosion are both in the graph.
- `pat-sovereign-ai` — Yaron survey: open-vs-closed drives model choice for
  only 5% of respondents.
- `pat-context-graphs` — Orbis: graph context has a corpus-churn boundary where
  cache-augmented generation wins.
- `pat-value-of-judgement` — mild counter from Snap's personal-agent-org talk.

---

## 2. Most valuable insights (cross-batch, curated)

1. **"Generation is solved; verification/specification is the frontier"** was
   independently argued by three of five frontier keynotes (Yan, Schillings,
   Meijer) and operationalized everywhere else: judge-as-classifier (Lyft),
   multilayer verification (Sonar), post-generation veto (Martin-Dye),
   property-based tests from specs (Kiro/AWS), computer-use verifiers
   (SWE-Marathon).
2. **The harness is where production happens — same model, wildly different
   outcomes.** HarnessBench: 52.4→76.2% spread on identical models. Phaidra:
   planner+deterministic-resolver held 100% correctness from 64 → 460k GPUs
   with ~300× token cut, where the LLM-native approach collapsed to 30%.
   Microsoft voice: frontier reasoning scaffolded out so Haiku-class models
   carry live lessons.
3. **But the harness thesis has a decay curve.** Prompt-shrink at Anthropic,
   TNG's pipeline re-absorption, and capability-overhang framing (Bhargava)
   all say today's scaffolding is a depreciating asset — matching Farrelly's
   "half-life" layer model (prompts weeks, models months, execution years).
4. **Judgment is the human edge. Career math changed.** Osmani's "choose what's
   worth doing", Litt's understanding-bottleneck (cognitive debt as the real
   deficit), Duolingo's discernment-not-approval (automation bias as system
   property), alpha-decay career math (capability edge ≈ one model release).
5. **Reward hacking is now an operational problem, not a thought experiment.**
   SWE-Marathon ran a live verifier-hardening arms race; Cursor sees it inside
   RSI loops; Unsloth documents anti-hacking RL methodology from model makers
   (GLM); Miranda shows the eval-contamination version for personas.
6. **Context is consolidating into a named stack layer.** Sankar's context
   layer, Castro's Foundry IQ, Daga's source-of-truth hierarchy, Atlan/company
   brains, Block's 25k-repo world model, decision traces (Neo4j, Europe
   preview) — `pat-context-graphs` is the most-validated seed thesis, with
   one honest boundary (fast-churn corpora → CAG).
7. **Agent memory is splitting from context into its own layer** — learning
   memory ≠ personalization memory (StarlightSearch), sleep cycles
   (Machinecraft), episodic auto-resolution (Datadog), session-log-as-agent
   (Omnara). Candidate pattern #6.
8. **The org chart is becoming a runtime.** Block, Automattic, Machinecraft
   (a thermoforming SMB!), Snap's personal org, Meta's parallel game teams —
   and the first layoffs directly attributed to agent autonomy (Block signal,
   deliberately held pattern-less for your read).
9. **Security's center of gravity moved to identity & provenance:** agent-scoped
   authorization (Scalekit), OAuth token exchange as agent backbone (Keycard),
   identity-aware proxies for control planes (Pomerium), attestation +
   user-held keys (Bee), signed receipts across org boundaries (Froglet),
   sleeper-agent backdoors that pass every eval (LexisNexis diff-SAE as the
   countermeasure).
10. **Voice cracked the production barrier by leaving the LLM out of the
    control loop** (both Microsoft talks, AWS turn-detection stack, JoinIn's
    multiparty floor-tracking) — the cleanest harness-over-model subdomain.
11. **RLMs (recursive language models) went from paper to movement inside one
    event** — MIT paper → RLM-Code → OpenProse → Agentica's ARC-AGI-3 jump →
    "Claude Code is finally an RLM" (Khattab, via dynamic workflows).
12. **The 2026 State of AI Engineering (n=1,048)** quantified the vibe: 81%
    role-blur, >⅓ non-devs shipping, 17% customer-facing, cost-as-SLA
    emerging, open-weights chosen on merit not ideology (5%).

---

## 3. Most frequently mentioned companies

Files-mentioning-count across 134 extraction files (a file ≈ a talk):

| # | Company | Files | Role in corpus |
|---|---|---|---|
| 1 | `co-anthropic` | 33 | Center of gravity: Claude Code/Fable/Tag/Cowork, auto mode, MCP lineage, security find-and-fix, culture session |
| 2 | `co-openai` | 18 | Codex + GPT-5.6 family, sandbox cloud, MLE-bench, hiring challenge, AGENTS.md |
| 3 | `co-cursor` | 11 | Composer models, RSI loop, FDE function, incidents-as-cautionary-tales |
| 4 | `co-google` | 9 | A2UI, A2A, WebMCP, Gemini; merge flag vs `co-google-deepmind` (6) still open |
| 5 | `co-github` | 8 | Copilot delegation, 80%-machine-generated stat, skills ecosystem |
| 6 | `co-microsoft` | 8 | Voice harness talks, Foundry/IQ, Chronicle, dev-role keynote |
| 7 | `co-aws` | 7 | Voice reference architecture, Strands/AgentCore, Kiro, token economics |
| 8 | `co-langchain` | 6 | LangGraph/deep agents (mostly as the thing people moved beyond) |
| 9 | `co-meta` | 6 | Superintelligence Labs infra, game-building experiment, internal agents |
| 10 | `co-nvidia` | 6 | DGX Spark/Station, Nemotron, PersonaPlex, local-AI push |

Notables beyond the top 10: `co-salesforce` (5 — mostly as SaaSpocalypse
casualty), `co-y-combinator` (3 — AI-native-org thesis), `co-block` +
`co-agentic-ai-foundation` (the Angie Jones restructure), `co-mit-media-lab`
(Nanda agentic web). The long tail is 150+ companies, mostly one-talk vendors —
the event's real texture is startups shipping harness-layer infrastructure.

**Read:** Anthropic's mention rate (~25% of all talks) is ecosystem gravity —
Claude Code is the de-facto reference harness (`el-claude-code`, 27 files;
`el-mcp`, 26; `el-agent-skills`, 16; `el-openclaw`, 14 — all Anthropic-lineage
elements at the top of the element frequency table alongside OpenAI's `el-codex`
at 13).

---

## 4. Numbers worth remembering

- **$830B** — six-day SaaS market-cap loss, Feb 2026 (seed, SaaSpocalypse)
- **52.4% → 76.2%** — same-model resolve-rate spread across harnesses (HarnessBench)
- **~300× / 100%-flat** — Phaidra token cut / correctness at 460k-GPU scale
- **26%** — best config (Opus 4.8 + Claude Code) on SWE-Marathon's project-scale benchmark
- **12.8% → 9% → ~0** — SWE-Marathon reward-hacking rate across verifier hardening
- **81% / >⅓ / 17%** — Yaron survey: role-blur / non-devs shipping / customer-facing
- **65%** — of Anthropic's PRs written by Claude (culture session)
- **+69%** — Block engineering-output gain post agent-org restructure
- **~3.5 months** — capability-density doubling ("densing law", Osman)
- **94%** — coding-token reduction from a local code index (Tesco talk)
- **~30% vs 2–3%** — Agentica RLM harness vs frontier baselines on ARC-AGI-3 (⚠ names unverified)
- **20–40%** — vuln-introduction rate of best models on BaxBench (Cable)

---

## 5. Other highlights

- **Protocol season:** MCP Apps (official extension), ACP (Zed), A2A (Google,
  repurposed internally at OpenGov), Froglet (agent transactions), AGENTS.md
  (vendor-neutral by design) — the interop layer is being standardized in real
  time, mostly in the open.
- **Best engineering war stories:** Form3's Patch Pilot (deterministic/agentic
  credential split), OpenAI's fork()-to-Fleet sandbox evolution, Bee's
  provider-blind wearable backend, the ESP32 physical OpenClaw terminal built
  solo in 3 months.
- **Recurring failure modes:** 100-tool schema collapse (13.6% vs 83% with
  semantic routing), fabricated success confirmations (single-loop agents),
  temp-0 non-reproducibility (batch variance + MoE routing), context rot past
  ~40% window, vector-RAG failing aggregation queries structurally.
- **Weakest-caption files** (verify before public use): Altos single-cell
  (model/paper names), ZenML "Kitaru", Tan's "G Brain", Agentica/Symbolica,
  several speaker names — all ⚠-flagged in the registry.
- **Provenance quirks documented:** one duplicate upload (Povilionis), one
  pulled video (Lance Martin), premieres appearing interleaved in the feed,
  cross-listed Europe talks inside the WF region, and the WF "Complete
  Playlist" containing only ~⅓ of the actual event uploads.

---

## 6. Where this goes next

1. **Pattern review pass** (highest leverage): decide the 6 candidate coins,
   the model-not-bottleneck ↔ harness-over-model relationship, and the
   `co-google`/`co-google-deepmind`, `co-aws`/`co-amazon` merges. Every
   decision has a pre-written rationale + rehoming list in the registry.
2. **Premiere sweep** (~Jul 24 completes the event): 6 talks.
3. **AIE Europe 2026**: 243 talks, zero covered; 18 keynotes are the wedge.
4. **Seeding**: convert reviewed extractions to `seed.jsonl` — the review
   markdown was built so this step is mechanical.
