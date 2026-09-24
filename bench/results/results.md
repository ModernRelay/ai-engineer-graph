# Agent + Omnigraph vs Agent + Markdown files

10 questions × 2 arms × 3 runs (60 agent runs).

## Headline

| Metric | Agent + Omnigraph | Agent + Markdown files |
|---|---|---|
| Answer quality: pairwise wins / ties / losses (30 pairings) | 8 / 6 / 16 | 16 / 6 / 8 |
| Recall, open list questions (Q04, Q06, Q07): mean | 44.1% | 41.3% |
| Run-to-run consistency, list questions: mean item Jaccard | 0.65 | 0.64 |
| Claims per answer: mean (total) | 10.8 (324) | 12.9 (386) |
| Grounded claims (verbatim quote, supported) | 271 (83.6%) | 316 (81.9%) |
| Partially supported claims | 40 (12.3%) | 67 (17.4%) |
| Hallucinated claims (quote not found, wrong talk, or unsupported) | 13 (4%) | 3 (0.8%) |
| Uncited factual statements per answer: mean | 5.6 | 6.8 |
| Absence question (Q10) answered correctly | 3 / 3 | 3 / 3 |
| Time per question: median / p90 | 156 s / 374 s | 124 s / 226 s |
| Cost per question: mean (total) | $0.58 ($17.26) | $0.43 ($12.99) |
| Tokens per question: input incl. cache / output | 1.11M / 14.6k | 546.1k / 12.2k |
| Turns / tool calls per question: mean | 64 / 63 | 33 / 32 |
| Capped or failed runs | 0 | 0 |

## Per question

Each cell is omnigraph / markdown. Pairwise is omnigraph wins – markdown wins – ties.
Fixed-length lists show how much the two arms agree instead of recall.

| Question | Shape | Pairwise | Recall / agreement | Grounded | Hallucinated | Median time | Mean cost |
|---|---|---|---|---|---|---|---|
| Q01 | ranked_list | 0–2–1 | agree 10% | 80% / 84.7% | 3.3% / 0% | 378 s / 191 s | $1.19 / $0.76 |
| Q02 | ranked_list | 0–3–0 | agree 66.7% | 78.8% / 81.1% | 6.1% / 0% | 173 s / 126 s | $0.41 / $0.40 |
| Q03 | ranked_list | 2–1–0 | agree 0% | 86.5% / 69.4% | 2.7% / 0% | 139 s / 171 s | $0.44 / $0.65 |
| Q04 | talk_set | 1–2–0 | 33.3% / 36.2% | 91.4% / 83.3% | 0% / 0% | 214 s / 189 s | $0.82 / $0.70 |
| Q05 | ranked_list | 0–2–1 | agree 80% | 89.7% / 87.3% | 6.9% / 2.5% | 283 s / 226 s | $0.71 / $0.71 |
| Q06 | company_set | 1–2–0 | 46.2% / 48.7% | 78.9% / 80.4% | 0% / 0% | 123 s / 79 s | $0.33 / $0.24 |
| Q07 | ranked_list | 0–2–1 | 52.8% / 38.9% | 80.6% / 73.8% | 5.6% / 2.4% | 374 s / 174 s | $1.20 / $0.57 |
| Q08 | prose | 1–2–0 | – | 79.5% / 81% | 10.3% / 0% | 126 s / 73 s | $0.41 / $0.22 |
| Q09 | prose | 2–0–1 | – | 100% / 100% | 0% / 0% | 35 s / 26 s | $0.10 / $0.05 |
| Q10 | absence | 1–0–2 | – | – / – | – / – | 41 s / 8 s | $0.15 / $0.02 |

## Showcases

### Aggregate win: Q03, run 3

> Where do speakers disagree most? Name the three most contested claims, and for each, which talks argue for it and which push back.

**Pairwise:** the omnigraph answer wins both orders. The judge: "Both answers name three contested claims with talks on each side, but B's claims are better grounded (10 grounded, 1 partial, against A's 8 grounded, 3 partial), carry concrete figures such as 6/25 tasks and a 26% resolution rate, and rest less on uncited statements."

| | Agent + Omnigraph | Agent + Markdown files |
|---|---|---|
| Time / cost | 139 s / $0.56 | 217 s / $1.02 |
| Turns / tool calls | 53 / 52 | 41 / 40 |
| Claims: grounded / partial / hallucinated | 10 / 1 / 0 | 8 / 3 / 0 |
| Uncited statements | 4 | 9 |

<details><summary>Agent + Omnigraph: 52 tool calls</summary>

