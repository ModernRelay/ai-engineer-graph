# SPIKE extraction — "The Miranda Hypothesis: How Hamilton Poisoned Persona Evals" (Jacob E. Thomas, Results Gen) — FOR REVIEW

Source transcript: `transcripts/thomas-miranda-hypothesis-persona-evals.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/IJXjTLPzvAU — AI Engineer World's Fair, published 2026-06-25.
`stagingTimestamp` for the artifact and all signals: 2026-06-25 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-thomas-miranda-hypothesis` | The Miranda Hypothesis: How Hamilton Poisoned Persona Evals (Jacob E. Thomas, Results Gen — AI Engineer World's Fair) | youtube | https://youtu.be/IJXjTLPzvAU |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-jacob-thomas`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-jacob-thomas` | Jacob E. Thomas (data scientist; runs the analytics lab at Results Gen, a labor-market intermediary; trained as a behavioral epidemiologist; ships production AI at global scale) | `AffiliatedWithCompany → co-results-gen` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-results-gen` | Results Gen | developer | labor-market intermediary whose analytics lab ships production AI; appears here via its lab lead's independent persona-eval research, not as an AI vendor |

## Elements (6 new + 1 registry reuse)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-miranda-hypothesis` | Miranda hypothesis | concept | training | Three-part claim about persona contamination: (1) in training corpora, culturally dominant representations of a figure exceed the primary documentary record in volume and recency (Federalist Papers ~175k words vs. orders-of-magnitude-larger musical-derived content); (2) next-token prediction compresses both with no architectural way to distinguish a 1789 letter from a 2019 viral tweet; (3) output defaults to a salience-weighted composite — fluent, in register, morally legible to modern users, corresponding to the figure at no verifiable moment of their life. Named for the Hamilton musical as paradigm case |
| `el-epistemic-simulation` | Epistemic simulation | concept | context | Proposed fourth paradigm stage for role-playing language agents (after rule-based templates, imitation, cognitive simulation): the constraint lives outside the model — corpus-bounded (reasoning licensed only by a specific primary-document corpus; the model is a reader of the archive, not a substitute for it), temporally anchored (instantiated at a specific life moment; later knowledge out of bounds), and expert-loop evaluated (judged against the evidentiary record by domain experts) |
| `el-role-playing-language-system` | Role-playing language system | concept | context | Reframed unit of analysis for persona AI, replacing "agent": the whole configured encounter — structured prompt, anchor material from primary documents, a temporal anchor, an off-the-shelf swappable model (the voice, not the mind), and a human curator with interpretive custody. The persona is the configuration, not the checkpoint: versionable, diffable, auditable, reproducible, and legible to domain experts |
| `el-prism-protocol` | Prism protocol (pre-registered persona-fidelity instrument) | framework | harness | Pre-registered instrument for measuring anachronistic compositing: figure × documented life-moments × seeding conditions matrix (bare model / primary sources / modern biography), expert-written diagnostic questions on documented fault lines, and a three-axis weighted rubric — anachronism detection 40%, documentary consistency 35%, contextual plausibility 25% — with rhetorical authenticity deliberately excluded as a criterion; predictions locked and timestamped before data collection; expert holds sealed a-priori vignettes. Pilot design: 4 Lincolns (1847/1858/1860/1862–65) × 3 conditions × 5 questions = 60 scored responses |
| `el-incharacter-benchmark` | InCharacter benchmark | framework | harness | Field gold-standard for RPLA personality fidelity, evaluating via psychological interviews rather than self-report scales; reports state-of-the-art systems at 80.7% alignment with human-perceived target-character personality — the talk's anchor example of an eval that measures convincingness (fluency, personality consistency) with no mechanism to measure fidelity to the documentary record |
| `el-time-locked-models` | Time-locked models | concept | training | Models trained from scratch on corpora that stop at fixed historical cutoffs ("Varnum and colleagues" per captions), addressing future contamination at the substrate level; endorsed by the speaker but argued to solve a different problem — a 1789-locked model is spared the musical yet still averages everything pre-1789 into a composite: period anchoring is not persona anchoring, so the fix must happen at the encounter |
| **[registry]** `el-claude-opus-47` | — | — | — | reused (batch 2); the speaker's open-source Companion framework demo (founding fathers, Lincoln instantiations) runs on Claude Opus 4.7 as the swappable frontier model |

Element edges: all six new elements `IdentifiedInArtifact → ia-aie-thomas-miranda-hypothesis`; `el-claude-opus-47` **[registry]** `IdentifiedInArtifact → ia-aie-thomas-miranda-hypothesis`; `el-miranda-hypothesis` `ExemplifiesPattern → pat-verification-gap` **[registry]**; `el-epistemic-simulation` `ExemplifiesPattern → pat-verification-gap` **[registry]**; `el-prism-protocol` `UsesElement → el-epistemic-simulation`.

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-thomas-miranda-hypothesis`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern |
|---|---|---|---|
| `sig-persona-evals-miss-dominant-failure` | harness | Persona-eval researcher/practitioner: the RPLA field's measurement apparatus — including the gold-standard InCharacter benchmark (80.7% personality fidelity) and the LLM-as-judge evaluators adopted for scale — systematically privileges fluency and personality consistency and has no mechanism to detect anachronistic compositing, the dominant failure mode; a top-scoring Hamilton "has read his own Broadway musical" (paraphrase). Full thesis: if the dominant failure is anachronistic compositing and evals measure fluency/consistency, the evals cannot detect the dominant failure | `FormsPattern → pat-verification-gap` **[registry]** |
| `sig-composite-overwrites-record` | training | The Miranda mechanism observed in the wild: culturally dominant representations overwrite documentary figures — reproducible today on any frontier model (a bare-model 1847 Lincoln reasons with "inherent executive authority," a 20th-century construction, in Spielberg's war-president register, while the actual 1848 Lincoln–Herndon letter argues the opposite); offline analog at the Schuyler Mansion, where post-musical visitors nearly tripled and arrived pre-loaded with wrong "facts" the staff must unteach | `FormsPattern → pat-verification-gap` **[registry]** |
| `sig-alignment-amplifies-composite` | training | Post-training does not pull personas back toward the record — it amplifies the composite: human raters evaluate with conceptual frameworks built by the same culturally dominant narratives that saturate the corpus, so preference optimization rewards the Hamilton the rater already believes in ("algorithmic sycophancy," paraphrase); compositing is not a bug you patch in post-training — post-training reinforces it | `FormsPattern → pat-verification-gap` **[registry]** |
| `sig-generalist-beats-persona-finetune` | training | Reported empirics against specialization-by-fine-tuning: a 2026 Nature Medicine study found general-purpose frontier models from Google, OpenAI, and Anthropic beat dedicated specialized clinical AI tools on physician-reviewed tasks blinded across 12 clinics; a separate study found biomedically fine-tuned models underperform their own base models (named mechanism: catastrophic forgetting). Speaker's transfer claim: persona fine-tuning does the same, layering a thin personal signal over cultural sediment while destroying auditability | `FormsPattern → pat-model-not-bottleneck` **[registry]** |
| `sig-persona-is-configuration` | context | Architectural reframe for role-playing systems: the persona lives in the configured encounter — prompt, primary-document anchors, temporal anchor, human curator — with the model as a swappable off-the-shelf component ("no more located in the weights than Hamlet is located in Laurence Olivier's body," paraphrase); context-window anchoring keeps documents intact and auditable where fine-tuning dissolves the archive into parameters, and it is a "kitchen-table capability" (free-tier model + documents + literacy) vs. fine-tuning's institutional one | `FormsPattern → pat-harness-over-model` **[registry]** |

## Insights (3 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-convincingness-fidelity-independent` | Convincingness and fidelity are independent properties: a system can score perfectly on personality consistency while reasoning from knowledge its historical counterpart never possessed. Current eval stacks were built to reward fluency, so they structurally cannot perform the inversion the problem requires — scoring plain-but-faithful above fluent-but-anachronistic | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-incharacter-benchmark`, `ReliesOnElement → el-miranda-hypothesis` |
| `ins-expert-is-the-instrument` | Fidelity is a relation between an output and a documentary record, so no automated metric operating on the model alone can adjudicate it — the metric cannot see the archive. A domain expert (historian, classicist, theologian, clinical psychologist) in the evaluation loop is a structural technical requirement, not a courtesy: "a persona system without a domain expert in its evaluation loop is a thermometer that cannot read temperature" (paraphrase) | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-prism-protocol`, `ReliesOnElement → el-epistemic-simulation` |
| `ins-archival-is-auditable` | The property that makes context-window persona architecture ethical is the same property that makes it debuggable: documents stay documents (provenance preserved, human interpretive custody, reversible encounter), so every input shaping the output is inspectable rather than smeared across billions of parameters — archival virtues and engineering virtues are the same virtues | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-role-playing-language-system` |

## KnowHow (3 new)

All `SourcedFromArtifact → ia-aie-thomas-miranda-hypothesis`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-compose-encounter-not-train` | Compose the encounter; don't train the persona | For role-playing systems: anchor primary documents in the context window at inference instead of fine-tuning them into weights; fix a temporal anchor (the specific life moment the persona speaks from — knowledge postdating it is out of bounds); keep prompt, corpus, and temporal anchor as versioned repo artifacts (diffable, revertible); keep a human curator with interpretive custody over what enters and what emerges; treat the model as the swappable voice, not the mind | `ReferencesElement → el-role-playing-language-system`, `ReferencesElement → el-epistemic-simulation` |
| `how-expert-eval-gate` | Gate persona systems on an expert-built instrument, not runtime staffing | The domain expert builds the instrument once — diagnostic questions on documented fault lines, sealed a-priori vignettes, weighted rubric (anachronism detection weighted highest; rhetorical authenticity excluded as a criterion), held-out gold set — and it becomes a pipeline gate: pass before ship, re-gate on every base-model change; automated metrics run only as a cheap first pass flagging candidates for expert review. Match expert to domain: classicist for a Marcus Aurelius tutor, theologian for a scripture companion, clinical psychologist for a therapeutic persona | `ReferencesElement → el-prism-protocol` |
| `how-prism-replication` | Replicate the pre-registered compositing experiment | Six steps: (1) pick a figure with both a primary record and a saturating cultural composite (the Miranda condition); (2) identify 3–4 documented moments where the figure's reasoning demonstrably differs; (3) with a domain expert, write diagnostic questions on those fault lines (test argument architecture, not recall); (4) run three seeding conditions — primary sources, modern biography, bare model; (5) score blind on the three-axis rubric; (6) report, confirm or refute, and publish corpus + questions + rubric + predictions before data exists | `ReferencesElement → el-prism-protocol` |

## Dropped

- Companion (the speaker's open-source prompt framework, demo vehicle on Claude Opus 4.7) — kept prose; the talk is about the eval gap, not the product. Coin `el-companion` at reconciliation if wanted.
- Character AI / Hello History as Company or Element nodes — platform examples establishing the RPLA class; folded into signal prose.
- CoSER ("Cooser"/"coaster" in captions; Wang et al., ~18k characters from hundreds of books, 70B model matching GPT-4 on three benchmarks) — field-context citation, prose only.
- Character-LLM, "26 qualitative psychological indicators" eval system — garbled citations, prose + review note.
- The mask-and-mirror metaphor, the "site of return" archive concept, the dementia hospital-room origin story — rhetorical/motivational frames folded into insights.
- Rick Halpern (historian, University of Toronto) and Shawn Martin (librarian, Washington College) — named collaborators who built the rubric/vignettes, not Experts contributing the artifact; see review note 3.

## Review notes

1. **`pat-benchmark-trust-crisis` (UNCOINED candidate) — STRONG added evidence, no edges, per instructions.** Specifics for the central decision: (a) the field's gold-standard benchmark (InCharacter, 80.7%) is shown structurally blind to the dominant failure mode of the system class it evaluates; (b) LLM-as-judge evaluators standard in the field "systematically privilege fluency and stylistic naturalness over fidelity to the record" (paraphrase of the talk citing Wang et al.); (c) alignment amplifies rather than fixes the error because raters share the contaminated prior (algorithmic sycophancy); (d) the corrective is a pre-registered, expert-scored instrument — i.e., trust re-architected outside the automated eval stack. All three signals carrying this evidence are parked on `pat-verification-gap` per registry briefs; rehome if/when the candidate is coined.
2. **Caption garbles:** "Cooser"/"coaster" → CoSER (Wang et al.); "Another eval system, Character.ai... 26 qualitative psychological indicators with knowledge graph memory" → likely a distinct benchmark (CharacterEval or similar), unresolved — do not read as the Character AI company; "In Character.ai, the one I opened with" → the InCharacter benchmark; "Varnum and colleagues" (time-locked models) — attribution unverified; "the philosopher Deirdre called the archive a site of return" → almost certainly Jacques Derrida; "E valves"/"E val's" → evals. Quotes throughout are paraphrases.
3. Halpern and Martin are load-bearing to the method (expert-in-the-loop) but did not author the talk; left un-coined to keep Expert = artifact contributor. Coin + affiliate at reconciliation if central wants collaborator experts.
4. Speaker affiliation: official listing "Results Gen"; transcript self-description "analytics lab at a labor market intermediary" — `co-results-gen` brief combines both; website unknown; company type `developer` is a judgment call.
5. `sig-generalist-beats-persona-finetune` carries secondhand citations (2026 Nature Medicine study; biomedical fine-tuning underperformance) — reported through the talk, not independently verified.
6. Element count is high (6 new) for one talk: the talk defines a named hypothesis, a proposed paradigm stage, a unit-of-analysis reframe, an instrument, a benchmark under critique, and an endorsed-but-critiqued alternative program — each carries distinct edges. Collapse `el-role-playing-language-system` into `el-epistemic-simulation` at reconciliation if that reads as one node.
7. "Prism" naming: the transcript introduces the instrument through a prism metaphor; it is not 100% clear "Prism" is the instrument's official name — `el-prism-protocol` slug chosen for retrievability, flag for verification against the forthcoming preprint.
8. Registry adjacents deliberately NOT edged: `el-item-response-theory` and `el-judge-as-classifier` **[registry]** (the psychometric-evals sibling material lives in batch 5's vidal file); `el-mcp` not mentioned. The pre-registration discipline echoes `pat-verification-gap`'s generator/validator logic rather than any element.
