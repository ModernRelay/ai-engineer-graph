# SPIKE extraction — "Computer Use at the Edge of the Statistical Precipice" (Pierluca D'Oro, Programma Labs) — FOR REVIEW

Source transcript: `transcripts/doro-programma-statistical-precipice.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/CTLa_p6iOiY — AI Engineer World's Fair, **Computer Use (CUA) track**, published 2026-08-14.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-14 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the track's evals-rigor talk, presenting paper work done at Meta Superintelligence Labs. Two problems in CUA benchmarks: (1) a **replay agent** — a <1MB blind script of recorded successful trajectories — matches or beats the frontier model it was extracted from on deterministic benchmarks, and pass@k is proved to be a metrification of that exploit; (2) confidence intervals computed from rollouts alone give ~20% coverage, causing overconfident and costly deploy decisions. Fixes: the **PRISM principles** for environment design and **DG-World**, a 15-app Android benchmark with 3.2M verified configs built by a compiler-like system; plus honest hierarchical confidence intervals. Caption garbles: "Pugadoro" → **Pierluca D'Oro**, "Programmabs/programmer" → **Programma Labs**, "Meta super intelligent labs" → **Meta Superintelligence Labs**, "OSW word/mobile word" → **OSWorld / MobileWorld** (⚠ see review note 3), "DGword/DG word/dig" → **DG-World**, "stockasticity" → stochasticity, "ku/Kua" → **CUA**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-doro-statistical-precipice` | Computer Use at the Edge of the Statistical Precipice (Pierluca D'Oro, Programma Labs — AI Engineer World's Fair) | youtube | https://youtu.be/CTLa_p6iOiY |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-pierluca-doro`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-pierluca-doro` | Pierluca D'Oro (founder, Programma Labs; the paper work was done while at Meta Superintelligence Labs) | `AffiliatedWithCompany → co-programma-labs`, `AffiliatedWithCompany → co-meta` **[registry]** |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-programma-labs` | Programma Labs | developer | Building "the best infrastructure for CUA-enabled verification"; hiring. The DG-World / PRISM / honest-confidence-interval work was done by the founder at Meta Superintelligence Labs and is now the company's basis |

