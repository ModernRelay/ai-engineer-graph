# SPIKE extraction — "Using Spec-Driven Development for Production Workflows" (Erik Hanchett, AWS) — FOR REVIEW

Source transcript: `transcripts/hanchett-aws-spec-driven-development.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/IddXPepIAS4 — AI Engineer World's Fair, published 2026-06-28.
`stagingTimestamp` for the artifact and all signals: 2026-06-28 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-hanchett-spec-driven` | Using Spec-Driven Development for Production Workflows (Erik Hanchett, AWS — AI Engineer World's Fair) | youtube | https://youtu.be/IddXPepIAS4 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-erik-hanchett` **[registry]**.

## Experts (0 new)

- `exp-erik-hanchett` **[registry]** (batch 8, senior developer advocate, AWS) — no new node. This is his second talk in the corpus (first: `ia-aie-hanchett-agent-wasting-tokens`); the batch-8 file pre-flagged this talk for reuse.

## Companies (0 new)

- `co-aws` **[registry]** — reused.

## Elements (3 new + 3 registry reuses)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-spec-driven-development` | Spec-driven development | concept | harness | Workflow in which structured specifications are created before any code: a requirements document (EARS-format user stories, produced after clarifying questions), a design document (architecture, mermaid diagrams), and an implementation task list — persisted as markdown the coding agent works from and the human edits between phases; the corrective to vibe-coding on larger features, complex projects, and legacy codebases |
| `el-kiro` | Kiro | product | harness | AWS's AI IDE + CLI (kiro.dev) built around vibe mode vs. spec mode: spec mode runs the requirements → design → tasks flow with clarifying questions, a quick-plan variant, steering docs, spec-mode-for-bug-fixes, and generated property-based tests; born from watching customers hand-roll the pattern; launch went viral (tens of thousands of downloads, gated preview that people bypassed) |
| `el-property-based-testing` | Property-based testing (against spec docs) | technology | harness | Tests generated from the requirements + design documents and run dozens-to-hundreds of times with randomized values (fast-check in the TypeScript demo) to verify that agent-implemented tasks actually satisfy the spec — machine verification wired to the spec artifacts rather than to hand-written cases |
| **[registry]** `el-agents-md` | — | — | — | reused (batch 6); the talk's context caution centers on agents.md / CLAUDE.md ("claw.md" in captions) steering files — the Goldilocks-zone advice below |
| **[registry]** `el-agent-skills` | — | — | — | reused (batch 1); recommended companion to spec-driven development — keyword- or slash-activated instruction files that fire on demand during spec creation or task implementation, instead of bloating the always-on steering doc |
| **[registry]** `el-mcp` | — | — | — | reused (seed); defended against "isn't MCP dead" takes and used to pull Jira/Asana tickets and PM-written requirements docs into the spec-creation step |

Element edges: `el-spec-driven-development`, `el-kiro`, `el-property-based-testing` `IdentifiedInArtifact → ia-aie-hanchett-spec-driven`; `el-agents-md`, `el-agent-skills`, `el-mcp` **[registry]** `IdentifiedInArtifact → ia-aie-hanchett-spec-driven`; `el-kiro` `DevelopedByCompany → co-aws` **[registry]**, `UsesElement → el-spec-driven-development`; `el-spec-driven-development` `ExemplifiesPattern → pat-harness-over-model` **[registry]**; `el-property-based-testing` `ExemplifiesPattern → pat-verification-gap` **[registry]**.

## Signals (5 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-hanchett-spec-driven`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-aws-productizes-spec-driven` | AWS watched teams and customers vibe-coding into bad outputs and hand-rolling a bespoke fix — having assistants write full requirements + design documents before code — and productized the pattern as Kiro (IDE + CLI); launch went viral with tens of thousands of downloads and a bypassed preview gate. Aside: the CLI version is "just as popular... most people are starting to use CLIs more often than IDEs" (paraphrase) — spec-driven development moving from folk practice to vendor product | `FormsPattern → pat-harness-over-model` **[registry]** | `RelevantCompany → co-aws` **[registry]**; `OnElement → el-kiro`, `OnElement → el-spec-driven-development` |
| `sig-models-still-need-specs` | Vendor answer to "can't the latest frontier models just do everything?": no — models improve every release, and harnesses are adding thinking/planning modes, but coding assistants are "AI interns" (paraphrase) that go off the rails with leeway; persisted spec documents with the human editing between phases still beat jump-to-code | `FormsPattern → pat-harness-over-model` **[registry]** | — |
| `sig-accountability-stays-human` | "Everything in the spec-driven development flow is you": the developer is the code reviewer of all generated code and the interactive editor of the requirements/design docs, because "if something goes wrong, you are the person that's going to be blamed for it, not the agent" (paraphrase) — accountability for agent output stays with the human, with AI review tools as assist, not replacement | `FormsPattern → pat-value-of-judgement` **[registry]** | — |
| `sig-property-tests-enter-agent-flow` | Kiro's spec flow generates property-based tests tied to the requirements and design documents (fast-check; dozens-to-hundreds of randomized runs per property) so the machine — not just the human reviewer — checks that agent-implemented tasks satisfy the spec; formal-methods-adjacent verification appearing as a default feature in a mass-market coding tool | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-property-based-testing`, `OnElement → el-kiro` |
| `sig-mcp-dead-claims-premature` | Hype-cycle whiplash datum: barely months after launch, "isn't MCP 6 months old and it's dead now?" is a question a vendor advocate must rebut on stage (the CLI-tools-suffice argument); his position — MCP is still maturing with a long road ahead, "especially with some of the security stuff it's doing" (paraphrase), and earns its keep piping PM systems (Jira/Asana requirements) into spec creation | — (pattern-less; see review note 3) | `OnElement → el-mcp` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-specs-are-durable-context` | The spec documents ARE the context engineering: requirements, design, and task lists persisted as markdown give the model durable, reviewable context — and give the human defined checkpoints to inject knowledge, expertise, and taste ("it's only as good as what you put in," paraphrase) — where in-harness planning modes are ephemeral and uninspectable | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-spec-driven-development` |
| `ins-goldilocks-steering-context` | Steering context has a Goldilocks zone: too little and the model goes off the rails, too much and quality degrades — keep agents.md/CLAUDE.md-style always-on files down to the rules that matter, and move on-demand knowledge into keyword-activated skills that load only when triggered | `HighlightsPattern → pat-harness-over-model` **[registry]** | `ReliesOnElement → el-agents-md` **[registry]**, `ReliesOnElement → el-agent-skills` **[registry]** |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-hanchett-spec-driven`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-three-doc-spec-flow` | Run the three-document spec flow (with or without Kiro) | (1) Requirements: have the assistant ask clarifying questions first, then produce EARS-format user stories — or seed it with the PM's actual requirements doc pulled via MCP from Jira/Asana (add a steering rule pointing at the MCP server); (2) design doc: architecture + mermaid/sequence diagrams — STOP here and edit in your own knowledge and taste, and review the markdown for inconsistencies and hallucinations; (3) implementation task list — tip: "take the top four tasks, put them at the top, and create an MVP first" so you see it working before implementing the rest. Works on years-old legacy codebases (dozens of spec files) and even bug fixes, not just greenfield; vibe-code the small stuff instead. Doable manually with any assistant, with GitHub's open-source kit, or in Kiro's spec mode | `ReferencesElement → el-spec-driven-development`, `ReferencesElement → el-kiro`, `ReferencesElement → el-mcp` **[registry]** |
| `how-property-tests-from-specs` | Generate and run property-based tests against the spec | Have property-based tests created from the requirements + design documents and actually executed (fast-check in TS runs each property dozens-to-hundreds of times with randomized values) so task implementations are machine-checked against the spec, e.g. "for any movie data set the extracted genre list must contain exactly a sorted set of unique genres" (paraphrase of demo) | `ReferencesElement → el-property-based-testing`, `ReferencesElement → el-spec-driven-development` |

## Dropped

- GitHub "Spec It" → almost certainly **Spec Kit** (GitHub's open-source spec-driven toolkit) — one-sentence shout-out, kept prose inside `how-three-doc-spec-flow`; registry `co-github` not edged.
- EARS format (Easy Approach to Requirements Syntax) as an Element — requirements-engineering notation predating AI, kept prose.
- The VP-intern anecdote — rhetorical frame for `sig-models-still-need-specs`.
- Jira/Asana — named only as MCP-reachable ticket systems; prose.

## Review notes

1. **Caption garbles:** "Qiro" and "Cara" → Kiro (kiro.dev appears verbatim in the transcript); "Spec It" → GitHub Spec Kit (unverified against captions, flagged); "claw.md" → CLAUDE.md. "We released Qiro uh early late last year in a general availability" — the GA timeline is garbled; not treated as a dated fact. Quotes are paraphrases.
2. **Same-speaker reuse:** `exp-erik-hanchett` + `co-aws` reused from batch 8 (`hanchett-aws-agent-wasting-tokens.md`), which pre-flagged this talk. The Eric-vs-Erik spelling flag from that file still stands (transcript sign-off "Eric Hanchett"; official listing "Erik").
3. `sig-mcp-dead-claims-premature` is deliberately pattern-less: it is an adoption/hype-velocity datum. `pat-agent-supply-chain` was considered for the MCP-security nod ("the security stuff it's doing") but the mention is too thin for an edge; note it as weak ambient evidence there.
4. `el-property-based-testing` is a decades-old technique (QuickCheck lineage) — coined anyway because its role here (spec-doc-derived machine verification of agent-implemented tasks) is the talk's load-bearing verification mechanism; precedent: daga's `el-semantic-layer`. Merge target if another batch coined a property-testing node under a different slug (none found).
5. Cross-talk resonance worth a registry note: Kiro's spec mode is the productized twin of the manual spec-culture signals elsewhere in this batch (razgaitis's RPT doc) and of batch-8 Tornow's spec-is-the-product — mild extra evidence for the `pat-adaptive-software` candidate ledger, but this talk treats specs as pre-code guidance, not as the runtime product, so no candidate evidence claimed.
