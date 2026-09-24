# Agent + Omnigraph vs Agent + Markdown files

10 questions × 2 arms × 3 runs (60 agent runs).

## Headline

| Metric | Agent + Omnigraph | Agent + Markdown files |
|---|---|---|
| Answer quality: pairwise wins / ties / losses (30 pairings) | 8 / 6 / 16 | 16 / 6 / 8 |
| Recall, open list questions (Q04, Q06, Q07): mean | 44.1% | 41.3% |
| Run-to-run consistency, list questions: mean item Jaccard | 0.65 | 0.64 |
| Claims per answer: mean (total) | 10.8 (324) | 12.9 (386) |
| Grounded claims (verbatim quote, supported) | 271 (83.6%) | 316 (81.9%) |
| Partially supported claims | 40 (12.3%) | 67 (17.4%) |
| Hallucinated claims (quote not found, wrong talk, or unsupported) | 13 (4%) | 3 (0.8%) |
| Uncited factual statements per answer: mean | 5.6 | 6.8 |
| Absence question (Q10) answered correctly | 3 / 3 | 3 / 3 |
| Time per question: median / p90 | 156 s / 374 s | 124 s / 226 s |
| Cost per question: mean (total) | $0.58 ($17.26) | $0.43 ($12.99) |
| Tokens per question: input incl. cache / output | 1.11M / 14.6k | 546.1k / 12.2k |
| Turns / tool calls per question: mean | 64 / 63 | 33 / 32 |
| Capped or failed runs | 0 | 0 |

## Per question

Each cell is omnigraph / markdown. Pairwise is omnigraph wins – markdown wins – ties.
Fixed-length lists show how much the two arms agree instead of recall.

| Question | Shape | Pairwise | Recall / agreement | Grounded | Hallucinated | Median time | Mean cost |
|---|---|---|---|---|---|---|---|
| Q01 | ranked_list | 0–2–1 | agree 10% | 80% / 84.7% | 3.3% / 0% | 378 s / 191 s | $1.19 / $0.76 |
| Q02 | ranked_list | 0–3–0 | agree 66.7% | 78.8% / 81.1% | 6.1% / 0% | 173 s / 126 s | $0.41 / $0.40 |
| Q03 | ranked_list | 2–1–0 | agree 0% | 86.5% / 69.4% | 2.7% / 0% | 139 s / 171 s | $0.44 / $0.65 |
| Q04 | talk_set | 1–2–0 | 33.3% / 36.2% | 91.4% / 83.3% | 0% / 0% | 214 s / 189 s | $0.82 / $0.70 |
| Q05 | ranked_list | 0–2–1 | agree 80% | 89.7% / 87.3% | 6.9% / 2.5% | 283 s / 226 s | $0.71 / $0.71 |
| Q06 | company_set | 1–2–0 | 46.2% / 48.7% | 78.9% / 80.4% | 0% / 0% | 123 s / 79 s | $0.33 / $0.24 |
| Q07 | ranked_list | 0–2–1 | 52.8% / 38.9% | 80.6% / 73.8% | 5.6% / 2.4% | 374 s / 174 s | $1.20 / $0.57 |
| Q08 | prose | 1–2–0 | – | 79.5% / 81% | 10.3% / 0% | 126 s / 73 s | $0.41 / $0.22 |
| Q09 | prose | 2–0–1 | – | 100% / 100% | 0% / 0% | 35 s / 26 s | $0.10 / $0.05 |
| Q10 | absence | 1–0–2 | – | – / – | – / – | 41 s / 8 s | $0.15 / $0.02 |

Graph `01M37ZANGF3QTZH8WDE3J9ZEN9`, corpus `63c73703991e`.
