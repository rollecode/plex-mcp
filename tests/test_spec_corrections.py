import json
import pathlib

from plex_mcp import tools

SPEC = json.loads((pathlib.Path(__file__).parent.parent / "openapi.json").read_text())


def test_watchlist_actions_use_put_with_rating_key():
    for path in ("/actions/addToWatchlist", "/actions/removeFromWatchlist"):
        methods = SPEC["paths"][path]
        assert list(methods) == ["put"]
        names = [p["name"] for p in methods["put"]["parameters"]]
        assert names == ["ratingKey"]


def test_watchlist_tool_sends_rating_key(monkeypatch):
    sent = {}

    def fake_call(method, path, **kwargs):
        sent.update(method=method, path=path, query=kwargs.get("query"))
        return "{}"

    monkeypatch.setattr(tools, "call", fake_call)
    tools.update_actions_add_to_watchlist(rating_key="656edbdc19dba549ab5f818d")
    assert sent == {
        "method": "PUT",
        "path": "/actions/addToWatchlist",
        "query": {"ratingKey": "656edbdc19dba549ab5f818d"},
    }
