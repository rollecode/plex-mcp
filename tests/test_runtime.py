import json

import httpx
import pytest

from plex_mcp import runtime


@pytest.fixture(autouse=True)
def reset(monkeypatch, tmp_path):
    monkeypatch.setenv("PLEX_TOKEN", "tok")
    monkeypatch.setenv("PLEX_URL", "http://plex.test:32400")
    monkeypatch.setattr(runtime, "_IDENTITY_PATH", tmp_path / "client-id")
    runtime._clients = {}
    yield
    runtime._clients = {}


def install(handler, base="http://plex.test:32400"):
    runtime._clients[base] = httpx.Client(
        base_url=base,
        headers=runtime._headers(),
        transport=httpx.MockTransport(handler),
    )


def test_missing_token_says_where_to_find_it(monkeypatch):
    monkeypatch.delenv("PLEX_TOKEN", raising=False)
    result = json.loads(runtime.call("GET", "/library/sections"))
    assert result["status"] == "error"
    assert "PLEX_TOKEN" in result["message"]


def test_auth_headers_are_sent():
    seen = {}

    def handler(request):
        seen.update(request.headers)
        return httpx.Response(200, json={})

    install(handler)
    runtime.call("GET", "/library/sections")
    assert seen["x-plex-token"] == "tok"
    assert seen["x-plex-client-identifier"]
    assert seen["accept"] == "application/json"


def test_the_client_identifier_is_stable_across_calls():
    first = runtime.client_identifier()
    assert runtime.client_identifier() == first


def test_cloud_operations_go_to_plex_tv():
    seen = {}

    def handler(request):
        seen["url"] = str(request.url)
        return httpx.Response(200, json={})

    install(handler, base="https://plex.tv/api/v2")
    runtime.call("GET", "/user", host="https://plex.tv/api/v2")
    assert seen["url"].startswith("https://plex.tv/api/v2/user")


def test_server_operations_go_to_the_configured_server():
    seen = {}

    def handler(request):
        seen["url"] = str(request.url)
        return httpx.Response(200, json={})

    install(handler)
    runtime.call("GET", "/library/sections")
    assert seen["url"].startswith("http://plex.test:32400/library/sections")


def test_xml_responses_come_back_as_text():
    install(lambda request: httpx.Response(200, text="<MediaContainer/>"))
    assert json.loads(runtime.call("GET", "/"))["result"] == "<MediaContainer/>"


def test_a_bad_token_names_the_variable():
    install(lambda request: httpx.Response(401))
    assert "PLEX_TOKEN" in json.loads(runtime.call("GET", "/"))["message"]


def test_empty_body_is_success():
    install(lambda request: httpx.Response(204))
    assert json.loads(runtime.call("DELETE", "/playlists/1"))["result"] is None


def test_every_tool_registers():
    import asyncio

    from plex_mcp import tools  # noqa: F401 -- registers the tools

    assert len(asyncio.run(runtime.mcp.list_tools())) == 405
