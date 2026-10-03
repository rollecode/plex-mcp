"""The tools a client actually sees.

405 tool definitions overflow the context of clients such as Claude Desktop
before a question is even asked. So a core set of everyday operations is
exposed directly, and every other operation stays reachable by name through
find_operation and run_operation.
"""

import inspect
import json
import re

from . import tools  # noqa: F401 -- importing fills OPERATIONS
from .runtime import _DESTRUCTIVE, _READ, OPERATIONS, mcp

CORE = (
    "list_library_sections",
    "get_library_sections_by_section_id_all",
    "get_library_sections_by_section_id_unwatched",
    "get_library_sections_by_section_id_collections",
    "get_library_collections_by_collection_id_items",
    "list_hubs_search",
    "get_library_metadata_by_ids",
    "get_library_metadata_by_id_children",
    "get_library_metadata_by_ids_similar",
    "list_library_recently_added",
    "list_hubs_continue_watching_items",
    "list_status_sessions",
    "list_status_sessions_history_all",
    "list_playlists",
    "get_playlists_by_playlist_id_items",
    "create_playlists",
    "update_playlists_by_playlist_id_items",
    "update_scrobble",
    "update_unscrobble",
    "update_rate",
    "create_library_sections_by_section_id_refresh",
    "list_library_sections_watchlist_all",
    "create_actions_add_to_watchlist",
    "create_actions_remove_from_watchlist",
    "list_identity",
)

for _name in CORE:
    _fn, _annotations = OPERATIONS[_name]
    mcp.tool(annotations=_annotations)(_fn)


def _words(text: str) -> list[str]:
    return [w for w in re.split(r"[\W_]+", text.lower()) if len(w) > 2]


def _describe(name: str) -> dict:
    fn, annotations = OPERATIONS[name]
    doc = inspect.getdoc(fn) or ""
    summary, _, rest = doc.partition("\n\n")
    route, _, args = rest.partition("Args:")
    return {
        "name": name,
        "route": route.strip(),
        "summary": summary.strip(),
        "read_only": annotations is _READ,
        "arguments": inspect.cleandoc(args) if args else "",
    }


@mcp.tool(annotations=_READ)
def find_operation(query: str, limit: int = 8) -> str:
    """Search all 405 Plex API operations, including those not exposed as tools.

    Returns each match's name, route, summary and arguments. Run one with
    run_operation.

    Args:
        query: Words describing what you want, such as "delete playlist item",
            "butler tasks" or "transcode sessions".
        limit: How many matches to return.
    """
    words = set(_words(query))
    scored = []
    for name, (fn, _) in OPERATIONS.items():
        in_name, in_doc = set(_words(name)), set(_words(inspect.getdoc(fn) or ""))
        score = sum(3 if w in in_name else 1 if w in in_doc else 0 for w in words)
        if score:
            scored.append((-score, len(name), name))
    found = [_describe(name) for *_, name in sorted(scored)[:limit]]
    return json.dumps({"status": "success", "operations": found}, ensure_ascii=False)


@mcp.tool(annotations=_DESTRUCTIVE)
def run_operation(name: str, arguments: dict | None = None) -> str:
    """Run any Plex API operation by name, as found with find_operation.

    Some operations change or delete things; check `read_only` in the
    find_operation result before running one the user did not ask for.

    Args:
        name: Operation name from find_operation.
        arguments: Its arguments as listed there, by name.
    """
    if name not in OPERATIONS:
        return json.dumps({
            "status": "error",
            "message": f"No operation named {name!r}. Search with find_operation first.",
        })
    fn, _ = OPERATIONS[name]
    try:
        inspect.signature(fn).bind(**(arguments or {}))
    except TypeError as e:
        return json.dumps({
            "status": "error",
            "message": f"{e}. {name} takes: {inspect.signature(fn)}",
        })
    return fn(**(arguments or {}))