Reused **[registry]**, edge-only: `co-meta` **[seed]** — where the work was done ("while at Meta Superintelligence Labs").

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-replay-agent` | The replay agent | concept | training | The exploit that motivates the whole talk: run a good frontier model on a benchmark, record one successful trajectory (taps, types, scrolls) per task, and compile them into a **blind script <1MB** that replays the recorded action sequence when a task arrives. On deterministic benchmarks (OSWorld, MobileWorld) this replay agent's success rate **equals or beats the frontier model it was extracted from** — "we shouldn't accept blind scripts beating frontier models." The tell is that most existing benchmarks are static and deterministic, hence gameable by memorized sequences |
| `el-passk-is-replay` | pass@k as a replay metrification | concept | training | The sharper formal result: pass@k (probability at least one of k attempts succeeds) is proved in the paper to be **literally the success rate of the replay agent on a deterministic environment**. "If the replay agent felt weird to you, pass@k on computer-use tasks should feel weird too — it is a metrification of that exploit." A widely-used CUA metric shown to reward memorization rather than capability |
| `el-prism-principles` | PRISM principles for environment design | concept | training | Guiding principles for robust, trustworthy environments so replay can't win: **multiffactorial variation** (vary data, appearance, initial state — stochasticity), with a system that **verifies every generated combination is valid**; **sandboxed**; **verifier-supported** (privileged information); and **realistic** (faithful reproduction so the score means something). No existing benchmark satisfies all of them — "some do some things well, others do other things well, but there's no unified benchmark that matches all these boxes" |
| `el-dg-world` | DG-World | product | training | The benchmark built to satisfy PRISM: 15 Android apps across domains, **387 verified scenarios**, and **~3.2M verified configurations** (scalable to billions), varying instance (exact amounts), data profile (contacts, emails), theme, and starting screen. Built by a **compiler-like system** — a parameterized task template + a matching verifier + mock data, assembled against a base UI state into valid configs, rejecting broken combinations. On DG-World the replay agent gets almost no performance ("a little, which is probably what you want — some tasks are repeatable by nature"), and it exposes frontier models as **poorly robust** to variation (a model good at a task often drops sharply when the starting screen or theme changes) |
| `el-honest-confidence-intervals` | Honest confidence intervals for CUA | concept | training | The metrics half: two sources of variation matter — action stochasticity (different trajectories per run) *and*, in a multi-config benchmark, environment variation — and both must be captured. Rollout-only confidence intervals give **~17–20% coverage** (you guess the true performance only ~20% of the time) while looking tight; a hierarchical method respecting benchmark structure reaches the intended 90–95% coverage. The consequence is a deploy decision: overconfident small intervals pick the wrong model, and "with 1M tasks, a 4% performance mismatch at ~$12 average per mistake costs hundreds of thousands of dollars a month." An honest interval instead says "I'm not confident enough to decide" — prompting more eval spend rather than a costly wrong call |

Element edges: all five `IdentifiedInArtifact → ia-aie-doro-statistical-precipice`.
`el-dg-world` `DevelopedByCompany → co-programma-labs`, `UsesElement → el-prism-principles`;
`el-prism-principles` `EnablesElement → el-dg-world`;
`el-replay-agent` `EnablesElement → el-passk-is-replay`;
`el-dg-world` `ExemplifiesPattern → pat-benchmark-trust-crisis`-adjacent — *not emitted* (uncoined; see review note 1);
`el-honest-confidence-intervals` `ExemplifiesPattern → pat-verification-gap` **[registry]**.

Reused elements (no new nodes): `el-computer-use-verifier` **[b7]**, `el-continual-learning` adjacency (none), `el-private-benchmark` **[b12]** (conceptual neighbor — contamination-resistant construction), edge left to review.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-doro-statistical-precipice`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-programma-labs`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-replay-agent-beats-frontier-models` | training | The demonstration: a <1MB blind script that replays recorded successful trajectories **matches or beats the frontier model it was extracted from** on deterministic CUA benchmarks (OSWorld, MobileWorld). "We shouldn't accept blind scripts beating frontier models." The cause is benchmark determinism — a static environment is gameable by memorized action sequences — which means high scores on these benchmarks can certify memorization rather than capability | `FormsPattern → pat-benchmark-trust-crisis` (coined 2026-08-16) | `OnElement → el-replay-agent`, `el-passk-is-replay` |
| `sig-passk-is-a-gameable-metric` | training | The formal result: pass@k on a deterministic environment is proved equal to the replay agent's success rate — "a metrification of that exploit." A metric in wide use for computer-use evaluation shown to reward the exact memorization the replay agent exploits, so a rising pass@k does not distinguish capability from a compiled tape of prior successes. Construction-methodology evidence of benchmark unreliability, with a proof rather than an anecdote | `FormsPattern → pat-benchmark-trust-crisis` (coined 2026-08-16) | `OnElement → el-passk-is-replay`, `el-replay-agent` |
| `sig-prism-environments-resist-replay` | training | The constructive fix: environments built to the PRISM principles — multifactorial variation with per-combination validity checking, sandboxed, verifier-supported, realistic — defeat the replay agent (which drops to near-zero on DG-World). The scaling insight is that coding agents can generate the variation but "a lot of software is not the same as an effective environment" — the key is a **verification strategy** (a compiler-like template + verifier + mock-data system rejecting invalid combinations), not raw generation volume. Bears directly on the environments-as-product thread | `FormsPattern → pat-environments-economy`-adjacent — **HELD PATTERN-LESS** (see review note 2) | `OnElement → el-prism-principles`, `el-dg-world` |
| `sig-frontier-models-not-robust-to-variation` | training | An empirical finding DG-World's variation surfaces: frontier models are "pretty bad at being robust to these variations" — a model good at a task often loses much of its performance when only the starting screen or the app theme changes. Static benchmarks hide this by testing one configuration; a multi-config benchmark measures it and lets teams calibrate expectations. Capability measured on one layout does not transfer, which is invisible to the benchmarks the field steers by | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-dg-world`, `el-prism-principles` |
| `sig-overconfident-evals-cost-real-money` | training | The metrics indictment with a dollar figure: rollout-only confidence intervals give ~20% coverage while appearing tight, so a deploy decision between models A and B is made on intervals that are actually overconfident — and "with 1M tasks and a 4% real performance mismatch at ~$12 per mistake, that's hundreds of thousands of dollars a month." An honest hierarchical interval instead reports insufficient confidence, prompting more eval rather than a wrong call. "A non-rigorous benchmark is misleading — for the field, and especially for your own decisions" | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-honest-confidence-intervals` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-determinism-is-the-exploit` | The replay agent and pass@k are the same defect viewed twice: a deterministic environment can be beaten by a compiled tape of past successes, and any metric that rewards "at least one success in k tries" is measuring that tape. The fix is not a better metric on the same environments but **variation with verified validity** — which is expensive precisely because each generated configuration must be proven valid, the step raw coding-agent generation skips. Environment rigor and metric rigor are one problem: without stochasticity there is nothing for an honest interval to measure | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-replay-agent`, `el-prism-principles` |
| `ins-coverage-is-the-honest-number` | The talk's transferable discipline is reporting **coverage** — does your 95% interval actually contain the truth 95% of the time — rather than interval width. Rollout-only intervals look confident and are wrong 80% of the time; the honest move is to respect the benchmark's hierarchy and, when the data can't support a decision, to say so and spend more. That reframes evaluation cost as insurance against a far larger deployment mistake, and it is the same "test the second pass, not the first" discipline the continual-learning benchmark talks reached (Asawa, b19), here formalized for computer use | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-honest-confidence-intervals`, `el-dg-world` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-doro-statistical-precipice`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-rigorous-cua-benchmarks` | Build CUA benchmarks a blind script can't beat | Assume a deterministic benchmark is gameable — a <1MB replay of recorded successful trajectories will match your frontier model, and pass@k on a static environment is literally that replay's success rate, so treat a high pass@k as unproven until you check for replay; design environments to the **PRISM principles** — multifactorial variation (data, appearance, initial state), per-combination validity verification, sandboxing, verifier support, and realistic reproduction — since no existing benchmark satisfies all of them; generate variation with coding agents but **verify every combination**, because volume of software is not the same as a valid environment — use a compiler-like pipeline of parameterized template + verifier + mock data that assembles configs and rejects broken ones; measure model **robustness across variation axes** (starting screen, theme, data profile), not just one configuration, because frontier models often lose much of their performance under variation; and report **coverage, not interval width** — rollout-only confidence intervals give ~20% coverage while looking tight, so use a hierarchical method that respects benchmark structure, and when it says you can't confidently decide between two models, spend more on evaluation rather than making a costly wrong deployment call | `ReferencesElement → el-prism-principles`, `el-dg-world`, `el-replay-agent`, `el-honest-confidence-intervals` |

