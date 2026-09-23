import asyncio
import os

import pytest

from bench.arms import (
    gate_hook,
    markdown_gate,
    markdown_options,
    omnigraph_gate,
    omnigraph_options,
)


@pytest.fixture
def talks(tmp_path):
    root = tmp_path / "markdown" / "talks"
    root.mkdir(parents=True)
    (root / "ia-aie-alpha-talk.md").write_text("# Alpha\n")
    (tmp_path / "secret.md").write_text("outside")
    return root


@pytest.fixture
def scratch(tmp_path):
    root = tmp_path / "omnigraph"
    root.mkdir()
    return root


# ── markdown arm: Read / Grep / Glob inside the talks dir only ──────────────


@pytest.mark.parametrize(
    "tool, tool_input",
    [
        ("Read", {"file_path": "{root}/ia-aie-alpha-talk.md"}),
        ("Read", {"file_path": "ia-aie-alpha-talk.md", "offset": 10, "limit": 50}),
        ("Grep", {"pattern": "verif", "output_mode": "count"}),
        ("Grep", {"pattern": "memory", "path": "{root}", "glob": "*.md"}),
        ("Glob", {"pattern": "*.md"}),
        ("Glob", {"pattern": "ia-aie-*.md", "path": "{root}"}),
    ],
)
def test_markdown_gate_allows_reading_the_talks(talks, tool, tool_input):
    tool_input = {
        k: v.format(root=talks) if isinstance(v, str) else v for k, v in tool_input.items()
    }

    assert markdown_gate(talks)(tool, tool_input) is None


@pytest.mark.parametrize(
    "tool, tool_input",
    [
        ("Read", {"file_path": "../../secret.md"}),
        ("Read", {"file_path": "{parent}/secret.md"}),
        ("Read", {"file_path": "/etc/passwd"}),
        ("Read", {"file_path": "~/.claude/CLAUDE.md"}),
        ("Grep", {"pattern": "x", "path": "{parent}"}),
        ("Grep", {"pattern": "x", "glob": "../**/*.md"}),
        ("Glob", {"pattern": "../**/*.md"}),
        ("Glob", {"pattern": "/Users/**/*.md"}),
        ("Glob", {"pattern": "*.md", "path": "/"}),
        ("Bash", {"command": "cat ia-aie-alpha-talk.md"}),
        ("Write", {"file_path": "{root}/new.md", "content": "x"}),
        ("WebFetch", {"url": "https://example.com", "prompt": "x"}),
        ("Agent", {"prompt": "read everything", "description": "fan out"}),
    ],
)
def test_markdown_gate_denies_everything_else(talks, tool, tool_input):
    parent = talks.parent.parent
    tool_input = {k: v.format(root=talks, parent=parent) for k, v in tool_input.items()}

    reason = markdown_gate(talks)(tool, tool_input)

    assert isinstance(reason, str) and reason


def test_markdown_gate_denies_a_symlink_that_points_outside(talks):
    (talks / "sneaky.md").symlink_to(talks.parent.parent / "secret.md")

    assert markdown_gate(talks)("Read", {"file_path": str(talks / "sneaky.md")})


# ── omnigraph arm: stored queries through the CLI, nothing else ─────────────


@pytest.mark.parametrize(
    "command",
    [
        "omnigraph alias top-patterns",
        "omnigraph alias pattern-signals pat-context-graphs --format kv",
        'omnigraph alias hybrid-search "give the agent a budget, not a token"',
        "omnigraph alias talk-semantic ia-aie-krieger-anthropic-how-anthropic-builds "
        "'how do they decide what to unship'",
        "omnigraph query top_patterns_by_signals --profile intel",
        """omnigraph query signals_by_domain --params '{"domain": "security"}'""",
        "omnigraph alias --help",
    ],
)
def test_omnigraph_gate_allows_stored_queries(scratch, command):
    assert omnigraph_gate(scratch)("Bash", {"command": command}) is None


