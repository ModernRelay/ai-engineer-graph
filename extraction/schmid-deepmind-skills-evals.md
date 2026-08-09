# SPIKE extraction — "Don't Ship Skills Without Evals" (Philipp Schmid, Google DeepMind) — FOR REVIEW

Source transcript: `transcripts/schmid-deepmind-skills-evals.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/0vphxNt4wyk — AI Engineer World's Fair, published 2026-07-14.
`stagingTimestamp` for the artifact and all signals: 2026-07-14 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-schmid-skills-evals` | Don't Ship Skills Without Evals (Philipp Schmid, Google DeepMind — AI Engineer World's Fair) | youtube | https://youtu.be/0vphxNt4wyk |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-philipp-schmid`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-philipp-schmid` | Philipp Schmid (Google DeepMind, Germany; works on Gemini API and agents) | `AffiliatedWithCompany → co-google-deepmind` **[registry]** |

## Companies (0 new)

- **[registry]** `co-google-deepmind` — reused.

## Elements (2 new, 2 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-skillsbench` | SkillsBench | framework | harness | Public benchmark/leaderboard for agent skills: indexed ~50,000 skills from GitHub; v1.1 evaluates open and closed models across multiple harnesses on ~100 coding/productivity tasks; open to community contributions. Headline findings: skills lift performance ~15% on average; human-written skills beat AI-generated (which can hurt); skill.md should stay under ~500 lines |
| `el-capability-preference-skills` | Capability vs preference skills | concept | harness | Two-class taxonomy for agent skills: capability skills teach a model what it can't yet do consistently — temporary by design, retired as models improve (evals tell you when); preference skills encode company/team-specific workflows, style, and references — durable, never absorbed by foundation models, and protected by evals against regression on agent updates |
| **[registry]** `el-agent-skills` | — | — | — | reused; the talk's core subject (folder + skill.md + assets) |
| **[registry]** `el-progressive-disclosure` | — | — | — | reused; the three-layer skill structure (description in always-on context → skill body → reference files) |

