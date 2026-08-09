# SPIKE extraction — "Building Great Agent Skills: The Missing Manual" (Matt Pocock, AI Hero) — FOR REVIEW

Source transcript: `transcripts/agent-skills-missing-manual.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/UNzCG3lw6O0 — AI Engineer World's Fair, published 2026-06-29. Recorded remotely (speaker could not attend in person).
Speaker not named in the talk title — resolved from the transcript: "we have Matt Pocock skills, which is my skills repo" + newsletter at aihero.dev → **Matt Pocock (AI Hero)**. See Review notes.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-06-29 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-pocock-missing-manual` | Building Great Agent Skills: The Missing Manual (Matt Pocock, AI Hero — AI Engineer World's Fair) | youtube | https://youtu.be/UNzCG3lw6O0 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-matt-pocock`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-matt-pocock` | Matt Pocock (developer educator, aihero.dev; author of the Matt Pocock skills repo, one of the most popular engineering skill sets) | `AffiliatedWithCompany → co-ai-hero` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-ai-hero` | AI Hero | media | Matt Pocock's developer-education outfit (aihero.dev): newsletter and courses on AI-assisted engineering; an "AI coding crash course" announced as upcoming. Type `media` is a judgment call — `developer` also defensible |

## Elements (2 new, 2 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-leading-words` | Leading words | concept | harness | Skill-steering technique: compact, high-prior phrases (e.g. "vertical slice" instead of a paragraph about not coding layer-by-layer) placed in skill text; the agent repeats them in its reasoning traces and output, re-emphasizing the packed-in behavior. Consistent use across the skill is the lever; the phrase surfacing in thinking traces is the observable success check |
| `el-matt-pocock-skills` | Matt Pocock skills | framework | harness | Popular open-source engineering skills repo (2PRD, grill-with-docs, domain-modeling, grill-me, writing-great-skills…) built around user-invoked skills, minimal skill.md files, and branch-specific reference hidden behind context pointers; the talk's whole checklist ships as the `writing-great-skills` skill inside it |

Reused: `el-agent-skills` **[registry]**, `el-progressive-disclosure` **[registry]** (the talk's "context pointers" are the same mechanism — flagged in Review notes).
Element edges: both new elements `IdentifiedInArtifact → ia-aie-pocock-missing-manual`. No company edge on `el-matt-pocock-skills` (personal OSS, not an AI Hero product).

## Signals (3 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-pocock-missing-manual`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | OnElement | RelevantCompany |
|---|---|---|---|---|
| `sig-skill-hell` | After tutorial hell and framework hell, practitioners are in "skill hell": freely downloadable community skills proliferate with no shared rubric to tell good from bad; individuals stack them without getting the promised results, and organizations cannot turn their operating procedures into working skills. The maintainer of one of the most popular skills repos reports even his own users are stuck ("just one more skill, bro") | `FormsPattern → pat-agent-supply-chain` | `OnElement → el-agent-skills` | — |
| `sig-model-invocation-tax` | The skill-invocation tradeoff, quantified by a leading skills author: every model-invoked skill's description permanently occupies agent context (100 skills = 100 descriptions on every request) and adds trigger unpredictability — the model may simply not follow a perfect context pointer — which forces skill-trigger evals. User-invoked skills instead tax human cognitive load. He deliberately ships user-invoked skills to delete the eval problem rather than manage it | `FormsPattern → pat-harness-over-model` | `OnElement → el-agent-skills` | — |
| `sig-plan-mode-eager-planning` | Consistent failure mode across every plan-mode implementation the author tried: the ask-clarifying-questions step never does enough legwork because the agent sees the downstream goal (produce a plan) and eagerly skips ahead; hiding future steps — splitting phases into separate skills so the agent sees one step at a time — reliably fixes it | `FormsPattern → pat-harness-over-model` | `OnElement → el-agent-skills` | — |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-context-load-vs-cognitive-load` | Skill invocation design is budget allocation between two scarce resources: model-invoked skills spend agent context (tokens on every request + one more thing to weigh) and buy convenience; user-invoked skills spend human cognitive load ("skill required of the pilot") and buy determinism. Neither is free — "more flexible" model invocation is a cost, not a default | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-agent-skills` |
| `ins-skills-need-lint` | Skills are a new class of software artifact stuck pre-linting: with no shared quality rubric, badness is invisible until failure. A checklist — trigger → structure → steering → pruning — functions as lint for skills, including auditing community-authored skills before pulling them into your environment | `HighlightsPattern → pat-agent-supply-chain` | `ReliesOnElement → el-agent-skills`, `ReliesOnElement → el-matt-pocock-skills` |

## KnowHow (4 new)

All `SourcedFromArtifact → ia-aie-pocock-missing-manual`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-skill-invocation-choice` | Decide user- vs model-invoked per skill | A skill's description is a context pointer that lands in agent context (model-invocable) unless disabled (`disable-model-invocation: true` → user-only); tamp down the number of model-invoked skills or go user-invoked; accept cognitive load on the human when trigger predictability matters more than convenience | `ReferencesElement → el-agent-skills` |
| `how-skill-structure-small` | Compose as steps + reference; keep skill.md minimal | Break every skill into steps (the procedure) and reference (supporting material); map the skill's branches; reference used on every branch stays in skill.md, branch-specific reference moves behind context pointers into bundled external files the agent pulls only when that branch is live; smaller skill.md = cheaper, easier to audit and maintain | `ReferencesElement → el-agent-skills`, `ReferencesElement → el-progressive-disclosure` **[registry]** |
| `how-leading-words-steering` | Steer with leading words; verify in traces | Choose phrases with strong priors that pack in the wanted behavior ("vertical slice"); repeat them consistently throughout the skill; confirm steering by watching the words reappear in reasoning traces; when a step needs more legwork, split it into its own skill so the future goal is hidden (e.g. grill-with-docs then 2PRD instead of one plan mode) | `ReferencesElement → el-leading-words` |
| `how-skill-pruning` | Prune skills with deletion tests | Massive skills are a symptom, not a style: enforce a single source of truth per piece of material (no duplication across steps/reference); clear sediment from communal editing (stale or never-relevant additions nobody dared delete); run deletion tests for no-ops — paragraphs whose removal doesn't change behavior (e.g. "write a long detailed commit message") get cut | `ReferencesElement → el-agent-skills` |

## Dropped

- "Superpowers" — the popular, primarily model-invoked skills repo used as the comparison anchor; one mention as contrast, deliberately not coined (see Review notes).
- Individual skills (2PRD, grill-me, grill-with-docs, domain-modeling, writing-great-skills) — features of `el-matt-pocock-skills`, kept as prose.
- Tutorial hell / framework hell framing — rhetorical setup, folded into `sig-skill-hell`.
- aihero.dev newsletter and coding-crash-course plans — speaker promo, folded into the company brief.

## Review notes

1. **Speaker identification** (title omitted it): resolved to Matt Pocock with high confidence — self-identifies as owner of "Matt Pocock skills" (captions also render "Matt Percot", "papago skills") and of the aihero.dev newsletter. Verify against the video byline before seeding. Affiliation modeled as AI Hero; the skills repo itself treated as personal OSS.
2. Talk was pre-recorded remotely for the conference — still an AIE World's Fair talk on the channel; artifact handled normally.
3. "Superpowers" not coined: single comparative mention here; it has not appeared elsewhere in the registry. Coin on recurrence (it is a real, popular community skills repo — likely to show up again).
4. Both `sig-model-invocation-tax` and `sig-plan-mode-eager-planning` form `pat-harness-over-model` on the reading "determinism engineered around the model beats trusting model choice." If review holds that pattern to runtime scaffolding only, park `sig-plan-mode-eager-planning` pattern-less.
5. `el-progressive-disclosure` **[registry]** equated with the talk's "context pointers" — same mechanism under a different name; unlink if review reads the registry element more narrowly.
6. This is a techniques talk with few dated external facts (like the Daga file): all three signals are practitioner-testimony observations. Fallback if that fails the signal bar: keep `sig-skill-hell` + the two insights.
