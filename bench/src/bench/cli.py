"""Command-line entry point: `uv run bench <command>`."""

import argparse
import asyncio
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from collections import Counter
from pathlib import Path

from bench.corpus import CHUNK_TALK_OVERRIDES, build_corpus, relink_chunk_edges
from bench.omnigraph import graph_secrets_in, install_shim

BENCH_DIR = Path(__file__).resolve().parents[2]
REPO_DIR = BENCH_DIR.parent
SHIM_BIN = BENCH_DIR / "bin"


def _real_omnigraph() -> Path | None:
    """The omnigraph CLI on PATH, skipping the shim itself."""
    dirs = os.environ.get("PATH", "").split(os.pathsep)
    path = os.pathsep.join(d for d in dirs if d and Path(d).resolve() != SHIM_BIN.resolve())
    found = shutil.which("omnigraph", path=path)
    return Path(found).resolve() if found else None


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="bench")
    commands = parser.add_subparsers(dest="command", required=True)

    corpus = commands.add_parser("corpus", help="build corpus/talks/*.md from the seed's chunks")
    corpus.add_argument("--seed", type=Path, default=REPO_DIR / "seed")
    corpus.add_argument("--out", type=Path, default=BENCH_DIR / "corpus" / "talks")

    relink = commands.add_parser(
        "relink-chunks", help="apply CHUNK_TALK_OVERRIDES to embedded chunk parts (local graph)"
    )
    relink.add_argument("parts_dir", type=Path)

    shim = commands.add_parser(
        "shim", help="install the reader-only omnigraph config (act-reader token on stdin)"
    )
    shim.add_argument("--home", type=Path, default=BENCH_DIR / ".omnigraph-home")
    shim.add_argument("--alias-pack", type=Path, default=REPO_DIR / "omnigraph-config.example.yaml")
    shim.add_argument("--omnigraph", type=Path, help="the real CLI (default: first on PATH)")

    check = commands.add_parser(
        "check-questions", help="answerability of each question from the markdown corpus alone"
    )
    check.add_argument("--questions", type=Path, default=BENCH_DIR / "questions.yaml")
    check.add_argument("--corpus", type=Path, default=BENCH_DIR / "corpus" / "talks")

    probe = commands.add_parser("probe", help="live isolation probe per arm (spends API money)")
    probe.add_argument("--arm", choices=["markdown", "omnigraph", "both"], default="both")

    run = commands.add_parser(
        "run", help="the benchmark: every question × arm × run (spends money)"
    )
    run.add_argument("--pilot", action="store_true", help="1 run per question per arm (else 3)")
    run.add_argument("--runs", type=int, help="runs per question per arm (overrides --pilot)")
    run.add_argument("--only", help="comma-separated question ids, e.g. Q01,Q09")
    run.add_argument("--arm", choices=["markdown", "omnigraph", "both"], default="both")
    run.add_argument("--concurrency", type=int, default=4)
    run.add_argument("--max-spend", type=float, help="USD; no new run starts once this is spent")

    score = commands.add_parser(
        "score", help="quote checks + support judge (asking the judge spends money; cached)"
    )
    score.add_argument("--dry-run", action="store_true", help="count claims and cost; ask nothing")
    score.add_argument("--limit", type=int, help="ask about at most N uncached claims, spread out")
    score.add_argument("--concurrency", type=int, default=4)
    score.add_argument("--runs-dir", type=Path, default=BENCH_DIR / "runs")
    score.add_argument("--corpus", type=Path, default=BENCH_DIR / "corpus" / "talks")
    score.add_argument("--seed", type=Path, default=REPO_DIR / "seed")
    score.add_argument("--cache", type=Path, default=BENCH_DIR / "runs" / "_judge")
    score.add_argument("--out", type=Path, default=BENCH_DIR / "results" / "scores.json")

    args = parser.parse_args(argv)
    if args.command == "corpus":
        written = build_corpus(args.seed, args.out, CHUNK_TALK_OVERRIDES)
        print(f"wrote {written} talks to {args.out}")
    elif args.command == "relink-chunks":
        moved = sum(
            relink_chunk_edges(part, CHUNK_TALK_OVERRIDES)
            for part in sorted(args.parts_dir.glob("part-*.jsonl"))
        )
        print(f"re-pointed {moved} chunk edge(s) in {args.parts_dir}")
    elif args.command == "shim":
        token = sys.stdin.read().strip()
        if not token:
            parser.exit(2, "bench shim: pipe the act-reader token on stdin\n")
        omnigraph_bin = args.omnigraph or _real_omnigraph()
        if omnigraph_bin is None:
            parser.exit(2, "bench shim: no omnigraph CLI on PATH\n")
        try:
            install_shim(args.home, args.alias_pack, omnigraph_bin, token)
        except subprocess.CalledProcessError as e:
            parser.exit(1, f"bench shim: omnigraph login failed: {e.stderr.strip()}\n")
        print(f"reader-only omnigraph config installed in {args.home}")
    elif args.command == "check-questions":
        from bench.questions import check_questions, load_questions

        results = check_questions(load_questions(args.questions), args.corpus)
        for r in results:
            hits = ", ".join(f"{term!r}: {n}" for term, n in r["hits"].items()) or r["detail"]
            print(f"{'PASS' if r['ok'] else 'FAIL'}  {r['id']}  {r['shape']:<12} {hits}")
        return 0 if all(r["ok"] for r in results) else 1
    elif args.command == "probe":
        return _probe(parser, ["markdown", "omnigraph"] if args.arm == "both" else [args.arm])
    elif args.command == "run":
        return _run(parser, args)
    elif args.command == "score":
        return _score(args)
    return 0


