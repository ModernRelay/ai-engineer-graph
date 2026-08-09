# SPIKE extraction — "Software engineering is not about writing code" (Benoit Schillings, Google DeepMind) — FOR REVIEW

Source transcript: `transcripts/schillings-deepmind-not-about-writing-code.txt` (auto-captions — quotes are paraphrases, not verbatim; "Benois Shellings" → Benoit Schillings).
Video: https://youtu.be/1P1hJ36rxM0 — AI Engineer World's Fair, published 2026-07-17.
`stagingTimestamp` for the artifact and all signals: 2026-07-17 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node. `el-model-first-languages` is defined in `horthy-et-al-great-loops-debate.md` (this batch) and referenced here by slug.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-schillings-beyond-code` | Software engineering is not about writing code (Benoit Schillings, VP of Research, Google DeepMind — AI Engineer World's Fair) | youtube | https://youtu.be/1P1hJ36rxM0 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-benoit-schillings`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-benoit-schillings` | Benoit Schillings (VP of Research, Google DeepMind; ex-Google X; team charter: whatever Gemini needs 1 month to 1 year out; started the Pitchfork ML-for-code project at X in 2018; 45 years writing code) | `AffiliatedWithCompany → co-google-deepmind` **[registry]** |

## Companies (0 new)

Reused: `co-google-deepmind` **[registry]** (per registry note, used instead of the batch-2 `co-google` node).

## Elements (1 new, 2 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-code-selfplay` | Coding self-play | concept | training | AlphaZero-style self-play applied to code: with human training data mined out, frontier code models create their own challenges, judge answer validity, and to some extent judge architecture — hundreds of millions of hours of verifiable self-play as the route to superhuman coding; works because code is uniquely verifiable (compile, run, test) |

Element edges: `el-code-selfplay` `IdentifiedInArtifact → ia-aie-schillings-beyond-code`; `el-code-selfplay` `EnablesPattern → pat-accelerated-research` **[registry]**; `el-code-selfplay` `DevelopedByCompany → co-google-deepmind` **[registry]** (as articulated practice, not a product).

Reused: `el-model-first-languages` (this batch, defined in the loops-debate file — Schillings gives the fuller version: design new strongly-typed, Lean-inspired, not-necessarily-human-readable languages that put the burden of correctness on the model now that writing code costs nothing); `el-claude-mythos-preview` **[registry]** (the "mythos... unreasonable number of vulnerabilities" news he cites).

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-schillings-beyond-code`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-google-deepmind` **[registry]** (speaker-institution testimony).

| slug | name / brief | domain | FormsPattern |
|---|---|---|---|
| `sig-github-80pct-machine-generated` | Schillings' estimate: ~80% of new code added to GitHub today is machine-generated — the era of mining human code for training data is ending, which is what forces the pivot to self-play; code's unique advantages (massive data, cheap verification) got models here, and those same properties make self-play viable | training | `FormsPattern → pat-verification-gap` **[registry]** (generation industrialized while human oversight of the corpus ends) |
| `sig-code-review-will-vanish` | Prediction from a DeepMind research VP: within a year, model-generated code will ship with nobody reading it — the compiler-assembly analogy (nobody checks compiler output anymore); replacement process is "active guardrails," and vulnerability discovery becomes a never-ending deepening cycle: models find a layer of bugs, get smarter, find subtler ones | security | `FormsPattern → pat-verification-gap`, `FormsPattern → pat-new-cyber-threats` **[registry]** |
| `sig-deepmind-correct-by-construction` | Schillings' team is actively working on the "grail": instead of detect-then-patch, teach models to write correct/secure code from the start (very hard, deeply context-dependent) — plus teaching models correct planning/problem decomposition ("inductive architecture") for 35-million-line-codebase-scale engineering, where the frontier still moves | security | `FormsPattern → pat-verification-gap` |
| `sig-code-economics-inverted` | The entire software culture, infrastructure, and company landscape was built on the assumption that writing code is the expensive part; writing code is now ~free, so produced code volume will explode and the discipline reorganizes around design adequacy, verification, and architecture — "superhuman syntax generation" is settled ("when Gemini writes a function, I can't do better — it's over") | harness | `FormsPattern → pat-saaspocalypse` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-human-memory-shaped-software` | Each software era was shaped by its binding constraint: machine power (assembly era), then the human brain — modular design, libraries, and abstraction exist because humans hold ~7–9 tokens of working memory; with model context effectively infinite, that constraint dissolves, and with it much of why software engineering is organized the way it is. Humans keep the roles the model lacks: specifying what is actually wanted, and inductive/cross-domain pattern transfer | `HighlightsPattern → pat-verification-gap` **[registry]** | — |
| `ins-evals-must-be-open-ended` | SWE-bench-style evals ("does the code run and produce the right output") measure a small slice of engineering; benchmarks need open-ended, never-saturating problems with scalar loss functions — e.g. lossless text compression scored as compressed size + source size — that force genuinely novel algorithms; relatedly, chain-of-code reasoning should extend to spatial/dynamic (multimodal) thinking, since code-writing is a visual activity for humans | `HighlightsPattern → pat-verification-gap` | `ReliesOnElement → el-code-selfplay` |

## KnowHow (1 new)

`SourcedFromArtifact → ia-aie-schillings-beyond-code`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-open-ended-eval-design` | Design open-ended evals with a loss function, not a pass/fail | Pick problems with no ceiling and machine-checkable scoring (compression ratio, proof size, runtime under correctness constraints); score = task metric + solution complexity so the model can't win by memorizing; use them to elicit novel algorithms rather than benchmark saturation | `ReferencesElement → el-code-selfplay` |

## Dropped

- Origin-story material (Pitchfork 2018, "English is not a programming language" mea culpa, assembly→C++→Python arc) — folded into the expert brief.
- Chemistry/biology/"gold we cannot see" closing — genuine `pat-accelerated-research` adjacency ("experiments become free" at the code×science intersection) but too sketchy for a signal; flagged here instead.
- Jeff Dean architecture aside, Waymo/Glass X credentials — color only.

## Review notes

1. This is a keynote of theses, not dated facts; the two hardest "signals" (`sig-github-80pct-machine-generated`, `sig-code-review-will-vanish`) are an estimate and a prediction respectively — but from the VP of Research at DeepMind on the record, which is exactly the attributable-observation-of-change the signal bar wants. If the reviewer wants only one, keep the 80% stat.
2. "mythos looking at a piece of code and detecting an unreasonable number of vulnerabilities" — mapped to `el-claude-mythos-preview` **[registry]**, consistent with the Yan and Han talks in this batch; cross-lab confirmation of the same event is itself notable.
3. `sig-code-economics-inverted` → `pat-saaspocalypse`: the signal is about the economics of code production rather than SaaS business collapse specifically; it's the closest existing seed pattern. Alternative filing: `pat-model-not-bottleneck`. No new pattern coined.
4. Cross-talk resonances worth a reconciliation pass: the 7±2 working-memory framing also anchors Garry Tan's talk (`ins-org-as-markdown` in `tan-yc-new-physics-of-business.md`), and `el-model-first-languages` is shared with the loops debate. Three of five frontier-set talks independently argue "generation is solved, verification/specification is the frontier."
