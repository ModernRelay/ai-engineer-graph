# SPIKE extraction — "How do you diffuse AI into the real world?" (Varun Shenoy, Long Lake) — FOR REVIEW

Source transcript: `transcripts/shenoy-longlake-diffuse-ai-real-world.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/B0fjR3yaZFU — AI Engineer World's Fair, published 2026-08-28.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a co-founder of Long Lake — which raised $3B+ and **acquires** services businesses (35 so far; a $6.3B take-private of Amex Global Business Travel) rather than selling them software — on AI diffusion as "the single most important problem for the next 20 years." Three lessons from owning the outcomes: agents climb a ladder from copilot to coworker and must *earn the right to do more*; real-work traces become ground-truth evals and post-training data no lab has; continual learning and enablement are one loop, and it only closes if you "touch grass" — embed in Excel/ERP/Outlook and show up in person. Caption garbles: "paralyzing"/"paralyze" → **parallelizing**, "Cloud code"/"Claude co-work" kept, "Jensen" → Jensen Huang.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-shenoy-longlake-diffuse-ai` | How do you diffuse AI into the real world? (Varun Shenoy, Long Lake — AI Engineer World's Fair) | youtube | https://youtu.be/B0fjR3yaZFU |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-varun-shenoy`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-varun-shenoy` | Varun Shenoy (Co-founder, Long Lake) | `AffiliatedWithCompany → co-long-lake` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-long-lake` | Long Lake | investor | Raised $3B+ (Elad Gil, General Catalyst, AlphaWave); acquires and operates services businesses — 35 across HOA/property management, architecture, HR services — plus the $6.3B take-private of American Express Global Business Travel; ~40% of staff in technology; ex-Palantir/Ramp/Glean/Blackstone; coerced acquirer-operator → investor. "We are not the vendor, we are the operator-owners" |

Referenced, not coined: American Express GBT, Palantir, Ramp, Glean, Blackstone (staff origins), the property-management firm in the opening.

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-ai-diffusion-problem` | AI diffusion is a generation-long problem | concept | | Everyone has seen the demo; walk into a 200-person property-management firm and nothing has changed — "totally normal, what we should expect" for a general-purpose technology. Electricity was demoed at Pearl Street in the 1880s; a Ford electrified moving assembly line is 1924: rip out the motors, bring in new equipment, train everyone. "AI diffusion is perhaps the single most important problem for the next 20 years" |
| `el-copilot-to-coworker-ladder` | The copilot-to-coworker ladder | concept | harness | Copilot (RAG chatbot) → synchronous agent (Claude Code/Codex/Cowork, 1–5 min, still you query) → asynchronous agent (background, externally triggerable, proactive from a job queue) → long-running agent (hours to months — "a core problem the labs are focused on, as are we") → AI coworker. Everyone sells the coworker; "you have to earn the right to do more" — the model isn't there for some tasks and the company must be walked up the rungs |
| `el-async-agents-for-services-work` | Asynchronous agents for serial work | concept | harness | For code the async rung is solved: wrap the coding agent in a sandbox, let it run, get a PR; engineers already parallelize ("job seven finishes before job three"). Services work is serial (an inbox, one email at a time). Open questions: represent knowledge work as code so coding agents can do it now; parallelize traditionally serial work; find form factors per industry — the code launcher won't work for architecture or property management |
| `el-real-work-traces-flywheel` | Real-work traces as evals and training data | concept | data-eng | The most valuable tasks are not on the internet (closing the books with missing receipts, scoping a blueprint, coordinating a roof repair) — they live in heads and 20-year-old software. Agents collaborate with employees on real work → rich traces (tool calls, hiccups, papercuts) → real-world evals with ground truth (did the roof get repaired?) → hill-climbing; every week's benchmark becomes a regression test. Explicit and implicit feedback (the diff between AI output and what was submitted); internal post-training on out-of-distribution business data; customization per company, per user, per client. "The exceptions are the job" |
| `el-software-service-co-design` | Extreme software–service co-design | concept | | Continual learning (research/platform) and enablement (growth/deployment) are usually siloed; they are one loop: more usage → learning → better agent → more usage. The elephant: initial usage never just shows up — "the person who's closed the books for 20 years keeps doing it the same way." Nvidia's hardware–software co-design applied to software and process: embed into Excel, the ERP, 3D design tools, Outlook; get on a plane, do lunch-and-learns, run a stand at their conference, sit one-on-one. "You cannot co-design with a services business over Zoom" |

Element edges: all five `IdentifiedInArtifact → ia-aie-shenoy-longlake-diffuse-ai`.
`el-copilot-to-coworker-ladder` `UsesElement → el-background-agents` **[registry]**, `el-agentic-spectrum` **[registry]**;
`el-async-agents-for-services-work` `UsesElement → el-copilot-to-coworker-ladder`;
`el-software-service-co-design` `UsesElement → el-real-work-traces-flywheel`, `el-forward-deployed-engineering` **[registry]**;
`el-real-work-traces-flywheel` `UsesElement → el-agent-execution-traces` **[registry]**, `el-golden-dataset` **[registry]**;
`el-ai-diffusion-problem` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**;
`el-real-work-traces-flywheel` `EnablesPattern → pat-continual-learning-turn` **[registry]**;
`el-software-service-co-design` `ExemplifiesPattern → pat-ai-native-org` **[registry]**.

Reused elements (no new nodes): `el-background-agents` **[registry]**, `el-agentic-spectrum` **[registry]**, `el-forward-deployed-engineering` **[registry]** (the owner-operator model is FDE taken to ownership), `el-agent-execution-traces` **[registry]**, `el-golden-dataset` **[registry]**.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-shenoy-longlake-diffuse-ai`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-long-lake`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-ai-diffusion-is-the-twenty-year-problem` | | "The models are going to keep getting better. The big question is how we get them into the real world." A $3B operator of 35 acquired services businesses reports that outside the demo nothing has changed in the average firm, and argues this is the expected shape of a general-purpose technology (electricity took 40 years from Pearl Street to the electrified assembly line). Diffusion, not capability, is the bottleneck for two decades | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-ai-diffusion-problem` |
| `sig-owner-operator-deploys-ai-into-acquired-businesses` | | A new deployment model: instead of selling software, acquire the services business and deploy AI from inside — "when the AI doesn't work, it's not their problem, it's our problem." More than half the team is technology staff deploying products into the field; the largest bet is a $6.3B take-private of the world's biggest corporate-travel platform. Forward-deployed engineering taken all the way to ownership | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-software-service-co-design`, `el-forward-deployed-engineering` **[registry]** |
| `sig-earn-the-right-to-more-autonomy` | harness | The copilot → sync → async → long-running → coworker ladder, with the operator's rule that you must earn each rung: models aren't there for some tasks, and the company has to be walked up. The async rung is solved for code (sandbox + PR; engineers already parallelize) and open for services (serial work, per-industry form factors) — "what does the forking mechanism for code look like for the rest of the world?" | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-copilot-to-coworker-ladder`, `el-async-agents-for-services-work` |
| `sig-real-work-traces-become-regression-tests` | data-eng | Because they own the work, Long Lake generates what no lab has: traces of agents doing real services tasks with ground truth (was the roof repaired? did the books close?), scored automatically, with implicit feedback from the diff between AI output and what was actually submitted. Weekly hill-climbing benchmarks become regression tests; internal post-training runs on out-of-distribution business data; agents are customized per company, user and client | `FormsPattern → pat-continual-learning-turn` **[registry]**; `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-real-work-traces-flywheel`, `el-agent-execution-traces` **[registry]** |
| `sig-enablement-and-continual-learning-are-one-loop` | | Continual learning and enablement are owned by different teams everywhere, but "the agent only improves if people use it, and people only use it if it's worth adopting" — one snowball. The missing piece is initial usage, which "never just shows up"; the fix is software–service co-design under one roof: products embedded in Excel/ERP/Outlook and people on planes doing lunch-and-learns and one-on-ones. "To get AI diffusion to work, you have to touch grass" | `FormsPattern → pat-continual-learning-turn` **[registry]**; `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-software-service-co-design` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-diffusion-is-the-bottleneck-not-capability` | The durable claim is temporal: general-purpose technologies take a generation to diffuse because adoption means ripping out equipment and retraining people, not because the technology is weak — so the binding constraint on AI's economic effect is deployment into firms that "still do things the same way," and the labs' capability curve is nearly irrelevant to it. Long Lake's answer (own the business, embed the product, show up) is the most extreme form of the corpus's FDE thesis | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-ai-diffusion-problem`, `el-software-service-co-design`, `el-copilot-to-coworker-ladder` |
| `ins-owning-the-work-owns-the-data` | The operator model's second dividend: owning the work means owning ground-truth traces of tasks that are not on the internet, which turns enablement (people using the agent) directly into evals, regression suites and post-training data. The accumulation loop the corpus keeps describing is, here, a property of the business structure rather than of the model | `HighlightsPattern → pat-continual-learning-turn` **[registry]** | `ReliesOnElement → el-real-work-traces-flywheel`, `el-software-service-co-design` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-shenoy-longlake-diffuse-ai`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-diffuse-ai-into-a-services-business` | Earn the rungs, own the traces, touch grass | Don't start at the AI coworker — climb copilot → synchronous → asynchronous → long-running, earning each rung by proving value and walking the business up with you; for services work, represent knowledge work as code so coding agents can do it, find how to parallelize serial work, and choose form factors per industry; have agents collaborate with employees on real work and **capture the traces** (tool calls, hiccups, the diff between AI output and what was submitted) as ground-truth evals that become weekly regression tests, and post-train on your out-of-distribution business data; customize per company, per user and per client; treat continual learning and enablement as one loop owned together; embed products where people already work (Excel, ERP, 3D tools, Outlook) to keep the enablement energy low; and show up in person — lunch-and-learns, their conferences, one-on-ones — because co-design doesn't happen over Zoom or support tickets | `ReferencesElement → el-copilot-to-coworker-ladder`, `el-async-agents-for-services-work`, `el-real-work-traces-flywheel`, `el-software-service-co-design` |

## Dropped

- **The team-composition slide** (ex-founders, ex-military, Palantir/Ramp/Glean, Blackstone/H.I.G.) — in the company row.
- **The "bike on a slope vs hills and ravines" image** — folded into `el-real-work-traces-flywheel` ("the exceptions are the job").

## Review notes

1. **⚑ `pat-fde-rise` ledger (uncoined):** the owner-operator model is forward-deployed engineering pushed to its limit — the vendor becomes the owner. Strong addition to the coin case, alongside Lovejoy (b22).
2. **`co-long-lake` typed `investor`** (acquirer/holding company); it behaves as an operator — review may prefer `developer`.
3. **⚠ Verify before seeding:** $3B raised, 35 acquisitions, the $6.3B Amex GBT take-private, "~40% technology team."
