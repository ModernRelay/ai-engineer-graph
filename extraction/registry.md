# Entity registry — shared slugs across all extractions

Single source of truth for cross-cutting entities. Per-talk extraction files
REFERENCE these by slug; they define only talk-local entities (signals,
insights, knowhows, and elements/companies/experts unique to that talk).
**[seed]** = already in `seed.jsonl`. **[batch1]** = defined in
`2026-07-20-security-track-part1.md` (reviewed).

## Patterns
- **[seed]** `pat-sovereign-ai`, `pat-saaspocalypse`, `pat-context-graphs`, `pat-new-cyber-threats`, `pat-accelerated-research`
- **[batch1]** `pat-verification-gap` — The Verification Gap (generation industrialized, verification didn't; trust re-architected outside the model)
- **[batch1]** `pat-agent-supply-chain` — The Agent Supply Chain (skills/MCP/extensions/hallucinated packages as a worse package ecosystem; exploitation begun)
- **[batch2]** `pat-model-not-bottleneck` — The Model Is Not the Bottleneck (dynamic); **[batch2]** `pat-harness-over-model` — The Harness Over the Model (dynamic); **[batch5]** `pat-value-of-judgement` — Value of Judgement (dynamic). _Full briefs in the batch-2 and batch-5 sections._
- **[batch19]** `pat-agent-memory-layer` — The Agent Memory Layer (dynamic) — persistent memory as a first-class stack layer rather than a per-product feature: systems that accumulate, synthesize and re-inject what they learn about a user, team or environment, maintained on a compute budget and updated outside the weights. **Coined 2026-08-14**, defined in `khemani-every-memory-system.md`. Contested from birth — 4 counter-edges attached at coin.
- **[batch19]** `pat-continual-learning-turn` — The Continual Learning Turn (dynamic) — the frontier of model improvement shifting from pre-training scale to post-deployment learning, making the accumulation loop rather than the base model the locus of compounding advantage. **Coined 2026-08-14**, defined in `su-neocognition-continual-learning-expertise.md`. Contested from birth — 1 counter-edge attached at coin.
- **[coined 2026-08-16]** `pat-durable-execution` — The Durable Execution Layer (dynamic) — durable runtime (state, workflows, retries, scheduling, crash-recovery) as a productized stack category below the harness; product-as-layer vs the convention counter. **6 support / 1 counter** at coin. Recommended since batch 5; ledger complete at b17.
- **[coined 2026-08-16]** `pat-benchmark-trust-crisis` — The Benchmark Trust Crisis (challenge) — benchmarks decoupling from real capability across many independent failure modes (replay/determinism with a formal proof, contamination, construction methodology, reporting threshold, simulation-awareness, task-distribution mismatch). **9 support / 2 counter** at coin.
- **[coined 2026-08-16]** `pat-ai-native-org` — The AI-Native Organization (dynamic) — companies restructuring around agent delegation (org-as-markdown, thin teams, review relocated/abolished, multiplayer-by-default), with a quantified adoption side and a dysfunction side. **11 support / 0 counter** at coin. Widest-evidenced candidate; proposed since batch 4.
- **[coined 2026-08-16]** `pat-agent-economy` — The Agent Economy (dynamic) — agents as primary economic actors (hiring humans, cartels, supply chains, receipts, agent-to-agent protocols) and the web being agentified via computer-use/browser layers and agent-legible standards. **8 support / 1 counter** at coin. ⚠ Registry flags a possible split (agent-commerce vs machine-web) — coined whole per user direction; revisit if the two legs diverge.
- **[⚑ REFRAME 2026-08-16, still uncoined]** `pat-fde-turn` → **rename to `pat-fde-rise` / "The Rise of Forward-Deployed Engineering"**. The old "turn/collapse toward product" framing was backwards (user, 2026-08-16): the thesis is the **rise** of FDE as an ascendant function — the forward-deployed engineer becoming a first-class role as vendors embed engineers in customer orgs (Anthropic, Factory, Cognition, Ramp, Sierra, Decagon, Kepler; the whole b14 FDE track). Contested from birth (Ganesh/Kepler: "this is a product strategy, not a role"). **Not coined** — no "add" given; reframed candidate awaiting a coin decision.

## Companies
- **[seed]** co-anthropic, co-google-deepmind, co-moonshot-ai, co-zylon, co-meta, co-edra, co-hornet, co-playerzero, co-sequoia, co-sap, co-nousresearch, co-klarna, co-salesforce, co-box, co-modern-relay, co-ucla
- **[batch1]** co-snyk, co-chainguard, co-replit, co-github

## Elements
- **[seed]** el-zylon, el-nanograph, el-hermes-agent, el-kimi-k25, el-mcp, el-anthropic-managed-agents, el-headless-saas, el-edra, el-hornet, el-playerzero-sim1, el-genkm, el-claude-mythos-preview, el-project-glasswing, el-permissioned-inference, el-precedent-poisoning, el-autoresearch, el-alphaevolve, el-karpathy-llm-wiki, el-erdos-ai-tools, el-claude-cowork, el-sap-ai, el-salesforce-crm, el-meta-internal-agents, el-openclaw
- **[batch1]** el-agent-skills, el-agent-hooks, el-generator-validator-separation, el-slopsquatting, el-snyk-evo, el-snyk-ads, el-snappy, el-chainguard-images, el-beads

## Experts
- **[seed]** exp-karpathy, exp-terence-tao, exp-balaji, exp-aaron-levie, exp-andrew-altshuler, exp-eugen-alpeza, exp-animesh-koratana
- **[batch1]** exp-manoj-nair, exp-steve-yegge, exp-ezra-tanzer, exp-dan-arpino

## SourceEntities
- **[seed]** source-reuters-nl, source-bloomberg-nl, source-techcrunch-bl, source-fortune-nl, source-forbes-nl, source-sequoia-bl, source-anthropic-bl, source-red-anthropic-bl, source-deepmind-bl, source-google-research-bl, source-tao-mastodon-bl, source-snyk-bl, source-paloalto-bl, source-cloudian-bl, source-moonshot-bl, source-zylon-bl
- **[batch1]** source-aie-yt — AI Engineer YouTube channel (all World's Fair talks publish here)

## Batch-2 additions (reconciled after extraction)

_20 talks (published 2026-07-20, AI Engineer World's Fair), one extraction file
per talk. Four thematic sets: security (Johner/Maida/Degges/Stanley/Korshakov),
verification & reliability (Shaukat/Lin/Dmello/Povilionis/Ramdoss),
enterprise data & agents (Daga/Petrov/Aghammadzada/Profirović/Kanukolanu),
voice & applied (Bahidika+Allou ×2, Agrawal+Wirjo, Shankhdhar, Baharlouei).
All artifacts `PublishedBySource → source-aie-yt`._

### Patterns (2 new — REVIEW: adjacent, see note)
- **[batch2]** `pat-model-not-bottleneck` — The Model Is Not the Bottleneck (dynamic) — models are good enough; production failure and value have migrated to the layers around them (config, delivery/rendering, memory, transaction/trust), and the industry is productizing that periphery. Defined in `dmello-nvidia-llm-stack-2008-database.md`; evidenced by 4 of the 5 verification-set talks.
- **[batch2]** `pat-harness-over-model` — The Harness Over the Model (dynamic) — in production agents, reliability/latency/control come from the deterministic scaffolding around the model (state machines, validators, turn-detection, rule engines), not the model's intelligence; the model is the smallest, swappable part. Defined in `bahidika-allou-msft-dont-let-llm-drive.md`; evidenced by both MSFT voice talks, AWS voice, Risa. Cross-link: `pat-verification-gap` ReliesOnPattern → `pat-harness-over-model`.
- **REVIEW — merge decision:** these two were coined independently (verification set vs voice set) and are close. Read as distinct: `pat-model-not-bottleneck` is the *industry/value* claim (where failure and productization moved), `pat-harness-over-model` the *engineering* claim (how you build for it) — keep both + cross-link `pat-harness-over-model` EnablesPattern → `pat-model-not-bottleneck`. If you read them as one thesis, merging into `pat-model-not-bottleneck` rehomes links in ~9 files.
- Candidates deliberately **not** coined (prose-flagged in review notes only, no edges): `pat-provider-blind-ai` (`korshakov-bee-privacy-intelligence.md` — **RETIRED at review 2026-07-22: design property, not a pattern; mechanism kept as elements**), `pat-agent-economy` (`povilionis-alithea-agents-need-receipts.md` — one-new-pattern budget spent).

### Companies (22 new)
- Security set: `co-form3` (fintech), `co-keycard` (security/STS), `co-dbt-labs` (data tooling), `co-bee` (AI wearable, acquired by Amazon ~Nov 2025)
- Verification set: `co-sonar` (code quality), `co-datadog` (observability), `co-nvidia` (hardware), `co-alithea-bio` (life-sciences agent infra, Froglet)
- Enterprise-data set: `co-tesla`, `co-datachain` (DVC lineage), `co-datarobot`, `co-pinterest`, `co-langchain`, `co-position2` (GTM agents)
- Voice/applied set: `co-microsoft`, `co-daily` (Daily.co — Pipecat/Smart Turn), `co-risa-labs` (oncology automation), `co-altos-labs` (biotech/cellular rejuvenation)
- Bigtech, coined on reference: `co-openai` (frontier lab; defined in both `degges-snyk-security-track-intro.md` and `petrov-datachain-physical-data-harnesses.md` — briefs compatible, single node), `co-amazon` (defined in both `korshakov-bee-privacy-intelligence.md` and `ramdoss-amazon-rendering-layer.md` — single node), `co-aws` (Amazon Web Services), `co-google`
- **REVIEW — merge flags:** `co-google` vs seed `co-google-deepmind` (keep both = corp vs lab, or merge; flagged in `ramdoss-amazon-rendering-layer.md` notes). `co-aws` vs `co-amazon` kept distinct (retail/corp vs cloud); collapse at seeding if you prefer one Amazon node.

### Experts (21 new)
- Security: `exp-moritz-johner` (co-form3), `exp-kim-maida` (co-keycard), `exp-randall-degges` (co-snyk), `exp-aaron-stanley` (co-dbt-labs), `exp-steve-korshakov` (co-bee/co-amazon)
- Verification: `exp-tariq-shaukat` (co-sonar, CEO), `exp-diane-lin` (co-datadog), `exp-lovina-dmello` (co-nvidia), `exp-armanas-povilionis` (co-alithea-bio), `exp-bala-ramdoss` (co-amazon)
- Enterprise data: `exp-ishita-daga` (co-tesla), `exp-dmitry-petrov` (co-datachain, DVC creator), `exp-elvin-aghammadzada` (co-datarobot), `exp-drasko-profirovic` (co-pinterest), `exp-sajjan-kanukolanu` (co-position2)
- Voice/applied: `exp-ornella-bahidika`, `exp-joel-allou` (both co-microsoft), `exp-chintan-agrawal`, `exp-daniel-wirjo` (both co-aws), `exp-anant-shankhdhar` (co-risa-labs), `exp-akram-baharlouei` (co-altos-labs)

### Elements (47 new)
- Security set: `el-patch-pilot`, `el-deterministic-agentic-split`, `el-firecracker`, `el-microsandbox`, `el-oauth-token-exchange`, `el-keycard`, `el-corrigibility-by-design`, `el-bee`, `el-sigstore`, `el-confidential-computing`
- Verification set: `el-sonar-vortex`, `el-multilayer-verification`, `el-active-learning`, `el-semantic-episodic-memory`, `el-ray`, `el-nist-ai-rmf`, `el-froglet`, `el-generative-ui`, `el-a2ui`
- Enterprise-data set: `el-source-of-truth-hierarchy`, `el-semantic-layer`, `el-data-harness`, `el-datachain`, `el-context-rot`, `el-progressive-disclosure`, `el-spark-medic`, `el-langgraph`, `el-buyer-context-graph`, `el-position2-intelligence`
- MSFT voice (shared by both talks): `el-ace-voice-tutor`, `el-harness-engineering`, `el-agent-state-machine`, `el-claude-haiku-45`, `el-claude-opus-47`
- AWS voice: `el-turn-detection`, `el-silero-vad`, `el-smart-turn`, `el-pipecat`
- Risa oncology: `el-risa-prior-auth`, `el-medical-necessity-agent`, `el-patient-medical-graph`, `el-payer-rule-kb`
- Altos single-cell: `el-single-cell-foundation-model`, `el-rna-seq`, `el-scgpt`, `el-flow-matching`, `el-primeflow` — ⚠ model/paper names in this talk are the weakest auto-captions of the batch; verify before public-facing use (flagged in file notes)

### SourceEntities
- reused `source-aie-yt` (all 20 talks); no new sources.

### InformationArtifacts (20 new, one per talk)
- Security: `ia-aie-johner-agent-prod-access`, `ia-aie-maida-agent-identity`, `ia-aie-degges-track-intro`, `ia-aie-stanley-jurassic-park`, `ia-aie-korshakov-privacy`
- Verification: `ia-aie-shaukat-verifiers-king`, `ia-aie-lin-agent-consistency`, `ia-aie-dmello-llm-stack`, `ia-aie-povilionis-receipts`, `ia-aie-ramdoss-rendering-layer`
- Enterprise data: `ia-aie-daga-structure-problem`, `ia-aie-petrov-physical-data`, `ia-aie-aghammadzada-skills-sdks`, `ia-aie-profirovic-spark-medic`, `ia-aie-kanukolanu-gtm-agent`
- Voice/applied: `ia-aie-msft-dont-let-llm-drive`, `ia-aie-msft-voice-no-frontier`, `ia-aie-aws-voice-interrupts`, `ia-aie-risa-oncology`, `ia-aie-altos-single-cell`

## Batch-3 additions (reconciled after extraction)

_20 talks (published 2026-07-15 → 07-19), one extraction file per talk. Four
thematic sets: engineering practice (Madabhushi/Walter/Ung/Schäfer/Tahir),
context & knowledge (Ainge/Maruthavanan/Palmer/Gupta/Castro), frontier &
keynotes (Yan/Horthy-panel/Han/Schillings/Tan), applied & product
(Shahandeh/Nanz/Bouffard/Jiang/Bonacci). All artifacts
`PublishedBySource → source-aie-yt`. Skipped: Lance Martin (Anthropic)
"Claude for Long-Horizon Tasks" — video unavailable; duplicate Povilionis
re-upload._

### Patterns (0 new)
- Zero new patterns coined across all 20 talks — every signal links to existing registry patterns (heaviest reuse: `pat-model-not-bottleneck`, `pat-harness-over-model`, `pat-verification-gap`, `pat-context-graphs`).
- Candidates flagged in review notes WITHOUT coining (no edges): "built-for-humans infrastructure breaks under agent actors" (madabhushi), "durable runtime as emerging stack category" (tahir), "content-is-code / shift-left content" (palmer), "AI adoption/UX gap" (nanz), "imagination as the new bottleneck" (bouffard), "AI-native organization" (tan), "benchmark-trust crisis" (han). Several could merge into existing patterns or each other if they recur in later batches.

### Companies (25 new)
- Eng practice: `co-scalekit` (agent auth), `co-hud` (runtime intel for coding agents), `co-lyft`, `co-sierra` (support agents, tau-bench), `co-langfuse` (LLM observability), `co-zenml`, `co-doordash`, `co-braintrust` (evals)
- Context/knowledge: `co-good-collective` (graph consultancy), `co-kalmantic-labs`, `co-uber`, `co-conductor` (⚠ disambiguation flagged in palmer file), `co-cursor` (Anysphere)
- Frontier/keynote: `co-mozilla`, `co-humanlayer`, `co-sentry`, `co-unsloth`, `co-zhipu-ai` (⚠ caption garble), `co-deepseek`
- Applied/product: `co-radicait` (in-silico PET), `co-weco` (AIDE/Aiden auto-research), `co-progress-software`, `co-cua` (computer-use infra), `co-snorkel-ai`
- `co-y-combinator` (investor) — coined identically by two agents (Tan talk + Bouffard talk); single node.

### Experts (23 new)
- Eng practice: `exp-ravi-madabhushi` (co-scalekit), `exp-may-walter` (co-hud, ⚠ name garbled in captions), `exp-nick-ung` (co-lyft), `exp-annabell-schafer` (co-langfuse), `exp-hamza-tahir` (co-zenml)
- Context/knowledge: `exp-tim-ainge` (co-good-collective), `exp-thiyagarajan-maruthavanan` (co-kalmantic-labs), `exp-matt-palmer` (co-conductor), `exp-sachin-gupta` (no company stated — no affiliation edge), `exp-pablo-castro` (co-microsoft)
- Frontier/keynote: `exp-eugene-yan` (co-anthropic), `exp-dex-horthy` (co-humanlayer, ⚠ caption garble resolved), `exp-geoff-huntley`, `exp-ian-livingstone` (co-keycard — batch-2 reuse), `exp-greg-pstrucha` (co-sentry, ⚠ garble resolved), `exp-daniel-han` (co-unsloth), `exp-benoit-schillings` (co-google-deepmind), `exp-garry-tan` (co-y-combinator)
- Applied/product: `exp-sina-shahandeh` (co-radicait), `exp-zhengyao-jiang` (co-weco, ⚠ UCR/UCL garble), `exp-kathryn-grayson-nanz` (co-progress-software), `exp-eve-bouffard` (co-y-combinator), `exp-francesco-bonacci` (co-cua)

### Elements (40 new)
- Eng practice: `el-agent-scoped-authorization`, `el-prod-to-code`, `el-tau-bench`, `el-judge-as-classifier`, `el-target-function`, `el-kitaru` (⚠ name garbled — verify before seeding), `el-agent-checkpoint-replay`
- Context/knowledge: `el-schema-guided-graph-extraction`, `el-personalized-pagerank`, `el-subgraph-matching`, `el-hipporag`, `el-token-factory`, `el-just-token-max` (⚠ garble), `el-remotion`, `el-content-engineering`, `el-agent-feature-flags`, `el-agent-kill-switch`, `el-microsoft-foundry`, `el-microsoft-iq`, `el-agentic-retrieval`, `el-foundry-agent-optimizer`
- Frontier/keynote: `el-agentic-vuln-pipeline`, `el-ralph-loop`, `el-model-first-languages`, `el-dynamic-quantization`, `el-torch-compile`, `el-process-supervision`, `el-code-selfplay`, `el-company-brain`, `el-gbrain` (⚠ spelling unverified)
- Applied/product: `el-hierarchical-decomposition`, `el-oracle-cli`, `el-aiden`, `el-aide`, `el-ai-ux-pillars`, `el-thinking-in-public`, `el-cua-driver`, `el-cua-bench`, `el-cua-fleet`

### SourceEntities
- reused `source-aie-yt` (all 20 talks); no new sources.

### InformationArtifacts (20 new, one per talk — slugs defined in each file)
- Eng practice: `ia-aie-madabhushi-bug-for-human`, `ia-aie-walter-agentic-perf`, `ia-aie-ung-evals-that-matter`, `ia-aie-schafer-stop-burning-tokens`, `ia-aie-tahir-save-button`
- Context/knowledge: `ia-aie-ainge-graphs-guide`, `ia-aie-maruthavanan-cognitive-infra`, `ia-aie-palmer-content-is-code`, `ia-aie-gupta-feature-flags`, `ia-aie-castro-ai-and-knowledge`
- Frontier/keynote: `ia-aie-yan-secure-source`, `ia-aie-horthy-loops-debate`, `ia-aie-han-kernels-rl`, `ia-aie-schillings-beyond-code`, `ia-aie-tan-new-physics`
- Applied/product: `ia-aie-shahandeh-scientific-agents`, `ia-aie-nanz-ux-of-ai`, `ia-aie-bouffard-imagination-engineering`, `ia-aie-jiang-aiden-parameter-golf`, `ia-aie-bonacci-computer-use`

## Batch-4 additions (reconciled after extraction)

_2 talks (published 2026-07-21): Farrelly/Inngest, Osman/Osmantic. 6 more
talks from this wave are scheduled premieres (see transcripts/README.md) —
pending. All artifacts `PublishedBySource → source-aie-yt`._

### Patterns (0 new — one candidate now at coin threshold)
- **REVIEW — coin decision:** "durable runtime / durable execution as an emerging stack layer" now has TWO independent vendor data points: ZenML's Kitaru (`tahir-zenml-agents-save-button.md`, batch 3) and Inngest (`farrelly-inngest-agent-architecture-half-life.md`, batch 4). Per the recurrence rule this is coinable — proposed slug `pat-durable-execution`, kind: dynamic. If coined, rehome the relevant signals in those two files (currently parked on `pat-harness-over-model`). Your call at review.
- Osman talk: no candidate — reads as the desktop face of `pat-sovereign-ai`; mechanism captured as `el-densing-law`.

### Companies (2 new)
- `co-inngest` (durable-execution platform), `co-osmantic` (local-AI; ⚠ file notes flag a possible earlier Osmantic mention — none found in seed/registry, coined fresh)

### Experts (2 new)
- `exp-dan-farrelly` (co-inngest, CTO), `exp-ahmad-osman` (co-osmantic)

### Elements (5 new)
- `el-three-layer-agent-architecture` (execution/context/compute layer model with per-layer half-lives), `el-inngest`, `el-densing-law` (capability density doubles ~3.5 months), `el-glm-52` (⚠ DevelopedByCompany → co-zhipu-ai inferred, flagged), `el-dgx-station`

### SourceEntities
- reused `source-aie-yt`; no new sources.

### InformationArtifacts (2 new)
- `ia-aie-farrelly-architecture-half-life`, `ia-aie-osman-desktop-frontier`

## Batch-5 additions (reconciled after extraction)

_20 talks (published 2026-07-11 → 07-15), one extraction file per talk. Four
thematic sets: coding-agents/frontier (Robinson/Wu+Shihipar/Brunet/Osmani/
Meijer), context & evals (Sankar/Schmid/Vidal/Fuentes/Phaidra), infra &
training (Bhardwaj/Brown/Shashi/Stagi/Adams), security & ecosystems (Cable/
Raskar/Taylor/Gupta/Dotta). All artifacts `PublishedBySource → source-aie-yt`.
Same-speaker reuse: `exp-sachin-gupta` (batch 3) also owns the ReviewDebt talk._

### Patterns (1 new + three candidates at coin threshold)
- **[batch5]** `pat-value-of-judgement` — Value of Judgement (dynamic) — as AI industrializes execution, the durable human/career edge shifts to judgment: choosing what's worth doing, verifying evidence, owning outcomes. Defined in `osmani-engineer-of-the-future.md`; evidenced independently by Osmani, Wu/Shihipar, Brunet.
- **REVIEW — coin decisions (candidates now at/past recurrence threshold):**
  - `pat-durable-execution` — now THREE-plus data points: ZenML Kitaru (batch 3), Inngest (batch 4), OpenAI sandbox-cloud storage-as-next-unlock (batch 5, first frontier-lab evidence), arguably Paperclip's control plane (batch 5). Strongest coin case of the three.
  - "benchmark-trust crisis" — now THREE data points: Han/Unsloth reward-hacking (batch 3), Vidal's psychometric-evals critique (batch 5), Robinson's reward-hacking-in-RSI (batch 5). Proposed slug `pat-benchmark-trust-crisis` (challenge).
  - `pat-agent-economy` — now TWO data points: Povilionis/Froglet receipts (batch 2), Raskar/Nanda agentic-web bazaar (batch 5, two pattern-less signals in the raskar file ready to rehome).
- "AI-native organization" gained two more resonance points (Wu/Shihipar 65%-of-PRs-by-Claude, Brunet org-redesign demand) on top of Tan (batch 3) — borderline.

### Companies (12 new)
- Coding/frontier: `co-spacexai` (⚠ SpaceX vs SpaceXAI garble flagged)
- Context/evals: `co-atlan` (data catalog/context layer), `co-mindmakers` (psychometric evals), `co-phaidra` (AI-factory agents)
- Infra/training: `co-prime-intellect` (open superintelligence stack), `co-superagentic` (RLM-Code), `co-ratel` (⚠ name garble flagged)
- Security/ecosystems: `co-corridor` (Jack Cable, ex-CISA), `co-mit-media-lab` (Project Nanda), `co-pomerium` (identity-aware proxy), `co-paperclip` (agent control plane), `co-faros-ai` (engineering intelligence)

### Experts (22 new)
- Coding/frontier: `exp-lee-robinson` (co-cursor), `exp-cat-wu`, `exp-thariq-shihipar` (both co-anthropic), `exp-simon-willison` (independent), `exp-pauline-brunet` (co-cursor), `exp-addy-osmani`, `exp-erik-meijer` (⚠ affiliation garbled)
- Context/evals: `exp-prukalpa-sankar` (co-atlan), `exp-philipp-schmid` (co-google-deepmind), `exp-alejandro-vidal` (co-mindmakers), `exp-elizabeth-fuentes` (co-aws), `exp-raahul-singh`, `exp-vanc-levstik` (both co-phaidra, ⚠ Levstik name garble)
- Infra/training: `exp-abhishek-bhardwaj` (co-openai), `exp-will-brown` (co-prime-intellect), `exp-shashi` (co-superagentic, ⚠ surname unresolved), `exp-roberto-stagi` (co-ratel), `exp-connor-adams` (indie, Remobi)
- Security/ecosystems: `exp-jack-cable` (co-corridor), `exp-ramesh-raskar` (co-mit-media-lab; co-presenter "Maria" not coined — no surname), `exp-nick-taylor` (co-pomerium), `exp-dotta` (co-paperclip, mononym/handle flagged)

### Elements (50 new)
- Coding/frontier: `el-recursive-model-improvement`, `el-cursor-composer`, `el-cursor-bench`, `el-textual-feedback`, `el-claude-code`, `el-claude-tag`, `el-claude-fable` (⚠ merge flag vs seed `el-claude-mythos-preview`), `el-claude-auto-mode`, `el-forward-deployed-engineering`, `el-cognitive-debt`, `el-alpha-decay`, `el-proof-carrying-agent-plans`, `el-lean`, `el-lethal-trifecta`
- Context/evals: `el-context-layer`, `el-skillsbench` (⚠ maintainer unverified), `el-capability-preference-skills`, `el-item-response-theory`, `el-residual-fingerprinting`, `el-strands-agents`, `el-bedrock-agentcore`, `el-graphrag`, `el-hierarchy-summarization`
- Infra/training: `el-microvm`, `el-gvisor`, `el-sandbox-snapshotting`, `el-verifiers`, `el-prime-rl`, `el-harness-interception`, `el-on-policy-distillation`, `el-recursive-language-models`, `el-rlm-code`, `el-typescript`, `el-vercel-ai-sdk`, `el-remobi`
- Security/ecosystems: `el-secure-by-design`, `el-memory-safe-languages`, `el-baxbench` (⚠ caption garble resolved), `el-nanda-index`, `el-nanda-town`, `el-maritime`, `el-identity-aware-proxy`, `el-reviewdebt`, `el-done-as-object`, `el-liveness-model`, `el-paperclip`

### SourceEntities
- reused `source-aie-yt` (all 20 talks); no new sources.

### InformationArtifacts (20 new, one per talk)
- Coding/frontier: `ia-aie-robinson-recursive-improvement`, `ia-aie-wu-shihipar-anthropic-culture`, `ia-aie-brunet-forward-deployed`, `ia-aie-osmani-engineer-of-future`, `ia-aie-meijer-tool-calls-scary`
- Context/evals: `ia-aie-sankar-context-layer`, `ia-aie-schmid-skills-evals`, `ia-aie-vidal-psychometric-evals`, `ia-aie-fuentes-agent-hallucinations`, `ia-aie-phaidra-semantic-blindness`
- Infra/training: `ia-aie-bhardwaj-agent-sandbox-cloud`, `ia-aie-brown-modern-post-training`, `ia-aie-shashi-rlm-codebases`, `ia-aie-stagi-types-and-agents`, `ia-aie-adams-remobi-mobile`
- Security/ecosystems: `ia-aie-cable-bugpocalypse`, `ia-aie-raskar-agentic-web`, `ia-aie-taylor-claws-out`, `ia-aie-gupta-reviewdebt`, `ia-aie-dotta-liveness`

## Batch-6 additions (reconciled after extraction)

_20 talks (published 2026-07-07 → 07-11), one extraction file per talk. Four
thematic sets: keynotes & software futures (OpenAI Golden Age/Browne/Litt/
Volkov/Local-AI panel), coding-agent practice (Fenner/Campos/Sheikh/Lajili/
Lee-Chan), agent ops & fleets (Doshi/Shrabony/Lee/Steinfurt/Bauer), applied &
vertical (Ramachandran/An+Hoe/Noring/Kumar/Melnikova). All artifacts
`PublishedBySource → source-aie-yt`._

### Patterns (0 new — candidate evidence keeps accumulating)
- Zero new patterns coined. Heaviest reuse: `pat-verification-gap`, `pat-harness-over-model`, `pat-model-not-bottleneck`, `pat-value-of-judgement`.
- **Candidate evidence added this batch (see registry batch-4/5 coin decisions):**
  - `pat-durable-execution`: +KRAFTON fleet crash-recovery/state-in-files (strongest single data point yet), +Shrabony scheduled-run monitoring, +OpenAI keynote (local/cloud split "obsolete", agent-picks-environment).
  - "AI-native organization": +Doshi (non-tech SMB runs GTM on 39 agents), +Lee-Chan (personal agent org), +An/Hoe (waterfall→parallel game teams), +Noring (dev-role/backlog fan-out), +Browne (products-as-markdown, soft). Combined with Tan/Wu+Shihipar/Brunet this is now the widest-evidenced uncoined candidate — proposed slug `pat-ai-native-org`.
  - `pat-agent-economy`: +Local-AI panel (Brev sees agents directly provisioning GPUs; Osman: agents renting their own compute).
  - `pat-benchmark-trust-crisis`: +Kumar (backdoored models pass every eval), +Campos (LLM-judge attribution, weak).
- **First counter-evidence edges:** Steinfurt signal uses ContradictsPattern → `pat-harness-over-model` (reasoning models absorbed pipeline steps back into the model); Lee-Chan file notes mild counter-evidence to `pat-value-of-judgement`.

### Companies (18 new)
- Keynotes/futures: `co-notion`, `co-weights-biases` (CoreWeave-owned), `co-exo-labs` (distributed local inference), `co-roboflow` (vision AI)
- Coding practice: `co-zed` (ACP), `co-witan-labs` (spreadsheet agents), `co-checkout-com` (fintech), `co-poolside` (from-scratch models + coding agents), `co-snap`
- Agent ops: `co-machinecraft` (Indian thermoforming SMB, 39-agent GTM brain), `co-krafton` (PUBG), `co-tng` (German consultancy), `co-upside` (agentic GTM data)
- Applied/vertical: `co-filed` (tax vertical AI), `co-lexisnexis`, `co-evil-martians` (devtools consultancy), `co-planetscale`, `co-typesense`

### Experts (26 new)
- Keynotes/futures: `exp-alexander-embiricos`, `exp-romain-huet`, `exp-peter-steinberger` (all co-openai; Steinberger = OpenClaw creator, el-oracle-cli author), `exp-theo-browne` (independent), `exp-geoffrey-litt` (co-notion), `exp-alex-volkov` (co-weights-biases), `exp-alex-cheema` (co-exo-labs), `exp-matthew-berman` (independent), `exp-joseph-nelson` (co-roboflow), `exp-nader-khalil` (co-nvidia/Brev, ⚠ identification inferred from garble — verify)
- Coding practice: `exp-bennet-fenner` (co-zed), `exp-nuno-campos` (co-witan-labs; ex-LangChain per public record but transcript never says it — no edge), `exp-talha-sheikh` (co-checkout-com), `exp-johan-lajili` (co-poolside, ⚠ "Joan" garble), `exp-jeffrey-lee-chan` (co-snap)
- Agent ops: `exp-rushabh-doshi` (co-machinecraft), `exp-sumaiya-shrabony` (no affiliation stated), `exp-kyle-jaejun-lee` (co-krafton), `exp-stephan-steinfurt` (co-tng), `exp-alex-bauer` (co-upside, role inferred)
- Applied/vertical: `exp-atul-ramachandran` (co-filed, CTO), `exp-danielle-an`, `exp-david-hoe` (both co-meta), `exp-chris-noring` (co-microsoft), `exp-sachin-kumar` (co-lexisnexis), `exp-victoria-melnikova` (co-evil-martians)

### Elements (39 new; `el-agents-md` defined twice, see note)
- Keynotes/futures: `el-codex`, `el-gpt-56` (Sol/Terra/Luna family), `el-agents-md`, `el-context-compaction`, `el-agent-loops`, `el-explain-diff`, `el-microworlds`, `el-zl-continuum`, `el-dgx-spark`, `el-nemotron` (⚠ version per captions), `el-ods` (resolves batch-4's unresolved "ODS" garble in the Osman file)
- Coding practice: `el-acp` (Agent Client Protocol), `el-code-mode`, `el-agent-repl`, `el-vector-harness`, `el-aix-engineering`, `el-cmux` (⚠ tmux/cmux garble)
- Agent ops: `el-brain-os` (forkmybrain.org), `el-agent-sleep-cycle`, `el-agent-handoff-gates`, `el-agent-org-hierarchy`, `el-filesystem-agent-state`, `el-kubernetes`, `el-chess-explainer-agent`, `el-gemini-31-pro` (⚠ name reconstructed), `el-jury-judge-workflow`, `el-upside-librarian`, `el-agent-tiers`, `el-commanders-intent`
- Applied/vertical: `el-conveyor-belt-agent-product`, `el-weekly-active-sessions`, `el-runtime-llm-gameplay`, `el-custom-agents`, `el-copilot-coding-agent`, `el-sleeper-agent-backdoor`, `el-diff-sae`, `el-pmf-compass`, `el-founder-led-gtm`
- **Merge note:** `el-agents-md` was independently defined in `noring-microsoft-code-to-systems.md` (concept/harness) and `embiricos-huet-steinberger-openai-golden-age.md` (technology/harness) — same slug, compatible briefs; single node, pick kind at seeding (OpenAI keynote is the origin story: named so other agents could adopt it).

### SourceEntities
- reused `source-aie-yt` (all 20 talks); no new sources.

### InformationArtifacts (20 new, one per talk)
- Keynotes/futures: `ia-aie-openai-golden-age`, `ia-aie-browne-everything-changed`, `ia-aie-litt-understanding-bottleneck`, `ia-aie-volkov-zl-continuum`, `ia-aie-local-ai-panel-state-of-union`
- Coding practice: `ia-aie-fenner-acp-live`, `ia-aie-campos-spreadsheet-agents`, `ia-aie-sheikh-agent-rules`, `ia-aie-lajili-agent-blindfolded`, `ia-aie-lee-chan-idea-velocity`
- Agent ops: `ia-aie-doshi-39-agents-factory`, `ia-aie-shrabony-solo-cicd`, `ia-aie-lee-agent-fleet`, `ia-aie-steinfurt-chess-channel`, `ia-aie-bauer-trust-patterns`
- Applied/vertical: `ia-aie-ramachandran-vertical-ai`, `ia-aie-an-hoe-game-with-ai`, `ia-aie-noring-code-to-systems`, `ia-aie-kumar-deception-monitor`, `ia-aie-melnikova-gtm-is-you`

## Batch-7 additions (reconciled after extraction)

_10 talks (published 2026-07-05 → 07-07), one extraction file per talk. Two
thematic sets: harness & frontier (Shihipar/Bhargava/Chandegra/Lichtenberg/
Desai), product & process (Ortmann Lee/Dumit/ten Teije/Grbic/Kalandadze). All
artifacts `PublishedBySource → source-aie-yt`. Same-speaker reuse:
`exp-thariq-shihipar` (batch 5) also owns the solo Fable talk._

### Patterns (0 new — candidate ledger keeps moving)
- Zero new patterns coined. `pat-harness-over-model` got direct **titular evidence** (Bhargava's talk is named after the thesis) — and simultaneously TWO more ContradictsPattern counter-edges (Shihipar's prompt-shrink arc: Claude Code's system prompt halved as models improved; Chandegra's fixed-harness obsolescence argument). With batch-6's Steinfurt edge that's three counter-edges — the harness thesis is now genuinely contested in the corpus, which is exactly what a living pattern should look like.
- **Candidate evidence added:**
  - `pat-benchmark-trust-crisis`: +SWE-Marathon reward-hacking arms race (12.8% → 9% → zero across verifier hardening rounds) — strongest data point yet (desai file); weak +retrieval-benchmark bias (lichtenberg).
  - `pat-ai-native-org`: +Automattic Radical Speed Month (500 people, 30 days, designers shipping) — strong; +Shihipar soft resonance.
  - `pat-durable-execution`: +Agency language-level serializable pause/resume (bhargava).
  - **NEW paired candidate — "adaptive software / emergent harnesses":** ten Teije ("The Pipeline Is Dead": one stem + per-user live divergences, the frozen build artifact dissolves — proposed `pat-adaptive-software`) and Chandegra ("Beyond the Harness": harness as runtime output, not input — proposed `pat-adaptive-harness`) arrived independently in the same batch and arguably state one thesis at two layers (product artifact / agent scaffolding). Review options: coin one combined pattern (two data points), or hold both as one-talk candidates.
  - Kalandadze explicitly NOT counted toward durable-execution (ops/observability, different claim).

### Companies (10 new)
- Harness/frontier: `co-etsy`, `co-annicha-labs` (⚠ "Anitcha" garble), `co-mixedbread` (search/retrieval), `co-abundant-ai` (RL environments, SWE-Marathon)
- Product/process: `co-duolingo` (DET), `co-watershed` (carbon accounting), `co-sky-valley` (⚠ "Differ" garble), `co-automattic`, `co-figma`, `co-wandero` (⚠ vertical inferred)

### Experts (10 new)
- Harness/frontier: `exp-aditya-bhargava` (co-etsy; Grokking Algorithms author, Agency creator, ⚠ garbles), `exp-rajiv-chandegra` (co-annicha-labs; physician + AI engineer), `exp-hanna-lichtenberg` (co-mixedbread), `exp-aamir-shakir` (co-mixedbread, ⚠ surname from public record), `exp-rishi-desai` (co-abundant-ai)
- Product/process: `exp-angel-ortmann-lee` (co-duolingo, ⚠ garble), `exp-andrew-dumit` (co-watershed, ⚠ Dumont/Dumit), `exp-iris-ten-teije` (co-sky-valley), `exp-sanja-grbic` (co-automattic), `exp-raphael-kalandadze` (co-wandero)

### Elements (16 new)
- Harness/frontier: `el-capability-overhang`, `el-agency-lang` (agencylang.com), `el-harness-bench` (⚠ verify paper), `el-adaptive-engineering`, `el-knowledge-gap`, `el-mixedbread-agentic-search`, `el-browsecomp-plus`, `el-swe-marathon`, `el-computer-use-verifier`
- Product/process: `el-automation-bias`, `el-interactions-as-labels`, `el-constrain-effects-not-expression` (⚠ merge-candidate vs `el-generator-validator-separation`/`el-deterministic-agentic-split`), `el-agent-as-runtime`, `el-stem-and-divergences`, `el-automattic-context-mcp` (⚠ name garbled), `el-meta-harness`

### SourceEntities
- reused `source-aie-yt` (all 10 talks); no new sources.

### InformationArtifacts (10 new)
- Harness/frontier: `ia-aie-shihipar-field-guide-fable`, `ia-aie-bhargava-harness-over-model`, `ia-aie-chandegra-beyond-harness`, `ia-aie-lichtenberg-agent-retrieval`, `ia-aie-desai-swe-marathon`
- Product/process: `ia-aie-ortmann-lee-discernment`, `ia-aie-dumit-respect-the-process`, `ia-aie-ten-teije-pipeline-dead`, `ia-aie-grbic-500-vibe-coders`, `ia-aie-kalandadze-missing-layer`

## Batch-8 additions (reconciled after extraction)

_21 talks: 20 chronological (published 2026-06-28 → 07-05) + Barr Yaron's
"2026 State of AI Engineering" premiere (published 2026-07-21, from the
batch-4 pending list). Four sets: MCP/skills/platform (Zullo/Pocock/Schroeder/
Tornow/Johnson), infra & reliability (Gupta/Chawla+Koul/Benzon/Hanchett/
Sakthivel), learning & evals (Yaron/Feizi/Nabors/Hylak/Sanftl), applied &
media (Pike/Shah/Kalinowski/Matini/Joshi/Horváth). All artifacts
`PublishedBySource → source-aie-yt`. Mystery speaker resolved: the skills
missing-manual talk is Matt Pocock's._

### Patterns (0 new — two candidates now overwhelming)
- Zero new patterns coined across all 21 talks.
- **`pat-ai-native-org` — coin case now overwhelming:** Yaron survey adds the first quantitative evidence (81% report role-blur; >1/3 of teams have non-devs shipping code; 17% ship customer-facing) on top of 8 prior qualitative data points (Tan, Wu/Shihipar, Brunet, Doshi, Lee-Chan, An/Hoe, Noring, Grbic/Automattic) + Horváth soft. Recommend coining at review.
- **`pat-adaptive-software` / `pat-adaptive-harness` (paired) — now ~5 data points:** +Tornow (spec-is-the-product, bespoke implementations on demand), +RELAI (optimizer rewrites the harness from production signals), +Mutagent (agents mutating agents), on top of batch-7's ten Teije + Chandegra. Recommend deciding the one-vs-two-patterns question at review.
- `pat-durable-execution`: +Resonate/Synadia (durable promise/task as protocol primitives), +Chronicle record/replay (Microsoft), +agentic control plane (adjacent, Meta).
- `pat-benchmark-trust-crisis`: weak add (Nabors: judge self-preference bias).
- `pat-agent-economy`: weak/context add (Yaron cost-as-SLA stats).
- **Counter-edge:** Yaron `sig-2026-openweight-augments-closed` ContradictsPattern → `pat-sovereign-ai` (open-vs-closed drives model choice for only 5% of survey).
- One-talk candidates flagged (no edges): "DSA/multi-agent composition era" + "intelligence-cost reversal" (schroeder), "AI adoption/UX gap" 2nd point (johnson, first was nanz batch-3).

### Companies (21 new)
- MCP/skills: `co-manufact` (mcp-use), `co-ai-hero` (Matt Pocock), `co-standardagents`, `co-vercel`, `co-resonate` (durable execution), `co-synadia` (NATS), `co-joinin-ai`
- Infra: `co-tesco` (speaker employer only)
- Learning/evals: `co-amplify-partners` (survey owner), `co-relai` (⚠ domain spelling), `co-university-of-maryland`, `co-arize`, `co-hey-ai` (⚠ thin), `co-mutagent`
- Applied/media: `co-forestwalk`, `co-thinking-machines-lab` (⚠ attribution garble), `co-tcs` (⚠ conflicts with official "Independent" listing), `co-callstack`, `co-ogilvy`, `co-mongodb`, `co-visuallabs`

### Experts (24 new)
- MCP/skills: `exp-pietro-zullo` (co-manufact), `exp-matt-pocock` (co-ai-hero), `exp-justin-schroeder` (co-standardagents), `exp-dominik-tornow` (co-resonate), `exp-ted-johnson` (co-joinin-ai)
- Infra: `exp-nishant-gupta` (co-meta — distinct from exp-sachin-gupta), `exp-tisha-chawla`, `exp-susheem-koul` (both co-microsoft), `exp-anna-marie-benzon` (no affiliation), `exp-erik-hanchett` (co-aws; has a second talk at feed position ~128 — reuse), `exp-rajkumar-sakthivel` (co-tesco)
- Learning/evals: `exp-barr-yaron` (co-amplify-partners), `exp-soheil-feizi` (co-relai + co-university-of-maryland), `exp-rl-nabors` (co-arize, ⚠ name garble), `exp-veronica-hylak` (co-hey-ai), `exp-benedikt-sanftl`, `exp-burak-ozafsar` (both co-mutagent, ⚠ surname from public record)
- Applied/media: `exp-allen-pike` (co-forestwalk), `exp-varsha-shah` (co-tcs, ⚠ flagged), `exp-lech-kalinowski` (co-callstack), `exp-abed-matini` (co-ogilvy), `exp-apoorva-joshi` (co-mongodb), `exp-balazs-horvath` (co-visuallabs)

### Elements (43 new)
- MCP/skills: `el-mcp-apps`, `el-mcp-app-stores`, `el-mcp-use`, `el-leading-words`, `el-matt-pocock-skills`, `el-domain-specific-agents`, `el-vercel-eve`, `el-resonate`, `el-nats`, `el-deterministic-simulation`, `el-channel-expression-protocol`, `el-personaplex` (⚠ garble), `el-gpt-realtime-2` (⚠ normalized), `el-multiparty-turn-taking`
- Infra: `el-agentic-control-plane`, `el-chronicle` (⚠ naming flagged), `el-inference-nondeterminism`, `el-tabular-q-learning`, `el-prompt-caching` (⚠ generic; merge target), `el-model-routing`, `el-local-code-index`
- Learning/evals: `el-continual-learning`, `el-replayable-learning-environment`, `el-verifiable-continual-learning`, `el-relai-vcl-engine`, `el-arize-phoenix`, `el-small-language-models`, `el-agentic-ai-engineer`, `el-eval-driven-development`, `el-mutagent-platform`
- Applied/media: `el-voice-in-visuals-out`, `el-prefix-caching` (⚠ near-dupe of el-prompt-caching — merge at seeding), `el-cross-document-correlation`, `el-physical-ai-terminal`, `el-multimodal-tax`, `el-docling`, `el-hybrid-search`, `el-langfuse` (product node; co-langfuse existed since batch 3), `el-ai-system-design-framework`, `el-story-mapping`, `el-vad-framework`

### SourceEntities
- reused `source-aie-yt` (all 21 talks); no new sources.

### InformationArtifacts (21 new)
- MCP/skills: `ia-aie-zullo-mcp-apps`, `ia-aie-pocock-missing-manual`, `ia-aie-schroeder-domain-specific-agents`, `ia-aie-tornow-prompt-is-platform`, `ia-aie-johnson-prompt-punch-card`
- Infra: `ia-aie-gupta-deterministic-infra`, `ia-aie-chawla-koul-agent-failed-prod`, `ia-aie-benzon-rl-etl-remediation`, `ia-aie-hanchett-agent-wasting-tokens`, `ia-aie-sakthivel-local-code-index`
- Learning/evals: `ia-aie-yaron-state-of-ai-eng`, `ia-aie-feizi-continual-learning`, `ia-aie-nabors-frontier-on-device`, `ia-aie-hylak-explain-it`, `ia-aie-sanftl-agentic-ai-engineer`
- Applied/media: `ia-aie-pike-voice-visuals`, `ia-aie-shah-compliance-correlation`, `ia-aie-kalinowski-physical-terminal`, `ia-aie-matini-multimodal-tax`, `ia-aie-joshi-ai-system-design`, `ia-aie-horvath-prompt-the-room`

## Batch-9 additions (reconciled after extraction) — WF chronological sweep COMPLETE

_20 talks (published 2026-06-25 → 06-28, the first days of World's Fair
uploads, + Russo/HeyGen published 07-21). Four sets: memory & context
(Iusztin+Bouchard/Savkin/Romero-Sevilla/Pankaj/Clyburn), agent-building &
orchestration (Jones ×2/Graziano/Weitekamp/Sehgal), evals & production
(Gupta/Thomas/De Mesa/Hanchett/Razgaitis), interfaces & applied (Russo/
Kapoor/Raj/Shaikh+Rastogi/Martin-Dye). All artifacts `PublishedBySource →
source-aie-yt`. Same-speaker reuses: exp-nishant-gupta + exp-erik-hanchett
(batch 8); exp-angie-jones owns two talks in this batch (defined once)._

### Patterns (0 new — one coin made and REVERSED at review)
- ~~`pat-html-native-medium`~~ — coined on two-talk evidence (Russo/HeyGen + Kapoor/Nori), then **DEMOTED at review 2026-07-22** (user: mechanism, not a seed-altitude thesis). The pre-written rejection fallback was applied: thesis kept as element `el-html-native-medium` (defined in `russo-heygen-html-all-agents-need.md`), all pattern edges rehomed to `pat-model-not-bottleneck`, the one input-side edge in `raj-ark-browser-agents-better-eyes.md` dropped. Also retired at the same review: `pat-provider-blind-ai` (batch-2 candidate — design property, not a pattern).
- **Candidate ledger (all still uncoined, awaiting your review):**
  - `pat-benchmark-trust-crisis`: +Thomas/Miranda (STRONGEST evidence in corpus — gold-standard persona benchmark structurally blind to its dominant failure mode; LLM judges privilege fluency; RLHF amplifies via sycophancy) and a new "governance" flavor from Weitekamp (ARC-AGI-3 private-eval refusal / open-harness leaderboard split).
  - `pat-ai-native-org`: +Jones/Block (strongest narrative data point — 3,500-engineer org restructure, non-engineers shipping via Builder Bot, +69% output, AND the layoffs dark side; `sig-block-autonomy-then-layoffs` held pattern-less for rehoming).
  - `pat-durable-execution`: +Sehgal/Omnara (purest statement in corpus — append-only session log AS the agent, disposable executors; two signals ready to rehome), +Jones idempotency/retry material.
  - `pat-adaptive-harness`/`pat-adaptive-software`: +Graziano AutoAgent (optimizer rewrites production agents from eval+trace signals), +Weitekamp (Claude Code dynamic workflows = runtime-generated harness), +Pankaj (Agent RX rewrites retrieval guidance from outcomes); mild counter-evidence logged (Jones: "don't let agents design agents").
  - **NEW multi-talk candidate:** "persistent agent memory as a first-class stack layer" — three data points in one batch (Iusztin+Bouchard second-brain research OS, Savkin/Nx Polygraph trace persistence, Pankaj/StarlightSearch outcome-weighted runtime memory); flagged in all three files.
  - Scoped counter-edge: Romero-Sevilla ContradictsPattern → `pat-context-graphs` (graph context has a corpus-churn boundary where CAG wins; downgradeable per file note).

### Companies (22 new)
- Memory/context: `co-decoding-ai`, `co-towards-ai`, `co-nx` (Polygraph), `co-orbis` (⚠ garble), `co-starlight-search` (⚠ garble), `co-pinecone` (⚠ attribution), `co-red-hat`, `co-hugging-face`
- Agent-building: `co-block` (Goose, Builder Bot), `co-agentic-ai-foundation`, `co-nearform`, `co-openprose`, `co-symbolica` (⚠ unverified), `co-omnara` (⚠ garble)
- Evals/production: `co-results-gen`, `co-opengov`, `co-higharc`
- Interfaces: `co-heygen` (Hyperframes), `co-nori` (⚠ garble), `co-ark` (⚠ listing-only), `co-prosodica` (⚠ garble), `co-isadora-and-co` (⚠ listing-only)

### Experts (19 new)
- Memory/context: `exp-paul-iusztin` (co-decoding-ai), `exp-louis-francois-bouchard` (co-towards-ai), `exp-victor-savkin` (co-nx, ⚠ role from public record), `exp-luis-romero-sevilla` (co-orbis, VP AI), `exp-sonam-pankaj` (co-starlight-search, ⚠ garble resolved), `exp-cedric-clyburn` (co-red-hat)
- Agent-building: `exp-angie-jones` (co-agentic-ai-foundation + co-block, dual affiliation flagged; owns BOTH Jones talks), `exp-alfonso-graziano` (co-nearform), `exp-raymond-weitekamp` (co-openprose, ⚠ garble), `exp-ishaan-sehgal` (co-omnara, CEO)
- Evals/production: `exp-jacob-thomas` (co-results-gen), `exp-gabe-de-mesa` (co-opengov), `exp-vaidas-razgaitis` (co-higharc)
- Interfaces: `exp-james-russo` (co-heygen), `exp-amol-kapoor` (co-nori, CEO), `exp-kushan-raj` (co-ark), `exp-sohail-shaikh`, `exp-ankush-rastogi` (both co-prosodica, ⚠ garbles resolved), `exp-isadora-martin-dye` (co-isadora-and-co)

### Elements (56 new)
- Memory/context: `el-ai-research-os`, `el-deep-research`, `el-second-brain`, `el-obsidian`, `el-polygraph`, `el-org-work-graph`, `el-cache-augmented-generation`, `el-extended-cag`, `el-agent-rx` (⚠ naming), `el-utility-score`, `el-memory-as-reasoning`, `el-chunkless-rag`
- Agent-building: `el-goose`, `el-builder-bot`, `el-agent-maturity-model`, `el-company-world-model` (⚠ merge-check vs el-company-brain/el-brain-os), `el-agent-output-contracts`, `el-agent-idempotency`, `el-autoagent`, `el-golden-dataset`, `el-recursive-coding-agents`, `el-openprose`, `el-claude-dynamic-workflows`, `el-agentica` (⚠ unverified), `el-dspy`, `el-pi-coding-agent` (resolves batch-7's `el-pi-agent` candidate mention), `el-agent-session-log`, `el-omnara-managed-agents`
- Evals/production: `el-scenario-based-evals`, `el-miranda-hypothesis`, `el-epistemic-simulation`, `el-role-playing-language-system`, `el-prism-protocol` (⚠ naming), `el-incharacter-benchmark`, `el-time-locked-models`, `el-og-assist`, `el-effect-ts`, `el-a2a-protocol`, `el-spec-driven-development`, `el-kiro`, `el-property-based-testing`, `el-research-prototype-taxonomy`, `el-ml-microservice-monorepo`, `el-graphite`
- Interfaces: `el-html-native-medium` (demoted from pattern at review), `el-hyperframes`, `el-nori-sessions`, `el-pelican-bicycle-test`, `el-compressed-page-markdown` (⚠ name ours), `el-semantic-tool-routing`, `el-just-in-time-context` (⚠ merge candidate vs el-progressive-disclosure), `el-bfcl`, `el-layered-voice-architecture`, `el-post-generation-veto` (⚠ merge candidates), `el-bloom` (⚠ inferred), `el-thread-light` (⚠ garbled)

### SourceEntities
- reused `source-aie-yt` (all 20 talks); no new sources.

### InformationArtifacts (20 new)
- Memory/context: `ia-aie-iusztin-bouchard-notes-memory`, `ia-aie-savkin-genius-amnesia`, `ia-aie-romero-sevilla-extended-cag`, `ia-aie-pankaj-retrieval-boundary`, `ia-aie-clyburn-structuring-unstructured`
- Agent-building: `ia-aie-jones-autonomous-org`, `ia-aie-jones-build-systems`, `ia-aie-graziano-agents-building-agents`, `ia-aie-weitekamp-recursive-agents`, `ia-aie-sehgal-log-is-agent`
- Evals/production: `ia-aie-gupta-production-evals`, `ia-aie-thomas-miranda-hypothesis`, `ia-aie-de-mesa-og-assist`, `ia-aie-hanchett-spec-driven`, `ia-aie-razgaitis-research-to-reality`
- Interfaces: `ia-aie-russo-html-agents-need`, `ia-aie-kapoor-html-graphics`, `ia-aie-raj-better-eyes`, `ia-aie-shaikh-rastogi-100-tool-trap`, `ia-aie-martin-dye-tone-layering`

## Batch-10 additions (reconciled after extraction) — graph/context/ontology cluster

_11 talks (published 2026-07-21 → 07-23): the Graphs/Context-Engineering track
wave. Three sets: Neo4j + ontology core (Blumenfeld workshop/Eifrem/Chin/
Coyle — THREE Neo4j-affiliated talks, `co-neo4j` defined once), enterprise
context (Bruchim+Ast/Phipps/Pandya/Sachs), memory & runtime (Chalef/Nakajima/
Le). All artifacts `PublishedBySource → source-aie-yt`._

### Patterns (0 new — the cluster is pure pat-context-graphs validation)
- Zero coined. This batch is the strongest single-wave confirmation of the `pat-context-graphs` seed thesis — 11 professional statements of it, including Neo4j's CEO. Notably his "execution traces" pillar restates the original thesis's decision-traces/event-clock claim.
- **`persistent agent memory as a first-class stack layer` — now ~9 data points** (batch-9's three + this batch: Zep/Graphiti, BabyAGI 4 event log, TwelveLabs video memory as the company's whole positioning, CrabRAG's thesis, Eifrem's traces pillar, Monday's durable profile). **Decisively past threshold — recommend coining `pat-agent-memory-layer` at review.**
- Cross-batch convergence flag: Nakajima independently cites "the log is the agent" and reuses `el-agent-session-log` (Omnara, batch 9) — same thesis, two independent vendors.
- Other candidate adds: pat-durable-execution + pat-adaptive-harness (BabyAGI 4 replay/fork), pat-ai-native-org (Notion software-factory signal, held pattern-less), pat-agent-economy weak (Notion token economics).

### Companies (11 new)
- Neo4j/ontology: `co-neo4j` (defined in blumenfeld file, shared ×3), `co-cognee` (⚠ Cognee-vs-Cognite garble — verify), `co-uc-berkeley`
- Enterprise: `co-monday`, `co-gates-foundation` (⚠ no type-enum fit), `co-jpmorgan` (⚠ no type-enum fit), `co-parallel` (web-search API), `co-decagon`
- Memory/runtime: `co-zep` (Graphiti), `co-untapped-capital`, `co-twelvelabs`

### Experts (12 new)
- `exp-zach-blumenfeld`, `exp-emil-eifrem` (CEO), `exp-stephen-chin` (all co-neo4j), `exp-frank-coyle` (co-uc-berkeley)
- `exp-omri-bruchim`, `exp-tomer-ast` (both co-monday), `exp-mike-phipps` (co-gates-foundation), `exp-ritvik-pandya` (co-jpmorgan), `exp-sarah-sachs` (co-notion)
- `exp-daniel-chalef` (co-zep), `exp-yohei-nakajima` (co-untapped-capital; BabyAGI creator), `exp-james-le` (co-twelvelabs)

### Elements (34 new)
- Neo4j/ontology: `el-context-shapes`, `el-neocarta` (⚠ spelling), `el-leiden-community-detection`, `el-neo4j-cli`, `el-ontology-semantic-layer`, `el-agent-execution-traces`, `el-crabrag`, `el-cognee`, `el-neuro-symbolic-ai`, `el-owl-rdfs`, `el-pydantic`
- Enterprise: `el-monday-sidekick`, `el-monday-world-model` (⚠ merge-check vs el-company-world-model), `el-fast-slow-context-engines`, `el-strategic-intelligence-platform`, `el-neo4j` (product node; distinct from co-neo4j), `el-learned-execution-graphs`, `el-opentelemetry`, `el-execution-drift-taxonomy`, `el-notion-auto-model`, `el-notion-workers`, `el-cost-per-capability-per-second`
- Memory/runtime: `el-graphiti`, `el-zep`, `el-graph-native-provenance`, `el-activegraph`, `el-babyagi`, `el-experiential-world-model`, `el-blackboard-architecture`, `el-marengo`, `el-pegasus`, `el-jockey`, `el-video-context-graph`, `el-video-worker`
- Note: `el-nanograph` [seed] checked against the Nakajima talk — no relation stated (talk cites Instagraph/Mindgraph); no edge.

### SourceEntities
- reused `source-aie-yt` (all 11); no new sources.

### InformationArtifacts (11 new)
- `ia-aie-blumenfeld-lakehouse-shapes`, `ia-aie-eifrem-thin-agents-substrate`, `ia-aie-chin-crabrag-graph-memory`, `ia-aie-coyle-agentic-ontologies`, `ia-aie-bruchim-ast-systems-of-context`, `ia-aie-phipps-data-model-moat`, `ia-aie-pandya-execution-graphs`, `ia-aie-sachs-token-town`, `ia-aie-chalef-kg-provenance`, `ia-aie-nakajima-active-graph`, `ia-aie-le-video-memory`

## Batch-11 additions (reconciled after extraction) — WF closing batch

_10 talks (published 2026-07-21 → 07-24): the contrarian/evals set (Horthy #2/
ZS/Petersson/Rivest+Miller/Bhagwat) + applied & workshops (Rolls+Wolf/Barth/
Quoraishee+Song/Liu/Estefania). Same-speaker reuse: exp-dex-horthy (batch 5).
All artifacts `PublishedBySource → source-aie-yt`._

### Patterns (0 new — the dialectic batch)
- Zero coined. **The harness thesis is now formally contested in both directions inside one batch**: Horthy #2 landed ContradictsPattern → `pat-harness-over-model` ×3 and → `pat-model-not-bottleneck` ×1 (software factories fail; gameable RL rewards; self-limiting judges), while Rivest/DSPy added FormsPattern support ×2. Total counter-edges on harness-over-model: 8.
- **`pat-agent-economy` — strongest corpus evidence yet** (Petersson/Vending-Bench: agents hiring humans via LinkedIn/Indeed, forming price cartels, cutting sponsorship deals; 3 signals held pattern-less for rehoming). With batch-2 Povilionis + batch-5 Raskar + Local-AI panel: **recommend coining.**
- `pat-benchmark-trust-crisis`: +simulation-awareness ("behavioral evals are doomed", Anthropic system-card corroboration) + Horthy's gameable-rewards material.
- `pat-adaptive-harness`: +DSPy Flex (learns a custom harness per function contract — prime evidence), +qualitative learning, +Bhagwat self-modifying claws, +NYT live-layout-rewriting agent.
- `pat-ai-native-org`: +Codex threads-as-agent-org, +AI-champion plugins.
- `pat-agent-memory-layer` + `pat-durable-execution` resonance: Codex persistent pinned threads.

### Companies (8 new)
- Contrarian/evals: `co-cognition` (Frontier Code benchmark), `co-zs-associates`, `co-andon-labs` (Vending-Bench), `co-shopify` (DSPy case study), `co-mastra`
- Applied/workshops: `co-arithmetic` (cyber post-training), `co-nyt` (media), `co-better-auth`

### Experts (14 new)
- `exp-subbiah-sethuraman`, `exp-abhilash-asokan` (both co-zs-associates, ⚠ garbles resolved), `exp-lukas-petersson` (co-andon-labs), `exp-maxime-rivest`, `exp-isaac-miller` (DSPy community, no company edges — flagged), `exp-sam-bhagwat` (co-mastra)
- `exp-uri-rolls` (co-arithmetic), `exp-thom-wolf` (co-hugging-face), `exp-antje-barth` (co-amazon — AGI Lab folded per the co-meta precedent), `exp-shafik-quoraishee`, `exp-joanne-song` (both co-nyt), `exp-jason-liu` (co-openai, ⚠ Instructor authorship not in transcript), `exp-paola-estefania`, `exp-bereket-habtemeskel` (both co-better-auth; Habtemeskel co-authored, did not present)

### Elements (38 new)
- Contrarian/evals: `el-lights-off-software-factory`, `el-swe-bench` (⚠ late coin — grep before seeding), `el-frontier-code`, `el-deepsuite` (⚠ garble), `el-humanlayer`, `el-knowledge-graph-control-plane` (⚠ merge-check vs el-agentic-control-plane), `el-single-reasoner`, `el-zs-signal-queue`, `el-vending-bench`, `el-simulation-awareness`, `el-real-to-sim-forking`, `el-andon-deployments`, `el-task-model-separation`, `el-gepa` (⚠ garble), `el-dspy-flex`, `el-qualitative-learning`, `el-agentic-spectrum` (⚠ merge-check vs el-agent-maturity-model), `el-steinbergers-law`, `el-mastra`
- Applied/workshops: `el-masov-benchmark` (⚠ name uncertain), `el-deterministic-partial-grading`, `el-access-control-vulnerabilities`, `el-perception-agent`, `el-annotation-tool`, `el-visual-verification`, `el-on-device-agentic-games`, `el-agentic-game-loop`, `el-on-device-agent-constraints`, `el-adaptive-accessibility-agent`, `el-appshots`, `el-codex-skills-plugins`, `el-codex-pinned-threads`, `el-codex-heartbeat-automations`, `el-codex-goals`, `el-personal-memory-vault`, `el-codex-computer-use`, `el-agent-auth-protocol`, `el-agent-capability-directory`

### Late addition: Terminal-Bench/Harbor talk (talk #158)
- `shaw-marten-everything-is-a-rollout.md` — "Everything Is a Rollout" (Laude Institute, 2026-07-24). **RE-EXTRACTED 2026-07-25 from complete captions** (3,662 words vs the truncated 2,607 first pass). Entities: `co-laude-institute` (⚠ garble), `exp-alex-shaw`, `exp-ryan-marten` (⚠ **byline only — the complete transcript is Alex Shaw start to finish; Marten never speaks and is never named. Weaker evidence than the first pass assumed; drop-option documented in the file**), `el-harbor` (revised), `el-agentic-environment`, `el-agent-development-as-ml`, plus from the newly-available sections: `co-ramp` (RampBench), `el-rollout`, `el-agentic-map-reduce`, `el-terminal-bench` (⚠ coined here, reversing two prior corpus declines in b11/b12 — see file review note 3).
- Confirmed lineage: `el-frontier-code` (b11) UsesElement → `el-harbor` — the cross-file edge proposed at batch 11 is now transcript-stated, not inferred.
- **NEW cross-batch candidate: `pat-environments-economy` — RECOMMEND COINING** — agentic environments (instruction+sandbox+verifier) as a standardized, tradeable asset class where evals ≡ RL training data. Post-re-extraction this file is its strongest source: task data called "already a multibillion-dollar market" by the format's author, and TWELVE independent projects built on Harbor within months (Cognition migrated all evals, Poolside, LangChain DeepAgents, Snorkel, Scale, Tinker, AfterQuery…). Six corpus data points, five signals held pattern-less awaiting the coin. Original four: Harbor's ~300-400-set registry (here), Prime Intellect's Verifiers/Environments Hub (b5), Abundant AI's environments-for-frontier-labs business (b7), Andon Labs' real-to-sim deployments (b11). `sig-environment-format-standardizing` held pattern-less for rehoming. Consider coining at review.
- Proposed cross-file edge at seeding: `el-swe-marathon` UsesElement → `el-harbor` (SWE-Marathon runs on Harbor environments).
- `el-gepa` reuse here corroborates the batch-11 "Jeepa/Japa" garble resolution.

### SourceEntities
- reused `source-aie-yt` (all 11 incl. late addition); no new sources.

### InformationArtifacts (10 new)
- `ia-aie-horthy-software-factories`, `ia-aie-sethuraman-asokan-killed-multiagent`, `ia-aie-petersson-vending-bench`, `ia-aie-rivest-task-from-model`, `ia-aie-bhagwat-every-harness-claw`, `ia-aie-rolls-wolf-outthink-hackers`, `ia-aie-barth-perception-agents`, `ia-aie-quoraishee-song-mobile-games`, `ia-aie-liu-codex-workshop`, `ia-aie-estefania-better-agent-auth`

## Batch-12 additions (reconciled after extraction) — Evals track

_6 talks (published 2026-07-24 → 07-25): the Arize-hosted Evals track. Two
sets: Arize + Snorkel (Lopatecki/Dhinakaran/Feyzkhanov), applied multimodal
evals (Bril/Gupta+Chopra/Bhateja+Bump). All artifacts
`PublishedBySource → source-aie-yt`. Notable: near-total company reuse —
only ONE new company across 6 talks._

### Patterns (0 new — but two candidates materially advanced)
- Zero coined. `pat-verification-gap` took 23+ reference edges from these three applied-eval files alone — it remains the corpus's dominant thesis.
- **`pat-environments-economy` — 5th and most commercial data point**: Snorkel *sells* benchmarks as product, runs millions of agent simulations/month, and states evals≡RL-training-data outright (small-planner distillation). Two signals held pattern-less for rehoming (`sig-harbor-format-adoption`, `sig-simulations-as-training-data`). Strongest coin case yet.
- **`pat-benchmark-trust-crisis` — NEW third leg (methodology)**: beyond gaming (b3/b5/b7) and contamination (b9), benchmark *construction* itself is unreliable — sim reward-hacking, over-broad verifiers that pass everything, wrong verifiers that fail everything, agent variance (Feyzkhanov); plus measurement blindness (Bril: judge scored 9.2/10 on "camera work" for a static 4-second shot) and production reward hacking (Uber: editor oversteers to a generic ceramic bowl that clears the QA gate). Countermeasures also captured: `el-oracle-solution`, `el-benchmark-as-software`, `el-private-benchmark`.
- **`pat-adaptive-harness` — strongest vendor data point in the corpus** (Gupta+Chopra/Uber: reflect/synthesize optimizer rewrites production agent configs from live human-label signal + benchmarks + versions into an agent store, no human in the loop). Ranks with RELAI, DSPy Flex, AutoAgent.
- Notable: Lopatecki contributes a *support* edge to `pat-harness-over-model` — worth weighing against its 8 counter-edges.

### Companies (1 new)
- `co-character-ai` (developer)
- **Reused, not coined**: `co-arize`, `co-snorkel-ai`, `co-anthropic` — and two identity resolutions: `co-uber` [registry] for the Gupta+Chopra talk (captions garbled Uber as "Aruba"/"Rue Ba"; the registry brief frames Uber as AI-*consuming* — **recommend widening that brief**, they are a builder here), and `co-google` [registry] for YouTube Ads per the corp/lab precedent (⚠ the talk never says "Google" — alternative is coining `co-youtube` type media; tradeoff in the bhateja file's review notes).

### Experts (8 new)
- `exp-jason-lopatecki` (co-arize, co-founder/CEO), `exp-aparna-dhinakaran` (co-arize, co-founder), `exp-rustem-feyzkhanov` (co-snorkel-ai)
- `exp-maor-bril` (co-character-ai, ⚠ "Mayur" caption garble), `exp-soumya-gupta`, `exp-jai-chopra` (both co-uber; Soumya is distinct from exp-sachin-gupta AND exp-nishant-gupta — three unrelated Guptas now in the corpus), `exp-preetika-bhateja`, `exp-daniel-bump` (both co-google/YouTube Ads; surname from video byline)

### Elements (28 new)
- Arize/Snorkel: `el-arize-signal`, `el-arize-alex`, `el-observability-skills`, `el-continuous-fix-loop` (⚠ merge-adjacent to el-prod-to-code), `el-agent-as-a-judge`, `el-trace-to-simulation`, `el-private-benchmark`, `el-oracle-solution`, `el-simulated-user`, `el-benchmark-as-software`
- Video/multimodal evals: `el-pairwise-preference-eval` (defined in bril, independently reused by the Uber talk — same-batch convergence), `el-frame-level-video-metrics`, `el-story-level-video-evals`, `el-manufactured-badness`, `el-distilled-vlm-judge`, `el-eval-in-the-generation-loop`, `el-judge-human-calibration`
- Closed-loop/production: `el-closed-loop-auto-tuning`, `el-diagnoser-agent`, `el-multi-dimensional-qa-gate`, `el-pass-at-k`, `el-swiss-cheese-gating`, `el-flat-trace-log`
- YouTube practice: `el-intuition-first-evals`, `el-rater-rubrics`, `el-online-evals`, `el-launch-readiness-gate`

### SourceEntities
- reused `source-aie-yt` (all 6); no new sources.

### InformationArtifacts (6 new)
- `ia-aie-lopatecki-signal-to-pr`, `ia-aie-dhinakaran-agent-as-judge`, `ia-aie-feyzkhanov-traces-to-simulations`, `ia-aie-bril-evaling-video-slop`, `ia-aie-gupta-chopra-closed-loop-evals`, `ia-aie-bhateja-model-whisperers`

## Batch-13 additions (reconciled after extraction) — data, benchmarks & loops

_6 talks (published 2026-07-25 → 07-26). Two sets: data & benchmarks (Shi/
Datacurve, Cai, Abdin+McHardy/poolside), loops & applied (Mistele/HumanLayer,
Reed+Revere/SonderMind, Brick/Google). All artifacts `PublishedBySource →
source-aie-yt`. **This is the corpus's most counter-evidence-dense batch** —
see below._

### Patterns (0 new — and three coin-ready candidates now have COUNTER-evidence)
- Zero coined. **Read this section before running the pattern-review pass — it changes two recommendations.**
- **`pat-benchmark-trust-crisis` — materially strengthened, and its character changed.** Two new legs:
  - *Insider contamination numbers* (Shi/Datacurve): agents recover the golden patch from `git log` in 25%/18% of runs by model family; measurable FP/FN rates on SWE-bench Pro.
  - **An economic motive** (Cai): "most benchmarks you see are quietly fake" — sell a lab the data, then sell the benchmark that data hill-climbs. *"Goodhart's law with a profit motive."* The candidate was about measurement being **hard**; it is now about measurement being **profitably corrupted**. That is a seed-altitude claim about industry structure, not a technique.
  - A fourth flavour, *purpose drift* (SonderMind): explicitly refusing benchmark perfection because chasing the score drifts focus off the humans the system protects.
- **`pat-durable-execution` — first serious COUNTER data point** (Mistele/HumanLayer): "we don't need a new cluster for this" — production agent loops run on stock GitHub Actions with a git-tracked feedback file as the durable state. Against ~10 supporting points (Kitaru, Inngest, OpenAI sandbox cloud, Omnara, Chronicle, Resonate/Synadia…), this argues the durable-runtime layer may be a vendor category rather than a necessary one. **Weigh before coining.**
- **`pat-environments-economy` — split evidence.** Cai adds the first analyst-side sizing ($10–15B/yr per lab; permanent unbundling into four specialist steps; labs mandating 20–30-vendor diversification; lab data purchasing leads product launches by 2–3 months). But SonderMind open-sources its clinically-reviewed guardrail scenarios **as a public good, explicitly not as a tradeable asset** — a counter-instance to the "environments are an asset class" framing.
- `pat-adaptive-harness` — counter-flavoured (Mistele's harness is deliberately hand-designed and deterministic: "never send an agent to do deterministic code's job").
- Proposed counter-edges (drop-options documented in-file): `sig-blind-loop-outcomes-critique` ContradictsPattern → `pat-harness-over-model` (would take counter-edges 8 → 9); `sig-dram-cost-gates-edge-ai` ContradictsPattern → `pat-sovereign-ai` (hardware-economics counter, joins the Yaron-survey edge).
- New candidate noted but NOT slugged (too thin, 2 same-batch points): "manufactured data supply as the binding input" (poolside exhausted unique high-quality tokens → 13% synthetic mix of a 6T corpus; Cai's "data is the underfunded leg").

### Garble resolved
- **`el-deepsuite` (batch 11) is DeepSWE by Datacurve.** The Shi talk is that benchmark, properly named. Element reused rather than re-coined; **recommend renaming the element and its brief at review**.

### Companies (10 new)
- Data/benchmarks: `co-datacurve`, `co-artificial-analysis` (independent index; swapped SWE-bench Pro → DeepSWE), `co-mercor` (⚠ garble), `co-surge-ai`, `co-scale-ai`, `co-handshake-ai` (⚠ thin; corroborates b11 BankerToolBench), `co-antikythera` (⚠ name reconstructed — Cai's new venture, announced in-talk)
- Loops/applied: `co-sondermind` (developer per the co-risa-labs/co-filed vertical-AI precedent — enum has no healthcare), `co-apple` (coined on reference to carry `el-fastvlm`)
- Reused: `co-poolside` (second corpus talk), `co-humanlayer` (THIRD corpus talk, first by a non-Horthy speaker), `co-google`

### Experts (7 new)
- `exp-james-shi` (co-datacurve), `exp-sean-cai` (independent analyst), `exp-marah-abdin`, `exp-robert-mchardy` (both co-poolside)
- `exp-kyle-mistele` (co-humanlayer), `exp-akele-reed`, `exp-dave-revere` (both co-sondermind, ⚠ caption garbles), `exp-cormac-brick` (co-google, ⚠ "Corman")

### Elements (38 new)
- Benchmarks/data: `el-original-task-authoring`, `el-shipped-platform`, `el-observable-behavior-verifier`, `el-git-history-leakage`, `el-mini-swe-agent`, `el-process-based-data`, `el-type-one-type-two-data`, `el-verifiers-law`, `el-verifiability-axes`, `el-antikythera-mechanism`, `el-benchmark-psychosis`
- Pre-training: `el-laguna-models`, `el-poolside-hive` (⚠ Apache Hive name collision), `el-synthetic-pipeline-anatomy`, `el-rephrasing-synthetic-data`, `el-model-replica-hashing`, `el-deepgemm` (FP8 race condition silently randomizing ~0.5% of gradients; fix unmerged)
- Loops: `el-agentic-control-loop`, `el-ast-grep`, `el-golden-patterns` (⚠ name-collision check vs `el-golden-dataset`), `el-loop-flow-control`, `el-loop-feedback-file`, `el-ci-as-loop-runtime` (⚠ merge-check vs el-agent-loops/el-inngest/el-kitaru)
- Health/guardrails: `el-guardrail-sandwich` (⚠ merge-check vs el-generator-validator-separation), `el-coded-risk-disclosure`, `el-guardrail-overcalibration`, `el-clinician-annotated-evals`, `el-sonder-coach`, `el-guardrail-scenario-datasets`
- Edge/tiny: `el-tiny-language-models` (⚠ merge-decision vs `el-small-language-models`), `el-litert-lm` (⚠ garble), `el-gemma-open-models` (⚠ version numbering), `el-function-gemma`, `el-voice-to-function-calling`, `el-synthetic-finetuning-playbook`, `el-on-device-dictation`, `el-fastvlm`

### SourceEntities
- reused `source-aie-yt` (all 6); no new sources.

### InformationArtifacts (6 new)
- `ia-aie-shi-deepswe-benchmark`, `ia-aie-cai-state-of-data`, `ia-aie-abdin-mchardy-synthetic-data`, `ia-aie-mistele-loop-engineering`, `ia-aie-reed-revere-mental-health-coach`, `ia-aie-brick-tiny-lms-edge`

## Batch-14 additions (reconciled after extraction) — Forward Deployed Engineering track + infra

_10 talks (published 2026-07-28): an entire FDE track (8 talks, 8 companies)
plus 2 infra talks. Three sets: FDE-A (Bai/Anthropic, Reyes/Factory,
Wu/Cognition, Mehr/Ramp), FDE-B (Meurer/Sierra, Rekhi/Decagon, Ganesh/Kepler,
Moza/Varick), infra (Borucki/Hugging Face, Shah/Netflix). One more pending:
Govindarajan/OpenAI "Your Agent Didn't Fail. Your Harness Did." (premieres
2026-07-29)._

### Patterns (0 coined — but the strongest coin case the corpus has produced)

**⚑ `pat-fde-turn` (proposed) — TWO INDEPENDENT AGENTS CONVERGED ON THE SAME THESIS.**
The FDE track was split across two extraction agents with **disjoint** evidence
(four talks each, neither seeing the other's files). Both independently
proposed the same claim:

- *Set A:* "Agentic products are customizable without limit, so implementation has moved from the buyer to the vendor — shipping software now means embedding engineers who co-build, measure and prove the outcome, turning go-to-market into a delivery-and-product-feedback function."
- *Set B:* "As models industrialize execution, the vendor's scarce work moves inside the customer — embedding engineers (and now FDE-support agents) in the customer's own processes to discover, define and guarantee outcomes — which collapses product engineering, services and go-to-market into a single function and drags pricing from seats toward outcomes."

Independent convergence across disjoint evidence is the strongest signal the
extraction method can produce. **Recommend coining** (kind: `dynamic`).

- **Distinct from `pat-saaspocalypse` [seed]:** that pattern is about *who gets paid* (services budgets captured by software); this is about *who owns implementation*. They interlock — outcome pricing is the payment consequence of vendor-owned implementation — but the claims are separable.
- **Contested from birth (carry into the brief):** Ganesh/Kepler dissents on the second clause — the collapse runs toward **product**, not services/GTM ("this is not a role, this is a product strategy"; "please don't treat FDEs as go-to-market extensions"). His signal currently carries ContradictsPattern → `pat-saaspocalypse` and would re-target the new pattern if coined.
- **Sharpening counter-instance:** Mehr/Ramp runs the same function and principles *inside a buyer's* engineering org — showing the mechanism is not vendor-specific.
- **Ready to rehome on coin:** `sig-fde-term-collapse`, `sig-decagon-fde-equals-product-eng`, `sig-phoenix-isolation-failure` (held pattern-less), plus the FDE edges currently homed on `pat-saaspocalypse`/`pat-value-of-judgement`.
- Scale evidence: Google (GCP customer engineers) and OpenAI (new corporate-AI unit) staffing FDE at hyperscaler/frontier-lab scale; Palantir's Project Frontline alumni (~350 engineers) now at OpenAI/Anthropic/xAI; Decagon org-charting FDE through 50→500 headcount in a year; a 2026 composite job posting demanding "staff eng 8yrs + 6yrs direct sales + 4yrs solution architect".

**⚑ Second counter of the same shape — worth its own review note.**
`pat-agent-memory-layer` gains a ~10th data point AND its first counter:
Netflix builds fleet-wide agent memory as **markdown in a central Git repo**,
explicitly rejecting "fancy vector search or a vector database". This is the
identical shape as batch-13's HumanLayer counter to `pat-durable-execution`
(agent loops on stock CI, "we don't need a new cluster for this"). Two
practitioners now say a candidate infrastructure layer is really a convention.
Either a refutation, or the early-adopter end of the same curve — decide at review.

- Other moves: `pat-adaptive-harness` weak +1 (Netflix catalog rewrites itself from production signal); `pat-sovereign-ai` +2 support edges (partially offsetting its 2 counter-edges); `pat-context-graphs` +1 (Varick's process dependency graph).
- Weakest pattern fit in the corpus, flagged honestly: Borucki/Hugging Face is a pure database/infra talk with zero agent content — all-pattern-less drop-option documented in-file.

### Garble/question resolutions
- **Netflix:** batch-3's "Netflix Headroom" benchmark is NOT corroborated by this Netflix talk; no Netflix element existed. `co-netflix` coined here (type media, co-nyt precedent; flip-to-bigtech option noted).
- `co-palantir` defined in BOTH `bai-anthropic-fde-101.md` and `meurer-sierra-fde-dirty-secret.md` — single node, first-wins dedup. Reverses the batch-5 Brunet decline: two talks here treat Palantir as subject, not name-drop.

### Companies (7 new)
- FDE: `co-palantir` (origin institution), `co-factory`, `co-kepler` (⚠ thin — talk states no product/market/stage), `co-varick-agents` (⚠ captioned "Veric")
- Reused: `co-anthropic`, `co-cognition`, `co-ramp`, `co-sierra`, `co-decagon`
- Infra: `co-netflix`, and reused `co-hugging-face`

### Experts (10 new)
- FDE-A: `exp-kevin-bai` (co-anthropic; ex-Palantir, ex-Rippling), `exp-eno-reyes` (co-factory, CTO), `exp-jia-wu` (co-cognition; joined via Windsurf acquisition), `exp-leo-mehr` (co-ramp)
- FDE-B: `exp-natalie-meurer` (co-sierra; ex-Palantir; coined "the agent engineer" July 2024), `exp-sunny-rekhi` (co-decagon, ⚠ verify functional-CTO title), `exp-vinoo-ganesh` (co-kepler; ex-Palantir, created Project Frontline), `exp-vasuman-moza` (co-varick-agents, CEO), `exp-jd-puit` (co-varick-agents, ⚠ weakest name in batch — one caption mention, drop-option documented)
- Infra: `exp-arek-borucki` (co-hugging-face — first insider HF account in the corpus), `exp-rajat-shah` (co-netflix; distinct from `exp-varsha-shah` b8)

### Elements (~28 new)
- FDE-A: `el-palantir-foundry` (shared with FDE-B), `el-outcome-as-the-product`, `el-shared-primitives-platform`, `el-software-factory`, `el-droid`, `el-agent-readiness`, `el-factory-missions`, `el-autonomy-ratio` (⚠ figures internally ambiguous), `el-devin`, `el-token-maxing` (cross-vendor vocabulary: Cognition + Ramp's "token-maxing slop cannon"), `el-session-engineering-hours`, `el-always-be-scoping`, `el-scale-with-tokens`, `el-fde-request-intake-agent`
- FDE-B: `el-fde-vintage` (five cumulative eras of the role), `el-outcome-based-pricing`, `el-agent-engineering`, `el-decagon-agent`, `el-fde-role-specialization`, `el-custom-to-self-serve`, `el-fde-as-product-strategy`, `el-project-frontline`, `el-linguistic-lock-in`, `el-fde-agent`, `el-varick-os`, `el-process-dependency-graph`
- Infra: `el-hugging-face-hub`, `el-metadata-artifact-separation`, `el-precomputed-search-tokens`, `el-atlas-search`, `el-replica-read-routing`, `el-database-sharding`, `el-two-layer-autoscaling`, `el-pattern-anti-pattern-catalog`, `el-profiler-as-agent-input`, `el-canary-as-ground-truth`, `el-shift-left-performance`

### InformationArtifacts (10 new)
`ia-aie-bai-fde-101`, `ia-aie-reyes-factory-deployed-engineering`, `ia-aie-wu-cognition-deployed-engineering`, `ia-aie-mehr-ramp-scoping-tokens`, `ia-aie-meurer-fde-dirty-secret`, `ia-aie-rekhi-decagon-fde`, `ia-aie-ganesh-fde-product-strategy`, `ia-aie-moza-fde-tools`, `ia-aie-borucki-hub-scaling`, `ia-aie-shah-agents-performance`

## Batch-15 additions (reconciled after extraction) — Data/RL/post-training + enterprise waves

_29 talks (published 2026-07-29 → 08-02), six thematic sets. **This batch
changes several standing coin recommendations — read before the review pass.**
Two more talks from the wave are premieres pending (Temporal async MCP Tasks;
"MCP Apps: Extending the Frontier")._

### ⚑ FINDING 1 — `pat-harness-over-model` is OVERBROAD, not merely contested

Will Brown (Prime Intellect) **supports** the pattern in batch 5 and
**contradicts** it here: *"some try this at the harness or prompt layer, but
ultimately the system must evolve autonomously"* — continual learning belongs
in the weights. Same speaker, two talks, opposite edges.

The resolution is not that he changed his mind; the pattern currently
conflates **two claims**:
1. *Reliability/latency/control come from the harness* — supported by ~135 signals, incl. this batch's OpenAI talk ("model proposes, harness commits, receipt proves it"), Applied Compute's BYOH training, and Nubank's fixed-harness model bake-off.
2. *Improvement/capability comes from the harness* — contradicted by most of the ~11 counter-edges: Brown (weights), Anthropic prompt-shrink, TNG pipeline re-absorption, Chandegra harness obsolescence, Almeida ("it is not the Claude Code era" — coding agents are still RLHF-era assistance).

**Recommend scoping the brief to claim 1 (reliability engineering) at review.**
Most counter-edges then resolve without discarding evidence, and the ones that
remain are real.

### ⚑ FINDING 2 — `pat-benchmark-trust-crisis` now has NINE distinguishable legs

Gaming (b3/b5/b7) · contamination (b9, + Datacurve's 25%/18% git-log recovery)
· construction methodology (b12) · **economic motive** (Cai, b13) ·
**demand-side illegibility** (Heiner: buyers can't assess validity so they
assess popularity — why disclosure never dislodges a bad benchmark) ·
**ground-truth noise floor** (Anand: humans ~80% self-consistent at 2 weeks) ·
**definitional invalidity** (Brumley: a whole cyber-benchmark family grades
crashes and reports hacking) · **categorical impossibility** (Ganesh: "evals
are not verifiable; you cannot eval your way to determinism") ·
**irrelevance/saturation-decoupled-from-deployability** (Almeida, Khial: no
engineer picked a model from a leaderboard in 6 months).

Two things to carry into the brief rather than discover later:
- **Scope boundary (Boundary/Gupta):** private owned-loop A/B measurement works fine. The failing instrument is the *public third-party* benchmark, not measurement.
- **A legitimate-benchmaxxing counter (MiniMax):** Parallel Kernel Bench is a benchmark *of unsolved problems* where overfitting is the deliverable — bench-maxed kernels get harvested into production.
- **Two competing causal stories, both from insiders:** Cai says conflict of interest (sell the data, then sell the benchmark it hill-climbs); Heiner (Surge) says economics — ~$15M to build a 1,000-task agentic coding benchmark, ~$5M/yr to replace the third obsoleted annually. Heiner never mentions the conflict, *while Surge sells both*. Belongs in `evolution`, not as a ContradictsPattern edge.

### ⚑ FINDING 3 — `pat-environments-economy` is now the best-evidenced candidate (~15 points)

New this batch: Prime Intellect states the canonical sentence verbatim
(*"environments and evals are really the same thing"*); **Morgan Stanley
open-sources its harness because 10–20 environments are the moat** (first
non-vendor, and a bank); General Reasoning's 350+ environment platform behind
one API; Bugcrowd selling **up to 10,000 zero-day RL environments/month** to
model companies; Theta, Bespoke, Emulated (×3), LatchBio.

Counters and qualifications now also substantial:
- **Two public-good counters**: LatchBio gives benchmarks away (value is directional pull on frontier post-training, not licence revenue); SonderMind (b13).
- **A scope-narrowing admission from a seller**: Bespoke reports SFT carried the bulk of agent gains, RL only the last few percent.
- **A ceiling argument** (Emulated): the standard single-sandbox format breaks at multi-node/company scale — first Harbor critique, delivered alongside adoption.

### ⚑ FINDING 4 — two NEW candidates crossed threshold this batch

- **"Manufactured data supply as the binding input"** (b13 thin candidate, now ~5 independent points): web-text share collapse 85% → 50% → ~15% across published recipes (Arcee); DatologyAI's quantified substitution rates (145×/8×/35× compute multipliers from curation alone); poolside exhausting unique high-quality tokens; Cai's "data is the underfunded leg"; Emulated's "a gap in models is usually a gap in data". **Recommend a coin decision.**
- **"Capability moved from the base model to what follows it"** — proposed independently by Taylor (post-training side) and Singh (pre-training side) in the same batch. Note the tension worth carrying: Almeida calls RLHF "a weird detour", Taylor calls it the Rubicon.

### ⚑ FINDING 5 — the "infrastructure layer is really a convention" counter reached THREE practitioners
HumanLayer (loops on stock CI, b13) · Netflix (agent memory as markdown in git, b14) · FlyersSoft (durability from stock Cosmos DB + change feed + saga; agent loop stateless, sub-500ms, b15). This shape now bears on BOTH `pat-durable-execution` and `pat-agent-memory-layer`. Either three refutations, or one meta-observation that infrastructure categories get productized ahead of necessity.

### Other pattern movement
- `pat-accelerated-research` roughly doubled (Socher: NanoChat 0.93→0.91 with novel mechanisms, NanoGPT speedrun ~70s, CUDA kernels beating NVIDIA's leaderboard with NVIDIA verifying no reward hacking; plus Morgan Stanley's Dec-2025 crossing claim).
- `pat-context-graphs` second scoped counter (Intuit: "context is not experience"; first was Romero-Sevilla b10).
- `pat-model-not-bottleneck` ×2 new counters (Almeida, Emulated); `pat-saaspocalypse` ×1 (Almeida: SaaS structurally unchanged since 2019 — drop-option documented).
- Most counter-dense file in the corpus: `almeida-typesafe-after-rlhf.md` carries THREE ContradictsPattern edges.
- `pat-agent-memory-layer` purest statement yet (Rallabandi: "the model is just the engine; the memory is what the agent becomes") AND another counter (Kumar: sub-500ms SLA forbids long-term memory).

### Garbles resolved / identity notes
- `el-deepsuite` = **DeepSWE by Datacurve** — third corroboration; the b13 rename is now safe to action.
- `el-gepa` — fourth and fifth independent garble corroborations ("Japa", "Jeph I").
- `el-terminal-bench` — first non-owner primary source (Bespoke core contributor).
- Chrome zero-day speaker RESOLVED from transcript: **David Brumley (Carnegie Mellon + Bugcrowd)**, with four corroborating details.
- **A FOURTH distinct Gupta** (Vaibhav/Boundary) joins Sachin, Nishant, Soumya — do not merge.
- ⚠ `co-intuit` double-coined across two concurrent agents (compatible briefs, first-wins). ⚠ General Reasoning's environments platform captioned "openreview.ai" — collides with OpenReview.net, verify before seeding. ⚠ `chan-china-resources-memo-not-demo.md` has the worst captions in the corpus (several sentences unrecoverable; "Trust is a number" inverts the intended meaning).
- Company-enum gap now acute: `co-morgan-stanley`, `co-citadel`, `co-china-resources`, `co-jpmorgan` (b10), `co-nubank`, `co-ramp` all banks/funds typed `investor` or `developer` by nearest fit. Recommend deciding the whole set together.

## Batch-16 additions (reconciled) — post-event wave 2: MCP unlock + inference/infra

_9 talks (published 2026-08-02 → 08-07), incl. the two formerly-locked premieres.
4 more premieres pending as of 2026-08-08: UC Berkeley CCA exam (Z-c11pV_uvU),
GitHub realtime (iQ5xldZ9StU), Resolve AI (vSx5IULvBns), and OpenAI "Codex,
Behind the Harness" (shRR1e2HXMk — harness-pattern-relevant)._

### ⚑ pat-durable-execution — the VENDOR spoke, and the evidence cuts both ways
Cornelia Davis (Temporal) on MCP Tasks. SUPPORT, strongest form yet: durability
is now a **vendor-neutral MCP spec requirement**; her answer to the
stock-infrastructure counters is concrete (nobody built the client half —
reconnect/resume/multiplexing forced her demo's MCP client to BE a Temporal
workflow; V2's update endpoint independently reinvents Temporal's signal
primitive). COUNTER, from the vendor itself: the title concedes **zero
agent-client adoption**, non-adopters are endorsed as "smart" (dodged the V1
rewrite — stateful spec scrapped for stateless V2 in ~8 months), and her
go-to-market folds tasks into stock FastMCP — **convention-shaped delivery**,
the same shape as the HumanLayer/Netflix/FlyersSoft counters. Ledger now
complete for a coin/reject decision: need is real and standardized; even the
canonical vendor distributes it as a convention.

### ⚑ pat-saaspocalypse — strongest wave since seeding (5 support edges, 2 mechanisms)
UI atomization (Salomon/Yosef: "no application will control the user journey
anymore"; ChatGPT Apps ARE MCP Apps; ~800M weekly users ≈ "170× App Store TAM",
brand-loss was THE MCP-server adoption blocker) + per-user code instantiation
(Varda: Claude forks your gadget's features in place; app-store gatekeeping and
the SaaS roadmap both dissolve). Evolution note: "SaaS survives by ceding
journey/context/distribution to the host."

### ⚑ pat-sovereign-ai — distribution-layer surge (~9 new edges)
The frontier-access shock (Fable withdrawal / GPT-5.6 embargo) → enterprise
flight to open/Chinese models exactly as GLM 5.2 crosses the open
Opus-inflection; quantization as THE distribution layer of open AI (GLM
1.5TB→250GB; labs absorbing QAT/NVFP4 into releases; HF-acquired-llama.cpp
claim ⚠ VERIFY); Open MDW licence making traces ownable training data; OCP
standardize-and-commoditize precedent. Independent cross-file corroboration:
abdallah panel and Cline state the embargo→open-flight mechanism separately.

### ⚑ Provider-commoditization space — evidence accumulating; retired pattern NOT resurrected
Per the standing rejection of pat-provider-blind-ai, two new signals held
pattern-less as a PAIRED set: OpenClaw heartbeats detonating auto-router
adoption after 2 dead years (demand-side segmentation) + Cline's
subsidize→lock-in→gouge arithmetic ($200 subs ≈ $8–14K API value). Han b3
per-provider accuracy spread is the third face. User decision whether this
is a distinct thesis.

### Other movement
- **pat-environments-economy +3** (NVIDIA ships environments with model releases; Prime Intellect's full commercialize-the-loop product; first PHYSICAL-RESOURCE shadow — RL environments driving cloud CPU/NVMe/DRAM scarcity, from a neutral infra vendor).
- **Counter-edges**: sig-small-models-thrash-out-of-distribution → pat-model-not-bottleneck (Opus 3× better at 1/10 cost than Haiku out-of-distribution — cheaper-to-use-frontier inversion); sig-collaboration-moves-into-the-weights → pat-harness-over-model (~№12, Steinfurt shape: orchestrator/executor roles RL-trained into Fable/GPT-5.5-5.6). Both files ALSO carry clean claim-1 supports (BYOH post-training; verification-infra-flattens-quality) — consistent with the FINDING-1 rescoping.
- **pat-ai-native-org** hardest quantification yet: Uber 95% engineers on AI tools, 70% committed code, $2K/user/mo, "outage = work stops"; the $500M/month CFO accident.
- **pat-benchmark-trust-crisis** two minor legs: deployed quants have NO benchmark coverage at all (absent-measurement flavour; KLD measures distance not capability) + practitioner behavioral leg (real-repo bug test over leaderboards; GLM verified its build, Opus broke prod). 4th arena-gaming corroboration (Cohere "Leaderboard Illusion").
- **NEW candidate: "AI-native software category"** (Kramer ×2: inference at the core of every interaction; Knowledge Navigator now buildable; agents = web pages of 1995). Adjacent to b7 pat-adaptive-software, Browne b6, An/Hoe b6. NOT pat-ai-native-org (orgs ≠ artifacts).
- **Turbopuffer texture**: object storage collapsed retrieval economics ~100× ($100→$1/M vectors; Cursor bill −95%); S3-KV-caching queued as the next repricing; bootstrapped-profitable counterculture signal kept pattern-less.
- MCP corpus consolidation: MCP restructured to stateless core + extensions (breaking rewrite <1 yr); MCP-UI → official Anthropic+OpenAI extension; WebMCP absorbed into view tools. Davis + Salomon/Yosef independently confirm the restructure.

### Garbles / identity
- b8 "Idel Solomon" RESOLVED → **exp-ido-salomon** (primary source; Manufact reading rejected). Kwindla Hultman Kramer node now exists (was prose-only b2).
- ⚠ public-record resolutions to verify: Chris Alexiuk (NVIDIA), "Flex Run", "LM router bench", NeMo Gym naming, HF/llama.cpp acquisition.
- 7 substantive panel speakers NOT coined under the first-name rule (Vincent/Prime Intellect, Merve/HF, Parth/Ollama, Walden/Cognition, Alex/OpenRouter, Tuhin/NVIDIA, unnamed ModelOpt eng) — add-options documented in-file.
- el-lmarena (coined b15 heiner) corroborated by compression panel (Cohere reference) — optional IdentifiedInArtifact edge left to review.
- Recommend widening el-model-routing's b8 brief (naive per-request routing → session-level controller with probes/sidekick/cache economics).

## Batch-17 additions (reconciled) — post-event wave 3: verification/ops + engineering practice

_7 talks (published 2026-08-08 → 08-09). Still premiere-locked: OpenAI "Codex,
Behind the Harness" (shRR1e2HXMk, ~2026-08-11)._

### ⚑ pat-durable-execution + pat-agent-memory-layer — BOTH ledgers now complete
The missing dedicated-layer vendor arrived: **Resolve AI** sells always-on
cloud/sandbox ops agents as a product (confidence-gated DM-confirm, four proven
workloads), bundled with the clearest vendor-moat memory claim yet ("models are
capable; the moat is the learning system that knows YOUR environment" — ~12th
memory point, direct disagreement with Netflix's markdown-in-git). Against it,
the convention side gained its 4th practitioner (**Dailey: doc-as-state,
stateless agents, durable decision log**) and its heaviest instance: **GitHub
itself ships Agentic Workflows as markdown compiled onto stock Actions** —
the platform owner institutionalizing b13's el-ci-as-loop-runtime. Read either
as the strongest convention counter yet, or as convention-becomes-product.
Decision-ready.

### ⚑ pat-benchmark-trust-crisis — two legs thickened
- **Practitioner-behavioral now 3 points**: Cline real-repo test (b16), Linkov's maintained private re-run suite (O3 3h+10 mistakes → Opus 4.8 one-shot on the same task), Singh's own-PR bench that flipped Superconductor's default to Codex (with 1.5B tok/mo behind the decision).
- **Construction-methodology, reporting-threshold flavour, now a 3-SPEAKER cluster**: Shaukat (b2), Garg (b15), Linkov (b17) independently argue METR-style curves must be read at 90–99% accuracy — the 50% headline inflates capability ~5×. Rehome-ready on coin.
- Vendor-owned-benchmark structural note: Sonar's LLM leaderboard is scored with Sonar's own metrics; its CMU productivity study measured with SonarQube (Heiner-structure incentive flag, not a signal).

### ⚑ pat-ai-native-org — biggest single-batch ledger haul (~7 held signals)
First full **pathology taxonomy** (Dailey's velocity sickness: PR floods, agent
bankruptcy, decision ceding) + hard numbers (Singh: 99.9% of PRs
agent-generated, 100% human-reviewed, 1.5B tokens/mo ≈ $10K/day; support/growth
staff shipping merged fixes) + GitHub PMs authoring background automations +
Ace's branches-in-microVMs multiplayer surface. The Wharton rubber-stamp stat
(92.7% follow right AI review, ~80% follow wrong) lands on
pat-verification-gap but belongs in this candidate's brief too.

### Other movement
- **pat-value-of-judgement** (new name's first live batch): Anthropic's proctored CCA cert as credentialing of judgment ("CS no longer the magic pathway"); the **inversion signal** — agents now invoke humans as clarifiers/pairs-of-hands (Gazit, OpenClaw convergence); decision-ceding as pathology (Dailey); "vendor exams reveal production truth" insight.
- **pat-harness-over-model** +5 supports, all claim-1/reliability-scoped (monorepo-as-agent-infrastructure, deterministic guardrails "prompting the guardrails = fox loose in the henhouse", exam-canon-is-harness-discipline, Böhm–Jacopini loop insight). Zero counters this batch.
- **Fable-withdrawal shock: 3rd independent corroboration** (Singh) — homed to pat-sovereign-ai; provider-commoditization ledger +2 faces (token-seller incentives; Smith's token clampdown).
- **70%-ops quantification** ("coding was never the bottleneck") + typing-is-5% (100-dev longitudinal, cites Litt b6) → pat-model-not-bottleneck.
- AI-native-software-category +1 (GitHub: background automations "a bigger category than interactive AI").

### Garbles / identity / merge-checks
- exp-frank-coyle REUSED (2nd talk). exp-arjun-singh NEW — ⚠ surname collision with exp-varun-singh (Arcee b15), different people. "Eitan"→Idan Gazit. "Fiable"→Fable. "Metis' preview"→el-claude-mythos-preview (may also resolve b13 Cai's "Metis").
- ⚠ VERIFY before seeding: Superconductor domain (captions "superagent.com"), CCA exam official name/date, Gazit's 5%-study provenance, "Any Gravity"→Antigravity.
- Merge-checks queued: el-verification-debt vs el-reviewdebt/el-cognitive-debt; el-codebase-benchmarking vs el-private-benchmark (b12); el-ai-psychosis vs el-automation-bias; el-stop-reason-loop-control vs el-loop-flow-control (b13); el-agent-anti-patterns vs el-pattern-anti-pattern-catalog (b14); sig-cmu-ai-productivity-spike-reverts ≈ b2 sig-cmu-velocity-fade (same study — merge option).
- el-sonarqube promoted (reverses b2 restraint; drop-option in file). el-doc-as-shared-state defined in dailey, reused by gazit (b12 precedent). "idea velocity" ≡ Lee-Chan b6 title (re-home option).

## Batch-18 additions (reconciled) — post-event wave 4: harness internals + RL infrastructure

_2 talks (both published 2026-08-10). Small batch by design — this is the
channel's live release edge, not a backlog sweep. Kundel resolves batch 17's
pending premiere. Still premiere-locked: Anthropic "Evolution of agentic
surfaces" (K0X9QDRkIdg, ~2026-08-12), plus 11 staged-but-private uploads
queued in the World's Fair playlist._

### ⚑ pat-harness-over-model — a new counter-edge, and the best-sourced one yet
> **CORRECTION (made at batch 19):** this section originally said "9th
> counter-edge," counting from the b11 note's total of 8. That was stale —
> b15's FINDING 1 supersedes it with **~11**. The Kundel edge is therefore
> roughly the **12th**, not the 9th. The claim about its *quality* stands.
> See the batch-19 section for how it interacts with FINDING 1's re-scoping.
`sig-models-trained-into-their-harness` (Kundel) is the first counter-evidence
from **inside a frontier lab's own harness team**, and it is mechanical rather
than predictive: models from GPT-5 on are trained on the apply-patch tool;
they reach for Ripgrep because training taught them to, so Codex **bundles
Ripgrep**; Windows models emit PowerShell natively; server-side compaction
uses the format the model was trained against. Prior counters argued the model
would *absorb* the scaffolding (Steinfurt b6, Shihipar/Chandegra b7, Horthy
b11 ×3). This one says something sharper — the scaffolding is **downstream of
the model's training**, so the model is the least swappable component, not the
smallest. Read against the standing flag that this pattern "is OVERBROAD, not
merely contested": that flag now has its cleanest supporting exhibit.
⚠ Same talk carries the opposite claim (open Responses schema ⇒ any provider
is pluggable). Both emitted as stated; the tension is the vendor's.

### ⚑ NEW candidate — `pat-compute-liquidity` (proposed, NOT coined)
_The compute eligible for frontier training is being unbundled from
contiguous, tightly-coupled clusters, so scattered heterogeneous capacity
becomes fungible with dedicated capacity._ Coined nothing; **two signals held
pattern-less** in the Jiang file (`sig-rl-compute-shape-mismatch`,
`sig-inference-capacity-becomes-rl-capacity`). One-talk candidate today —
recorded so the ledger can accumulate. Prior corpus points to audit at review:
OpenAI agent sandbox cloud (b5), Prime Intellect decentralized post-training
(b5 + b15), Theta long-horizon environments (b15), MiniMax infrastructure
(b15), and the b16 Local-AI panel's "agents provisioning their own GPUs"
thread currently logged on `pat-agent-economy`. Distinct from
`pat-environments-economy` (that one is about environments as a tradeable
asset; this is about the *substrate* the training runs on).

### Other movement
- **pat-verification-gap** +1 strong: auto-review as a **read-only judge subagent that cannot spawn subagents**, given the risk taxonomy and live transcript, gating sandbox escalation — verification delegated to an agent made trustworthy by structural constraint rather than capability. Pairs with b17's Sonar/Resolve material as the "verifier is a boxed agent" thread.
- **pat-model-not-bottleneck** +4, unusually literal: Kundel's network-is-the-bottleneck finding (at ~1,000 tok/s on Cerebras the constraint became transport, not inference) and Jiang's whole framing (RL discourse is algorithms; at scale the problem is physical plant). Also the harness-differentiation-migrates-to-the-protocol signal.
- **Provider-commoditization ledger** (b17, homed on `pat-sovereign-ai`) gains a mirror-image data point: a frontier lab commoditizing **its own harness layer** — open-source Rust harness, open Responses schema under a governance body with Ollama, LM Studio and NVIDIA. No edge emitted; ledger note only.
- **pat-harness-over-model** also +2 supports from the same file (explicit context budgeting; agents scripting their own computer use via code execution) — the batch is net-contested on this pattern, not net-negative.

### Companies (4 new)
- `co-modal` (serverless GPU compute; author of Stitch — ⚠ captioned "Moto"/"model" throughout)
- `co-cerebras` (hardware; runs GPT-5.3 Codex Spark at ~1,000 tok/s)
- `co-ollama`, `co-lm-studio` (coined on reference per the b2 `co-openai` precedent, as Responses-schema governance partners; gives the b16 compression-panel Ollama thread a node to attach to — its speaker "Parth" was not coined under the first-name rule)
- Reused: `co-openai` (brief widens substantially — harness is open source, Rust, MIT/Apache-2), `co-nvidia`, `co-anthropic`, `co-cursor` (Composer 2 as an Adam post-training example), `co-moonshot-ai` (Kimi-scale checkpoint ≈500 GB; Muon adopter), `co-deepseek` (Muon adopter), `co-zhipu-ai` (GLM 4.7 Air, Modal's measurement run)

### Experts (2 new)
- `exp-dominik-kundel` (co-openai, Codex) — gave a second, separate World's Fair talk the prior day on the app server protocol; if that video publishes, `el-codex-app-server` is where it lands.
- `exp-nan-jiang` (co-modal) — ⚠ given name from the video byline only; captions render the self-introduction as "I'm N from Moto".
- NOT coined under the first-name rule: "David", author of OpenAI's Windows-sandbox write-up.

### Elements (15 new)
- Codex/harness internals: `el-responses-api`, `el-codex-app-server`, `el-deferred-tools`, `el-apply-patch`, `el-codex-sandbox`, `el-auto-review`, `el-websocket-mode`, `el-goal-continuation-prompt`
- RL infrastructure: `el-cathedral-vs-bazaar-compute`, `el-rollout-serving-island`, `el-adam-absorption`, `el-sparse-weight-delta`, `el-rollout-weight-version`, `el-version-aware-sidecar`, `el-stitch`
- **Element restraint on the Codex side:** five existing nodes reused rather than re-coined — `el-codex`, `el-context-compaction` (b6), `el-codex-computer-use`, `el-codex-goals`, `el-codex-skills-plugins` (b11). Each gains real new detail (the 2% skills cap; compaction trained-for-parity; computer use moving from an enumerated action API to code execution). **Recommend widening those briefs at seeding.** `el-goal-continuation-prompt` is coined separately because the continuation-prompt loop is the generalizable mechanism, distinct from the `/goal` feature.

### Garbles / identity / merge-checks
- ⚠ **The Jiang transcript is the worst in the corpus since b15 Chan/China Resources.** Normalization table in the file's review note 1: "IO"/"ADMIC"→RL, "Moto"→Modal, "addon"/"atom"→Adam, "BFC"/"BF6"→BF16, "oop"→ULP, "scikar"/"psychar"→sidecar, "muan"→Muon, "deepc4"→DeepSeek, "sjet"→SGLang, "bro"→bazaar, "way sync"→weight sync, "Kim scale"→Kimi-scale, "GM 4.7 air"→GLM 4.7 Air.
- ⚠ **VERIFY before seeding (Jiang):** the **cited paper is never named** — the Adam-step bound is attributed to "the paper I cited" with the slide off-transcript. Every quantity in that file is single-source caption text (~99% bit-identical/step; 500 GB→500 MB; BF16 ULP ≈0.0078, boundary ≈0.0039; Adam step ≈3e-6; GLM 4.7 Air FP8 at 0.15%→0.05%). The fragment "cursor composer 2 mi they all using add in the post training" may name a second vendor (possibly MiniMax, b15) — tail unrecoverable, only the Cursor reference emitted.
- ⚠ **VERIFY before seeding (Kundel):** model version strings are load-bearing and caption-sourced — **GPT-5.4** (added deferred-tool marking), **GPT-5.3 Codex Spark** (the Cerebras deployment), the 1,000 tok/s figure, and the 2% skills cap.
- **Merge-check queued: `el-rollout` collision.** Coined b11 (Laude/Harbor) as the *unit of agent evaluation*; used here as the *serving job producing trajectories*. Reused as one node with `UsesElement → el-rollout-serving-island` on a same-concept-two-altitudes reading. If review disagrees, split into `el-rollout-eval` / `el-rollout-serving` and re-point the single edge in the Jiang file — nothing else depends on it.
- Forward flag: the Jiang argument is **Adam-specific by construction**. If Muon breaks the bounded-step property, `sig-rollout-weights-99pct-bit-identical` narrows from a general result to an Adam-era one. Re-check when the next post-training wave lands.

### Bookkeeping fix
`extraction/README.md` — the seven enterprise-tail files (kumar-flyerssoft,
rallabandi, emani, chan, ganesh-kepler-verifiable, menkes, rappazzo) are
**batch-15** talks that had been dangling under whichever batch header was
appended last (b16, then b17). Labelled with an explicit "Batch 15 (cont.)"
marker row rather than moved, so file order and any in-flight review links are
preserved. Batch 15's count of 29 talks reconciles only with these seven
included.

## Batch-19 additions (reconciled) — the Continual Learning track + agent design

_13 talks (10 published 2026-08-12 as a **dedicated Continual Learning
track**, 3 agent-design talks published 2026-08-11 → 08-12, including
batch-18's twice-slipped Anthropic premiere). The largest single-theme batch
in the corpus. The staged-private queue has fully drained; no premieres
pending for the first time since batch 16._

### ⚑⚑ COIN RECOMMENDATION 1 — `pat-agent-memory-layer` — the ledger is now closed
Recommended for coining since **batch 10** ("decisively past threshold"), and
recorded complete at b17. This batch supplies the two things it still lacked:

- **An independent survey.** Khemani spent a year reverse-engineering ChatGPT, Claude, Gemini and Poke. Findings: three years of *independent* evolution converged on the same architecture from opposite ends — ChatGPT from a user-curated fact list toward background profile synthesis, Claude from retrieval-only tools toward a profile — and **neither uses RAG**, the approach the industry assumed. Published cost trade-offs for both (ChatGPT ~4,000 tokens every few days; Claude ~1,000 tokens every 24 hours — opposite corners of the same maintenance-versus-serving constraint). Plus a market scan: every top consumer AI product has memory, **none outsource it**.
- **A frontier-lab roadmap.** Anthropic ships memory + **dreaming** (periodic batch over session transcripts + memory state, editing memory so the next day's sessions are smarter), calls them "two cornerstones of a new frontier unified memory system," and flags **organizational-scale memory** (team runbooks) as an emerging third form.

**Held pattern-less awaiting the coin:** `sig-memory-architectures-converged`,
`sig-memory-cannot-be-outsourced`, `sig-continual-learning-already-shipping`
(all Khemani), `sig-session-log-powers-memory-and-dreaming` (Anthropic).
**Would re-target on coin:** `sig-memory-budget-is-a-compute-decision`
(currently on `pat-model-not-bottleneck`).
**⚑ Attach as a COUNTER-edge on day one:** `sig-memory-adds-nothing-when-context-fits`
(Druga) — a controlled ablation finding that when the task fits in context,
memory adds cost and **zero** capability. A pattern that arrives with its own
counter-evidence is healthier than one that does not.
**Scope note for the brief:** Khemani's no-outsourcing finding is explicitly
about *consumer personalization*; most vendors in this track sell into
enterprise. Say so in the brief rather than letting the two collide.

### ⚑ COIN RECOMMENDATION 2 — `pat-continual-learning-turn` (proposed at b19, NOT coined)
_Thesis: the frontier of model improvement is shifting from pre-training scale
to post-deployment learning, making the accumulation loop — not the base model
— the locus of compounding advantage._ A ten-talk dedicated track in one day
is the strongest single-batch evidence the corpus has ever seen for any
candidate. **Six distinguishable legs:**

1. **New axis of scale** — Su ("intelligence is abundant, expertise is scarce"; orthogonality; *escape intelligence*), Morris (a named fourth axis, since data and model size are fixed for a private corpus).
2. **Algorithms** — Malde's OPSD (satisfies all four post-training criteria at once by making the teacher the same model with a hint), Denton's four-quadrant offline/online × trace/hint taxonomy with two measured results.
3. **Measurement** — Asawa's CL-Bench and the **gain** metric (stateful minus stateless), plus the finding that benchmark instances are *designed* independent and therefore cannot be chained.
4. **Supply/economics** — Morris (all scaling has only ever touched public data, and the data-vendor layer structurally reproduces that boundary), Su (private microworlds as the next internet-scale data opportunity), Hooker (pre-training saturated; returns moved to distributable post-training compute).
5. **Already shipping** — Khemani (running profiles *are* a learning loop, outside the weights), Anthropic (dreaming), Holmes (nightly cloud enrichment of a personal corpus), Trivedy (observability and continual learning are the same problem from two ends).
6. **Enterprise reality** — Denton ("this is where a lot of enterprises are today": a pile of traces and "make our agent better").

**⚑ Arrives with three independent dissents — preserve them:** Hylak
(cross-customer production visibility: "in the real world there's really not
that much continual learning"), Asawa (**vanilla in-context learning tops the
CL-Bench leaderboard** on reward *and* both cost-adjusted Pareto frontiers,
beating engineered context management), Druga (memory adds nothing below the
context-window threshold). Malde adds a self-dissent: the field is in
"pseudo continual learning" — batch updates offline, then re-upload.

**Naming convergence is unusually strong.** "Dreaming" is used independently
by Khemani (community name for background synthesis), Morris (in an
eight-synonym list — sleep-time compute, neural memory, write-time compute,
note taking, dreaming, studying, machine studying, amortized inference),
Trivedy (sleep-time compute over the agent lifecycle), and Anthropic (a
shipped feature). Four uses, one batch, no coordination.

### ⚑ FINDING — `pat-harness-over-model`: b19 is the decisive test case for FINDING 1
b15's FINDING 1 recommends scoping the brief to **claim 1 (reliability/
latency/control)** and dropping claim 2 (improvement/capability). This batch
supplies the cleanest test yet, from one talk:
- **Anthropic carries both edges, minutes apart.** `sig-harness-is-now-the-limiting-factor` (a frontier lab stating "harnesses have become the limiting factor to what models can achieve") **supports**; `sig-harness-fixes-become-dead-weight` — Sonnet 4.5's *context anxiety* prompted harness context-resets, Opus 4.5 didn't exhibit it, and the fix became "pure overhead, adding latency and causing issues with the cache being discarded incorrectly" — **contradicts**.
- Under the recommended re-scoping the support survives cleanly and the counter resolves into a **maintenance** claim (harness workarounds for model deficiencies expire), not a capability claim. **Read the Bhat/He file first at the pattern review.**
- Same resolution applies to b18's Kundel counter (harness ships what the model was trained on) — it targets claim 2 and would resolve.
- **Does NOT resolve:** Asawa's `sig-vanilla-icl-tops-the-leaderboard`. That is an independent academic result, cost-adjusted, on real tasks, against engineered machinery — a genuine claim-1 survivor. Treat it as the counter-edge that matters.
- Clean claim-1 exemplars this batch: Khandelwal (team harness engineering, progressive disclosure with a measurable threshold), Trivedy (harness-first-then-finetune, argued from feedback latency), Hylak (deterministic detection, agentic investigation).

### Other movement
- **pat-verification-gap** — remains the corpus's dominant thesis; +9 this batch. Most significant: **both leading labs shipped verification-by-constrained-second-agent as a platform primitive within 48 hours** — Anthropic's **outcomes** (rubric-defined success, separate grader agent, loop until met) and OpenAI's **auto-review** (b18: read-only judge subagent, cannot spawn subagents, gates sandbox escalation). Neither references the other. Also: Asawa's gain metric, Druga's oracle-doesn't-saturate finding, Hylak's four eval/triage signals, Malde's hint-leakage.
- **pat-model-not-bottleneck** +8. Strongest: Morris's structural argument that the commercial data layer *cannot* cross the public/private boundary because vendors can only sell what a model may say back.
- **pat-sovereign-ai** +4, from an unusual direction: Druga (local-model evaluation as sovereignty, corroborated by **Coinbase** cutting AI spend while raising usage), Hooker ×2 (pre-training compute must be co-located; post-training compute distributes, so "the person with the best idea has a higher chance of winning"), Su (private microworlds; enterprises "in charge of their means of production").
- **`pat-compute-liquidity` (b18 candidate)** — Hooker is its second data point and its mirror image: b18's Modal talk argues scattered compute becomes *usable* for post-training; Hooker argues post-training is where returns now *live*. Read together at review.
- **pat-ai-native-org** — Khandelwal adds a second high-quality dysfunction data point after b17's Dailey: the full arc (leverage → mandates → token-maxxing → slop and sev-2s → retraction → budgets bolted on), from a frontier-lab engineering org rather than a vendor.
- **pat-benchmark-trust-crisis** — two more legs, both held pattern-less: Malde's **task-distribution mismatch** (benchmarks decoupled from where tokens are actually spent — a 10th distinguishable leg) and Asawa's construction-methodology point. Trivedy adds an unemitted gaming-leg restatement from the builder's side ("the purpose of evals is roughly to make them pass").
- **pat-durable-execution** — Holmes's nightly cloud enrichment (sync down, run skills, sync back; explicitly contrasted with laptop-bound local automation) is a clean addition; held pattern-less.
- **pat-context-graphs** — Khemani's context-acquisition gap and Holmes's generated wikis both land here; the seed thesis keeps absorbing this cluster.

### Companies (9 new)
- Continual-learning startups: `co-neocognition` (Su), `co-engram` (⚠ captioned "Ngram"/"N gram"; normalized from `ngr.am`), `co-trajectory` (Malde), `co-adaption-labs` (Hooker)
- Research/labs: `co-sakana-ai` (Tokyo; sovereign-AI position stated institutionally), `co-ohio-state` (Su's dual affiliation, per the b8 `co-university-of-maryland` precedent)
- Tooling/observability: `co-warp` (terminal + oz.dev automation cloud), `co-raindrop` (agent observability; "Sentry, but for agents")
- Coined on reference: `co-windsurf` (Malde's prior employer, ⚠ see garbles), `co-coinbase` (spend-down/usage-up with local models — the only third-party quantitative support in the Druga talk)
- Reused with substantial new facts, **recommend widening briefs**: `co-anthropic` (Applied AI team; three-generation surface lineage; dreaming/outcomes), `co-applied-compute` (2nd appearance — platform research team, distillation taxonomy), `co-langchain` (applied research function, trace mining, open-model fine-tuning service), `co-amazon` (3rd AGI Lab appearance, 1st on internal engineering practice), `co-uc-berkeley` (3rd, 1st from research rather than curriculum), `co-snorkel-ai` and `co-laude-institute` (both now recorded as **funders** of neutral benchmark infrastructure — a repeat role, b12 and b11 respectively), `co-decagon` (2nd, now as an AI-infrastructure *buyer*)
- **Add-option at review:** `co-harvey` — two independent b19 mentions (Trivedy's legal-benchmark collaborator; Malde's early-access customer). Not coined in either file since neither attaches company facts.

### Experts (14 new)
`exp-yu-su` (co-neocognition + co-ohio-state), `exp-jack-morris` (co-engram),
`exp-ronak-malde` (co-trajectory), `exp-parth-asawa` (co-uc-berkeley),
`exp-samuel-denton` (co-applied-compute), `exp-sara-hooker` (co-adaption-labs +
co-google-deepmind), `exp-shlok-khemani` (independent — **no company edge**),
`exp-stefania-druga` (co-sakana-ai), `exp-ben-holmes` (co-warp),
`exp-vivek-trivedy` (co-langchain), `exp-gagan-bhat` + `exp-isabella-kai-he`
(both co-anthropic), `exp-aditya-khandelwal` (co-amazon), `exp-ben-hylak`
(co-raindrop).
- ⚠ **`exp-ben-hylak` vs `exp-veronica-hylak` (b8, Hey AI) — different people.** Keep given names in both labels. Same class as b17's `exp-arjun-singh`/`exp-varun-singh`.
- NOT coined under the first-name / passing-reference rules: Rosanne Liu, Merve (HF — declined again, consistent with b16), Andrew Ng, Satya Nadella, Ilya Sutskever, Karpathy, Schulman, Demis Hassabis, Dwarkesh Patel, Gwern, "David" (b18).
- ⚠ **Corpus-correction lead:** Khemani cites "Lance Martin's talk yesterday" on dreaming. The corpus has listed Martin's Anthropic talk as *permanently unavailable* since b3 and `transcripts/README.md` still says so. He evidently spoke at this event — worth a re-check.

### Elements (~64 new)
- Conceptual frame: `el-intelligence-vs-expertise`, `el-microworlds-thesis` (⚠ collision with `el-microworlds` b6), `el-modern-moravec-paradox`, `el-continual-learning-definition`, `el-escape-intelligence`
- Scaling/method: `el-scaling-compute-on-context`, `el-breadth-vs-depth`, `el-private-corpus-training`, `el-synthetic-data-wall`, `el-recursive-self-improvement-loop`, `el-death-of-scaling`, `el-distributed-compute-returns`, `el-auto-scientist`, `el-unreasonably-narrow-path`
- Distillation: `el-post-training-four-criteria`, `el-on-policy-self-distillation`, `el-hint-leakage`, `el-step-level-divergence-weighting`, `el-residual-guidance`, `el-distillation-spectrum`, `el-hint-provenance-axis`, `el-distillation-quadrants`, `el-per-step-hinting`, `el-relevance-masked-distillation`
- Measurement: `el-continual-learning-bench`, `el-gain-metric`, `el-cl-benchmark-criteria`, `el-stability-plasticity-failures`, `el-cl-first-order-design`
- Memory: `el-running-profile`, `el-memory-fact-list`, `el-conversation-search-tools`, `el-memory-convergence`, `el-memory-compute-tradeoff`, `el-context-acquisition-gap`, `el-memory-write-manage-read`, `el-recall-policy-ladder`, `el-decisions-ledger`, `el-recall-policy-as-metric`, `el-dreaming`
- Knowledge bases: `el-llm-knowledge-base`, `el-voice-capture-pipeline`, `el-enrich-note-skill`, `el-generated-wiki`, `el-nightly-agent-schedule`
- Traces/observability: `el-agent-trace-mining`, `el-trace-scale-problem`, `el-model-harness-task-fit`, `el-harness-then-finetune-sandwich`, `el-dense-feedback-signal`, `el-issue-not-cluster`, `el-issue-onset-and-blast-radius`, `el-code-mode-over-traces`, `el-evals-as-code`, `el-floor-vs-ceiling`
- Agent architecture: `el-agentic-surface-generations`, `el-harness-assumption-staleness`, `el-brain-hands-decoupling`, `el-managed-agent-primitives`, `el-durable-session-log`, `el-outcomes-grader`
- Team practice: `el-fear-utilization-map`, `el-bad-setup-symptoms`, `el-team-harness-engineering`, `el-progressive-disclosure-codebase`, `el-ship-it-skill`
- **Reuse discipline — recommend widening these briefs at seeding** rather than re-coining: `el-anthropic-managed-agents` **[seed]** (the Bhat/He file is by far its richest source; the seed node predates every engineering detail — highest-value cleanup in this batch), `el-continual-learning` **[b8]** (Su supplies the definitional scaffolding it lacked), `el-on-policy-distillation` **[b5]** (Malde is its deepest treatment), `el-autoresearch` **[seed]** (Hooker's data-co-optimization contrast is its sharpest differentiation), `el-agents-md` **[b6]** and `el-agent-skills` **[batch1]** (concrete authoring constraints: thin-index discipline, ~100-line skill cap, fixed tag vocabularies, enrichment timestamps), `el-code-mode` **[b6]** (extended from MCP to trace analysis), `el-context-compaction` **[b6]** (measuring behaviour *across* compaction boundaries is a new use).

### Cross-file edges emitted within this batch (unusual — flagged)
- `el-hint-provenance-axis` (Denton) `UsesElement → el-on-policy-self-distillation` (Malde). The two talks are the same technique from two vantage points — Malde derives it and names its failure mode, Denton industrializes it and adds provenance, per-step injection and relevance masking. Neither cites the other. **Drop if review prefers strictly within-file edges**; the relationship is also recorded in prose in both files.
- Proposed but NOT emitted, left to review: `el-on-policy-self-distillation` → `el-scaling-compute-on-context` (Morris cites Malde by name from the stage); `el-llm-knowledge-base` → `el-html-native-medium` (b9); `el-team-harness-engineering` → `el-reviewdebt` (b5).

### Garbles / identity / merge-checks
- ⚠ **Title/content mismatch — Hooker.** Billed "Adaption Labs: Gradient-Free Continual Learning"; the delivered talk never uses the phrase and presents no gradient-free method. No element coined for it; the `ia-` node keeps the billed title for link fidelity. If the lab's gradient-free work matters, it needs a different source.
- ⚠ **`el-microworlds-thesis` vs `el-microworlds` (b6)** — coined separately on the view that Su's "millions of microworlds" (idiosyncratic per-organization environments requiring per-instance learning) is a distinct claim. Grep both before seeding; merge if review disagrees.
- ⚠ **VERIFY before seeding (highest-risk):** Malde's Windsurf story ("SWE-1… the two billion acquisition at DeepMind" — model name, amount and acquirer all need checking); Anthropic model version strings (**Sonnet 4.5**, **Opus 4.5** in the context-anxiety story, **Opus 4.8** in the demo) and whether "context anxiety" appears in Anthropic's public writing; Khemani's memory dates and token sizes (reverse-engineered observations, not vendor documentation); Denton's "Qwen 3.5 thinking"; Druga's "Qwen 27B" (likely **Qwen3 27B**) and the unattributed 30-cookbook repo (captioned "Diamond"); Trivedy's product name (captioned "LangSplat engine" — almost certainly wrong, so no product node coined); Hooker's "fewer than 5,000 people" and the death-of-scaling paper title; Khandelwal's context thresholds (20–25K baseline / 40–50K as failure) and the ~100-line skill cap.
- Systematic garbles resolved per file: "hardness"→harness (Khandelwal, throughout), "Cloud"→Claude (Bhat/He, throughout), "Chad GPT"→ChatGPT (Khemani), "gpo"→GRPO and "opsd/ops"→OPSD (Malde), "N gram"→Engram (Morris), "Isu"→Yu Su, "Partasawa"→Parth Asawa, "Schllo"→Shlok, "Century"→Sentry (Hylak), "Parto Frontiers"→Pareto frontiers (Asawa).

### Note on scale
This batch adds ~64 elements and ~66 signals across 13 files — roughly triple
a normal batch. If review wants to prune, the highest-confidence keeps are:
Druga's controlled ablation (the only properly-designed memory experiment),
Asawa's gain metric and ICL result, Denton's two measured before/afters,
Malde's failure analysis, Anthropic's split evidence on the harness pattern,
and Khemani's survey. The weakest evidence base despite the strongest
credentials is Hooker's — every quantity in it is vendor-stated without a
baseline.

## Coinage record — 2026-08-14

User approved both batch-19 recommendations at review. Two patterns coined,
bringing the corpus to **12 coined patterns** (5 seed + 2 b1 + 2 b2 + 1 b5 +
2 b19). This is the first coinage since batch 5 — the corpus ran 14 batches
on ledger discipline before either candidate cleared.

### `pat-agent-memory-layer` — The Agent Memory Layer (dynamic)
Defined in `khemani-every-memory-system.md`. Recommended since b10, complete
at b17, coined on b19's survey evidence.

**Support edges attached (6):**
| signal | file | note |
|---|---|---|
| `sig-memory-architectures-converged` | khemani (b19) | ChatGPT and Claude converged from opposite ends; neither uses RAG |
| `sig-continual-learning-already-shipping` | khemani (b19) | dual edge with `pat-continual-learning-turn` — running profiles *are* a learning loop, outside the weights |
| `sig-memory-budget-is-a-compute-decision` | khemani (b19) | **re-targeted** from `pat-model-not-bottleneck` |
| `sig-session-log-powers-memory-and-dreaming` | bhat-he (b19) | frontier-lab roadmap: memory + dreaming as "cornerstones of a unified memory system" |
| `sig-memory-is-what-the-agent-becomes` | rallabandi (b15) | **rehomed** from `pat-context-graphs` per that file's review note 4 |
| `sig-ops-agent-value-is-learned-context` | smith-resolve (b17) | the clearest vendor-moat framing in the ledger |
| `sig-observability-and-continual-learning-converge` | trivedy (b19) | dual edge with `pat-continual-learning-turn` |

**Counter edges attached at coin (4)** — deliberate, and the reason the
pattern is healthy:
| signal | file | the counter |
|---|---|---|
| `sig-memory-adds-nothing-when-context-fits` | druga (b19) | controlled ablation: below the context window, memory costs tokens and buys **zero** capability |
| `sig-memory-cannot-be-outsourced` | khemani (b19) | no serious consumer product outsources memory; converged part is cheap, divergent part is product-specific |
| `sig-netflix-pattern-catalog-memory` | shah-netflix (b14) | convention counter — markdown in a git repo, not a memory product |
| `sig-sla-budget-caps-agent-design` | kumar-flyerssoft (b15) | SLA counter — a sub-500 ms budget rules long-term agent memory out entirely |
| `sig-docs-replace-chats-as-work-atom` | dailey (b17) | convention counter — the state layer is a shared document |

_(5 rows; the Netflix and FlyersSoft signals keep their existing
`pat-harness-over-model` edges and gain the counter as a second edge.)_

**⚠ Follow-up pass still owed — b9/b10 graph-cluster files.** The b10 registry
note counted ~9 data points toward this ledger from the graph/context/ontology
cluster: Zep/Graphiti (`chalef-zep-kg-provenance`), BabyAGI 4's event log
(`nakajima-babyagi4-active-graph-runtime`), TwelveLabs video memory
(`le-twelvelabs-video-memory`), CrabRAG (`chin-neo4j-crabrag-graph-memory`),
Eifrem's traces pillar (`eifrem-neo4j-ontology-semantic-layer`), monday.com's
durable profile (`bruchim-ast-monday-systems-of-context`), plus batch 9's
three. **Those signals were NOT auto-rehomed** — they are currently on
`pat-context-graphs`, they were homed there deliberately, and several belong
there on the merits (the talks argue graph organization, not memory-as-layer).
Each needs a per-signal judgement: rehome, dual-edge, or leave. Recommend a
dedicated pass rather than a sweep.

**⚠ Also owed:** `smith-resolve-always-on-agents.md` withheld
`ExemplifiesPattern` edges from `el-background-agents` and
`el-production-learning-system` because no fitting pattern existed. The second
now has one. Element-level edges were not swept in this pass.

### `pat-continual-learning-turn` — The Continual Learning Turn (dynamic)
Defined in `su-neocognition-continual-learning-expertise.md`. Proposed and
coined in the same batch — justified by a ten-talk dedicated track in one day,
the largest single-theme evidence base the corpus has seen.

**Support edges attached (8):**
| signal | file | leg |
|---|---|---|
| `sig-scaling-expertise-as-new-axis` | su | new axis of scale (anchor) |
| `sig-reliability-plasticity-tension` | su | stability/plasticity |
| `sig-scaling-only-ever-touched-public-data` | morris | supply economics |
| `sig-fourth-scaling-axis-proposed` | morris | new axis of scale (second anchor) |
| `sig-software-that-improves-every-use` | malde | algorithms |
| `sig-cl-failures-split-stability-plasticity` | asawa | measurement / stability-plasticity |
| `sig-enterprises-start-at-offline-traces` | denton | enterprise reality |
| `sig-observability-and-continual-learning-converge` | trivedy | already shipping (dual edge) |
| `sig-continual-learning-already-shipping` | khemani | already shipping (dual edge) |

**Counter edge attached at coin (1):**
| `sig-little-real-continual-learning` | hylak (b19) | an observability vendor with cross-customer production visibility reports seeing little real continual learning in the wild |

**Two further dissents recorded but not edged**, because they target the
methods rather than the thesis: Asawa's `sig-vanilla-icl-tops-the-leaderboard`
(currently `ContradictsPattern → pat-harness-over-model`) and Malde's
"pseudo continual learning" admission inside
`sig-software-that-improves-every-use`. Both belong in the brief's contested
clause, which they are in.

### Consequences for the remaining ledgers
- `pat-agent-economy`, `pat-environments-economy`, `pat-ai-native-org`, `pat-benchmark-trust-crisis`, `pat-durable-execution`, `pat-adaptive-software`/`pat-adaptive-harness`, `pat-fde-turn`, `pat-compute-liquidity` (b18) all remain **uncoined**. Nothing in this coinage changes their status.
- `pat-durable-execution` is now the longest-standing recommendation (b5), and b17 recorded its ledger complete. It is the obvious next candidate.
- b15's **FINDING 1** on `pat-harness-over-model` (re-scope to claim 1) is untouched by this coinage and still pending. The b19 Anthropic file remains the recommended test case.

## Batch-20 additions (reconciled) — the Computer Use (CUA) track

_7 talks, all published 2026-08-14, released as a dedicated **Computer Use
(CUA)** channel playlist (`PLEz0frWjePik`) OUTSIDE the World's Fair 2026
playlist — the first track the channel has published as its own collection
rather than folding into the main playlist. Coherent theme: agents using the
web the way humans do (pixels, clicks, browsers), the infrastructure and
training behind it, and the data/context supply layer._

### ⚑ The track is one sustained argument, split across two coined-pattern axes
Four talks converge on **"the web gets agentified by computer-use, not
protocols"** but split exactly along b15's FINDING 1 claim-1/claim-2 line:
- **Batra (Yutori) — thesis talk.** The long tail of the web will never publish APIs/MCP; the browser is a rendering engine so pixels are the source of truth; general pixels-in models generalize where per-site scaffolds don't. `sig-scaffolds-dont-generalize-pixels-do` **contradicts** `pat-harness-over-model` (capability/claim-2 side — the model generalizes, the scaffold doesn't).
- **Klein (Browserbase) — opposite emphasis, same track.** Models are already good enough; the gap is a *capabilities overhang* closed by harness + infrastructure. `sig-domain-harness-beats-raw-model` **supports** `pat-harness-over-model` (reliability/claim-1 side).
- **Mishra (Amazon AGI) — from inside the training loop, holds BOTH.** Perception is a missing *model* capability coding can't supply (`sig-coding-skill-insufficient-for-cua` **contradicts** `pat-model-not-bottleneck`), AND the harness is temporary scaffolding that "thins as the model improves" (`sig-harness-thins-as-model-improves` **contradicts** `pat-harness-over-model`, claim-2).
- **Gallon — the how-to.** CLI-driving-CDP beats MCP on reuse/speed/cost; `sig-cli-beats-mcp-for-browser-control` **supports** `pat-harness-over-model` (claim-1).

**This track is the single best exhibit yet for the FINDING 1 re-scoping**
(scope `pat-harness-over-model` to claim 1). Under it: Klein and Gallon's
supports survive; Batra's and Mishra's counters resolve as claim-2 (capability
migrates to the model). Read Mishra first at the pattern review — one speaker
holding perception-needs-more *and* harness-needs-less coherently is the
cleanest statement of the split the corpus has produced. Net counter-edges on
`pat-harness-over-model` from this batch: +2 (Batra, Mishra), both claim-2.

### ⚑ `pat-new-cyber-threats` — biggest single exhibit since batch 1
**Gallon defeats four production CAPTCHAs live, no human in the loop**
(Cloudflare Turnstile, MTCaptcha, GeeTest-style jigsaw, reCAPTCHA v2) on
commodity primitives: CDP's **trusted-event path** (a real input-domain click
is stamped "trusted," indistinguishable from a human mouse) plus a vision
model. Two signals home directly on the pattern; `ins-captcha-is-over-as-a-boundary`
ties it to Klein's "Verisign moment" gap in the same track — bot defense must
move from challenge to **attestation/identity**, which nobody has built.
`el-cdp-cli-driving` carries a rare `EnablesPattern → pat-new-cyber-threats`
(element enabling a threat pattern — appropriate; the capability *is* the
threat surface). Klein's `ins-trust-not-capability-gates-the-agent-web` adds a
second `pat-new-cyber-threats` insight from the defense side.

### ⚑ `pat-agent-economy` — the biggest single-batch haul (machine-web leg)
The candidate the corpus has circled since b2/b5 (Povilionis receipts, Raskar
bazaar, Vending-Bench, Local-AI panel, b16 MCP-apps). This batch adds the
**machine-web leg**: agents becoming the web's primary actors, routing around
API governance by using the human interface. Signals held pattern-less awaiting
the coin: `sig-long-tail-will-never-publish-apis` (Batra — counter-flavoured
vs the protocol-optimist side), `sig-web-agentified-by-browser-layer` (Batra),
`sig-web-must-become-agent-legible` (Klein), `sig-web-ui-as-permissionless-api`
(Gallon). **Recommend adding `pat-agent-economy` to the next coin review** — it
now spans commerce (b2/b5/b11), protocols (b8/b16), and the machine-web (b20),
which is either strong convergence or a sign the candidate is too broad and
should split (machine-web vs agent-commerce). Flag the split question.

### ⚑ `pat-benchmark-trust-crisis` — two rigorous new legs, with a proof
D'Oro's **replay agent** (a <1MB blind script of recorded trajectories matches/
beats the frontier model on deterministic CUA benchmarks) and the **pass@k =
replay** proof are gaming/construction-methodology legs with a *formal proof*,
not an anecdote — a CUA-specific determinism/replay leg distinct from the nine
in b15 FINDING 2. Both held pattern-less (`sig-replay-agent-beats-frontier-models`,
`sig-passk-is-a-gameable-metric`). This candidate (~13 registry mentions) is the
best-evidenced uncoined pattern after `pat-agent-economy`. `sig-frontier-models-not-robust-to-variation`
(DG-World shows models lose performance under theme/screen variation) homes on
`pat-model-not-bottleneck`.

### ⚑ `pat-agent-memory-layer` (COINED b19) — first supply-side evidence, already contested
Primor (Bright Data) coins the term **CaaS (context-as-a-service)** — vendors
structuring the web into agent-consumable knowledge graphs. This is the
**acquisition** side of the memory layer (b19 coined it from the *retention*
side). Arrives contested from the same talk: `sig-caas-category-emerging` and
`sig-owned-context-compounds` **support**; `sig-caas-limited-to-what-it-holds`
**contradicts** (pre-indexed context answers within its index, goes silent
outside it). Žemaitytė (Oxylabs) adds `sig-web-infra-is-adapt-forever`
(maintenance-as-moat) from the raw-data layer beneath CaaS.
**Recommend the brief note both sides:** retention (memory products) +
acquisition (CaaS), with data-decay as why acquisition is a subscription.

### `pat-environments-economy` (uncoined) — two more data points
Mishra's "flight school, not exams" (deliberately messy/adversarial training
sandboxes; fidelity as moat) and D'Oro's PRISM/DG-World (verified-valid
environments; verification strategy as the moat, not generation volume). Both
held pattern-less. This candidate keeps accumulating without a coin — worth
pairing with `pat-benchmark-trust-crisis` at review since D'Oro's work straddles
both.

### Companies (7 new)
- CUA model/agent vendors: `co-yutori` (Batra — Navigator model), `co-browserbase` (Klein — browser infra + Browse.sh/AutoBrowse/Browserbase agents), `co-programma-labs` (D'Oro — CUA verification infra)
- Web-data / context vendors: `co-bright-data` (Primor — CaaS, Scraper Studio), `co-oxylabs` (Žemaitytė — proxy/web-data infra)
- Reused with new facts: `co-amazon` (**5th** AGI Lab appearance — Mishra, 1st on CUA *training*; also the AgentCore web index in Primor's talk — recommend widening brief), `co-cloudflare` (Turnstile, in Gallon), `co-microsoft` (web-BYOQ, in Primor), `co-openai` (Gallon's ban story + Codex), `co-meta` (D'Oro's work done there), `co-anthropic` (Opus 4.8 as harness), `co-google` (WebMCP, grounding docs, reCAPTCHA)
- **Add-option:** the AI-search cohort Exa/you.com/Tavily named in Primor (Parallel already coined) — not coined, passing references.

### Experts (7 new)
`exp-dhruv-batra` (co-yutori), `exp-paul-klein` (co-browserbase), `exp-corey-gallon`
(**no company edge** — Chrome Agent is his, no employer stated), `exp-gaurav-mishra`
(co-amazon; ex-Google Brain/DeepMind), `exp-pierluca-doro` (co-programma-labs +
co-meta, dual affiliation), `exp-omer-primor` (co-bright-data), `exp-patricija-zemaityte`
(co-oxylabs).
- NOT coined (passing references): Karpathy, Brockman, Will/Exa, "Docus" (unresolved).

### Elements (~34 new)
- CUA thesis/model: `el-long-tail-web`, `el-pixels-are-source-of-truth`, `el-yutori-navigator`, `el-agentification-by-accretion`, `el-cua-progress-rate`
- Browser harness/infra: `el-cua-capability-overhang`, `el-browser-agent-triad`, `el-agent-legible-web`, `el-browserbase-agents`, `el-agent-identity-broker`
- Web-automation how-to: `el-cdp-cli-driving`, `el-digital-senses`, `el-sense-act-verify-loop`, `el-meatbag-ladder`, `el-solver-operator-split`
- CUA training: `el-rl-to-irl-gap`, `el-flight-school-not-exams`, `el-high-fidelity-sandbox`, `el-cua-perception-primitives`, `el-thinning-harness`
- CUA evals: `el-replay-agent`, `el-passk-is-replay`, `el-prism-principles`, `el-dg-world`, `el-honest-confidence-intervals`
- Context/data supply: `el-context-as-a-service`, `el-web-as-context-not-data`, `el-data-decay`, `el-rented-vs-owned-context`, `el-web-context-engineering`, `el-web-data-pipeline`, `el-speed-becomes-product`, `el-scale-is-not-a-finish-line`, `el-adapt-forever-infrastructure`
- Reuse: `el-mcp`, `el-agents-md`, `el-code-mode`, `el-agent-skills`, `el-computer-use-verifier`, `el-openclaw`, `el-company-brain` — several with new deployment surfaces (Browse.sh = per-website skills; CLI-over-MCP = code-mode instance). Recommend widening `el-company-brain` if the Primor cross-file edge is accepted.

### Cross-file edges (within batch, proposed but NOT emitted — left to review)
- `el-context-as-a-service` (Primor) `UsesElement → el-web-data-pipeline` (Žemaitytė) — CaaS built on raw web-data infra. Same-batch siblings.
- `el-rented-vs-owned-context` (Primor) → `el-company-brain` (b3, Tan) — the data-supply mechanics under Tan's company-brain thesis.
- `el-dg-world` / `el-private-benchmark` (b12) — contamination-resistant construction neighbors.

### Garbles / identity / merge-checks
- ⚠ **Batra caption garble is load-bearing:** "agentify / API-fy the web" → "identify" throughout, INCLUDING the title's verb. Normalized on the video title's authority.
- ⚠ **VERIFY before seeding (all vendor-stated, caption-sourced):** Yutori's 97%/Online-Mind2Web + $0.80-vs-$2.30; Arize CLI-vs-MCP study (83% parity, 7-vs-71 turns, 75× cheaper); D'Oro's OSWorld/MobileWorld names + DG-World 15apps/387/3.2M + 20%-vs-95% coverage + $12/1M-task cost; Bright Data scale (50B pages/day, "70% of AI labs"); Oxylabs 550ms + 400M→6B req; Amazon AgentCore index + Microsoft web-BYOQ launch dates.
- ⚠ "by Lemon" (Gallon) → almost certainly **GeeTest** (jigsaw-slider CAPTCHA), medium confidence. "OffMD" (Klein) → **auth.md** (WorkOS), medium confidence. "MobileWorld" (D'Oro) → possibly **AndroidWorld**.
- `exp-corey-gallon` and `exp-shlok-khemani` (b19) are the corpus's two experts with NO company edge (both genuinely independent).
- `el-yutori-navigator` naming: "Navigator N1.5" per captions — verify the model name/version.

## Coinage record — 2026-08-16 (four patterns + FDE reframe)

User directive: "add" pat-agent-economy, pat-ai-native-org,
pat-durable-execution, pat-benchmark-trust-crisis; reframe pat-fde-turn as
the *rise* of FDE. Corpus now at **16 coined patterns**. Edges loaded via
`seed-work/frag-21-coinage.jsonl` (4 Pattern nodes + 38 FormsPattern/
ContradictsPattern edges); b16-20 element/signal edges that previously
dangled against these candidates now also resolve.

### `pat-durable-execution` (dynamic) — 6 support / 1 counter
Support: `sig-mcp-spec-mandates-task-durability` (davis-temporal),
`sig-knowledge-work-moves-to-nightly-cloud` (holmes-warp),
`sig-background-agents-absorb-ops-long-tail` (smith-resolve),
`sig-inngest-durable-execution-vendor` (farrelly-inngest),
`sig-durable-runtime-category-emerging` (tahir-zenml),
`sig-reset-over-compact` (lee-krafton — rehomed from `pat-harness-over-model`).
Counter: `sig-mcp-tasks-zero-client-adoption` (davis-temporal — the
convention/adoption-gap counter).

### `pat-benchmark-trust-crisis` (challenge) — 9 support / 2 counter
Support: `sig-benchmarks-saturate-while-deployment-stalls` (almeida),
`sig-benchmarks-cannot-be-chained` (asawa), `sig-replay-agent-beats-frontier-models`
+ `sig-passk-is-a-gameable-metric` (doro — the formal proof), `sig-long-horizon-is-a-scalar`
(garg), `sig-metr-50pct-headline-inflates-capability` (linkov), `sig-rl-environments-decoupled-from-reality`
(malde), `sig-reward-hacking-arms-race` (desai — rehomed from `pat-verification-gap`),
`sig-simulation-awareness-breaks-evals` (petersson — rehomed from `pat-verification-gap`).
Counter: `sig-private-task-reruns-over-leaderboards` (linkov), `sig-benchmark-on-your-own-codebase`
(singh) — private/real-codebase re-run suites as the trustworthy antidote.

### `pat-ai-native-org` (dynamic) — 11 support / 0 counter
Support: `sig-velocity-sickness-pathologies` (dailey), `sig-adoption-arc-fear-then-slop`
(khandelwal), `sig-background-automation-is-the-ballgame` + `sig-multiplayer-surface-for-realtime-dev`
(gazit), `sig-notion-software-factory` (sachs), `sig-agent-sessions-as-team-surface` (singh-superconductor),
`sig-block-autonomy-then-layoffs` (jones — the layoffs/dark-side data point),
`sig-boundary-ships-without-code-review` + `sig-writing-is-the-review-surface`
(gupta-boundary — rehomed from `pat-value-of-judgement`), `sig-automattic-radical-speed-month`
+ `sig-designers-ship-ios-chat-6-days` (grbic).

### `pat-agent-economy` (dynamic) — 8 support / 1 counter
Support: `sig-web-agentified-by-browser-layer` (batra), `sig-web-ui-as-permissionless-api`
(gallon), `sig-web-must-become-agent-legible` (klein), `sig-agent-walled-gardens-aol-era`
(raskar), `sig-agent-mediated-consumers-break-human-ground-truth` (anand),
`sig-andon-real-world-deployments` + `sig-vending-arena-emergent-misconduct` +
`sig-agents-no-longterm-investment` (petersson — the Vending-Bench cluster, the
ledger's strongest data).
Counter: `sig-long-tail-will-never-publish-apis` (batra — the protocol-optimist
counter to the machine-web leg).

### ⚑ Completeness tail still owed (per-pattern sweeps)
Coined with the clearly-held and explicitly-named-rehome signals above; the
registry ledgers reference further scattered older-batch evidence NOT yet
attached (same deferral shape as `pat-agent-memory-layer`'s b9/b10 tail):
- **pat-ai-native-org:** the batch-4/5/6 echoes still on `pat-saaspocalypse`/`pat-harness-over-model` — Tan (3 saaspocalypse links, tan-yc file review note 1), Doshi, Lee-Chan, An/Hoe, Noring, Browne, Yaron survey. Each needs a rehome/dual-edge judgement.
- **pat-durable-execution:** the b3/b4/b5 vendor cluster (ZenML/Kitaru original, KRAFTON `sig-multi-machine-five-failures`, Shrabony, OpenAI keynote, Paperclip, Resonate/Synadia, Chronicle, Bhargava Agency, FlyersSoft) — several still parked on `pat-harness-over-model`.
- **pat-benchmark-trust-crisis:** the b3/b5/b6/b9/b12/b13 legs (Han reward-hacking, Vidal, Robinson, Kumar, Campos, Datacurve contamination, Cai economic motive, `sig-weak-verifier-attack-surface`) — many still on `pat-verification-gap`.
- **pat-agent-economy:** Povilionis receipts (b2), Local-AI panel (b6), `sig-real-economy-runs-on-php-and-clicks` (klein, drop-option from `pat-saaspocalypse`).
Recommend a dedicated per-signal rehome pass rather than a blind sweep, since
each is a form/contradict + rehome-from-which-pattern judgement.

### Consequences for remaining ledgers
- Still uncoined: `pat-environments-economy`, `pat-liquid-software` (reframed below), `pat-compute-liquidity`, `pat-fde-rise` (reframed, uncoined), `pat-provider-blind-ai`/`pat-html-native-medium` (retired).

### ⚑ REFRAME 2026-08-16 — `pat-adaptive-*` → single `pat-liquid-software`
User rejected "adaptive" as too weak (it implies a fixed system adjusting
within bounds). Chosen framing: **Dissolving / Liquid**. **Pair-vs-merge
resolved (user, 2026-08-16): keep ONE pattern, `pat-liquid-software`; drop
the separate `pat-liquid-harness`.** The former `pat-adaptive-software` and
`pat-adaptive-harness` both consolidate here — a harness is a build artifact
too, so it's a facet of the same thesis, not its own pattern.
- `pat-adaptive-software` **and** `pat-adaptive-harness` → **`pat-liquid-software`** — "Liquid Software"

Thesis (sharpened): **the frozen build artifact dissolves** — software (and
its harness) is materialized per-use/per-context at runtime instead of being
shipped as a fixed thing. One stem + per-user live divergences (ten Teije
"the pipeline is dead"); harness as runtime output not input (Chandegra);
spec-is-the-product / bespoke-on-demand (Tornow); optimizer rewrites the
harness from production signals (RELAI); agents mutating agents (Mutagent).

**Still uncoined** (no "add" given). ~5 data points across b7 (ten Teije,
Chandegra) + b8 (Tornow, RELAI, Mutagent). Historical registry/extraction
mentions of `pat-adaptive-software` / `pat-adaptive-harness` predate this
reframe and stand as record; this note is the authority. If coined, the
harness-side evidence attaches to `pat-liquid-software` as a facet.
- `pat-agent-economy` breadth: watch whether the machine-web signals (Batra/Klein/Gallon) and the agent-commerce signals (Petersson/Povilionis/Raskar) stay coherent under one pattern or want splitting.
