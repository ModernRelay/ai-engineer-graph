import io
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from bench.cli import main
from bench.omnigraph import graph_secrets_in, install_shim

SHIM = Path(__file__).resolve().parents[1] / "bin" / "omnigraph"
ALIAS_PACK_TEXT = (
    "servers:\n"
    "  intel-local:\n"
    "    url: http://127.0.0.1:8081\n"
    "aliases:\n"
    "  top-patterns: { server: intel-local, graph: spike, query: top_patterns_by_signals }\n"
)


@pytest.fixture
def fake_omnigraph(tmp_path):
    """Stands in for the real CLI: records its argv, stdin and graph-related env."""
    script = tmp_path / "real-omnigraph"
    script.write_text(
        f"#!{sys.executable}\n"
        "import json, os, sys\n"
        "record = {\n"
        "    'argv': sys.argv[1:],\n"
        "    'stdin': sys.stdin.read(),\n"
        "    'env': {k: v for k, v in os.environ.items()\n"
        "            if k.startswith(('OMNIGRAPH_', 'AWS_', 'TOKEN_ACT_', 'GEMINI_'))},\n"
        "}\n"
        "open(os.environ['FAKE_RECORD'], 'w').write(json.dumps(record))\n"
    )
    script.chmod(0o755)
    return script


@pytest.fixture
def alias_pack(tmp_path):
    path = tmp_path / "omnigraph-config.example.yaml"
    path.write_text(ALIAS_PACK_TEXT)
    return path


def recorded(path: Path) -> dict:
    return json.loads(path.read_text())


# ── install ─────────────────────────────────────────────────────────────────


def test_install_uses_the_alias_pack_as_the_config(
    tmp_path, alias_pack, fake_omnigraph, monkeypatch
):
    monkeypatch.setenv("FAKE_RECORD", str(tmp_path / "login.json"))
    home = tmp_path / ".omnigraph-home"

    install_shim(home, alias_pack, fake_omnigraph, "reader-token")

    assert (home / "config.yaml").read_text() == ALIAS_PACK_TEXT


def test_install_logs_in_with_the_token_on_stdin(tmp_path, alias_pack, fake_omnigraph, monkeypatch):
    monkeypatch.setenv("FAKE_RECORD", str(tmp_path / "login.json"))
    home = tmp_path / ".omnigraph-home"

    install_shim(home, alias_pack, fake_omnigraph, "reader-token")

    login = recorded(tmp_path / "login.json")
    assert login["argv"] == ["login", "intel-local"]
    assert login["stdin"] == "reader-token"
    assert login["env"]["OMNIGRAPH_HOME"] == str(home)


def test_install_keeps_the_home_private(tmp_path, alias_pack, fake_omnigraph, monkeypatch):
    monkeypatch.setenv("FAKE_RECORD", str(tmp_path / "login.json"))
    home = tmp_path / ".omnigraph-home"

    install_shim(home, alias_pack, fake_omnigraph, "reader-token")

    assert home.stat().st_mode & 0o777 == 0o700


def test_install_fails_when_login_fails(tmp_path, alias_pack):
    failing = tmp_path / "failing-omnigraph"
    failing.write_text("#!/bin/sh\necho 'bad token' >&2\nexit 3\n")
    failing.chmod(0o755)

    with pytest.raises(subprocess.CalledProcessError):
        install_shim(tmp_path / ".omnigraph-home", alias_pack, failing, "reader-token")


# ── the shim the agent actually runs ────────────────────────────────────────


