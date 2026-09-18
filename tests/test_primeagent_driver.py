from aegis.config import Agent
from aegis.drivers import DRIVERS
from aegis.drivers.primeagent import PrimeAgentDriver


WD = "/tmp/wd"
MCP_URL = "http://127.0.0.1:9/mcp/"


def test_registry_has_prime_agent():
    assert DRIVERS["prime-agent"] is PrimeAgentDriver


def test_argv_without_model_is_bare_base_cmd():
    agent = Agent(harness="prime-agent", model="")
    argv = PrimeAgentDriver().build_argv(agent, WD, MCP_URL, "h")
    assert argv == ["prime-agent", "--mode", "acp"]


def test_argv_passes_model_through_dash_dash_model():
    agent = Agent(harness="prime-agent", model="glm-5.1")
    argv = PrimeAgentDriver().build_argv(agent, WD, MCP_URL, "h")
    assert argv == ["prime-agent", "--mode", "acp", "--model", "glm-5.1"]
