# Extraction → seed JSONL conversion spec

You convert SPIKE extraction markdown files into Omnigraph load JSONL. Follow
this spec EXACTLY — output from all agents is merged and validated centrally.

## Output

One JSONL file at the path you were given. One JSON object per line:

- Node: `{"type":"<Type>","data":{"id":"<slug>","slug":"<slug>", ...fields}}`
  (`id` mirrors `slug` — matches the existing seed.jsonl convention)
- Edge: `{"edge":"<EdgeName>","from":"<src-slug>","to":"<dst-slug>","data":{}}`

## Ground truth

Read `/Users/andrew/code/intel-graph/schema.pg` FIRST. Only its node types,
fields, enums, and edge types exist. The registry
(`extraction/registry.md`) tells you which entities are [seed]/[registry]
reuses (do NOT re-emit them — edges may point at them).

## What to emit per file

- Every entity DEFINED in the file (its definition tables/rows): Signals,
  Insights, KnowHows, Elements, Companies, Experts, InformationArtifacts —
  and Patterns only where the file explicitly defines one.
- Every edge the file states, INCLUDING edges to registry/seed entities.
- NOTHING for entities the file merely references (marked [registry]/[seed]
  or "defined in <other file>").

## Field mapping

Timestamps: DateTime ISO `"YYYY-MM-DDT00:00:00Z"`. Use the file's stated
stagingTimestamp/publish date for `stagingTimestamp`, `createdAt`,
`updatedAt` of everything the file defines.

- **Signal** (required: slug,name,brief,stagingTimestamp,createdAt,updatedAt):
  `name` = a short label distilled from the row (≤90 chars, declarative);
  `brief` = the row's full brief text (or its first ~2 sentences if huge, with
  the rest going to `description`); `domain` from `(domain: x)` annotations or
  the section's "All: domain `x`" line — must be one of
  training|inference|infra|harness|robotics|security|data-eng|context, else omit.
- **Element** (required: slug,name,kind,createdAt,updatedAt): `kind` must be
  product|technology|framework|concept|ops. Extraction files state kind —
  coerce obvious synonyms (tool→technology, library→framework, method→concept,
  metric→concept, doc/process→ops). `brief` = the row's brief; `domain` if
  stated and valid; `website` only if a URL/domain-name appears verbatim in
  the row; do not invent other optional fields.
- **Pattern** (required: slug,name,kind): kind challenge|disruption|dynamic as
  stated. NOTE: `pat-html-native-medium` and `pat-provider-blind-ai` were
  retired at review — they are NOT nodes; do not emit them and do not emit
  edges to them (files were already rehomed; if you still find such an edge,
  skip it and note it).
- **Insight** (required: slug,name): `name` = short label (≤90 chars);
  `brief`/`description` from the row text; `importance` only if stated.
- **KnowHow** (required: slug,name,stagingTimestamp): `guidelines` =
  [String] — split the guidelines cell on `;` into trimmed items;
  `context`/`url` only if present.
- **Company** (required: slug,name): `brief` from the row; `type` must be
  bigtech|developer|investor|research|hardware|media — coerce
  (fintech/consultancy/startup/enterprise→developer, university/lab→research,
  VC/accelerator→investor, advertising/publisher/education-content→media),
  omit if unclear. Note every coercion in your manifest.
- **SourceEntity** (required: slug,name): only if the file DEFINES one (e.g.
  batch-1 file defines `source-aie-yt`: type video_channel, platform YouTube,
  url https://www.youtube.com/@aiDotEngineer).
- **Expert** (required: slug,name): schema has ONLY slug+name — affiliation
  goes into an AffiliatedWithCompany edge, titles/roles are dropped.
- **InformationArtifact** (required: slug,name,artifactType,stagingTimestamp):
  artifactType `youtube`; `link` = the youtu.be URL (must be unique).

## Edges — the complete legal set (direction matters)

FormsPattern Signal→Pattern · ContradictsPattern Signal→Pattern ·
HighlightsPattern Insight→Pattern · ReliesOnElement Insight→Element ·
ReliesOnPattern Pattern→Pattern · DrivesPattern Pattern→Pattern ·
ContradictsToPattern Pattern→Pattern · OnElement Signal→Element ·
EnablesElement Element→Element · UsesElement Element→Element ·
ExemplifiesPattern Element→Pattern · EnablesPattern Element→Pattern ·
PublishedBySource InformationArtifact→SourceEntity ·
ContributedByExpert InformationArtifact→Expert ·
SpottedInArtifact Signal→InformationArtifact ·
IdentifiedInArtifact Element→InformationArtifact ·
SourcedFromArtifact KnowHow→InformationArtifact ·
SourcedFromSource Signal→SourceEntity ·
RelevantCompany Signal→Company · DevelopedByCompany Element→Company ·
AffiliatedWithCompany Expert→Company · ReferencesElement KnowHow→Element

Rules:
- A cell listing multiple targets (`FormsPattern → pat-a, pat-b` or
  `pat-a; pat-b`) → one edge line per target.
- Section-level blanket lines ("All: SpottedInArtifact → ia-x,
  SourcedFromSource → source-aie-yt") apply to every row of that section —
  emit them per row.
- An edge name not in the list above, or with mismatched endpoint types:
  SKIP and record in your manifest (e.g. Insight→Artifact links do not exist
  in the schema — drop them).
- If a file states an edge in reversed direction, emit it in the schema
  direction.
- Deduplicate identical edge lines within your own output.

## Manifest (your final message — machine-parsed)

```
FRAGMENT|<path>
COUNTS|Signal=<n>|Element=<n>|Pattern=<n>|Insight=<n>|KnowHow=<n>|Company=<n>|Expert=<n>|SourceEntity=<n>|InformationArtifact=<n>|edges=<n>
COERCED|<slug>: <original> -> <coerced>   (one line each; NONE if none)
SKIPPED|<file>: <what and why>            (one line each; NONE if none)
```
