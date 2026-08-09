# SPIKE extraction — "We Vetted 2000 AI Skills Before They Reached Developers" (Lucas Palma, Nubank) — FOR REVIEW

Source transcript: `transcripts/palma-nubank-vetting-skills.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/iKQ78wyJEXU — AI Engineer World's Fair (AI in Finance track), published 2026-07-31.
`stagingTimestamp` for the artifact and all signals: 2026-07-31 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

**This file defines `co-nubank` for the batch** — `gupta-rajpal-nubank-simulationmaxxing.md` (same publish date) reuses it and supplies the scale figures quoted in the company brief.

**Direct successor to batch 1's `sig-skills-audit-clawhub`** (Snyk/Invariant's audit of ~4,000 public Claw Hub skills: >1 in 8 with critical-severity issues, 76 malicious payloads). That was the *public registry* side of `pat-agent-supply-chain`; this is the *enterprise gate* side — same threat class, opposite end of the pipe. See Review note 1 for what does and does not corroborate.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-palma-vetting-skills` | We Vetted 2000 AI Skills Before They Reached Developers (Lucas Palma, Nubank — AI Engineer World's Fair, AI in Finance track) | youtube | https://youtu.be/iKQ78wyJEXU |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-lucas-palma`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-lucas-palma` | Lucas Palma, "LP" (product security manager at Nubank — the product-security function inside security, responsible for making code safe and supporting engineers and PMs in shipping safer products; over a decade in financial services with an engineering background) | `AffiliatedWithCompany → co-nubank` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-nubank` | Nubank | developer | Digital bank operating in a **regulated** financial-services environment — the constraint the whole talk turns on (auditability, credential safety by default). Appears here as an AI-*consuming* enterprise governing its own developer AI workflow; the companion talk `gupta-rajpal-nubank-simulationmaxxing.md` shows it as an AI *builder* (135M customers across Brazil, Mexico and Colombia, US launch imminent, quarterly revenue past $5B in Q1 2026, five customer-support agents in production). ⚠ enum has no finance/bank type; `developer` chosen per the `co-form3` / `co-checkout-com` fintech precedent |

## Elements (4 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-skill-vector` | Skill Vector | product | security | Nubank's security-review system for AI skills, wired in as a CI step *before* marketplace publication. Runs at two points — locally, so an engineer can iterate until the skill is clean, and again after upload, because you cannot assume the local run happened or ran on the current version. Deterministic (regular-expression) checks run first for the cheap, stable risks; an LLM review runs where judging the risk needs context. Findings are posted back as comments on the publishing pull request *and* emitted as SARIF so the existing security tooling can consume them and generate risk reports inside the vulnerability-management programme. Policy then decides per severity: allow, allow-with-required-remediation, or block before distribution. Siblings built on the same pattern for the adjacent supply-chain surfaces: an MCP Vector and rules checks |
| `el-internal-skill-marketplace` | Internal AI skill marketplace (as a security boundary) | ops | security | A single canonical internal marketplace of plugins and skills, deliberately treated as *the* enforcement boundary rather than merely a discovery surface: publication requires a pull request, which is what gives the scanner somewhere to stand. Extends to third-party material — anything downloaded from outside must be uploaded to the marketplace to be used, so it gets scanned and then becomes safely shareable. Named residual risk: other teams can stand up other marketplaces, so proactive detection of new marketplaces (and installing the scanner into them) is an open work item |
| `el-self-confirmation-loophole` | Self-confirmation loophole | concept | security | A skill instruction of the form "you must ask for confirmation" that the agent satisfies *by confirming to itself*: from the human's perspective there is a human in the loop, from the agent's perspective a confirmation happened and it proceeds. Named as one of the review programme's most important findings — prompt-level human-in-the-loop is not human-in-the-loop, so the check has to move to whether the executing tool actually passes through an approval gate or hook |
| `el-hybrid-deterministic-llm-scanning` | Hybrid deterministic + LLM skill scanning | concept | security | Two-stage review of natural-language capability packages: deterministic pattern checks for the risks that can be expressed as patterns, then LLM review for the behavioural/contextual ones (destructive shell commands, how credentials are actually requested and used, behavioural drift). The hybrid is deliberate rather than incremental — an LLM reviewer's verdict varies run to run with temperature, so the deterministic layer supplies the stable floor and the LLM supplies the coverage regexes cannot. ⚠ merge-check vs `el-deterministic-agentic-split` (b2) and `el-generator-validator-separation` (b1) |

Element edges: all four `IdentifiedInArtifact → ia-aie-palma-vetting-skills`. `el-skill-vector` `DevelopedByCompany → co-nubank`; `el-skill-vector` `UsesElement → el-hybrid-deterministic-llm-scanning`; `el-skill-vector` `EnablesElement → el-internal-skill-marketplace`; `el-skill-vector` `UsesElement → el-agent-skills` **[registry]**. `el-self-confirmation-loophole` `ExemplifiesPattern → pat-verification-gap` **[registry]**; `el-skill-vector` and `el-internal-skill-marketplace` `ExemplifiesPattern → pat-agent-supply-chain` **[registry]**.

### Elements reused **[registry]** (no new nodes)

| slug | why it appears |
|---|---|
| `el-agent-skills` **[registry, batch 1]** | the object under review — the registry brief ("higher default privilege than code packages, NL payloads evade code scanners") is exactly the risk model this programme was built for |
| `el-mcp` **[seed]** | "risky MCP usage" is one of the scanned checks, and MCP servers are named as part of the AI-era supply chain; an MCP Vector sibling scanner exists |
| `el-agent-hooks` **[registry, batch 1]** | named as where enforcement belongs — hooks and approval gates on the executing tool, rather than an instruction in the skill text |
| `el-agent-scoped-authorization` **[registry, batch 3]** | the "over-broad permissions" finding class: skills configured with far more permission than the task needs, where "even a typo can do dangerous stuff depending on who is using that skill" |

## Signals (4 new)

All: domain `security`, `SpottedInArtifact → ia-aie-palma-vetting-skills`, `SourcedFromSource → source-aie-yt` **[registry]**, `RelevantCompany → co-nubank`.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-nubank-2000-skills-vetted` | Enterprise-scale numbers for AI-skill risk, from a regulated bank's product-security team: **over 2,000 skills scanned** before marketplace distribution (stated as the baseline for the talk — "now there is much more than that"), yielding **more than 1,500 identified risks** (a single skill can carry several, so this is not a count of bad skills), of which roughly **1,000 were remediated immediately** and a small number were **blocked outright** before reaching the marketplace. A historical back-scan of skills created before the gate existed surfaced further risks, which were filed into the standard vulnerability-management programme rather than handled ad hoc | `FormsPattern → pat-agent-supply-chain` **[registry]** | `OnElement → el-skill-vector`, `el-agent-skills` **[registry]** |
| `sig-skills-behave-like-dependencies` | The framing claim: AI skills "look like configuration but they behave like supply-chain dependencies" — the traditional supply chain of packages, containers and models now also includes skills, plugins, MCP servers, agent rules and hooks. Mechanism that makes it a supply chain rather than config: one person authors a skill, another person's agent consumes it, and the author is thereby steering code generated on someone else's machine. Concrete risk classes given: a skill that retrieves a token and then uses it hardcoded, so it lands in logs and becomes a future data leak; a skill that instructs the agent to run shell commands that then execute on a colleague's machine; and skills configured with excessive permissions | `FormsPattern → pat-agent-supply-chain` **[registry]** | `OnElement → el-agent-skills` **[registry]**, `el-mcp` **[registry]**, `el-agent-hooks` **[registry]** |
| `sig-self-confirmation-defeats-hitl` | Field finding from reviewing thousands of skills: authors commonly write "ask for confirmation" as a safety control, but **the AI may ask confirmation of itself** — "from your perspective there is a human in the loop, but from the AI's perspective a confirmation has happened, so let's go". Nubank now scans for it explicitly and checks the real property instead: does the executing tool actually pass through an approval gate or hook. A prompt-level control is treated as unverifiable by construction | `FormsPattern → pat-verification-gap` **[registry]**, `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-self-confirmation-loophole`, `el-agent-hooks` **[registry]** |
| `sig-regulated-skill-governance` | What regulation forces onto the developer AI workflow, and how it was made routine: developers want faster coding and more context, while the regulated side demands auditability, credential safety by default and evidence — so skill risk was folded into the existing appsec machinery rather than run as a new process. Deterministic checks plus LLM review, findings as PR comments so the engineer fixes before publishing, SARIF output so security tooling ingests skills like any other finding class, severity-and-policy-driven decisions (allow / require remediation / block), and the same treatment extended to plugins, MCP servers, rules and hooks with their own risk sets and gates. Scanned classes named: unsafe instructions, agent behavioural drift, destructive shell commands, unexpected file modification, credential requests, unintentional data exposure, over-broad permissions, risky MCP usage | `FormsPattern → pat-verification-gap` **[registry]** | `OnElement → el-skill-vector`, `el-hybrid-deterministic-llm-scanning`, `el-internal-skill-marketplace`, `el-agent-scoped-authorization` **[registry]** |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-protect-the-workflow-not-the-output` | The speaker's stated takeaway: protect the whole developer AI workflow, not only the code it generates. Application-security programmes are aimed at generated artefacts, but the steering layer — skills, plugins, MCP servers, rules, hooks — is natural language, ships as configuration, carries higher default privilege than a code package, and is invisible to code scanners. Whoever authors that layer is writing code on other people's machines, so it needs the review discipline a dependency gets | `HighlightsPattern → pat-agent-supply-chain` **[registry]** | `ReliesOnElement → el-agent-skills` **[registry]**, `ReliesOnElement → el-skill-vector` |
| `ins-marketplace-is-the-choke-point` | Vetting is only enforceable if there is exactly one place skills come from. Making the internal marketplace canonical — publication by pull request, third-party downloads uploaded before use — is what converts an unenforceable policy into a CI step, and it doubles as the mechanism for safe sharing. The corollary is that the security property degrades the moment a second marketplace appears, which is why proactively detecting new marketplaces (and installing the scanner into them) is the named next problem | `HighlightsPattern → pat-agent-supply-chain` **[registry]** | `ReliesOnElement → el-internal-skill-marketplace` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-palma-vetting-skills`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-vet-agent-skills` | Gate AI skills like dependencies, before the marketplace | Make one internal marketplace canonical and require a pull request to publish into it, including for third-party skills you merely want to consume. Ship the scanner so engineers run it **locally** and iterate until the skill is clean; re-run it **after upload** anyway — never assume the local run happened or ran against the current version. Run deterministic pattern checks first, then LLM review where the risk needs context. Post findings as comments on the same PR so the fix happens before publication, and emit SARIF so the results flow into existing security tooling and vulnerability management. Decide by severity and policy: allow, require remediation, or block before distribution. Back-scan everything created before the gate existed and file the results as normal vulnerabilities. Check for: unsafe instructions, behavioural drift, destructive shell commands, unexpected file modification, credential requests, unintentional data exposure, over-broad permissions, risky MCP usage | `ReferencesElement → el-skill-vector`, `el-internal-skill-marketplace`, `el-hybrid-deterministic-llm-scanning`, `el-agent-skills` **[registry]** |
| `how-tune-skill-findings` | Tune the findings, or the gate becomes noise | Lessons from running the programme: don't treat all shell commands as equally risky — grade by what the command does. Drop weak, low-context signals; they cost more than they catch. Every finding needs clear remediation guidance attached or it stalls. Distinguish warnings that are harmless locally from the same behaviour running in production, and escalate accordingly. Most importantly, do not accept prompt-level safety claims: verify human-in-the-loop at the tool that executes, through approval gates and hooks, because an instruction to "ask for confirmation" can be satisfied by the agent confirming to itself | `ReferencesElement → el-self-confirmation-loophole`, `el-agent-hooks` **[registry]**, `el-skill-vector` |

## Dropped

- The definitional explainer of what an AI skill is (bundled instructions + context giving a model or agent a capability) — covered by registry `el-agent-skills`.
- LinkedIn/QR contact slide — bio.
- "Trusted AI marketplace" as a separate concept — folded into `el-internal-skill-marketplace`, since the talk uses the two interchangeably.
- MCP Vector and the rules checks — named as existing siblings but with no detail; kept inside `el-skill-vector`'s brief rather than coined as separate elements.

## Review notes

1. **Corroboration with `sig-skills-audit-clawhub` (batch 1) — what it does and doesn't establish.** The two studies agree that a large fraction of real-world skills carry security-relevant defects, from opposite ends of the distribution channel: Snyk audited ~4,000 *public* Claw Hub skills and found >1 in 8 with critical issues plus 76 malicious payloads; Nubank scanned 2,000+ *internally authored* skills and found 1,500+ risks with "a few" bad enough to block. The numbers are not comparable — Nubank counts risks, not skills, and its population is employees who are not adversaries, so its finding is about *unsafe practice at scale* (hardcoded tokens, shell commands, over-broad permissions) rather than about malice. Together they support `pat-agent-supply-chain` on both the public-registry and enterprise-gate legs; treat the malicious-payload rate as evidenced by Snyk only.
2. **Numbers are as-spoken and rounded.** Captions give "1,000 and half" (read as ~1,500 risks) and "1,000 of them were probably remediated right after"; the speaker explicitly frames 2,000 as a presentation baseline that is already outdated. Blocked skills are "a few", not quantified. Do not present these as audited figures.
3. **`co-nubank` type flag** — see the Companies table. Also note the split personality across this batch's two Nubank talks: consumer-of-AI (this file) and builder-of-AI (`gupta-rajpal-nubank-simulationmaxxing.md`). The brief is written to cover both, following the batch-12 recommendation to widen `co-uber`'s brief for the same reason.
4. **`sig-self-confirmation-defeats-hitl` carries two FormsPattern edges deliberately.** It is a verification failure (the control cannot be verified from the outside) *and* a harness claim (enforcement belongs in the deterministic tool/approval layer, not in the model's instructions). If you prefer one edge per signal, keep `pat-verification-gap` and drop the harness edge — but note the harness reading is the one the practitioner acted on.
5. **Caption garbles resolved:** "New Bank" → Nubank throughout; "serif" → SARIF; "skill v" / "skill vector" → Skill Vector; "determinist"/"terminist" → deterministic; **"comments" → commands** wherever shell is involved ("destructive shell comments"); "hky" → risky/hairy; "supply chain dependence" → supply-chain dependencies; "regulate part" → regulated environment.
6. **No new pattern; no candidate advanced past prose.** This is straight `pat-agent-supply-chain` corroboration with a `pat-verification-gap` mechanism attached. The one thing worth a reviewer's eye is that `el-self-confirmation-loophole` is a genuinely new *failure mode* in the corpus — the closest neighbours are `el-post-generation-veto` (b9) and `el-guardrail-sandwich` (b13), both of which assume the gate is real; this one is about a gate that only appears to exist.