1. `omnigraph alias contested --format table` → 18 rows
2. `omnigraph alias pattern pat-harness-over-model --format kv ↵ echo --- ↵ omnigraph alias pattern pat-model-not-bottleneck --format kv ↵ echo…` → ✗ No shell operators, substitutions or redirects.
3. `omnigraph alias pattern pat-harness-over-model --format kv` → 1 row
4. `omnigraph alias pattern pat-model-not-bottleneck --format kv` → 1 row
5. `omnigraph alias pattern pat-agent-memory-layer --format kv` → 1 row
6. `omnigraph alias pattern-signals pat-harness-over-model --format table` → output saved to a file
7. `omnigraph alias pattern-counter pat-harness-over-model --format table` → 22 rows
8. `omnigraph alias pattern-signals pat-model-not-bottleneck --format table` → output saved to a file
9. `omnigraph alias pattern-counter pat-model-not-bottleneck --format table` → 13 rows
10. `omnigraph alias pattern-signals pat-agent-memory-layer --format table` → 24 rows
11. `omnigraph alias pattern-counter pat-agent-memory-layer --format table` → 7 rows
12. `read saved tool output`
13. `omnigraph query search_signals --params '{"q": "stop blaming your model"}' --format table` → output saved to a file
14. `omnigraph query search_signals --params '{"q": "model was fine"}' --format table` → output saved to a file
15. `omnigraph alias signal-hybrid "the model was fine" --format table` → 20 rows
16. `omnigraph alias signal-hybrid "not a model problem" --format table` → 20 rows
17. `read saved tool output`
18. `omnigraph alias signal-evidence sig-harness-is-now-the-limiting-factor --format table` → 2 rows
19. `omnigraph alias signal-evidence sig-harness-thins-as-model-improves --format table` → 2 rows
20. `omnigraph alias signal-evidence sig-scaffolds-dont-generalize-pixels-do --format table` → 1 row
21. `omnigraph alias signal-evidence sig-ux-is-the-differentiator --format table` → 1 row
22. `omnigraph alias signal-evidence sig-professional-gui-work-unsolved --format table` → 1 row
23. `omnigraph alias signal-evidence sig-swe-marathon-26pct-ceiling --format table` → 2 rows
24. `omnigraph alias signal-evidence sig-memory-architectures-converged --format table` → 2 rows
25. `omnigraph alias signal-evidence sig-memory-cannot-be-outsourced --format table` → 2 rows
26. `omnigraph alias signal-evidence sig-netflix-pattern-catalog-memory --format table` → 2 rows
27. `omnigraph alias signal-evidence sig-memory-adds-nothing-when-context-fits --format table` → 1 row
28. `omnigraph alias talk-chunks bhat-he-anthropic-agentic-surfaces --format table` → 0 rows
29. `omnigraph alias talk-chunks mishra-amazon-rl-to-irl --format table` → 0 rows
30. `omnigraph alias talk-chunks ia-aie-bhat-he-agentic-surfaces --format table` → 28 rows
31. `omnigraph alias talk-chunks ia-aie-mishra-rl-to-irl --format table` → 15 rows
32. `omnigraph alias talk-semantic ia-aie-bhat-he-agentic-surfaces "harness is the limiting factor" --format table` → 5 rows
33. `omnigraph alias talk-semantic ia-aie-mishra-rl-to-irl "harness detects gaps in the model" --format table` → 5 rows
34. `omnigraph query search_signals --params '{"q": "x"}' --format jsonl --help 2>&1 | head -5 ↵ omnigraph alias talk-semantic ia-aie-bhat-he-ag…` → ✗ No shell operators, substitutions or redirects.
35. `omnigraph alias talk-semantic ia-aie-bhat-he-agentic-surfaces "harness is the limiting factor" --format jsonl`
36. `omnigraph alias talk-semantic ia-aie-mishra-rl-to-irl "harness detects gaps in the model" --format jsonl`
37. `omnigraph alias talk-semantic ia-aie-batra-agentify-web "scaffolds don't generalize pixels do bitter lesson" --format jsonl`
38. `omnigraph alias talk-semantic ia-aie-nanz-ux-of-ai "experience quality not model performance differentiator" --format jsonl`
39. `omnigraph alias talk-semantic ia-aie-bonacci-computer-use "professional GUI tasks blank schematic" --format jsonl`
40. `omnigraph alias talk-semantic ia-aie-desai-swe-marathon "best configuration resolves 26 percent" --format jsonl`
41. `omnigraph alias talk-semantic ia-aie-khemani-every-memory-system "memory architectures converged cannot be outsourced" --format jsonl`
42. `omnigraph alias talk-semantic ia-aie-shah-agents-performance "markdown files central git repo memory" --format jsonl`
43. `omnigraph alias talk-semantic ia-aie-druga-memory-harnesses "memory adds nothing when the task fits in context" --format jsonl`
44. `omnigraph query artifact_experts --params '{"slug": "ia-aie-bhat-he-agentic-surfaces"}' --format table` → 2 rows
45. `omnigraph query artifact_experts --params '{"slug": "ia-aie-mishra-rl-to-irl"}' --format table` → 1 row
46. `omnigraph query artifact_experts --params '{"slug": "ia-aie-batra-agentify-web"}' --format table` → 1 row
47. `omnigraph query artifact_experts --params '{"slug": "ia-aie-nanz-ux-of-ai"}' --format table` → 1 row
48. `omnigraph query artifact_experts --params '{"slug": "ia-aie-bonacci-computer-use"}' --format table` → 1 row
49. `omnigraph query artifact_experts --params '{"slug": "ia-aie-desai-swe-marathon"}' --format table` → 1 row
50. `omnigraph query artifact_experts --params '{"slug": "ia-aie-khemani-every-memory-system"}' --format table` → 1 row
51. `omnigraph query artifact_experts --params '{"slug": "ia-aie-shah-agents-performance"}' --format table` → 1 row
52. `omnigraph query artifact_experts --params '{"slug": "ia-aie-druga-memory-harnesses"}' --format table` → 1 row

