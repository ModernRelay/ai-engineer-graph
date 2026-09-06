# SPIKE extraction — "How I automate my own job at Hugging Face using agents" (Niels Rogge, Hugging Face) — FOR REVIEW

Source transcript: `transcripts/rogge-huggingface-automate-own-job.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/FLUoowDJg4I — AI Engineer World's Fair, published 2026-08-20.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-20 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: an ML engineer on Hugging Face's community science team ("the Google Drive to the Hub team") automated his outreach job in two stages: in 2024 a deterministic **cron workflow** (LLM API calls, no framework, GitHub Actions, Langfuse tracing) that reads hundreds of arXiv papers nightly and opens GitHub issues/PRs; in 2025 the follow-up became a fully **autonomous agent** — Claude Agent SDK, bash + the Hugging Face CLI, one skill, a Modal sandbox per issue — now on GLM 5.2 via Hugging Face inference providers because "models have become so good." He doesn't disclose the agent; two negative replies in thousands; agents now reply to his agents. Caption garbles: "Neils" → **Niels**, "hugging phase"/"Hingo" → **Hugging Face**, "Entropic"/"entropic" → **Anthropic**, "cloth agents SDK" → **Claude Agent SDK**, "Kurser" → **Cursor**, "model" (deploy) → **Modal**, "chron" → **cron**, "excellraw" → **Excalidraw**, "Hamel Husin" → **Hamel Husain**, "op 4.8" → **Opus 4.8**, "Mac Mitchell" → **Margaret Mitchell**, "pedal OCR" → **PaddleOCR**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-rogge-huggingface-automate-own-job` | How I automate my own job at Hugging Face using agents (Niels Rogge, Hugging Face — AI Engineer World's Fair) | youtube | https://youtu.be/FLUoowDJg4I |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-niels-rogge`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-niels-rogge` | Niels Rogge (ML Engineer, Community Science team, Hugging Face; 5 years) | `AffiliatedWithCompany → co-hugging-face` **[registry]** |

## Companies (0 new)

Reused **[registry]**, edge-only: `co-hugging-face` — new facts: the community-science team's outreach (paper pages linking artifacts, metadata tags, model/dataset cards) is now run by agents opening hundreds of GitHub issues nightly; Hugging Face inference providers wrap Together, Fireworks, Cerebras and others behind OpenAI/Anthropic-compatible endpoints; the Daily Papers X account (90K followers) runs on the same workflow; a papers-with-code revival at paperswithcode.co. Reused `co-anthropic` **[seed]** ("building effective agents" post; Claude Agent SDK; the NYC workshop that said agents may beat workflows), `co-modal` (batch containers, one agent loop per issue), `co-cursor` (Composer 2.5 invoking the skill; the "12,000 lines → 200-line skill" talk), `co-zhipu-ai` (GLM 5.2), `co-apple` and `co-google-deepmind` (outreach targets), `co-google` (Gemini picks tweet visuals). Referenced, not coined: PaddleOCR, Together AI / Fireworks (providers), Langfuse (booth; see element).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-community-science-outreach-agent` | The community-science outreach agent | product | harness | The job: watch arXiv/GitHub for trending work, find the repo, read the README, check whether weights/datasets are on the Hub with proper cards and metadata, open a GitHub issue ("could you release this checkpoint on Hugging Face?") or a PR adding cards, follow up. Hundreds of papers a day made it unscalable by hand. Stage one (2024): a deterministic workflow mirroring his own steps — LLM API calls inside a predefined pipeline, no framework, deployed as a nightly cron on GitHub Actions ("free cron jobs"), traced in Langfuse. Hundreds of issues per night |
| `el-workflow-then-agent-choice` | Workflow first, agent when the models allow | concept | harness | Anthropic's *Building Effective Agents* (2024): workflows are predictable and controllable, agents flexible but less predictable — start simple, avoid frameworks. So the outreach was a workflow. By late 2025 Anthropic's own workshop said models are good enough that agents may beat workflows; Cursor replaced 12,000 lines of custom workflow with a 200-line skill. His follow-up automation therefore became an autonomous agent — "I can replace thousands of lines of custom code with a simple agent with a CLI as a tool and a skill" |
| `el-cli-skill-sandbox-agent` | The CLI + skill + sandbox agent | technology | harness | Follow-up on GitHub issues as a fully autonomous agent: Claude Agent SDK; bash as the tool, driving the Hugging Face CLI; one skill (the HF CLI skill) — "that's all it needs"; deployed on Modal's batch processing, one container per GitHub issue, fast starts; posts results to Slack. Model: initially Claude, now **GLM 5.2** via Hugging Face inference providers (cheaper; beats Opus 4.8 on some Cursor benches). Invoked as a Cursor skill (`process unread`) that has Composer 2.5 fan out the agents — "the loop people are talking about" |
| `el-undisclosed-agent-outreach` | Undisclosed agent outreach and its reception | concept | | He doesn't disclose it's a bot ("if people know it's a bot they might close the issue"; it posts exactly what he posted manually). Out of thousands of issues, two negative replies ("please close this slop"); researchers from Apple and Google DeepMind replied to "him"; a Chinese OCR company migrated all its models; a trending paper's issue got 60+ upvotes; agents completing Margaret Mitchell's model-card template even credited "Niels, community science team." Increasingly "people use an agent to reply to my agents." Guard against slop with evals (Hamel Husain's LLM-evals FAQ) |
| `el-daily-papers-bot` | Daily Papers and papers-with-code revival | product | | An X account posting interesting papers and artifacts every four hours or on release, on the same workflow, with Gemini choosing the visual — 90,000 followers "without any involvement of me" (a tweet on Nvidia's optimized GLM 5.2 got 2,000+ likes). Plus a revival of Papers with Code (acquired, then died) at paperswithcode.co as benchmarks and an educational resource |

Element edges: all five `IdentifiedInArtifact → ia-aie-rogge-huggingface-automate-own-job`.
`el-community-science-outreach-agent` `DevelopedByCompany → co-hugging-face` **[registry]**;
`el-community-science-outreach-agent` `UsesElement → el-background-agents` **[registry]**, `el-langfuse` **[registry]**, `el-hugging-face-hub` **[registry]**;
`el-cli-skill-sandbox-agent` `UsesElement → el-workflow-then-agent-choice`, `el-agent-skills` **[registry]**, `el-glm-52` **[registry]**, `el-thinning-harness` **[registry]**;
`el-undisclosed-agent-outreach` `UsesElement → el-cli-skill-sandbox-agent`;
`el-daily-papers-bot` `UsesElement → el-community-science-outreach-agent`;
`el-cli-skill-sandbox-agent` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**;
`el-undisclosed-agent-outreach` `ExemplifiesPattern → pat-agent-economy` **[registry]**;
`el-community-science-outreach-agent` `ExemplifiesPattern → pat-ai-native-org` **[registry]**.

Reused elements (no new nodes): `el-background-agents` **[registry]**, `el-langfuse` **[registry]**, `el-hugging-face-hub` **[registry]**, `el-agent-skills` **[registry]**, `el-glm-52` **[registry]**, `el-thinning-harness` **[registry]** (the 12,000 → 200 lines story is its cleanest instance), `el-cursor-composer` **[registry]**.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-rogge-huggingface-automate-own-job`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-hugging-face` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-agent-replaced-thousands-of-lines-of-workflow` | harness | The follow-up automation went from a deterministic multi-step workflow to an autonomous agent needing only bash, the Hugging Face CLI, one skill and a sandbox — "because the models have become so good" (Anthropic's own guidance flipped from workflows to agents; Cursor replaced 12,000 lines with a 200-line skill). The scaffolding shrank as the model improved — a practitioner instance of the harness thinning | `ContradictsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-workflow-then-agent-choice`, `el-cli-skill-sandbox-agent`, `el-thinning-harness` **[registry]** |
| `sig-open-models-run-the-outreach-agent` | inference | The agent moved from Claude to GLM 5.2 via Hugging Face inference providers (Together, Fireworks, Cerebras behind one compatible endpoint) — "beats Opus 4.8 on Cursor's bench and is cheaper… there's no reason not to use it." Open models "are getting great — GLM 5.2, DeepSeek V4 — we are able to replace closed models with open ones" for this class of background agent | `FormsPattern → pat-sovereign-ai` **[registry]**; `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-cli-skill-sandbox-agent`, `el-glm-52` **[registry]** |
| `sig-undisclosed-agents-do-research-outreach-at-scale` | | Thousands of GitHub issues opened by an undisclosed agent, two negative replies, Apple and DeepMind researchers answering, an OCR company migrating all its models, model cards auto-completed — and researchers increasingly answering with their own agents. Agents acting as first-class participants in the research ecosystem, on the participant's own name, with human-level acceptance | `FormsPattern → pat-agent-economy` **[registry]** | `OnElement → el-undisclosed-agent-outreach` |
| `sig-a-nightly-cron-agent-scaled-a-team` | | One engineer's outreach job — hundreds of papers a day — now runs as a nightly cron workflow plus an on-demand agent fan-out, with a 90K-follower X account on the same pipeline "without any involvement of me." The community-science team is, operationally, one person plus background agents | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-community-science-outreach-agent`, `el-daily-papers-bot`, `el-background-agents` **[registry]** |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-the-harness-thins-when-the-model-permits` | The durable observation is the reversal over one year: the deterministic workflow was the right call in 2024 (per the lab's own advice) and the wrong call in 2025, when the same lab said agents may beat workflows and the scaffolding collapsed to a CLI, a skill and a sandbox. Harness weight is a function of model capability at the moment of building, which is why "build before you buy" and "revisit every six months" (Box, b22) both hold | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-workflow-then-agent-choice`, `el-cli-skill-sandbox-agent`, `el-thinning-harness` **[registry]** |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-rogge-huggingface-automate-own-job`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-automate-a-repetitive-outreach-job` | Workflow first, then a CLI+skill agent when the models allow | Write down your own steps and replicate them as a deterministic workflow of LLM API calls with no framework; deploy it as a **nightly cron** (GitHub Actions is a generous free start) and trace it (Langfuse) to see prompts, outputs, cost and latency; when models are good enough, replace multi-step custom code with an **autonomous agent** — bash plus your product's CLI as the tool, one skill, a sandbox per unit of work (Modal batch), results posted to Slack; run it on **open models** through an inference-provider aggregator and re-benchmark cost; invoke fan-outs from a coding-agent skill; keep evals to avoid posting slop; and decide deliberately whether to disclose the agent | `ReferencesElement → el-community-science-outreach-agent`, `el-workflow-then-agent-choice`, `el-cli-skill-sandbox-agent`, `el-undisclosed-agent-outreach` |

## Dropped

- **The Belgium intro** — color.
- **Hub metadata/tag mechanics** — folded into the company reuse and the outreach element.

## Review notes

1. **⚑ `ContradictsPattern → pat-harness-over-model`** is deliberate: the clearest first-person "harness thinned as the model improved" story (12,000 → 200 lines; workflow → CLI+skill), alongside the corpus's earlier "harness thins as model improves" counters. Keeps the pattern honestly contested.
2. **Ethics note for review:** undisclosed agent outreach at scale is a practice claim, not endorsed by the corpus; recorded as a signal because of its acceptance data (2 negatives in thousands).
3. **⚠ Verify before seeding:** GLM 5.2 vs Opus 4.8 on Cursor's bench, "90,000 followers," "60+ upvotes," the Cursor 12,000→200 figure, the Hamel Husain reference.
