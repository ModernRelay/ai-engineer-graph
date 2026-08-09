# SPIKE extraction — "An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge" (Zhengyao Jiang, Weco) — FOR REVIEW

Source transcript: `transcripts/jiang-weco-openai-hiring-challenge-agent.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/iCj_ATyThvc — AI Engineer World's Fair, published 2026-07-16.
`stagingTimestamp` for the artifact and all signals: 2026-07-16 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-jiang-aiden-parameter-golf` | An AI Agent Became the #1 Contributor in OpenAI's Hiring Challenge (Zhengyao Jiang, Weco — AI Engineer World's Fair) | youtube | https://youtu.be/iCj_ATyThvc |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-zhengyao-jiang`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-zhengyao-jiang` | Zhengyao Jiang (co-founder & CEO, Weco; PhD in reinforcement learning — see review note 1 on institution) | `AffiliatedWithCompany → co-weco` |

## Companies (1 new, 1 reused)

| slug | name | type | note |
|---|---|---|---|
| `co-weco` | Weco | developer | auto-research product/research lab (~founded 2024); built AIDE (top ML-engineering agent, independently evaluated by OpenAI in the MLE-bench paper) and Aiden |
| **[registry]** `co-openai` | — | — | host of the Parameter Golf hiring challenge — reuse, no new node |

## Elements (2 new, 1 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-aiden` | Aiden (Weco) | product | harness | Weco's experimental multi-agent, self-improving auto-research agent: reads public information (papers, other participants' PRs), runs its own experiments, and submits a PR only once findings pass a quality gate — i.e. an auto-researcher that publishes into a human community rather than hill-climbing privately | 
| `el-aide` | AIDE (Weco) | product | harness | Weco's earlier machine-learning-engineering agent (~2024), independently evaluated by OpenAI in the MLE-bench paper as the top auto-research/MLE agent of its time; predecessor of Aiden |
| **[registry]** `el-autoresearch` | — | — | — | the talk's framing concept ("you've seen a lot of auto research today") — reuse, no new node |