def corpus_sha(talks_dir: Path) -> str:
    """A fingerprint of the corpus the markdown arm reads: file names and bytes, in order."""
    digest = hashlib.sha256()
    for path in sorted(talks_dir.glob("*.md")):
        digest.update(path.name.encode() + b"\0" + path.read_bytes() + b"\0")
    return digest.hexdigest()


def graph_head() -> str:
    """The local graph's head commit on main, read straight from the store (not via the agent)."""
    binary = _real_omnigraph()
    store = BENCH_DIR / ".graph" / "graphs" / "spike.omni"
    if binary is None or not store.exists():
        return "unknown"
    out = subprocess.run(
        [str(binary), "commit", "list", "--branch", "main", str(store)],
        capture_output=True,
        text=True,
    )
    return (out.stdout.split("\n", 1)[0].split() or ["unknown"])[0]


def _preflight(parser: argparse.ArgumentParser, command: str, arms: list[str]) -> dict:
    if secrets := graph_secrets_in(os.environ):
        parser.exit(2, f"bench {command}: unset graph credentials first: {', '.join(secrets)}\n")
    from bench.provider import openrouter_env

    provider_env = openrouter_env(BENCH_DIR / ".env")
    if "markdown" in arms and not any((BENCH_DIR / "corpus" / "talks").glob("*.md")):
        parser.exit(2, f"bench {command}: no corpus; run `uv run bench corpus`\n")
    if "omnigraph" in arms:
        if not (BENCH_DIR / ".omnigraph-home" / "omnigraph-bin").exists():
            parser.exit(2, f"bench {command}: reader shim not installed; see `bench shim`\n")
        try:
            urllib.request.urlopen("http://127.0.0.1:8081/healthz", timeout=3)
        except OSError:
            parser.exit(2, f"bench {command}: graph server is down; scripts/local-graph.sh serve\n")
    return provider_env


