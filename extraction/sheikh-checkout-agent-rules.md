# SPIKE extraction — "Your coding agent doesn't always follow your rules" (Talha Sheikh, Checkout.com) — FOR REVIEW

Source transcript: `transcripts/sheikh-checkout-agent-rules.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/MpZzWMdmQCE — AI Engineer World's Fair, published 2026-07-08.
`stagingTimestamp` for the artifact and all signals: 2026-07-08 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-sheikh-agent-rules` | Your coding agent doesn't always follow your rules (Talha Sheikh, Checkout.com — AI Engineer World's Fair) | youtube | https://youtu.be/MpZzWMdmQCE |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-talha-sheikh`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-talha-sheikh` | Talha Sheikh (engineer at Checkout.com; built the Vector Harness deterministic verification layer for coding agents) | `AffiliatedWithCompany → co-checkout-com` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-checkout-com` | Checkout.com | developer | Global payments company (fintech — enum lacks the category); appears as an enterprise building its own internal agent-enforcement tooling, not as an AI vendor |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-vector-harness` | Vector Harness | product | harness | Deterministic post-completion verification harness for coding agents: a Claude hook fires when the session ends, runs config-defined test cases against the agent's claimed-done output, and on failure feeds "this is failing — try again" back to the agent until checks pass; positioned as an enforcement contract (given task → fulfill these checks; the middle is developer-defined), runnable at every level (conversation end, pre-commit, multi-agent steps, async agents, optional LLM-as-judge); public |

Element edges: `el-vector-harness` `IdentifiedInArtifact → ia-aie-sheikh-agent-rules`; `UsesElement → el-agent-hooks` **[registry]**; `ExemplifiesPattern → pat-verification-gap` **[registry]**.
Also reused: `el-generator-validator-separation` **[registry]**, `el-harness-engineering` **[registry]**, `el-claude-code` **[registry]** (edges below).

## Signals (4 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-sheikh-agent-rules`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-vector-diy-enforcement` | A Checkout.com engineer built Vector after repeated "task completed" claims from Claude Code failed on actual run — realization: "I am the enforcement layer"; hook-triggered deterministic checks plus an automatic retry loop replaced him as the checker; framed as trust, not capability: "not whether Claude can do the task — can I trust it to" | `FormsPattern → pat-verification-gap` | `OnElement → el-vector-harness`; `OnElement → el-agent-hooks` **[registry]**; `OnElement → el-claude-code` **[registry]**; `RelevantCompany → co-checkout-com` |
| `sig-lab-predicts-enforcement-obsolete` | An Anthropic engineer told the speaker enforcement layers won't be needed — "another model will be so smart you won't need enforcement" — alongside a teased super-capable release (captions: "project Claude Swing … Project Methuselah", garbled — see note 1); speaker's counter, delivered as the talk's thesis: each model generation raises capability, which is not the same axis as reliability | `FormsPattern → pat-verification-gap` | `RelevantCompany → co-anthropic` **[registry]** |
| `sig-guardrails-downshift-models` | With deterministic guardrails in the harness, smaller/cheaper models (Haiku-class, open-source) still converge on the wanted output; more guardrail investment → drastically cheaper runs (plus async execution) vs defaulting to a frontier Opus-class model — verification spend substitutes for model spend | `FormsPattern → pat-harness-over-model` | `OnElement → el-vector-harness` |
| `sig-enforcement-convergence-and-fragmentation` | Everyone is building bespoke, unshareable enforcement (Anthropic, Meta, Checkout.com, indie devs — "what I enforce isn't what you'd enforce") while the industry converges publicly on the same idea: Anthropic's executor/advisor pattern (one agent codes, an advisor feeds back), OpenAI's harness engineering, Qodo-style comprehensive PR review (captions "Cudo"), WorkOS's "enforce, don't instruct", and a keynote's "slow the hell down" — verification is becoming the product surface | `FormsPattern → pat-verification-gap` | `OnElement → el-generator-validator-separation` **[registry]**; `OnElement → el-harness-engineering` **[registry]**; `RelevantCompany → co-anthropic`, `co-openai`, `co-meta` **[registry]** |

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-capability-is-not-reliability` | Capability and reliability are different axes: better specs, MCP servers, sub-agents, and context are instructions, and instructions are not verification — however good the input, you still verify the output; trust, not ability, is the bottleneck for delegation | `HighlightsPattern → pat-verification-gap` | — |
| `ins-verification-is-the-new-value` | The value shifted from the code you create to the verification you design — "not can you code, but can you verify"; TLDR: work on the harness, not the code | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-vector-harness` |
| `ins-enforcement-needs-a-contract` | Bespoke enforcement doesn't scale socially — it must become a language-agnostic, shareable contract ("given this task, fulfill this; the middle is developer-defined") that runs at every level: conversation end, pre-commit, multi-agent workflow steps, async agents, plus non-deterministic LLM-as-judge checks where needed | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-vector-harness` |

## KnowHow (1 new)

All `SourcedFromArtifact → ia-aie-sheikh-agent-rules`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-hook-based-deterministic-verification` | Wire deterministic enforcement into coding-agent workflows | Hook session end (Claude hooks) to trigger an external checker; define test cases in a config file — what "done the way I want it" means; on failure, auto-feed "this is failing, try again" until checks pass; layer checks at every level (conversation end, pre-commit, multi-agent steps, async agents, optional LLM-as-judge for the non-deterministic residue); then exploit the harness to downshift model cost — Haiku-class or open-source models under guardrails instead of frontier models everywhere | `ReferencesElement → el-vector-harness`, `ReferencesElement → el-agent-hooks` **[registry]** |

## Dropped

- "Play Cyberpunk on my Xbox while Claude works" — motivation color; prose only.
- WorkOS and Qodo ("Cudo") — one-line citations inside `sig-enforcement-convergence-and-fragmentation`; not coined (passing, and Qodo is a caption guess).
- The "top token spender at your company" Q&A joke — noise (though it corroborates that verification layers burn tokens).

## Review notes

1. Unresolved caption garble: "they released this project Claude Swing that shows Project Methuselah, which is supposed to be so good it will solve everything." Plausibly the seed elements `el-project-glasswing` and/or `el-claude-mythos-preview` — no edge added pending someone checking the video; if confirmed, add `OnElement` from `sig-lab-predicts-enforcement-obsolete`.
2. "Cudo" read as Qodo (AI code-review vendor) — best guess, flagged, not coined.
3. `sig-lab-predicts-enforcement-obsolete` could alternatively be modeled as `ContradictsPattern → pat-verification-gap` from the lab-claim side; I kept `FormsPattern` because the signal as delivered is the speaker's capability≠reliability rebuttal, with the lab claim as context. Reviewer's call.
4. Vector is described as the speaker's personal build ("my own product, Vector V1"; public as "Vector Harness" via LinkedIn DM — no URL given), so no `DevelopedByCompany → co-checkout-com` edge on `el-vector-harness`.
5. "Executed advisor pattern" (Anthropic) mapped to the existing `el-generator-validator-separation` rather than coining `el-executor-advisor` — same mechanism (generator + feedback-giving validator). Split it out if you want the Anthropic-branded pattern as its own node.
6. `el-harness-engineering` reuse: batch 2 defined it in the MSFT voice context; here it's explicitly attributed to OpenAI ("harness engineering — tools + context + verification"). Compatible; reused.