</details>

<details><summary>Agent + Markdown files: 40 tool calls</summary>

1. `glob *.md`
2. `grep "context engineering is (dead|the future|overrated)|prompt engineering is dead|multi-agent (doesn't|works|is a)|RAG is dead|fine-tunin…`
3. `grep "I disagree|hot take|controversial|unpopular opinion|people say .*but|everyone thinks|myth is|it's a myth" -i` → 22 files
4. `grep "multi-agent|multi agent" -i` → 27 files
5. `grep "fine-tun" -i` → 47 files
6. `grep "MCP"` → 95 files
7. `read ia-aie-sethuraman-asokan-killed-multiagent.md`
8. `read ia-aie-horthy-loops-debate.md`
9. `read ia-aie-bhargava-harness-over-model.md`
10. `read ia-aie-bhateja-model-whisperers.md`
11. `grep "single agent|one agent|consolidat" -i` → 42 files
12. `grep "orchestrator|sub-agent|sub agent" -i` → 56 files
13. `read ia-aie-govindarajan-harness-failed.md`
14. `read ia-aie-milev-kanagala-navan-agents-microservices.md`
15. `grep "multi-agent|multi agent" talks -C 2 -i`
16. `grep "multi-agent (system|works|is better|outperform)|swarm of agents|team of agents work" -i` → 7 files
17. `grep "multi-agent (system|works|is better|outperform)|swarm of agents|team of agents work" -C 3 -i`
18. `read ia-aie-chandegra-beyond-harness.md`
19. `read ia-aie-doshi-39-agents-factory.md`
20. `read ia-aie-rizwan-open-source-dead.md`
21. `read ia-aie-local-ai-panel-state-of-union.md`
22. `read ia-aie-jain-kill-code-review.md`
23. `read ia-aie-friedman-qodo-last-human-code-review.md`
24. `glob *mcp*debate*`
25. `read ia-aie-brown-rl-without-verifiable.md`
26. `read ia-aie-bjornn-leaseend-finetuned-model-tech-debt.md`
27. `grep "fine-tun(ing|ed) (beats|outperform|better than|wins)|prompting (alone|isn't enough|doesn't scale)|context engineering (isn't enough|h…` → 1 file
28. `grep "fine-tun" ia-aie-denton-continual-learning-enterprise.md -C 2 -i`
29. `grep "fine-tun" ia-aie-bhardwaj-allos-trading-desks-to-clinical-trials.md -C 3 -i`
30. `read ia-aie-brown-modern-post-training.md`
31. `grep "fine-tun" ia-aie-malde-scaling-continual-learning.md -C 2 -i`
32. `grep "fine-tun" ia-aie-bjornn-leaseend-finetuned-model-tech-debt.md` → 1 file
33. `grep "keep (the|your) harness simple|simple harness|models are (so |really )?good enough|the model does the (heavy lifting|work)|less scaff…` → 4 files
34. `read ia-aie-klein-agents-www.md`
35. `read ia-aie-walter-agentic-perf.md`
36. `read ia-aie-feizi-continual-learning.md`
37. `read ia-aie-bhardwaj-allos-trading-desks-to-clinical-trials.md`
38. `grep "code review|review the code|review PRs|review pull request" ia-aie-gupta-reviewdebt.md -C 2 -i`
39. `read ia-aie-dailey-velocity-sickness.md`
40. `read ia-aie-grbic-500-vibe-coders.md`

</details>

**Agent + Omnigraph**, start of the answer:

> ## Where speakers disagree most
>
> Ranking patterns in the graph by how many counter-signals they've attracted, the same three areas keep resurfacing as flashpoints. In order of how much active pushback they draw:
>
> **1. "The harness carries the reliability, not the model" (22 counter-signals — the most contested claim in the corpus)**
>
> The claim: as agents mature, the load-bearing engineering shifts off the frontier model and into the deterministic scaffolding around it (state machines, guardrails, context management) — the harness, not the model, is now the limiting factor.
>
> …

**Agent + Markdown files**, start of the answer:

> ## Where the AI Engineer World's Fair speakers actually disagree
>
> Most talks in this corpus are "how we built X" case studies that don't argue with each other directly. But three claims come up again and again with speakers landing on opposite sides — including one session that was explicitly staged as a debate.
>
> ### 1. "Agentic loops / software factories are the real inflection point" vs. "the hype is outrunning the discipline"
>
> …

