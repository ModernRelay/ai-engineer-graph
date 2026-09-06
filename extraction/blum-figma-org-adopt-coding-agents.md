# SPIKE extraction — "How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage)" (Eyal Blum, Figma) — FOR REVIEW

Source transcript: `transcripts/blum-figma-org-adopt-coding-agents.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/5Bn0xro2ol8 — AI Engineer World's Fair, published 2026-08-28.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a Figma engineer on internal adoption of coding agents while keeping the codebase good. Adoption is a three-act story (quick wins → failure on bigger problems → the real skill), it is uneven across teams, and it creates specific frictions: lost developer agency, the best engineers becoming the bottleneck and the slowest adopters, communication inflating 3–4×. Remedies: invest in verification above all, plan-not-prompt (a week of planning → 20 small PRs overnight, ~5×), attention-aware communication (mark what a human wrote), and put the skeptics in charge of the safety roadmap. Caption garbles: "Alon Blum" → **Eyal Blum** (per the listing), "contacts" → **context**, "bell system" → ⚠ likely **build system**, "Latin hour" → ⚠ unclear (a team session).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-blum-figma-org-adopt-coding-agents` | How to Get Your Org to Adopt Coding Agents (Without Shipping Garbage) (Eyal Blum, Figma — AI Engineer World's Fair) | youtube | https://youtu.be/5Bn0xro2ol8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-eyal-blum`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-eyal-blum` | Eyal Blum (Software Engineer, Figma) | `AffiliatedWithCompany → co-figma` **[registry]** |

## Companies (0 new)

Reused **[registry]**, edge-only: `co-figma` — new facts: "pivoted very strongly from a traditional tool to an AI-first tool"; internal agent adoption is uneven across teams and explicitly "a journey we have not come out the other end of"; cloud-agent automation still limited by build-system dependencies.

## Elements (6 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-three-act-adoption` | The three-act adoption story | concept | | Act one: pick up AI, get simple things working 10× faster. Act two: apply the same practices to bigger problems — "AI fails pretty badly," bugs, trust breaks down. Act three: the real skill — guardrails, prompting, context — that actually scales. Individuals, teams and companies all go through it, at different speeds, and they must ship together |
| `el-uneven-adoption-frictions` | The frictions of uneven adoption | concept | | AI-forward teams coexist with teams still experimenting or who lost confidence. **Reduced developer agency**: engineers who took pride in flow-state coding sit in a prompt cycle waiting on output — less fun, burnout. **The best engineers become the bottleneck**: the ones holding all the context in their heads are "mental duct tape" for every place agents fail, so they carry the burden, see the problems first, and are slowest to adopt. **Communication inflation**: docs, Slack and email are 3–4× longer and 2–3× more numerous while saying the same, and quality markers are harder to read |
| `el-left-shift-verification-to-agents` | Left-shift verification to agents | concept | harness | "Investing in verification is probably the highest-value thing we can do in our codebase." Every check that moves from a human to an agent is a win (Playwright + MCP letting the agent explore instead of a human). When the agent finds something useful, encode it into a deterministic, repeatable flow — tokens and time saved, and the LLM is used only where reasoning is needed. Ask the agent to write tests first (red → green) so code fits the verification criteria rather than tests fitting the code. Testing pyramid: deterministic analysis (lint, compiler, unit tests) at the bottom, agent review on encoded architectural standards in the middle, humans only at the top for functionality and "is this the right thing to build" |
| `el-plan-over-prompt` | Plan, don't prompt | concept | harness | Spend a week writing a detailed plan — decisions made, iterated, reviewed by teammates — then hand it to the agent to implement overnight. A good plan starts with the **why** (an executive summary the agent must not rewrite — prevents drift), breaks into phases each independently verifiable with a validation gate (no stage built on unvalidated assumptions), sized by the **coffee test** — if you'd need a coffee before reviewing that PR, it's too big; then each phase fits a sub-agent. Result: ~20 PRs of 10–100 lines from one plan; six weeks of coding in one week — ~5× including review. Restores the joy of building; workflows can vary per person, with diminishing returns to centralizing |
| `el-attention-aware-communication` | Attention-aware communication | concept | | Human attention is the scarce resource, so mark what was generated by AI versus written by a human so readers know how much time to spend and how much slop to expect. Team convention: every PR description opens with a hand-written paragraph, then the AI description; same in Slack and email. Cautionary tale: sending a senior skeptic an AI-generated analysis without marking it — "I did not expect somebody I respect this much to send me something this sloppy" — fixed by labeling intent: this is mine, this is the AI's, here is the feedback I need |
| `el-skeptics-own-the-safety-roadmap` | Put the skeptics in charge of the roadmap | concept | | The skeptical, most-burdened engineers see exactly where validation is lacking and where tools fail — their feedback *is* the roadmap for making AI safe in the codebase. Bring them in and let them own it rather than trying to make them use AI; they come along when the improvements make their lives better. Meanwhile normalize use where people already are: tag the agent in a Slack thread ("let's see if it can get it this time") and let it close the loop |

Element edges: all six `IdentifiedInArtifact → ia-aie-blum-figma-org-adopt-coding-agents`.
`el-uneven-adoption-frictions` `UsesElement → el-three-act-adoption`, `el-slop-as-unread-code` **[registry]**;
`el-left-shift-verification-to-agents` `UsesElement → el-generator-validator-separation` **[registry]**, `el-agent-hooks` **[registry]**;
`el-plan-over-prompt` `UsesElement → el-spec-driven-development` **[registry]**, `el-left-shift-verification-to-agents`;
`el-skeptics-own-the-safety-roadmap` `UsesElement → el-uneven-adoption-frictions`;
`el-attention-aware-communication` `UsesElement → el-uneven-adoption-frictions`;
`el-left-shift-verification-to-agents` `ExemplifiesPattern → pat-verification-gap` **[registry]**;
`el-plan-over-prompt` `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-uneven-adoption-frictions` `ExemplifiesPattern → pat-ai-native-org` **[registry]**.

Reused elements (no new nodes): `el-slop-as-unread-code` **[registry]**, `el-generator-validator-separation` **[registry]**, `el-agent-hooks` **[registry]**, `el-spec-driven-development` **[registry]** (the plan discipline is its practical form — with the validation gates b21's critique said it lacked), `el-software-factory` **[registry]**.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-blum-figma-org-adopt-coding-agents`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-figma` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-adoption-is-a-three-act-story` | | Figma's internal observation: every individual, team and company goes through quick wins → failure at scale and broken trust → the real skill of guardrails, prompting and context. Adoption is uneven — AI-forward teams and teams that lost confidence must ship the same product together — and "this is the biggest change by orders of magnitude in 15 years in the valley, in culture and technology" | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-three-act-adoption`, `el-uneven-adoption-frictions` |
| `sig-best-engineers-become-the-bottleneck` | | The counter-intuitive friction: the engineers holding the most context become "mental duct tape" for every place agents fail, absorb the burden, see the problems first and adopt slowest — while communication inflates 3–4× and developer agency and job satisfaction drop. The dysfunction side of the AI-native org, observed from inside an AI-first company | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-uneven-adoption-frictions`, `el-slop-as-unread-code` **[registry]** |
| `sig-verification-is-the-highest-value-investment` | harness | "Anytime we can left-shift a check from a human to an agent, that's a big win," then encode what the agent found into a deterministic flow; tests first so code fits the criteria; a pyramid where lint/compiler/unit tests and encoded-standard agent review leave humans only functionality and "is this the right thing." Verification, not generation, is where Figma puts its engineering | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-left-shift-verification-to-agents`, `el-generator-validator-separation` **[registry]** |
| `sig-plans-restore-developer-agency` | harness | A week of planning (why at the top, independently verifiable phases, coffee-test PR sizing, teammate review) then overnight implementation into ~20 small PRs — six weeks of coding in one week, ~5× including review — and the joy of building returns because the decisions are the craft. Planning is where the human's judgement lives; the loop underneath can be any workflow | `FormsPattern → pat-value-of-judgement` **[registry]**; `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-plan-over-prompt`, `el-spec-driven-development` **[registry]** |
| `sig-mark-what-the-human-wrote` | | Attention-aware communication as culture: label AI-generated versus human-written text in PRs, Slack and email so readers allocate scarce attention and expect the right amount of slop — and let skeptics own the safety roadmap, since their objections map exactly where validation is missing. Culture change "is just as important as the engineering challenges" | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-attention-aware-communication`, `el-skeptics-own-the-safety-roadmap` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-verification-is-the-adoption-lever` | The durable claim connects the org problem to the engineering one: uneven adoption and skeptical senior engineers are symptoms of missing verification, so the highest-leverage investment is moving checks to agents and encoding discoveries as deterministic gates — which is also what turns the skeptics into the roadmap. Trust in agents is built at the bottom of the testing pyramid, not by persuasion | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-left-shift-verification-to-agents`, `el-skeptics-own-the-safety-roadmap`, `el-uneven-adoption-frictions` |
| `ins-the-plan-is-the-new-craft` | Planning-then-delegating (why, verifiable phases, review-sized PRs) is where developer agency and judgement relocate once implementation is delegated — the same "judgement is the value" thesis the corpus holds, here with a measured ~5× and a stated reason it restores job satisfaction. The plan is the artifact humans should be proud of | `HighlightsPattern → pat-value-of-judgement` **[registry]** | `ReliesOnElement → el-plan-over-prompt`, `el-attention-aware-communication` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-blum-figma-org-adopt-coding-agents`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-adopt-coding-agents-without-shipping-garbage` | Verify first, plan not prompt, mark your words, empower the skeptics | Expect three acts (wins, failure at scale, real skill) and uneven speeds across teams; make **verification** the top investment — move every check you can from humans to agents, encode what the agent discovers as deterministic repeatable flows, have agents write tests first (red → green), and keep humans only for functionality and "is this the right thing"; **plan, don't prompt** — a detailed plan with the why at the top, phases each independently verifiable with a validation gate, sized by the coffee test, reviewed by teammates, then handed to an agent overnight for small PRs; let people keep their own workflows (diminishing returns to centralizing); practice **attention-aware communication** — hand-written summary first, AI text after, in PRs, Slack and email; put the **skeptics in charge** of the safety roadmap because their objections are the map of missing validation; and normalize everyday use by tagging the agent in the Slack thread to close the loop | `ReferencesElement → el-left-shift-verification-to-agents`, `el-plan-over-prompt`, `el-attention-aware-communication`, `el-skeptics-own-the-safety-roadmap`, `el-three-act-adoption` |

## Dropped

- **Figma product pivot framing** — one line in the company reuse; the talk is explicitly about the internal org.
- **The plan screenshot / brag slide** — figures folded into `el-plan-over-prompt`.

## Review notes

1. **`sig-best-engineers-become-the-bottleneck`** is a new dysfunction datum for `pat-ai-native-org` (with Hong's "reviewing slop" and Hall's token-maxing from b22): the context-holders adopt last.
2. **`el-plan-over-prompt` vs `el-spec-driven-development` (b9) and b21's critique** — Blum's version has the feedback loop b21 said was missing (validation gates per phase). Recommend widening the b9 element rather than a new thread.
3. **⚠ Verify before seeding:** the ~5× / six-weeks-in-one figure, "3–4× longer" communications, and the speaker's first name (captions say Alon).
