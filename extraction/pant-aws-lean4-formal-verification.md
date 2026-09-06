# SPIKE extraction — "Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers" (Varun Pant, AWS) — FOR REVIEW

Source transcript: `transcripts/pant-aws-lean4-formal-verification.txt` (auto-captions — quotes are paraphrases, not verbatim; a 10-minute lightning talk).
Video: https://youtu.be/lRa9sPaMyy4 — AI Engineer World's Fair, published 2026-08-28.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: agents generate thousands of PRs a week; LLM-as-judge is probabilistic, tests check some inputs, human review doesn't scale — only **formal verification** says "for all inputs." The methodology: **humans own the specification, machines own the code and the proof** — write what correct means (in Lean, or in natural language auto-formalized by AI), validate the spec (it is upstream of everything), let the coding agent implement, let the prover check. Lean is code and proof in one language with a small trusted kernel and independently checkable proofs. Exhibits: an AI converted zlib to Lean in about a week with 32,000 lines of proof; Cedar (AWS's authorization language) has its spec in Lean and production in Rust, reconciled by ~100M differential random tests nightly; Verus (Z3 pre/post conditions), Aeneas (Rust MIR → Lean), and AWS's work-in-progress **Strata** (any language → dialect → a Lean-based core IR → provers, SMT solvers, model checkers). Caption garbles: "back driven development" → **spec-driven development**, "Andreo" → ⚠ unclear (the zlib conversion's author), "forbid Trump's permit" → **forbid trumps permit**, "Eneus" → **Aeneas**, "Arena Lang" → ⚠ likely a Lean community link, "probably correct" (end) → **provably correct**.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-pant-aws-lean4-formal-verification` | Your Code Has Bugs. Lean4 Has Proofs: Formal Verification for Engineers (Varun Pant, AWS — AI Engineer World's Fair) | youtube | https://youtu.be/lRa9sPaMyy4 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-varun-pant`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-varun-pant` | Varun Pant (AI products / formal verification teams, AWS) | `AffiliatedWithCompany → co-aws` **[registry]** |

## Companies (0 new)

Reused **[registry]**, edge-only: `co-aws` — new facts: leads formal-verification product teams; Cedar (spec in Lean, Rust in production, used by Verified Permissions) ships no version until ~100M nightly differential tests pass; building **Strata**, an open-source any-language verification IR in Lean; Kiro as the spec-driven entry point. Referenced, not coined: the Lean community, Z3, the open-source zlib-to-Lean conversion.

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-humans-own-the-spec-machines-own-code-and-proof` | Humans own the specification; machines own the code and the proof | concept | harness | Spec-driven development (e.g. with Kiro) with a proof at the end: write what correct means — formally in Lean, or in natural language that AI **auto-formalizes** — then **validate the specification** (human review, or test that it holds on some inputs), because the spec is upstream: "a living, breathing artifact the builder interacts with; everything else is downstream." The coding agent implements from the spec; the verification tool proves the implementation satisfies it, for every possible input. Contrast: LLM-as-judge is probabilistic, tests cover some inputs, human review can't match agent throughput |
| `el-lean-kernel-and-tactics` | Lean: one language for code and proof, a small kernel, tactics as chess moves | concept | harness | Lean is a programming language and a proof assistant in the same language — no translation layer — implemented in Lean (extensible), with a **small trusted kernel** and proofs that can be exported and checked by independent kernels (C++, Rust, Lean — you can write your own). Proving is chess: tactics are moves, the theorem is checkmate, you traverse a tree and backtrack from dead branches; an incorrect proof is rejected immediately by the kernel. AI decomposes a theorem into lemma subgoals, proves each with tactics, assembles the theorem, and the kernel checks it |
| `el-cedar-differential-verification` | Cedar: spec in Lean, production in Rust, nightly differential testing | technology | security | AWS's open-source authorization policy language has its functional specification in Lean and its production implementation in Rust; properties such as "for any satisfied forbid policy the request is always denied" are proven on the model, and ~100 million differential random tests run nightly to check the Rust code matches the Lean spec on the same inputs — "no version ships until this is satisfied." The pattern for verifying code you don't rewrite in Lean |
| `el-strata-verification-ir` | Strata and the deductive-verification toolchain | technology | harness | For Rust: **Verus** (pre/post conditions — `requires`/`ensures` — as static, runtime-erased "ghost" checks discharged by the Z3 solver, "a very powerful calculator") and **Aeneas** (Rust MIR → functional translation into Lean, then the same prover). For any language: AWS's work-in-progress open-source **Strata** — define a dialect (like a compiler front end), lower a high-level IR to Strata core (written in Lean), then dispatch to any engine: the Lean prover, SMT solvers, model checkers |

Element edges: all four `IdentifiedInArtifact → ia-aie-pant-aws-lean4-formal-verification`.
`el-humans-own-the-spec-machines-own-code-and-proof` `UsesElement → el-lean` **[registry]**, `el-spec-driven-development` **[registry]**, `el-kiro` **[registry]**, `el-verifiers-law` **[registry]**;
`el-lean-kernel-and-tactics` `UsesElement → el-lean` **[registry]**;
`el-cedar-differential-verification` `UsesElement → el-lean-kernel-and-tactics`, `el-property-based-testing` **[registry]**;
`el-strata-verification-ir` `UsesElement → el-lean-kernel-and-tactics`;
`el-cedar-differential-verification` `DevelopedByCompany → co-aws` **[registry]**;
`el-strata-verification-ir` `DevelopedByCompany → co-aws` **[registry]**;
`el-humans-own-the-spec-machines-own-code-and-proof` `ExemplifiesPattern → pat-verification-gap` **[registry]**;
`el-lean-kernel-and-tactics` `EnablesPattern → pat-verification-gap` **[registry]**.

Reused elements (no new nodes): `el-lean` **[registry]**, `el-spec-driven-development` **[registry]**, `el-kiro` **[registry]**, `el-verifiers-law` **[registry]** (a proof is the ultimate free grader), `el-property-based-testing` **[registry]**, `el-proof-carrying-agent-plans` **[registry]**, `el-generator-validator-separation` **[registry]**.

## Signals (4 new)

All: `SpottedInArtifact → ia-aie-pant-aws-lean4-formal-verification`, `SourcedFromSource → source-aie-yt` **[registry]**; all `RelevantCompany → co-aws` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-only-proofs-scale-to-agent-throughput` | harness | With agents producing hundreds and thousands of PRs a week, the three verification options fail on coverage or throughput — LLM-as-judge is probabilistic, tests check some inputs, human review can't keep up — and "none can say for all inputs the code is correct. Formal verification can." AWS's formal-verification product lead positions proofs as the verification layer that matches agent speed | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-humans-own-the-spec-machines-own-code-and-proof`, `el-verifiers-law` **[registry]** |
| `sig-humans-own-the-spec-machines-own-code-and-proof` | harness | The division of labor: the human writes and validates the specification (or validates an AI auto-formalization of natural language), the coding agent implements, the prover checks. The spec is the upstream living artifact the builder owns; everything else is machine work. Judgement relocates to *what correct means*, and the machine's output is trusted because a small kernel checked it | `FormsPattern → pat-verification-gap` **[registry]**; `FormsPattern → pat-value-of-judgement` **[registry]** | `OnElement → el-humans-own-the-spec-machines-own-code-and-proof`, `el-spec-driven-development` **[registry]** |
| `sig-ai-converted-zlib-to-lean-with-32k-lines-of-proof` | harness | An open-source AI conversion of zlib (a C compression library) to Lean in about a week: natural-language spec ("decompress of compress returns the original") → AI-generated formal spec (checked) → AI-written Lean code → AI-generated helper lemmas and a proved theorem, ~32,000 lines of proof, verified by the independent kernel. An agent doing the decomposition-and-proof work at library scale | `FormsPattern → pat-accelerated-research` **[registry]**; `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-lean-kernel-and-tactics` |
| `sig-cedar-ships-only-after-100m-differential-tests` | security | Cedar's spec lives in Lean and its production code in Rust; properties like "forbid trumps permit" are proven on the spec, and ~100M differential random tests nightly confirm the Rust matches — no version ships otherwise. With Verus, Aeneas and Strata, AWS is building the toolchain to verify code in the language it's written in rather than rewriting it | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-cedar-differential-verification`, `el-strata-verification-ir` |