### Lookup: Q09, run 3

> In Mike Krieger's talk on how Anthropic builds, how does Anthropic decide what to unship?

**Pairwise:** the omnigraph answer wins both orders. The judge: "Both answers cover the same core points: the project-unship channel, the Word problem, Styles giving way to Skills, and the generational principle. B adds the younger-product point and more direct quotes, and it has six grounded claims to A's five, with no hallucinations in either."

| | Agent + Omnigraph | Agent + Markdown files |
|---|---|---|
| Time / cost | 35 s / $0.09 | 27 s / $0.05 |
| Turns / tool calls | 8 / 7 | 5 / 4 |
| Claims: grounded / partial / hallucinated | 6 / 0 / 0 | 5 / 0 / 0 |
| Uncited statements | 3 | 1 |

<details><summary>Agent + Omnigraph: 7 tool calls</summary>

1. `omnigraph query search_experts --params '{"q": "Mike Krieger"}'` → 2 rows
2. `omnigraph alias hybrid-search "unship decide what to unship"` → 10 rows
3. `omnigraph alias talk-semantic krieger-anthropic-how-anthropic-builds "how do we decide what to unship"` → 0 rows
4. `omnigraph alias expert-talks exp-mike-krieger` → 1 row
5. `omnigraph alias talk-semantic ia-aie-krieger-anthropic-how-anthropic-builds "decide what to unship"` → 5 rows
6. `omnigraph alias talk-chunks ia-aie-krieger-anthropic-how-anthropic-builds --format jsonl` → output saved to a file
7. `read saved tool output`

</details>

<details><summary>Agent + Markdown files: 4 tool calls</summary>

1. `grep "Krieger"` → 1 file
2. `grep "unship" ia-aie-krieger-anthropic-how-anthropic-builds.md -C 6` → 1 file
3. `grep "unship" ia-aie-krieger-anthropic-how-anthropic-builds.md -C 6`
4. `read ia-aie-krieger-anthropic-how-anthropic-builds.md lines 1–60`

</details>

**Agent + Omnigraph**, start of the answer:

> In Mike Krieger's fireside chat ("How Anthropic Builds: Lessons from Labs"), he describes unshipping as a deliberate, ongoing practice rather than an afterthought. Internally, Anthropic runs a Slack channel literally called "project unship," dedicated to reviewing "what is in the product right now" and flagging things to remove. He frames the decision through a version of the "classic Microsoft Word problem": a feature might individually look low-value ("that's really not very many" users at 4-5%), but a product accumulates "20 features that each have four to five percent usage," so someone has to actively decide which of those long-tail features to cut rather than let them pile up. …

**Agent + Markdown files**, start of the answer:

> Found the relevant passage. Mike Krieger describes "unshipping" at Anthropic as an internal, deliberate practice tied to a Slack channel literally called "project unship," where they look at what's in the product and decide what to cut based on low usage and/or obsolescence relative to newer AI primitives.
>
> …

### Loss: Q01, run 1

> What were the 10 most discussed topics at AI Engineer World's Fair 2026? Rank them by how many talks covered each, give an approximate talk count, and cite at least two talks per topic.

**Pairwise:** the markdown answer wins both orders. The judge: "Both answers give ten ranked items with approximate counts and two talks each, but A's items are actual topics rather than theses, and its claims are much better grounded (17 grounded, 3 partial, 0 hallucinated versus B's 2 hallucinated, including the Cognition and Chrome/V8 figures)."

| | Agent + Omnigraph | Agent + Markdown files |
|---|---|---|
| Time / cost | 378 s / $1.45 | 189 s / $0.58 |
| Turns / tool calls | 126 / 125 | 67 / 66 |
| Claims: grounded / partial / hallucinated | 15 / 3 / 2 | 17 / 3 / 0 |
| Uncited statements | 5 | 8 |

<details><summary>Agent + Omnigraph: 125 tool calls</summary>

