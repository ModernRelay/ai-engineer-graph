# SPIKE extraction — "Scaling Compute on Context" (Jack Morris, Engram) — FOR REVIEW

Source transcript: `transcripts/morris-engram-scaling-compute-on-context.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/WiqDvX6isc4 — AI Engineer World's Fair, **Continual Learning track**, published 2026-08-12.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-12 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: a researcher frames one problem — *given a fixed private corpus D and a pre-trained model θ, produce θ\* that knows D* — then walks the solution space (naive next-token training, KV compaction, on-policy distillation, synthetic continued pre-training, unsupervised RL environments), finds every approach saturates, and argues the missing ingredient is **self-improvement that makes its own training harder**. Caption garbles: "N gram"/"Ngram" → **Engram** (company; `ngr.am.com` per the closing slide), "meter" → **METR**, "GBT" → GPT, "Terrence Tao" → **Terence Tao**, "theta the star" → θ\*.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-morris-scaling-compute-on-context` | Scaling Compute on Context (Jack Morris, Engram — AI Engineer World's Fair) | youtube | https://youtu.be/WiqDvX6isc4 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-jack-morris`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-jack-morris` | Jack Morris (researcher, Engram — company launched the week before the talk) | `AffiliatedWithCompany → co-engram` |

Reused **[registry]**, edge-only: `exp-terence-tao` **[seed]** — used as the talk's opening exhibit for breadth-versus-depth: a heavy AI user and advocate in mathematics who observes that models know every public mathematical topic and can bridge literature gaps no human could, while lacking the depth of a graduate student who spent five years in one area. No `ContributedByExpert` edge; the reference is second-hand characterization. Also referenced without coining: Andrej Karpathy (a slide skipped live).

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-engram` | Engram | developer | Continual-learning startup, launched the week before the talk; building methods to train private corpora into models. ⚠ captioned "N gram"/"Ngram" throughout — normalized from the closing URL `ngr.am` |

Reused **[registry]**, edge-only: `co-scale-ai`, `co-surge-ai` **[b15]** and `co-mercor` **[b15]** — named together as the post-training data-acquisition layer, with the argument that even their expert-generated data "is still by definition publicly available data, because it's something the model could tell to a user." `co-anthropic` **[seed]** and `co-openai` **[b2]** referenced for model behaviour only.

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-scaling-compute-on-context` | Scaling compute on context | concept | training | The talk's name for the problem and its proposed fourth scaling axis. The three classical axes — more data, more compute, bigger models — have driven the entire deep-learning revolution but operate **only on public data**. For a private corpus the data axis is unavailable (you cannot create more of it) and training from scratch is off the table (you want the world knowledge), which leaves compute as the only axis: *how do you spend arbitrarily more compute on a fixed D and keep getting a better model?* Explicitly catalogued as one concept under many names — sleep-time compute, continual learning, neural memory, write-time compute, note taking, dreaming, studying, machine studying, and classically **amortized inference** — with the naming chaos read as evidence the paradigm is pre-paradigmatic |
| `el-breadth-vs-depth` | Breadth versus depth | concept | training | The framing of what current models lack. Models have superhuman breadth across public knowledge but not the "almost subconscious intuition" that comes from prolonged practice in one area. Three concrete failure classes: no knowledge of anything after the training cutoff; poor long-tail skill acquisition where public examples are thin (**AMD kernels** given as the example — "there are not that many good kernels written on AMD GPUs that are public"); and no knowledge of *you* — your emails, your writing style, your company's partnerships — "unless you happen to be famous enough to appear in the pre-training data" |
| `el-private-corpus-training` | The θ→θ\* problem | concept | training | The problem stated formally enough to compare methods: given a pre-trained θ and an unstructured private corpus D (every email you have written, every meeting transcript your company has ever had), produce θ\* that *knows* D — where "know" is explicitly flagged as the load-bearing, under-defined term that gives the field its leeway. Requirements are behavioural, not loss-based: answer questions about D, generate new artifacts like those in D, generalize beyond exact matches |
| `el-synthetic-data-wall` | The synthetic data wall | concept | training | Why every surveyed method saturates. Whatever you do — KV compaction, on-policy distillation, self-study QA pairs from the cartridges line of work, synthetic continued pre-training, unsupervised RL environments — you must first *define a dataset*, and "unless your model is under-parameterized, eventually it will learn all the data." That yields a bounded curve rather than pre-training's beautiful scaling: you fit the synthetic data, you know some of D but not all of it, and adding compute stops helping. The naive baseline is worse still — next-token training directly on D reaches a loss of ~0.0001 and then **collapses on generation**, memorizing without acquiring any generalization |
| `el-recursive-self-improvement-loop` | Training that makes itself harder | concept | training | The proposed missing ingredient, drawn by analogy to **AlphaGo**: the reason RL self-play scales is that "AlphaGo makes its own training questions harder by getting better through training." Applied to private corpora, the goal is a technique where the model generates data, improves, and then generates *better* data recursively — converting the flat post-saturation curve into one where compute continues to buy depth. Presented as the company's active research direction and as an honest open problem: their early curves plateaued exactly like everyone else's before "more sophisticated things that make the training gradually harder" |

Element edges: all five `IdentifiedInArtifact → ia-aie-morris-scaling-compute-on-context`.
`el-breadth-vs-depth` `EnablesElement → el-private-corpus-training`;
`el-private-corpus-training` `UsesElement → el-scaling-compute-on-context`;
`el-synthetic-data-wall` `EnablesElement → el-recursive-self-improvement-loop`;
`el-recursive-self-improvement-loop` `UsesElement → el-scaling-compute-on-context`;
`el-scaling-compute-on-context` `DevelopedByCompany`-adjacent → *not emitted* (a concept, not a product); `co-engram` linkage carried by signals.

Reused elements (no new nodes): `el-on-policy-distillation` **[b5, Brown/Prime Intellect]** — surveyed here as one candidate method and explicitly cross-referenced to Ronak Malde's talk earlier in the same track ("I think Ronak was talking about on-policy distillation"), which is a rare in-corpus, in-track citation between two extractions. `el-context-compaction` **[b6]** — invoked as the KV-compaction analogue ("similar to the way Claude Code or Codex does compaction"). `el-continual-learning` **[b8]**.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-morris-scaling-compute-on-context`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-engram`.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-scaling-only-ever-touched-public-data` | training | The structural observation the talk is built on: all three scaling axes have only ever been applied to public data — Wikipedia, Reddit, arXiv, GitHub — and even the post-training layer bought from Scale, Surge and Mercor "is still by definition creating publicly available data, because it's something the model could tell to a user." So models keep getting better at public coding and public maths and get no better at your life or your company. Framed not as an academic gap but as "the core problem with the current paradigm in AI." **HELD PATTERN-LESS** — the supply-side leg of the `pat-continual-learning-turn` candidate | — (held pattern-less) | `OnElement → el-breadth-vs-depth`, `el-scaling-compute-on-context` |
| `sig-private-corpus-methods-all-saturate` | training | An unusually candid competitive survey from someone selling the solution: naive next-token training on D collapses at generation; KV compaction only covers what fits in context and forgoes the benefit of gradients; on-policy distillation works but leaves open what data to distil; synthetic continued pre-training overwrites pre-training and is hard to scale, and presumes a base model most teams no longer have. All of them share one defect — you must define a dataset, and once fitted, additional compute buys nothing. A vendor publicly naming the ceiling its own category has not yet cleared | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-synthetic-data-wall`, `el-private-corpus-training`, `el-on-policy-distillation` **[registry, b5]** |
| `sig-fourth-scaling-axis-proposed` | training | The positive claim: with data fixed and model size fixed, **compute becomes the only remaining axis**, and the open research problem is how to spend it without saturating. Named "scaling compute on context" and explicitly identified as one idea wearing eight names across the industry — sleep-time compute, neural memory, write-time compute, note taking, dreaming, studying, machine studying, amortized inference — with the naming disorder itself offered as evidence that the paradigm "hasn't solidified the way pre-training or post-training have." **HELD PATTERN-LESS** — with Su's escape-intelligence claim, the second anchor of `pat-continual-learning-turn` | — (held pattern-less) | `OnElement → el-scaling-compute-on-context` |
| `sig-self-improvement-is-the-missing-ingredient` | training | The proposed way past the wall, argued from AlphaGo: scaling worked there because the system's own improvement made its training questions harder, so the curve never flattened. The equivalent for private corpora is a loop where the model generates training data, improves, and generates harder data — "everyone is looking for a technique that can make models better, which makes them train themselves better." Reported honestly as partially solved: the company's initial curves plateaued like everyone else's until they found methods that gradually raise difficulty | `FormsPattern → pat-accelerated-research` **[registry]** | `OnElement → el-recursive-self-improvement-loop`, `el-synthetic-data-wall` |
| `sig-depth-is-the-unclaimed-capability` | training | The market read behind the research: models have breadth no human can match and none of the depth a specialist accumulates, and the three visible symptoms are the training cutoff, thin long-tail skills like AMD kernel authoring, and the total absence of personal or company knowledge. The Terence Tao exhibit sharpens it — the world's most famous mathematician values AI for cross-literature connections while noting it lacks a graduate student's five-year intuition. Depth, not breadth, is framed as the unclaimed axis | `FormsPattern → pat-model-not-bottleneck` **[registry]** | `OnElement → el-breadth-vs-depth`; `RelevantCompany` also → `co-scale-ai`, `co-surge-ai` **[registry, b15]** |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-public-data-ceiling-is-structural` | The reason scaling has never touched private data is not neglect but definition: a data vendor can only sell what a model is allowed to say back to a user, so the entire commercial data-acquisition layer reproduces the public/private boundary rather than crossing it. That makes the private-corpus problem structurally immune to the industry's current fix for data scarcity — you cannot buy your way past it, because the buying mechanism is what enforces the limit. Any method that works has to spend compute rather than acquire data | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-scaling-compute-on-context`, `el-breadth-vs-depth` |
| `ins-saturation-is-the-real-benchmark` | Every method in this space can be made to look good on a single pass and they differ only in where they stop, so the honest evaluation is not "does it learn D" but "does adding compute keep helping." Under that test the field's current toolkit is uniformly bounded, and the one existence proof of an unbounded curve — self-play — worked because improvement fed back into problem difficulty. The practical filter for anyone assessing continual-learning vendors is therefore to ask what happens on the second and third pass, not the first | `HighlightsPattern → pat-accelerated-research` **[registry]** | `ReliesOnElement → el-synthetic-data-wall`, `el-recursive-self-improvement-loop` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-morris-scaling-compute-on-context`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-evaluate-private-corpus-training` | Judge private-corpus training by whether compute keeps paying | State the problem precisely before choosing a method — a fixed pre-trained model, a fixed unstructured corpus, and a behavioural definition of "knows" that covers answering, generating and generalizing, since that word is where most vendor claims hide; do not train next-token directly on your corpus expecting knowledge, because loss will go to ~0.0001 while generation collapses and nothing generalizes beyond exact matches; treat KV compaction as limited to what fits in context and as forgoing what gradients give you; when using on-policy distillation, recognize that the hard question is *what data* you distil, since raw documents do not work and QA-pair generation changes the objective; expect synthetic continued pre-training to overwrite some pre-training and to assume a base model you may not have; and above all **test the second pass** — every dataset-defining method saturates once fitted, so the question that separates approaches is whether additional compute still buys depth, which today requires a loop that makes its own training progressively harder; finally, remember the data budget is softer than the idealized problem implies, since a real learner also seeks out adjacent textbooks, searches the internet, and asks practitioners | `ReferencesElement → el-private-corpus-training`, `el-synthetic-data-wall`, `el-recursive-self-improvement-loop`, `el-scaling-compute-on-context` |

## Dropped

- **The launch-photo slide and the closing hiring pitch** (`ngr.am`, engineering and research roles) — logistics, though the URL is what resolves the company-name garble.
- **The METR task-length curve** — cited in passing as pure evidence of scaling working; already represented in the corpus from earlier batches, no new node.
- **The skipped Karpathy slide** — the speaker says "let's skip Andre" while running short; no content to extract.
- **The Mexico football-match aside** — the illustration of post-cutoff ignorance; folded into `el-breadth-vs-depth`.

## Review notes

1. **Second anchor for `pat-continual-learning-turn` (proposed, NOT coined).** Where Su argues the *why* (expertise is the scarce axis), this file argues the *what* — a named fourth scaling axis with a formal problem statement and an honest map of why current methods stop. Two signals held pattern-less. The eight-synonym list (sleep-time compute, neural memory, write-time compute, note taking, **dreaming**, studying, machine studying, amortized inference) is directly useful to the coin decision: it is the clearest in-corpus evidence that this is one thesis with no settled name, and it links this talk to Anthropic's "dreaming" feature in the same batch.
2. **Rare in-track cross-citation.** The speaker refers to Ronak Malde's talk ("I think Ronak was talking about on-policy distillation") delivered earlier the same day. Both files are in this batch, and Malde's OPSD is the deeper treatment of the method Morris surveys in one line. Worth a proposed cross-file edge at seeding: `el-on-policy-self-distillation` (Malde) `EnablesElement → el-scaling-compute-on-context` (here) — **left to review** rather than emitted, since neither speaker states the dependency.
3. **⚠ Verify before seeding.** `co-engram` is reconstructed from captions plus the closing URL — the transcript never spells the name. The cited papers are gestured at, never named ("a very cute paper", "the cartridges paper", "three pretty interesting approaches"), so no artifact nodes are emitted for them; if the slides surface, several are probably citable.
4. **Pattern homing.** Two signals take `pat-model-not-bottleneck` (the ceiling is in the data-and-method layer around the model, not the model) and one takes `pat-accelerated-research` (self-improving loops that make their own problems harder). The `pat-accelerated-research` edge is the seed pattern's first genuinely *methodological* evidence rather than an instance of agents running experiments — flagged in case review prefers to hold it for the new candidate instead.
5. **Signal-bar caveat.** No numbers except the ~0.0001 loss anecdote, and no results from the company's own method beyond "our early curves plateaued and then didn't." This is a research-agenda talk from a week-old startup; its value to the corpus is the problem taxonomy, which is unusually clean, not any measured claim.