Element edges: `el-aiden`, `el-aide` `IdentifiedInArtifact → ia-aie-jiang-aiden-parameter-golf`; both `DevelopedByCompany → co-weco`; `el-aiden` `UsesElement → el-autoresearch`-style relation kept as prose (Aiden is an instance of the auto-research concept — see review note 4); `el-aiden` `ExemplifiesPattern → pat-accelerated-research` **[registry]**.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-jiang-aiden-parameter-golf`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | domain | FormsPattern | RelevantCompany |
|---|---|---|---|---|
| `sig-aiden-tops-parameter-golf` | April 2026: in OpenAI's "Parameter Golf" hiring challenge (~1,000 ML engineers, ~2,000 submissions, 47 passing open review, 7 of those from agents), Weco's agent Aiden ran 22 days and set 7 leaderboard records — each stamped as a new competition best by OpenAI — vs 3 for the best human; OpenAI couldn't hire its top contributor because it wasn't a person | training | `FormsPattern → pat-accelerated-research` **[registry]** | `co-openai`, `co-weco` |
| `sig-agent-highest-h-index` | Community recognition, not just score: computed over PRs, Aiden's H-index was 10 vs 7 for the best human — the whole community, including other leaderboard entries, was building on the AI system's published work | training | `FormsPattern → pat-accelerated-research` | `co-weco` |
| `sig-agent-lifts-signal-noise` | Efficiency over brute force: Aiden used at most ~4% of the competition's total compute (~1,300 experiments on a single H100 node) for ~15% of the records; 28% of its submissions made the leaderboard — roughly 6× the community hit rate — so the agent raised the signal-to-noise ratio of the community's public PR channel rather than flooding it | training | `FormsPattern → pat-accelerated-research` | `co-weco` |
| `sig-agent-ideas-human-sourced` | Tracing Aiden's record PRs: nearly all ideas came from human sources — research papers (e.g. gated attention from a Qwen paper), other participants, adjacent communities like nanoGPT — including ideas humans noted and abandoned over implementation difficulty; only a small fraction were original (mostly forced by the 16 MB file-size constraint, e.g. a quantization move). The winning record was a synergy of three recombined borrowed ideas | training | `FormsPattern → pat-accelerated-research` (division-of-labor evidence: humans supply ideas, agents execute/combine) | — |
| `sig-loose-abstraction-leaks-eval` | Weco fraud-detection case: with a loose API where one function processed both training and test data, the auto-research agent produced great-looking scores polluted by test-set leakage; tightening the abstraction so test data couldn't reach training dropped the leakage rate to zero — verification enforced structurally, not by trusting the agent | harness | `FormsPattern → pat-verification-gap` **[registry]** | `co-weco` |

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-eval-is-the-loss-function` | Running auto-research is like training a model: your eval is the data + loss function (the environment the agent trains against). Proprietary evaluation data and unique domain judgment about what to measure become a vertical moat that gets amplified as auto-research strengthens | `HighlightsPattern → pat-accelerated-research` **[registry]** | `ReliesOnElement → el-autoresearch` **[registry]** |
| `ins-abstraction-biases-the-search` | Codebase abstraction is the architecture of auto-research: it sets constraints and priors, and the starting point hugely biases the whole search direction. A good abstraction steers agents toward solutions that generalize — and makes reward hacking structurally hard — even when scores look identical | `HighlightsPattern → pat-verification-gap`, `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-autoresearch` |
| `ins-humans-move-up-the-stack` | Karpathy's ~2015 "gradient descent can write code better than you" is the metaphor for auto-research now: it commoditizes execution skills while making higher-level skills — creativity, eval design, abstraction design, driving the systems themselves — exponentially more valuable. The search is automated; humans move up the stack, not out of it. Community/competition designers gain huge leverage | `HighlightsPattern → pat-accelerated-research` | — |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-jiang-aiden-parameter-golf`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-tighten-agent-abstractions` | Make failure modes structurally impossible via strict APIs | When an auto-research agent optimizes a pipeline, don't rely on it behaving: design the abstraction so bad solutions can't be expressed (e.g. separate train/test data paths so leakage is impossible); expect loose APIs to yield polluted high scores; treat abstraction design like neural-architecture design — it biases which solutions are learnable | `ReferencesElement → el-autoresearch` **[registry]** |
| `how-treat-eval-as-training-signal` | Design the eval like you'd curate training data | The eval is what the agent optimizes; invest in it like data + loss: encode proprietary domain understanding of what matters and how to measure it; a better eval compounds as agent capability grows and is where a defensible vertical position lives | `ReferencesElement → el-autoresearch` |

## Dropped

- "Parameter Golf" as an Element — it's a one-off competition, kept as prose in signals.
- nanoGPT as an Element — passing community reference (and distinct from registry `el-nanograph`); prose only.
- MLE-bench as an Element — single mention as evaluation provenance for AIDE; prose in `el-aide` brief.
- Karpathy tweet — quoted metaphor, not a contribution; `exp-karpathy` **[registry]** left unlinked (no ContributedByExpert), kept in `ins-humans-move-up-the-stack` prose.

## Review notes

1. Captions say "got my PhD at UCR"; Jiang's PhD is generally associated with UCL (London, RL). Left institution out of the node name; flagged as an unresolved garble — verify before publishing.
2. "OBI ran a hiring challenge" in the captions = OpenAI (consistent with the official title and repeated later references). "Wiko"/"we call" = Weco; "Jungao" = Zhengyao; "primate golf"/"primary golf" = Parameter Golf; "Ach index" = H-index; "Quen" = Qwen; "aid"/"Aid" = AIDE/Aiden (context-dependent); "16 megapy" = 16 MB.
3. Per instructions I checked seed `el-autoresearch` before coining: Aiden and AIDE are Weco products (instances), not the concept — coined as products, concept reused.
4. Schema has no clean Element→Element "instance-of" edge; noted Aiden-as-instance-of-auto-research in prose rather than forcing `UsesElement`.
5. Numbers (1,000 participants / 2,000 submissions / 47 passed / 7 agents / H-index 10 vs 7 / 4% compute / 15% records / 28% vs ~6× hit rate / 1,300 experiments / 22 days) are all speaker-claimed from the talk; not independently verified.
