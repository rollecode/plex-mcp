"""Server instance, client and the call helper every generated tool uses."""

import importlib.metadata
import json
import logging
import os
import uuid
from pathlib import Path

import httpx
from mcp.server.fastmcp import FastMCP
from mcp.types import Icon

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

APP = "plex"
TITLE = "Plex"
ENV_URL = "PLEX_URL"
ENV_TOKEN = "PLEX_TOKEN"
DEFAULT_URL = "http://127.0.0.1:32400"
DEFAULT_PORT = 8590

# Plex refuses requests without a stable client identity, and hands out a
# device entry per identifier, so it is generated once and kept.
_IDENTITY_PATH = (
    Path(os.getenv("XDG_CACHE_HOME") or Path.home() / ".cache")
    / "plex-mcp"
    / "client-id"
)

PRODUCT = "plex-mcp"
DEVICE = "Claude"

try:
    __version__ = importlib.metadata.version(f"{APP}-mcp")
except importlib.metadata.PackageNotFoundError:  # running from a source tree
    __version__ = "0.0.0"

_ICON_BASE = os.getenv("MCP_PUBLIC_URL", "").rstrip("/")
_ICON_SIZES = (48, 96, 256)

mcp = FastMCP(
    APP,
    icons=(
        [
            Icon(
                src=f"{_ICON_BASE}/icon.png"
                if size == 256
                else f"{_ICON_BASE}/icon-{size}.png",
                mimeType="image/png",
                sizes=[f"{size}x{size}"],
            )
            for size in _ICON_SIZES
        ]
        if _ICON_BASE
        else None
    ),
    website_url=_ICON_BASE or None,
    instructions=(
        "Manage a Plex Media Server: libraries and their contents, playlists, "
        "collections, hubs, search, sessions and playback, transcoding, "
        "watchlists, users and server settings. Every operation is a tool, "
        "named verb-first: list_* and get_* read, create_*, update_* and "
        "delete_* change. "
        "Start with list_library_sections to get a section key, then "
        "list_library_sections_by_section_key_all to browse it. Ratings keys "
        "identify items. Tools whose path starts with a plex.tv host act on "
        "the account rather than the server, so they work even when the "
        "server is unreachable."
    ),
)

mcp._mcp_server.version = __version__

_READ = {
    "readOnlyHint": True,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": True,
}
_WRITE = {
    "readOnlyHint": False,
    "destructiveHint": False,
    "idempotentHint": True,
    "openWorldHint": True,
}
_DESTRUCTIVE = {**_WRITE, "destructiveHint": True}

_clients: dict[str, httpx.Client] = {}


def client_identifier() -> str:
    try:
        return _IDENTITY_PATH.read_text().strip()
    except OSError:
        identifier = str(uuid.uuid4())
        _IDENTITY_PATH.parent.mkdir(parents=True, exist_ok=True)
        _IDENTITY_PATH.write_text(identifier)
        return identifier


def _headers() -> dict[str, str]:
    token = os.getenv(ENV_TOKEN)
    if not token:
        raise RuntimeError(
            f"{ENV_TOKEN} is not set. Find it by opening any item in the Plex "
            "web app, choosing Get Info, then View XML: the token is the "
            "X-Plex-Token in the address bar."
        )
    return {
        "X-Plex-Token": token,
        "X-Plex-Client-Identifier": client_identifier(),
        "X-Plex-Product": PRODUCT,
        "X-Plex-Device": DEVICE,
        "X-Plex-Version": __version__,
        # Plex speaks XML by default and JSON only when asked.
        "Accept": "application/json",
    }


def _client(host: str) -> httpx.Client:
    """One client per host, since operations span the server and plex.tv."""
    base = (os.getenv(ENV_URL) or DEFAULT_URL).rstrip("/") if host == "server" else host
    if base not in _clients:
        _clients[base] = httpx.Client(
            base_url=base,
            headers=_headers(),
            timeout=httpx.Timeout(300.0, connect=15.0),
            follow_redirects=True,
        )
    return _clients[base]


def _err(e: Exception) -> str:
    if isinstance(e, httpx.HTTPStatusError):
        status = e.response.status_code
        hints = {
            401: f"{TITLE} rejected the token. Check {ENV_TOKEN}.",
            403: "Not allowed. This token belongs to a user without rights here.",
            404: "No such resource. Check the rating key or section key.",
        }
        msg = hints.get(status) or f"{TITLE} API error (HTTP {status}): {_detail(e.response)}"
    elif isinstance(e, httpx.ConnectError):
        msg = (
            f"Could not connect to {TITLE}. Check that the server is running "
            f"and {ENV_URL} points at it."
        )
    elif isinstance(e, httpx.TimeoutException):
        msg = f"Request timed out. {TITLE} may be busy -- try again."
    else:
        msg = f"{type(e).__name__}: {e}"

    return json.dumps({"status": "error", "message": msg})


def _detail(response: httpx.Response) -> str:
    try:
        return json.dumps(response.json())[:800]
    except ValueError:
        return response.text[:400]


def call(
    method: str,
    path: str,
    query: dict | None = None,
    body: dict | None = None,
    form: dict | None = None,
    host: str = "server",
) -> str:
    """Perform one API call and return its result as a JSON string.

    `host` says whether the operation belongs to the media server or to one of
    the plex.tv cloud services, which the spec records per operation.
    """
    try:
        params = {k: v for k, v in (query or {}).items() if v is not None}
        fields = {k: v for k, v in (form or {}).items() if v is not None}
        response = _client(host).request(
            method, path, params=params or None, json=body, data=fields or None
        )
        response.raise_for_status()

        if not response.content:
            return json.dumps({"status": "success", "result": None})
        try:
            return json.dumps(
                {"status": "success", "result": response.json()}, indent=2
            )
        except ValueError:
            # Some endpoints ignore the Accept header and answer in XML.
            return json.dumps({"status": "success", "result": response.text})
    except Exception as e:
        return _err(e)


def main() -> None:
    import argparse

    from dotenv import find_dotenv, load_dotenv

    from . import tools  # noqa: F401 -- importing registers every tool

    dotenv_path = find_dotenv(usecwd=True)
    if dotenv_path and load_dotenv(dotenv_path, override=False):
        logger.info("Loaded .env from %s", dotenv_path)

    parser = argparse.ArgumentParser(prog=f"{APP}-mcp")
    parser.add_argument(
        "--transport",
        choices=("stdio", "http"),
        default=os.getenv("MCP_TRANSPORT", "stdio"),
    )
    parser.add_argument("--host", default=os.getenv("MCP_HOST", "127.0.0.1"))
    parser.add_argument(
        "--port", type=int, default=int(os.getenv("MCP_PORT", str(DEFAULT_PORT)))
    )
    args = parser.parse_args()

    if args.transport == "stdio":
        mcp.run(transport="stdio")
        return

    if args.host not in ("127.0.0.1", "::1", "localhost"):
        raise SystemExit(
            f"refusing to listen on {args.host}: this server has no login of "
            "its own. Keep it on the local machine and put a proxy in front."
        )

    mcp.settings.host = args.host
    mcp.settings.port = args.port
    logger.info("Listening on http://%s:%d/mcp", args.host, args.port)
    mcp.run(transport="streamable-http")
