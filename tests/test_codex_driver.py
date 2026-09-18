from aegis.config import Agent
from aegis.drivers import DRIVERS
from aegis.drivers.codex import CodexDriver


WD = "/tmp/wd"
MCP_URL = "http://127.0.0.1:9/mcp/"


def test_registry_has_codex():
    assert DRIVERS["codex"] is CodexDriver


def test_argv_without_model_is_bare_base_cmd():
    agent = Agent(harness="codex", model="")
    argv = CodexDriver().build_argv(agent, WD, MCP_URL, "h")
    assert argv == ["codex-acp"]


def test_argv_passes_model_through_dash_c_toml_override():
    agent = Agent(harness="codex", model="gpt-5.1-codex")
    argv = CodexDriver().build_argv(agent, WD, MCP_URL, "h")
    assert argv == ["codex-acp", "-c", 'model="gpt-5.1-codex"']