## Dropped

- **The pass@k formal-proof details** — the result (pass@k = replay success rate on deterministic envs) is in `el-passk-is-replay`; the derivation is left to the paper.
- **The DG-World compiler internals** (base case + template + verifier assembly) — folded into `el-dg-world`.
- **The hiring close** — logistics.

## Review notes

1. **⚑ Two more legs for `pat-benchmark-trust-crisis`, both held pattern-less, both unusually rigorous.** The replay-agent result and the pass@k-is-replay proof are *construction-methodology / gaming* evidence with a formal proof rather than an anecdote — joining the b15 FINDING 2 catalog (which already had nine distinguishable legs; this adds a computer-use-specific replay/determinism leg). That candidate is at ~13 registry mentions and remains the corpus's best-evidenced uncoined pattern after `pat-agent-economy`. Strongly worth the coin review; rehome both signals on coin.
2. **⚠ `sig-prism-environments-resist-replay` also feeds `pat-environments-economy`** (verified-valid environments as the product; verification strategy as the moat, not generation volume) — the same both-ledgers straddle as b19's continual-learning-bench work. Held pattern-less; no edge emitted to either uncoined candidate.
3. **⚠ Verify before seeding:** "OSWorld"/"MobileWorld" benchmark names (reconstructed — OSWorld is real; "MobileWorld" may be **AndroidWorld/MobileWorld**, medium confidence); DG-World's 15 apps / 387 scenarios / 3.2M configs; the ~17–20% vs 90–95% coverage figures; the $12-per-mistake / 1M-task / 4%-mismatch cost illustration. All caption-sourced and paper-backed but unverified here.
4. **Dual affiliation** (`co-programma-labs` current + `co-meta` where the work was done) per the b8 dual-affiliation precedent. `el-private-benchmark` **[b12]** is a conceptual neighbor (contamination-resistant construction) — proposed cross-file edge left to review, not emitted.
