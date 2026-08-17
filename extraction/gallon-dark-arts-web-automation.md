# SPIKE extraction — "The Dark Arts of Web Automation" (Corey Gallon) — FOR REVIEW

Source transcript: `transcripts/gallon-dark-arts-web-automation.txt` (auto-captions — quotes are paraphrases, not verbatim).
Video: https://youtu.be/26RtyAm9y_Q — AI Engineer World's Fair, **Computer Use (CUA) track**, published 2026-08-14.
`stagingTimestamp` for the artifact and all dated nodes: 2026-08-14 (publish date).
Entities marked **[registry]** are already in the registry — edges link to them, no new node.
Shape of the talk: the track's how-to talk — a live demonstration of agents defeating four production CAPTCHAs (Cloudflare Turnstile, MTCaptcha, GeeTest-style jigsaw, reCAPTCHA v2) with no human in the loop, framed as one methodology: **give the agent a CLI driving Chrome via CDP, run a sense-act-verify loop, climb the "meatbag ladder" only as high as the page forces, then write the solution down.** Opens with the speaker's OpenAI account nearly banned for the prep work. Caption garbles: "meat bag" → **meatbag** (deliberate coinage, kept), "Arise AI" → **Arize AI**, "MT capture" → **MTCaptcha**, "by Lemon" → likely **GeeTest** (jigsaw CAPTCHA — see review note 3), "moves like Jagger" → deliberate pun (kept), "Demazon/damazon" → anonymized "Demazon" (kept), "Chrome Agent" → the speaker's tool (kept).

---

## InformationArtifact (1 new)

