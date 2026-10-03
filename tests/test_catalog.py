import asyncio
import json

import httpx
import pytest

from plex_mcp import catalog, runtime, tools


@pytest.fixture(autouse=True)
def reset(monkeypatch, tmp_path):
    monkeypatch.setenv("PLEX_TOKEN", "tok")
    monkeypatch.setenv("PLEX_URL", "http://plex.test:32400")
    monkeypatch.setattr(runtime, "_IDENTITY_PATH", tmp_path / "client-id")
    runtime._clients = {}
    yield
    runtime._clients = {}


def test_few_tools_reach_every_operation():
    exposed = {t.name for t in asyncio.run(runtime.mcp.list_tools())}
    assert len(exposed) <= 30
    assert {"find_operation", "run_operation", "get_result_page"} <= exposed
    generated = {n for n, f in vars(tools).items() if callable(f) and getattr(f, "__module__", "") == tools.__name__}
    assert generated == set(runtime.OPERATIONS)
    assert len(generated) == 405


def test_core_tools_are_real_operations():
    assert set(catalog.CORE) <= set(runtime.OPERATIONS)


def test_find_operation_ranks_by_the_words_given():
    found = json.loads(catalog.find_operation("add to watchlist"))["operations"]
    assert found[0]["name"] == "update_actions_add_to_watchlist"
    assert "rating_key" in found[0]["arguments"]


def test_run_operation_calls_the_api():
    seen = {}

    def handler(request):
        seen["path"] = request.url.path
        return httpx.Response(200, json={"MediaContainer": {"size": 0}})

    runtime._clients["http://plex.test:32400"] = httpx.Client(
        base_url="http://plex.test:32400", transport=httpx.MockTransport(handler)
    )
    out = json.loads(catalog.run_operation("list_butler"))
    assert out["status"] == "success"
    assert seen["path"] == "/butler"


def test_run_operation_explains_mistakes():
    assert "find_operation" in json.loads(catalog.run_operation("no_such_thing"))["message"]
    bad = json.loads(catalog.run_operation("update_actions_add_to_watchlist", {"nope": 1}))
    assert bad["status"] == "error" and "rating_key" in bad["message"]