def test_shim_runs_the_real_cli_with_the_bench_home_and_nothing_inherited(
    tmp_path, alias_pack, fake_omnigraph, monkeypatch
):
    monkeypatch.setenv("FAKE_RECORD", str(tmp_path / "login.json"))
    home = tmp_path / ".omnigraph-home"
    install_shim(home, alias_pack, fake_omnigraph, "reader-token")
    (tmp_path / "bin").mkdir()
    shim = tmp_path / "bin" / "omnigraph"
    shutil.copy2(SHIM, shim)
    hostile = {
        "PATH": "/usr/bin:/bin",
        "FAKE_RECORD": str(tmp_path / "shim.json"),
        "OMNIGRAPH_HOME": "/Users/someone/.omnigraph",
        "OMNIGRAPH_PROFILE": "prod",
        "OMNIGRAPH_BEARER_TOKEN": "analyst-token",
        "OMNIGRAPH_CONTROL_API": "https://control.example",
        "AWS_SECRET_ACCESS_KEY": "aws-secret",
        "TOKEN_ACT_ADMIN": "admin-token",
        "GEMINI_API_KEY": "gemini-key",
    }

    subprocess.run(
        [str(shim), "alias", "hybrid-search", "give the agent a budget, not a token"],
        env=hostile,
        input="",
        check=True,
    )

    run = recorded(tmp_path / "shim.json")
    assert run["argv"] == ["alias", "hybrid-search", "give the agent a budget, not a token"]
    assert run["env"] == {"OMNIGRAPH_HOME": str(home), "OMNIGRAPH_PROFILE": "intel"}


# ── the environment the benchmark runs in ───────────────────────────────────


def test_graph_secrets_in_flags_credentials_the_agent_could_reach():
    environ = {
        "PATH": "/usr/bin",
        "HOME": "/Users/me",
        "ANTHROPIC_API_KEY": "needed-by-the-sdk",
        "OMNIGRAPH_PROFILE": "intel",
        "MY_AWS_NOTES": "not a credential",
        "AWS_ACCESS_KEY_ID": "x",
        "AWS_SECRET_ACCESS_KEY": "x",
        "TOKEN_ACT_ANALYST": "x",
        "OMNIGRAPH_SERVER_BEARER_TOKENS_JSON": "x",
        "OMNIGRAPH_BEARER_TOKEN": "x",
        "OMNIGRAPH_CONTROL_API": "x",
        "GEMINI_API_KEY": "x",
    }

    assert graph_secrets_in(environ) == [
        "AWS_ACCESS_KEY_ID",
        "AWS_SECRET_ACCESS_KEY",
        "GEMINI_API_KEY",
        "OMNIGRAPH_BEARER_TOKEN",
        "OMNIGRAPH_CONTROL_API",
        "OMNIGRAPH_SERVER_BEARER_TOKENS_JSON",
        "TOKEN_ACT_ANALYST",
    ]


def test_graph_secrets_in_a_clean_environment_is_empty():
    assert graph_secrets_in({"PATH": "/usr/bin", "ANTHROPIC_API_KEY": "x"}) == []


# ── `bench shim` ────────────────────────────────────────────────────────────


def shim_command(tmp_path, alias_pack, fake_omnigraph):
    return [
        "shim",
        "--home",
        str(tmp_path / ".omnigraph-home"),
        "--alias-pack",
        str(alias_pack),
        "--omnigraph",
        str(fake_omnigraph),
    ]


def test_shim_command_installs_without_echoing_the_token(
    tmp_path, alias_pack, fake_omnigraph, monkeypatch, capsys
):
    monkeypatch.setenv("FAKE_RECORD", str(tmp_path / "login.json"))
    monkeypatch.setattr(sys, "stdin", io.StringIO("reader-token\n"))

    code = main(shim_command(tmp_path, alias_pack, fake_omnigraph))

    assert code == 0
    assert recorded(tmp_path / "login.json")["stdin"] == "reader-token"
    out = capsys.readouterr()
    assert "reader-token" not in out.out + out.err


def test_shim_command_refuses_an_empty_token(
    tmp_path, alias_pack, fake_omnigraph, monkeypatch, capsys
):
    monkeypatch.setattr(sys, "stdin", io.StringIO("\n"))

    with pytest.raises(SystemExit) as exit_:
        main(shim_command(tmp_path, alias_pack, fake_omnigraph))

    assert exit_.value.code != 0
    assert "act-reader token" in capsys.readouterr().err
    assert not (tmp_path / ".omnigraph-home").exists()
