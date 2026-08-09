# SPIKE extraction — "The Pipeline Is Dead" (Iris ten Teije, Sky Valley Ambient Computing) — FOR REVIEW

Source transcript: `transcripts/ten-teije-sky-valley-pipeline-is-dead.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/bRnoEpoK5m4 — AI Engineer World's Fair, published 2026-07-07.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-07-07 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-ten-teije-pipeline-dead` | The Pipeline Is Dead (Iris ten Teije, Sky Valley Ambient Computing — AI Engineer World's Fair) | youtube | https://youtu.be/bRnoEpoK5m4 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-iris-ten-teije`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-iris-ten-teije` | Iris ten Teije (co-founder, Sky Valley Ambient Computing — venture rendered "Differ" in captions; a decade in fintech, early at a scaled-and-exited digital bank) | `AffiliatedWithCompany → co-sky-valley` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-sky-valley` | Sky Valley Ambient Computing | developer | startup building adaptive software: one canonical stem deployed, every user runs a bounded per-user divergence adapted live by agents. Captions consistently render the venture/product name as "Differ" (⚠ see notes); co-founder Noam was JFrog's first engineer and helped build the CI/artifact pipeline the talk declares dying |

## Elements (2 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-agent-as-runtime` | Agent as the runtime | concept | infra | When the thing that runs software can also modify it, development and distribution stop being separate phases: correct changes are produced where the software runs (server, client, live user session) instead of frozen at build time — dissolving the build→freeze→ship pipeline and the one-version-for-everyone assumption it encoded |
| `el-stem-and-divergences` | Stem plus divergences | concept | infra | Architecture for per-user adaptive software: deploy one canonical stem; each user runs an isolated, bounded, immutable, individually reversible divergence. Blast radius is one user context; rollback is live with no deploy; "what is this user running and why" becomes a graph query, traceable signal → recommendation → adaptation; developers declare off-limits zones (auth, payments, never-drop fields) |

Element edges: both `IdentifiedInArtifact → ia-aie-ten-teije-pipeline-dead`; `el-agent-as-runtime` `EnablesElement → el-stem-and-divergences`; `el-stem-and-divergences` `EnablesPattern → pat-saaspocalypse` **[registry]**; both `DevelopedByCompany → co-sky-valley` (the architecture is their product bet; drop if you keep concept elements vendor-neutral).

## Signals (4 new)

All: domain `infra`, `SpottedInArtifact → ia-aie-ten-teije-pipeline-dead`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-frozen-artifact-was-economics` | Founder thesis (from the co-founder who built JFrog's pipeline): "one version for everyone, frozen" was never a fact about software — only about cost. Correct changes took skilled humans hours or days, so production was rare, central, verified, then frozen; every reliability guarantee (reproducibility, preview, rollback) flows from the artifact not changing. As AI collapses the cost of a correct, scoped change toward zero — and the change can happen where the software runs — the reason to separate development from distribution dissolves | `FormsPattern → pat-saaspocalypse` **[registry]** | `RelevantCompany → co-sky-valley` |
| `sig-demand-for-personal-software` | Demand-side evidence predates AI by decades: enterprise professional services / forward-deployed engineers as an entire industry line item, engineers hand-rebuilding dotfiles on every machine, Excel as millions of people's personal programs, algorithmic feeds beating one-size-fits-all content on every metric — plus feature flags, segmentation, and A/B testing as pre-agent attempts at divergence, forced into pre-declared buckets. Demand was never the constraint; production cost was | `FormsPattern → pat-saaspocalypse` | — |
| `sig-differ-per-user-divergence-bet` | Sky Valley/Differ's product bet: instead of one codebase gated by flags and shipped to everyone, one canonical stem with every user running her own live-adapted divergence — "from the least-worst version for everyone to the best version for anyone." Example: a CRM that observes an investor's usage (intro paths, skipped fields, deal-checking habits) and reshapes itself, or implements user-requested changes within developer-set boundaries without going back to the developer — letting horizontal SaaS address far more personas without increasing R&D spend | `FormsPattern → pat-saaspocalypse` | `RelevantCompany → co-sky-valley` |
| `sig-generation-easy-80-percent` | "Calling a model to write some code is something everyone can do — generation is the easy 80%." The business is the substrate: observability, validation (correctness across the stem and every divergence), desirability measurement (did a correct change actually improve retention / churn / support tickets?), coordination (propagating updates across a million versions), provenance | `FormsPattern → pat-model-not-bottleneck` **[registry]**; `FormsPattern → pat-verification-gap` **[registry]** | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-pipeline-death-is-cost-shift` | The entire CI/packaging/registry/app-store stack exists to move a frozen artifact from build machine to run machine safely, reproducibly, once. The pipeline isn't failing — the constraint it was built for (software expensive to produce, cheap to run) went away. The next 20 years are about shipping the right version to anyone, with isolation and provenance making that safe instead of terrifying | `HighlightsPattern → pat-saaspocalypse` **[registry]** | `ReliesOnElement → el-agent-as-runtime` |
| `ins-bounded-divergence-beats-brittleness` | The CTO objection ("I can barely reason about one AI-generated codebase and you want me to run millions — you're describing my worst problem multiplied") aims the right instinct at the wrong target: brittleness is unmanaged divergence inside one tangled artifact. Stem+divergences makes safety structural — isolation, immutability, per-divergence live rollback, one-context blast radius — rather than asking anyone to trust AI coordination; the honest answer is architecture, not "AI is good at coding" | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-stem-and-divergences` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-ten-teije-pipeline-dead`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-bound-adaptive-divergences` | Make adaptive software safe with structure, not trust | Deploy one canonical stem; keep every per-user divergence bounded, isolated, immutable, and individually reversible (blast radius = one user context; rollback live, no deploy); declare what can never be adapted (auth, payments, mandatory fields); trace every variant back through signal → recommendation → adaptation so bug reports on a program that exists for one user stay debuggable; test correctness across stem + divergences, and separately measure desirability against explicit product goals (retention, churn, support tickets) — a correct change is not necessarily a good one; coordinate updates by merging intent/outcome, not code: users need not run the same commit, they converge on the same goal via their own path; earn autonomy — start where recommendations would be conservative, but build toward a system legible and reliable enough that humans in the loop choose to step back | `ReferencesElement → el-stem-and-divergences` |

## Dropped

- Salesforce — illustration of the professional-services line item; no edge to `co-salesforce` **[registry]**.
- JFrog — biographical context for co-founder Noam; kept in company/expert prose, no node.
- Excel / Microsoft, dotfiles, social feeds — demand-side illustrations folded into `sig-demand-for-personal-software`.
- The no-branch digital bank analogy — rhetorical frame.

## Review notes

1. **Company-name garble, unresolved:** the official listing says "Sky Valley Ambient Computing"; captions consistently say "Differ" ("I'm one of the co-founders of Differ"; closing "I'm Iris, this is different [Differ?] and that's what we're building"). Coined `co-sky-valley` per official metadata with the "Differ" rendering noted in the brief — verify whether Differ is the product name, the actual company name, or a caption garble before seeding.
2. Co-founder "Noam" (first engineer at JFrog) has no surname in the transcript — not coined (batch-5 "Maria" precedent).
3. **Pattern candidate NOT coined (one-talk evidence):** "adaptive software / death of the frozen artifact / per-user divergence" — the talk's own thesis is seed-altitude (an industry-change claim about software distribution) but single-sourced. Parked on `pat-saaspocalypse` as its distribution-economics mechanism; if it recurs in later batches, proposed slug `pat-adaptive-software` (disruption), and the three saaspocalypse edges here would re-home.
4. `pat-saaspocalypse` edges assume the seed brief ≈ "AI-cheap custom/per-user software displaces one-size-fits-all SaaS"; re-home if the seed brief is narrower than that.
5. The CTO quote is the speaker paraphrasing a call ("what he said roughly was…") — a double paraphrase.
6. `sig-generation-easy-80-percent` carries two FormsPattern edges (model-not-bottleneck + verification-gap) — both readings are explicit in the text ("anyone can make a code change now; the hard part is knowing whether you actually found an improvement"); trim to one if single-edge discipline is preferred.
7. `el-forward-deployed-engineering` **[registry]** deliberately not edged: the FDE mention is historical demand evidence, not a claim about the practice itself; kept in signal prose.
