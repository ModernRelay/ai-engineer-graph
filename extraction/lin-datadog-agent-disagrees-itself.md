# SPIKE extraction — "Why Your Agent Disagrees With Itself (And What To Do About It)" (Diane Lin, Datadog) — FOR REVIEW

Source transcript: `transcripts/lin-datadog-agent-disagrees-itself.txt` (auto-captions — quotes are paraphrases; "Dyan Huang Lin" = Diane Lin per talk listing; her acquired startup's name is garbled as "Chrome innate" — unresolved, see review notes).
Published 2026-07-20 on the AI Engineer channel (World's Fair). `stagingTimestamp` for all nodes: 2026-07-20.
Entities marked **[registry]** already exist; `pat-model-not-bottleneck` is **[batch2]**, defined in `dmello-nvidia-llm-stack-2008-database.md`.

---

## InformationArtifact

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-lin-agent-consistency` | Why Your Agent Disagrees With Itself (And What To Do About It) (Diane Lin, Datadog — AI Engineer World's Fair) | youtube | https://youtu.be/wEc9aG7cRQc |

Edges: `PublishedBySource → source-aie-yt`; `ContributedByExpert → exp-diane-lin`.

## Experts (1 new)

| slug | name | AffiliatedWithCompany |
|---|---|---|
| `exp-diane-lin` | Diane Lin (Datadog, leads self-evolving-agent development; co-founded an AI SOC auto-triage startup acquired by Datadog; ex-Alexa QA team, ex-Vicarious, ex-Zscaler) | `co-datadog` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-datadog` | Datadog | developer | Observability/security platform; acquired Lin's SOC auto-triage startup in early 2026 |

> Zscaler, Vicarious (now part of Google DeepMind), Alexa/Amazon appear only in
> biographical prose — not promoted to Company edges.

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-active-learning` | Active learning (for agent QC) | concept | harness | Classic ML technique repurposed for LLM agents: instead of reviewing every output, select the cases the system is most likely to get wrong and spend human attention there; for LLMs the reliable selection strategy is disagreement across repeated runs/models (query-by-committee), not self-reported confidence |
| `el-semantic-episodic-memory` | Semantic + episodic agent memory | concept | harness | Lightweight alternative to fine-tuning: episodic memory (past similar cases and their decisions, referenced automatically) resolves recurring situations without human intervention; semantic memory (distilled domain rules/policies from human review) sharpens the decision boundary; the two are complementary, not competing |

Element edges: both IdentifiedInArtifact → `ia-aie-lin-agent-consistency`; `el-semantic-episodic-memory` EnablesPattern → `pat-verification-gap`.

## Patterns (0 new)

Links to **[registry]** `pat-verification-gap` (consistency as the trust
bottleneck of shipped agents) and **[batch2]** `pat-model-not-bottleneck`
("it's not your AI agent's fault — stop blaming your model").

## Signals (4 new)

All: domain `security`, `SpottedInArtifact → ia-aie-lin-agent-consistency`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-datadog-triage-flipflop-25pct` | Datadog experiment: 93 real security alerts run 3× through an LLM triage agent — ~25% flip-flopped their malicious/benign verdict across runs; adding episodic memory locked down ~15 points of that, leaving ~10% for human review plus semantic-knowledge disambiguation | `pat-verification-gap` | RelevantCompany → `co-datadog` |
| `sig-llm-confidence-unreliable` | Datadog practice finding: LLM self-reported uncertainty is not a usable active-learning signal — the model "doesn't know what it doesn't know" and high confidence doesn't imply correctness; disagreement across repeated runs or across models is the reliable selector | `pat-verification-gap` | RelevantCompany → `co-datadog`; OnElement → `el-active-learning` |
| `sig-flipflops-cluster-gray-zone` | Observation replicated across two domains (hotel sentiment, SOC alert triage): the cases that flip-flop concentrate near the decision boundary — exactly where human experts also disagree and where the "right" label is a matter of company policy/preference (e.g., password spray with no successful login: notify or ignore?) | `pat-verification-gap`, `pat-model-not-bottleneck` | RelevantCompany → `co-datadog` |
| `sig-datadog-acquires-triage-startup` | Datadog acquired Lin's AI SOC auto-triage startup in early 2026 (startup name garbled in captions); she now leads "self-evolving agent" development at Datadog — consolidation of agent-triage/verification tooling into observability platforms | `pat-verification-gap` | RelevantCompany → `co-datadog` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-inconsistency-is-ambiguity` | Agent self-disagreement usually isn't a model problem — the agent is surfacing ambiguity that already exists (underspecified labeling policy, missing disambiguating information) at the decision boundary where humans and classical classifiers also fail. Model disagreement is a feature, not a bug: each flip-flop is a pointer to exactly where clarification teaches the system the most | `pat-model-not-bottleneck`, `pat-verification-gap` | `el-active-learning` |
| `ins-consistency-is-trust` | Consistency, not just accuracy, is what enterprise buyers experience as trust: a single evaluation run tells you nothing (you must average repeated runs), and in a POC bake-off the vendor whose agent flip-flops loses the deal regardless of average efficacy | `pat-verification-gap` | — |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-lin-agent-consistency`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-disagreement-active-learning` | Use disagreement-driven active learning as agent quality control | Run the agent in monitor mode on production data, multiple runs per case; select for review the cases whose verdicts disagree across runs/models (not low-confidence ones — LLM confidence is unreliable); have humans clarify only that subset: fix the label or add the disambiguating feature; feed both back. Small labeling effort, high return — and you're gathering customer-preference adaptation for free | `el-active-learning` |
| `how-memory-not-finetuning` | Reach for memory augmentation before retraining | Fine-tuning is expensive and slow to iterate; instead: episodic memory auto-resolves recurring cases by referencing past similar cases and their decisions (great for recurring false-positive noise); what still flips escalates to human review; humans distill the reasoning into semantic-memory rules (e.g., "password spray without successful login → benign; with a final successful login + MFA pass → malicious"), which sharpens the boundary for both the agent and human labelers | `el-semantic-episodic-memory` |

## Dropped

- Lin's full career biography (Imperial PhD, MIT one-shot learning, Alexa, Vicarious→DeepMind, Zscaler) — kept one line in the Expert row, rest is prose.
- The traditional ML active-learning pipeline walkthrough — textbook material; only the LLM-era deltas (selection strategy, memory-instead-of-retrain) are captured.
- Colleague acknowledgments.

## Review notes

1. **Startup name unresolved**: captions say "Chrome innate has been acquired by Data Dog earlier this year." Verify the real name before seeding `sig-datadog-acquires-triage-startup`; the signal stands on the acquisition fact either way — or drop it if you consider M&A-without-name too weak.
2. Domain choice: signals are `security` (SOC triage context); `harness` is defensible for `sig-llm-confidence-unreliable`.
3. `sig-flipflops-cluster-gray-zone` double-forms both patterns — the gray-zone fact is the batch's cleanest bridge between them; trim to one if you want single-home signals.