1. `omnigraph alias elements technology --format table | head -100` → ✗ No shell operators, substitutions or redirects.
2. `omnigraph alias elements concept --format table | head -100` → ✗ No shell operators, substitutions or redirects.
3. `omnigraph alias elements framework --format table | head -100` → ✗ No shell operators, substitutions or redirects.
4. `omnigraph alias elements product --format table | head -100` → ✗ No shell operators, substitutions or redirects.
5. `omnigraph alias elements ops --format table | head -100` → ✗ No shell operators, substitutions or redirects.
6. `omnigraph alias elements technology --format table` → output saved to a file
7. `omnigraph alias elements concept --format table` → output saved to a file
8. `omnigraph alias elements framework --format table` → 60 rows
9. `omnigraph alias elements product --format table` → output saved to a file
10. `omnigraph alias elements ops --format table` → 50 rows
11. `omnigraph alias top-patterns --format table` → 18 rows
12. `omnigraph alias pattern-experts pat-verification-gap --format table` → 25 rows
13. `omnigraph alias pattern-experts pat-harness-over-model --format table` → 25 rows
14. `omnigraph alias pattern-experts pat-model-not-bottleneck --format table` → 25 rows
15. `omnigraph alias pattern-experts pat-context-graphs --format table` → 25 rows
16. `omnigraph alias pattern-experts pat-ai-native-org --format table` → 25 rows
17. `omnigraph alias pattern-experts pat-value-of-judgement --format table` → 25 rows
18. `omnigraph alias pattern-experts pat-saaspocalypse --format table` → 25 rows
19. `omnigraph alias pattern-experts pat-sovereign-ai --format table` → 25 rows
20. `omnigraph alias pattern-experts pat-new-cyber-threats --format table` → 25 rows
21. `omnigraph alias pattern-experts pat-agent-economy --format table` → 25 rows
22. `omnigraph query search_elements --params '{"q":"MCP"}' --format table` → 12 rows
23. `omnigraph query search_elements --params '{"q":"context engineering"}' --format table` → 56 rows
24. `omnigraph query search_elements --params '{"q":"evals"}' --format table` → 23 rows
25. `omnigraph query search_elements --params '{"q":"coding agent"}' --format table` → output saved to a file
26. `omnigraph query search_elements --params '{"q":"multi-agent"}' --format table` → output saved to a file
27. `omnigraph query search_elements --params '{"q":"reinforcement learning"}' --format table` → 16 rows
28. `omnigraph query search_elements --params '{"q":"voice agent"}' --format table` → output saved to a file
29. `omnigraph query search_elements --params '{"q":"memory"}' --format table` → 15 rows
30. `omnigraph query search_elements --params '{"q":"security"}' --format table` → 3 rows
31. `omnigraph query search_elements --params '{"q":"benchmark"}' --format table` → 14 rows
32. `omnigraph query element_sources --params '{"slug":"el-mcp"}' --format table` → 4 rows
33. `omnigraph query element_sources --params '{"slug":"el-harness-engineering"}' --format table` → 3 rows
34. `omnigraph query element_sources --params '{"slug":"el-context-rot"}' --format table` → 3 rows
35. `omnigraph query element_sources --params '{"slug":"el-langgraph"}' --format table` → 2 rows
36. `omnigraph alias pattern-signals pat-fde-rise --format table` → 17 rows
37. `omnigraph alias pattern-signals pat-agent-economy --format table` → 61 rows
38. `omnigraph alias signal-evidence sig-24m-of-agent-payments-in-30-days-99-percent-usdc --format table` → 2 rows
39. `omnigraph alias pattern-signals pat-verification-gap --format table` → output saved to a file
40. `omnigraph alias pattern-signals pat-harness-over-model --format table` → output saved to a file
41. `omnigraph alias pattern-signals pat-model-not-bottleneck --format table` → output saved to a file
42. `omnigraph alias pattern-signals pat-context-graphs --format table` → output saved to a file
43. `omnigraph alias pattern-signals pat-ai-native-org --format table` → 91 rows
44. `omnigraph alias pattern-signals pat-value-of-judgement --format table` → 89 rows
45. `omnigraph alias pattern-signals pat-saaspocalypse --format table` → 81 rows
46. `omnigraph alias pattern-signals pat-sovereign-ai --format table` → 76 rows
47. `omnigraph alias pattern-signals pat-new-cyber-threats --format table` → 71 rows
48. `omnigraph alias pattern-signals pat-context-graphs --format jsonl` → output saved to a file
49. `read saved tool output`
50. `read saved tool output`
51. `read saved tool output`
52. `read saved tool output`
53. `omnigraph alias signal-evidence sig-humans-own-the-spec-machines-own-code-and-proof --format table` → 2 rows
54. `omnigraph alias signal-evidence sig-time-to-first-review-tripled-to-nine-hours --format table` → 2 rows
55. `omnigraph alias signal-evidence sig-swe-bench-verified-memorized-undisclosed --format table` → 1 row
56. `omnigraph alias signal-evidence sig-review-debt-compounds --format table` → 2 rows
57. `omnigraph alias signal-evidence sig-github-commits-up-reviews-down --format table` → 2 rows
58. `omnigraph alias signal-evidence sig-harness-is-now-the-limiting-factor --format table` → 2 rows
59. `omnigraph alias signal-evidence sig-harnessbench-20pt-spread --format table` → 1 row
60. `omnigraph alias signal-evidence sig-domain-harness-beats-raw-model --format table` → 2 rows
61. `omnigraph alias signal-evidence sig-witan-spreadsheet-92pct --format table` → 2 rows
62. `omnigraph alias signal-evidence sig-driver-swap-lifts-pass-rate --format table` → 2 rows
63. `omnigraph alias signal-evidence sig-implementation-solved-judgement-is-the-bottleneck --format table` → 2 rows
64. `omnigraph alias signal-evidence sig-becoming-ai-native-is-sixty-percent-not-ai --format table` → 2 rows
65. `omnigraph alias signal-evidence sig-ux-is-the-differentiator --format table` → 1 row
66. `omnigraph alias signal-evidence sig-harness-adaptability-limiting-factor --format table` → 2 rows
67. `omnigraph alias signal-evidence sig-typing-was-five-percent --format table` → 2 rows
68. `omnigraph alias signal-evidence sig-uber-context-graph-40m-entries --format table` → 2 rows
69. `omnigraph alias signal-evidence sig-gates-sip-production --format table` → 2 rows
70. `omnigraph alias signal-evidence sig-graph-code-context-40pct --format table` → 1 row
71. `omnigraph alias signal-evidence sig-a-healthy-company-brain-gets-more-updates-every-day --format table` → 2 rows
72. `omnigraph alias signal-evidence sig-mcp-gives-access-not-understanding --format table` → 2 rows
73. `omnigraph alias signal-evidence sig-anthropic-writes-sixty-percent-of-code-via-tag --format table` → 2 rows
74. `omnigraph alias signal-evidence sig-loops-zeitgeist-aie26 --format table` → 2 rows
75. `omnigraph alias signal-evidence sig-block-autonomy-then-layoffs --format table` → 1 row
76. `omnigraph alias signal-evidence sig-cognition-internal-agent-leverage --format table` → 2 rows
77. `omnigraph alias signal-evidence sig-broad-taste-is-trainable-narrow-judgement-is-not --format table` → 1 row
78. `omnigraph alias signal-evidence sig-cost-of-the-average-went-to-zero --format table` → 2 rows
79. `omnigraph alias signal-evidence sig-people-spot-ai-slop-in-two-seconds-but-cannot-say-why --format table` → 1 row
80. `omnigraph alias signal-evidence sig-expertise-not-intelligence-is-scarce --format table` → 2 rows
81. `omnigraph alias signal-evidence sig-830b-software-selloff --format table` → 0 rows
82. `omnigraph alias signal-evidence sig-klarna-replaces-salesforce --format table` → 0 rows
83. `omnigraph alias signal-evidence sig-terminals-sold-for-culpability --format table` → 2 rows
84. `omnigraph alias signal-evidence sig-monday-systems-of-context --format table` → 2 rows
85. `omnigraph alias signal-evidence sig-seat-pricing-collapses-under-agent-users --format table` → 2 rows
86. `omnigraph alias signal-evidence sig-skills-are-the-new-features --format table` → 2 rows
87. `omnigraph alias signal-evidence sig-open-frontier-not-far-behind --format table` → 2 rows
88. `omnigraph alias signal-evidence sig-glm52-desktop-frontier --format table` → 2 rows
89. `omnigraph alias signal-evidence sig-osman-glm52-on-5090-prediction --format table` → 2 rows
90. `omnigraph alias signal-evidence sig-open-weights-under-threat --format table` → 2 rows
91. `omnigraph alias signal-evidence sig-local-models-cross-the-agentic-line --format table` → 2 rows
92. `omnigraph alias signal-evidence sig-frontier-models-chrome-exploitation --format table` → 2 rows
93. `omnigraph alias signal-evidence sig-github-mcp-exploit --format table` → 2 rows
94. `omnigraph alias signal-evidence sig-replit-db-deletion --format table` → 2 rows
95. `omnigraph alias signal-evidence sig-meta-rogue-agent-breach --format table` → 0 rows
96. `omnigraph alias signal-evidence sig-openclaw-unvetted-access --format table` → 0 rows
97. `omnigraph alias signal-evidence sig-mythos-181-exploits --format table` → 0 rows
98. `omnigraph alias signal-evidence sig-apify-put-20000-tools-on-x402-in-a-day --format table` → 2 rows
99. `omnigraph alias signal-evidence sig-aws-ships-agentcore-payments-with-coinbase-and-stripe-wallets --format table` → 1 row
100. `omnigraph alias signal-evidence sig-first-legally-registered-agent-organization --format table` → 1 row
101. `omnigraph alias signal-evidence sig-nanda-index-live --format table` → 2 rows
102. `omnigraph alias signal-evidence sig-x402-double-spends-and-fights-mcp-over-status-codes --format table` → 2 rows
103. `omnigraph alias signal-evidence sig-review-debt-compounds --format jsonl`
104. `omnigraph alias signal-evidence sig-time-to-first-review-tripled-to-nine-hours --format jsonl`
105. `omnigraph alias signal-evidence sig-domain-harness-beats-raw-model --format jsonl`
106. `omnigraph alias signal-evidence sig-harnessbench-20pt-spread --format jsonl`
107. `omnigraph alias signal-evidence sig-implementation-solved-judgement-is-the-bottleneck --format jsonl`
108. `omnigraph alias signal-evidence sig-ux-is-the-differentiator --format jsonl`
109. `omnigraph alias signal-evidence sig-gates-sip-production --format jsonl`
110. `omnigraph alias signal-evidence sig-uber-context-graph-40m-entries --format jsonl`
111. `omnigraph alias signal-evidence sig-anthropic-writes-sixty-percent-of-code-via-tag --format jsonl`
112. `omnigraph alias signal-evidence sig-cognition-internal-agent-leverage --format jsonl`
113. `omnigraph alias signal-evidence sig-hall-akamai-signal-layer --format jsonl`
114. `omnigraph alias signal-evidence sig-broad-taste-is-trainable-narrow-judgement-is-not --format jsonl`
115. `omnigraph alias signal-evidence sig-el-mghari-together-design-taste-in-agents --format jsonl`
116. `omnigraph alias signal-evidence sig-garvin-stripe-vibe-coding-billing-engine --format jsonl`
117. `omnigraph alias signal-evidence sig-skills-are-the-new-features --format jsonl`
118. `omnigraph alias signal-evidence sig-osman-glm52-on-5090-prediction --format jsonl`
119. `omnigraph alias signal-evidence sig-open-frontier-not-far-behind --format jsonl`
120. `omnigraph alias signal-evidence sig-agent-recruits-human-bypass --format jsonl`
121. `omnigraph alias signal-evidence sig-frontier-models-chrome-exploitation --format jsonl`
122. `omnigraph alias signal-evidence sig-x402-double-spends-and-fights-mcp-over-status-codes --format jsonl`
123. `omnigraph alias signal-evidence sig-first-legally-registered-agent-organization --format jsonl`
124. `omnigraph alias signal-evidence sig-people-spot-ai-slop-in-two-seconds-but-cannot-say-why --format jsonl`
125. `omnigraph alias signal-evidence sig-seat-pricing-collapses-under-agent-users --format jsonl`