Element edges: both new elements `IdentifiedInArtifact → ia-aie-schmid-skills-evals`; `el-skillsbench` `ExemplifiesPattern → pat-verification-gap`; `el-capability-preference-skills` `UsesElement → el-agent-skills`.

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-schmid-skills-evals`, `SourcedFromSource → source-aie-yt`.

| slug | name / brief | FormsPattern | RelevantCompany | OnElement |
|---|---|---|---|---|
| `sig-skills-shipped-untested` | Of ~50,000 skills SkillsBench indexed from GitHub, almost none had evals; most were AI-written and untested — and given agent non-determinism you can't tell whether a task failed because the skill is bad or the task too hard. A whole distribution layer shipping unverified behavior | `pat-verification-gap`, `pat-agent-supply-chain` | — | `el-skillsbench`, `el-agent-skills` |
| `sig-skillsbench-15pct-lift` | SkillsBench 1.1 across open/closed models and multiple harnesses: skills improve task performance ~15% on average over ~100 tasks; human-written skills are the best available, AI-generated skills can degrade performance; keep skill.md under ~500 lines | `pat-harness-over-model` | — | `el-skillsbench` |
| `sig-deepmind-skill-eval-gates` | Google DeepMind now keeps evals alongside every internal skill and gates changes on them: any diff to a skill file triggers the eval run, and the change does not merge unless it improves (or extends) the test cases — skills regression-tested exactly like code | `pat-verification-gap` | `co-google-deepmind` | `el-agent-skills` |
| `sig-gemini-interactions-skill` | DeepMind built a skill for the Gemini Interactions API (released after Gemini 3's training cutoff, so the model has zero knowledge of it): 117 test cases from real user data, synthetic generation, and user feedback drove valid-code generation to ~90% with latest models; ~50% of observed failures were trigger failures — the skill description too weak for shallow end-user prompts | `pat-harness-over-model` | `co-google-deepmind` | `el-agent-skills` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-evals-outlive-skills` | Capability skills are depreciating assets — temporary patches over model gaps, retired surprisingly fast as models update ("needed six months ago, not today"); the eval is the durable asset: keep it after retiring the skill, use it to detect degradation, and reintroduce the skill only when the eval says so. Run ablations (with/without skill) to know which regime you're in | `pat-verification-gap` | `el-capability-preference-skills` |
| `ins-agents-you-build-vs-use` | The eval bar differs by audience: in agents you use (Cursor, Claude Code), the engineer notices a missed skill trigger and reprompts; in agents you build for customers, users don't know skills exist and never invoke them explicitly — model-triggered activation off shallow prompts is the whole game, so triggering behavior must be eval-verified, not eyeballed | `pat-verification-gap` | `el-agent-skills` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-schmid-skills-evals`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-write-skills` | Write skills as directives, lean and layered | Description is the always-paid token cost — make it directive (why/how/when to use), not essay; keep skill.md lean and push cloud-specific or deep detail into reference files (progressive disclosure); include negative cases ("only for React components", not "web development") to stop over-triggering; set the right freedom level — if the workflow is fixed step-by-step, write a script and tell the model to run it, don't burn tokens; strip no-ops (instructions that change nothing, common in AI-generated skills — per "Matt's" no-op-killer skill); retire skills when ablation evals show the model no longer needs them | `el-agent-skills`, `el-progressive-disclosure` |
| `how-skill-eval-harness` | Build a cheap skill-eval harness before shipping | Start small: 10–20 prompts per skill (≈5 happy-path, ≈5 should-NOT-trigger, plus real production traces when available); encode cases as JSON/YAML — prompt, language, should_trigger, expected checks; most asserts can be regex (correct SDK/model/methods, no legacy patterns) so runs are cheap and repeatable; run the agent (e.g. Gemini CLI) via a basic Python script; use isolated clean workspaces (agents cheat by mining prior chats); run 3–6 trials per case for reliability; test across harnesses and models (good on Gemini may fail on Codex); score outcomes, not paths (don't require skill-load on turn one); escalate to LLM-as-judge with a rubric only for complex trace-level checks; gate every skill change on the eval | `el-agent-skills`, `el-skillsbench` |

## Dropped

- Gemini Interactions API as an Element — it's the eval case study's subject, not a load-bearing industry entity here; kept as prose in `sig-gemini-interactions-skill`.
- "Matt" and his no-ops skill/repo — unresolvable from captions (no surname); kept as attributed prose in `how-write-skills`, flagged below.
- Model-triggered vs user-invoked skills distinction — folded into `ins-agents-you-build-vs-use` and the knowhow.
- Named harnesses (Antigravity, Cursor, Claude Code, Codex, Gemini CLI) — prose only.

## Review notes

1. "Skill Bench"/"skills bench" in captions: rendered as SkillsBench (`el-skillsbench`). Its maintainer is not stated — no `DevelopedByCompany` edge; verify official name/spelling before seeding.
2. "Matt, a great AI educator" who published the no-ops finding — surname never given in captions; likely identifiable from the blog post Schmid mentions, but I did not coin an Expert on a first name. Flag for resolution.
3. The ~15% lift, <500-line threshold, 117 test cases, ~90% valid-code rate, and 50%-trigger-failure figures are speaker-cited; the 15% figure is attributed to SkillsBench 1.1, the rest to DeepMind internal work.
4. `sig-skillsbench-15pct-lift` on `pat-harness-over-model`: skills are harness-side scaffolding lifting outcomes without touching the model — reads as core evidence to me, but it's the least "change-over-time" of the four signals; drop to prose if it fails the signal bar.
5. LLM-as-judge mention is generic; I did not link registry `el-judge-as-classifier` (that element carries a specific classifier framing from another talk).