| slug | name | artifactType | link |
|---|---|---|---|
| `ia-aie-gallon-dark-arts-web-automation` | The Dark Arts of Web Automation (Corey Gallon — AI Engineer World's Fair) | youtube | https://youtu.be/26RtyAm9y_Q |

Edges: `PublishedBySource → source-aie-yt` **[registry]**; `ContributedByExpert → exp-corey-gallon`.

## Experts (1 new)

| slug | name | edges |
|---|---|---|
| `exp-corey-gallon` | Corey Gallon (author of **Chrome Agent**, a CDP-driving CLI tool in the Python ecosystem — "I use it all day, every day"; OpenAI threatened then rescinded a ban over the talk's prep) | — (no company stated; independent) |

Referenced without coining: Arize AI (the CLI-vs-MCP capability study), OpenAI (the ban threat, Codex), Anthropic (the 75×-cheaper CLI token figure).

## Companies (0 new)

Reused **[registry]**, edge-only: `co-openai` **[b2]** (ban threat and reinstatement; Codex access), `co-cloudflare` **[b16]** (Turnstile, the hardest of the four), `co-anthropic` **[seed]** (the CLI token-cost figure). Not coined: Arize AI (study source, no facts beyond it), Google (the reCAPTCHA/trusted-event references).

## Elements (5 new)

| slug | name | kind | domain | brief |
|---|---|---|---|---|
| `el-cdp-cli-driving` | Driving Chrome via CDP from a CLI | technology | harness | The premise on one slide: "a CDP browser is just like a meatbag with a mouse — as far as Google and Cloudflare can tell." An agent driving Chrome through the **Chrome DevTools Protocol** (the F12 panel's own protocol) sends clicks and keystrokes down the exact same internal path a human's do. Delivered as a CLI, not an MCP server, on three grounds from an Arize AI study: capability is a wash (~83% task success either way), but the CLI wins on **reuse** (a sequence is programmed once, run 1,000× with no model in the loop; MCP hits the model every turn), **speed** (7 turns / <1 min vs MCP's 71 round trips / 8 min for the same task), and **cost** (Anthropic-reported up to 75× cheaper in tokens). CDP is large — 57 domains, hundreds of methods — but only a small subset is needed, grouped as **digital senses** |
| `el-digital-senses` | The digital senses | concept | harness | The CDP subset that mirrors human perception and action: **see** the page (DOM structure, accessibility-tree semantics, or a screenshot for pixels), **hear** it (network traffic, console, logs), and **operate** it (clicks, keystrokes, navigation). The framing that reduces CDP's 57 domains to the handful an agent actually needs to act like a human |
| `el-sense-act-verify-loop` | Sense–act–verify loop | concept | harness | The control loop: perceive through one channel, take exactly one action, then **verify through a different channel** — "if you've clicked something, don't ask the click if it was successful; check the network or check the screen." Repeat until the page gives in; when it won't close despite sense-act-verify, that is the page fighting back, and the signal to climb the ladder |
| `el-meatbag-ladder` | The meatbag ladder | concept | harness | Three rungs of increasing human-likeness, climbed only as high as the page forces (lowest working rung wins). **Rung 1** — don't act human at all: use an exposed in-page API or a synthetic JavaScript click ("easy, free, instant, the right default"). **Rung 2** — a real click via CDP's input domain when synthetic clicks are silently dropped, because Chrome stamps every event **trusted/untrusted** and pages quietly discard untrusted input. **Rung 3** — genuine human input and behavior: real mouse paths with dwell and jitter, deliberate overshoot-and-ease-back, and vision, for pages actively hunting bots. Then **write down the path that worked** as code and/or an agent skill |
| `el-solver-operator-split` | Solver / operator split | technology | harness | The architecture that beats a timed CAPTCHA (reCAPTCHA v2): a **solver** in pure deterministic code (trusted checkbox click, iframe piercing, per-round grid screenshot, self-re-arming on expiry — "fast and free") that taps the **operator** — a vision model — for the single step code can't do: looking at the fuzzy grid and picking the tiles. "Code does the deterministic driving; the agent does the only bits that require eyes and a brain." The point is speed: a model round-tripped on every click burns the round clock and loses — "deterministic code at machine speed with one quick AI look per round" |

Element edges: all five `IdentifiedInArtifact → ia-aie-gallon-dark-arts-web-automation`.
`el-cdp-cli-driving` `UsesElement → el-digital-senses`;
`el-sense-act-verify-loop` `UsesElement → el-digital-senses`;
`el-meatbag-ladder` `UsesElement → el-sense-act-verify-loop`;
`el-solver-operator-split` `UsesElement → el-meatbag-ladder`, `el-cdp-cli-driving`;
`el-solver-operator-split` `ExemplifiesPattern → pat-harness-over-model` **[registry]**;
`el-cdp-cli-driving` `EnablesPattern → pat-new-cyber-threats` **[registry]**.

Reused elements (no new nodes): `el-code-mode` **[b6]** — the CLI-over-MCP argument is a direct instance (program once, run without a model in the loop); edge via signals. `el-agent-skills` **[batch1]** (writing the worked path down as a skill).

## Signals (5 new)

All: `SpottedInArtifact → ia-aie-gallon-dark-arts-web-automation`, `SourcedFromSource → source-aie-yt` **[registry]**.

| slug | domain | name / brief | FormsPattern | other edges |
|---|---|---|---|---|
| `sig-agents-defeat-production-captchas` | security | A live demonstration of AI agents solving four production CAPTCHAs with **no human in the loop** — Cloudflare Turnstile (checkbox hidden behind a closed shadow root inside a cross-origin iframe inside another shadow root; beaten by computing the on-screen position and firing a trusted click at the glass), MTCaptcha (screenshot + vision to read characters, trusted keystrokes into the iframe), a GeeTest-style jigsaw (human-like drag with jitter, curve, and deliberate overshoot), and reCAPTCHA v2 (the solver/operator split). "Three gates built to keep agents out, and we beat each one." The strongest single demonstration in the corpus that the bot/human boundary has collapsed at the input layer | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-solver-operator-split`, `el-meatbag-ladder` |
| `sig-trusted-event-boundary-defeated` | security | The mechanism that makes it work: Chrome stamps every input event **trusted** (from the real input path) or **untrusted** (synthetic JS), and pages defend by dropping untrusted events — but a CDP input-domain click travels the identical internal path as a human mouse and is stamped trusted, indistinguishable to the page. "A CDP browser is just like a meatbag with a mouse, as far as Google and Cloudflare can tell." The primary anti-automation signal is shown to be bypassable by construction, not by evasion | `FormsPattern → pat-new-cyber-threats` **[registry]** | `OnElement → el-cdp-cli-driving`, `el-digital-senses` |
| `sig-cli-beats-mcp-for-browser-control` | harness | The tooling argument with numbers: an Arize AI study finds CLI and MCP roughly tied on capability (~83% success) but the CLI winning decisively on reuse, speed (7 turns/<1min vs 71 round-trips/8min), and cost (Anthropic: up to 75× cheaper in tokens), because a CLI sequence is programmed once and replayed without a model in the loop while MCP invokes the model every turn. A concrete data point in the corpus's CLI-vs-MCP / code-mode thread, from the browser-control domain | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-cdp-cli-driving`, `el-code-mode` **[registry, b6]** |
| `sig-climb-only-as-high-as-forced` | harness | The methodology as a reliability principle: sense–act–verify (verifying through a *different* channel than the action), and climb the human-likeness ladder only to the lowest rung that works — synthetic click, then trusted CDP click, then real mouse paths with jitter and vision — then persist the working path as code or a skill. "You figure it out once and you do it forever." A disciplined-engineering account of durable web automation, explicitly not a model-capability story | `FormsPattern → pat-harness-over-model` **[registry]** | `OnElement → el-meatbag-ladder`, `el-sense-act-verify-loop` |
| `sig-web-ui-as-permissionless-api` | infra | A sharp reframing from the Outlook demo: driving the web UI *is* the API when the real API is gated — an Office 365 tenant's API needs an app registration and admin approval an employee can't get, "whereas the web login you have is all you need." The web UI becomes "a universal API, a permissionless API." Convergent with Batra's long-tail argument and directly relevant to the enterprise-access thread: agents route around API governance by using the human interface | `FormsPattern → pat-agent-economy` (coined 2026-08-16) | `OnElement → el-cdp-cli-driving` |

## Insights (2 new)

| slug | name / brief | HighlightsPattern | ReliesOnElement |
|---|---|---|---|
| `ins-captcha-is-over-as-a-boundary` | The four solves together retire the CAPTCHA as a human/bot boundary: the checkbox class falls to trusted-click-at-computed-position, the OCR class to vision, the behavioral-drag class to human-like motion synthesis, and the timed-grid class to a code-plus-one-vision-look architecture. What defeats each is not a novel exploit but the CDP trusted-event path plus a vision model — both now commodity. Any defense that assumes "a bot cannot do this in the browser" is already false, which relocates bot defense to identity and attestation (the exact gap Klein names in the same track) | `HighlightsPattern → pat-new-cyber-threats` **[registry]** | `ReliesOnElement → el-solver-operator-split`, `el-cdp-cli-driving` |
| `ins-determinism-with-a-vision-oracle` | The reCAPTCHA architecture is the transferable lesson beyond CAPTCHAs: keep the loop deterministic and fast, and call the model only for the irreducible perception step, because anything that round-trips a model per action loses on latency and cost. It is the same detection-deterministic / investigation-agentic division the observability talks reached (Hylak, b19), arrived at independently under a hard time constraint — and it generalizes to any high-frequency browser task where a model-in-every-step harness is too slow and too expensive | `HighlightsPattern → pat-model-not-bottleneck` **[registry]** | `ReliesOnElement → el-solver-operator-split`, `el-sense-act-verify-loop` |

## KnowHow (1 new)

All: `SourcedFromArtifact → ia-aie-gallon-dark-arts-web-automation`.

| slug | name | guidelines (condensed) | ReferencesElement |
|---|---|---|---|
| `how-drive-a-browser-like-a-human` | Drive a browser like a human, deterministically | Give the agent a **CLI driving Chrome through CDP**, not an MCP server, so sequences are programmed once and replayed without a model in the loop — capability is comparable but reuse, speed and token cost favor the CLI heavily; work through the **digital senses** — read the page via DOM, accessibility tree, or screenshot; sense state via network, console, logs; operate via clicks, keystrokes, navigation — and only learn the small CDP subset you need rather than all 57 domains; run a **sense–act–verify loop**, always verifying through a *different* channel than the one you acted on; **climb the ladder only as high as the page forces** — try an exposed API or synthetic JS click first (free and instant), escalate to a trusted CDP input-domain click when synthetic clicks are silently dropped (Chrome's trusted/untrusted stamp is why), and only reach real mouse paths with jitter, overshoot and vision when a page actively hunts bots; for **timed or high-frequency challenges keep the loop in deterministic code and call a vision model only for the single perception step**, because a model round-tripped per action burns the clock; and once something works, **write the path down** as code and/or an agent skill so you solve it once and reuse it forever; finally, run only against infrastructure and accounts you own | `ReferencesElement → el-cdp-cli-driving`, `el-digital-senses`, `el-meatbag-ladder`, `el-sense-act-verify-loop`, `el-solver-operator-split` |

## Dropped

- **The OpenAI ban-threat framing (open and close)** — narrative device; the fact that prep triggered "cyber abuse" flags is real texture but carries no node.
- **The attorney disclaimer** ("everything runs only on infrastructure I own") — kept as the closing clause of the KnowHow rather than a node.
- **The Outlook email-blast specifics** — the permissionless-API point is in `sig-web-ui-as-permissionless-api`; the batch-of-personalized-emails mechanics are illustration.

## Review notes

1. **⚑ The corpus's strongest single exhibit for `pat-new-cyber-threats` since batch 1.** Four production anti-bot systems defeated live, no human in the loop, on commodity primitives (CDP trusted events + a vision model). Two signals homed directly on the pattern; `ins-captcha-is-over-as-a-boundary` ties it to Klein's "Verisign moment" gap in the same track — bot defense must move from challenge to attestation. `sig-web-ui-as-permissionless-api` is held for the `pat-agent-economy` ledger (agents routing around API governance).
2. **Cross-track convergence worth carrying to review.** The solver/operator split (deterministic code + one vision look) is the *same architecture* as Hylak's "deterministic detection, agentic investigation" (b19) and Batra's "click when you can, vision to verify" — three independent arrivals at model-only-for-the-irreducible-step. Candidate texture for a future pattern; none proposed (mechanism, not thesis).
3. **⚠ Verify before seeding:** "by Lemon" is almost certainly **GeeTest** (the jigsaw-slider CAPTCHA vendor) — reconstructed, medium confidence; the Arize AI study numbers (83% parity, 7-vs-71 turns, 1-vs-8 min); Anthropic's "75× cheaper" CLI figure; the CDP "57 domains" count. `exp-corey-gallon` has **no company edge** — the tool (Chrome Agent) is his but no employer is stated.
4. **`el-cdp-cli-driving` carries a rare `EnablesPattern → pat-new-cyber-threats`** (an element enabling a threat pattern) — appropriate here since the capability *is* the threat surface. Flagged because element→threat-pattern edges are uncommon in the corpus.
