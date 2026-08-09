# SPIKE extraction — "Everything we knew about software has changed" (Theo Browne, @t3dotgg) — FOR REVIEW

Source transcript: `transcripts/browne-everything-changed.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/xUnRQ9vLXxo — AI Engineer World's Fair, published 2026-07-08.
`stagingTimestamp` for the artifact and all dated nodes (signals, knowhows): 2026-07-08 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-browne-everything-changed` | Everything we knew about software has changed (Theo Browne — AI Engineer World's Fair) | youtube | https://youtu.be/xUnRQ9vLXxo |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-theo-browne`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-theo-browne` | Theo Browne (@t3dotgg — dev YouTuber and founder; YC alum with Ping/"Zoom for streamers", 2021; currently building an unnamed "full-stack cloud" — Vercel-plus-databases-plus-auth) | — (no affiliation edge; his current company is unnamed in-talk — see review note 2) |

## Companies (0 new)

Reused for edges: `co-aws`, `co-salesforce`, `co-anthropic` **[registry]**. Vercel, Slack, Apple, Y Combinator mentioned in prose only.

## Elements (0 new)

Reused: `el-claude-mythos-preview` **[registry]** and `el-claude-fable` **[registry]** (the orchestration-era models his thesis rides on), `el-gbrain` **[registry]** (Tan's company-brain product — Browne names a whole product tier after it, see review note 3), `el-agent-loops` (defined in `embiricos-huet-steinberger-openai-golden-age.md`, this batch), `el-codex` (same file), `el-claude-code` **[registry]**.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-browne-everything-changed`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | domain | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-model-eras-to-orchestration` | Browne periodizes coding models into eras: Sonnet 3.5 = the tool-call era (first to call tools reliably enough for daily codebase work); Opus 4.5 (Nov–Dec 2025) = long-running tasks lasting hours without losing the thread ("when my AI psychosis started"); Mythos/Fable = the orchestration era — the first models that understand *themselves*, spawning and verifying sub-models on a bare prompt, no custom software factory needed; he publicly recants his earlier "we're hitting a wall" claim: "the models are getting better faster than we are" | harness | `FormsPattern → pat-accelerated-research` **[registry]**, `FormsPattern → pat-model-not-bottleneck` **[registry]** | `RelevantCompany → co-anthropic` **[registry]**, `OnElement → el-claude-mythos-preview` **[registry]**, `OnElement → el-claude-fable` **[registry]** |
| `sig-startup-tier-collapse` | The build-size tiers shifted down a full level in ~a year: his 2021 YC startup (Ping) would be a side project today; his 2021 side project (Reddit meme scraper, 2–3 days of work) drops below the line; startups exhibiting at this very conference have products he judges buildable as side projects — some "could just be a markdown file"; most Jira tickets from his previous job are trivial for Opus 4.5-class models | — | `FormsPattern → pat-saaspocalypse` **[registry]** | — |
| `sig-markdown-file-products` | Concrete replacement, dated and running: his PR-triage service is now literally a markdown file — "go to these four GitHub repos, look at open PRs, figure out status, prioritize, update the static HTML file, send to S3, give me the URL" — piped to Codex/Claude on a 9:00 a.m. cron; by ~9:15 his workday is generated; "executing markdown" is the new deployment target and he calls this whole product tier "the G brain tier" | harness | `FormsPattern → pat-saaspocalypse` **[registry]** | `OnElement → el-agent-loops` (this batch), `OnElement → el-gbrain` **[registry]** |
| `sig-breadth-viable-for-small-teams` | Breadth-vs-depth economics inverted: pre-AI, startups had to out-depth incumbents in a narrow vertical (Vercel vs AWS — "even the agents prefer Vercel"); now a tiny team can cover AWS-scale *range* ("build a database platform into your product in a day or two of prompting"), ship shallow-everywhere, and let users vibe-build missing vertical features themselves if the architecture allows it — Slack accidentally proved the shape: a mediocre product that became "the platform people run their agents in half the time" because its bot API lets users build what's missing; his call: it's time to directly challenge Slack, AWS, Salesforce | — | `FormsPattern → pat-saaspocalypse` **[registry]** | `RelevantCompany → co-aws` **[registry]**, `RelevantCompany → co-salesforce` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-skeuomorphic-dev-phase` | Software developers are in their skeuomorphic phase: like iOS ≤6 compasses that had to look like compasses, we bolt natural language onto terminals, keep git conventions ("why can't we commit env files?"), qualify ourselves by languages, and guilt-merge PRs because someone spent two weeks — attachments that existed to convince/comfort, not to be useful. The iOS 7 moment is due: stop imitating the old tools, embrace what the new medium is actually good at; sunk-cost feelings about code evaporate when the code is disposable and an agent wrote it | `HighlightsPattern → pat-value-of-judgement` **[registry]** | — |
| `ins-stupid-sized-ideas` | The "too big" ceiling has gone indeterminate — Browne can no longer say what's beyond a one-team build (train a model? an OS? compete with npm?), so ambition must be recalibrated by feel: "if your idea doesn't feel stupid, it's not big enough"; think *wider* (spectrum coverage), not just bigger, and find the new limits by overshooting them | `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-claude-mythos-preview` **[registry]** |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-browne-everything-changed`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-markdown-cron-services` | Replace glue services with markdown-on-cron | Write the service as a plain-English markdown task (sources to check, decision to make, artifact to produce); pipe it to a coding agent (Codex / Claude) on a cron; have the run end by publishing its own artifact (e.g., regenerate static HTML, push to S3, return the URL); audit how many of your internal tools reduce to this before building or buying software | `ReferencesElement → el-agent-loops` (this batch), `ReferencesElement → el-codex` (this batch), `ReferencesElement → el-claude-code` **[registry]** |
| `how-architect-for-user-extension` | Build breadth, let users build the depth | Cover the widest usable spectrum shallowly instead of out-depthing incumbents in one vertical; architect deliberate extension points (APIs/bots/plugins — Slack's accidental lesson) so users and their agents can add the vertical features you don't ship; treat a missing feature as "not your problem" only if your architecture genuinely lets the user build it; when users can vibe-code the gaps, incumbent feature-count moats stop binding | — |

## Dropped

- iOS 6→7 compass/skeuomorphism walkthrough — retained only inside `ins-skeuomorphic-dev-phase`.
- Vim/tmux/GNU-screen identity riff, "who's coded 10+ years" audience polls — color supporting the insight.
- His unnamed full-stack cloud pitch ("don't compete with me on this one") — self-promotion, no extractable claim beyond the tier chart.

## Review notes

1. This is an argument talk, not a data talk — the four signals are the concrete, falsifiable observations (model eras with dates, the tier chart applied to his own three real projects, the running cron service, the Slack observation); everything else is exhortation and lives in the insights.
2. No company coined for Browne: the talk self-describes him as "a YouTuber"; Ping is defunct/pivoted and the full-stack cloud is unnamed. If the reconciler wants an affiliation, coin his company when it launches publicly.
3. **`el-gbrain` cross-reference:** Browne's "G brain tier — it's a markdown file" reads as a live riff on Garry Tan's G Brain (batch 3, `el-gbrain`, org-as-markdown thesis) — a second independent occurrence of the term at this conference. Seconds the registry's ⚠ spelling-unverified flag; the OnElement edge is intentional but low-confidence — drop it if the reconciler reads "G brain tier" as a coincidental coinage.
4. `el-claude-mythos-preview` **[seed]** vs `el-claude-fable` **[batch5]** merge flag already exists in the registry; this file edges both (the talk names both). Rehome if merged.
5. Pattern check: nothing new coined. The tier-collapse/breadth thesis is `pat-saaspocalypse` evidence throughout; the orchestration-era claim adds a soft data point to the batch-3 "AI-native organization" candidate (products = markdown + harness) — noted, no edge.
6. Anthropic model names (Sonnet 3.5, Opus 4.5, Mythos, Fable) are clean in captions; no unresolved garbles worth flagging in this transcript.
