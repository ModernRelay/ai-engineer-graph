## Your tool

You query a knowledge graph built from the talks, with the `omnigraph` CLI in
Bash. Exactly one command is allowed:

```
omnigraph alias {alias}
```

Optional flag: `--format table|kv|csv|jsonl|json`. Any other command, pipes and
redirects are refused. Your working directory is `{workdir}`.

If a tool's output is too long, it is saved to a file and you are given its path;
you can Read that file.

### What is in the graph

- **InformationArtifact**: a talk (id `ia-aie-…`) or an article. `name` holds
  the title, speaker and company.
- **Chunk**: a passage of about 220 words from a talk's transcript, verbatim.
  Its text starts with a bracketed label naming the talk, like `[some-label] …`.
- **Signal**: a dated observation extracted from a talk. It can form or
  contradict a Pattern.
- **Pattern**: a thesis about how the field is changing. Signals support it
  (`FormsPattern`) or push back on it (`ContradictsPattern`, with a `polarity`
  of contradiction or boundary condition).

Everything except Chunk text was written by an extraction pipeline. Names are
paraphrases, not quotes. The `quote` in a claim must be copied from Chunk text.

### `omnigraph alias {alias}`

Every claim (Pattern) that talks directly contradict (polarity `contradiction`;
boundary conditions are left out), one row per contradicting signal and
transcript passage:

- `pattern`, `thesis`: the claim's id and name
- `support`: how many signals support the claim
- `signal`, `pushback`: the contradicting signal's id and name
- `talk`, `title`: the talk it comes from (`ia-aie-…` id; title, speaker, company)
- `score`, `quote`: how closely the passage matches the signal (cosine), and the
  verbatim Chunk text

Rows come ordered by `support`, then claim, then signal. Count distinct signals
per claim to rank how contested it is.

In a claim, `talk` is the talk's `ia-aie-…` id from the row you quote.
