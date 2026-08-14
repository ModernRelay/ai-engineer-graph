#!/usr/bin/env python3
"""Convert batch 17/18/19 extraction markdown -> frag-{17,18,19}.jsonl.

Follows seed-work/CONVERSION-SPEC.md. Structural parser: only designated
edge-bearing cells/lines are scanned, never prose paragraphs, so "Reused
elements (no new nodes): `el-foo`" can never leak an edge.

Signal/Insight tables carry a combined "name / brief" column, so `name` is
derived deterministically from the slug (declarative, <=90 chars) and the cell
text becomes `brief` — matching the spec's "short label distilled from the row".
"""
import json, re, sys, collections, pathlib

ROOT = pathlib.Path("/Users/andrew/code/intel-graph")
EX = ROOT / "extraction"

BATCHES = {
    # NOTE: frag-16a/frag-16b on disk are batch *15*'s conversion (29 talks).
    # Batch 16's own 9 talks were never converted — emitted here as frag-16c.
    "16c": ["davis-temporal-mcp-tasks", "salomon-yosef-mcp-apps", "varda-cloudflare-gadgets",
            "kramer-daily-ai-native-primitives", "abdallah-nvidia-local-models",
            "panel-compression-at-the-edge", "panel-state-of-model-routing",
            "eskildsen-turbopuffer-building", "rizwan-cline-open-source-dead"],
    17: ["chatterjee-sonar-guide-verify-solve", "smith-resolve-always-on-agents",
         "linkov-wisedocs-coding-agent-benchmarks", "singh-superconductor-multiplayer-agents",
         "gazit-github-realtime-multiplayer", "dailey-ref-velocity-sickness",
         "coyle-berkeley-cca-field-guide"],
    18: ["kundel-openai-codex-behind-harness", "jiang-modal-rl-cross-datacenter"],
    19: ["su-neocognition-continual-learning-expertise", "morris-engram-scaling-compute-on-context",
         "malde-trajectory-scaling-continual-learning", "asawa-berkeley-evaluating-continual-learning",
         "denton-applied-compute-continual-learning-enterprise", "hooker-adaption-gradient-free-learning",
         "khemani-every-memory-system", "druga-sakana-memory-harnesses",
         "holmes-warp-llm-knowledge-bases", "trivedy-langchain-agents-data-mining",
         "bhat-he-anthropic-agentic-surfaces", "khandelwal-amazon-agents-codebases-teams",
         "hylak-raindrop-designing-agents"],
}

EDGES = {
    "FormsPattern": ("Signal", "Pattern"), "ContradictsPattern": ("Signal", "Pattern"),
    "HighlightsPattern": ("Insight", "Pattern"), "ReliesOnElement": ("Insight", "Element"),
    "ReliesOnPattern": ("Pattern", "Pattern"), "DrivesPattern": ("Pattern", "Pattern"),
    "ContradictsToPattern": ("Pattern", "Pattern"), "OnElement": ("Signal", "Element"),
    "EnablesElement": ("Element", "Element"), "UsesElement": ("Element", "Element"),
    "ExemplifiesPattern": ("Element", "Pattern"), "EnablesPattern": ("Element", "Pattern"),
    "PublishedBySource": ("InformationArtifact", "SourceEntity"),
    "ContributedByExpert": ("InformationArtifact", "Expert"),
    "SpottedInArtifact": ("Signal", "InformationArtifact"),
    "IdentifiedInArtifact": ("Element", "InformationArtifact"),
    "SourcedFromArtifact": ("KnowHow", "InformationArtifact"),
    "SourcedFromSource": ("Signal", "SourceEntity"),
    "RelevantCompany": ("Signal", "Company"), "DevelopedByCompany": ("Element", "Company"),
    "AffiliatedWithCompany": ("Expert", "Company"), "ReferencesElement": ("KnowHow", "Element"),
}
SLUG = re.compile(r"`((?:sig|pat|el|ins|how|co|exp|ia|source)-[a-z0-9][a-z0-9-]*)`")
EDGENAME = re.compile(r"\b(" + "|".join(EDGES) + r")\b`?\s*(?:also\s+|now\s+)?`?\s*(?:→|->)")
TOKEN = re.compile(EDGENAME.pattern + r"|" + SLUG.pattern)

