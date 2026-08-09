#!/usr/bin/env python3
"""Merge frag-*.jsonl + existing seed.jsonl into seed-full.jsonl with strict validation."""
import json, glob, re, sys, collections

ROOT = "/Users/andrew/code/intel-graph"
DT = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z$")

REQUIRED = {
    "Signal": ["slug","name","brief","stagingTimestamp","createdAt","updatedAt"],
    "Element": ["slug","name","kind","createdAt","updatedAt"],
    "Pattern": ["slug","name","kind","createdAt","updatedAt"],
    "Insight": ["slug","name","createdAt","updatedAt"],
    "KnowHow": ["slug","name","stagingTimestamp","createdAt","updatedAt"],
    "Company": ["slug","name"],
    "SourceEntity": ["slug","name"],
    "Expert": ["slug","name"],
    "InformationArtifact": ["slug","name","artifactType","stagingTimestamp","createdAt","updatedAt"],
}
ENUMS = {
    ("Signal","domain"): {"training","inference","infra","harness","robotics","security","data-eng","context"},
    ("Element","domain"): {"training","inference","infra","harness","robotics","security","data-eng","context"},
    ("Element","kind"): {"product","technology","framework","concept","ops"},
    ("Pattern","kind"): {"challenge","disruption","dynamic"},
    ("Company","type"): {"bigtech","developer","investor","research","hardware","media"},
    ("SourceEntity","type"): {"blog","newsletter","video_channel","academic_repository","podcast","organization"},
    ("InformationArtifact","artifactType"): {"email","youtube","pdf","article"},
}
EDGES = {  # name: (srcType, dstType)
    "FormsPattern":("Signal","Pattern"), "ContradictsPattern":("Signal","Pattern"),
    "HighlightsPattern":("Insight","Pattern"), "ReliesOnElement":("Insight","Element"),
    "ReliesOnPattern":("Pattern","Pattern"), "DrivesPattern":("Pattern","Pattern"),
    "ContradictsToPattern":("Pattern","Pattern"), "OnElement":("Signal","Element"),
    "EnablesElement":("Element","Element"), "UsesElement":("Element","Element"),
    "ExemplifiesPattern":("Element","Pattern"), "EnablesPattern":("Element","Pattern"),
    "PublishedBySource":("InformationArtifact","SourceEntity"),
    "ContributedByExpert":("InformationArtifact","Expert"),
    "SpottedInArtifact":("Signal","InformationArtifact"),
    "IdentifiedInArtifact":("Element","InformationArtifact"),
    "SourcedFromArtifact":("KnowHow","InformationArtifact"),
    "SourcedFromSource":("Signal","SourceEntity"),
    "RelevantCompany":("Signal","Company"), "DevelopedByCompany":("Element","Company"),
    "AffiliatedWithCompany":("Expert","Company"), "ReferencesElement":("KnowHow","Element"),
}
RETIRED = {"pat-html-native-medium","pat-provider-blind-ai"}

slug_type = {}          # slug -> type (base + accepted new)
base_lines = []
problems = collections.Counter()
detail = []

for line in open(f"{ROOT}/seed.jsonl"):
    line = line.strip()
    if not line: continue
    d = json.loads(line)
    if "type" in d:
        slug_type[d["data"]["slug"]] = d["type"]
    base_lines.append(line)

new_nodes = {}          # slug -> (line, type, frag)
edges_raw = []          # (edge, from, to, frag)
dupes = []

