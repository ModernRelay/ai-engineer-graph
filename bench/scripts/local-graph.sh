#!/usr/bin/env bash
# A local, file-backed copy of the graph for the benchmark, under bench/.graph/
# (gitignored). The tracked cluster.yaml is left alone: setup copies it without
# the S3 `storage:` line, plus the schema, queries and policies.
#
#   bench/scripts/local-graph.sh setup   # config copy, fresh bearer tokens, cluster import + apply
#   bench/scripts/local-graph.sh load    # seed nodes + edges, chunks (embedded via OpenRouter), evidence, optimize
#   bench/scripts/local-graph.sh serve   # omnigraph-server on 127.0.0.1:8081
#   bench/scripts/local-graph.sh stop
#   bench/scripts/local-graph.sh status
#
# Chunks are embedded with google/gemini-embedding-2-preview (the seed's
# embed-spec model) through OpenRouter's OpenAI-compatible API, so it needs
# OPENROUTER_KEY in bench/.env. The server uses the same model for nearest().
set -euo pipefail

cd "$(dirname "$0")/../.."
L=bench/.graph
G=$L/graphs/spike.omni
E=$L/embedded
BIND=127.0.0.1:8081

strip() { grep -v -E "Backtrace|RUST_BACKTRACE|Location:|\.rs:" | sed -E 's/sk-or-[A-Za-z0-9-]+/<key>/g' || true; }
head_commit() { omnigraph commit list --branch main "$G" 2>/dev/null | head -1; }

embedding_env() {
  set -a; . bench/.env; set +a
  export OPENROUTER_API_KEY="$OPENROUTER_KEY" OMNIGRAPH_EMBED_PROVIDER=openai-compatible \
         OMNIGRAPH_EMBED_MODEL=google/gemini-embedding-2-preview
}

load_once() {  # load_once <file> <mode> <marker>: loads a file at most once, checks the head moved
  local file=$1 mode=$2 marker=$E/$3.loaded before
  [ -f "$marker" ] && { echo "$3: already loaded"; return; }
  before=$(head_commit)
  omnigraph load --data "$file" --mode "$mode" --as act-analyst --yes "$G" 2>&1 | strip | tail -1
  [ "$(head_commit)" != "$before" ] || { echo "$3: commit head did not advance" >&2; exit 1; }
  touch "$marker"
}

setup() {
  mkdir -p "$L" && chmod 700 "$L"
  grep -v '^storage:' cluster.yaml > "$L/cluster.yaml"
  cp schema.pg "$L/"
  rm -rf "$L/queries" "$L/policies" && cp -R queries policies "$L/"
  python3 -c "
import json, sys
spec = json.load(open('seed/embed-spec.json'))
spec['model'] = 'google/' + spec['model']
json.dump(spec, open('$L/embed-spec.json', 'w'), indent=2)"
  if [ ! -f "$L/tokens.env" ]; then
    python3 - "$L/tokens.env" <<'PY'
import json, os, secrets, sys
tokens = {a: secrets.token_urlsafe(32) for a in ("act-reader", "act-analyst", "act-admin")}
with open(sys.argv[1], "w") as f:
    f.write(f"OMNIGRAPH_SERVER_BEARER_TOKENS_JSON='{json.dumps(tokens)}'\n")
    for actor, token in tokens.items():
        f.write(f"TOKEN_{actor.upper().replace('-', '_')}={token}\n")
os.chmod(sys.argv[1], 0o600)
PY
  fi
  [ -f "$L/__cluster/state.json" ] || omnigraph cluster import --config "$L" | strip
  omnigraph cluster apply --config "$L" --as act-admin 2>&1 | strip | tail -2
}

embed_part() {  # embed_part <seed part>: writes $E/<part>.jsonl, retrying with backoff
  local f=$1 p out attempt
  p=$(basename "$f" .jsonl) out=$E/$(basename "$f")
  [ -s "$out" ] && return 0
  for attempt in 1 2 3 4; do
    if omnigraph embed --input "$f" --output "$out.tmp" --spec "$L/embed-spec.json" --json \
         > "$E/$p.embed.log" 2>&1; then
      mv "$out.tmp" "$out" && echo "$p: embedded" && return 0
    fi
    echo "$p: embed attempt $attempt failed: $(strip < "$E/$p.embed.log" | grep -v '^\s*$' | tail -1)"
    sleep $((attempt * 30))
  done
  return 1
}

load() {
  mkdir -p "$E"
  for f in seed/0[1-9]-*.jsonl seed/10-edges.jsonl; do
    load_once "$f" overwrite "$(basename "$f" .jsonl)"
  done
  # Embedding is network-bound, so parts embed four at a time; loads stay sequential.
  embedding_env
  export -f embed_part strip && export L E
  ls seed/chunks/part-*.jsonl | xargs -P 4 -I{} bash -c 'embed_part "$1"' _ {} \
    || { echo "embedding failed; re-run load to resume" >&2; exit 1; }
  # Known seed mis-links (bench.corpus.CHUNK_TALK_OVERRIDES) are corrected in the local
  # copies only, so the graph and the markdown corpus agree; the tracked seed is untouched.
  (cd bench && uv run --quiet bench relink-chunks "../$E")
  for f in seed/chunks/part-*.jsonl; do
    load_once "$E/$(basename "$f")" merge "$(basename "$f" .jsonl)"
  done
  load_once seed/11-evidence.jsonl merge evidence
  omnigraph optimize "$G" --json 2>&1 | strip | tail -3
}

serve() {
  if curl -s -m 2 "http://$BIND/healthz" >/dev/null; then echo "already serving on $BIND"; return; fi
  ( set -a; . "$L/tokens.env"; set +a; embedding_env
    nohup omnigraph-server --cluster "$L" --bind "$BIND" > "$L/server.log" 2>&1 & echo $! > "$L/server.pid" )
  for _ in $(seq 20); do
    curl -s -m 2 "http://$BIND/healthz" && { echo; return; }
    sleep 1
  done
  echo "server did not come up; see $L/server.log" >&2; exit 1
}

stop() {
  [ -f "$L/server.pid" ] && kill "$(cat "$L/server.pid")" 2>/dev/null && rm -f "$L/server.pid" && echo stopped || echo "not running"
}

status() {
  curl -s -m 2 "http://$BIND/healthz" && echo || echo "server: down"
  echo "graph head: $(head_commit)"
  ls "$E"/*.loaded 2>/dev/null | wc -l | xargs echo "loaded markers:"
}

"${1:?usage: local-graph.sh setup|load|serve|stop|status}"
