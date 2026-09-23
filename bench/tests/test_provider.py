import pytest

from bench.provider import cost_usd, openrouter_env, session_cost


def test_openrouter_env_points_the_cli_at_openrouter(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("# keys\nOTHER=1\nOPENROUTER_KEY=test-openrouter-key\n")

    assert openrouter_env(env_file) == {
        "ANTHROPIC_BASE_URL": "https://openrouter.ai/api",
        "ANTHROPIC_AUTH_TOKEN": "test-openrouter-key",
        "ANTHROPIC_API_KEY": "",
    }


def test_openrouter_env_accepts_quoted_values(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text('OPENROUTER_KEY="test-quoted-key"\n')

    assert openrouter_env(env_file)["ANTHROPIC_AUTH_TOKEN"] == "test-quoted-key"


def test_openrouter_env_without_a_key_is_an_error(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("OPENROUTER_KEY=\n")

    with pytest.raises(ValueError, match="OPENROUTER_KEY"):
        openrouter_env(env_file)


def test_cost_prices_every_token_kind_for_sonnet():
    usage = {
        "input_tokens": 1_000_000,
        "output_tokens": 100_000,
        "cache_read_input_tokens": 2_000_000,
        "cache_creation_input_tokens": 400_000,
    }

    # 1M × $2 + 0.1M × $10 + 2M × $0.20 + 0.4M × $2.50
    assert cost_usd("anthropic/claude-sonnet-5", usage) == pytest.approx(2 + 1 + 0.4 + 1)


def test_cost_uses_the_judge_model_prices():
    usage = {"input_tokens": 500_000, "output_tokens": 50_000}

    # 0.5M × $4 + 0.05M × $20
    assert cost_usd("anthropic/claude-opus-5.5", usage) == pytest.approx(2 + 1)


def test_cost_of_an_unpriced_model_is_an_error():
    with pytest.raises(KeyError):
        cost_usd("anthropic/claude-haiku-4.5", {"input_tokens": 1})


def test_session_cost_prices_the_cli_model_usage_like_the_sdk_does():
    # model_usage from the 2026-09-23 markdown probe; the SDK reported $0.0307594
    model_usage = {
        "anthropic/claude-sonnet-5": {
            "inputTokens": 1533,
            "outputTokens": 615,
            "cacheReadInputTokens": 44567,
            "cacheCreationInputTokens": 5052,
            "costUSD": 0.0307594,
        }
    }

    assert session_cost(model_usage) == pytest.approx(0.0307594)


def test_session_cost_adds_up_every_model_in_the_session():
    model_usage = {
        "anthropic/claude-sonnet-5": {"inputTokens": 1_000_000, "outputTokens": 0},
        "anthropic/claude-opus-5.5": {"inputTokens": 0, "outputTokens": 100_000},
    }

    assert session_cost(model_usage) == pytest.approx(2.0 + 2.0)