for frag in sorted(glob.glob(f"{ROOT}/seed-work/frag-*.jsonl")):
    fname = frag.split("/")[-1]
    for ln, line in enumerate(open(frag), 1):
        line = line.strip()
        if not line: continue
        try:
            d = json.loads(line)
        except Exception as e:
            problems["bad-json"] += 1; detail.append(f"{fname}:{ln} bad json: {e}"); continue
        if "edge" in d:
            edges_raw.append((d["edge"], d.get("from"), d.get("to"), f"{fname}:{ln}"))
            continue
        t = d.get("type"); data = d.get("data", {})
        slug = data.get("slug")
        if t not in REQUIRED:
            problems["bad-type"] += 1; detail.append(f"{fname}:{ln} unknown type {t}"); continue
        if not slug:
            problems["no-slug"] += 1; detail.append(f"{fname}:{ln} missing slug"); continue
        if slug in RETIRED:
            problems["retired"] += 1; detail.append(f"{fname}:{ln} retired slug {slug}"); continue
        missing = [k for k in REQUIRED[t] if not data.get(k)]
        if missing:
            problems["missing-required"] += 1
            detail.append(f"{fname}:{ln} {t} {slug} missing {missing}"); continue
        bad_enum = False
        for (tt, field), allowed in ENUMS.items():
            if tt == t and data.get(field) is not None and data[field] not in allowed:
                problems["bad-enum"] += 1
                detail.append(f"{fname}:{ln} {t} {slug} {field}={data[field]!r} not in enum"); bad_enum = True
        if bad_enum: continue
        for field in ("stagingTimestamp","createdAt","updatedAt"):
            if field in data and data[field] is not None and not DT.match(str(data[field])):
                problems["bad-datetime"] += 1
                detail.append(f"{fname}:{ln} {t} {slug} {field}={data[field]!r}"); bad_enum = True
        if bad_enum: continue
        data.setdefault("id", slug)
        if slug in slug_type or slug in new_nodes:
            dupes.append(f"{slug} ({t}) dup in {fname}:{ln}"); continue
        new_nodes[slug] = (json.dumps({"type":t,"data":data}, ensure_ascii=False), t, fname)

for slug, (_, t, _) in new_nodes.items():
    slug_type[slug] = t

accepted_edges, seen_edges = [], set()
for name, f, to, where in edges_raw:
    if name not in EDGES:
        problems["bad-edge-name"] += 1; detail.append(f"{where} unknown edge {name}"); continue
    if f in RETIRED or to in RETIRED:
        problems["retired-edge"] += 1; detail.append(f"{where} edge to retired {name} {f}->{to}"); continue
    st, dt_ = EDGES[name]
    if f not in slug_type:
        problems["dangling-from"] += 1; detail.append(f"{where} {name} from {f} undefined"); continue
    if to not in slug_type:
        problems["dangling-to"] += 1; detail.append(f"{where} {name} to {to} undefined"); continue
    if slug_type[f] != st or slug_type[to] != dt_:
        problems["type-mismatch"] += 1
        detail.append(f"{where} {name} {f}({slug_type[f]})->{to}({slug_type[to]}) wants {st}->{dt_}"); continue
    key = (name, f, to)
    if key in seen_edges: continue
    seen_edges.add(key)
    accepted_edges.append(json.dumps({"edge":name,"from":f,"to":to,"data":{}}))

with open(f"{ROOT}/seed-work/seed-full.jsonl","w") as out:
    for l in base_lines: out.write(l + "\n")
    for slug in new_nodes: out.write(new_nodes[slug][0] + "\n")
    for e in accepted_edges: out.write(e + "\n")

tc = collections.Counter(t for _, (_, t, _) in new_nodes.items())
ec = collections.Counter(json.loads(e)["edge"] for e in accepted_edges)
with open(f"{ROOT}/seed-work/validation-report.txt","w") as r:
    r.write(f"new nodes: {sum(tc.values())} {dict(tc)}\n")
    r.write(f"accepted edges: {len(accepted_edges)} {dict(ec)}\n")
    r.write(f"cross-fragment dupes (first wins): {len(dupes)}\n")
    for d_ in dupes: r.write(f"  DUP {d_}\n")
    r.write(f"problems: {dict(problems)}\n")
    for d_ in detail: r.write(f"  {d_}\n")
print(f"new nodes: {sum(tc.values())} | edges: {len(accepted_edges)} | dupes: {len(dupes)} | problems: {sum(problems.values())}")
print(dict(problems))
