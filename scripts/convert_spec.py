#!/usr/bin/env python3
"""Turn the Plex OpenAPI spec into the JSON the generator reads.

Plex publishes no spec of its own; `LukeHagar/plex-api-spec` is the community
one its official SDKs are generated from. Two things need handling. It is 2.5 MB
of response schemas, of which the generator reads only paths, methods,
summaries and parameters. And it spans two different API families: the media
server itself, and the plex.tv cloud services. Each operation records which one
it belongs to as `x-plex-host`, so the client can send it to the right place.

    python scripts/convert_spec.py plex-api-spec.yaml openapi.json
"""

import json
import sys

import yaml

# The templated server URL is the user's own Plex Media Server; everything else
# is an absolute cloud endpoint.
SERVER_MARKER = "plex.direct"


def host_of(operation: dict, path_item: dict, spec: dict) -> str:
    servers = operation.get("servers") or path_item.get("servers") or spec.get("servers")
    if not servers:
        return "server"
    url = servers[0].get("url", "")
    return "server" if SERVER_MARKER in url else url.rstrip("/")


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2

    with open(sys.argv[1]) as handle:
        spec = yaml.safe_load(handle)

    slim: dict = {
        "openapi": spec.get("openapi", "3.1.0"),
        "info": spec.get("info", {}),
        "paths": {},
    }

    for path, path_item in spec["paths"].items():
        for method, operation in path_item.items():
            if method not in ("get", "post", "put", "delete", "patch"):
                continue

            parameters = []
            for parameter in operation.get("parameters") or []:
                if "$ref" in parameter:
                    continue
                kept = {
                    k: v
                    for k, v in parameter.items()
                    if k in ("name", "in", "required", "description", "schema")
                }
                # Plex sends its auth headers for us; they are not tool inputs.
                if kept.get("name", "").startswith("X-Plex"):
                    continue
                if kept.get("in") == "header":
                    continue
                schema = kept.get("schema") or {}
                kept["schema"] = {"type": schema.get("type", "string")}
                parameters.append(kept)

            entry = {
                "summary": (operation.get("summary") or "").strip(),
                "tags": operation.get("tags") or [],
                "parameters": parameters,
                "x-plex-host": host_of(operation, path_item, spec),
            }
            if operation.get("requestBody"):
                entry["requestBody"] = {
                    "required": operation["requestBody"].get("required", False),
                    "content": {"application/json": {"schema": {"type": "object"}}},
                }
            slim["paths"].setdefault(path, {})[method] = entry

    with open(sys.argv[2], "w") as handle:
        json.dump(slim, handle, indent=1)

    operations = sum(len(m) for m in slim["paths"].values())
    cloud = sum(
        1
        for m in slim["paths"].values()
        for op in m.values()
        if op["x-plex-host"] != "server"
    )
    print(
        f"{len(slim['paths'])} paths, {operations} operations "
        f"({operations - cloud} on the media server, {cloud} on plex.tv) "
        f"-> {sys.argv[2]}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