## Insights (1 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-the-spec-is-the-human-artifact` | The durable claim inverts where trust comes from: when generation is machine-speed, the only checker that also runs at machine speed with total coverage is a proof against a specification — so the human's irreplaceable artifact becomes the spec (and its validation), not the code or the review. The corpus's verification-gap thesis gets its strongest-form answer, with the boundary made explicit: an auto-formalized spec must itself be validated, or the proof proves the wrong thing | `HighlightsPattern → pat-verification-gap` **[registry]** | `ReliesOnElement → el-humans-own-the-spec-machines-own-code-and-proof`, `el-lean-kernel-and-tactics`, `el-cedar-differential-verification` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-pant-aws-lean4-formal-verification`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-verify-agent-written-code-formally` | Own the spec, validate it, let machines prove the rest | Pick your most critical code and **write what correct means** — formally in Lean, or in natural language that AI auto-formalizes; **validate the specification** (human review, or test it on sample inputs) before anything is built on it, because it is upstream of all the code and proofs; let the coding agent implement from the spec and let the prover — Lean's small kernel — check it for all inputs, decomposing into lemmas as needed; for code that stays in Rust use pre/post conditions with a solver (Verus) or translate to Lean (Aeneas), or keep the spec in Lean and reconcile production with nightly differential random testing (Cedar's ~100M/night, ship-gating); for other languages watch Strata (dialect → Lean core IR → provers, SMT, model checkers); and remember that proofs can be exported and checked by an independent kernel you can write yourself | `ReferencesElement → el-humans-own-the-spec-machines-own-code-and-proof`, `el-lean-kernel-and-tactics`, `el-cedar-differential-verification`, `el-strata-verification-ir` |

## Dropped

- **The list-reverse example** — illustration of code + theorem in one file; folded into the Lean element.
- **"Go to Lean in your browser"** — the call to action; a clause in the know-how.

## Review notes

1. **`pat-verification-gap` in its strongest form** (proofs for all inputs) from the vendor building the tooling; pairs with the corpus's `el-lean` / `el-proof-carrying-agent-plans` (earlier batches) and with Hall's b22 "the compiler is a free grader."
2. **`sig-ai-converted-zlib-to-lean-with-32k-lines-of-proof` → `pat-accelerated-research`** is a support point (an agent doing library-scale formalization) — sits opposite Arora's measured counter in the same batch; both belong in the pattern brief.
3. **⚠ Verify before seeding:** the zlib conversion's author and "about a week / 32,000 lines," the "~100 million nightly" Cedar figure, and Strata's status.
