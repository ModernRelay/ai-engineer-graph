# SPIKE extraction — "How Anthropic Builds: Lessons from Labs" (Mike Krieger, Anthropic — keynote conversation) — FOR REVIEW

Source transcript: `transcripts/krieger-anthropic-how-anthropic-builds.txt` (auto-captions — quotes are paraphrases, not verbatim; an interview format with the conference host).
Video: https://youtu.be/qqrk7CtkuIw — AI Engineer World's Fair, published 2026-08-27.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-27 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the Instagram co-founder, now a member of technical staff running Anthropic Labs (after two years as CPO), on how Anthropic builds: delegation shifted from task breakdown to **expressing the end state**; users and product teams must be taught to be **unreasonable** because first-generation AI products "put the model in a box"; ~60% of Anthropic's code is written via **Claude Tag** in a multiplayer, async, proactive mode; the bottleneck is human ability to conceptualize changes, hence **Claude Code artifacts** (intent and trade-offs instead of 2,000-line diffs); Labs runs two-week **persevere-or-pivot** reviews over "bets" with DRIs who manage no one; primitives get **unshipped** (styles → skills); startups win on user understanding because "writing code was never the limiting part"; finance needs verifiability without constraining agentic workloads. Caption garbles: "Fable"/"Mythos" kept (model names), "Bun Zig to Rust" kept, "Monkey Type" → **MonkeyType**, "Cloud Design"/"cloud code" → **Claude Design / Claude Code**, "Chris Lovejoy" → Christopher Lovejoy (b22), "Pinterest" → ⚠ mis-caption for Anthropic, "Tariq" → the prior keynote's "be unreasonable."

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-krieger-anthropic-how-anthropic-builds` | How Anthropic Builds: Lessons from Labs (Mike Krieger, Anthropic — AI Engineer World's Fair keynote) | youtube | https://youtu.be/qqrk7CtkuIw |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-mike-krieger`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-mike-krieger` | Mike Krieger (Member of Technical Staff / Anthropic Labs; ex-CPO; co-founder of Instagram) | `AffiliatedWithCompany → co-anthropic` **[seed]** |

## Companies (0 new)

Reused **[seed]**, edge-only: `co-anthropic` — new facts: ~60% of code written via Claude Tag; Labs runs two-week persevere-or-pivot reviews over bets, shutting projects down "basically every cycle"; shipped Claude Code artifacts and Claude Design (second major release in June); a "project unship" channel; former CTOs joining as ICs; hired Christopher Lovejoy for healthcare. Reused `co-meta` **[seed]** (Instagram's MonkeyType, rollouts and dynamic config as the precedent), `co-anterior` **[b22]** (Lovejoy's prior company). Referenced, not coined: Midjourney (Discord multiplayer analogy), Notion, Bun.

## Elements (6 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-express-the-end-state` | Express the end state | concept | harness | The delegation shift as models reached the Mythos/Fable snapshots: from "break the idea into steps in my head and iterate" to "describe the goal, let it work, discuss trade-offs and questions along the way, then figure out where it landed." The model is "way smarter than me" — "explain it to me like I'm a little dumber than you are." Former CTOs are joining Anthropic as ICs because the building is that interesting |
| `el-be-unreasonable` | Be unreasonable | concept | | First-generation AI products "put the model too much in a box" — constrained tools and degrees of freedom made it hard to be unreasonable ("I can write code but can't really run it"). Cowork giving every knowledge worker a VM that can run bash looks excessive until the model remediates its own PDF-parsing failure with a script. Teach users and product teams to ask for more; a non-technical colleague asking for changes was told "why don't you ask Claude?" Personal extreme: porting a couple-hundred-thousand-line Python codebase to TypeScript over a weekend via a dynamic workflow that ported, verified, cross-read and churned until Monday |
| `el-tag-multiplayer-delegation` | Multiplayer delegation via Claude Tag | concept | harness | ~60% of Anthropic's code is written via tagging: Claude Code for high-bandwidth interactive iteration, but most usage is delegation in shared channels — like Midjourney on Discord, everyone sees how others use it, which spreads ambition: "don't just fix this bug — you're responsible for this part of the codebase, monitor this feedback channel, proactively take on tasks." The advanced version is a teammate that holds context, has memory and is proactive: "much more multiplayer async proactive than everyone in their own CLI" |
| `el-intent-artifacts-over-diffs` | Intent artifacts over diffs | concept | harness | Still bottlenecked on review for architectural changes — "and more subtly, on human ability to even fully conceptualize what we're doing." A 2,000-line PR "looks like code to me," so Claude Code artifacts ship the explanation, intention and trade-offs; code stays verifiable by tooling, humans discuss intent and trade-offs and measure in production. Krieger's own review: "I talk to Claude about the code — these are the questions I'd have, go investigate" — Claude-powered, human-driven; cosmetic changes fix forward. Instagram-era priors: pre-measure everything, first-class flags and dynamic config; MonkeyType's runtime-type capture as a model for production-data-guided conversions |
| `el-labs-persevere-or-pivot` | Labs: bets, persevere-or-pivot, DRIs who manage no one | concept | | Labs' cadence is a two-week review of every project — persevere, pivot, or shut down — and projects are shut down nearly every cycle; the intention is to prototype quickly, ship internally, maybe early access, and wind down what doesn't work. Aligning the org chart to projects would mean re-orging biweekly, so a pod for each "bet" draws people from product and engineering with a bet lead / DRI who usually manages none of them; engineering managers coach and keep everyone on what excites them. "Loose until it solidifies" — once a product has legs (Claude Design) it gets a dedicated, hired team. "The death of the engineering manager has been greatly exaggerated" |
| `el-unship-previous-generation-primitives` | Unship the previous generation's primitives | concept | | A "project unship" channel asks what should leave the product: styles (small usage, prescriptive) were unshipped because skills do it better — "take the primitives of one generation of AI and unship or supplant them with the next." The biggest deletion candidate is product complexity itself: the code / cowork / chat distinctions don't interoperate, can't delegate to each other, and "the average person could not explain why those are different" — pasting a Cowork plan into Claude Code "is a 2020 workflow that shouldn't exist." Claude Design's next steps: surfaces that talk to each other, and the blur from design to persistent, shareable app |

