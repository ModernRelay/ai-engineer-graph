# SPIKE extraction — "How to Kill the Code Review" (Ankit Jain, Aviator) — FOR REVIEW

Source transcript: `transcripts/jain-aviator-kill-code-review.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/YgEv7IQzGdM — AI Engineer World's Fair, published 2026-08-17.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-17 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the founder of an AI code-verification company argues line-by-line review is already dead (30%+ of changes merge unreviewed) and that the mistake is doing AI review in a UI where "AI reviews and nobody reads." The real function of review is **alignment** (knowledge sharing, architecture, mentorship), which must survive even as semantic-accuracy checking gets automated. His model: capture the **intent from the agent session** (not the code) as acceptance criteria, pair it with an **AI slop registry** of recurring review comments, compile a **test plan**, and verify against a live preview — so **the review surface becomes the intent and evidence, not the diff.** Caption garbles: "spectrum development" → **spec-driven development** (systematic), "AI slot register/registry" → **AI slop registry**, "Dex" → **Dex (Horthy)**, "sand flying" → likely **sanity/smoke testing**, "Verify" kept (product name).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-jain-kill-code-review` | How to Kill the Code Review (Ankit Jain, Aviator — AI Engineer World's Fair) | youtube | https://youtu.be/YgEv7IQzGdM |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-ankit-jain`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-ankit-jain` | Ankit Jain (co-founder, Aviator; wrote a LinkedIn post proposing a five-layer trust model for merging without line-by-line review) | `AffiliatedWithCompany → co-aviator` |

Referenced without coining: Dex Horthy ("Dex was talking about yesterday" — the point that an agent building the code should not also build the test plan that catches its issues).

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-aviator` | Aviator | developer | Building an **AI code-verification platform**; piloting a product called **Verify** that combines alignment capture with semantic-accuracy detection via an AI slop registry. Origin: the founder's five-layer trust model for review-free merging |

Reused **[registry]**, edge-only: `co-google` **[b2]** (Mondrian, 2006, "made formal code review a thing"), `co-microsoft` **[b2]** (early Windows built without reviews). Referenced for behaviour: Claude Code, Codex, Cursor.

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-review-is-alignment` | Code review is alignment, not just correctness | concept | harness | The reframe the talk turns on: review catches bugs and conventions, but its load-bearing function is **alignment** — knowledge sharing, mentorship, architectural feedback, onboarding, collaboration — the piece missing from the speaker's earlier five-layer model. "For semantic accuracy we can build better tooling, but alignment must survive." The dysfunction to avoid: "when AI reviews and nobody reads, we've configured the wrong thing" — a UI where two or three AI agents review and the human just skims and merges |
| `el-review-crisis-metrics` | The review bottleneck | concept | harness | The problem stated in numbers: line-by-line review "has already stopped" (30%+ of changes merge with no review at all); code churn and incident-to-PR ratio rising; median review time up ~4x — "coding is solved, now reviewing is the bottleneck where everything gets stuck." ⚠ figures caption-sourced ("861% code churn"), see review note 3 |
| `el-intent-from-session` | Intent captured from the session | concept | harness | The core mechanism, and the fix for spec-driven development's waterfall flaw (spec written before everything is known, no feedback loop, "LLMs aren't deterministic — they make decisions themselves"). Intent doesn't only live in the spec — it lives in the Jira ticket, the PRD, and **most of all in the prompts**, "where the real decisions are being made" in the back-and-forth with the agent. The mistake today: "we create a PR and then throw away the prompts." Capture the user responses from the session as **acceptance criteria** — and crucially build the test plan from the *session*, not the code, because "if the code is built by the same agent building the test plan, it won't catch issues" (crediting Dex Horthy) |
| `el-ai-slop-registry` | The AI slop registry | technology | harness | The semantic-accuracy half: humans re-identify the same review issues over and over, so **codify recurring review comments into a registry** that then auto-flags them — "every recurring comment is now a guardrail you don't have to review again." Framed as learning on top of the base LLM from the review experience humans provide; compounds with every merged PR. Homework offered: "mine your last 1,000 review comments and build a registry for the repeatable ones." Follows a J-curve (upfront pain before payoff) |
| `el-intent-review-surface` | The intent-and-evidence review surface | concept | harness | The synthesis: session→acceptance-criteria + AI-slop-registry → a **test plan**, verified by spinning up a **live preview** and running it end-to-end ("even if the code looks right, does it actually work?"). That verification output *becomes the review surface* — reviewers look at intent, whether the capability was implemented, and whether behaviour met the criteria, plus screenshots and DB snapshots as evidence, rather than reading the diff. "Deterministic where it can be, LLM where you must." Closer to behaviour-driven than test-driven development; the test plan is English, so PMs and designers can participate. Tests are created in real time, so you don't maintain a test suite |

Element edges: all five `IdentifiedInArtifact → ia-aie-jain-kill-code-review`.
`el-intent-review-surface` `UsesElement → el-intent-from-session`, `el-ai-slop-registry`;
`el-review-is-alignment` `EnablesElement → el-intent-review-surface`;
`el-review-crisis-metrics` `EnablesElement → el-review-is-alignment`;
`el-intent-review-surface` `ExemplifiesPattern → pat-verification-gap` **[registry]**;
`el-intent-from-session` `UsesElement → el-spec-driven-development` **[registry]**.

Reused elements (no new nodes): `el-spec-driven-development` **[b9]** (critiqued as waterfall-with-no-feedback-loop — a genuinely new critical reading of that node), `el-reviewdebt` **[b5]** (the review-bottleneck thread; edge left to review), `el-claude-code`/`el-codex`/`el-cursor-composer` **[registry]** (the coding sessions where intent is made).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-jain-kill-code-review`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-aviator`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-line-review-already-dead` | harness | A verification vendor's blunt diagnosis: line-by-line review "has already stopped" — 30%+ of changes merge unreviewed, code churn and incident-to-PR ratios rising, median review time up ~4x — so "coding is solved, reviewing is the bottleneck." And doing AI review in a GitHub UI produces the anti-pattern "AI reviews and nobody reads." The generation-outpaces-verification thesis, quantified from the review side | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-review-crisis-metrics`, `el-review-is-alignment` |
| `sig-review-is-really-alignment` | harness | The reframe: review's durable value is **alignment** — knowledge sharing, mentorship, architecture, onboarding — not line-reading, and that is what must survive automation. "This is not a talk for solo/vibe-coding; if you're in teams you need knowledge sharing." Semantic accuracy can be tooled; alignment is the human-in-the-loop part. Relocates the human role in review from correctness-checking to alignment-owning, a claim about how engineering collaboration re-bundles | `FormsPattern → pat-ai-native-org` **[registry]** | `OnElement → el-review-is-alignment` |
| `sig-capture-intent-not-code` | harness | The mechanism claim: intent lives in Jira, PRDs, and **most of all in the prompts** where decisions are actually made — and "today we create a PR and throw away the prompts." Capture the session's user responses as acceptance criteria, and build the test plan from the **session, not the code**, because an agent that wrote the code will not write a test plan that catches its own issues (credited to Dex Horthy). Session provenance, not diff provenance, as the basis for verification | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-intent-from-session` |
| `sig-slop-registry-compounds` | harness | The learning-loop claim: recurring review comments are codified into an **AI slop registry** that auto-flags them, "a guardrail you don't have to review again," compounding with every merged PR — the review experience humans provide becomes training the system learns from. A team-specific, accumulating verification asset built from human review history; follows a J-curve. Bears on the accumulation-loop thesis from the review-quality side | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-ai-slop-registry` |
| `sig-review-surface-becomes-intent` | harness | The synthesis: session→criteria + slop-registry → test plan → live-preview verification, and **that verification output becomes the review surface** — reviewers check intent and evidence (screenshots, DB snapshots, did-it-actually-work), not the diff. "Deterministic where it can be, LLM where you must," test plan in English so PMs and designers participate, tests created in real time. Verification re-architected as evidence-against-intent rather than reading generated code | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-intent-review-surface`, `el-spec-driven-development` **[registry]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-review-value-migrates-to-alignment` | The talk's sharpest point is that automating review's correctness function does not eliminate review — it strips it down to its actual purpose, alignment, which is a human coordination problem no verifier replaces. Teams that read "AI reviews everything" as "no one reviews" have thrown away the alignment that made review valuable; teams that relocate the human to owning architecture and intent keep it. That reframes the whole kill-the-review debate as a question of *which half you automate*, and it is the same execution-industrializes-judgment-survives shape as `pat-value-of-judgement`, here specific to collaboration | `HighlightsPattern → pat-ai-native-org` **[registry]** | `ReliesOnElement → el-review-is-alignment`, `el-intent-review-surface` |
| `ins-verify-against-intent-not-artifact` | Building the verification target from the session rather than the code closes the loophole that makes agent-written tests worthless: the artifact cannot be its own oracle. Capturing intent from prompts, PRDs and tickets gives an independent specification to check behaviour against, and turning that into a live-preview test plan makes the check about *did it do what was wanted* rather than *does the code look right*. It is the corpus's verification-gap thesis with a concrete provenance rule — the oracle must come from a different source than the artifact | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-intent-from-session`, `el-ai-slop-registry` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-jain-kill-code-review`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-replace-code-review-with-intent-verification` | Replace line-by-line review with intent-and-evidence verification | Accept that line-by-line review is already gone (a large share of changes merge unreviewed) and that reviewing has become the bottleneck — but do not conclude "no review," because review's real function is **alignment** (knowledge sharing, architecture, mentorship) and that must survive; separate the two halves — automate **semantic accuracy**, keep humans on **alignment**; capture **intent from the agent session**, not the code, since the real decisions are made in the prompts and get thrown away at PR time, and since an agent that wrote the code cannot be trusted to write the test plan that catches its own issues; turn captured session responses into **acceptance criteria**, and build an **AI slop registry** by mining your recurring review comments so each becomes an automatic guardrail that compounds with every merge (expect a J-curve before payoff); compile criteria plus registry into a **test plan** and verify it against a **live preview** end-to-end, collecting evidence (screenshots, DB snapshots) — because working matters more than looking right; make **that verification output the review surface**, so reviewers examine intent and evidence rather than the diff and can discuss architecture one level up; keep it **deterministic where possible and LLM where necessary**, and write the test plan in English so PMs and designers can participate | `ReferencesElement → el-review-is-alignment`, `el-intent-from-session`, `el-ai-slop-registry`, `el-intent-review-surface` |

## Dropped

- **The five-layer trust model / LinkedIn post origin** — framing; the "what I got wrong (alignment was missing)" correction is in `el-review-is-alignment`.
- **The Mondrian/Google-2006 and early-Windows history** — kept as one clause each; no nodes (companies reused).
- **The payment-form verification example** (agent browses the app, fills a form, captures screenshots + DB snapshot as evidence) — illustration folded into `el-intent-review-surface`.
- **The Verify product pitch / early-design-partner ask** — logistics; the product is carried by `co-aviator`.

## Review notes

1. **Lands on two coined patterns, both freshly relevant.** `pat-verification-gap` (the dominant thesis) takes the core — verify against intent-and-evidence, not the diff — and `pat-ai-native-org` (coined 2026-08-16) takes the alignment/collaboration reframe (review's value migrates to a human coordination role). Good early post-coinage evidence for `pat-ai-native-org` from the engineering-practice side, complementing its dysfunction-side data (Dailey b17, Khandelwal b19).
2. **A genuinely new critical reading of `el-spec-driven-development` [b9].** Prior corpus treatment was largely favourable (Hanchett b9); Jain critiques it as waterfall-with-no-feedback-loop that assumes determinism LLMs don't have. Worth noting on that element's brief at seeding — the corpus now holds both the pro and con.
3. **⚠ Verify before seeding:** "861% code churn," "4x median review time," "30%+ merge without review" are all caption-sourced single mentions with no citation. The Dex Horthy attribution ("yesterday") and the product name "Verify" should be confirmed.
4. **Proposed cross-file edges, left to review:** `el-intent-review-surface` / `el-doc-as-shared-state` (b17 Dailey — decisions-as-durable-state); `el-ai-slop-registry` / `el-reviewdebt` (b5) and `el-slop-as-unread-code` (b15 Gupta/Boundary). Not emitted; thematic.