ELEMENT_KINDS = {"product", "technology", "framework", "concept", "ops"}
KIND_COERCE = {"tool": "technology", "library": "framework", "method": "concept",
               "metric": "concept", "doc": "ops", "process": "ops", "practice": "ops"}
CO_TYPES = {"bigtech", "developer", "investor", "research", "hardware", "media"}
CO_COERCE = {"fintech": "developer", "consultancy": "developer", "startup": "developer",
             "enterprise": "developer", "university": "research", "lab": "research",
             "vc": "investor", "accelerator": "investor", "advertising": "media",
             "publisher": "media", "education-content": "media"}

coerced, skipped = [], []


def cells(line):
    if not line.strip().startswith("|"):
        return None
    parts = [c.strip() for c in line.strip().strip("|").split("|")]
    return parts


def is_sep(parts):
    return parts and all(set(c) <= set("-: ") and c for c in parts)


def table_rows(lines, start, end=None):
    """Yield cell-lists of a markdown table beginning at/after `start`.

    Never crosses `end` — a section with no table (e.g. "## Companies (0 new)")
    must not fall through into the next section's table.
    """
    i, header = start, None
    end = len(lines) if end is None else end
    while i < end:
        p = cells(lines[i])
        if p is None:
            if header is not None:
                break
            i += 1
            continue
        if is_sep(p):
            i += 1
            continue
        if header is None:
            header = p
            i += 1
            continue
        yield p
        i += 1


REUSE_MARK = re.compile(r"^(Reused|Not coined|Referenced,|Referenced without|Kept in prose)")


def section(lines, name):
    """Return (start_index, end_index) of a '## <name>' section body."""
    for i, l in enumerate(lines):
        if re.match(rf"^##\s+{re.escape(name)}\b", l):
            for j in range(i + 1, len(lines)):
                if lines[j].startswith("## "):
                    return i + 1, j
            return i + 1, len(lines)
    return None


def defs_end(lines, s):
    """End of the DEFINITION region of a section: stops at the first
    'Reused …' / 'Not coined …' marker so reuse tables are never read as
    new nodes."""
    for j in range(s[0], s[1]):
        if REUSE_MARK.match(lines[j].strip()):
            return j
    return s[1]


SPAN = re.compile(r"`([^`]*)`")


def normalize_spans(text):
    """Rewrite `Edge -> target` code spans into `Edge` -> `target`.

    Extractions write the edge and its FIRST target inside one code span
    ("`OnElement -> el-foo`, `el-bar`"), so a strict backtick-delimited slug
    regex silently drops that first target. Normalizing here keeps the strict
    regex — a permissive one would match prose like "co-optimize" as a co- slug.
    """
    def fix(m):
        inner = m.group(1)
        if "→" in inner or "->" in inner:
            parts = re.split(r"→|->", inner)
            head = parts[0].strip()
            tail = [x.strip() for x in parts[1:] if x.strip()]
            return "`" + head + "` → " + ", ".join("`" + x + "`" for x in tail)
        return m.group(0)
    return SPAN.sub(fix, text)


def parse_edges(text, subject):
    """Extract (edge, subject, target) from a designated edge-bearing string."""
    text = normalize_spans(text)
    out, cur = [], None
    for m in TOKEN.finditer(text):
        if m.group(1):
            cur = m.group(1)
        elif m.group(2) and cur:
            out.append((cur, subject, m.group(2)))
    return out


def split_segments(text):
    """Split an element-edge line on ';' at paren/bracket depth 0.

    Batch-16 blocks put several subjects on one line ("`el-a` `Edge -> x`;
    `el-b` `Edge -> y`"), while b17-19 use one subject per line. Depth-aware
    so a ';' inside a parenthetical aside never splits a segment.
    """
    segs, buf, depth = [], [], 0
    for ch in text:
        if ch in "([":
            depth += 1
        elif ch in ")]":
            depth = max(0, depth - 1)
        if ch == ";" and depth == 0:
            segs.append("".join(buf)); buf = []
        else:
            buf.append(ch)
    segs.append("".join(buf))
    return [s for s in segs if s.strip()]


def clean(s):
    s = re.sub(r"\*\*\[[^\]]*\]\*\*", "", s)
    s = s.replace("**", "").replace("`", "").strip()
    return re.sub(r"\s+", " ", s)


