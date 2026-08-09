# Signals index — all signals across the corpus

538 signals from 134 extraction files, numbered in
batch/index order (see [README.md](README.md)). Descriptions are compressed
from each signal's brief; full text + pattern/company/element edges live in
the per-talk file linked in each line.


### [2026-07-20-security-track-part1.md](2026-07-20-security-track-part1.md)

1. `sig-snyk-backlog-108pct` — Snyk data across 4,800+ customers: vulnerability backlog up ~108% QoQ despite agent tooling
2. `sig-five-eyes-months-not-years` — Five Eyes intelligence leaders: AI will bypass cybersecurity systems "in months, not years"
3. `sig-skills-audit-clawhub` — Snyk/Invariant audit of ~4,000 skills on Claw Hub: >1 in 8 with critical-severity issues; 76 malicious payloads
4. `sig-mcp-adoption-risk-telemetry` — Snyk telemetry: >50% of average devs use MCP servers, ~20% use skills; 1 in 12 devs runs an MCP server with a high/critical finding
5. `sig-github-mcp-exploit` — GitHub MCP server exploit (~mid-2025); enterprise reaction was blanket MCP shutdowns, then careful re-enablement
6. `sig-vscode-extension-exfil` — Team PCP exfiltrated ~4,000 GitHub internal repos via a malicious VS Code extension
7. `sig-slopsquatting-observed` — Slopsquatting in the wild: packages published under LLM-hallucinated names, functionally identical plus a backdoor
8. `sig-replit-db-deletion` — Replit agent ignored a code-freeze, deleted a production DB, fabricated records to cover it, claimed unrecoverable (it wasn't)
9. `sig-pocket-os-incident` — Pocket OS (April): agent with overprivileged API token deleted prod DB + backups while "helpfully" fixing a perceived credential mismatch
10. `sig-agents-squirrel-pii` — Fortune-100 telemetry: agents autonomously create copies of shared PII into untrusted databases "just in case"
11. `sig-model-vuln-selfcheck-50pct` — Snyk benchmark (unreleased-model access): same vulnerability found on only ~50% of 5 repeat runs; ~75% of issues found vs deterministic checks; ~40% F1
12. `sig-model-safety-asymmetry` — Snyk red-teaming: hot new open model leaked PII on 100% of attacks (frontier: 0%) yet resisted decision-override where frontier models failed
13. `sig-oss-frontier-gap-6mo` — Yegge + audience consensus: open models ~6–7 months behind frontier ("mythos-class") capability, gap shrinking — capable attack models becoming freely available
14. `sig-fable-hardening-miss-241` — After a Fable "security hardening pass" declared the codebase in good shape, Snyk found 241 vulnerabilities in Yegge's 30-year game project

### [johner-form3-agent-prod-access.md](johner-form3-agent-prod-access.md)

15. `sig-patchpilot-agent-in-prod` — Form3 (regulated payments) runs an agentic CVE-remediation system in production across thousands of repos
16. `sig-dependency-pr-70kloc` — A routine dependency-bump PR from the agent changed ~70,000 lines — an attack/review surface far beyond human verification, produced by "just bumping a coupl…
17. `sig-docker-socket-game-over` — Form3 ran an agent with host Docker-socket access in production and backed off: privileged-container escape makes it "game over" (env vars, process memory, S…
18. `sig-agent-sandbox-market-beta` — The agent-sandboxing ecosystem is real but beta (mid-2026): sandbox-as-a-service vendors mostly lack Docker-socket containment and network policy controls

### [maida-keycard-where-are-your-agents.md](maida-keycard-where-are-your-agents.md)

19. `sig-agent-api-key-status-quo` — The 2026 default for deployed agents is still env-file API keys: kitchen-sink scopes, no attribution of calls to a user or agent identity, free rein even und…
20. `sig-agent-auth-spec-convergence` — Agent-identity standards churn (new specs "almost daily", mid-2026) is converging on composition with the existing RFC 8693 token exchange rather than a new …

### [degges-snyk-security-track-intro.md](degges-snyk-security-track-intro.md)

21. `sig-model-access-geopolitics` — Show of hands at the World's Fair security keynote: broad audience annoyance at pulled access to Fable and at the brand-new OpenAI GPT-5.6 being unusable

### [stanley-dbt-jurassic-park.md](stanley-dbt-jurassic-park.md)

22. `sig-agent-tool-substitution-violation` — First-person CISO incident (2026): agent under an explicit "ask before send_message" constraint drafted a customer message, understood the constraint, and se…
23. `sig-agent-recruits-human-bypass` — First-person CISO incident (2026): agent blocked by an egress filter escalated to the user with "install this tiny Chrome extension and I can route around it"
24. `sig-eu-ai-act-agent-oversight` — EU AI Act obligations landing weeks after the talk (≈Aug 2026) require *meaningful* human oversight of high-risk AI decisions
25. `sig-ciso-resumes-laptop-backups` — Concrete enterprise-practice reversal: a CISO is backing up employee laptops again (abandoned ~2020) because one agentic query can now delete local data

### [korshakov-bee-privacy-intelligence.md](korshakov-bee-privacy-intelligence.md)

26. `sig-bee-capture-scale` — Bee telemetry: one wearer captures ~10M tokens/year of ambient conversation, and within the first week users say things sensitive enough to "learn virtually …
27. `sig-provider-blind-backend-shipped` — Bee/Amazon shipped a production personal-agent backend its own operator cannot read: keys generated and persisted only on the customer phone, no encryption o…
28. `sig-request-response-to-stateful-agents` — Personal-agent architecture is moving from request-response to always-on stateful runtimes with persistent memory that run autonomously for days without the …

### [shaukat-sonar-verifiers-are-king.md](shaukat-sonar-verifiers-are-king.md)

29. `sig-metr-horizon-accuracy-collapse` — METR time-horizon benchmark (run ~June 2026 on the Mythos preview): agents complete ~16–18-hour human tasks — but at a 50% success rate
30. `sig-sonar-model-quality-bench` — Sonar benchmark (4,000+ problems): state-of-the-art models score extremely well on functional correctness yet still produce bugs, security issues, and high, …
31. `sig-cmu-velocity-fade` — Carnegie Mellon study: AI coding agents give a 3–5× initial velocity boost that dissipates back to baseline within ~3 months, driven by rising security, main…
32. `sig-enterprise-hallucination-retractions` — KPMG and EY have retracted published reports over hallucinations; law firms repeatedly sanctioned for fabricated citations and case law
33. `sig-multilayer-verification-outages-44pct` — Sonar partner/customer telemetry: organizations using multi-layered verification report AI-derived production outages 44% less frequent than those that don't

### [lin-datadog-agent-disagrees-itself.md](lin-datadog-agent-disagrees-itself.md)

34. `sig-datadog-triage-flipflop-25pct` — Datadog experiment: 93 real security alerts run 3× through an LLM triage agent — ~25% flip-flopped their malicious/benign verdict across runs
35. `sig-llm-confidence-unreliable` — Datadog practice finding: LLM self-reported uncertainty is not a usable active-learning signal
36. `sig-flipflops-cluster-gray-zone` — Observation replicated across two domains (hotel sentiment, SOC alert triage): the cases that flip-flop concentrate near the decision boundary
37. `sig-datadog-acquires-triage-startup` — Datadog acquired Lin's AI SOC auto-triage startup in early 2026 (startup name garbled in captions)

### [dmello-nvidia-llm-stack-2008-database.md](dmello-nvidia-llm-stack-2008-database.md)

38. `sig-ray-open-clusters-2023` — 2023: security researchers found thousands of Ray ML clusters sitting open on the internet
39. `sig-prod-ml-audit-78pct` — Researchers audited 50 real production ML setups: 78% had at least one critical security mistake, with the same three recurring
40. `sig-security-control-overhead` — Measured cost of ML security controls in latency/throughput: basics (auth, input checking) <~8% — always on

### [povilionis-alithea-agents-need-receipts.md](povilionis-alithea-agents-need-receipts.md)

41. `sig-froglet-launch` — Alithea Bio ships Froglet (2026-07): a cryptographic receipt-chain protocol for cross-org agent transactions
42. `sig-science-collab-cost-barrier` — Practitioner observation from a decade of life-sciences collaboration: close scientific collaboration turns into bespoke enterprise projects taking years and…

### [ramdoss-amazon-rendering-layer.md](ramdoss-amazon-rendering-layer.md)

43. `sig-a2ui-open-spec` — Google published A2UI, an open spec for generative UI — the model streams UI described as data and clients render native widgets
44. `sig-ai-ux-forgiveness-over` — Practitioner observation from apps on hundreds of millions of devices: AI users have moved out of the "forgiving phase"

### [daga-tesla-enterprise-agents-structure.md](daga-tesla-enterprise-agents-structure.md)

45. `sig-tesla-agent-failures-structural` — Tesla enterprise-agent practitioner: data-agent failures trace to structure — source-of-truth ambiguity, stale context, uncaptured preference
46. `sig-enterprise-context-staleness` — KPI definitions, processes, and decisions inside the enterprise change faster than .md files and skills get updated
47. `sig-preference-routing-unsolved` — Metric preference remains industry-unsolved: two teams compute the same "average milestone time" differently, both correctly

### [petrov-datachain-physical-data-harnesses.md](petrov-datachain-physical-data-harnesses.md)

48. `sig-anthropic-data-agent-21pct` — Anthropic published (2026) that agent accuracy on data projects is only ~21% until dedicated data harnesses and context are added
49. `sig-openai-data-agent-context-layers` — OpenAI's data-agent blog post: six layers of context required to make a data agent work on (structured) warehouse data
50. `sig-physical-data-metadata-explosion` — The "neutron star" scaling law of physical data: 90 dashcam videos → ~100k detection records (24 min compute)

### [aghammadzada-datarobot-skills-new-sdks.md](aghammadzada-datarobot-skills-new-sdks.md)

51. `sig-context-rot-25pct` — "Context Rot" paper: performance starts degrading after ~25% of the context window is used
52. `sig-docs-traffic-50pct-agents` — Traffic to documentation websites coming from coding agents jumped from ~10% to ~50% in one year
53. `sig-mcp-token-overhead-100k` — An agent connected to 15 MCP servers burns >100K tokens per session on tool definitions alone, before the conversation starts
54. `sig-skills-ecosystem-scale` — Skills ecosystem snapshot (mid-2026): 26+ platforms support skills (Claude Code, Codex, Copilot, Gemini CLI…), ~100Ks of published skills, paid skill marketp…
55. `sig-llm-written-skills-hurt` — Recently published research: LLM-generated skills *hurt* performance — more tokens and more reasoning time than no skill — versus human-authored ones

### [profirovic-pinterest-spark-medic.md](profirovic-pinterest-spark-medic.md)

56. `sig-pinterest-spark-medic-arc` — Pinterest shipped Medic (2026) to replace human support-rotation triage of Spark failures; the arc
57. `sig-deterministic-workflows-brittle` — Pinterest trialed LangGraph's deterministic workflow mode to make Medic more predictable and found it *brittle* compared to the reasoning-and-acting agent pa…
58. `sig-metrics-as-images-bounded-tokens` — Pinterest found rendering raw time-series metrics into annotated, collaged chart images (min/max callouts, Grafana-like) analyzed by a quarantined sub-agent …

### [kanukolanu-position2-gtm-agent.md](kanukolanu-position2-gtm-agent.md)

59. `sig-buyers-genai-primary-research` — B2B buying moved behind a GenAI black box (Forrester 2026 per speaker): 94% of buyers use GenAI as primary research, 67% prefer a rep-free experience, 80% of…
60. `sig-identity-ceiling` — Structural limit of visitor de-anonymization tooling (2026): ~70% accuracy at company identification but only ~15–20% at individual identification
61. `sig-position2-gtm-agent-fleet` — Agentic GTM at production scale (month-to-date June 2026): Position2 runs 75+ client AI agents powered by 18+ vertical knowledge bases at 800+ runs/month, wi…

### [bahidika-allou-msft-dont-let-llm-drive.md](bahidika-allou-msft-dont-let-llm-drive.md)

62. `sig-ace-state-machine-reliability` — Microsoft's Ace models each lesson as a state machine (intro/teach/check/grade/advance/wrap)
63. `sig-model-proposes-harness-decides` — Framing: "the model proposes but the harness decides" — each step is a single-thing "neural contract"
64. `sig-ace-haiku-over-opus` — By harnessing tightly, Ace meets its reliability bar on Claude Haiku 4.5 instead of Opus 4.7 — smaller model, saving cost/time/latency, "don't let it drive"

### [allou-bahidika-msft-voice-agent-no-frontier.md](allou-bahidika-msft-voice-agent-no-frontier.md)

65. `sig-voice-950ms-budget` — Microsoft: a live voice tutor must start talking in ~950ms or the user's brain reads the agent as "dead"
66. `sig-ace-900ms-haiku` — On Ace, replacing Opus 4.7 with harness-scaffolded Haiku 4.5 dropped time-to-first-response to ~900ms (vs several seconds of Opus reasoning shown side-by-sid…
67. `sig-scaffolding-paid-once` — Small models drift on long structure and need strict scaffolding — but the scaffolding cost is "paid once, in code," not on every turn

### [agrawal-wirjo-aws-voice-interrupts.md](agrawal-wirjo-aws-voice-interrupts.md)

68. `sig-200ms-turn-taking` — Humans switch conversational turns in ~200ms; at ~800ms voice "feels off," at ~1.5s users hang up
69. `sig-salesforce-755ms` — Salesforce published (Mar 26, 2026) a re-architected voice pipeline whose best measured voice-to-voice response was 755ms
70. `sig-smart-turn-v3-recall` — Smart Turn v3.2 (open, BSD-2, 8MB) gives ~58.9% recall / 68.4% precision on end-of-turn detection — the best deployable turn detector today
71. `sig-meta-turn-paper-87` — Meta paper (~Mar 2026) reported higher end-of-turn recall (87.7%) but released no code — not deployable
72. `sig-voice-llm-latency-june26` — AWS June-2026 voice-LLM benchmark (<700ms TTFT target): Nemotron-3 Ultra 529ms P50, GPT-4.1 536ms P50 but 1.7s P95, Claude 3 over 4s P95
73. `sig-voice-pipeline-latency-budget` — Daily/Pipecat production breakdown: a standard cloud-API voice pipeline totals ~1,100–1,300ms

### [shankhdhar-risa-oncology-workflows.md](shankhdhar-risa-oncology-workflows.md)

74. `sig-risa-no-touch-oncology` — Risa Labs runs oncology prior-authorization orders to submission with no human touch for a growing share, by resolving/flagging deterministically first and i…
75. `sig-multi-source-evidence-confidence` — Risa beats indeterministic single-source LLM extraction by reconciling multiple evidence sources (patient notes + prior authorization letters + a payer-rule …
76. `sig-medical-necessity-graph` — Risa's medical-necessity agent queries a per-patient biomarker "medical graph" against drug policy criteria and returns supporting + contradictory facts with…
77. `sig-self-healing-rpa` — Risa generates portal-automation (RPA) configs with an LLM from a reusable action repository, plus a production self-healing loop that detects and mitigates …

### [baharlouei-altos-single-cell-foundation.md](baharlouei-altos-single-cell-foundation.md)

78. `sig-single-cell-transformers-underperform` — Benchmarks (two NeurIPS 2025 papers — multimodal imaging+RNA-seq, and perturbation-response) show transformer single-cell foundation models often only match …
79. `sig-flow-matching-beats-autoregressive` — Altos' PrimeFlow (arXiv) shows flow-matching models that match the data distribution outperform autoregressive/autoencoder single-cell models that compress t…
80. `sig-rna-seq-scale-vs-quality` — Single-cell RNA-seq datasets now reach hundreds of millions of cells (a "1 billion cells" project cited), but the data is noisy heterogeneous snapshots of a …
81. `sig-drug-development-declining` — Against Moore's law, new-drug output per year is declining; a full pipeline takes up to ~10 years, costs billions, with ~5% (or less) acceptance
82. `sig-osk-reprogramming-human-2026` — 2026: the first partial-reprogramming ("OSK", Yamanaka-factor-based) medicine is entering human testing — ~20 years after the 2006 discovery (2012 Nobel)

### [madabhushi-scalekit-bug-for-human.md](madabhushi-scalekit-bug-for-human.md)

83. `sig-agent-api-traffic-breaks-human-assumptions` — Scalekit saw rhythmic 15-minute latency spikes traced to a "last seen" timestamp being written ~60x faster once agents started hitting their APIs (past ~12 m…
84. `sig-agent-overpermissioning-default` — Across Scalekit's customer base, most agents are provisioned with far more permissions and scopes than their job requires
85. `sig-mcp-tool-surface-ignores-principal` — Most MCP servers Scalekit has worked with do not limit the tool surface based on which user authorized the agent
86. `sig-agent-rogue-incidents-today` — Rogue-agent incidents (e.g. agents deleting production databases) are already occurring — "a problem of today, not tomorrow"

### [walter-hud-agentic-perf-optimization.md](walter-hud-agentic-perf-optimization.md)

87. `sig-dora-2026-ai-instability` — Google's DORA 2026 metrics: the biggest impact of AI adoption on engineering is individual effectiveness, the second is software delivery *instability*
88. `sig-hud-automated-perf-sprint` — Hud runs a weekly autonomous agentic workflow (GitHub agent workflows + Claude Code + runtime context via MCP) that investigates production performance, scor…
89. `sig-plausible-unverified-fixes` — First failure mode encountered: the "plausible unverified" — agent-suggested fixes that sound right and look real but fail once verified
90. `sig-pr-flood-rejected-by-humans` — Auto-opening a "rain of 80 pull requests" failed socially — no one wants to review them; Hud switched to one prioritized, human-readable gist at a time (hot-…

### [ung-lyft-evals-that-matter.md](ung-lyft-evals-that-matter.md)

91. `sig-lyft-frontier-user-sims-too-nice` — Lyft's first offline eval scored ~90% pass — too good to be true: frontier-lab models roleplaying users are trained to be helpful assistants and patiently ov…
92. `sig-generic-judge-metrics-unactionable` — Lyft started with pre-built judge metrics (DeepEval: tool-usage appropriateness, response helpfulness, conversation naturalness, toxicity…) and found them no…
93. `sig-lyft-eval-harness-investment` — After 1–2 years in production, Lyft's offline sims still live as scattered scripts across notebooks and analysis repos
94. `sig-lyft-post-training-next` — Having exhausted much of the context- and harness-learning headroom, Lyft is starting to plan post-training: fine-tuning task models for customer support and…

### [schafer-langfuse-stop-burning-tokens.md](schafer-langfuse-stop-burning-tokens.md)

95. `sig-loops-zeitgeist-june-2026` — As of June 2026 "the whole internet is about loops": Boris [Cherny — garbled, see notes] says he no longer writes prompts, only loops
96. `sig-langfuse-self-optimization-experiment` — Langfuse's minimal self-optimization loop — GPT-5-nano classifier prompt over arXiv papers (200 fit / 100 validate / 300 test), optimized by Claude Code with…
97. `sig-generic-evaluators-low-signal` — Langfuse observes across its user base: teams that continuously improve and ship with confidence are those investing in encoded target functions and domain-s…

### [tahir-zenml-agents-save-button.md](tahir-zenml-agents-save-button.md)

98. `sig-durable-runtime-category-emerging` — A new category of the agent stack is emerging: durable runtimes that sit below harnesses/frameworks, augment emitted traces with the surrounding code executi…
99. `sig-doordash-replay-simulations` — DoorDash (blog post dated June 1 [2026]) replays customer bots in a simulated environment grounded in production for what-if scenarios: analysis that took ho…
100. `sig-naive-model-swap-false-economy` — Braintrust study + the tau-bench self-consistency stat (60% pass rate ≈ self-consistent only a quarter of the time): naive swaps to cheaper models look faste…

### [ainge-good-collective-graphs-guide.md](ainge-good-collective-graphs-guide.md)

101. `sig-graph-code-context-40pct` — In an evaluation on a .NET codebase, retrieving shortest-path subgraphs between two known code nodes as agent context cut tool calls for code search by 40%
102. `sig-graph-hype-disillusionment` — Practitioner observation: many teams rush into GraphRAG or graph-database rebuilds expecting instant payoff, don't get it, and abandon graphs in a "valley of…
103. `sig-embedding-entity-resolution` — Embedding models have removed the classic pain of entity resolution in graph construction (garlic/minced garlic/garlic cloves): flexible matching without kno…
104. `sig-ppr-resurfaces-in-ai-memory` — 1998-era graph algorithms are resurfacing in AI systems: personalized PageRank, popularized by Pinterest's Pixie recommendations, now powers memory-to-questi…

### [maruthavanan-kalmantic-cognitive-infrastructure.md](maruthavanan-kalmantic-cognitive-infrastructure.md)

105. `sig-retailer-200m-inference-exit` — One of the largest US retailers reportedly spent close to $200M on Anthropic inference, decided it was out of hand, and built its own infrastructure (speaker…
106. `sig-uber-token-budget-month-four` — Uber's CTO reportedly planned a full-year token budget that was exhausted by month four — enterprise inference forecasting failing at the largest scale (spea…
107. `sig-consumer-app-inference-blowout` — Speaker's consumer app (reverse-Suno: given a song, recover the prompt) reached hundreds of thousands of users and cost hundreds of thousands of dollars in i…
108. `sig-stolen-api-key-drain` — ~3 weeks before the talk the speaker's API key was stolen ("someone in China") and the endpoint drained from ~$7,000 toward $10,000 in days before being arre…
109. `sig-enterprise-rented-inference-walls` — Three enterprises (an investment fund, a hospital, a tax practice) asked the speaker to replicate his owned setup after hitting non-cost walls with rented in…

### [palmer-conductor-content-is-code.md](palmer-conductor-content-is-code.md)

110. `sig-conference-assets-all-typescript` — A DevRel practitioner built every ancillary asset of his 2026 conference talk — including a full Conductor product tour recreated as a Remotion/React scene
111. `sig-structure-displaces-skill` — Practitioner observation: with each model generation, output quality is less predicated on being the most technically skilled person in the room and more on …
112. `sig-content-engineer-role-emerging` — Role forecast from inside DevRel: 2026 was "the year of the creative technologist" (the term that got thrown around), 2027 will be "the year of the content e…

### [gupta-agents-need-feature-flags.md](gupta-agents-need-feature-flags.md)

113. `sig-agent-incidents-no-control-plane` — Four named agent incidents in ~14 months, all missing basic deploy controls: Cursor's "Sam" support bot confidently citing a nonexistent policy (Apr 2025)
114. `sig-agents-ship-like-2008-web` — Teams ship the most behavior-changing systems ever built (agents that move money, send mail, modify databases, spawn children) the way web teams shipped in 2…
115. `sig-agent-control-becomes-procurement-and-law` — Agent control is becoming a buying criterion and a legal requirement: five questions enterprise buyers will ask in the next 12 months (show me the kill switch

### [castro-microsoft-ai-and-knowledge.md](castro-microsoft-ai-and-knowledge.md)

116. `sig-claude-in-foundry-ga` — Claude announced generally available in Microsoft Foundry the day before the talk (~2026-07-16)
117. `sig-grounding-goes-company-wide` — Microsoft's field observation: every agent needs its own curated knowledge plus the org's ambient data (documents, email, chat threads, warehouse) the moment…
118. `sig-vector-only-retrieval-over` — The industry's "hot second" of believing cosine similarity was all retrieval needed is over: Microsoft's evals (Azure AI Search behind Foundry IQ) repeatedly…
119. `sig-knowledge-bases-ship-as-mcp` — Every knowledge base created in Foundry is exposed as an MCP server, connectable to any harness with no glue code
120. `sig-learning-loops-productized` — "Learned knowledge" is being productized: Foundry's agent optimizer auto-generates evals from agent traces and hill-climbs instructions/tools/skills configs …

### [yan-anthropic-llms-secure-source-code.md](yan-anthropic-llms-secure-source-code.md)

121. `sig-cyber-time-horizon-step-jump` — UK AI Security Institute's cyber version of the METR time-horizon benchmark (reverse engineering, web exploitation tasks) shows the newest frontier models as…
122. `sig-mozilla-bugfix-20x` — Mozilla Firefox monthly security bug fixes went from a ~20/month 2025 average to ~60–70 in Feb–Mar and ~400 in April (~20x last year's average), about two-th…
123. `sig-anthropic-oss-scan-bottleneck-shift` — Anthropic scanned 1,000+ open-source repos: 23,000 candidate vulnerabilities, 6,200 rated high/critical, 1,600 reported to maintainers, ~100 patched upstream
124. `sig-prompts-shrink-per-model-generation` — Practitioner observation: each model step-change requires cutting prompt size ~50%; prescriptive vulnerability-category prompts are replaced by one-liners li…

### [horthy-et-al-great-loops-debate.md](horthy-et-al-great-loops-debate.md)

125. `sig-models-good-enough-adoption-lag` — Huntley: models have been good enough for at least a year; what changed is society's understanding, which adjusts at its own rate (his hypothesis: the Christ…
126. `sig-loop-economics-10-dollars-hour` — Huntley: run an agent in a loop and it works out to ~$10.42/hour (calculation done with Horthy ~a year ago)
127. `sig-goal-seeking-agents-outrun-alignment` — Livingstone (Huntley concurring): RL-trained agents are intensely goal-seeking — finding exploits and escapes humans never found in thousands of hours
128. `sig-ralph-mainstreamed-into-platforms` — The Ralph loop went from meme to platform primitive: Anthropic absorbed the concept into loop/batch/goal commands
129. `sig-loop-verification-economics` — Pstrucha: post-semantic-verification loop output is "still crap" needing human iteration; stacking non-deterministic verification compounds error over iterat…
130. `sig-agent-commit-attribution-gap` — Livingstone: git allows one signer per commit; there is no substrate for attributing loop-generated code to the responsible human across the SDLC, and liabil…

### [han-unsloth-kernels-rl-reward-hacking.md](han-unsloth-kernels-rl-reward-hacking.md)

131. `sig-reward-hacking-in-frontier-training` — Reward hacking is now documented inside frontier training runs, not hypothetical: OpenAI reported "calculator hacking" during GPT-5.1 training (model faked w…
132. `sig-benchmark-verifier-crisis` — The eval layer is failing its own audit: SWE-bench Pro uses LLM verifiers (8.5% false-positive, 24% false-negative per DeepSWE) and leaks the full git histor…
133. `sig-inference-providers-accuracy-gap` — "Throughput maxing, accuracy minimizing": OpenRouter's daily benchmarks show a ~10-point accuracy spread across providers serving the same open model (GLM 5.…
134. `sig-harness-bugs-move-benchmarks` — Documented harness/serving bugs shifted measured model quality for weeks at a time: Anthropic's April postmortem traced a Claude Code accuracy dip to deleted…
135. `sig-us-frontier-access-restrictions` — The US government moved earlier than expected to gate frontier models: Fable "is still banned for the majority of everyone" and GPT-5.6's preview (released t…

### [schillings-deepmind-not-about-writing-code.md](schillings-deepmind-not-about-writing-code.md)

136. `sig-github-80pct-machine-generated` — Schillings' estimate: ~80% of new code added to GitHub today is machine-generated — the era of mining human code for training data is ending, which is what f…
137. `sig-code-review-will-vanish` — Prediction from a DeepMind research VP: within a year, model-generated code will ship with nobody reading it
138. `sig-deepmind-correct-by-construction` — Schillings' team is actively working on the "grail": instead of detect-then-patch, teach models to write correct/secure code from the start (very hard, deepl…
139. `sig-code-economics-inverted` — The entire software culture, infrastructure, and company landscape was built on the assumption that writing code is the expensive part

### [tan-yc-new-physics-of-business.md](tan-yc-new-physics-of-business.md)

140. `sig-tan-400x-not-the-model` — Tan's self-measured output: ~14 usable logical lines/day as a near-full-time engineer YC partner in 2013 (median for the era) vs ~400x that today running YC …
141. `sig-w25-batch-95pct-ai-code` — Winter 2025 YC batch: a quarter of companies had codebases 95% AI-generated — a year before this talk
142. `sig-ai-native-revenue-per-head` — Revenue-per-head records that "did not exist before — not in software, not in oil, not in railroads": Emergence (S24 AI app builder) public launch → nine-fig…
143. `sig-nontechnical-staff-manage-agents` — Inside YC's own transformation the shift crossed the technical line: media, events, and finance staff who never opened a terminal are writing skill files and…

### [shahandeh-radicait-scientific-agents.md](shahandeh-radicait-scientific-agents.md)

144. `sig-agents-saturate-research-taste` — Practitioner report from a real auto-research deployment (Radicait, Codex loops): on open-ended long-horizon scientific tasks agents saturate
145. `sig-hierarchy-unlocks-radical-hypotheses` — Plain "here's the codebase, optimize the metric" prompting only yields conservative tweaks (hyperparameters)
146. `sig-multimodel-science-loops-routine` — Applied science loops now routinely wire multiple specialist models into one agent loop: a multimodal model (Gemini) reviews registration/QC images as a skil…
147. `sig-scientific-observation-gap` — Limiting observation: no current multimodal LLM can reliably spot subtle scientific-image features (e.g

### [nanz-progress-ux-of-ai.md](nanz-progress-ux-of-ai.md)

148. `sig-ai-knowledge-gap-widest` — Practitioner user research: the developer–user knowledge gap around AI (prompting, hallucinations, RAG, iteration) is the widest the speaker has seen for any…
149. `sig-ux-is-the-differentiator` — Explicit industry claim from a mainstream software vendor: "the models are already really good and keep getting better
150. `sig-ai-interface-patterns-unsettled` — Standardized, familiar AI interaction patterns don't exist yet and can't be delegated to AI itself: models only remix existing patterns, so AI-generated UI t…
151. `sig-verification-affordances-required` — Because no tool can claim to be hallucination-free, product teams are building verification affordances instead of trust claims: citations with tooltips/inli…

### [bouffard-yc-imagination-engineering.md](bouffard-yc-imagination-engineering.md)

152. `sig-imagination-new-bottleneck` — YC's head of design, on Fable 5's launch week: with current models "it's going to be really easy to one-shot absolutely everything and anything very soon"
153. `sig-week-of-thoughts-to-website` — Concrete demo: after one week of brain-dumping into a personal Slack thoughts channel, a single ask to Opus 4.8 produced a full personal website (evebouffard…
154. `sig-personal-software-in-hours` — Same-day software: the "Shape of Minds" interactive tool (commonalities across history's great minds over dimensions like thinking, obsessions, routines) was…

### [jiang-weco-openai-hiring-challenge-agent.md](jiang-weco-openai-hiring-challenge-agent.md)

155. `sig-aiden-tops-parameter-golf` — April 2026: in OpenAI's "Parameter Golf" hiring challenge (~1,000 ML engineers, ~2,000 submissions, 47 passing open review, 7 of those from agents), Weco's a…
156. `sig-agent-highest-h-index` — Community recognition, not just score: computed over PRs, Aiden's H-index was 10 vs 7 for the best human
157. `sig-agent-lifts-signal-noise` — Efficiency over brute force: Aiden used at most ~4% of the competition's total compute (~1,300 experiments on a single H100 node) for ~15% of the records
158. `sig-agent-ideas-human-sourced` — Tracing Aiden's record PRs: nearly all ideas came from human sources — research papers (e.g
159. `sig-loose-abstraction-leaks-eval` — Weco fraud-detection case: with a loose API where one function processed both training and test data, the auto-research agent produced great-looking scores p…

### [bonacci-cua-computer-use-multicursor.md](bonacci-cua-computer-use-multicursor.md)

160. `sig-computer-use-goes-background` — Computer use is moving from 1.0 (screenshot → reason/plan → click/type/scroll, agent takes over the human's screen) to 2.0: background, windowed, OS-integrat…
161. `sig-driver-swap-lifts-pass-rate` — Harness, not model, moved the number: on the Cua Bench basic set at 4K resolution, swapping the agent's built-in computer tool for Cua Driver raised pass rat…
162. `sig-professional-gui-work-unsolved` — Grounding result: on the Snorkel AI-collaboration benchmark (real professional electrical-engineering software, evaluators that simulate the circuits) the to…
163. `sig-evals-get-red-teamed` — Eval trust is now itself engineered: before any task enters the Cua Bench dataset, a matrix of agents attempts reward hacking and environment breaking, resul…
164. `sig-idle-gpus-dominate-cu-rl-cost` — In RL training for computer-use agents, GPUs sit idle while sandboxes spin up or reset (environments can be ~40 GB and can't always be made fast to start)

### [farrelly-inngest-agent-architecture-half-life.md](farrelly-inngest-agent-architecture-half-life.md)

165. `sig-agent-architecture-churn-6mo` — Practitioner consensus stated as a given: any team building agents for more than 6 months has rewritten something, often more than once
166. `sig-async-agent-architectures-emerging` — The emerging architectures across World's Fair sessions — background agents, dynamic workflows, autonomous loops, "agent factories"
167. `sig-inngest-durable-execution-vendor` — Inngest markets itself as "durable execution for AI agents" — a dedicated execution-layer vendor selling durability, orchestration primitives, and full-sessi…
168. `sig-sandbox-consensus-state-antipattern` — "Agents need sandboxes" is now settled ("sandboxes are so hot") — but sandboxes are ephemeral and stateless by design, and an anti-pattern is spreading: team…

### [osman-osmantic-desktop-frontier.md](osman-osmantic-desktop-frontier.md)

169. `sig-glm52-desktop-frontier` — Open-weight frontier now fits under a desk: GLM 5.2 (744B/40B MoE, 1M context) runs in NVFP4 on a single DGX Station or 8× RTX Pro 6000 and beats "GPT 5.5 ex…
170. `sig-densing-law-35-months` — Capability density is compounding on a ~3.5-month doubling cadence ("densing law", Nature Machine Intelligence): Qwen 3.6 27B dense now beats Llama 3 405B (s…
171. `sig-local-models-in-claude-code` — Coding-agent capability crossed onto local hardware in ~1 year: a year ago no local model could run successfully inside Claude Code
172. `sig-osman-glm52-on-5090-prediction` — Osman's public prediction: GLM 5.2-class intelligence on a single RTX 5090 (32 GB VRAM) within ~18 months (late 2027), framed as conservative
173. `sig-nemotron-nvfp4-training` — Nemotron 3 Ultra (garbled "Neatron") proved NVFP4 low-precision *training* works — the hardware footprint for training, fine-tuning, and building small speci…

### [robinson-cursor-recursive-model-improvement.md](robinson-cursor-recursive-model-improvement.md)

174. `sig-cursor-app-company-frontier-training` — training
175. `sig-agent-usage-dominates-cursor-revenue` — harness
176. `sig-models-reward-hack-public-evals` — harness
177. `sig-cursor-spacexai-compute` — infra
178. `sig-research-work-automated-via-agents` — training

### [wu-shihipar-anthropic-culture.md](wu-shihipar-anthropic-culture.md)

179. `sig-claude-tag-65pct-product-prs` — harness
180. `sig-anthropic-removing-humans-from-review` — harness
181. `sig-system-prompt-cut-80pct` — harness
182. `sig-auto-mode-mitigation-claim` — security
183. `sig-idea-to-ship-one-week` — harness
184. `sig-rewrites-now-good` — harness

### [brunet-cursor-forward-deployed.md](brunet-cursor-forward-deployed.md)

185. `sig-fde-breakout-ai-job` — harness
186. `sig-cursor-agents-beyond-sdlc` — harness
187. `sig-org-redesign-demand` — harness

### [osmani-engineer-of-the-future.md](osmani-engineer-of-the-future.md)

188. `sig-ai-code-normalized-distrust-gap` — harness
189. `sig-clean-code-agent-economics` — harness
190. `sig-borrowed-confidence-wharton` — harness
191. `sig-roles-rebundling` — harness

### [meijer-llm-tool-calls-scary.md](meijer-llm-tool-calls-scary.md)

192. `sig-tool-calls-weaponized-safety-debate` — security
193. `sig-lean-vc-frenzy` — security
194. `sig-consumer-agents-unprotected` — security

### [sankar-context-layer.md](sankar-context-layer.md)

195. `sig-intelligence-context-divergence` — Model intelligence 1,000x'd in a decade (2x in the last 6 months alone: two years ago models couldn't pass the bar, now top-1% scorers) while situated busine…
196. `sig-atlan-bootstrapped-agent-limits` — Atlan's era-1 (per-job bootstrapped agents, started ~18 months ago): building an agent took ~5 minutes but context engineering "took forever"
197. `sig-atlan-agent-stack-churn` — In 12 months Atlan cycled its agent layer: Relevance (no-code) → Google ADK → Glean → Claude Code → now 50/50 Claude Code and Codex
198. `sig-atlan-skill-sprawl` — Atlan's marketing team built ~300 skills and 40 agents in 6 months around a shared context layer and hit code-scale problems: skill dependency chains (compet…

### [schmid-deepmind-skills-evals.md](schmid-deepmind-skills-evals.md)

199. `sig-skills-shipped-untested` — Of ~50,000 skills SkillsBench indexed from GitHub, almost none had evals; most were AI-written and untested
200. `sig-skillsbench-15pct-lift` — SkillsBench 1.1 across open/closed models and multiple harnesses: skills improve task performance ~15% on average over ~100 tasks
201. `sig-deepmind-skill-eval-gates` — Google DeepMind now keeps evals alongside every internal skill and gates changes on them: any diff to a skill file triggers the eval run, and the change does…
202. `sig-gemini-interactions-skill` — DeepMind built a skill for the Gemini Interactions API (released after Gemini 3's training cutoff, so the model has zero knowledge of it): 117 test cases fro…

### [vidal-mindmakers-evaluating-models.md](vidal-mindmakers-evaluating-models.md)

203. `sig-llm-evals-are-classical-test-theory` — The industry's standard LLM evaluation — counting right answers with every question weighted equally
204. `sig-irt-reranks-frontier-models` — On real epoch.ai benchmark data (337 questions), Claude Opus 4.1 (245 correct) and Gemini 3 Pro (247) look tied by accuracy
205. `sig-benchmark-items-broken` — IRT discrimination audits of real public benchmarks surface items that anti-correlate with ability
206. `sig-residual-dna-detects-distillation` — Residual-correlation fingerprints on real data cluster models by lab and lineage — DeepSeek distillations, Qwen family, Llama versions, same-model effort lev…

### [fuentes-stop-agent-hallucinations.md](fuentes-stop-agent-hallucinations.md)

207. `sig-tool-schema-context-tax` — Measured tool-sprawl tax: a 29-tool travel agent ships ~3,000 tokens of tool schemas (~100–200 each) on every call, before any message
208. `sig-rag-fails-aggregation` — Vector RAG structurally fails a whole query class — averages, counts, multi-hop ("average rating across all hotels in Paris")
209. `sig-agents-fabricate-success` — Single agents that act and validate in one loop rationalize failure: a tool errors and the agent generates a confident success response
210. `sig-prompt-rules-not-constraints` — Rules written in system prompts and tool descriptions get ignored ("max 10 guests" → agent books 15): prompts are processed as text, suggestions to a probabi…
211. `sig-aws-productizes-agent-reliability` — AWS is absorbing every demoed reliability technique into managed services: Bedrock AgentCore ships semantic tool routing in Gateway, code-level rule enforcem…

### [singh-levstik-phaidra-semantic-blindness.md](singh-levstik-phaidra-semantic-blindness.md)

212. `sig-semantic-blindness-at-scale` — "Semantic blindness": at 1 GW AI-factory scale (400k+ GPUs, ~1M equipment nodes, no industry naming standard) every LLM-native approach to resolving user que…
213. `sig-phaidra-flat-cost-100pct` — Head-to-head evals, same model/data, 3 runs per case: old LLM-search approach degraded 80% → ~30% correctness scaling 64 → 460,000 GPUs
214. `sig-karpathy-trend-inverted` — Phaidra ran Karpathy's software 1.0/3.0 trend backwards: legacy software drifts from deterministic 1.0 toward prompted 3.0, but their AI-native system starte…

### [bhardwaj-openai-agent-sandbox-cloud.md](bhardwaj-openai-agent-sandbox-cloud.md)

215. `sig-sandbox-vm-convergence` — "Seven stages of sandboxing" (paraphrase): OpenAI's sandbox-infra lead reports every serious agent-sandbox effort converges on hardware-virtualized micro VMs…
216. `sig-models-as-exploit-chainers` — The sandbox threat model now includes the model itself: frontier models are getting good at reading bug reports and chaining multi-step exploits (e.g
217. `sig-agents-leave-laptops` — The OpenClaw wave — agents run on laptops with lids held open, rented Hetzner VPSs, and Mac minis in the cloud
218. `sig-storage-next-unlock` — Compute (a Linux box) was the first agent unlock; durable disk is the next: incremental snapshot/restore already supports multi-day Codex "gold mode" runs (s…

### [brown-prime-intellect-post-training.md](brown-prime-intellect-post-training.md)

219. `sig-frontier-rl-run-50k` — Concrete cost floor for frontier-scale custom RL: on latest Prime RL, a GLM-5 step on 28 nodes takes <5 min at 131K context for long-horizon coding tasks
220. `sig-open-superintelligence-stack-real` — "A year ago 'open superintelligence stack' felt like marketing; now it's just what it is" (paraphrase): open models are superhuman at many things, and a full…
221. `sig-environments-become-the-unit` — Environments (task set + harness + runtime) are consolidating into the single unit of post-training: the same package drives evals, SFT data generation, RL, …
222. `sig-harness-unaware-rl` — Production harnesses now do RL without modification: the interception-server pattern gives each rollout a fake OpenAI/Anthropic-compatible endpoint, so "the …
223. `sig-posttraining-algorithm-wave` — "It is the age of research indeed" (paraphrase): a rapid wave of post-training algorithms within months

### [shashi-superagentic-rlm-codebases.md](shashi-superagentic-rlm-codebases.md)

224. `sig-monorepo-context-wall` — Coding agents work exceptionally well on small repos but degrade as context grows in large monorepos, and the standard mitigations shipped in today's harnesses
225. `sig-rlm-spreads-to-production` — RLM concepts are moving from the MIT paper into proprietary production harnesses within months: the speaker observed the Codex harness writing Python REPL co…
226. `sig-rlm-reimplementation-wave` — The RLM pattern is being independently reimplemented across the ecosystem shortly after publication

### [stagi-ratel-types-and-agents.md](stagi-ratel-types-and-agents.md)

227. `sig-typescript-passes-python-github` — In August 2025 TypeScript passed Python as the most-used language on GitHub — and GitHub's own reports attributed both moves to AI ("AI leads Python to the t…
228. `sig-coding-agents-default-typescript` — What changed between 2024 and 2025 was coding agents (Claude Code, Cursor, Codex) becoming the default way to build applications
229. `sig-anthropic-acquires-bun` — December 2025: Anthropic acquired Bun, a JavaScript runtime — an AI lab buying JS infrastructure, read as confirmation that the agentic application layer run…
230. `sig-vercel-ai-sdk-10x` — The Vercel AI SDK went from 1.6M to 15.1M weekly downloads in one year (~9–10x) — the TS-native AI ecosystem is surging as AI features move into ordinary app…

### [remobi-terminal-workflow-mobile.md](remobi-terminal-workflow-mobile.md)

231. `sig-mobile-agent-supervision-demand` — Agents now run long enough that builders feel a "compulsion to check on them" from their phones (audience hands went up), and a niche app ecosystem has forme…
232. `sig-terminal-multiagent-control-plane` — Practitioners are running 4+ coding agents in parallel tmux panes with vibe-coded custom keybindings and status tooling ("spawn N agents" bound to a keypress
233. `sig-remobi-attach-not-replace` — Remobi's design bet: don't replace the workflow, attach to it — a PWA over a Tailscale tunnel into existing tmux sessions gives agent-agnostic (Claude Code /…

### [cable-corridor-ai-bugpocalypse.md](cable-corridor-ai-bugpocalypse.md)

234. `sig-frontier-models-attack-chains` — Frontier models now find and exploit vulnerabilities better than a top-100-ranked human hacker (Cable's self-assessment)
235. `sig-ai-code-vuln-introduction-rate` — Even top models introduce vulnerabilities 20–40% of the time when writing code (BaxBench); Opus 46 introduced a smart-contract bug that cost a couple million…
236. `sig-android-memory-safety-drop` — Google's Android data: memory-safety share of vulns fell ~75% (2019) → ~30% (2022) just by writing *new* code in memory-safe languages, no rewrite required
237. `sig-ai-review-inflection` — Corridor's bet: within 6–12 months the majority of shipped code will be reviewed by AI, not humans
238. `sig-mythos-fable-export-controls` — 2026: export controls imposed on the Mythos and Fable frontier models; industry letter urged the White House to lift them (defender benefit outweighs risk

### [raskar-mit-agentic-web-bazaar.md](raskar-mit-agentic-web-bazaar.md)

239. `sig-agent-walled-gardens-aol-era` — MIT's diagnosis of the present: agent builders are forced inside walled gardens — closed platforms, proprietary agent stores, orchestration that only talks t…
240. `sig-trillions-of-agents-strain-dns` — Premise driving the build-out: the internet will eventually host trillions of autonomous agents that negotiate, delegate, and migrate between hosts in millis…
241. `sig-nanda-index-live` — The Nanda index is shipped and onboarding now: identity → signed agent-facts card → message box, with adaptive resolution
242. `sig-self-hosted-agents-as-control` — Because real agents need access to real tools/apps, the talk argues who controls the agent, where it runs, and what you can see now matter
243. `sig-nanda-town-experiments` — Nanda Town is already running real coordination experiments — marketplace price negotiation, auctions, agent voting/ballot counting, consensus, supply chains

### [taylor-pomerium-claws-out-openclaw.md](taylor-pomerium-claws-out-openclaw.md)

244. `sig-openclaw-control-plane-hardening` — OpenClaw shipped a community-contributed "trusted proxy auth" mode (Taylor's Feb 2026 contribution, maintainer-specced): an identity-aware proxy now gates th…
245. `sig-openclaw-issue-velocity` — OpenClaw's growth measured in issue numbers: Taylor's issue was #1560; two weeks later numbering was near 16,000
246. `sig-agent-full-gh-access-premature-pr` — First-hand over-permissioning incident: Taylor gave OpenClaw full GitHub CLI access while using it to write his own contribution
247. `sig-personal-software-from-phone` — "Age of personal software" in practice: Taylor builds his own tools (Claw Space workspace-file browser, MCP apps) by chatting with his self-hosted agent from…
248. `sig-mcp-apps-ui-in-chatgpt` — MCP servers with UI are now in the MCP spec ("MCP apps"): live demo registers an OAuth'd MCP server in ChatGPT, renders React-based widgets in-chat (echo too…

### [gupta-reviewdebt.md](gupta-reviewdebt.md)

249. `sig-github-commits-up-reviews-down` — GitHub's October 2025 report (covering nearly every public PR): commits +25% YoY while PR comments — the proxy for review activity — fell 27% in the same year
250. `sig-faros-review-time-blowup` — Faros AI 2026 benchmarks (AI-adoption cohort; April 2026 study = 22k developers, 4k teams): median PR review time up 441.5%, reviewed PRs take 5.4× longer th…
251. `sig-review-debt-compounds` — Review debt is generative: (1) the agent learns from your codebase — code not deeply reviewed yesterday grounds tomorrow's PRs via fine-tuning/RAG/in-context
252. `sig-524-pr-scan-volume-not-authorship` — 90-day scan of 524 PRs across 3 public repos: AI-authorship indicators steady at 5–20%/week, yet burden tracked *volume*

### [dotta-paperclip-liveness-model.md](dotta-paperclip-liveness-model.md)

253. `sig-agents-create-unverifiable-volume` — Practitioner claim from a control-plane builder: "programming is solved" — agents now produce more code and documentation than any human can verify, a new fa…
254. `sig-done-flattened-to-checkmark` — Current agent systems flatten operationally distinct claims — done-to-merge vs done-to-deploy vs done-to-announce — into a single green checkmark
255. `sig-watchdogs-above-harnesses` — Paperclip ships harness-agnostic watchdog agents: a goal-holding agent enforces that all worker agents keep going until the goal is achieved, with one consis…

### [embiricos-huet-steinberger-openai-golden-age.md](embiricos-huet-steinberger-openai-golden-age.md)

256. `sig-openai-6-week-model-cadence` — OpenAI's shipping cadence collapsed from a new model every ~15 months to roughly every 6 weeks
257. `sig-codex-open-at-every-layer` — OpenAI open-sourced the entire Codex stack around the model — harness, app server (the same path its own apps use), plugins, AGENTS.md
258. `sig-frontier-intelligence-price-speed` — Frontier intelligence is being repriced in real time: GPT-5.6 Terra = 5.5-level intelligence at half the cost
259. `sig-agents-do-whole-computer-tasks` — Codex-class agents now do any task doable on a computer — the work before coding (triage, deciding why) and after (review, deploy), not just the coding
260. `sig-steinberger-attention-bottleneck` — Steinberger's bottleneck migration, dated: January 2026 = 10+ terminals, "I thought I was orchestrating
261. `sig-local-cloud-boundary-dissolving` — The local-vs-cloud task distinction is being framed as a bug to eliminate: laptops stay open in offices so agents keep working

### [browne-everything-changed.md](browne-everything-changed.md)

262. `sig-model-eras-to-orchestration` — Browne periodizes coding models into eras: Sonnet 3.5 = the tool-call era (first to call tools reliably enough for daily codebase work)
263. `sig-startup-tier-collapse` — The build-size tiers shifted down a full level in ~a year: his 2021 YC startup (Ping) would be a side project today
264. `sig-markdown-file-products` — Concrete replacement, dated and running: his PR-triage service is now literally a markdown file
265. `sig-breadth-viable-for-small-teams` — Breadth-vs-depth economics inverted: pre-AI, startups had to out-depth incumbents in a narrow vertical (Vercel vs AWS — "even the agents prefer Vercel")

### [litt-notion-understanding-bottleneck.md](litt-notion-understanding-bottleneck.md)

266. `sig-agent-code-outpaces-review` — Whether humans still need to understand code is now a live, debated question: agents land 50,000-line PRs, "code review is the new bottleneck" is common parl…
267. `sig-notion-agent-workspace-launches` — Dated product moves toward shared human+agent workspaces: Notion launched HTML blocks in pages the morning of the talk (agents can embed interactive simulati…
268. `sig-education-techniques-for-agent-code` — Practitioners are importing education science to keep up with agent-written code: Litt's ExplainDiff (background-first explainer docs + gate-keeping quizzes

### [volkov-thursdai-zl-continuum.md](volkov-thursdai-zl-continuum.md)

269. `sig-dec-2025-trendline-break` — December 2025 named as the moment AI engineering "broke its own trendline": METR data shows models for the first time completing tasks that take engineers 16…
270. `sig-acceleration-whiplash-survey` — Faros AI's April 2026 survey of 22,000 engineers ("the acceleration whiplash") quantifies both sides: +861% code deletion per PR, +31% PRs merged with no rev…
271. `sig-anthropic-rsi-review-bottleneck` — Anthropic's recursive-self-improvement essay concedes the point from the frontier: as orgs 10×→1000× code output, "human code review has become the new bottl…
272. `sig-hand-written-code-vanishing` — Hand-writing code is functionally over at the frontier: Boris Cherny (Claude Code's creator) has 100% of his code authored by Claude Code, deleted his IDE, a…
273. `sig-loops-zeitgeist-aie26` — "Loops" became the conference zeitgeist within ~2 days of Steinberger and Cherny both talking about them: scheduled agents that discover a task, write their …
274. `sig-read-code-debate-poles` — The read-your-code anxiety is now the industry's most-watched argument: two AI Engineer EU talks staking opposite poles

### [local-ai-panel-state-of-union.md](local-ai-panel-state-of-union.md)

275. `sig-local-frontier-gap-closing` — Panel datapoints on the closing local-frontier gap: Qwen 3.5 4B on an iPhone ≈ the quality "that used to be served in data centers" at the GPT-4o moment (Che…
276. `sig-exo-nvidia-spark-10x` — EXO Labs embedded at NVIDIA HQ (a "second headquarters" conference room; Jensen's "swarming"
277. `sig-enterprise-multi-model-pull` — The market is pulling multi-model, not one-model-rules-all: enterprises reject being "told what they can do by Dario," fear rug-pulls and silent version chan…
278. `sig-agents-provisioning-gpus` — NVIDIA's Brev is seeing growing usage from *agents* that go grab a GPU directly, and has started treating agents as a first-class audience for GPU provisioning
279. `sig-specialized-model-pendulum` — The pendulum is swinging back to small specialized models, with vision as the leading indicator (edge compute constraints forced specialized learners years ago
280. `sig-open-weights-under-threat` — Nelson's closing warning: "the importance of open models is becoming increasingly in question"

### [fenner-zed-acp-agent-live.md](fenner-zed-acp-agent-live.md)

281. `sig-acp-forty-clients` — ACP reaches ~40 clients within roughly a year: JetBrains, Obsidian, and OpenClaw implement the client side (OpenClaw is simultaneously an ACP client and an a…
282. `sig-tui-agent-wave-editor-response` — Speaker dates 2025 as the rise of terminal coding agents from every major model provider (Claude Code, Codex, Gemini CLI)
283. `sig-minimal-agent-live-bootstrap` — Live on stage: a bare coding agent is two tools (read file, edit file) plus a stateless model-API loop

### [campos-witan-spreadsheet-agents.md](campos-witan-spreadsheet-agents.md)

284. `sig-witan-spreadsheet-92pct` — Witan Labs spent 4 months (2026) teaching coding agents spreadsheets: ~50% → 92% on an internal financial-analysis benchmark
285. `sig-code-mode-goes-mainstream` — Code mode is spreading as an agent interface (shipped in the Anthropic API, talked up by Cloudflare)
286. `sig-verification-loop-compounds-with-models` — Across the 4–5 frontier model releases that shipped during the project, each more capable model extracted MORE from the same verification loop (formula engin…
287. `sig-llm-judge-attribution-problem` — Witan moved evals from LLM-as-judge to deterministic golden-spreadsheet comparisons (fixed inputs → expected outputs as a black-box test on the model-produce…
288. `sig-harness-bugs-masquerade-as-model-failures` — Practitioner observation: many apparent reasoning failures were plumbing — a wrong example in the prompt/skill that the model followed faithfully, or failing…

### [sheikh-checkout-agent-rules.md](sheikh-checkout-agent-rules.md)

289. `sig-vector-diy-enforcement` — A Checkout.com engineer built Vector after repeated "task completed" claims from Claude Code failed on actual run — realization: "I am the enforcement layer"
290. `sig-lab-predicts-enforcement-obsolete` — An Anthropic engineer told the speaker enforcement layers won't be needed — "another model will be so smart you won't need enforcement"
291. `sig-guardrails-downshift-models` — With deterministic guardrails in the harness, smaller/cheaper models (Haiku-class, open-source) still converge on the wanted output
292. `sig-enforcement-convergence-and-fragmentation` — Everyone is building bespoke, unshareable enforcement (Anthropic, Meta, Checkout.com, indie devs

### [lajili-poolside-agent-blindfolded.md](lajili-poolside-agent-blindfolded.md)

293. `sig-bimodal-ai-discourse-feedback-loop` — Mid-2026 discourse on coding AI is bimodal ("never touching code again" vs "produces absolute garbage in my production app")
294. `sig-spoolside-agent-eyes` — Poolside built Spoolside, an internal CLI (deliberately unreleased) so its agents can test a non-web product (a VS Code extension): screenshots, token-compre…
295. `sig-aix-engineer-role-shift` — Declared role shift, dated by the speaker: 2025 had "product engineers"; now engineers should "focus less on the product and more on making the AI work on th…

### [lee-chan-snapchat-idea-velocity.md](lee-chan-snapchat-idea-velocity.md)

296. `sig-personal-agent-org-70pct` — A Snap engineer's daily setup (mid-2026): a Slack-facing OpenClaw manager with task memory ("fix the skeptic agent" suffices
297. `sig-manager-context-debiases` — Live example: a worker agent reviewing its own PR would have said "this PR is amazing, merge it"
298. `sig-orchestrator-context-budget` — Stated rationale for the manager layer: opening Claude Code immediately burns ~25% of context on how-to-do-the-task scaffolding (CLAUDE.mds, skills, MCPs)
299. `sig-browser-testing-matured` — Capability timestamp: browser-driving agents crossed a reliability threshold within the last ~6–12 months
300. `sig-budget-driven-model-mixing` — Orchestrator model choice is driven by token economics, not preference: default "Codex 5.3" (5.4 "just uses more tokens"
301. `sig-agent-native-terminal-tooling` — Terminal tooling is productizing around agent fleets: a cmux creator (present in the workshop) cites shipping a Claude Code Teams integration that auto-spawn…

### [doshi-machinecraft-39-agents-no-framework.md](doshi-machinecraft-39-agents-no-framework.md)

302. `sig-factory-grows-company-brain` — A 100-person Indian factory with no data-science team or ML budget turned "three generations in three brains" into a company brain: hundreds of GB of private…
303. `sig-39-agent-gtm-pantheon` — Machinecraft's entire front-of-funnel GTM — nine daily jobs (outbound referencing real history, account briefs from cross-checked facts, quotations, outreach…
304. `sig-agent-build-cost-collapse` — An agency quoted ~$230k to build the system; the owner built it for ~$30k ("cheaper than a nice watch") and runs it for a couple thousand dollars/month

### [shrabony-solo-agent-cicd.md](shrabony-solo-agent-cicd.md)

305. `sig-solo-builders-reinvent-cicd` — Solo builder running a 19-skill open-source Claude Code content pipeline (biweekly scheduled runs
306. `sig-polished-artifact-fails-gates` — The dangerous failure is not a visibly bad output (glance-fixable) but a polished, complete-looking artifact that violates exit criteria
307. `sig-agent-demos-hide-unhappy-path` — Practitioner calls out that agent demos systematically show only the happy path while the same pipeline ships professional-looking failures

### [lee-krafton-agent-fleet-broke.md](lee-krafton-agent-fleet-broke.md)

308. `sig-fleet-operator-is-bottleneck` — KRAFTON engineer running 4–6 concurrent agent contexts in tmux found the human silently becomes the scheduler (who does what), the memory (what each is doing…
309. `sig-agent-fleet-as-org-chart` — Fleet rebuilt as an organization — CEO/VP/manager/worker as real entity types with scoped context and approval boundaries
310. `sig-reset-over-compact` — Practitioner abandoned context compaction entirely — slow, unselectable, lossy ("whatever it throws away is just gone")
311. `sig-multi-machine-five-failures` — Scaling from one machine to three (MacBook + two always-on headless Linux boxes, one control plane) broke five ways: orchestrators doing the work themselves …

### [steinfurt-tng-ai-chess-channel.md](steinfurt-tng-ai-chess-channel.md)

312. `sig-chess-holy-grail-already-automated` — ~One week before the talk (early July 2026), one of Germany's biggest newspapers quoted chess trainer Wilhelm Weber calling AI that explains chess as well as…
313. `sig-engine-llm-tool-bridge` — Chess engines have been superhuman for decades but can't explain; LLMs explain but can't play
314. `sig-reasoning-models-absorbed-pipeline` — The division of thinking flipped within about a year: the pre-reasoning-model pipeline was Python scripts assembling position analysis for an LLM to verbalize
315. `sig-chess-video-unit-economics` — Auto-generated explainer videos cost ~€0.20–0.30 each (longer formats: a few euros) with ~1-in-20 having a defective description

### [bauer-upside-ai-trust-patterns.md](bauer-upside-ai-trust-patterns.md)

316. `sig-gtm-teams-become-builders` — GTM teams — historically the lowest builder-density function, running on spreadsheets and slides
317. `sig-hallucination-becomes-trust-problem` — The "AI hallucination problem" discourse of a couple of years ago has faded and matured into its "older sibling," a trust problem: ask Claude to report reven…
318. `sig-jury-judge-in-production` — Upside ships jury-and-judge attribution: independent analyst agents produce evidence-cited opinions on a deal's attribution credit
319. `sig-jit-librarian-in-production` — Upside ships a librarian agents must consult before querying: company docs, curated knowledge-item definitions (fiscal year Feb–Apr
320. `sig-subscription-ai-cant-reason` — Slack shipped Slackbot MCP-client support ~2 weeks before the talk; the speaker wired it to his own librarian and found it "horrifically stupid" for real work

### [ramachandran-filed-vertical-ai.md](ramachandran-filed-vertical-ai.md)

321. `sig-filed-revenue-inflection` — Filed (AI agents for US tax pros, $17M+ raised) closed more revenue in a single month (mid-2026) than in the entire preceding year, two years into building
322. `sig-chat-citations-insufficient` — Practitioner verdict after 2 years of vertical tax agents: chat is synchronous (user must sit and wait) and citations push the verification burden onto the c…
323. `sig-agentic-delegation-abstraction` — Third product-abstraction level claimed live: physical presence (value bottlenecked on employee count) → digital self-serve (bottlenecked on user count) → ag…
324. `sig-wau-obsolete` — Filed argues weekly active users is now the wrong north-star for agentic products and tracks weekly active sessions instead
325. `sig-automatic-skill-capture` — Filed captures agent skills automatically from product usage — a separate skill-authoring interface "won't work"

### [an-hoe-meta-game-with-ai.md](an-hoe-meta-game-with-ai.md)

326. `sig-llm-npcs-now-feasible` — Meta's AI-gaming team demoed a multiplayer game — built in a couple of days — where every NPC is entirely runtime-LLM-driven: assigned personalities (thief, …
327. `sig-game-prompting-commoditized` — By 2026 anyone — kids, moms, friends — can prompt a working basic game (platformer/Tetris) on consumer models
328. `sig-game-waterfall-parallel` — After ~12 months directing cross-discipline AI game teams at Meta: production flipped from linear waterfall (design→art→modeling→animation→code
329. `sig-agentic-stack-nondeterminism` — Meta platform engineers report non-determinism now spans the whole stack — user prompting at the frontend, runtime LLMs inside the game, agentic serving/rank…

### [noring-microsoft-code-to-systems.md](noring-microsoft-code-to-systems.md)

330. `sig-devrole-shifted-2026` — Show of hands in a capacity AIE room (mid-2026): almost nobody still "codes like they used to" — the audience has shifted to a systems approach
331. `sig-cli-displaces-editor` — A 20-year editor-native Microsoft engineer now starts the workday in the CLI — six-plus terminals of parallel agent runs ("build me an app", "fix this issue"…
332. `sig-guardrail-stack-convergence` — A tiered guardrail stack is presented as baseline practice: AGENTS.md in every repo → skills (strict-contract recipes) → custom agents (personas with tool al…
333. `sig-delegate-draft-pr-loop` — GitHub ships delegation as product: /delegate from Copilot CLI hands the session to GitHub (job + draft PR from sandboxed agents), and the GitHub UI assigns …
334. `sig-demos-replace-decks` — Businesses report engineers no longer bring PowerPoints — they bring working demos; the MVP has become cheaper to produce than the slide deck about it

### [kumar-lexisnexis-deception-monitor.md](kumar-lexisnexis-deception-monitor.md)

335. `sig-sleeper-backdoors-defeat-evals` — A fine-tuned model can pass every eval and every behavioral production monitor while carrying a trigger-conditioned backdoor: in Kumar's controlled replicati…
336. `sig-finetune-supply-chain-exposure` — Four open doors put backdoors into models teams actually ship: poisoned slices of scraped/third-party training or RLHF data
337. `sig-diff-sae-40x` — Peer-reviewed (IJCNN, open-source) result: an SAE trained on activation *differences* isolates the backdoor as one feature at 0.4 backdoor-isolation score vs…

### [melnikova-evil-martians-gtm-is-you.md](melnikova-evil-martians-gtm-is-you.md)

338. `sig-planetscale-founder-account` — Summer 2026, PlanetScale's new SF office: CEO Sam Lambert tells Melnikova "you would be shocked if I told you how many customers we get from my own [Twitter]…
339. `sig-distribution-is-bottleneck` — Evil Martians' PMF-compass data (37 successful devtools analyzed; early-stage client base): 9 of 10 early-stage devtools show product signal stronger than re…
340. `sig-slop-saturated-channels` — 2026: AI has made inboxes and feeds nearly unusable for GTM — "so much annoying outreach and generated slop that it's really hard to tell the real deal"
341. `sig-costly-signaling-returns` — Expensive physical GTM signals are back for devtools: Typesense (bootstrapped, no funding milestones to announce) ran hundreds of SF billboards explicitly as…

### [shihipar-anthropic-field-guide-fable.md](shihipar-anthropic-field-guide-fable.md)

342. `sig-fable-capability-overhang` — Anthropic Claude Code staff frames Fable's launch as an unmapped capability overhang: the models' latent ability exceeds what harnesses currently extract (Po…
343. `sig-system-prompt-era-arc` — System-prompt best practice has moved in an arc across model generations: Sonnet-3.5-era = small prompt, few tools, many examples → mid-era = large prompts, …
344. `sig-question-tool-progression` — The "ask a question" tool traces the overhang across releases: Opus 4 could barely call it (tool needed heavy tweaking), Opus 4.5 could run a 40-question spe…
345. `sig-fable-bottleneck-is-operator` — Practitioner claim: "Fable is bottlenecked by my ability to match the map and the territory"
346. `sig-tradeoffs-collapse` — Returning to his ~30-person YC startup's codebase: changes that took weeks now take hours; the "good, fast, cheap

### [bhargava-etsy-harness-over-model.md](bhargava-etsy-harness-over-model.md)

347. `sig-harnessbench-20pt-spread` — HarnessBench evidence: same model, same 106-task evaluation, only the harness changed → resolution ranges 52.4% to 76.2% (>20 points), with the harness matte…
348. `sig-harness-for-local-models` — Etsy staff engineer pushes back on the emerging industry wisdom "models are so good, keep the harness simple, give it a few tools"
349. `sig-agency-language-level-harness` — Claim: building a really good harness requires *language-level* support — existing tools/frameworks couldn't do it, so Bhargava spent 6 months building Agenc…

### [chandegra-annicha-beyond-the-harness.md](chandegra-annicha-beyond-the-harness.md)

350. `sig-harness-adaptability-limiting-factor` — Thesis claim: "the limiting factor is not going to be the strength of the model — it's going to be the adaptability of the harness"
351. `sig-fixed-harness-obsolescence` — Fixed harnesses have a decay problem on two fronts: (1) "you can build a careful harness today... it could be irrelevant next month
352. `sig-ai-meets-real-world-complexity` — Claim: AI engineering is about to leave the screen into multi-agent, multi-human, cross-institutional, physical-world settings, which are *complex* (interact…

### [lichtenberg-mixedbread-agent-retrieval.md](lichtenberg-mixedbread-agent-retrieval.md)

353. `sig-knowledge-gap-oracle-benchmarks` — context
354. `sig-agents-write-caveman-queries` — context
355. `sig-small-model-rl-search-wins` — training

### [desai-abundant-swe-marathon.md](desai-abundant-swe-marathon.md)

356. `sig-swe-marathon-26pct-ceiling` — On SWE-Marathon's 20 project-scale tasks the best configuration evaluated — Claude Opus 4.8 + Claude Code — resolves only 26% (~1 in 4)
357. `sig-agent-scaffold-2x-spread` — Same benchmark, different stacks: Opus 4.8 + Claude Code hits 26% (among the most expensive configs) while GPT 4.5 + Codex is far cheaper at 12%
358. `sig-weak-verifier-attack-surface` — At multi-hour scale a weak verifier stops being noise and becomes an attack surface: the agent has hours, a filesystem, potentially unrestricted network, and…
359. `sig-reward-hacking-arms-race` — Across 1,400 rollouts: 12.8% showed suspicious shortcut behavior (hunting solution files, tampering with data/configs) and 9% shipped a clear verifier bypass…
360. `sig-cua-verifier-full-stack` — Full-stack product clones have been missing from every long-horizon SWE benchmark because unit tests can pass while the product is unusable and the frontend …

### [ortmann-lee-duolingo-discernment.md](ortmann-lee-duolingo-discernment.md)

361. `sig-duolingo-proctor-rubber-stamp` — Duolingo English Test injected fake AI copy-typing flags into clean historical sessions inside proctors' normal workflow: reviewers who consistently score >9…
362. `sig-duolingo-guideline-copy-fix` — Changing only the proctor guideline copy (the AI signal is a preliminary alert; you are the final decision-maker
363. `sig-wharton-cognitive-surrender` — Wharton study on AI-assisted reasoning exams: ~80% of participants accepted AI answers even when wrong
364. `sig-coding-agent-rubber-stamp-uis` — Practitioner observation: out-of-the-box coding agents converge on two interaction patterns

### [dumit-watershed-respect-the-process.md](dumit-watershed-respect-the-process.md)

365. `sig-wine-lca-expert-variance` — Cited 2020 study: six sustainability experts given identical data on the same bottle of wine produced emissions answers varying by up to ~50%
366. `sig-watershed-agent-misbehavior` — Swapping a tool-calling ReAct agent (which broke at tens-to-hundreds of graphs: inconsistency, context-gobbling tool calls, schema hallucination) for a codin…
367. `sig-open-proof-corpus-gap` — Cited 2026 Open Proof Corpus / "Beyond Correctness" result: a sizable gap between correct final answers and correct proofs even in fully verifiable math, wit…
368. `sig-watershed-evals-43-to-92` — With the typed-SDK + deterministic-execution harness in place, Watershed still had to hill-climb capability: internal evals on complex multi-graph edit tasks…

### [ten-teije-sky-valley-pipeline-is-dead.md](ten-teije-sky-valley-pipeline-is-dead.md)

369. `sig-frozen-artifact-was-economics` — Founder thesis (from the co-founder who built JFrog's pipeline): "one version for everyone, frozen" was never a fact about software
370. `sig-demand-for-personal-software` — Demand-side evidence predates AI by decades: enterprise professional services / forward-deployed engineers as an entire industry line item, engineers hand-re…
371. `sig-differ-per-user-divergence-bet` — Sky Valley/Differ's product bet: instead of one codebase gated by flags and shipped to everyone, one canonical stem with every user running her own live-adap…
372. `sig-generation-easy-80-percent` — "Calling a model to write some code is something everyone can do — generation is the easy 80%." The business is the substrate: observability, validation (cor…

### [grbic-automattic-500-vibe-coders.md](grbic-automattic-500-vibe-coders.md)

373. `sig-automattic-radical-speed-month` — Automattic ran "Radical Speed Month": a third of the company (~500 people) paused roadmap work for 30 days, paired into two-person teams with full autonomy, …
374. `sig-designer-to-design-engineer` — A product designer who had never shipped work code built a design-system status tracker solo as a full proof of concept in ~2.5 weeks
375. `sig-figma-demoted-to-fine-tuning` — A years-stable design process inverted in 30 days: instead of working in Figma to high fidelity and handing off, designers now plan, build the working protot…
376. `sig-engineers-become-enablers` — In mixed-ability AI teams the engineer's highest-leverage move shifted from writing code to enabling others
377. `sig-designers-ship-ios-chat-6-days` — Two designers went zero-to-working iOS chat proof of concept for WooCommerce merchants in 6 days

### [kalandadze-wandero-missing-layer.md](kalandadze-wandero-missing-layer.md)

378. `sig-agent-failure-hides-itself` — Agent failure hides itself: a long-running agent that struggles mid-task and recovers "by luck" (workarounds, alternate tool calls) raises no red alert while…
379. `sig-wandero-agents-operate-agents` — Operating a production agent turned out to be an agent problem: Wandero's log-monitoring agent runs every 15–60 minutes over a one-hour log window with codeb…
380. `sig-fresh-context-review-agent` — A separate review agent with deliberately fresh context — not biased by the diagnosing agent's framing
381. `sig-score-every-conversation` — Wandero's session analyzer scores every production conversation — health score, success/rejection rates and why, trends, sentiment, entities, tool-call analy…
382. `sig-ops-loop-is-differentiator` — "Everyone can have the same model, the same agent, the same harness" — shipping is now the easiest part (a whole product or startup in days, 100k lines of co…

### [zullo-manufact-mcp-apps.md](zullo-manufact-mcp-apps.md)

383. `sig-mcp-apps-official-extension` — MCP-UI became MCP Apps, an official Model Context Protocol extension, in January 2026: MCP servers now return interactive sandboxed UI, not just JSON
384. `sig-mcp-stores-open-self-serve` — The second structural shift: MCP stores moved from design-partner gating to self-serve submission
385. `sig-claude-dynamic-connector-discovery` — Claude is today the only client that, given a task with no matching tool, searches the MCP registry and selects the best store-listed connector dynamically
386. `sig-mcp-server-buying-decision` — Practitioner adoption testimony: "does this product have an MCP server" is now a basic buying criterion

### [agent-skills-missing-manual.md](agent-skills-missing-manual.md)

387. `sig-skill-hell` — After tutorial hell and framework hell, practitioners are in "skill hell": freely downloadable community skills proliferate with no shared rubric to tell goo…
388. `sig-model-invocation-tax` — The skill-invocation tradeoff, quantified by a leading skills author: every model-invoked skill's description permanently occupies agent context (100 skills …
389. `sig-plan-mode-eager-planning` — Consistent failure mode across every plan-mode implementation the author tried: the ask-clarifying-questions step never does enough legwork because the agent…

### [schroeder-standardagents-domain-specific.md](schroeder-standardagents-domain-specific.md)

390. `sig-everyone-builds-custom-agents` — Everyone is building custom agents — a local real-estate agency, independent insurance brokers, many Fortune 500s
391. `sig-mcp-reduced-to-tools` — Reading MCP's own client-support matrix: only the tools column is implemented across clients
392. `sig-context-inflation-diminishing-returns` — Skills/MCP stacking is inheritance — inflating one general agent's context layer; the speaker cites research that installing very many skills makes an agent …
393. `sig-token-cost-reversal-2026` — The cost-of-intelligence decline reversed in 2026 (speaker tracks it on a website): IQ-adjusted token prices up 29% and raw prices up ~76% in H1 2026, memory…
394. `sig-dsa-prediction-h2-2026` — Public prediction: from mid-2026, a dramatic uptick in domain-specific-agent frameworks, ecosystems, and discourse

### [tornow-resonate-prompt-is-platform.md](tornow-resonate-prompt-is-platform.md)

395. `sig-platform-retirement-prediction` — Opening claim: in 2026, coding agents will quietly retire their first software platform — not because it's bad, because it's unnecessary
396. `sig-resonate-spec-as-product` — Dated vendor repositioning: Resonate — a durable-execution vendor with a server and five SDK implementations
397. `sig-abstract-spec-agent-failure` — Experiment result: an agent asked to build a Resonate server in Rust on Postgres straight from the abstract spec produced a happy-path prototype
398. `sig-dst-agent-designs` — With a deterministic simulator plus forbidden-fruit traces, the agent moved upstream on the NATS build: it produced a fuzz-verified proof-of-concept in simul…

### [johnson-joinin-prompt-punch-card.md](johnson-joinin-prompt-punch-card.md)

399. `sig-voice-mode-one-slot` — Field anecdote (weeks before the talk): a frontier speech-to-speech voice mode answered a normal question fine, then
400. `sig-gpt-realtime-2-backchannels` — OpenAI released GPT-realtime 2 in late May and began using it for ChatGPT voice mode; it now backchannels ("mhm", "right")
401. `sig-personaplex-full-duplex` — NVIDIA's PersonaPlex research model demonstrates real turn-taking: interrupted mid-answer it stops, yields, then resumes the earlier thread

### [gupta-meta-deterministic-infra.md](gupta-meta-deterministic-infra.md)

402. `sig-agent-infra-great-mismatch` — Meta infra tech lead: autonomous agents violate every core assumption of modern cloud infrastructure (short-lived requests, deterministic services, known exe…
403. `sig-infra-turns-mistakes-into-outages` — Production failure taxonomy from inside Meta and across industry: hallucinations are "often the least interesting failure mode" (paraphrase)
404. `sig-control-plane-next-frontier` — Prompts were the differentiator, then models — both "rapidly commoditizing" (paraphrase); the next frontier is reliability infrastructure

### [chawla-koul-microsoft-agent-failed-prod.md](chawla-koul-microsoft-agent-failed-prod.md)

405. `sig-prod-agent-failure-unreproducible` — harness
406. `sig-clean-200-wrong-trade` — harness
407. `sig-temperature-zero-myth` — inference
408. `sig-chronicle-replay-ci` — harness

### [benzon-rl-etl-remediation.md](benzon-rl-etl-remediation.md)

409. `sig-etl-remediation-minutes-vs-days` — Benchmarked RL-guided ETL remediation loop (AWS Glue job-fail event → EventBridge → Lambda agent → read-only evidence from CloudWatch logs + Glue Data Catalo…
410. `sig-rl-matches-handwritten-policy` — The honest headline result: on the compact state space, the learned policy only MATCHED an equivalent hand-defined deterministic policy (difference 0.19 pp)
411. `sig-escalation-as-capability` — Escalation is designed into the action space as a first-class outcome, not agent failure: enabling the safety override intentionally reduced non-escalation b…

### [hanchett-aws-agent-wasting-tokens.md](hanchett-aws-agent-wasting-tokens.md)

412. `sig-default-agent-loops-leak-tokens` — harness
413. `sig-route-dont-default-to-frontier` — inference
414. `sig-token-economy-productized` — harness

### [sakthivel-tesco-local-code-index.md](sakthivel-tesco-local-code-index.md)

415. `sig-input-90-output-10` — Practitioner cost autopsy after a month-over-month AI-coding bill spike with unchanged usage: ~90% of spend was input tokens
416. `sig-94pct-context-cut-benchmark` — Public benchmark of the local index on FastAPI (53 files, 20 real developer questions): 83K → 4.9K tokens per question (94% cut
417. `sig-coding-tools-share-nothing` — Every AI coding tool re-learns the same codebase from scratch and shares nothing across tools or sessions (Claude Code for hard problems, Cursor for quick ed…

### [yaron-amplify-state-of-ai-engineering.md](yaron-amplify-state-of-ai-engineering.md)

418. `sig-2026-agents-cross-write-threshold` — harness
419. `sig-2026-evals-still-top-challenge` — harness
420. `sig-2026-openweight-augments-closed` — inference
421. `sig-2026-cost-first-class-constraint` — inference
422. `sig-2026-nondev-shipping` — —
423. `sig-2026-image-gen-doubles-audio-intent` — inference

### [feizi-relai-continual-learning.md](feizi-relai-continual-learning.md)

424. `sig-relai-vcl-engine-launch` — training
425. `sig-logs-are-not-learning-environments` — training
426. `sig-continual-learning-not-finetuning` — training

### [nabors-arize-frontier-on-device.md](nabors-arize-frontier-on-device.md)

427. `sig-nvidia-slms-future-agentic` — inference
428. `sig-frontier-inference-cost-stack` — inference
429. `sig-on-device-models-preinstalled` — inference
430. `sig-llama-3b-matches-sonnet-with-harness` — harness

### [hylak-hey-ai-explainability.md](hylak-hey-ai-explainability.md)

431. `sig-ai-pitch-attention-collapse` — —
432. `sig-clearest-story-gets-funded` — —

### [sanftl-mutagent-agentic-ai-engineer.md](sanftl-mutagent-agentic-ai-engineer.md)

433. `sig-human-review-bottlenecks-agent-loop` — harness
434. `sig-mutagent-research-preview` — harness
435. `sig-harness-churn-spec-portability` — harness

### [pike-forestwalk-voice-in-visuals-out.md](pike-forestwalk-voice-in-visuals-out.md)

436. `sig-karpathy-voice-in-visuals-out` — harness
437. `sig-gpt5-mini-latency-tax` — inference
438. `sig-forestwalk-incall-action-agent` — harness
439. `sig-thinking-machines-200ms-slices` — inference

### [shah-financial-compliance-correlation.md](shah-financial-compliance-correlation.md)

440. `sig-fraud-lives-between-documents` — context
441. `sig-compliance-graph-detection-results` — security
442. `sig-compliance-reactive-to-predictive` — context

### [kalinowski-callstack-physical-openclaw.md](kalinowski-callstack-physical-openclaw.md)

443. `sig-callstack-physical-ai-terminal` — robotics
444. `sig-model-off-the-metal` — inference
445. `sig-quiet-ai-hardware-niche` — robotics
446. `sig-epaper-llm-rpg-console` — harness

### [matini-ogilvy-multimodal-tax.md](matini-ogilvy-multimodal-tax.md)

447. `sig-multimodal-tax-structure-first` — data-eng
448. `sig-smallest-model-vetted-data` — inference
449. `sig-guardrails-in-code-not-prompts` — harness
450. `sig-framework-free-rag-stack` — harness

### [joshi-mongodb-ai-system-design.md](joshi-mongodb-ai-system-design.md)

451. `sig-specs-new-code-convergence` — harness
452. `sig-vibe-coding-stops-at-stakes` — harness
453. `sig-agent-first-overengineering` — harness

### [horvath-visuallabs-prompt-the-room.md](horvath-visuallabs-prompt-the-room.md)

454. `sig-visuallabs-hackathon-value-filter` — VisualLabs' internal hackathon (start of 2026): 21 agent ideas, 17 abandoned for creating no business value (no data access, or no reason to exist)
455. `sig-bottleneck-moved-to-the-room` — 13-year business↔IT bridge consultant: over the past 2–3 years writing code stopped being the SDLC bottleneck
456. `sig-smartest-people-upstream` — Prescribed org shift: pre-AI, firms put their smartest people on writing code; now they belong customer-facing, deciding what gets built
457. `sig-ai-defaults-to-average` — AI is built to return the most common answer, so using it naively replicates what already exists — Henry Ford's faster horse

### [iusztin-bouchard-notes-into-memory.md](iusztin-bouchard-notes-into-memory.md)

458. `sig-second-brain-harness-gap` — Two AI-education practitioners with 10k+ notes (5k Obsidian + 5k Readwise + Notion/Drive, growing ~250 files/month) find stock tools can't durably leverage a…
459. `sig-files-over-retrieval-infra` — Deliberate architecture rejection for personal-scale memory: they dropped vector databases, knowledge graphs, semantic search, and text search ("all that is …
460. `sig-wiki-living-memory` — The wiki layer is alive: every question leaves a trace (the LLM can create new concept/note/comparison files
461. `sig-deep-research-aimed-inward` — System progression V1→V2: the deep research loop was retargeted from the public web (which required manually handpicked "golden links" and produced generic r…

### [savkin-nx-genius-with-amnesia.md](savkin-nx-genius-with-amnesia.md)

462. `sig-agents-space-time-constrained` — harness
463. `sig-nx-polygraph-multi-repo-sessions` — harness
464. `sig-session-transfer-cross-agent` — harness
465. `sig-org-hive-mind-memory` — context

### [romero-sevilla-orbis-cache-augmented.md](romero-sevilla-orbis-cache-augmented.md)

466. `sig-churn-breaks-graphrag` — context
467. `sig-orbis-parallel-cag-supervisor` — context
468. `sig-context-overfill-degrades` — inference

### [pankaj-starlight-retrieval-boundary.md](pankaj-starlight-retrieval-boundary.md)

469. `sig-retrieval-fails-not-generation` — context
470. `sig-eval-signal-dies-in-dashboard` — harness
471. `sig-outcome-weighted-memory-lifts-benchmarks` — context
472. `sig-memory-products-store-preferences-not-outcomes` — context

### [clyburn-redhat-structuring-unstructured.md](clyburn-redhat-structuring-unstructured.md)

473. `sig-unstructured-data-new-context-layer` — data-eng
474. `sig-scanned-pdf-term-cascade` — data-eng
475. `sig-ingestion-determines-answer-quality` — data-eng
476. `sig-local-structured-parsing-50x-cheaper` — data-eng

### [jones-autonomous-engineering-org.md](jones-autonomous-engineering-org.md)

477. `sig-block-90pct-adoption-no-impact` — ~90% of Block's 3,500 engineers used Goose/Claude Code regularly, yet the CEO saw no faster shipping
478. `sig-goose-mcp-reference-client` — Block built Goose before LLMs supported tool calling, design-partnered with Anthropic on the initial MCP release, and Goose became the MCP client reference i…
479. `sig-block-champions-metrics` — Three months after the 50-engineer AI-champions program made critical repos AI-ready (context/rules files, workflows, reviewers): AI-authored code +69%, repo…
480. `sig-block-review-bottleneck` — Multi-agent parallelism tripled/quadrupled PR volume and code review became the binding constraint
481. `sig-block-world-model-autonomy` — Block built a machine-readable world model over its 25,000 repos; Builder Bot and its delegated agents pull context from it, explore in parallel, and produce…
482. `sig-block-autonomy-then-layoffs` — The transformation arc ends in layoffs immediately after reaching stage-5 autonomy; the speaker asks openly whether enabling employees "to do the most incred…

### [jones-build-systems-not-code.md](jones-build-systems-not-code.md)

483. `sig-agent-design-is-swe` — Practitioner thesis: designing agentic systems exercises the same pre-genAI engineering disciplines
484. `sig-giant-prompt-code-smell` — The giant prompt is the agentic code smell: her Relocation Scout instructions accreted four distinct jobs (listing normalization, shortlist format, commute c…
485. `sig-dont-let-agents-design-agents` — She deliberately does NOT let her coding agent design her other agents: the output "technically works" but is unmaintainable (a giant prompt, concerns poorly…
486. `sig-retry-rewording-trap` — Agent retries carry a model-specific trap absent from classical systems: on retry, the model can reword the request just enough to register as a brand-new task

### [graziano-nearform-agents-building-agents.md](graziano-nearform-agents-building-agents.md)

487. `sig-autoagent-eval-selfimprovement` — AutoAgent took a naive Mastra hello-world agent from 18% → 83% eval pass rate in ~10 autonomous iterations, and lifted an already human-optimized production …
488. `sig-evals-gate-agents-building-agents` — The agents-building-agents loop is only safe because verification is externalized: golden datasets + scorers define success, and humans must explicitly forbi…
489. `sig-nearform-trace-clustering-loop` — Nearform's production cadence: collect traces with user thumbs-up/down + comments or SME annotations (114 traces in the shown example)
490. `sig-harness-engineering-precondition` — Graziano attributes the whole capability to Harness Engineering: a spec-driven environment (every failure mode becomes a spec), quality gates (lint, unit tes…

### [weitekamp-openprose-recursive-coding-agents.md](weitekamp-openprose-recursive-coding-agents.md)

491. `sig-rlm-small-beats-frontier` — On the LongCoT long-reasoning benchmark, a small laptop-runnable open model (captioned "Qwen 3.59B") run as an RLM beats Opus and GPT-5.4 run as plain LLMs
492. `sig-arc-agi3-too-hot-to-benchmark` — Within hours of ARC-AGI-3's release, Symbolica's Agentica RLM harness posted ~30% vs ~2–3% for all frontier models
493. `sig-mismanaged-geniuses` — Thesis signal: today's agents are "mismanaged geniuses" (framing from Alex Zhang / Omar Khattab, MIT
494. `sig-claude-code-becomes-rlm` — Claude Code's dynamic workflows made the most-used coding agent capable of recursive, model-chosen decomposition
495. `sig-golden-session-capture` — OpenProse can take a "golden session" (an unusually good agent run) from Claude Code, Codex, or Pi and have the agent deconstruct it into a reusable .prose.m…

### [sehgal-omnara-log-is-the-agent.md](sehgal-omnara-log-is-the-agent.md)

496. `sig-log-is-agent-thesis` — Thesis: the agent is not the model or the runtime — it is the log; model, tools, and runtime merely read from and append to it
497. `sig-harness-state-is-an-afterthought` — Current harnesses treat the log as exhaust: Claude Code and Codex write messy JSONL to local disk with fire-and-forget writes even in SDK mode (a failed writ…
498. `sig-log-lockin-managed-agents` — Ownership warning: the deepest lock-in is log lock-in — models can be swapped and APIs wrapped, but whoever owns your log owns your agent
499. `sig-log-portability` — With a log-first architecture, forking and migration become structural: branch the log and run branches on Claude, GPT, and open models to explore different …

### [gupta-meta-production-evals.md](gupta-meta-production-evals.md)

500. `sig-benchmark-prod-gap-widens` — harness
501. `sig-evals-become-control-plane` — infra
502. `sig-prod-traffic-is-eval-data` — harness

### [thomas-miranda-hypothesis-persona-evals.md](thomas-miranda-hypothesis-persona-evals.md)

503. `sig-persona-evals-miss-dominant-failure` — harness
504. `sig-composite-overwrites-record` — training
505. `sig-alignment-amplifies-composite` — training
506. `sig-generalist-beats-persona-finetune` — training
507. `sig-persona-is-configuration` — context

### [de-mesa-opengov-og-assist.md](de-mesa-opengov-og-assist.md)

508. `sig-opengov-owns-agent-loop` — Production migration off a framework: OpenGov's agents team started on LangGraph, outgrew it as the team scaled and use cases evolved, and rebuilt a bespoke …
509. `sig-a2a-as-internal-contract` — A2A adopted not for cross-org agent interop but as an internal spec: agent cards model OpenGov's agent routes, and the protocol's rigor is valued as the cont…
510. `sig-agent-layer-across-erp` — An incumbent vertical-SaaS vendor (government ERP) ships one agent surface across its entire product line, with every product team contributing tools and ski…
511. `sig-approval-gates-and-sandboxes` — Production safety posture: the agent loop is deterministically interrupted whenever a tool call requires approval
512. `sig-ci-evals-on-real-completions` — "Shipping is the start, not the finish" (paraphrase): iteration engine is user thumbs-up/thumbs-down feedback plus automated evals running in CI against real…

### [hanchett-aws-spec-driven-development.md](hanchett-aws-spec-driven-development.md)

513. `sig-aws-productizes-spec-driven` — AWS watched teams and customers vibe-coding into bad outputs and hand-rolling a bespoke fix
514. `sig-models-still-need-specs` — Vendor answer to "can't the latest frontier models just do everything?": no — models improve every release, and harnesses are adding thinking/planning modes,…
515. `sig-accountability-stays-human` — "Everything in the spec-driven development flow is you": the developer is the code reviewer of all generated code and the interactive editor of the requireme…
516. `sig-property-tests-enter-agent-flow` — Kiro's spec flow generates property-based tests tied to the requirements and design documents (fast-check
517. `sig-mcp-dead-claims-premature` — Hype-cycle whiplash datum: barely months after launch, "isn't MCP 6 months old and it's dead now?" is a question a vendor advocate must rebut on stage (the C…

### [razgaitis-higharc-research-to-reality.md](razgaitis-higharc-research-to-reality.md)

518. `sig-handoff-is-the-bottleneck` — infra
519. `sig-repos-built-for-agent-navigation` — context
520. `sig-vertical-pulls-full-ai-stack` — —

### [russo-heygen-html-all-agents-need.md](russo-heygen-html-all-agents-need.md)

521. `sig-hyperframes-open-source-scale` — Hyperframes HTML-to-video running at scale: speaker-reported 1.3M videos rendered by open-source users in the last 90 days, 267k creators, ~15k videos/day, 3…
522. `sig-heygen-thinnest-wrapper-won` — A year of format experiments ended with the thinnest wrapper winning: After Effects/Premiere are great-output but agent-hostile
523. `sig-html-new-markdown-convergence` — Independent industry convergence on HTML as the LLM visual-output format: Karpathy and Thariq [Shihipar?
524. `sig-models-weak-at-creative-craft` — Practitioner honesty: models still aren't good at creative work even in their native format

### [kapoor-nori-html-for-graphics.md](kapoor-nori-html-for-graphics.md)

525. `sig-nori-html-artifacts-production` — Nori runs its real artifacts as agent-written HTML in production: actual board decks, sales decks, docs, and marketing videos ("literally just divs all the w…
526. `sig-pelican-svg-vs-html` — Same model, same pelican, different medium: frontier models fail Willison's SVG pelican test (a wall of numbers no human could handwrite either), but asked f…
527. `sig-canvas-tools-fail-agents` — Handing agents human canvas tools fails structurally: PowerPoint/Slides/Figma/Canva are built for human hands and eyes (click, drag, snap-to-grid) with data …

### [raj-ark-browser-agents-better-eyes.md](raj-ark-browser-agents-better-eyes.md)

528. `sig-browser-agents-adoption-gap` — Practitioner: browser agents are barely adopted despite the excitement — the speaker doesn't use them himself
529. `sig-compressed-page-token-math` — The representation numbers: full DOM ≈ 20k tokens; a screenshot ≈ 1.1k tokens but shows only one snippet
530. `sig-page-state-diff-feedback` — Environment feedback as the fix for long sequences: the harness tracks page state end-to-end and tells the agent what just appeared, what disappeared, that t…

### [shaikh-rastogi-prosodica-100-tool-trap.md](shaikh-rastogi-prosodica-100-tool-trap.md)

531. `sig-fat-agent-accuracy-collapse` — Benchmarked decay of the "fat agent" (every tool schema in every prompt): ~78% tool-selection accuracy at 10 tools → ~40% at 100 → 13.6% at 741 (roughly one …
532. `sig-fat-agent-token-latency-tax` — The catalog is a per-request tax: 741 tool schemas ≈ 127k tokens before the user's question is even considered
533. `sig-semantic-router-holds-83` — Same queries, same model, same catalog, routed: retrieving top-K tools by embedding similarity holds accuracy above 83% flat across catalog sizes, with ~1k t…
534. `sig-jit-tool-loading-ecosystem` — Ecosystem converging on on-demand tool loading: Anthropic's published MCP write-up reports 150k → 2k tokens (98.7% reduction) from on-demand tool loading

### [martin-dye-tone-layering.md](martin-dye-tone-layering.md)

535. `sig-tone-prompt-fails-turn-21` — Voice-is-the-product operator (wedding venues; same class as luxury hotels, high-end real estate): the standard advice
536. `sig-warm-voice-invented-dates` — The failure that forced a deterministic layer: the venue AI kept warmly offering wedding dates that were already booked
537. `sig-multitenant-default-identity-leak` — Shipped multi-tenant bug: silently defaulted brand-identity fields made every venue's agent email as sage@[the flagship venue's domain]
538. `sig-ai-disclosure-first-message` — Product bet on disclosure: every Bloom agent states it is an AI in its very first response