Element edges: all six `IdentifiedInArtifact → ia-aie-krieger-anthropic-how-anthropic-builds`.
`el-tag-multiplayer-delegation` `UsesElement → el-claude-tag` **[registry]**, `el-claude-code` **[registry]**, `el-express-the-end-state`;
`el-intent-artifacts-over-diffs` `UsesElement → el-intent-review-surface` **[registry]**, `el-claude-code` **[registry]**;
`el-be-unreasonable` `UsesElement → el-claude-cowork` **[registry]**, `el-claude-dynamic-workflows` **[registry]**, `el-express-the-end-state`;
`el-unship-previous-generation-primitives` `UsesElement → el-agent-skills` **[registry]**;
`el-labs-persevere-or-pivot` `UsesElement → el-unship-previous-generation-primitives`;
`el-tag-multiplayer-delegation` `ExemplifiesPattern → pat-ai-native-org` **[registry]**;
`el-intent-artifacts-over-diffs` `ExemplifiesPattern → pat-verification-gap` **[registry]**;
`el-be-unreasonable` `ExemplifiesPattern → pat-model-not-bottleneck` **[registry]**.

Reused elements (no new nodes): `el-claude-tag` **[registry]**, `el-claude-code` **[registry]**, `el-claude-cowork` **[seed]**, `el-claude-dynamic-workflows` **[registry]**, `el-intent-review-surface` **[registry, b21]** (Jain's thesis, confirmed from inside the lab as shipped artifacts), `el-agent-skills` **[registry]**, `el-claude-fable` **[registry]**, `el-claude-mythos-preview` **[seed]**.

## Signals (6 new)

All: `SpottedInArtifact → ia-aie-krieger-anthropic-how-anthropic-builds`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-anthropic` **[seed]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-anthropic-writes-sixty-percent-of-code-via-tag` | harness | Inside Anthropic, ~60% of code is written through Claude Tag — multiplayer delegation in shared channels rather than individual CLIs — where seeing a colleague hand Claude responsibility for a codebase area and a feedback channel spreads ambition; the destination is a proactive teammate with memory. "That's really changed how we operate internally" | `FormsPattern → pat-ai-native-org` **[registry]**; `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-tag-multiplayer-delegation`, `el-claude-tag` **[registry]** |
| `sig-bottleneck-is-conceptualizing-not-reviewing` | harness | Anthropic is "still bottlenecked on review" for architectural changes — but more subtly on the human ability to conceptualize what's being built. Hence Claude Code artifacts: send the intention and trade-offs, not the 2,000-line diff; verify code with tooling, discuss intent, measure in production; review becomes a conversation with Claude about the code, human-driven; cosmetic changes fix forward. The lab confirming, as shipped product, b21's "review the intent not the diff" | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-intent-artifacts-over-diffs`, `el-intent-review-surface` **[registry]** |
| `sig-be-unreasonable-the-product-was-the-box` | | The lab's self-critique: first-generation AI products constrained models' tools and degrees of freedom, so users couldn't be unreasonable; giving every knowledge worker a VM with bash looks absurd until it self-remediates. The proof of unreasonableness: a couple-hundred-thousand-line Python→TypeScript port completed over a weekend by a dynamic workflow. The capability was there; the product boxed it | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-be-unreasonable`, `el-express-the-end-state`, `el-claude-dynamic-workflows` **[registry]** |
| `sig-labs-run-two-week-persevere-or-pivot` | | Anthropic Labs reviews every bet every two weeks — persevere, pivot or shut down — and shuts projects down nearly every cycle by design; pods draw from product and engineering with a DRI who manages no one, engineering managers coach, and structure is added only when a product has legs (Claude Design). The org chart is deliberately decoupled from projects so rapid iteration doesn't mean biweekly re-orgs | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-labs-persevere-or-pivot` |
| `sig-writing-code-was-never-the-limiting-part` | | On "why not just join Anthropic": a lab is a platform and will ship "googly" products bound by its integrations; a group of four or five obsessed with a vertical will out-move it on user understanding, reach and iteration — though "some things can be skillified and maybe don't need their own product." Writing code "was never the thing that was going to make or break a startup"; the space and user understanding were | `FormsPattern → pat-value-of-judgement` **[registry]**; `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-express-the-end-state` |
| `sig-unship-the-primitives-collapse-the-surfaces` | | Product design as deletion: unship a prior generation's primitives when the next supplants them (styles → skills), and delete the code/cowork/chat distinctions users can't explain and that can't delegate to each other. The lab reads its own product complexity as the thing holding the model back | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-unship-previous-generation-primitives`, `el-agent-skills` **[registry]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-the-lab-is-bottlenecked-on-humans-too` | The durable datum is that the frontier lab reports the same constraints as its customers: review for architectural changes, the human ability to conceptualize what agents built, product surfaces that box the model, and org structures that would need biweekly re-orgs to keep up. Its answers — intent artifacts, tagging as multiplayer delegation, persevere-or-pivot pods, unshipping — are the AI-native org as practiced by the organization with the least excuse to be bottlenecked | `HighlightsPattern → pat-ai-native-org` **[registry]** | `ReliesOnElement → el-tag-multiplayer-delegation`, `el-intent-artifacts-over-diffs`, `el-labs-persevere-or-pivot` |
| `ins-unreasonableness-is-the-new-product-spec` | "Be unreasonable" reframes the harness question from the lab's side: the boxes early products built around models were the bottleneck, and each generation's primitives (styles, separate surfaces) should be deleted as the model absorbs them — a lab-side endorsement of thinning the harness where capability permits, while still shipping the deterministic parts (flags, measurement, verifiable code) that keep it safe | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-be-unreasonable`, `el-unship-previous-generation-primitives`, `el-express-the-end-state` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-krieger-anthropic-how-anthropic-builds`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-build-like-anthropic-labs` | End states, tagging, intent artifacts, biweekly bets | Delegate by **expressing the end state** and discussing trade-offs, not by decomposing tasks; be unreasonable — give agents real degrees of freedom (a VM that runs code) and teach users and product teams to ask for more; work **multiplayer** — delegate in shared channels where ambition is visible, and grow the agent into a proactive teammate with memory; communicate changes as **intent artifacts** (intention, trade-offs, evidence) rather than raw diffs, verify code with tooling, measure in production, fix forward on cosmetic work; run product bets on a **two-week persevere-or-pivot** cadence with DRIs who don't manage the pod, and add structure only once something has legs; keep a standing **unship** list and delete primitives the next generation supplants; pre-measure everything and keep first-class flags and dynamic config; and remember burnout: no job is so important you can't be offline for a few days, and "you're never as good as your best game or as bad as your worst" | `ReferencesElement → el-express-the-end-state`, `el-be-unreasonable`, `el-tag-multiplayer-delegation`, `el-intent-artifacts-over-diffs`, `el-labs-persevere-or-pivot`, `el-unship-previous-generation-primitives` |

## Dropped

- **The Instagram launch-week scaling stories** (pre-measure, flags, self-DDoS) — one line inside `el-intent-artifacts-over-diffs`.
- **Finance vertical remarks** (verifiability, audit logging and provenance "without constraining agentic workloads"; vertical startups' own evals as a barometer) — noted for the finance track; not extracted.
- **Mental-health close** — one line in the know-how.

## Review notes

1. **⚑ Lab-side confirmation of b21's `el-intent-review-surface`** (Jain/Aviator): Claude Code artifacts ship exactly that surface. Recommend citing in `pat-verification-gap`'s brief.
2. **`pat-fde-rise` ledger (uncoined):** Anthropic hiring Christopher Lovejoy (b22's FDE talk) for healthcare — a third data point this batch pair (Lovejoy, Long Lake, this).
3. **`sig-be-unreasonable-the-product-was-the-box`** sits beside this batch's two harness-thinning counters (Rogge, Bhatawdekar) as a lab-side view that boxes/primitives should be deleted as capability grows; edged to `pat-model-not-bottleneck` rather than as a contradiction, since Krieger keeps the deterministic parts.
4. **⚠ Verify before seeding:** "~60% of code via Tag," the Python→TypeScript port size, "two-week" cadence, Claude Design's June release, and which model snapshot triggered the delegation shift.