def _run(parser: argparse.ArgumentParser, args: argparse.Namespace) -> int:
    from bench.questions import load_questions
    from bench.run import plan_runs, run_all

    questions = load_questions(BENCH_DIR / "questions.yaml")
    if args.only:
        wanted = [q.strip() for q in args.only.split(",") if q.strip()]
        unknown = sorted(set(wanted) - {q.id for q in questions})
        if unknown:
            parser.exit(2, f"bench run: unknown question ids: {', '.join(unknown)}\n")
        questions = [q for q in questions if q.id in wanted]
    arms = ["markdown", "omnigraph"] if args.arm == "both" else [args.arm]
    provider_env = _preflight(parser, "run", arms)

    runs = args.runs or (1 if args.pilot else 3)
    plan = plan_runs(questions, arms, runs)
    meta = {"graph_head": graph_head(), "corpus_sha": corpus_sha(BENCH_DIR / "corpus" / "talks")}
    print(f"{len(plan)} runs planned ({len(questions)} questions × {len(arms)} arms × {runs})")

    def report(r: dict) -> None:
        cost = f"${r.get('cost_usd', 0):.3f}"
        tools = r.get("tool_calls", "-")
        print(
            f"  {r['qid']} {r['arm']:<9} #{r['run']}  {r['status']:<6} "
            f"{r.get('wall_s', '-')}s  {cost}  turns={r.get('num_turns', '-')}  tools={tools}"
            + (f"  attempts={r['attempts']}" if r.get("attempts", 1) > 1 else "")
            + (f"  ({r['stop_reason']})" if r["status"] != "ok" else "")
        )

    results = asyncio.run(
        run_all(
            plan,
            concurrency=args.concurrency,
            on_done=report,
            max_spend=args.max_spend,
            bench_dir=BENCH_DIR,
            out_root=BENCH_DIR / "runs",
            work_root=Path(tempfile.gettempdir()).resolve() / "aie-bench" / "runs",
            provider_env=provider_env,
            meta=meta,
        )
    )
    already = sum((BENCH_DIR / "runs" / p.question.id / p.arm / str(p.run)).exists() for p in plan)
    spent = sum((r.get("cost_usd") or 0) + r.get("retry_cost_usd", 0) for r in results)
    errors = sum(r["status"] == "error" for r in results)
    print(f"done: {len(results)} ran, {errors} errors, ${spent:.2f} spent")
    if (missing := len(plan) - already) > 0:
        print(f"{missing} runs not started (spend limit); re-run to continue")
    return 1 if errors else 0


