<center align="center" style="text-align: center;justify-content:center;">
<div align="center" style="text-align: center;justify-content:center;">
<h1 align="center" style="text-align: center;justify-content:center;">

Plex MCP server

<img style="justify-content:center;text-align: center;width: 95px; height: auto;" width="793" height="411" alt="image" src="https://github.com/user-attachments/assets/abed1a04-d69b-4ab4-a490-d606064df72d" />
<img style="justify-content:center;text-align: center;width: 49px; height: auto;" alt="Plex" src="public/logo.png" />

</h1>


![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Plex](https://img.shields.io/badge/Plex-E5A00D?style=for-the-badge&logo=plex&logoColor=white) ![Coverage](https://img.shields.io/badge/API_coverage-405%2F405-brightgreen?style=for-the-badge)

</div>
</center>

<hr>

Run Plex from Claude.ai and Claude Code. All 405 operations are tools: 353 on your media server and 52 on the plex.tv cloud services, each routed to the right host automatically. Not a curated subset.

<hr>

## Why not the other options

Measured against the community spec Plex's own SDKs are generated from, which has 344 paths and 405 operations:

| Server | Plex tools | Coverage |
| --- | --- | --- |
| `niavasha/plex-mcp-server` | ~40 | 10 % |
| `tdabasinskas/plex-mcp-server` | libraries, playlists, clients | partial |
| `eddmann/plex-mcp` | viewing context and subtitles | partial |
| This one | **405** | **100 %** |

The existing servers cover libraries, playlists and what is playing. None of them reach the transcoder, the hub and discovery endpoints, butler tasks, server settings, sync, or the plex.tv side at all: watchlist, sharing, devices and account.

## How it stays complete

Plex publishes no OpenAPI document. [`LukeHagar/plex-api-spec`](https://github.com/LukeHagar/plex-api-spec) is the community one Plex's own SDKs are generated from; `scripts/convert_spec.py` slims its 2.5 MB down to what the generator reads and records which host each operation belongs to:

```bash
curl -o plex-api-spec.yaml https://raw.githubusercontent.com/LukeHagar/plex-api-spec/main/plex-api-spec.yaml
python scripts/convert_spec.py plex-api-spec.yaml openapi.json
python scripts/generate_tools.py openapi.json src/plex_mcp/tools.py
```

A test compares every generated call against every operation in the spec, in both directions. An endpoint Plex adds and this misses fails the build; so does a tool pointing at an endpoint the spec does not define.

## Tool names

Verb first, derived from the method and path, so the name says what it does:

| Pattern | Meaning | Example |
| --- | --- | --- |
| `list_*` | Read a collection | `list_library_sections`, `list_status_sessions` |
| `get_*_by_id` | Read one record | `get_library_metadata_by_rating_key` |
| `create_*` | POST | `create_playlists`, `create_library_sections` |
| `update_*` | PUT | `update_playlists_by_playlist_id` |
| `delete_*` | DELETE | `delete_playlists_by_playlist_id` |

405 tools is a lot to put in front of a model at once. If your client supports tool filtering, narrow it to the groups you use.

## Two APIs, one server

Plex splits across the media server and the plex.tv cloud. The spec records which host each operation belongs to and the client routes on it, so a watchlist call reaches plex.tv while a library call reaches your server:

| Host | Operations |
| --- | --- |
| Your media server | 353 |
| `plex.tv/api/v2` | 27 |
| `plex.tv/api` | 11 |
| `plex.tv` | 6 |
| `discover.provider.plex.tv` | 4 |
| `clients.plex.tv/api/v2` | 4 |

## What is covered

`Activities`, `Authentication`, `Butler`, `Collections`, `Content`, `DVRs`, `Devices`, `Download Queue`, `EPG`, `Events`, `General`, `Hubs`, `Library`, `Library Collections`, `Library Playlists`, `Live TV`, `Log`, `Play Queue`, `Playback`, `Playlist`, `Playlists`, `Plex`, `Preferences`, `Provider`, `Rate`, `Search`, `Status`, `Subscriptions`, `Timeline`, `Transcoder`, `UltraBlur`, `Updater`, `Users`.

## Setup

```bash
git clone https://github.com/rollecode/plex-mcp.git
cd plex-mcp
uv venv && uv pip install -e .
```

```bash
export PLEX_URL=http://127.0.0.1:32400
export PLEX_TOKEN=...   # see below
```

Find the token by opening any item in the Plex web app, choosing Get Info, then View XML: it is the `X-Plex-Token` in the address bar.

### Claude Code

```bash
claude mcp add plex -- /path/to/plex-mcp/.venv/bin/plex-mcp
```

## Notes

Plex answers in XML unless asked for JSON, which the client does; a few endpoints ignore that and their raw XML comes back as text. Rating keys identify items, section keys identify libraries.

## Hosting it

Running it over HTTP puts it in reach of Claude.ai as a custom connector, and of Claude Code on other machines. Three tiers, the same shape the other servers in this family use:

| Tier | Port | What it does |
| --- | --- | --- |
| `plex-mcp` | 8590 | The server. No login of its own, never exposed |
| nginx | 8591 | Front door, behind a Cloudflare Tunnel |
| `auth-server.js` | 8592 | OAuth 2.1 sign-in, or a fixed bearer token |

```bash
npm install
node set-password.js 'a password for the sign-in page'
printf 'PLEX_URL=...\nPLEX_TOKEN=...\n' > ~/.config/plex-mcp/env
chmod 600 ~/.config/plex-mcp/env
```

Copy `systemd/*.service` into `/etc/systemd/system/`, replacing `YOUR_USER` and the `ISSUER` hostname, then:

```bash
sudo systemctl enable --now plex-mcp plex-mcp-auth
```

Point `nginx/plex-mcp.conf` at your own hostname and send the tunnel at `127.0.0.1:8591`.

### Claude.ai

Settings, Connectors, Add custom connector, URL `https://plex-mcp.your-domain/mcp`, client ID and secret blank. The sign-in page asks for the password set above.

## Development

```bash
uv pip install -e . pytest ruff
.venv/bin/python -m pytest tests
.venv/bin/ruff check .
```

