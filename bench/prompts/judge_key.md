You map an answer about conference talks onto an answer key.

You get the question, the key's claims (numbered, each with a short description), the
answer's prose, its numbered list entries, and its numbered cited claims. Each cited claim
belongs to a list entry (in brackets) and names the talk it quotes.

For every list entry, give the number of the key claim it is about, or 0 if it is about
none of them.

- An entry matches a key claim when it names the same claim, in other words or at another
  level of detail: "the harness matters more than the model" matches "The Harness Over the
  Model"; "is the model still the bottleneck?" matches "The Model Is Not the Bottleneck".
- An entry framed as a debate between two positions matches a key claim when one of the
  two positions is that claim.
- An entry about a different claim is 0, even when the topic is related.
- Two entries may match the same key claim.

For every cited claim, give the side its talk takes on the entry's claim, as the answer
presents it:

- "for": the talk argues for the claim, or supports it with evidence.
- "against": the talk contradicts the claim, pushes back on it, or limits where it holds.
- "neither": the talk is cited for context, or the answer doesn't say which side it is on.

For an entry framed as a debate between two positions, "for" and "against" are relative to
the position that matches the key claim; if the entry matches no key claim, use the first
position it names.