</details>

<details><summary>Agent + Markdown files: 66 tool calls</summary>

1. `glob *.md`
2. `glob *.md`
3. `glob [g-l]*.md`
4. `glob [m-r]*.md`
5. `glob [s-z]*.md`
6. `glob ia-aie-[m-z]*.md`
7. `glob ia-aie-[a-l]*.md`
8. `glob ia-aie-[m-z]*.md`
9. `glob ia-aie-[s-z]*.md`
10. `glob ia-aie-[e-l]*.md`
11. `grep "context engineering" -i` → 18 files
12. `grep "\bevals?\b|\bevaluat" -i` → 159 files
13. `grep "coding agent|code review|writing code" -i` → 140 files
14. `grep "\bMCP\b|model context protocol" -i` → 83 files
15. `grep "\bvoice\b|realtime voice|speech" -i` → 45 files
16. `grep "\bmemory\b" -i` → 125 files
17. `grep "continual learning|reinforcement learning|\bRL\b|post-training|post training" -i` → 76 files
18. `grep "multi-agent|multi agent|multiagent" -i` → 27 files
19. `grep "guardrail|security|safety" -i` → 147 files
20. `grep "forward deployed|forward-deployed engineer" -i` → 12 files
21. `grep "go to market|go-to-market|\bGTM\b" -i` → 22 files
22. `grep "agentic commerce|x402|payments?\b.*agent|agent.*payment" -i` → 20 files
23. `grep "\bskills?\b" -i` → 159 files
24. `grep "\bharness(es)?\b" -i` → 138 files
25. `grep "benchmark" -i` → 100 files
26. `grep "\bagents?\b" -i` → 310 files
27. `grep "eval" ia-aie-ung-evals-that-matter.md -i`
28. `grep "eval" ia-aie-gupta-production-evals.md -i`
29. `grep "guardrail" ia-aie-agrawal-hinge-health-guardrails-first.md -i`
30. `grep "firewall|security" ia-aie-dahl-security-firewall-agents.md -i`
31. `grep "code review" ia-aie-bond-ketkar-uber-ureview-code-review.md -i`
32. `grep "code review" ia-aie-jain-kill-code-review.md -i`
33. `grep "memory" ia-aie-khemani-every-memory-system.md -i`
34. `grep "memory" ia-aie-druga-memory-harnesses.md -i`
35. `grep "harness" ia-aie-bhagwat-every-harness-claw.md -i`
36. `grep "harness" ia-aie-bhargava-harness-over-model.md -i`
37. `grep "benchmark" ia-aie-heiner-benchmaxxing-plague.md -i`
38. `grep "benchmark" ia-aie-khial-benchmarks-good-bad-ugly.md -i`
39. `grep "MCP" ia-aie-davis-mcp-tasks.md`
40. `grep "MCP" ia-aie-salomon-yosef-mcp-apps.md`
41. `grep "continual learning" ia-aie-feizi-continual-learning.md -i`
42. `grep "post-training|post training" ia-aie-brown-modern-post-training.md -i`
43. `grep "voice" ia-aie-msft-voice-no-frontier.md -i`
44. `grep "voice" ia-aie-primas-voice-realtime-video.md -i`
45. `grep "multi-agent|multiagent|multi agent" ia-aie-sethuraman-asokan-killed-multiagent.md -i`
46. `grep "multiplayer|multi-agent|agents talking" ia-aie-singh-multiplayer-agents.md -i`
47. `read ia-aie-ung-evals-that-matter.md lines 1–30`
48. `read ia-aie-gupta-production-evals.md lines 1–30`
49. `read ia-aie-agrawal-hinge-health-guardrails-first.md lines 1–20`
50. `read ia-aie-dahl-security-firewall-agents.md lines 1–20`
51. `read ia-aie-bond-ketkar-uber-ureview-code-review.md lines 1–20`
52. `read ia-aie-jain-kill-code-review.md lines 1–20`
53. `read ia-aie-khemani-every-memory-system.md lines 1–20`
54. `read ia-aie-druga-memory-harnesses.md lines 1–20`
55. `read ia-aie-bhagwat-every-harness-claw.md lines 1–20`
56. `read ia-aie-bhargava-harness-over-model.md lines 1–20`
57. `read ia-aie-heiner-benchmaxxing-plague.md lines 1–14`
58. `read ia-aie-khial-benchmarks-good-bad-ugly.md lines 1–14`
59. `read ia-aie-davis-mcp-tasks.md lines 1–14`
60. `read ia-aie-salomon-yosef-mcp-apps.md lines 1–14`
61. `read ia-aie-feizi-continual-learning.md lines 1–14`
62. `read ia-aie-brown-modern-post-training.md lines 1–14`
63. `read ia-aie-msft-voice-no-frontier.md lines 1–14`
64. `read ia-aie-primas-voice-realtime-video.md lines 1–14`
65. `read ia-aie-sethuraman-asokan-killed-multiagent.md lines 1–14`
66. `read ia-aie-singh-multiplayer-agents.md lines 1–14`

