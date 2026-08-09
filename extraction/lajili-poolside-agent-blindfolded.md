# SPIKE extraction — "Your agent is blindfolded" (Johan Lajili, Poolside AI) — FOR REVIEW

Source transcript: `transcripts/lajili-poolside-agent-blindfolded.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/iRcX54EO5g8 — AI Engineer World's Fair, published 2026-07-08.
`stagingTimestamp` for the artifact and all signals: 2026-07-08 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-lajili-agent-blindfolded` | Your agent is blindfolded (Johan Lajili, Poolside AI — AI Engineer World's Fair) | youtube | https://youtu.be/iRcX54EO5g8 |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-johan-lajili`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-johan-lajili` | Johan Lajili (engineer at Poolside AI; built the internal Spoolside agent-testing CLI; coined "AIX engineers") | `AffiliatedWithCompany → co-poolside` |

## Companies (1 new)

| slug | name | type | note |
|---|---|---|---|
| `co-poolside` | Poolside AI | developer | One of the handful of companies training their own foundation models from scratch plus coding agents; "research" also defensible — flip if preferred |

## Elements (1 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-aix-engineering` | AIX engineering (AI experience engineering) | concept | harness | Proposed successor role to product engineering: engineers spend less time on the product and more on making the AI able to work on the product — perception tools (screenshots, token-compressed UI snapshots, log extraction), codebase legibility, knowledge bases; deliverable as CLI, skill, or MCP. Rule of thumb: "put the mask on the AI before your own" — make the AI self-served before feature work; the up-front slowdown pays off once agents are multiplied or run overnight |

Element edges: `el-aix-engineering` `IdentifiedInArtifact → ia-aie-lajili-agent-blindfolded`; `ExemplifiesPattern → pat-harness-over-model` **[registry]**.

## Signals (3 new)

All: domain `harness`, `SpottedInArtifact → ia-aie-lajili-agent-blindfolded`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | name / brief | FormsPattern | other edges |
|---|---|---|---|
| `sig-bimodal-ai-discourse-feedback-loop` | Mid-2026 discourse on coding AI is bimodal ("never touching code again" vs "produces absolute garbage in my production app"); a Poolside engineer rejects the usual greenfield/brownfield explanation (legacy successes exist, including his own) — the real differentiator is whether a feedback loop exists; greenfield just means the agent's intuition happens to be right by default, while brownfield has dragons it can't see | `FormsPattern → pat-verification-gap` | — |
| `sig-spoolside-agent-eyes` | Poolside built Spoolside, an internal CLI (deliberately unreleased) so its agents can test a non-web product (a VS Code extension): screenshots, token-compressed UI-state snapshots, backend/frontend log extraction, service restarts, stackable high-level UI commands (open menu, message the in-product agent, await reply, upload image); house policy: the agent must reproduce a bug before its fix is trusted; framed as the precondition for running agents overnight or multiplying them | `FormsPattern → pat-harness-over-model` | `RelevantCompany → co-poolside`; `OnElement → el-aix-engineering` |
| `sig-aix-engineer-role-shift` | Declared role shift, dated by the speaker: 2025 had "product engineers"; now engineers should "focus less on the product and more on making the AI work on the product" — tools, codebase improvements, knowledge bases — becoming "AIX engineers", with per-product judgment (ASCII view of a Unity 3D world? easy agent logins for permissioned apps?) as the new core skill | `FormsPattern → pat-value-of-judgement` | `OnElement → el-aix-engineering`; `RelevantCompany → co-poolside` |

## Insights (2 new)

| slug | name | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-done-claims-are-hypotheses` | An agent's "I've implemented the new auth flow and it's all working perfectly" decodes to "to the best of my capabilities and of what you gave me, that sounds like it should work" — maybe it verified, maybe not; whether a user iterates on that gap or quits at the first false "done" is exactly the cleavage between AI maximalists and skeptics | `HighlightsPattern → pat-verification-gap` | — |
| `ins-blindfold-not-brain` | In brownfield code the binding constraint isn't the agent's intelligence but its perception — dead code and cross-module surprises it has never looked at; give it eyes (logs, screenshots, UI state, service control) and its intuition converts into verified, trustable work | `HighlightsPattern → pat-harness-over-model` | `ReliesOnElement → el-aix-engineering` |

## KnowHow (2 new)

All `SourcedFromArtifact → ia-aie-lajili-agent-blindfolded`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-agent-perception-harness` | Give your agent eyes before you give it features | Build agent-facing access to your app: screenshots; token-compressed snapshots of UI state; log extraction across backend/frontend services; restart commands; high-level stackable UI actions; require bug reproduction before accepting any fix ("until it reproduces the bug, I don't trust you"); ship it however is simplest — CLI here, skill or MCP equally valid; expect it to be product-specific and to differ person to person, problem to problem | `ReferencesElement → el-aix-engineering` |
| `how-agent-self-realization-loop` | Make the AI notice problems by itself | When you visually spot an issue the agent missed, don't just tell it — step back and build the capability for the agent to detect it itself; run retro loops over agent logs ("did you notice any issues, any stink?" — `sleep(15)` scattered everywhere is a stink; so is re-running storybooks constantly); prefer ephemeral, human-like test flows over rigid automated tests (speaker's stated preference) | `ReferencesElement → el-aix-engineering` |

## Dropped

- Spoolside as an Element — intentionally not coined: internal, unreleased ("not something you're going to find on GitHub"), and the talk's explicit point is "build your own"; captured in `sig-spoolside-agent-eyes`. Flip to `el-spoolside` if internal tools deserve product nodes.
- "G stack" — garbled reference to an existing tool with screenshots + token-compressed page snapshots (Playwright-MCP-like); unresolved, prose only (see note 2).
- CLI/skill/MCP delivery options — passing mention; `el-agent-skills`/`el-mcp` **[registry]** not edge-linked.
- The airline oxygen-mask metaphor — folded into the `el-aix-engineering` brief.

## Review notes

1. Speaker name: captions say "Joan from Poolside"; official listing is Johan Lajili — official used.
2. "G stack" is an unresolved caption garble (a known tool providing screenshots and token-compressed web-page snapshots); verify against the video before attributing.
3. `sig-aix-engineer-role-shift` sits between `pat-value-of-judgement` (role/career claim — chosen) and `pat-harness-over-model` (the work itself is harness-building); the element edge carries the harness link, so both readings are represented without double-counting.
4. No new pattern coined; "engineers become AI-enablers" is covered by the existing pair above. If "AIX engineering" recurs as a named role in later batches, consider promoting the framing.
5. `co-poolside` type set to `developer` although they train their own foundation models — `research` is defensible; reviewer's call.
