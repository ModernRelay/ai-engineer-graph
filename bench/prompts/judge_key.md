You map an answer about conference talks onto an answer key.

You get the question, the key's entries (numbered, each with a short description), the
answer's prose, its numbered list entries, and its numbered cited claims. A key entry is a
claim, a problem or a company, depending on the question. Each cited claim belongs to a list
entry (in brackets) and names the talk it quotes.

For every list entry, give the number of the key entry it is about, or 0 if it is about
none of them.

- An entry matches a key entry when it names the same thing, in other words or at another
  level of detail: "the harness matters more than the model" matches "The Harness Over the
  Model"; "evaluating agent outputs" matches "The Verification Gap" when that entry is about
  verifying what agents produce; "Amazon Web Services" matches "Amazon Web Services (AWS)".
- An entry framed as a debate between two positions matches a key entry when one of the
  two positions is that entry.
- An entry that joins two things ("Security & identity") matches the key entry it leads with.
- An entry about something different is 0, even when the topic is related. For companies,
  a different company is 0 even if related ("Amazon" is not "Amazon Web Services (AWS)"
  when both are key entries; match the one the entry names first).
- Two list entries may match the same key entry.

For every cited claim, give the side its talk takes on its list entry, as the answer
presents it:

- "for": the talk argues for the entry's claim, gives evidence of the problem, or (for a
  company) is one of that company's talks.
- "against": the talk contradicts the claim, pushes back on it, or limits where it holds.
- "neither": the talk is cited for context, or the answer doesn't say which side it is on.

For an entry framed as a debate between two positions, "for" and "against" are relative to
the position that matches the key entry; if the entry matches no key entry, use the first
position it names.