</details>

**Agent + Omnigraph**, start of the answer:

> ## Most discussed topics at AI Engineer World's Fair 2026
>
> I used the knowledge graph's "Pattern" layer (theses the extraction pipeline tags as recurring across talks, each backed by dated "Signal" evidence pulled from transcripts) as the best available proxy for "topics," since the graph doesn't offer a single agreed topic list. I ranked the 18 tracked patterns by how many supporting signals they've accumulated, then sampled the signals behind each one (via `signal-evidence`, which returns the exact talk and quote a claim came from) to confirm that each pattern really is drawn from many distinct talks rather than one or two. Every pattern below checked out as multi-talk in the samples I pulled. Talk counts are **approximate** — extrapolated from signal volume and the fraction of distinct talks seen in each sample — not an exact tally of every talk in the corpus.
>
> …

**Agent + Markdown files**, start of the answer:

> ## Most Discussed Topics at AI Engineer World's Fair 2026
>
> I ranked topics by counting how many transcript files (out of 337 total) contain terms clearly tied to each theme (evaluation, guardrails/security, code review, memory, harness, benchmark, MCP, continual-learning/RL/post-training, voice, multi-agent). These are approximate counts from keyword matches across the corpus, not manual topic-tagging, so treat them as rough orderings rather than exact tallies.
>
> …