@pytest.mark.parametrize(
    "command",
    [
        # other verbs and other programs
        "omnigraph mutate add_signal --params '{}'",
        "omnigraph export --server intel-local --graph spike",
        "cat ia-aie-alpha-talk.md",
        "OMNIGRAPH_PROFILE=x omnigraph alias top-patterns",
        # ad-hoc queries, direct store access, other identities, files on disk
        "omnigraph query -e 'query q() { match { $s: Signal } return { $s.slug } }'",
        "omnigraph query q --query-string='query q() {}'",
        "omnigraph query q --query /tmp/q.gq",
        "omnigraph query top_patterns_by_signals --store s3://intel-graph/x",
        "omnigraph alias top-patterns --direct",
        "omnigraph alias top-patterns --as act-admin",
        "omnigraph query signals_by_domain --params-file /etc/passwd",
        "omnigraph query top_patterns_by_signals --branch scratch",
        # shell plumbing
        "omnigraph alias top-patterns; ls",
        "omnigraph alias top-patterns && cat /etc/passwd",
        "omnigraph alias top-patterns | head",
        "omnigraph alias top-patterns > out.txt",
        "omnigraph alias hybrid-search $(cat secret.md)",
        "omnigraph alias hybrid-search `cat secret.md`",
        "omnigraph alias top-patterns\nls",
        'omnigraph alias hybrid-search "unbalanced',
    ],
)
def test_omnigraph_gate_denies_anything_but_stored_queries(scratch, command):
    reason = omnigraph_gate(scratch)("Bash", {"command": command})

    assert isinstance(reason, str) and reason


def test_omnigraph_gate_denies_background_commands(scratch):
    tool_input = {"command": "omnigraph alias top-patterns", "run_in_background": True}

    assert omnigraph_gate(scratch)("Bash", tool_input)


def test_omnigraph_gate_reads_only_its_own_scratch_dir(scratch, tmp_path):
    (scratch / "output.txt").write_text("spilled tool output")
    gate = omnigraph_gate(scratch)

    assert gate("Read", {"file_path": str(scratch / "output.txt")}) is None
    assert gate("Read", {"file_path": str(tmp_path / "markdown" / "talks" / "x.md")})
    assert gate("Grep", {"pattern": "x"})
    assert gate("Glob", {"pattern": "*"})


# ── hook wiring: the shape the CLI reads from a PreToolUse hook ─────────────


def run_hook(matcher, tool_name, tool_input):
    callback = matcher.hooks[0]
    hook_input = {
        "hook_event_name": "PreToolUse",
        "session_id": "s",
        "transcript_path": "/tmp/t.jsonl",
        "cwd": "/tmp",
        "tool_name": tool_name,
        "tool_input": tool_input,
        "tool_use_id": "toolu_1",
    }
    return asyncio.run(callback(hook_input, "toolu_1", {"signal": None}))


def test_gate_hook_returns_an_explicit_allow(talks):
    out = run_hook(gate_hook(markdown_gate(talks)), "Glob", {"pattern": "*.md"})

    assert out["hookSpecificOutput"]["hookEventName"] == "PreToolUse"
    assert out["hookSpecificOutput"]["permissionDecision"] == "allow"


def test_gate_hook_returns_a_deny_with_the_reason(talks):
    out = run_hook(gate_hook(markdown_gate(talks)), "Read", {"file_path": "/etc/passwd"})

    assert out["hookSpecificOutput"]["permissionDecision"] == "deny"
    assert "/etc/passwd" in out["hookSpecificOutput"]["permissionDecisionReason"]


# ── options: symmetric arms, isolated from settings, MCP, skills, subagents ─


SHARED = [
    "model",
    "effort",
    "max_turns",
    "max_budget_usd",
    "setting_sources",
    "strict_mcp_config",
    "allowed_tools",
    "mcp_servers",
    "plugins",
    "skills",
    "agents",
    "permission_mode",
]


def test_arms_differ_only_in_tools_workdir_and_prompt(talks, scratch, tmp_path):
    md = markdown_options(talks, "MD")
    og = omnigraph_options(scratch, "OG", shim_bin=tmp_path / "bin")

    assert {f: getattr(md, f) for f in SHARED} == {f: getattr(og, f) for f in SHARED}
    assert (md.tools, md.cwd, md.system_prompt) == (["Read", "Grep", "Glob"], talks, "MD")
    assert (og.tools, og.cwd, og.system_prompt) == (["Bash", "Read"], scratch, "OG")


def test_arms_load_no_settings_mcp_or_preapproved_tools(talks):
    md = markdown_options(talks, "MD")

    assert md.model == "claude-sonnet-5"
    assert md.setting_sources == []
    assert md.strict_mcp_config is True
    assert md.allowed_tools == []
    assert md.agents is None
    assert md.can_use_tool is not None
    assert list(md.hooks) == ["PreToolUse"]


def test_omnigraph_arm_finds_the_shim_first_on_path(scratch, tmp_path):
    og = omnigraph_options(scratch, "OG", shim_bin=tmp_path / "bin")

    assert og.env["PATH"].split(os.pathsep)[0] == str(tmp_path / "bin")


def test_anything_reaching_the_permission_prompt_is_denied(talks):
    md = markdown_options(talks, "MD")

    result = asyncio.run(md.can_use_tool("Read", {"file_path": "x"}, None))

    assert result.behavior == "deny"