def _score(args: argparse.Namespace) -> int:
    from collections.abc import Callable
    from concurrent.futures import ThreadPoolExecutor, as_completed

    import anthropic

    from bench import judge
    from bench.corpus import talk_labels
    from bench.parse import normalise
    from bench.provider import JUDGE_MODEL, cost_usd
    from bench.score import load_runs, score_runs, spread, support_requests, uncited_requests
    from bench.verify import Corpus

    corpus = Corpus.load(args.corpus, talk_labels(args.seed, CHUNK_TALK_OVERRIDES))
    runs = load_runs(args.runs_dir)
    support_todo, uncited_todo = support_requests(runs, corpus), uncited_requests(runs)
    # Identical requests share one judgment: one entry per cache file.
    requests: dict[Path, tuple[str, dict, Callable[[dict], bool]]] = {}
    for todo, valid in ((support_todo, judge.valid_support), (uncited_todo, judge.valid_uncited)):
        for label, request in todo:
            requests.setdefault(judge.cache_path(request, args.cache), (label, request, valid))
    records = {
        path: judge.lookup(request, args.cache) for path, (_, request, _) in requests.items()
    }
    uncached = [item for path, item in requests.items() if records[path] is None]

    def counts(todo: list[tuple[str, dict]]) -> str:
        paths = {judge.cache_path(request, args.cache) for _, request in todo}
        missing = sum(records[path] is None for path in paths)
        return f"{len(paths) - missing} cached, {missing} to ask"

    claims = sum(len(normalise(run.get("answer_json")).claims) for run in runs)
    print(
        f"{len(runs)} runs, {claims} claims, {len(support_todo)} to judge: {counts(support_todo)}"
    )
    print(f"uncited check: {len(uncited_todo)} runs, {counts(uncited_todo)}")
    costs = [cost_usd(JUDGE_MODEL, record["usage"]) for record in records.values() if record]
    if costs and uncached:
        mean = sum(costs) / len(costs)
        rest = mean * len(uncached)
        print(f"judged so far ${sum(costs):.2f}, ${mean:.4f} a request: the rest ≈ ${rest:.2f}")
    if args.dry_run:
        return 0

    batch = spread(uncached, args.limit) if args.limit is not None else uncached
    errors, spent = 0, 0.0
    if batch:
        ask = judge.openrouter_ask(BENCH_DIR / ".env")
        with ThreadPoolExecutor(args.concurrency) as pool:
            futures = {
                pool.submit(judge.cached, request, ask, args.cache, valid): label
                for label, request, valid in batch
            }
            for n, future in enumerate(as_completed(futures), 1):
                label = futures[future]
                try:
                    record = future.result()
                except (judge.JudgeError, anthropic.APIError) as e:
                    errors += 1
                    print(f"  [{n}/{len(batch)}] {label}  error: {e}", flush=True)
                    continue
                cost = cost_usd(JUDGE_MODEL, record["usage"])
                spent += cost
                output = record["output"]
                result = output.get("verdict") or f"uncited {len(output['uncited'])}"
                print(
                    f"  [{n}/{len(batch)}] {label}  {result:<11} ${cost:.4f}"
                    f"  out={record['usage'].get('output_tokens')}",
                    flush=True,
                )
        done = len(batch) - errors
        print(
            f"asked {len(batch)}: {errors} errors, ${spent:.2f}"
            + (f", ${spent / done:.4f} a request" if done else "")
        )

    scored = score_runs(runs, corpus, args.cache)
    left_claims = sum(claim["grounding"] is None for run in scored for claim in run["claims"])
    left_runs = sum(run["uncited"] is None for run in scored)
    if left_claims or left_runs:
        print(f"{left_claims} claims and {left_runs} runs still unjudged; {args.out} not written")
        return 1 if errors else 0
    total = sum(
        cost_usd(JUDGE_MODEL, judge.lookup(request, args.cache)["usage"])
        for _, request, _ in requests.values()
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    scores = {
        "judge": {
            "model": JUDGE_MODEL,
            "claims_judged": len(support_todo),
            "runs_checked": len(uncited_todo),
            "requests": len(requests),
            "cost_usd": round(total, 4),
        },
        "runs": scored,
    }
    args.out.write_text(json.dumps(scores, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for arm in sorted({run["arm"] for run in scored}):
        arm_runs = [run for run in scored if run["arm"] == arm]
        buckets = Counter(c["grounding"] for run in arm_runs for c in run["claims"])
        uncited = sum(len(run["uncited"]) for run in arm_runs)
        print(
            f"{arm}: "
            + ", ".join(f"{b} {buckets[b]}" for b in ("grounded", "partial", "hallucinated"))
            + f"; uncited {uncited} in {len(arm_runs)} answers"
        )
    print(f"wrote {args.out}")
    return 1 if errors else 0


def _probe(parser: argparse.ArgumentParser, arms: list[str]) -> int:
    provider_env = _preflight(parser, "probe", arms)
    from bench.probe import run_probe

    failed = 0
    for arm in arms:
        summary = run_probe(arm, BENCH_DIR, REPO_DIR, provider_env, BENCH_DIR / "runs" / "_probe")
        print(
            f"\n{arm}: {summary['num_turns']} turns, {summary['wall_s']}s, ${summary['cost_usd']}"
        )
        for c in summary["checks"]:
            print(f"  {'PASS' if c['ok'] else 'FAIL'}  {c['check']:<20} {c['detail']}")
        print(f"  trace: {summary['out']}")
        failed += sum(not c["ok"] for c in summary["checks"])
    return 1 if failed else 0