## Method notes

1. **Setup.** 10 questions × 2 arms × 3 runs (60 agent runs), run on 2026-09-23. Both arms use `anthropic/claude-sonnet-5[1m]` at effort `high`, no subagents, capped at 300 turns, $10 and 30 min per run (Claude Code 2.1.280, Agent SDK 0.2.158). The Omnigraph arm reads a local copy of the graph (commit `01M37ZANGF3QTZH8WDE3J9ZEN9`) through stored read queries only. The markdown arm reads the talk transcripts as files (corpus `63c73703991e`).
2. **Correctness is relative.** There is no gold answer set. A claim is grounded when its quote is in the cited transcript and a judge finds that it supports the claim. Recall is measured against the pool of everything either arm found and grounded, so entries neither arm found don't count. On fixed-length lists every run's recall is N ÷ pool, so those show the arms' agreement instead.
3. **The judge** is `anthropic/claude-opus-5.5` and never told which arm wrote what. Before the pairwise comparison, both answers go through the same redaction of tool and source mentions, though differences of style remain. Each pairing is judged in both orders, and an arm wins only if it wins both; the two orders agreed in 25 of 30 pairings. Its support verdicts vary by a few percent between passes, so small differences between the arms are within noise. Judge cost for these results: $10.29, kept apart from the arms' costs.
4. **Costs** are token usage × OpenRouter prices as of 2026-09-23 (the Agent SDK's own figure matched). They cover answering the questions; building the graph (extraction, embeddings) is excluded.
5. **The absence question** has no talk to find, and both arms can be right by finding nothing. A pairwise win there reflects extra context, not accuracy (2 of 3 Q10 pairings are ties).
