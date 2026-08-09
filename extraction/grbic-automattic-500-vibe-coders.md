# SPIKE extraction — "500 people vibe-coded for 30 days. I was one of them." (Sanja Grbic, Automattic) — FOR REVIEW

Source transcript: `transcripts/grbic-automattic-500-vibe-coders.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/UcYoMg-8-L8 — AI Engineer World's Fair, published 2026-07-07.
`stagingTimestamp` for the artifact, all signals, and knowhow: 2026-07-07 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-grbic-500-vibe-coders` | 500 people vibe-coded for 30 days. I was one of them. (Sanja Grbic, Automattic — AI Engineer World's Fair) | youtube | https://youtu.be/UcYoMg-8-L8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-sanja-grbic`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-sanja-grbic` | Sanja Grbic (product designer, Jetpack design team, Automattic; 5 years at the company, a decade-plus building software) | `AffiliatedWithCompany → co-automattic` |

## Companies (2 new)

| slug | name | type | note |
|---|---|---|---|
| `co-automattic` | Automattic | developer | ~1,400-person fully-distributed, asynchronous company behind WordPress.com, Jetpack, WooCommerce, Tumblr, Beeper and more; decades of work exhaustively documented (which its internal knowledge MCP exploits) |
| `co-figma` | Figma | developer | collaborative interface-design SaaS; appears here as the incumbent design tool demoted from primary working artifact to after-the-fact visual fine-tuning by prototype-first AI workflows |

## Elements (1 new + 1 reused)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-automattic-context-mcp` | Automattic internal knowledge MCP server (rendered "context AC" in captions — ⚠ name garbled) | product | context | Internal MCP server giving AI tools access to Automattic's decades of documented knowledge, decisions, and data; used daily for research and planning by non-engineers — the context layer that grounds org-wide vibe-coding in real institutional knowledge |

Reused: `el-claude-code` **[registry]** — the coding agent used throughout (the training-exercise app used "only Claude Code"; shared project folders; solo prototype builds).

Element edges: `el-automattic-context-mcp` `IdentifiedInArtifact → ia-aie-grbic-500-vibe-coders`, `DevelopedByCompany → co-automattic`; `el-claude-code` `IdentifiedInArtifact → ia-aie-grbic-500-vibe-coders` (reuse edge only).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-grbic-500-vibe-coders`, `SourcedFromSource → source-aie-yt` **[registry]**. Domain left unset (org-level observations; the enum has no org fit).

| slug | name / brief | FormsPattern | RelevantCompany |
|---|---|---|---|
| `sig-automattic-radical-speed-month` | Automattic ran "Radical Speed Month": a third of the company (~500 people) paused roadmap work for 30 days, paired into two-person teams with full autonomy, and started ~794 ship-something-real projects; AI use encouraged but not required. Preceded by permanent enablement machinery: a role-specific two-week immersive AI course for every employee, ops-hardened security/processes, and dev-env docs good enough for non-engineers | — (pat-ai-native-org candidate evidence — see notes) | `RelevantCompany → co-automattic` |
| `sig-designer-to-design-engineer` | A product designer who had never shipped work code built a design-system status tracker solo as a full proof of concept in ~2.5 weeks — live component previews, ingesting GitHub/Storybook/Figma links, sorted/tagged/searchable — after an engineer questioned whether it was even buildable; then deployed it as an internal tool plus a curated public-facing site. "I moved from a designer to a design engineer" — pushing code to production in a large established system | `FormsPattern → pat-value-of-judgement` **[registry]** | `RelevantCompany → co-automattic` |
| `sig-figma-demoted-to-fine-tuning` | A years-stable design process inverted in 30 days: instead of working in Figma to high fidelity and handing off, designers now plan, build the working prototype directly (Claude Code), and return to Figma only afterward for mood boards and UI fine-tuning — the live project, not the mock, is the main working artifact | `FormsPattern → pat-saaspocalypse` **[registry]** | `RelevantCompany → co-figma` |
| `sig-engineers-become-enablers` | In mixed-ability AI teams the engineer's highest-leverage move shifted from writing code to enabling others — repo setup, teaching Git, making basic commands legible: "if you're an engineer, the impact you have when you enable others may be far greater than the impact of doing more engineering yourself"; with AI everyone can work a little outside their domain, so engineers become enablers and teachers | `FormsPattern → pat-value-of-judgement` | `RelevantCompany → co-automattic` |
| `sig-designers-ship-ios-chat-6-days` | Two designers went zero-to-working iOS chat proof of concept for WooCommerce merchants in 6 days — wordpress.com auth, Jetpack connection, a widget inheriting site theming, and a site-scanning AI answer agent that discerns when it can't answer — using a shared Claude Code project folder (all chats/ideas recorded to the file system) as the collaboration substrate; alignment was easy because both think user-first | — (pat-ai-native-org candidate evidence — see notes) | `RelevantCompany → co-automattic` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-enablement-is-the-bottleneck` | Org-wide AI velocity was unlocked less by the models than by enablement machinery: per-role immersive training, security/processes/docs a non-engineer can follow, an internal knowledge MCP over decades of documentation, and engineers repositioned as teachers. The constraint on AI speed in a large org is human process change, not tool capability | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-automattic-context-mcp` |
| `ins-agency-unlocks-ai-speed` | The speed came from collapsing negotiation and handover: one person (or a pair) owning discovery→design→build→deploy end-to-end inside pre-built guardrails. In large organizations that agency — not the tooling — is the scarce resource; changing process means shifting the human behavior behind it: access, champions, experimentation space, permission to break habits | `HighlightsPattern → pat-value-of-judgement` **[registry]** | — |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-grbic-500-vibe-coders`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-org-wide-vibe-coding-rollout` | Roll out org-wide AI building in a large company | Provide tool access plus role-specific immersive training (Automattic: two-week course per employee, lectures + hands-on); invest in security, processes, and dev-env documentation that non-engineers can follow; expose institutional knowledge to AI tools (internal MCP over documentation); run a bounded experiment window with roadmap paused (30 days, two-person teams, full autonomy, "ship something real", staged thirds of the company); find enablers and champions; grant agency so people break out of habitual processes — start at team level if you can't do it company-wide | `ReferencesElement → el-automattic-context-mcp` |
| `how-shared-agent-project-folder` | Use a shared coding-agent project folder as the collaboration record | Start explorations as a Claude Code project folder where all chats and ideas are recorded into the file system; the folder becomes the alignment artifact between collaborators, speeds ideation-to-build handoff dramatically, and carries into daily work as a standing practice | `ReferencesElement → el-claude-code` **[registry]** |

## Dropped

- Nano Banana (image generation for the 16-bit office illustration) — single passing mention; prose only.
- The board-game session manager (2-hour training-exercise app) — folded into `sig-engineers-become-enablers` context; no node.
- The AI-enablement course as an Element — kept as a KnowHow guideline instead.
- WordPress.com / Jetpack / WooCommerce / Tumblr / Beeper as separate companies — folded into the `co-automattic` brief.
- Adobe / Sketch — design-tool history scene-setting.

## Review notes

1. **pat-ai-native-org candidate evidence (NOT coined, no edges, per instruction):** this talk is a strong single-org data point — a company-wide 30-day vibe-coding month (~500 people, ~794 projects), role boundaries dissolving (designer→design engineer), engineers repositioned as enablers, and permanent org machinery (per-role AI training for every employee, knowledge MCP, non-engineer dev environments). Adds to the Tan / Wu+Shihipar / Brunet / Doshi / Lee-Chan / An+Hoe / Noring / Browne evidence already logged in the registry. Signals 1 and 5 left deliberately pattern-less rather than force-fit to an existing pattern.
2. "context AC" — the internal MCP server's name is garbled in captions; `el-automattic-context-mcp` coined with a descriptive placeholder name — resolve the real product name before seeding.
3. "~794 projects" from ~500 people in 30 days is as-captioned; plausible (participants ran multiple projects — the speaker did three) but verify. "Radical Speed Month" also appears garbled once as "Radico Speedman".
4. `sig-figma-demoted-to-fine-tuning` → `pat-saaspocalypse` is a judgment call: read as incumbent-design-SaaS displacement (the tool demoted from center of workflow to accessory). Re-home or drop if too aggressive; `co-figma` was coined mainly to make this signal queryable.
5. Speaker's surname never appears in captions (only "Sanja"); "Grbic" from the official listing.
6. The tracker and iOS chat are proofs of concept (internal / curated-public), not shipped products — briefs phrased accordingly.
