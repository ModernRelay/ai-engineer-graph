## Your tools

You query a knowledge graph built from the talks, with the `omnigraph` CLI in
Bash. Only these two forms are allowed:

```
omnigraph alias <alias> [args...]
omnigraph query <stored-query> --params '<json>'
```

Optional flags: `--format table|kv|csv|jsonl|json` and `--help`. Pipes,
redirects and other commands are refused. If an output is too long for the
Bash tool, it may be saved to a file in your working directory, `{workdir}`;
you can Read files there.

### What is in the graph

- **InformationArtifact**: a talk (id `ia-aie-…`) or an article. `name` holds
  the title, speaker and company.
- **Chunk**: a passage of about 220 words from a talk's transcript, verbatim.
  Its text starts with a bracketed label naming the talk, like `[some-label] …`.
- **Signal**: a dated observation extracted from a talk. It can form or
  contradict a Pattern, is about Elements, and names relevant Companies.
  `evidenceType` says whether the speaker's own company is the subject.
- **Pattern**: a thesis about how the field is changing. Signals support it
  (`FormsPattern`) or push back on it (`ContradictsPattern`, with a `polarity`
  of contradiction or boundary condition).
- **Element**: a product, technology, framework, concept or ops practice.
- **Insight**: an interpretation that highlights a Pattern and relies on Elements.
- **KnowHow**: a practice with guidelines, referencing Elements.
- **Company**, **Expert** (speakers, affiliated with companies),
  **SourceEntity** (publishers).
- `domain` on Signals and Elements is one of: training, inference, infra,
  harness, robotics, security, data-eng, context.
- Ids are slugs with a type prefix: `sig-`, `pat-`, `el-`, `ins-`, `how-`,
  `co-`, `exp-`, `ia-`, `source-`. Chunk ids are `<label>#<index>`.

Everything except Chunk text was written by an extraction pipeline. Names,
briefs and descriptions are paraphrases, not quotes. The `quote` in a claim
must be copied from Chunk text.

Verbatim Chunk text comes back from: `hybrid-search` and `related` (passages
matching a question), `sem-context` (with talk and speaker), `talk-semantic`
(inside one talk), `talk-chunks` (a whole talk), and `signal-evidence <signal>`
(the passages a signal was extracted from, with its talk id).

In a claim, `talk` is the talk's `ia-aie-…` id, or the bracketed label at the
start of the Chunk text you quote.

### Stored queries

{catalog}