def label_from_slug(slug):
    body = slug.split("-", 1)[1].replace("-", " ")
    return (body[:1].upper() + body[1:])[:90]


def convert(stem):
    md = (EX / f"{stem}.md").read_text()
    lines = md.split("\n")
    m = re.search(r"all dated nodes[^:]*:\s*(\d{4}-\d{2}-\d{2})", md) or \
        re.search(r"published (\d{4}-\d{2}-\d{2})", md)
    if not m:
        raise SystemExit(f"{stem}: no date")
    ts = m.group(1) + "T00:00:00Z"
    nodes, edges = [], []
    defined = collections.defaultdict(set)

    def add(t, data):
        data.setdefault("id", data["slug"])
        nodes.append({"type": t, "data": data})
        defined[t].add(data["slug"])

    # ---- InformationArtifact
    s = section(lines, "InformationArtifact")
    ia_slug = None
    for r in table_rows(lines, s[0], defs_end(lines, s)):
        sl = SLUG.search(r[0])
        if not sl:
            continue
        ia_slug = sl.group(1)
        add("InformationArtifact", {"slug": ia_slug, "name": clean(r[1]),
                                    "artifactType": clean(r[2]) or "youtube",
                                    "link": clean(r[3]), "stagingTimestamp": ts,
                                    "createdAt": ts, "updatedAt": ts})
    for l in lines[s[0]:s[1]]:
        if l.startswith("Edges:"):
            edges += parse_edges(l, ia_slug)

    # ---- Experts
    s = section(lines, "Experts")
    if s:
        for r in table_rows(lines, s[0], defs_end(lines, s)):
            sl = SLUG.search(r[0])
            if not sl:
                continue
            slug = sl.group(1)
            add("Expert", {"slug": slug, "name": clean(r[1].split("(")[0])})
            if len(r) > 2:
                edges += parse_edges(r[2], slug)

    # ---- Companies
    s = section(lines, "Companies")
    if s:
        for r in table_rows(lines, s[0], defs_end(lines, s)):
            sl = SLUG.search(r[0])
            if not sl:
                continue
            slug = sl.group(1)
            d = {"slug": slug, "name": clean(r[1])}
            if len(r) > 2:
                raw = clean(r[2]).lower()
                t = raw if raw in CO_TYPES else CO_COERCE.get(raw)
                if t:
                    if t != raw:
                        coerced.append(f"{slug}: {raw} -> {t}")
                    d["type"] = t
                elif raw and raw != "—":
                    skipped.append(f"{stem}: company {slug} type {raw!r} unmapped, omitted")
            if len(r) > 3 and clean(r[3]):
                d["brief"] = clean(r[3])
            add("Company", d)

    # ---- Patterns (only where defined)
    s = section(lines, "Patterns")
    if s:
        for r in table_rows(lines, s[0], defs_end(lines, s)):
            sl = SLUG.search(r[0])
            if not sl:
                continue
            add("Pattern", {"slug": sl.group(1), "name": clean(r[1]), "kind": clean(r[2]),
                            "brief": clean(r[3])[:2000], "createdAt": ts, "updatedAt": ts})

    # ---- Elements
    s = section(lines, "Elements")
    el_slugs = []
    if s:
        for r in table_rows(lines, s[0], defs_end(lines, s)):
            sl = SLUG.search(r[0])
            if not sl:
                continue
            slug = sl.group(1)
            kind = clean(r[2]).lower()
            if kind not in ELEMENT_KINDS:
                nk = KIND_COERCE.get(kind)
                if nk:
                    coerced.append(f"{slug}: {kind} -> {nk}")
                    kind = nk
                else:
                    skipped.append(f"{stem}: element {slug} kind {kind!r} unmapped -> concept")
                    kind = "concept"
            d = {"slug": slug, "name": clean(r[1]), "kind": kind,
                 "brief": clean(r[4])[:4000], "createdAt": ts, "updatedAt": ts}
            dom = clean(r[3])
            if dom in {"training", "inference", "infra", "harness", "robotics",
                       "security", "data-eng", "context"}:
                d["domain"] = dom
            add("Element", d)
            el_slugs.append(slug)
        # element edge block
        block, inblock = [], False
        for l in lines[s[0]:s[1]]:
            if l.startswith("Element edges:"):
                inblock = True
            elif inblock and (not l.strip() or l.startswith("Reused elements")):
                inblock = False
            if inblock:
                block.append(l)
        for l in block:
            if re.search(r"all\s+\w+\s+`?IdentifiedInArtifact", l) or \
               ("IdentifiedInArtifact" in l and re.search(r"\ball\b", l)):
                for e in el_slugs:
                    edges.append(("IdentifiedInArtifact", e, ia_slug))
                continue
            body = l.split(":", 1)[1] if l.startswith("Element edges:") else l
            for seg in split_segments(normalize_spans(body)):
                subj = SLUG.search(seg)
                if not subj:
                    continue
                edges += parse_edges(seg[subj.end():], subj.group(1))

    # ---- Signals
    s = section(lines, "Signals")
    sig_slugs, blanket = [], []
    if s:
        for l in lines[s[0]:s[1]]:
            if l.startswith("All:") or l.startswith("All :"):
                blanket.append(l)
        for r in table_rows(lines, s[0], defs_end(lines, s)):
            sl = SLUG.search(r[0])
            if not sl:
                continue
            slug = sl.group(1)
            d = {"slug": slug, "name": label_from_slug(slug), "brief": clean(r[2])[:4000],
                 "stagingTimestamp": ts, "createdAt": ts, "updatedAt": ts}
            dom = clean(r[1])
            if dom in {"training", "inference", "infra", "harness", "robotics",
                       "security", "data-eng", "context"}:
                d["domain"] = dom
            add("Signal", d)
            sig_slugs.append(slug)
            for col in r[3:]:
                edges += parse_edges(col, slug)
        for l in blanket:
            for sg in sig_slugs:
                edges += parse_edges(l, sg)

    # ---- Insights
    s = section(lines, "Insights")
    if s:
        for r in table_rows(lines, s[0], defs_end(lines, s)):
            sl = SLUG.search(r[0])
            if not sl:
                continue
            slug = sl.group(1)
            add("Insight", {"slug": slug, "name": label_from_slug(slug),
                            "brief": clean(r[1])[:4000], "createdAt": ts, "updatedAt": ts})
            for col in r[2:]:
                edges += parse_edges(col, slug)

    # ---- KnowHow
    s = section(lines, "KnowHow")
    if s:
        kh_slugs, kh_blanket = [], []
        for l in lines[s[0]:s[1]]:
            if l.startswith("All:"):
                kh_blanket.append(l)
        for r in table_rows(lines, s[0], defs_end(lines, s)):
            sl = SLUG.search(r[0])
            if not sl:
                continue
            slug = sl.group(1)
            g = [x.strip() for x in re.split(r";", clean(r[2])) if x.strip()]
            add("KnowHow", {"slug": slug, "name": clean(r[1]), "guidelines": g[:60],
                            "stagingTimestamp": ts, "createdAt": ts, "updatedAt": ts})
            kh_slugs.append(slug)
            for col in r[3:]:
                edges += parse_edges(col, slug)
        for l in kh_blanket:
            for k in kh_slugs:
                edges += parse_edges(l, k)

    return nodes, edges


def main():
    for b, stems in BATCHES.items():
        allnodes, alledges, seen = [], set(), set()
        for stem in stems:
            n, e = convert(stem)
            for node in n:
                allnodes.append(node)
            for edge in e:
                if None in edge:
                    continue
                alledges.add(edge)
        out = ROOT / "seed-work" / f"frag-{b}.jsonl"
        with open(out, "w") as fh:
            for node in allnodes:
                fh.write(json.dumps(node, ensure_ascii=False) + "\n")
            for (name, f, t) in sorted(alledges):
                fh.write(json.dumps({"edge": name, "from": f, "to": t, "data": {}}) + "\n")
        tc = collections.Counter(x["type"] for x in allnodes)
        print(f"FRAGMENT|{out}")
        print("COUNTS|" + "|".join(f"{k}={v}" for k, v in sorted(tc.items())) +
              f"|edges={len(alledges)}")
    print("COERCED|" + ("; ".join(sorted(set(coerced))) or "NONE"))
    print("SKIPPED|" + ("; ".join(sorted(set(skipped))) or "NONE"))


if __name__ == "__main__":
    main()
