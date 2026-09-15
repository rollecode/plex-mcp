"""Generated from the OpenAPI document. Do not edit by hand.

Regenerate with:

    python scripts/generate_tools.py openapi.json src/plex_mcp/tools.py

One tool per operation, 405 of them, covering the whole API.
"""

from .runtime import _DESTRUCTIVE, _READ, _WRITE, call, mcp


@mcp.tool(annotations=_WRITE)
def create_actions_add_to_watchlist(uri: str | None = None) -> str:
    """Add to Watchlist.

    POST /actions/addToWatchlist

    Args:
        uri: The URI of the item to add or remove
    """
    return call("POST", "/actions/addToWatchlist", query={"uri": uri}, body=None, form=None, host='https://discover.provider.plex.tv')


@mcp.tool(annotations=_WRITE)
def create_actions_remove_from_watchlist(uri: str | None = None) -> str:
    """Remove from Watchlist.

    POST /actions/removeFromWatchlist

    Args:
        uri: The URI of the item to add or remove
    """
    return call("POST", "/actions/removeFromWatchlist", query={"uri": uri}, body=None, form=None, host='https://discover.provider.plex.tv')


@mcp.tool(annotations=_WRITE)
def create_auth_jwk(body: dict) -> str:
    """Register Device JWK.

    POST /auth/jwk

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/auth/jwk", query=None, body=body, form=None, host='https://clients.plex.tv/api/v2')


@mcp.tool(annotations=_WRITE)
def create_auth_token(body: dict) -> str:
    """Exchange JWT Token.

    POST /auth/token

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/auth/token", query=None, body=body, form=None, host='https://clients.plex.tv/api/v2')


@mcp.tool(annotations=_WRITE)
def create_butler() -> str:
    """Start all Butler tasks.

    POST /butler
    """
    return call("POST", "/butler", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_butler_by_butler_task(butler_task: str) -> str:
    """Start a single Butler task.

    POST /butler/{butlerTask}

    Args:
        butler_task: The task name
    """
    return call("POST", f"/butler/{butler_task}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_by_transcode_type_transcode_universal_fallback(transcode_type: str) -> str:
    """Manually trigger a transcoder fallback.

    POST /{transcodeType}/:/transcode/universal/fallback

    Args:
        transcode_type: Path parameter.
    """
    return call("POST", f"/{transcode_type}/:/transcode/universal/fallback", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_download_queue() -> str:
    """Create download queue.

    POST /downloadQueue
    """
    return call("POST", "/downloadQueue", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_download_queue_by_queue_id_add(queue_id: int, keys: list | None = None) -> str:
    """Add to download queue.

    POST /downloadQueue/{queueId}/add

    Args:
        queue_id: The queue id
        keys: Keys to add
    """
    return call("POST", f"/downloadQueue/{queue_id}/add", query={"keys": keys}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_download_queue_by_queue_id_items_by_item_id_restart(queue_id: int, item_id: list) -> str:
    """Restart processing of items from the decision.

    POST /downloadQueue/{queueId}/items/{itemId}/restart

    Args:
        queue_id: The queue id
        item_id: The item ids
    """
    return call("POST", f"/downloadQueue/{queue_id}/items/{item_id}/restart", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_home_users() -> str:
    """Create Home User.

    POST /home/users
    """
    return call("POST", "/home/users", query=None, body=None, form=None, host='https://plex.tv/api')


@mcp.tool(annotations=_WRITE)
def create_home_users_by_id_switch(id: int) -> str:
    """Switch Home User.

    POST /home/users/{id}/switch

    Args:
        id: The unique identifier of the item
    """
    return call("POST", f"/home/users/{id}/switch", query=None, body=None, form=None, host='https://plex.tv/api')


@mcp.tool(annotations=_WRITE)
def create_hubs_sections_by_section_id_manage(section_id: int, metadata_item_id: int | None = None, promoted_to_recommended: str | None = None, promoted_to_own_home: str | None = None, promoted_to_shared_home: str | None = None) -> str:
    """Create a custom hub.

    POST /hubs/sections/{sectionId}/manage

    Args:
        section_id: The section ID for the hubs to reorder
        metadata_item_id: The metadata item on which to base this hub.  This must currently be a collection
        promoted_to_recommended: Whether this hub should be displayed in recommended
        promoted_to_own_home: Whether this hub should be displayed in admin's home
        promoted_to_shared_home: Whether this hub should be displayed in shared user's home
    """
    return call("POST", f"/hubs/sections/{section_id}/manage", query={"metadataItemId": metadata_item_id, "promotedToRecommended": promoted_to_recommended, "promotedToOwnHome": promoted_to_own_home, "promotedToSharedHome": promoted_to_shared_home}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_collections(section_id: str | None = None, uri: str | None = None) -> str:
    """Create collection.

    POST /library/collections

    Args:
        section_id: The section where this collection will be created
        uri: The URI for processing the smart collection.  Required for a smart collection
    """
    return call("POST", "/library/collections", query={"sectionId": section_id, "uri": uri}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_file(url: str | None = None, virtual_file_path: str | None = None, compute_hashes: str | None = None, ingest_non_matches: str | None = None) -> str:
    """Ingest a transient item.

    POST /library/file

    Args:
        url: The file of the file to ingest.
        virtual_file_path: A virtual path to use when the url is opaque.
        compute_hashes: Whether or not to compute Plex and OpenSubtitle hashes for the file. Defaults to 0.
        ingest_non_matches: Whether or not non matching media should be stored. Defaults to 0.
    """
    return call("POST", "/library/file", query={"url": url, "virtualFilePath": virtual_file_path, "computeHashes": compute_hashes, "ingestNonMatches": ingest_non_matches}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_metadata_by_id_arts(id: int, body: dict) -> str:
    """Upload media art Art.

    POST /library/metadata/{id}/arts

    Args:
        id: The unique identifier of the item
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/library/metadata/{id}/arts", query=None, body=body, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_metadata_by_id_posters(id: int, body: dict) -> str:
    """Upload media art Poster.

    POST /library/metadata/{id}/posters

    Args:
        id: The unique identifier of the item
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", f"/library/metadata/{id}/posters", query=None, body=body, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_metadata_by_ids_by_element(ids: str, element: str, url: str | None = None) -> str:
    """Set an item's artwork, theme, etc.

    POST /library/metadata/{ids}/{element}

    Args:
        ids: Comma-separated list of IDs
        element: The type of artwork element (e.g., art, poster, thumb)
        url: The url of the new asset.  If not provided, the binary of the asset must be provided in the post body.
    """
    return call("POST", f"/library/metadata/{ids}/{element}", query={"url": url}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_metadata_by_ids_extras(ids: str, extra_type: int | None = None, url: str | None = None) -> str:
    """Add to an item's extras.

    POST /library/metadata/{ids}/extras

    Args:
        ids: Comma-separated list of IDs
        extra_type: The metadata type of the extra
        url: The URL of the extra
    """
    return call("POST", f"/library/metadata/{ids}/extras", query={"extraType": extra_type, "url": url}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_metadata_by_ids_marker(ids: str, type: int | None = None, start_time_offset: int | None = None, end_time_offset: int | None = None, attributes: dict | None = None) -> str:
    """Create a marker.

    POST /library/metadata/{ids}/marker

    Args:
        ids: Comma-separated list of IDs
        type: The type of marker to edit/create
        start_time_offset: The start time of the marker
        end_time_offset: The end time of the marker
        attributes: The attributes to assign to this marker
    """
    return call("POST", f"/library/metadata/{ids}/marker", query={"type": type, "startTimeOffset": start_time_offset, "endTimeOffset": end_time_offset, "attributes": attributes}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_optimize() -> str:
    """Optimize Library.

    POST /library/optimize
    """
    return call("POST", "/library/optimize", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_sections_all(name: str | None = None, type: int | None = None, scanner: str | None = None, agent: str | None = None, metadata_agent_provider_group_id: str | None = None, language: str | None = None, locations: list | None = None, prefs: dict | None = None, relative: str | None = None, import_fromi_tunes: str | None = None) -> str:
    """Add a library section.

    POST /library/sections/all

    Args:
        name: The name of the new section
        type: The type of library section
        scanner: The scanner this section should use
        agent: The agent this section should use for metadata
        metadata_agent_provider_group_id: The agent group id for this section
        language: The language of this section
        locations: The locations on disk to add to this section
        prefs: The preferences for this section
        relative: If set, paths are relative to `Media Upload` path
        import_fromi_tunes: If set, import media from iTunes.
    """
    return call("POST", "/library/sections/all", query={"name": name, "type": type, "scanner": scanner, "agent": agent, "metadataAgentProviderGroupId": metadata_agent_provider_group_id, "language": language, "locations": locations, "prefs": prefs, "relative": relative, "importFromiTunes": import_fromi_tunes}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_sections_by_section_id_empty_trash(section_id: int) -> str:
    """Empty Trash.

    POST /library/sections/{sectionId}/emptyTrash

    Args:
        section_id: The unique identifier of the library section
    """
    return call("POST", f"/library/sections/{section_id}/emptyTrash", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_sections_by_section_id_optimize(section_id: int) -> str:
    """Optimize Section.

    POST /library/sections/{sectionId}/optimize

    Args:
        section_id: The unique identifier of the library section
    """
    return call("POST", f"/library/sections/{section_id}/optimize", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_sections_by_section_id_refresh(section_id: int, force: str | None = None, path: str | None = None) -> str:
    """Refresh Section.

    POST /library/sections/{sectionId}/refresh

    Args:
        section_id: Section identifier
        force: Whether the update of metadata and items should be performed even if modification dates indicate the items have not change
        path: Restrict refresh to the specified path
    """
    return call("POST", f"/library/sections/{section_id}/refresh", query={"force": force, "path": path}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_library_sections_refresh(force: bool | None = None) -> str:
    """Refresh all sections.

    POST /library/sections/refresh

    Args:
        force: Force refresh of metadata
    """
    return call("POST", "/library/sections/refresh", query={"force": force}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_livetv_dvrs(lineup: str | None = None, device: list | None = None, language: str | None = None) -> str:
    """Create a DVR.

    POST /livetv/dvrs

    Args:
        lineup: The EPG lineup.
        device: The device.
        language: The language.
    """
    return call("POST", "/livetv/dvrs", query={"lineup": lineup, "device": device, "language": language}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_livetv_dvrs_by_dvr_id_channels_by_channel_tune(dvr_id: int, channel: str) -> str:
    """Tune a channel on a DVR.

    POST /livetv/dvrs/{dvrId}/channels/{channel}/tune

    Args:
        dvr_id: The ID of the DVR.
        channel: The channel ID to tune
    """
    return call("POST", f"/livetv/dvrs/{dvr_id}/channels/{channel}/tune", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_livetv_dvrs_by_dvr_id_reload_guide(dvr_id: int) -> str:
    """Tell a DVR to reload program guide.

    POST /livetv/dvrs/{dvrId}/reloadGuide

    Args:
        dvr_id: The ID of the DVR.
    """
    return call("POST", f"/livetv/dvrs/{dvr_id}/reloadGuide", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_log(body: dict) -> str:
    """Logging a multi-line message to the Plex Media Server log.

    POST /log

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/log", query=None, body=body, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_log_networked(minutes: int | None = None) -> str:
    """Enabling Papertrail.

    POST /log/networked

    Args:
        minutes: The number of minutes logging should be sent to Papertrail
    """
    return call("POST", "/log/networked", query={"minutes": minutes}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_media_grabbers_devices(uri: str | None = None) -> str:
    """Add a device.

    POST /media/grabbers/devices

    Args:
        uri: The URI of the device.
    """
    return call("POST", "/media/grabbers/devices", query={"uri": uri}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_media_grabbers_devices_by_device_id_scan(device_id: int, source: str | None = None) -> str:
    """Tell a device to scan for channels.

    POST /media/grabbers/devices/{deviceId}/scan

    Args:
        device_id: The ID of the device.
        source: A valid source for the scan
    """
    return call("POST", f"/media/grabbers/devices/{device_id}/scan", query={"source": source}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_media_providers(url: str | None = None) -> str:
    """Add a media provider.

    POST /media/providers

    Args:
        url: The URL of the media provider to add.
    """
    return call("POST", "/media/providers", query={"url": url}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_media_providers_refresh() -> str:
    """Refresh media providers.

    POST /media/providers/refresh
    """
    return call("POST", "/media/providers/refresh", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_media_subscriptions(target_library_section_id: int | None = None, target_section_location_id: int | None = None, type: int | None = None, hints: dict | None = None, prefs: dict | None = None, params: dict | None = None) -> str:
    """Create a subscription.

    POST /media/subscriptions

    Args:
        target_library_section_id: The library section into which we'll grab the media.  Not actually required when the subscription is to a playlist.
        target_section_location_id: The section location into which to grab.
        type: The type of the thing we're subscribing too (e.g. show, season).
        hints: Hints describing what we're looking for.  Note: The hint `ratingKey` is required for downloading from a PMS remote.
        prefs: Subscription preferences.
        params: Subscription parameters.
  - `mediaProviderID`: Required for downloads to indicate which MP the subscription will download into
  - `source`: Required for downloads to indicate the source of the downloaded content.
    """
    return call("POST", "/media/subscriptions", query={"targetLibrarySectionID": target_library_section_id, "targetSectionLocationID": target_section_location_id, "type": type, "hints": hints, "prefs": prefs, "params": params}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_media_subscriptions_process() -> str:
    """Process all subscriptions.

    POST /media/subscriptions/process
    """
    return call("POST", "/media/subscriptions/process", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_myplex_claim() -> str:
    """Claim Server.

    POST /myplex/claim
    """
    return call("POST", "/myplex/claim", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_pins() -> str:
    """Create OAuth PIN.

    POST /pins
    """
    return call("POST", "/pins", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_WRITE)
def create_pins_xml() -> str:
    """Create Legacy PIN.

    POST /pins.xml
    """
    return call("POST", "/pins.xml", query=None, body=None, form=None, host='https://plex.tv')


@mcp.tool(annotations=_WRITE)
def create_play_queues(uri: str | None = None, playlist_id: int | None = None, type: str | None = None, key: str | None = None, shuffle: str | None = None, repeat: str | None = None, continuous: str | None = None, extras_prefix_count: int | None = None, recursive: str | None = None, on_deck: str | None = None) -> str:
    """Create a play queue.

    POST /playQueues

    Args:
        uri: The content URI for what we're playing.
        playlist_id: the ID of the playlist we're playing.
        type: The type of play queue to create
        key: The key of the first item to play, defaults to the first in the play queue.
        shuffle: Whether to shuffle the playlist, defaults to 0.
        repeat: If the PQ is bigger than the window, fill any empty space with wraparound items, defaults to 0.
        continuous: Whether to create a continuous play queue (e.g. from an episode), defaults to 0.
        extras_prefix_count: Number of trailers to prepend a movie with not including the pre-roll. If omitted the pre-roll will not be returned in the play queue. When resuming a movie `extrasPrefixCount` should be omitted as a parameter instead of passing 0.
        recursive: Only applies to queues of type photo, whether to retrieve all descendent photos from an album or section, defaults to 1.
        on_deck: Only applies to queues of type show or seasons, whether to return a queue that is started on the On Deck episode if one exists. Otherwise begins the play queue on the beginning of the show or season.
    """
    return call("POST", "/playQueues", query={"uri": uri, "playlistID": playlist_id, "type": type, "key": key, "shuffle": shuffle, "repeat": repeat, "continuous": continuous, "extrasPrefixCount": extras_prefix_count, "recursive": recursive, "onDeck": on_deck}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_audio_stream(stream_id: int | None = None) -> str:
    """Player Audio Stream.

    POST /player/playback/audioStream

    Args:
        stream_id: The unique identifier of the stream
    """
    return call("POST", "/player/playback/audioStream", query={"streamID": stream_id}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_mute() -> str:
    """Player Mute.

    POST /player/playback/mute
    """
    return call("POST", "/player/playback/mute", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_pause() -> str:
    """Player Pause.

    POST /player/playback/pause
    """
    return call("POST", "/player/playback/pause", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_play() -> str:
    """Player Play.

    POST /player/playback/play
    """
    return call("POST", "/player/playback/play", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_play_media(key: str | None = None, offset: int | None = None, machine_identifier: str | None = None) -> str:
    """Player Play Media.

    POST /player/playback/playMedia

    Args:
        key: The key of the media item to play
        offset: The byte offset for stream seeking
        machine_identifier: The machine identifier of the target device
    """
    return call("POST", "/player/playback/playMedia", query={"key": key, "offset": offset, "machineIdentifier": machine_identifier}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_refresh_play_queue() -> str:
    """Player Refresh Play Queue.

    POST /player/playback/refreshPlayQueue
    """
    return call("POST", "/player/playback/refreshPlayQueue", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_seek(offset: int | None = None) -> str:
    """Player Seek.

    POST /player/playback/seek

    Args:
        offset: Target offset in milliseconds
    """
    return call("POST", "/player/playback/seek", query={"offset": offset}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_set_parameters(shuffle: int | None = None, repeat: int | None = None, volume: int | None = None) -> str:
    """Player Set Parameters.

    POST /player/playback/setParameters

    Args:
        shuffle: Whether to enable shuffle mode
        repeat: The repeat mode to set
        volume: The volume level to set
    """
    return call("POST", "/player/playback/setParameters", query={"shuffle": shuffle, "repeat": repeat, "volume": volume}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_set_rating(rating: int | None = None) -> str:
    """Player Set Rating.

    POST /player/playback/setRating

    Args:
        rating: The rating value to set
    """
    return call("POST", "/player/playback/setRating", query={"rating": rating}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_set_state(state: str | None = None) -> str:
    """Player Set State.

    POST /player/playback/setState

    Args:
        state: The desired playback state
    """
    return call("POST", "/player/playback/setState", query={"state": state}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_set_streams(audio_stream_id: int | None = None, subtitle_stream_id: int | None = None, video_stream_id: int | None = None) -> str:
    """Player Set Streams.

    POST /player/playback/setStreams

    Args:
        audio_stream_id: The unique identifier of the audiostream
        subtitle_stream_id: The unique identifier of the subtitlestream
        video_stream_id: The unique identifier of the videostream
    """
    return call("POST", "/player/playback/setStreams", query={"audioStreamID": audio_stream_id, "subtitleStreamID": subtitle_stream_id, "videoStreamID": video_stream_id}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_set_text_stream(stream_id: int | None = None) -> str:
    """Player Set Text Stream.

    POST /player/playback/setTextStream

    Args:
        stream_id: The unique identifier of the stream
    """
    return call("POST", "/player/playback/setTextStream", query={"streamID": stream_id}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_set_view_offset(offset: int | None = None) -> str:
    """Player Set View Offset.

    POST /player/playback/setViewOffset

    Args:
        offset: The byte offset for stream seeking
    """
    return call("POST", "/player/playback/setViewOffset", query={"offset": offset}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_skip_by(offset: int | None = None) -> str:
    """Player Skip By.

    POST /player/playback/skipBy

    Args:
        offset: Number of items to skip (positive for forward, negative for backward)
    """
    return call("POST", "/player/playback/skipBy", query={"offset": offset}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_skip_to(key: str | None = None) -> str:
    """Player Skip To.

    POST /player/playback/skipTo

    Args:
        key: The key of the item to skip to
    """
    return call("POST", "/player/playback/skipTo", query={"key": key}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_step_back() -> str:
    """Player Step Back.

    POST /player/playback/stepBack
    """
    return call("POST", "/player/playback/stepBack", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_step_forward() -> str:
    """Player Step Forward.

    POST /player/playback/stepForward
    """
    return call("POST", "/player/playback/stepForward", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_stop() -> str:
    """Player Stop.

    POST /player/playback/stop
    """
    return call("POST", "/player/playback/stop", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_subtitle_stream(stream_id: int | None = None) -> str:
    """Player Subtitle Stream.

    POST /player/playback/subtitleStream

    Args:
        stream_id: The unique identifier of the stream
    """
    return call("POST", "/player/playback/subtitleStream", query={"streamID": stream_id}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_unmute() -> str:
    """Player Unmute.

    POST /player/playback/unmute
    """
    return call("POST", "/player/playback/unmute", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_video_stream(stream_id: int | None = None) -> str:
    """Player Video Stream.

    POST /player/playback/videoStream

    Args:
        stream_id: The unique identifier of the stream
    """
    return call("POST", "/player/playback/videoStream", query={"streamID": stream_id}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_player_playback_volume(level: int | None = None) -> str:
    """Player Volume.

    POST /player/playback/volume

    Args:
        level: The level
    """
    return call("POST", "/player/playback/volume", query={"level": level}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_playlists(uri: str | None = None, play_queue_id: int | None = None) -> str:
    """Create a Playlist.

    POST /playlists

    Args:
        uri: The content URI for what we're playing (e.g. `library://...`).
        play_queue_id: To create a playlist from an existing play queue.
    """
    return call("POST", "/playlists", query={"uri": uri, "playQueueID": play_queue_id}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_playlists_upload(path: str | None = None, force: str | None = None) -> str:
    """Upload media art.

    POST /playlists/upload

    Args:
        path: Absolute path to a directory on the server where m3u files are stored, or the absolute path to a playlist file on the server. If the `path` argument is a directory, that path will be scanned for playlist files to be processed. Each file in that directory creates a separate playlist, with a name based on the filename of the file that created it. The GUID of each playlist is based on the filename. If the `path` argument is a file, that file will be used to create a new playlist, with the name based on the filename of the file that created it. The GUID of each playlist is based on the filename.
        force: Force overwriting of duplicate playlists. By default, a playlist file uploaded with the same path will overwrite the existing playlist. The `force` argument is used to disable overwriting. If the `force` argument is set to 0, a new playlist will be created suffixed with the date and time that the duplicate was uploaded.
    """
    return call("POST", "/playlists/upload", query={"path": path, "force": force}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_security_token(type: str | None = None, scope: str | None = None) -> str:
    """Get Transient Tokens.

    POST /security/token

    Args:
        type: The value `delegation` is the only supported `type` parameter.
        scope: The value `all` is the only supported `scope` parameter.
    """
    return call("POST", "/security/token", query={"type": type, "scope": scope}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_servers_by_machine_id_shared_servers(machine_id: str) -> str:
    """Share Server (Legacy v1).

    POST /servers/{machineId}/shared_servers

    Args:
        machine_id: The unique machine identifier of the server
    """
    return call("POST", f"/servers/{machine_id}/shared_servers", query=None, body=None, form=None, host='https://plex.tv/api')


@mcp.tool(annotations=_WRITE)
def create_shared_servers() -> str:
    """Share Server.

    POST /shared_servers
    """
    return call("POST", "/shared_servers", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_WRITE)
def create_status_sessions_terminate(session_id: str | None = None, reason: str | None = None) -> str:
    """Terminate a session.

    POST /status/sessions/terminate

    Args:
        session_id: The session id (found in the `Session` element in [/status/sessions](#tag/Status/operation/statusGetSlash))
        reason: The reason to give to the user (typically displayed in the client)
    """
    return call("POST", "/status/sessions/terminate", query={"sessionId": session_id, "reason": reason}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_timeline(key: str | None = None, rating_key: str | None = None, state: str | None = None, play_queue_item_id: str | None = None, time: int | None = None, duration: int | None = None, continuing: str | None = None, updated: int | None = None, offline: str | None = None, time_to_first_frame: int | None = None, time_stalled: int | None = None, bandwidth: int | None = None, buffered_time: int | None = None, buffered_size: int | None = None, container_key: str | None = None, guid: str | None = None, play_queue_id: int | None = None, url: str | None = None) -> str:
    """Report media timeline.

    POST /:/timeline

    Args:
        key: The details key for the item.
        rating_key: The rating key attribute for the item.
        state: The current state of the media.
        play_queue_item_id: If playing media from a play queue, the play queue's ID.
        time: The current time offset of playback in ms.
        duration: The total duration of the item in ms.
        continuing: When state is `stopped`, a flag indicating whether or not the client is going to continue playing anothe item.
        updated: Used when a sync client comes online and is syncing media timelines, holds the time at which the playback state was last updated.
        offline: Also used by sync clients, used to indicate that a timeline is being synced from being offline, as opposed to being "live".
        time_to_first_frame: Time in seconds till first frame is displayed.  Sent only on the first playing timeline request.
        time_stalled: Time in seconds spent buffering since last request.
        bandwidth: Bandwidth in kbps as estimated by the client.
        buffered_time: Amount of time in seconds buffered by client.  Omit if computed by `bufferedSize` below.
        buffered_size: Size in kilobytes of data buffered by client.  Omit if computed by `bufferedTime` above
        container_key: Groups timeline reports (e.g. /playQueues/123).
        guid: Global unique identifier for the item.
        play_queue_id: Identifies the play queue itself (distinct from playQueueItemID).
        url: Alternative to key/ratingKey (legacy).
    """
    return call("POST", "/:/timeline", query={"key": key, "ratingKey": rating_key, "state": state, "playQueueItemID": play_queue_item_id, "time": time, "duration": duration, "continuing": continuing, "updated": updated, "offline": offline, "timeToFirstFrame": time_to_first_frame, "timeStalled": time_stalled, "bandwidth": bandwidth, "bufferedTime": buffered_time, "bufferedSize": buffered_size, "containerKey": container_key, "guid": guid, "playQueueID": play_queue_id, "url": url}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def create_users_password() -> str:
    """Change Password.

    POST /users/password
    """
    return call("POST", "/users/password", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_WRITE)
def create_users_signin(body: dict) -> str:
    """Get User Sign In Data.

    POST /users/signin

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("POST", "/users/signin", query=None, body=body, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_WRITE)
def create_v2_user_webhooks() -> str:
    """Add User Webhook.

    POST /api/v2/user/webhooks
    """
    return call("POST", "/api/v2/user/webhooks", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_WRITE)
def create_webhooks() -> str:
    """Add Webhook.

    POST /webhooks
    """
    return call("POST", "/webhooks", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_activities_by_activity_id(activity_id: str) -> str:
    """Cancel a running activity.

    DELETE /activities/{activityId}

    Args:
        activity_id: The UUID of the activity to cancel.
    """
    return call("DELETE", f"/activities/{activity_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_butler() -> str:
    """Stop all Butler tasks.

    DELETE /butler
    """
    return call("DELETE", "/butler", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_butler_by_butler_task(butler_task: str) -> str:
    """Stop a single Butler task.

    DELETE /butler/{butlerTask}

    Args:
        butler_task: The task name
    """
    return call("DELETE", f"/butler/{butler_task}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_download_queue_by_queue_id_items_by_item_id(queue_id: int, item_id: list) -> str:
    """Delete download queue items.

    DELETE /downloadQueue/{queueId}/items/{itemId}

    Args:
        queue_id: The queue id
        item_id: The item id
    """
    return call("DELETE", f"/downloadQueue/{queue_id}/items/{item_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_home_users_by_user_id(user_id: int) -> str:
    """Delete Home User.

    DELETE /home/users/{userId}

    Args:
        user_id: The unique identifier of the user
    """
    return call("DELETE", f"/home/users/{user_id}", query=None, body=None, form=None, host='https://plex.tv/api')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_hubs_sections_by_section_id_manage(section_id: int) -> str:
    """Reset hubs to defaults.

    DELETE /hubs/sections/{sectionId}/manage

    Args:
        section_id: The section ID for the hubs to reorder
    """
    return call("DELETE", f"/hubs/sections/{section_id}/manage", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_hubs_sections_by_section_id_manage_by_identifier(section_id: int, identifier: str) -> str:
    """Delete a custom hub.

    DELETE /hubs/sections/{sectionId}/manage/{identifier}

    Args:
        section_id: The section ID for the hubs to change
        identifier: The identifier of the hub to change
    """
    return call("DELETE", f"/hubs/sections/{section_id}/manage/{identifier}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_library_caches() -> str:
    """Delete library caches.

    DELETE /library/caches
    """
    return call("DELETE", "/library/caches", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_library_metadata_by_ids(ids: str, proxy: str | None = None) -> str:
    """Delete a metadata item.

    DELETE /library/metadata/{ids}

    Args:
        ids: Comma-separated list of IDs
        proxy: Whether proxy items, such as media optimized versions, should also be deleted.  Defaults to false.
    """
    return call("DELETE", f"/library/metadata/{ids}", query={"proxy": proxy}, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_library_metadata_by_ids_marker_by_marker(ids: str, marker: str) -> str:
    """Delete a marker.

    DELETE /library/metadata/{ids}/marker/{marker}

    Args:
        ids: Comma-separated list of IDs
        marker: The marker identifier
    """
    return call("DELETE", f"/library/metadata/{ids}/marker/{marker}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_library_metadata_by_ids_media_by_media_item(ids: str, media_item: str, proxy: str | None = None) -> str:
    """Delete a media item.

    DELETE /library/metadata/{ids}/media/{mediaItem}

    Args:
        ids: Comma-separated list of IDs
        media_item: The mediaItem
        proxy: Whether proxy items, such as media optimized versions, should also be deleted.  Defaults to false.
    """
    return call("DELETE", f"/library/metadata/{ids}/media/{media_item}", query={"proxy": proxy}, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_library_sections_all_refresh() -> str:
    """Stop refresh.

    DELETE /library/sections/all/refresh
    """
    return call("DELETE", "/library/sections/all/refresh", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_library_sections_by_section_id(section_id: str, async_: str | None = None) -> str:
    """Delete a library section.

    DELETE /library/sections/{sectionId}

    Args:
        section_id: The section identifier
        async_: If set, response will return an activity with the actual deletion process.  Otherwise request will return when deletion is complete
    """
    return call("DELETE", f"/library/sections/{section_id}", query={"async": async_}, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_library_sections_by_section_id_collection_by_collection_id(section_id: int, collection_id: int) -> str:
    """Delete a collection.

    DELETE /library/sections/{sectionId}/collection/{collectionId}

    Args:
        section_id: Section identifier
        collection_id: Collection Id
    """
    return call("DELETE", f"/library/sections/{section_id}/collection/{collection_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_library_sections_by_section_id_indexes(section_id: int) -> str:
    """Delete section indexes.

    DELETE /library/sections/{sectionId}/indexes

    Args:
        section_id: Section identifier
    """
    return call("DELETE", f"/library/sections/{section_id}/indexes", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_library_sections_by_section_id_intros(section_id: int) -> str:
    """Delete section intro markers.

    DELETE /library/sections/{sectionId}/intros

    Args:
        section_id: Section identifier
    """
    return call("DELETE", f"/library/sections/{section_id}/intros", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_library_sections_by_section_id_refresh(section_id: int) -> str:
    """Cancel section refresh.

    DELETE /library/sections/{sectionId}/refresh

    Args:
        section_id: Section identifier
    """
    return call("DELETE", f"/library/sections/{section_id}/refresh", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_library_streams_by_stream_id_ext(stream_id: int, ext: str) -> str:
    """Delete a stream.

    DELETE /library/streams/{streamId}.{ext}

    Args:
        stream_id: The id of the stream
        ext: This is not a part of this endpoint but documented here to satisfy OpenAPI
    """
    return call("DELETE", f"/library/streams/{stream_id}.{ext}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_livetv_dvrs_by_dvr_id(dvr_id: int) -> str:
    """Delete a single DVR.

    DELETE /livetv/dvrs/{dvrId}

    Args:
        dvr_id: The ID of the DVR.
    """
    return call("DELETE", f"/livetv/dvrs/{dvr_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_livetv_dvrs_by_dvr_id_devices_by_device_id(dvr_id: int, device_id: int) -> str:
    """Remove a device from an existing DVR.

    DELETE /livetv/dvrs/{dvrId}/devices/{deviceId}

    Args:
        dvr_id: The ID of the DVR.
        device_id: The ID of the device to add.
    """
    return call("DELETE", f"/livetv/dvrs/{dvr_id}/devices/{device_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_livetv_dvrs_by_dvr_id_lineups(dvr_id: int, lineup: str | None = None) -> str:
    """Delete a DVR Lineup.

    DELETE /livetv/dvrs/{dvrId}/lineups

    Args:
        dvr_id: The ID of the DVR.
        lineup: The lineup to delete
    """
    return call("DELETE", f"/livetv/dvrs/{dvr_id}/lineups", query={"lineup": lineup}, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_livetv_dvrs_by_dvr_id_reload_guide(dvr_id: int) -> str:
    """Tell a DVR to stop reloading program guide.

    DELETE /livetv/dvrs/{dvrId}/reloadGuide

    Args:
        dvr_id: The ID of the DVR.
    """
    return call("DELETE", f"/livetv/dvrs/{dvr_id}/reloadGuide", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_livetv_sessions_by_session_id(session_id: str) -> str:
    """Delete Live TV Session.

    DELETE /livetv/sessions/{sessionId}

    Args:
        session_id: The session id
    """
    return call("DELETE", f"/livetv/sessions/{session_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_media_grabbers_devices_by_device_id(device_id: int) -> str:
    """Remove a device.

    DELETE /media/grabbers/devices/{deviceId}

    Args:
        device_id: The ID of the device.
    """
    return call("DELETE", f"/media/grabbers/devices/{device_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_media_grabbers_devices_by_device_id_scan(device_id: int) -> str:
    """Tell a device to stop scanning for channels.

    DELETE /media/grabbers/devices/{deviceId}/scan

    Args:
        device_id: The ID of the device.
    """
    return call("DELETE", f"/media/grabbers/devices/{device_id}/scan", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_media_grabbers_operations_by_operation_id(operation_id: str) -> str:
    """Cancel an existing grab.

    DELETE /media/grabbers/operations/{operationId}

    Args:
        operation_id: The ID of the operation.
    """
    return call("DELETE", f"/media/grabbers/operations/{operation_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_media_providers_by_provider(provider: str) -> str:
    """Delete a media provider.

    DELETE /media/providers/{provider}

    Args:
        provider: The ID of the media provider to delete
    """
    return call("DELETE", f"/media/providers/{provider}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_media_subscriptions_by_subscription_id(subscription_id: int) -> str:
    """Delete a subscription.

    DELETE /media/subscriptions/{subscriptionId}

    Args:
        subscription_id: The unique identifier of the subscription
    """
    return call("DELETE", f"/media/subscriptions/{subscription_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_play_queues_by_play_queue_id_items(play_queue_id: int) -> str:
    """Clear a play queue.

    DELETE /playQueues/{playQueueId}/items

    Args:
        play_queue_id: The ID of the play queue.
    """
    return call("DELETE", f"/playQueues/{play_queue_id}/items", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_play_queues_by_play_queue_id_items_by_play_queue_item_id(play_queue_id: int, play_queue_item_id: int) -> str:
    """Delete an item from a play queue.

    DELETE /playQueues/{playQueueId}/items/{playQueueItemId}

    Args:
        play_queue_id: The ID of the play queue.
        play_queue_item_id: The play queue item ID to delete.
    """
    return call("DELETE", f"/playQueues/{play_queue_id}/items/{play_queue_item_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_playlists(rating_key: int | None = None) -> str:
    """Delete Playlist.

    DELETE /playlists

    Args:
        rating_key: The rating key of the playlist to delete.
    """
    return call("DELETE", "/playlists", query={"ratingKey": rating_key}, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_playlists_by_playlist_id(playlist_id: int) -> str:
    """Delete a Playlist.

    DELETE /playlists/{playlistId}

    Args:
        playlist_id: The ID of the playlist
    """
    return call("DELETE", f"/playlists/{playlist_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_playlists_by_playlist_id_items(playlist_id: int) -> str:
    """Clearing a playlist.

    DELETE /playlists/{playlistId}/items

    Args:
        playlist_id: The ID of the playlist
    """
    return call("DELETE", f"/playlists/{playlist_id}/items", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_playlists_by_playlist_id_items_by_generator_id(playlist_id: int, generator_id: int) -> str:
    """Delete a Generator.

    DELETE /playlists/{playlistId}/items/{generatorId}

    Args:
        playlist_id: The ID of the playlist
        generator_id: The generator item ID to delete.
    """
    return call("DELETE", f"/playlists/{playlist_id}/items/{generator_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_sharings_by_user_id(user_id: int) -> str:
    """Remove Share.

    DELETE /sharings/{userId}

    Args:
        user_id: The unique identifier of the user
    """
    return call("DELETE", f"/sharings/{user_id}", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_status_sessions_history_by_history_id(history_id: int) -> str:
    """Delete Single History Item.

    DELETE /status/sessions/history/{historyId}

    Args:
        history_id: The id of the history item (the `historyKey` from above)
    """
    return call("DELETE", f"/status/sessions/history/{history_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_DESTRUCTIVE)
def delete_users_signout() -> str:
    """Sign Out.

    DELETE /users/signout
    """
    return call("DELETE", "/users/signout", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def get_by_transcode_type_transcode_universal_decision(transcode_type: str, platform: str | None = None, audio_boost: int | None = None, audio_channel_count: int | None = None, auto_adjust_quality: str | None = None, auto_adjust_subtitle: str | None = None, direct_play: str | None = None, direct_stream: str | None = None, direct_stream_audio: str | None = None, disable_resolution_rotation: str | None = None, has_mde: str | None = None, location: str | None = None, media_buffer_size: int | None = None, media_index: int | None = None, music_bitrate: int | None = None, offset: float | None = None, part_index: int | None = None, path: str | None = None, peak_bitrate: int | None = None, photo_resolution: str | None = None, protocol: str | None = None, seconds_per_segment: int | None = None, subtitle_size: int | None = None, subtitles: str | None = None, max_video_bitrate: int | None = None, video_resolution: str | None = None, copyts: str | None = None, video_bitrate: int | None = None, video_quality: int | None = None) -> str:
    """Make a decision on media playback.

    GET /{transcodeType}/:/transcode/universal/decision

    Args:
        transcode_type: Path parameter.
        platform: Client platform (some clients send this in addition to headers).
        audio_boost: Percentage of original audio loudness to use when transcoding (100 is equivalent to original volume, 50 is half, 200 is double, etc)
        audio_channel_count: Target video number of audio channels.
        auto_adjust_quality: Indicates the client supports ABR.
        auto_adjust_subtitle: Indicates if the server should adjust subtitles based on Voice Activity Data.
        direct_play: Indicates the client supports direct playing the indicated content.
        direct_stream: Indicates the client supports direct streaming the video of the indicated content.
        direct_stream_audio: Indicates the client supports direct streaming the audio of the indicated content.
        disable_resolution_rotation: Indicates if resolution should be adjusted for orientation.
        has_mde: Ignore client profiles when determining if direct play is possible. Only has an effect when directPlay=1 and both mediaIndex and partIndex are specified and neither are -1
        location: Network type of the client, can be used to help determine target bitrate.
        media_buffer_size: Buffer size used in playback (in KB). Clients should specify a lower bound if not known exactly. This value could make the difference between transcoding and direct play on bandwidth constrained networks.
        media_index: Index of the media to transcode. -1 or not specified indicates let the server choose.
        music_bitrate: Target bitrate for audio only files (in kbps, used to transcode).
        offset: Offset from the start of the media (in seconds).
        part_index: Index of the part to transcode. -1 or not specified indicates the server should join parts together in a transcode
        path: Internal PMS path of the media to transcode.
        peak_bitrate: Maximum bitrate (in kbps) to use in ABR.
        photo_resolution: Target photo resolution.
        protocol: Indicates the network streaming protocol to be used for the transcode session: * 'http' - include the file in the http response such as MKV streaming * 'hls' - hls stream (RFC 8216) * 'dash' - dash stream (ISO/IEC 23009-1:2022)
        seconds_per_segment: Number of seconds to include in each transcoded segment
        subtitle_size: Percentage of original subtitle size to use when burning subtitles (100 is equivalent to original size, 50 is half, ect)
        subtitles: Indicates how subtitles should be included: * 'auto' - Compute the appropriate subtitle setting automatically * 'burn' - Burn the selected subtitle; auto if no selected subtitle * 'none' - Ignore all subtitle streams * 'sidecar' - The selected subtitle should be provided as a sidecar * 'embedded' - The selected subtitle should be provided as an embedded stream * 'segmented' - The selected subtitle should be provided as a segmented stream
        max_video_bitrate: Client-side maximum video bitrate cap in kbps
        video_resolution: Cap resolution string (e.g. 1920x1080)
        copyts: Copy timestamps instead of re-encoding them
        video_bitrate: Target video bitrate (in kbps).
        video_quality: Target photo quality.
    """
    return call("GET", f"/{transcode_type}/:/transcode/universal/decision", query={"platform": platform, "audioBoost": audio_boost, "audioChannelCount": audio_channel_count, "autoAdjustQuality": auto_adjust_quality, "autoAdjustSubtitle": auto_adjust_subtitle, "directPlay": direct_play, "directStream": direct_stream, "directStreamAudio": direct_stream_audio, "disableResolutionRotation": disable_resolution_rotation, "hasMDE": has_mde, "location": location, "mediaBufferSize": media_buffer_size, "mediaIndex": media_index, "musicBitrate": music_bitrate, "offset": offset, "partIndex": part_index, "path": path, "peakBitrate": peak_bitrate, "photoResolution": photo_resolution, "protocol": protocol, "secondsPerSegment": seconds_per_segment, "subtitleSize": subtitle_size, "subtitles": subtitles, "maxVideoBitrate": max_video_bitrate, "videoResolution": video_resolution, "copyts": copyts, "videoBitrate": video_bitrate, "videoQuality": video_quality}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_by_transcode_type_transcode_universal_session_by_session_id_by_segment_id_m4s(transcode_type: str, session_id: str, segment_id: str) -> str:
    """Get DASH Segment.

    GET /{transcodeType}/:/transcode/universal/session/{sessionId}/{segmentId}.m4s

    Args:
        transcode_type: The type of transcoding (e.g., video, audio)
        session_id: The unique identifier of the session
        segment_id: The unique identifier of the media segment
    """
    return call("GET", f"/{transcode_type}/:/transcode/universal/session/{session_id}/{segment_id}.m4s", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_by_transcode_type_transcode_universal_session_by_session_id_by_segment_id_ts(transcode_type: str, session_id: str, segment_id: str) -> str:
    """Get HLS Segment.

    GET /{transcodeType}/:/transcode/universal/session/{sessionId}/{segmentId}.ts

    Args:
        transcode_type: The type of transcoding (e.g., video, audio)
        session_id: The unique identifier of the session
        segment_id: The unique identifier of the media segment
    """
    return call("GET", f"/{transcode_type}/:/transcode/universal/session/{session_id}/{segment_id}.ts", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_by_transcode_type_transcode_universal_start_extension(extension: str, transcode_type: str, platform: str | None = None, audio_boost: int | None = None, audio_channel_count: int | None = None, auto_adjust_quality: str | None = None, auto_adjust_subtitle: str | None = None, direct_play: str | None = None, direct_stream: str | None = None, direct_stream_audio: str | None = None, disable_resolution_rotation: str | None = None, has_mde: str | None = None, location: str | None = None, media_buffer_size: int | None = None, media_index: int | None = None, music_bitrate: int | None = None, offset: float | None = None, part_index: int | None = None, path: str | None = None, peak_bitrate: int | None = None, photo_resolution: str | None = None, protocol: str | None = None, seconds_per_segment: int | None = None, subtitle_size: int | None = None, subtitles: str | None = None, max_video_bitrate: int | None = None, video_resolution: str | None = None, copyts: str | None = None, video_bitrate: int | None = None, video_quality: int | None = None) -> str:
    """Start A Transcoding Session.

    GET /{transcodeType}/:/transcode/universal/start.{extension}

    Args:
        extension: Extension
        transcode_type: Path parameter.
        platform: Client platform (some clients send this in addition to headers).
        audio_boost: Percentage of original audio loudness to use when transcoding (100 is equivalent to original volume, 50 is half, 200 is double, etc)
        audio_channel_count: Target video number of audio channels.
        auto_adjust_quality: Indicates the client supports ABR.
        auto_adjust_subtitle: Indicates if the server should adjust subtitles based on Voice Activity Data.
        direct_play: Indicates the client supports direct playing the indicated content.
        direct_stream: Indicates the client supports direct streaming the video of the indicated content.
        direct_stream_audio: Indicates the client supports direct streaming the audio of the indicated content.
        disable_resolution_rotation: Indicates if resolution should be adjusted for orientation.
        has_mde: Ignore client profiles when determining if direct play is possible. Only has an effect when directPlay=1 and both mediaIndex and partIndex are specified and neither are -1
        location: Network type of the client, can be used to help determine target bitrate.
        media_buffer_size: Buffer size used in playback (in KB). Clients should specify a lower bound if not known exactly. This value could make the difference between transcoding and direct play on bandwidth constrained networks.
        media_index: Index of the media to transcode. -1 or not specified indicates let the server choose.
        music_bitrate: Target bitrate for audio only files (in kbps, used to transcode).
        offset: Offset from the start of the media (in seconds).
        part_index: Index of the part to transcode. -1 or not specified indicates the server should join parts together in a transcode
        path: Internal PMS path of the media to transcode.
        peak_bitrate: Maximum bitrate (in kbps) to use in ABR.
        photo_resolution: Target photo resolution.
        protocol: Indicates the network streaming protocol to be used for the transcode session: * 'http' - include the file in the http response such as MKV streaming * 'hls' - hls stream (RFC 8216) * 'dash' - dash stream (ISO/IEC 23009-1:2022)
        seconds_per_segment: Number of seconds to include in each transcoded segment
        subtitle_size: Percentage of original subtitle size to use when burning subtitles (100 is equivalent to original size, 50 is half, ect)
        subtitles: Indicates how subtitles should be included: * 'auto' - Compute the appropriate subtitle setting automatically * 'burn' - Burn the selected subtitle; auto if no selected subtitle * 'none' - Ignore all subtitle streams * 'sidecar' - The selected subtitle should be provided as a sidecar * 'embedded' - The selected subtitle should be provided as an embedded stream * 'segmented' - The selected subtitle should be provided as a segmented stream
        max_video_bitrate: Client-side maximum video bitrate cap in kbps
        video_resolution: Cap resolution string (e.g. 1920x1080)
        copyts: Copy timestamps instead of re-encoding them
        video_bitrate: Target video bitrate (in kbps).
        video_quality: Target photo quality.
    """
    return call("GET", f"/{transcode_type}/:/transcode/universal/start.{extension}", query={"platform": platform, "audioBoost": audio_boost, "audioChannelCount": audio_channel_count, "autoAdjustQuality": auto_adjust_quality, "autoAdjustSubtitle": auto_adjust_subtitle, "directPlay": direct_play, "directStream": direct_stream, "directStreamAudio": direct_stream_audio, "disableResolutionRotation": disable_resolution_rotation, "hasMDE": has_mde, "location": location, "mediaBufferSize": media_buffer_size, "mediaIndex": media_index, "musicBitrate": music_bitrate, "offset": offset, "partIndex": part_index, "path": path, "peakBitrate": peak_bitrate, "photoResolution": photo_resolution, "protocol": protocol, "secondsPerSegment": seconds_per_segment, "subtitleSize": subtitle_size, "subtitles": subtitles, "maxVideoBitrate": max_video_bitrate, "videoResolution": video_resolution, "copyts": copyts, "videoBitrate": video_bitrate, "videoQuality": video_quality}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_by_transcode_type_transcode_universal_subtitles(transcode_type: str, platform: str | None = None, audio_boost: int | None = None, audio_channel_count: int | None = None, auto_adjust_quality: str | None = None, auto_adjust_subtitle: str | None = None, direct_play: str | None = None, direct_stream: str | None = None, direct_stream_audio: str | None = None, disable_resolution_rotation: str | None = None, has_mde: str | None = None, location: str | None = None, media_buffer_size: int | None = None, media_index: int | None = None, music_bitrate: int | None = None, offset: float | None = None, part_index: int | None = None, path: str | None = None, peak_bitrate: int | None = None, photo_resolution: str | None = None, protocol: str | None = None, seconds_per_segment: int | None = None, subtitle_size: int | None = None, subtitles: str | None = None, max_video_bitrate: int | None = None, video_resolution: str | None = None, copyts: str | None = None, video_bitrate: int | None = None, video_quality: int | None = None) -> str:
    """Transcode subtitles.

    GET /{transcodeType}/:/transcode/universal/subtitles

    Args:
        transcode_type: Path parameter.
        platform: Client platform (some clients send this in addition to headers).
        audio_boost: Percentage of original audio loudness to use when transcoding (100 is equivalent to original volume, 50 is half, 200 is double, etc)
        audio_channel_count: Target video number of audio channels.
        auto_adjust_quality: Indicates the client supports ABR.
        auto_adjust_subtitle: Indicates if the server should adjust subtitles based on Voice Activity Data.
        direct_play: Indicates the client supports direct playing the indicated content.
        direct_stream: Indicates the client supports direct streaming the video of the indicated content.
        direct_stream_audio: Indicates the client supports direct streaming the audio of the indicated content.
        disable_resolution_rotation: Indicates if resolution should be adjusted for orientation.
        has_mde: Ignore client profiles when determining if direct play is possible. Only has an effect when directPlay=1 and both mediaIndex and partIndex are specified and neither are -1
        location: Network type of the client, can be used to help determine target bitrate.
        media_buffer_size: Buffer size used in playback (in KB). Clients should specify a lower bound if not known exactly. This value could make the difference between transcoding and direct play on bandwidth constrained networks.
        media_index: Index of the media to transcode. -1 or not specified indicates let the server choose.
        music_bitrate: Target bitrate for audio only files (in kbps, used to transcode).
        offset: Offset from the start of the media (in seconds).
        part_index: Index of the part to transcode. -1 or not specified indicates the server should join parts together in a transcode
        path: Internal PMS path of the media to transcode.
        peak_bitrate: Maximum bitrate (in kbps) to use in ABR.
        photo_resolution: Target photo resolution.
        protocol: Indicates the network streaming protocol to be used for the transcode session: * 'http' - include the file in the http response such as MKV streaming * 'hls' - hls stream (RFC 8216) * 'dash' - dash stream (ISO/IEC 23009-1:2022)
        seconds_per_segment: Number of seconds to include in each transcoded segment
        subtitle_size: Percentage of original subtitle size to use when burning subtitles (100 is equivalent to original size, 50 is half, ect)
        subtitles: Indicates how subtitles should be included: * 'auto' - Compute the appropriate subtitle setting automatically * 'burn' - Burn the selected subtitle; auto if no selected subtitle * 'none' - Ignore all subtitle streams * 'sidecar' - The selected subtitle should be provided as a sidecar * 'embedded' - The selected subtitle should be provided as an embedded stream * 'segmented' - The selected subtitle should be provided as a segmented stream
        max_video_bitrate: Client-side maximum video bitrate cap in kbps
        video_resolution: Cap resolution string (e.g. 1920x1080)
        copyts: Copy timestamps instead of re-encoding them
        video_bitrate: Target video bitrate (in kbps).
        video_quality: Target photo quality.
    """
    return call("GET", f"/{transcode_type}/:/transcode/universal/subtitles", query={"platform": platform, "audioBoost": audio_boost, "audioChannelCount": audio_channel_count, "autoAdjustQuality": auto_adjust_quality, "autoAdjustSubtitle": auto_adjust_subtitle, "directPlay": direct_play, "directStream": direct_stream, "directStreamAudio": direct_stream_audio, "disableResolutionRotation": disable_resolution_rotation, "hasMDE": has_mde, "location": location, "mediaBufferSize": media_buffer_size, "mediaIndex": media_index, "musicBitrate": music_bitrate, "offset": offset, "partIndex": part_index, "path": path, "peakBitrate": peak_bitrate, "photoResolution": photo_resolution, "protocol": protocol, "secondsPerSegment": seconds_per_segment, "subtitleSize": subtitle_size, "subtitles": subtitles, "maxVideoBitrate": max_video_bitrate, "videoResolution": video_resolution, "copyts": copyts, "videoBitrate": video_bitrate, "videoQuality": video_quality}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_download_queue_by_queue_id(queue_id: int) -> str:
    """Get a download queue.

    GET /downloadQueue/{queueId}

    Args:
        queue_id: The queue id
    """
    return call("GET", f"/downloadQueue/{queue_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_download_queue_by_queue_id_item_by_item_id_decision(queue_id: int, item_id: int) -> str:
    """Grab download queue item decision.

    GET /downloadQueue/{queueId}/item/{itemId}/decision

    Args:
        queue_id: The queue id
        item_id: The item ids
    """
    return call("GET", f"/downloadQueue/{queue_id}/item/{item_id}/decision", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_download_queue_by_queue_id_item_by_item_id_media(queue_id: int, item_id: int) -> str:
    """Grab download queue media.

    GET /downloadQueue/{queueId}/item/{itemId}/media

    Args:
        queue_id: The queue id
        item_id: The item ids
    """
    return call("GET", f"/downloadQueue/{queue_id}/item/{item_id}/media", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_download_queue_by_queue_id_items(queue_id: int) -> str:
    """Get download queue items.

    GET /downloadQueue/{queueId}/items

    Args:
        queue_id: The queue id
    """
    return call("GET", f"/downloadQueue/{queue_id}/items", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_download_queue_by_queue_id_items_by_item_id(queue_id: int, item_id: list) -> str:
    """Get download queue items.

    GET /downloadQueue/{queueId}/items/{itemId}

    Args:
        queue_id: The queue id
        item_id: The item ids
    """
    return call("GET", f"/downloadQueue/{queue_id}/items/{item_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_downloads_by_channel_json(channel: str) -> str:
    """Get Plex Downloads.

    GET /downloads/{channel}.json

    Args:
        channel: The channel identifier
    """
    return call("GET", f"/downloads/{channel}.json", query=None, body=None, form=None, host='https://plex.tv')


@mcp.tool(annotations=_READ)
def get_hubs_metadata_by_metadata_id(metadata_id: int, only_transient: str | None = None) -> str:
    """Get hubs for section by metadata item.

    GET /hubs/metadata/{metadataId}

    Args:
        metadata_id: The metadata ID for the hubs to fetch
        only_transient: Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)
    """
    return call("GET", f"/hubs/metadata/{metadata_id}", query={"onlyTransient": only_transient}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_hubs_metadata_by_metadata_id_postplay(metadata_id: int, only_transient: str | None = None) -> str:
    """Get postplay hubs.

    GET /hubs/metadata/{metadataId}/postplay

    Args:
        metadata_id: The metadata ID for the hubs to fetch
        only_transient: Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)
    """
    return call("GET", f"/hubs/metadata/{metadata_id}/postplay", query={"onlyTransient": only_transient}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_hubs_metadata_by_metadata_id_related(metadata_id: int, only_transient: str | None = None) -> str:
    """Get related hubs.

    GET /hubs/metadata/{metadataId}/related

    Args:
        metadata_id: The metadata ID for the hubs to fetch
        only_transient: Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)
    """
    return call("GET", f"/hubs/metadata/{metadata_id}/related", query={"onlyTransient": only_transient}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_hubs_sections_by_section_id(section_id: int, only_transient: str | None = None) -> str:
    """Get section hubs.

    GET /hubs/sections/{sectionId}

    Args:
        section_id: The section ID for the hubs to fetch
        only_transient: Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)
    """
    return call("GET", f"/hubs/sections/{section_id}", query={"onlyTransient": only_transient}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_hubs_sections_by_section_id_manage(section_id: int, metadata_item_id: int | None = None) -> str:
    """Get hubs.

    GET /hubs/sections/{sectionId}/manage

    Args:
        section_id: The section ID for the hubs to reorder
        metadata_item_id: Restrict hubs to ones relevant to the provided metadata item
    """
    return call("GET", f"/hubs/sections/{section_id}/manage", query={"metadataItemId": metadata_item_id}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_collections_by_collection_id_composite_by_updated_at(collection_id: int, updated_at: int) -> str:
    """Get a collection's image.

    GET /library/collections/{collectionId}/composite/{updatedAt}

    Args:
        collection_id: The collection id
        updated_at: The update time of the image.  Used for busting cache.
    """
    return call("GET", f"/library/collections/{collection_id}/composite/{updated_at}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_collections_by_collection_id_items(collection_id: int) -> str:
    """Get items in a collection.

    GET /library/collections/{collectionId}/items

    Args:
        collection_id: The collection id
    """
    return call("GET", f"/library/collections/{collection_id}/items", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_media_by_media_id_chapter_images_by_chapter(media_id: int, chapter: int) -> str:
    """Get a chapter image.

    GET /library/media/{mediaId}/chapterImages/{chapter}

    Args:
        media_id: The id of the media item
        chapter: The index of the chapter
    """
    return call("GET", f"/library/media/{media_id}/chapterImages/{chapter}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_augmentations_by_augmentation_id(augmentation_id: str, wait: str | None = None) -> str:
    """Get augmentation status.

    GET /library/metadata/augmentations/{augmentationId}

    Args:
        augmentation_id: The id of the augmentation
        wait: Wait for augmentation completion before returning
    """
    return call("GET", f"/library/metadata/augmentations/{augmentation_id}", query={"wait": wait}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_id_children(id: int) -> str:
    """Get Metadata Children.

    GET /library/metadata/{id}/children

    Args:
        id: The unique identifier of the item
    """
    return call("GET", f"/library/metadata/{id}/children", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_id_compute_path(id: int) -> str:
    """Compute Sonic Path.

    GET /library/metadata/{id}/computePath

    Args:
        id: The unique identifier of the item
    """
    return call("GET", f"/library/metadata/{id}/computePath", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_id_grandchildren(id: int) -> str:
    """Get Metadata Grandchildren.

    GET /library/metadata/{id}/grandchildren

    Args:
        id: The unique identifier of the item
    """
    return call("GET", f"/library/metadata/{id}/grandchildren", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_id_grandparent(id: int) -> str:
    """Get Metadata Grandparent.

    GET /library/metadata/{id}/grandparent

    Args:
        id: The unique identifier of the item
    """
    return call("GET", f"/library/metadata/{id}/grandparent", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_id_nearest(id: int, exclude_parent_id: int | None = None, exclude_grandparent_id: int | None = None, limit: int | None = None, max_distance: float | None = None) -> str:
    """Get Nearest Metadata.

    GET /library/metadata/{id}/nearest

    Args:
        id: The unique identifier of the item
        exclude_parent_id: The unique identifier of the excludeparent
        exclude_grandparent_id: The unique identifier of the excludegrandparent
        limit: Maximum number of items to return
        max_distance: The maxDistance
    """
    return call("GET", f"/library/metadata/{id}/nearest", query={"excludeParentID": exclude_parent_id, "excludeGrandparentID": exclude_grandparent_id, "limit": limit, "maxDistance": max_distance}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_id_on_deck(id: int) -> str:
    """Get Metadata On Deck.

    GET /library/metadata/{id}/onDeck

    Args:
        id: The unique identifier of the item
    """
    return call("GET", f"/library/metadata/{id}/onDeck", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_id_parent(id: int) -> str:
    """Get Metadata Parent.

    GET /library/metadata/{id}/parent

    Args:
        id: The unique identifier of the item
    """
    return call("GET", f"/library/metadata/{id}/parent", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_id_reviews(id: int) -> str:
    """Get Metadata Reviews.

    GET /library/metadata/{id}/reviews

    Args:
        id: The unique identifier of the item
    """
    return call("GET", f"/library/metadata/{id}/reviews", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_ids(ids: list, async_check_files: str | None = None, async_refresh_local_media_agent: str | None = None, async_refresh_analysis: str | None = None, check_files: str | None = None, skip_refresh: str | None = None, check_file_availability: str | None = None, async_augment_metadata: str | None = None, augment_count: str | None = None, include_markers: bool | None = None, include_guids: bool | None = None, include_chapters: bool | None = None, include_external_media: bool | None = None, include_extras: bool | None = None, include_related: bool | None = None, include_on_deck: bool | None = None, include_popular_leaves: bool | None = None, include_reviews: bool | None = None, include_stations: bool | None = None, exclude_elements: str | None = None, exclude_fields: str | None = None) -> str:
    """Get a metadata item.

    GET /library/metadata/{ids}

    Args:
        ids: Comma-separated list of IDs
        async_check_files: Determines if file check should be performed asynchronously.  An activity is created to indicate progress.  Default is false.
        async_refresh_local_media_agent: Determines if local media agent refresh should be performed asynchronously.  An activity is created to indicate progress.  Default is false.
        async_refresh_analysis: Determines if analysis refresh should be performed asynchronously.  An activity is created to indicate progress.  Default is false.
        check_files: Determines if file check should be performed synchronously.  Specifying `asyncCheckFiles` will cause this option to be ignored.  Default is false.
        skip_refresh: Determines if synchronous local media agent and analysis refresh should be skipped.  Specifying async versions will cause synchronous versions to be skipped.  Default is false.
        check_file_availability: Determines if file existence check should be performed synchronously.  Specifying `checkFiles` will imply this option.  Default is false.
        async_augment_metadata: Add metadata augmentations.  An activity is created to indicate progress.  Option will be ignored if specified by non-admin or if multiple metadata items are requested.  Default is false.
        augment_count: Number of augmentations to add.  Requires `asyncAugmentMetadata` to be specified.
        include_markers: Include intro/credits markers in the response
        include_guids: Include external GUIDs (e.g. TMDB, TVDB) in the response
        include_chapters: Include chapter data in the response
        include_external_media: Include external/online media in the response
        include_extras: Include trailers, behind-the-scenes, and other extras
        include_related: Include related items in the response
        include_on_deck: Include On Deck status in the response
        include_popular_leaves: Include popular episodes in the response
        include_reviews: Include user reviews in the response
        include_stations: Include radio station data in the response
        exclude_elements: Comma-separated list of elements to exclude from the response
        exclude_fields: Comma-separated list of fields to exclude from the response
    """
    return call("GET", f"/library/metadata/{ids}", query={"asyncCheckFiles": async_check_files, "asyncRefreshLocalMediaAgent": async_refresh_local_media_agent, "asyncRefreshAnalysis": async_refresh_analysis, "checkFiles": check_files, "skipRefresh": skip_refresh, "checkFileAvailability": check_file_availability, "asyncAugmentMetadata": async_augment_metadata, "augmentCount": augment_count, "includeMarkers": include_markers, "includeGuids": include_guids, "includeChapters": include_chapters, "includeExternalMedia": include_external_media, "includeExtras": include_extras, "includeRelated": include_related, "includeOnDeck": include_on_deck, "includePopularLeaves": include_popular_leaves, "includeReviews": include_reviews, "includeStations": include_stations, "excludeElements": exclude_elements, "excludeFields": exclude_fields}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_ids_all_leaves(ids: str) -> str:
    """Get the leaves of an item.

    GET /library/metadata/{ids}/allLeaves

    Args:
        ids: Comma-separated list of IDs
    """
    return call("GET", f"/library/metadata/{ids}/allLeaves", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_ids_by_element_by_timestamp(ids: str, element: str, timestamp: int) -> str:
    """Get an item's artwork, theme, etc.

    GET /library/metadata/{ids}/{element}/{timestamp}

    Args:
        ids: Comma-separated list of IDs
        element: The type of artwork element (e.g., art, poster, thumb)
        timestamp: A timestamp on the element used for cache management in the client
    """
    return call("GET", f"/library/metadata/{ids}/{element}/{timestamp}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_ids_extras(ids: str) -> str:
    """Get an item's extras.

    GET /library/metadata/{ids}/extras

    Args:
        ids: Comma-separated list of IDs
    """
    return call("GET", f"/library/metadata/{ids}/extras", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_ids_file(ids: str, url: str | None = None) -> str:
    """Get a file from a metadata or media bundle.

    GET /library/metadata/{ids}/file

    Args:
        ids: Comma-separated list of IDs
        url: The bundle url, typically starting with `metadata://` or `media://`
    """
    return call("GET", f"/library/metadata/{ids}/file", query={"url": url}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_ids_related(ids: str) -> str:
    """Get related items.

    GET /library/metadata/{ids}/related

    Args:
        ids: Comma-separated list of IDs
    """
    return call("GET", f"/library/metadata/{ids}/related", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_ids_similar(ids: str) -> str:
    """Get similar items.

    GET /library/metadata/{ids}/similar

    Args:
        ids: Comma-separated list of IDs
    """
    return call("GET", f"/library/metadata/{ids}/similar", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_ids_subtitles(ids: str, title: str | None = None, language: str | None = None, media_item_id: int | None = None, url: str | None = None, format: str | None = None, forced: str | None = None, hearing_impaired: str | None = None) -> str:
    """Get subtitles.

    GET /library/metadata/{ids}/subtitles

    Args:
        ids: Comma-separated list of IDs
        title: The title to filter by
        language: The language code to use
        media_item_id: The unique identifier of the mediaitem
        url: The URL of the subtitle.  If not provided, the contents of the subtitle must be in the post body
        format: The format
        forced: The forced
        hearing_impaired: The hearingImpaired
    """
    return call("GET", f"/library/metadata/{ids}/subtitles", query={"title": title, "language": language, "mediaItemID": media_item_id, "url": url, "format": format, "forced": forced, "hearingImpaired": hearing_impaired}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_ids_tree(ids: str) -> str:
    """Get metadata items as a tree.

    GET /library/metadata/{ids}/tree

    Args:
        ids: Comma-separated list of IDs
    """
    return call("GET", f"/library/metadata/{ids}/tree", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_metadata_by_ids_users_top(ids: str) -> str:
    """Get metadata top users.

    GET /library/metadata/{ids}/users/top

    Args:
        ids: Comma-separated list of IDs
    """
    return call("GET", f"/library/metadata/{ids}/users/top", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_parts_by_part_id_by_changestamp_by_filename(part_id: int, changestamp: int, filename: str, download: str | None = None) -> str:
    """Get a media part.

    GET /library/parts/{partId}/{changestamp}/{filename}

    Args:
        part_id: The part id who's index is to be fetched
        changestamp: The changestamp of the part; used for busting potential caches.  Provided in the `key` for the part
        filename: A generic filename used for a client media stack which relies on the extension in the request.  Provided in the `key` for the part
        download: Whether this is a file download
    """
    return call("GET", f"/library/parts/{part_id}/{changestamp}/{filename}", query={"download": download}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_parts_by_part_id_indexes_by_index(part_id: int, index: str, interval: int | None = None) -> str:
    """Get BIF index for a part.

    GET /library/parts/{partId}/indexes/{index}

    Args:
        part_id: The part id who's index is to be fetched
        index: The type of index to grab.
        interval: The interval between images to return in ms.
    """
    return call("GET", f"/library/parts/{part_id}/indexes/{index}", query={"interval": interval}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_parts_by_part_id_indexes_by_index_by_offset(part_id: int, index: str, offset: int) -> str:
    """Get an image from part BIF.

    GET /library/parts/{partId}/indexes/{index}/{offset}

    Args:
        part_id: The part id who's index is to be fetched
        index: The type of index to grab.
        offset: The offset to seek in ms.
    """
    return call("GET", f"/library/parts/{part_id}/indexes/{index}/{offset}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_people_by_person_id(person_id: str) -> str:
    """Get person details.

    GET /library/people/{personId}

    Args:
        person_id: Either the PMS tag `id` of the person or `tagKey` of the actor.  Note the `tagKey` is the hex portion of the plex guid for the actor
    """
    return call("GET", f"/library/people/{person_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_people_by_person_id_media(person_id: str) -> str:
    """Get media for a person.

    GET /library/people/{personId}/media

    Args:
        person_id: Either the PMS tag `id` of the person or `tagKey` of the actor.  Note the `tagKey` is the hex portion of the plex guid for the actor
    """
    return call("GET", f"/library/people/{person_id}/media", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id(section_id: str, include_details: str | None = None) -> str:
    """Get a library section by id.

    GET /library/sections/{sectionId}

    Args:
        section_id: The section identifier
        include_details: Whether or not to include details for a section (types, filters, and sorts). Only exists for backwards compatibility, media providers other than the server libraries have it on always.
    """
    return call("GET", f"/library/sections/{section_id}", query={"includeDetails": include_details}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_agents(section_id: int) -> str:
    """Get Section Agents.

    GET /library/sections/{sectionId}/agents

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/agents", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_albums(section_id: int) -> str:
    """Set section albums.

    GET /library/sections/{sectionId}/albums

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/albums", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_all(section_id: int, include_meta: str | None = None, include_guids: str | None = None, include_collections: str | None = None, include_external_media: str | None = None, include_advanced: str | None = None, check_files: str | None = None, include_related: str | None = None, include_extras: str | None = None, include_popular_leaves: str | None = None, include_concerts: str | None = None, include_on_deck: str | None = None, include_chapters: str | None = None, include_preferences: str | None = None, include_bandwidths: str | None = None, include_loudness_ramps: str | None = None, include_stations: str | None = None, include_external_ids: str | None = None, include_reviews: str | None = None, include_credits: str | None = None, include_art: str | None = None, include_thumb: str | None = None, include_banner: str | None = None, include_theme: str | None = None, include_fields: str | None = None, exclude_fields: str | None = None, async_augment_metadata: str | None = None, async_refresh_local_media_agent: str | None = None, nocache: str | None = None, skip_refresh: str | None = None, exclude_elements: str | None = None, filters: str | None = None, unwatched: str | None = None, genre: str | None = None, studio: str | None = None, content_rating: str | None = None, resolution: str | None = None, year: int | None = None, first_character: str | None = None) -> str:
    """Get items in the section.

    GET /library/sections/{sectionId}/all

    Args:
        section_id: The id of the section
        include_meta: Adds the Meta object to the response
        include_guids: Adds the Guid object to the response
        include_collections: Include collection items in results
        include_external_media: Include external or online media
        include_advanced: Include advanced settings
        check_files: Verify file existence
        include_related: Include related items
        include_extras: Include trailers, behind-the-scenes, etc.
        include_popular_leaves: Include popular episodes
        include_concerts: Include concert items
        include_on_deck: Include On Deck status
        include_chapters: Include chapter markers
        include_preferences: Include user preferences
        include_bandwidths: Include bandwidth info
        include_loudness_ramps: Include loudness ramp data
        include_stations: Include radio station data
        include_external_ids: Include external GUIDs
        include_reviews: Include user reviews
        include_credits: Include full credits
        include_art: Force inclusion of artwork fields
        include_thumb: Force inclusion of thumbnail fields
        include_banner: Force inclusion of banner fields
        include_theme: Force inclusion of theme fields
        include_fields: Whitelist of fields to return
        exclude_fields: Blacklist of fields to omit
        async_augment_metadata: Async metadata augmentation
        async_refresh_local_media_agent: Async local media agent refresh
        nocache: Bypass cache
        skip_refresh: Skip synchronous refresh
        exclude_elements: Comma-separated list of elements to exclude from the response
        filters: General filtering expression.
        unwatched: Filter to unwatched only (1 = true).
        genre: Filter by genre.
        studio: Filter by studio.
        content_rating: Filter by content rating.
        resolution: Filter by resolution.
        year: Filter by year.
        first_character: Filter by first character of title.
    """
    return call("GET", f"/library/sections/{section_id}/all", query={"includeMeta": include_meta, "includeGuids": include_guids, "includeCollections": include_collections, "includeExternalMedia": include_external_media, "includeAdvanced": include_advanced, "checkFiles": check_files, "includeRelated": include_related, "includeExtras": include_extras, "includePopularLeaves": include_popular_leaves, "includeConcerts": include_concerts, "includeOnDeck": include_on_deck, "includeChapters": include_chapters, "includePreferences": include_preferences, "includeBandwidths": include_bandwidths, "includeLoudnessRamps": include_loudness_ramps, "includeStations": include_stations, "includeExternalIds": include_external_ids, "includeReviews": include_reviews, "includeCredits": include_credits, "includeArt": include_art, "includeThumb": include_thumb, "includeBanner": include_banner, "includeTheme": include_theme, "includeFields": include_fields, "excludeFields": exclude_fields, "asyncAugmentMetadata": async_augment_metadata, "asyncRefreshLocalMediaAgent": async_refresh_local_media_agent, "nocache": nocache, "skipRefresh": skip_refresh, "excludeElements": exclude_elements, "filters": filters, "unwatched": unwatched, "genre": genre, "studio": studio, "contentRating": content_rating, "resolution": resolution, "year": year, "firstCharacter": first_character}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_all_leaves(section_id: int) -> str:
    """Set section leaves.

    GET /library/sections/{sectionId}/allLeaves

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/allLeaves", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_artists(section_id: int) -> str:
    """Get Section Artists.

    GET /library/sections/{sectionId}/artists

    Args:
        section_id: The id of the section
    """
    return call("GET", f"/library/sections/{section_id}/artists", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_arts(section_id: int) -> str:
    """Set section artwork.

    GET /library/sections/{sectionId}/arts

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/arts", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_autocomplete(section_id: int, field_query: str | None = None) -> str:
    """Get autocompletions for search.

    GET /library/sections/{sectionId}/autocomplete

    Args:
        section_id: Section identifier
        field_query: The "field" stands in for any field, the value is a partial string for matching
    """
    return call("GET", f"/library/sections/{section_id}/autocomplete", query={"field.query": field_query}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_by_content_rating(section_id: int) -> str:
    """Get By Content Rating.

    GET /library/sections/{sectionId}/byContentRating

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/byContentRating", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_by_decade(section_id: int) -> str:
    """Get By Decade.

    GET /library/sections/{sectionId}/byDecade

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/byDecade", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_by_folder(section_id: int) -> str:
    """Get By Folder.

    GET /library/sections/{sectionId}/byFolder

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/byFolder", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_by_resolution(section_id: int) -> str:
    """Get By Resolution.

    GET /library/sections/{sectionId}/byResolution

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/byResolution", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_by_year(section_id: int) -> str:
    """Get By Year.

    GET /library/sections/{sectionId}/byYear

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/byYear", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_categories(section_id: int) -> str:
    """Set section categories.

    GET /library/sections/{sectionId}/categories

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/categories", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_clips(section_id: int) -> str:
    """Get Section Clips.

    GET /library/sections/{sectionId}/clips

    Args:
        section_id: The id of the section
    """
    return call("GET", f"/library/sections/{section_id}/clips", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_cluster(section_id: int) -> str:
    """Set section clusters.

    GET /library/sections/{sectionId}/cluster

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/cluster", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_collections(section_id: int) -> str:
    """Get collections in a section.

    GET /library/sections/{sectionId}/collections

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/collections", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_common(section_id: int) -> str:
    """Get common fields for items.

    GET /library/sections/{sectionId}/common

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/common", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_composite_by_updated_at(section_id: int, updated_at: int) -> str:
    """Get a section composite image.

    GET /library/sections/{sectionId}/composite/{updatedAt}

    Args:
        section_id: Section identifier
        updated_at: The update time of the image.  Used for busting cache.
    """
    return call("GET", f"/library/sections/{section_id}/composite/{updated_at}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_compute_path(section_id: int, start_id: int | None = None, end_id: int | None = None, max_distance: float | None = None) -> str:
    """Similar tracks to transition from one to another.

    GET /library/sections/{sectionId}/computePath

    Args:
        section_id: Section identifier
        start_id: The starting metadata item id
        end_id: The ending metadata item id
        max_distance: The maximum distance allowed along the path; defaults to 0.25
    """
    return call("GET", f"/library/sections/{section_id}/computePath", query={"startID": start_id, "endID": end_id, "maxDistance": max_distance}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_edit(section_id: int) -> str:
    """Edit Section.

    GET /library/sections/{sectionId}/edit

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/edit", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_empty_trash(section_id: int) -> str:
    """Get Empty Trash.

    GET /library/sections/{sectionId}/emptyTrash

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/emptyTrash", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_episodes(section_id: int) -> str:
    """Get Section Episodes.

    GET /library/sections/{sectionId}/episodes

    Args:
        section_id: The id of the section
    """
    return call("GET", f"/library/sections/{section_id}/episodes", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_filters(section_id: int) -> str:
    """Get section filters.

    GET /library/sections/{sectionId}/filters

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/filters", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_first_characters(section_id: int) -> str:
    """Get list of first characters.

    GET /library/sections/{sectionId}/firstCharacters

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/firstCharacters", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_hubs(section_id: int) -> str:
    """Get Section Hubs.

    GET /library/sections/{sectionId}/hubs

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/hubs", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_label(section_id: int) -> str:
    """Get Section Labels.

    GET /library/sections/{sectionId}/label

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/label", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_location(section_id: int) -> str:
    """Get all folder locations.

    GET /library/sections/{sectionId}/location

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/location", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_match(section_id: int) -> str:
    """Match Section Items.

    GET /library/sections/{sectionId}/match

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/match", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_moment(section_id: int) -> str:
    """Set section moments.

    GET /library/sections/{sectionId}/moment

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/moment", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_movies(section_id: int) -> str:
    """Get Section Movies.

    GET /library/sections/{sectionId}/movies

    Args:
        section_id: The id of the section
    """
    return call("GET", f"/library/sections/{section_id}/movies", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_nearest(section_id: int, type: int | None = None, values: list | None = None, limit: int | None = None, max_distance: float | None = None) -> str:
    """The nearest audio tracks.

    GET /library/sections/{sectionId}/nearest

    Args:
        section_id: Section identifier
        type: The metadata type to fetch (should be 10 for audio track)
        values: The music analysis to center the search.  Typically obtained from the `musicAnalysis` of a track
        limit: The limit of the number of items to fetch; defaults to 50
        max_distance: The maximum distance to search, defaults to 0.25
    """
    return call("GET", f"/library/sections/{section_id}/nearest", query={"type": type, "values": values, "limit": limit, "maxDistance": max_distance}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_newest(section_id: int) -> str:
    """Get Newest for Section.

    GET /library/sections/{sectionId}/newest

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/newest", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_on_deck(section_id: int) -> str:
    """Get On Deck for Section.

    GET /library/sections/{sectionId}/onDeck

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/onDeck", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_optimize(section_id: int) -> str:
    """Get Optimize Section.

    GET /library/sections/{sectionId}/optimize

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/optimize", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_photos(section_id: int) -> str:
    """Get Section Photos.

    GET /library/sections/{sectionId}/photos

    Args:
        section_id: The id of the section
    """
    return call("GET", f"/library/sections/{section_id}/photos", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_playlists(section_id: int) -> str:
    """Get Section Playlists.

    GET /library/sections/{sectionId}/playlists

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/playlists", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_prefs(section_id: int, agent: str | None = None) -> str:
    """Get section prefs.

    GET /library/sections/{sectionId}/prefs

    Args:
        section_id: Section identifier
        agent: The identifier of the metadata agent to use
    """
    return call("GET", f"/library/sections/{section_id}/prefs", query={"agent": agent}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_recently_added(section_id: int) -> str:
    """Get Recently Added for Section.

    GET /library/sections/{sectionId}/recentlyAdded

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/recentlyAdded", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_refresh(section_id: int) -> str:
    """Get Refresh Section.

    GET /library/sections/{sectionId}/refresh

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/refresh", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_search(section_id: int) -> str:
    """Search Section.

    GET /library/sections/{sectionId}/search

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/search", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_settings(section_id: int) -> str:
    """Get Section Settings.

    GET /library/sections/{sectionId}/settings

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/settings", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_shows(section_id: int) -> str:
    """Get Section Shows.

    GET /library/sections/{sectionId}/shows

    Args:
        section_id: The id of the section
    """
    return call("GET", f"/library/sections/{section_id}/shows", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_sorts(section_id: int) -> str:
    """Get a section sorts.

    GET /library/sections/{sectionId}/sorts

    Args:
        section_id: Section identifier
    """
    return call("GET", f"/library/sections/{section_id}/sorts", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_tags(section_id: int) -> str:
    """Get Section Tags.

    GET /library/sections/{sectionId}/tags

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/tags", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_timeline(section_id: int) -> str:
    """Get Section Timeline.

    GET /library/sections/{sectionId}/timeline

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/timeline", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_unmatch(section_id: int) -> str:
    """Unmatch Section Items.

    GET /library/sections/{sectionId}/unmatch

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/unmatch", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_sections_by_section_id_unwatched(section_id: int) -> str:
    """Get Unwatched for Section.

    GET /library/sections/{sectionId}/unwatched

    Args:
        section_id: The unique identifier of the library section
    """
    return call("GET", f"/library/sections/{section_id}/unwatched", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_streams_by_stream_id_ext(stream_id: int, ext: str, encoding: str | None = None, format: str | None = None, auto_adjust_subtitle: str | None = None) -> str:
    """Get a stream.

    GET /library/streams/{streamId}.{ext}

    Args:
        stream_id: The id of the stream
        ext: The extension of the stream.  Required to fetch the `sub` portion of `idx`/`sub` subtitles
        encoding: The requested encoding for the subtitle (only used for text subtitles)
        format: The requested format for the subtitle to convert the subtitles to (only used for text subtitles)
        auto_adjust_subtitle: Whether the server should attempt to automatically adjust the subtitle timestamps to match the media
    """
    return call("GET", f"/library/streams/{stream_id}.{ext}", query={"encoding": encoding, "format": format, "autoAdjustSubtitle": auto_adjust_subtitle}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_streams_by_stream_id_levels(stream_id: int, subsample: int | None = None) -> str:
    """Get loudness about a stream in json.

    GET /library/streams/{streamId}/levels

    Args:
        stream_id: The id of the stream
        subsample: Subsample result down to return only the provided number of samples
    """
    return call("GET", f"/library/streams/{stream_id}/levels", query={"subsample": subsample}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_library_streams_by_stream_id_loudness(stream_id: int, subsample: int | None = None) -> str:
    """Get loudness about a stream.

    GET /library/streams/{streamId}/loudness

    Args:
        stream_id: The id of the stream
        subsample: Subsample result down to return only the provided number of samples
    """
    return call("GET", f"/library/streams/{stream_id}/loudness", query={"subsample": subsample}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_livetv_dvrs_by_dvr_id(dvr_id: int) -> str:
    """Get a single DVR.

    GET /livetv/dvrs/{dvrId}

    Args:
        dvr_id: The ID of the DVR.
    """
    return call("GET", f"/livetv/dvrs/{dvr_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_livetv_dvrs_by_dvr_id_channels(dvr_id: int) -> str:
    """Get DVR Channels.

    GET /livetv/dvrs/{dvrId}/channels

    Args:
        dvr_id: The ID of the DVR.
    """
    return call("GET", f"/livetv/dvrs/{dvr_id}/channels", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_livetv_dvrs_by_dvr_id_guide(dvr_id: int) -> str:
    """Get DVR Guide.

    GET /livetv/dvrs/{dvrId}/guide

    Args:
        dvr_id: The ID of the DVR.
    """
    return call("GET", f"/livetv/dvrs/{dvr_id}/guide", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_livetv_dvrs_by_dvr_id_recordings(dvr_id: int) -> str:
    """Get DVR Recordings by DVR.

    GET /livetv/dvrs/{dvrId}/recordings

    Args:
        dvr_id: The ID of the DVR.
    """
    return call("GET", f"/livetv/dvrs/{dvr_id}/recordings", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_livetv_epg_countries_by_country_by_epg_id_lineups(country: str, epg_id: str, postal_code: str | None = None) -> str:
    """Get lineups for a country via postal code.

    GET /livetv/epg/countries/{country}/{epgId}/lineups

    Args:
        country: 3 letter country code
        epg_id: The `providerIdentifier` of the provider
        postal_code: The postal code for the lineups to fetch
    """
    return call("GET", f"/livetv/epg/countries/{country}/{epg_id}/lineups", query={"postalCode": postal_code}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_livetv_epg_countries_by_country_by_epg_id_regions(country: str, epg_id: str) -> str:
    """Get regions for a country.

    GET /livetv/epg/countries/{country}/{epgId}/regions

    Args:
        country: 3 letter country code
        epg_id: The `providerIdentifier` of the provider
    """
    return call("GET", f"/livetv/epg/countries/{country}/{epg_id}/regions", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_livetv_epg_countries_by_country_by_epg_id_regions_by_region_lineups(country: str, epg_id: str, region: str) -> str:
    """Get lineups for a region.

    GET /livetv/epg/countries/{country}/{epgId}/regions/{region}/lineups

    Args:
        country: 3 letter country code
        epg_id: The `providerIdentifier` of the provider
        region: The region for the lineup
    """
    return call("GET", f"/livetv/epg/countries/{country}/{epg_id}/regions/{region}/lineups", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_livetv_sessions_by_session_id(session_id: str) -> str:
    """Get a single session.

    GET /livetv/sessions/{sessionId}

    Args:
        session_id: The session id
    """
    return call("GET", f"/livetv/sessions/{session_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_livetv_sessions_by_session_id_by_consumer_id_by_segment_id(session_id: str, consumer_id: str, segment_id: str) -> str:
    """Get a single session segment.

    GET /livetv/sessions/{sessionId}/{consumerId}/{segmentId}

    Args:
        session_id: The session id
        consumer_id: The consumer id
        segment_id: The segment id
    """
    return call("GET", f"/livetv/sessions/{session_id}/{consumer_id}/{segment_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_livetv_sessions_by_session_id_by_consumer_id_index_m3u8(session_id: str, consumer_id: str) -> str:
    """Get a session playlist index.

    GET /livetv/sessions/{sessionId}/{consumerId}/index.m3u8

    Args:
        session_id: The session id
        consumer_id: The consumer id
    """
    return call("GET", f"/livetv/sessions/{session_id}/{consumer_id}/index.m3u8", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_media_grabbers_devices_by_device_id(device_id: int) -> str:
    """Get device details.

    GET /media/grabbers/devices/{deviceId}

    Args:
        device_id: The ID of the device.
    """
    return call("GET", f"/media/grabbers/devices/{device_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_media_grabbers_devices_by_device_id_channels(device_id: int) -> str:
    """Get a device's channels.

    GET /media/grabbers/devices/{deviceId}/channels

    Args:
        device_id: The ID of the device.
    """
    return call("GET", f"/media/grabbers/devices/{device_id}/channels", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_media_grabbers_devices_by_device_id_thumb_by_version(device_id: int, version: int) -> str:
    """Get device thumb.

    GET /media/grabbers/devices/{deviceId}/thumb/{version}

    Args:
        device_id: The ID of the device.
        version: A version number of the thumb used for busting cache
    """
    return call("GET", f"/media/grabbers/devices/{device_id}/thumb/{version}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_media_subscriptions_by_subscription_id(subscription_id: int, include_grabs: str | None = None, include_storage: str | None = None) -> str:
    """Get a single subscription.

    GET /media/subscriptions/{subscriptionId}

    Args:
        subscription_id: The unique identifier of the subscription
        include_grabs: Indicates whether the active grabs should be included as well
        include_storage: Compute the storage of recorded items desired by this subscription
    """
    return call("GET", f"/media/subscriptions/{subscription_id}", query={"includeGrabs": include_grabs, "includeStorage": include_storage}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_pins_by_pin_id(pin_id: int) -> str:
    """Get OAuth PIN Status.

    GET /pins/{pinId}

    Args:
        pin_id: The unique identifier of the pin
    """
    return call("GET", f"/pins/{pin_id}", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def get_play_queues_by_play_queue_id(play_queue_id: int, own: str | None = None, center: str | None = None, window: int | None = None, include_before: str | None = None, include_after: str | None = None) -> str:
    """Retrieve a play queue.

    GET /playQueues/{playQueueId}

    Args:
        play_queue_id: The ID of the play queue.
        own: If the server should transfer ownership to the requesting client (used in remote control scenarios).
        center: The play queue item ID for the center of the window - this doesn't change the current selected item.
        window: How many items on each side of the center of the window
        include_before: Whether to include the items before the center (if 0, center is not included either), defaults to 1.
        include_after: Whether to include the items after the center (if 0, center is not included either), defaults to 1.
    """
    return call("GET", f"/playQueues/{play_queue_id}", query={"own": own, "center": center, "window": window, "includeBefore": include_before, "includeAfter": include_after}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_playlists_by_playlist_id(playlist_id: int) -> str:
    """Retrieve Playlist.

    GET /playlists/{playlistId}

    Args:
        playlist_id: The ID of the playlist
    """
    return call("GET", f"/playlists/{playlist_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_playlists_by_playlist_id_generators(playlist_id: int) -> str:
    """Get a playlist's generators.

    GET /playlists/{playlistId}/generators

    Args:
        playlist_id: The ID of the playlist
    """
    return call("GET", f"/playlists/{playlist_id}/generators", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_playlists_by_playlist_id_items(playlist_id: int, type: list | None = None) -> str:
    """Retrieve Playlist Contents.

    GET /playlists/{playlistId}/items

    Args:
        playlist_id: The ID of the playlist
        type: The metadata types of the item to return.  Values past the first are only used in fetching items from the background processing playlist.
    """
    return call("GET", f"/playlists/{playlist_id}/items", query={"type": type}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_playlists_by_playlist_id_items_by_generator_id(playlist_id: int, generator_id: int) -> str:
    """Get a playlist generator.

    GET /playlists/{playlistId}/items/{generatorId}

    Args:
        playlist_id: The ID of the playlist
        generator_id: The generator item ID to delete.
    """
    return call("GET", f"/playlists/{playlist_id}/items/{generator_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_playlists_by_playlist_id_items_by_generator_id_items(playlist_id: int, generator_id: int) -> str:
    """Get a playlist generator's items.

    GET /playlists/{playlistId}/items/{generatorId}/items

    Args:
        playlist_id: The ID of the playlist
        generator_id: The generator item ID to delete.
    """
    return call("GET", f"/playlists/{playlist_id}/items/{generator_id}/items", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_servers_by_machine_id(machine_id: str) -> str:
    """Get Server Details.

    GET /servers/{machineId}

    Args:
        machine_id: The unique machine identifier of the server
    """
    return call("GET", f"/servers/{machine_id}", query=None, body=None, form=None, host='https://plex.tv/api')


@mcp.tool(annotations=_READ)
def get_services_browse_by_base64path(base64path: str) -> str:
    """Browse Filesystem Path.

    GET /services/browse/{base64path}

    Args:
        base64path: The base64path
    """
    return call("GET", f"/services/browse/{base64path}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_status_sessions_history_by_history_id(history_id: int) -> str:
    """Get Single History Item.

    GET /status/sessions/history/{historyId}

    Args:
        history_id: The id of the history item (the `historyKey` from above)
    """
    return call("GET", f"/status/sessions/history/{history_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_sync_items_by_sync_id(sync_id: int) -> str:
    """Get Sync Item.

    GET /sync/items/{syncId}

    Args:
        sync_id: The unique identifier of the sync item
    """
    return call("GET", f"/sync/items/{sync_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_system_agents_by_agent_id(agent_id: str) -> str:
    """Get Metadata Agent Details.

    GET /system/agents/{agentId}

    Args:
        agent_id: The unique identifier of the metadata agent
    """
    return call("GET", f"/system/agents/{agent_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def get_user_by_uuid_settings_opt_outs(uuid: str) -> str:
    """Get User Opt-Outs.

    GET /user/{uuid}/settings/opt_outs

    Args:
        uuid: The universally unique identifier
    """
    return call("GET", f"/user/{uuid}/settings/opt_outs", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_accounts() -> str:
    """Get System Accounts.

    GET /accounts
    """
    return call("GET", "/accounts", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_activities() -> str:
    """Get all activities.

    GET /activities
    """
    return call("GET", "/activities", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_auth_keys() -> str:
    """Get Auth Keys.

    GET /auth/keys
    """
    return call("GET", "/auth/keys", query=None, body=None, form=None, host='https://clients.plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_auth_nonce() -> str:
    """Get Auth Nonce.

    GET /auth/nonce
    """
    return call("GET", "/auth/nonce", query=None, body=None, form=None, host='https://clients.plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_butler() -> str:
    """Get all Butler tasks.

    GET /butler
    """
    return call("GET", "/butler", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_claim_token_json() -> str:
    """Get Claim Token.

    GET /claim/token.json
    """
    return call("GET", "/claim/token.json", query=None, body=None, form=None, host='https://plex.tv/api')


@mcp.tool(annotations=_READ)
def list_clients() -> str:
    """Get Clients.

    GET /clients
    """
    return call("GET", "/clients", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_cloud_server() -> str:
    """Get Cloud Server.

    GET /cloud_server
    """
    return call("GET", "/cloud_server", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_devices() -> str:
    """Get System Devices.

    GET /devices
    """
    return call("GET", "/devices", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_diagnostics() -> str:
    """Get Diagnostics.

    GET /diagnostics
    """
    return call("GET", "/diagnostics", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_diagnostics_databases() -> str:
    """Download Database Diagnostics.

    GET /diagnostics/databases
    """
    return call("GET", "/diagnostics/databases", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_diagnostics_logs() -> str:
    """Download Log Bundle.

    GET /diagnostics/logs
    """
    return call("GET", "/diagnostics/logs", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_eventsource_notifications(filter: list | None = None) -> str:
    """Connect to Eventsource.

    GET /:/eventsource/notifications

    Args:
        filter: By default, all events except logs are sent. A rich filtering mechanism is provided to allow clients to opt into or out of each event type using the `filters` parameter. For example:

- `filters=-log`: All event types except logs (the default).
- `filters=foo,bar`: Only the foo and bar event types.
- `filters=`: All events types.
- `filters=-foo,bar`: All event types except foo and bar.
    """
    return call("GET", "/:/eventsource/notifications", query={"filter": filter}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_features() -> str:
    """Get Features.

    GET /features
    """
    return call("GET", "/features", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_friends() -> str:
    """Get Friends.

    GET /friends
    """
    return call("GET", "/friends", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_geoip() -> str:
    """Get GeoIP.

    GET /geoip
    """
    return call("GET", "/geoip", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_home() -> str:
    """Get home hubs.

    GET /home
    """
    return call("GET", "/home", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_home_users() -> str:
    """Get home hubs Users.

    GET /home/users
    """
    return call("GET", "/home/users", query=None, body=None, form=None, host='https://plex.tv/api')


@mcp.tool(annotations=_READ)
def list_hubs(only_transient: str | None = None, identifier: list | None = None) -> str:
    """Get global hubs.

    GET /hubs

    Args:
        only_transient: Only return hubs which are "transient", meaning those which are prone to changing after media playback or addition (e.g. On Deck, or Recently Added)
        identifier: If provided, limit to only specified hubs
    """
    return call("GET", "/hubs", query={"onlyTransient": only_transient, "identifier": identifier}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_hubs_continue_watching() -> str:
    """Get the continue watching hub.

    GET /hubs/continueWatching
    """
    return call("GET", "/hubs/continueWatching", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_hubs_continue_watching_items() -> str:
    """Get Continue Watching Items.

    GET /hubs/continueWatching/items
    """
    return call("GET", "/hubs/continueWatching/items", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_hubs_home_recently_added() -> str:
    """Get home hubs Recently Added.

    GET /hubs/home/recentlyAdded
    """
    return call("GET", "/hubs/home/recentlyAdded", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_hubs_items(identifier: list | None = None) -> str:
    """Get a hub's items.

    GET /hubs/items

    Args:
        identifier: If provided, limit to only specified hubs
    """
    return call("GET", "/hubs/items", query={"identifier": identifier}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_hubs_promoted() -> str:
    """Get the hubs which are promoted.

    GET /hubs/promoted
    """
    return call("GET", "/hubs/promoted", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_hubs_search(query: str | None = None, section_id: int | None = None, limit: int | None = None, include_collections: bool | None = None) -> str:
    """Search Hub.

    GET /hubs/search

    Args:
        query: The query term
        section_id: This gives context to the search, and can result in re-ordering of search result hubs.
        limit: The number of items to return per hub.  3 if not specified
        include_collections: Include collection results in search hubs
    """
    return call("GET", "/hubs/search", query={"query": query, "sectionId": section_id, "limit": limit, "includeCollections": include_collections}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_hubs_search_voice(query: str | None = None, limit: int | None = None, include_collections: bool | None = None) -> str:
    """Voice Search Hub.

    GET /hubs/search/voice

    Args:
        query: The query term
        limit: The number of items to return per hub.  3 if not specified
        include_collections: Include collection results in search hubs
    """
    return call("GET", "/hubs/search/voice", query={"query": query, "limit": limit, "includeCollections": include_collections}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_identity() -> str:
    """Get PMS identity.

    GET /identity
    """
    return call("GET", "/identity", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_ip() -> str:
    """Get IP.

    GET /ip
    """
    return call("GET", "/ip", query=None, body=None, form=None, host='https://plex.tv')


@mcp.tool(annotations=_READ)
def list_library() -> str:
    """Get Root Library.

    GET /library
    """
    return call("GET", "/library", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_library_all() -> str:
    """Get all items in library.

    GET /library/all
    """
    return call("GET", "/library/all", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_library_matches(include_full_metadata: str | None = None, include_ancestor_metadata: str | None = None, include_alternate_metadata_sources: str | None = None, guid: str | None = None, year: int | None = None, path: str | None = None, grandparent_title: str | None = None, grandparent_year: int | None = None, parent_index: int | None = None, index: int | None = None, originally_available_at: str | None = None, parent_title: str | None = None) -> str:
    """Get library matches.

    GET /library/matches

    Args:
        include_full_metadata: Include full metadata in the response
        include_ancestor_metadata: Include ancestor metadata in the response
        include_alternate_metadata_sources: Include alternate metadata sources in the response
        guid: Used for movies, shows, artists, albums, and tracks.  Allowed for various URI schemes, to be defined.
        year: Used for movies shows, and albums.  Optional.
        path: Used for movies, episodes, and tracks.  The full path to the media file, used for "cloud-scanning" an item.
        grandparent_title: Used for episodes and tracks.  The title of the show/artist. Required if `path` isn't passed.
        grandparent_year: Used for episodes.  The year of the show.
        parent_index: Used for episodes and tracks.  The season/album number.
        index: Used for episodes and tracks.  The episode/tracks number in the season/album.
        originally_available_at: Used for episodes.  In the format `YYYY-MM-DD`.
        parent_title: Used for albums and tracks. The artist name for albums or the album name for tracks.
    """
    return call("GET", "/library/matches", query={"includeFullMetadata": include_full_metadata, "includeAncestorMetadata": include_ancestor_metadata, "includeAlternateMetadataSources": include_alternate_metadata_sources, "guid": guid, "year": year, "path": path, "grandparentTitle": grandparent_title, "grandparentYear": grandparent_year, "parentIndex": parent_index, "index": index, "originallyAvailableAt": originally_available_at, "parentTitle": parent_title}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_library_optimize() -> str:
    """Get Optimize Library.

    GET /library/optimize
    """
    return call("GET", "/library/optimize", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_library_random_artwork(sections: list | None = None) -> str:
    """Get random artwork.

    GET /library/randomArtwork

    Args:
        sections: The sections for which to fetch artwork.
    """
    return call("GET", "/library/randomArtwork", query={"sections": sections}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_library_recently_added() -> str:
    """Get Global Recently Added.

    GET /library/recentlyAdded
    """
    return call("GET", "/library/recentlyAdded", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_library_search(query: str | None = None, limit: int | None = None, search_types: str | None = None, search_providers: str | None = None, include_metadata: int | None = None) -> str:
    """Search Discover.

    GET /library/search

    Args:
        query: The search query string
        limit: Maximum number of items to return
        search_types: Types of content to search for
        search_providers: Providers to include in the search
        include_metadata: Include metadata in the search results
    """
    return call("GET", "/library/search", query={"query": query, "limit": limit, "searchTypes": search_types, "searchProviders": search_providers, "includeMetadata": include_metadata}, body=None, form=None, host='https://discover.provider.plex.tv')


@mcp.tool(annotations=_READ)
def list_library_sections() -> str:
    """Get Library Sections (Fallback).

    GET /library/sections/
    """
    return call("GET", "/library/sections/", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_library_sections_all() -> str:
    """Get library sections (main Media Provider Only).

    GET /library/sections/all
    """
    return call("GET", "/library/sections/all", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_library_sections_prefs(type: int | None = None, agent: str | None = None) -> str:
    """Get section prefs.

    GET /library/sections/prefs

    Args:
        type: The metadata type
        agent: The metadata agent in use
    """
    return call("GET", "/library/sections/prefs", query={"type": type, "agent": agent}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_library_sections_watchlist_all() -> str:
    """Get Watchlist.

    GET /library/sections/watchlist/all
    """
    return call("GET", "/library/sections/watchlist/all", query=None, body=None, form=None, host='https://discover.provider.plex.tv')


@mcp.tool(annotations=_READ)
def list_library_tags() -> str:
    """Get all library tags of a type.

    GET /library/tags
    """
    return call("GET", "/library/tags", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_livetv_dvrs(uuid: str | None = None, lineup: str | None = None) -> str:
    """Get DVRs.

    GET /livetv/dvrs

    Args:
        uuid: Filter by DVR UUID.
        lineup: Filter by lineup.
    """
    return call("GET", "/livetv/dvrs", query={"uuid": uuid, "lineup": lineup}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_livetv_epg_channelmap(device: str | None = None, lineup: str | None = None) -> str:
    """Compute the best channel map.

    GET /livetv/epg/channelmap

    Args:
        device: The URI describing the device
        lineup: The URI describing the lineup
    """
    return call("GET", "/livetv/epg/channelmap", query={"device": device, "lineup": lineup}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_livetv_epg_channels(lineup: str | None = None) -> str:
    """Get channels for a lineup.

    GET /livetv/epg/channels

    Args:
        lineup: The URI describing the lineup
    """
    return call("GET", "/livetv/epg/channels", query={"lineup": lineup}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_livetv_epg_countries() -> str:
    """Get all countries.

    GET /livetv/epg/countries
    """
    return call("GET", "/livetv/epg/countries", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_livetv_epg_guide() -> str:
    """Get EPG Guide.

    GET /livetv/epg/guide
    """
    return call("GET", "/livetv/epg/guide", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_livetv_epg_languages() -> str:
    """Get all languages.

    GET /livetv/epg/languages
    """
    return call("GET", "/livetv/epg/languages", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_livetv_epg_lineup(device: str | None = None, lineup_group: str | None = None) -> str:
    """Compute the best lineup.

    GET /livetv/epg/lineup

    Args:
        device: The URI describing the device
        lineup_group: The URI describing the lineupGroup
    """
    return call("GET", "/livetv/epg/lineup", query={"device": device, "lineupGroup": lineup_group}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_livetv_epg_lineupchannels(lineup: list | None = None) -> str:
    """Get the channels for multiple lineups.

    GET /livetv/epg/lineupchannels

    Args:
        lineup: The URIs describing the lineups
    """
    return call("GET", "/livetv/epg/lineupchannels", query={"lineup": lineup}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_livetv_epg_search() -> str:
    """Search EPG.

    GET /livetv/epg/search
    """
    return call("GET", "/livetv/epg/search", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_livetv_recordings() -> str:
    """Get DVR Recordings.

    GET /livetv/recordings
    """
    return call("GET", "/livetv/recordings", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_livetv_sessions(dvr_id: int | None = None, channel: int | None = None) -> str:
    """Get all sessions.

    GET /livetv/sessions

    Args:
        dvr_id: Filter by DVR ID.
        channel: Filter by channel ID.
    """
    return call("GET", "/livetv/sessions", query={"dvrId": dvr_id, "channel": channel}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_media_grabbers(protocol: str | None = None) -> str:
    """Get available grabbers.

    GET /media/grabbers

    Args:
        protocol: Only return grabbers providing this protocol.
    """
    return call("GET", "/media/grabbers", query={"protocol": protocol}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_media_grabbers_devices() -> str:
    """Get all devices.

    GET /media/grabbers/devices
    """
    return call("GET", "/media/grabbers/devices", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_media_grabbers_devices_discover(protocol: str | None = None, grabber_identifier: str | None = None) -> str:
    """Tell grabbers to discover devices.

    GET /media/grabbers/devices/discover

    Args:
        protocol: Protocol to filter discovery.
        grabber_identifier: Targeted grabber identifier.
    """
    return call("GET", "/media/grabbers/devices/discover", query={"protocol": protocol, "grabberIdentifier": grabber_identifier}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_media_providers() -> str:
    """Get the list of available media providers.

    GET /media/providers
    """
    return call("GET", "/media/providers", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_media_subscriptions(include_grabs: str | None = None, include_storage: str | None = None) -> str:
    """Get all subscriptions.

    GET /media/subscriptions

    Args:
        include_grabs: Indicates whether the active grabs should be included as well
        include_storage: Compute the storage of recorded items desired by this subscription
    """
    return call("GET", "/media/subscriptions", query={"includeGrabs": include_grabs, "includeStorage": include_storage}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_media_subscriptions_scheduled() -> str:
    """Get all scheduled recordings.

    GET /media/subscriptions/scheduled
    """
    return call("GET", "/media/subscriptions/scheduled", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_media_subscriptions_template(guid: str | None = None, type: str | None = None, target_library_section_id: int | None = None) -> str:
    """Get the subscription template.

    GET /media/subscriptions/template

    Args:
        guid: The guid of the item for which to get the template
        type: Subscription type.
        target_library_section_id: Target library section ID.
    """
    return call("GET", "/media/subscriptions/template", query={"guid": guid, "type": type, "targetLibrarySectionID": target_library_section_id}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_music_transcode() -> str:
    """Transcode Music.

    GET /music/:/transcode
    """
    return call("GET", "/music/:/transcode", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_myplex_account() -> str:
    """Get MyPlex Account.

    GET /myplex/account
    """
    return call("GET", "/myplex/account", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_photo_transcode(url: str | None = None, format: str | None = None, width: int | None = None, height: int | None = None, quality: int | None = None, background: str | None = None, upscale: str | None = None, min_size: str | None = None, rotate: str | None = None, blur: int | None = None, saturation: int | None = None, opacity: int | None = None, chroma_subsampling: int | None = None, blend_color: str | None = None) -> str:
    """Transcode an image.

    GET /photo/:/transcode

    Args:
        url: The source URL for the image to transcode.  Note, if this URL requires a token such as `X-Plex-Token`, it should be given as a query parameter to this url.
        format: The output format for the image; defaults to jpg
        width: The desired width of the output image
        height: The desired height of the output image
        quality: The desired quality of the output.  -1 means the highest quality.  Defaults to -1
        background: The background color to apply before painting the image.  Only really applicable if image has transparency.  Defaults to none
        upscale: Indicates if image should be upscaled to the desired width/height.  Defaults to false
        min_size: Indicates if image should be scaled to fit the smaller dimension.  By default (false) the image is scaled to fit within the width/height specified but if this parameter is true, it will allow overflowing one dimension to fit the other.  Essentially it is making the width/height minimum sizes of the image or sizing the image to fill the entire width/height even if it overflows one dimension.
        rotate: Obey the rotation values specified in EXIF data.  Defaults to true.
        blur: Apply a blur to the image, Defaults to 0 (none)
        saturation: Scale the image saturation by the specified percentage.  Defaults to 100
        opacity: Render the image at the specified opacity percentage.  Defaults to 100
        chroma_subsampling: Use the specified chroma subsambling.
  - 0: 411
  - 1: 420
  - 2: 422
  - 3: 444
Defaults to 3 (444)
        blend_color: The color to blend with the image.  Defaults to none
    """
    return call("GET", "/photo/:/transcode", query={"url": url, "format": format, "width": width, "height": height, "quality": quality, "background": background, "upscale": upscale, "minSize": min_size, "rotate": rotate, "blur": blur, "saturation": saturation, "opacity": opacity, "chromaSubsampling": chroma_subsampling, "blendColor": blend_color}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_ping() -> str:
    """Ping the server.

    GET /ping
    """
    return call("GET", "/ping", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_play_queues_1() -> str:
    """Get Conversion Queue.

    GET /playQueues/1
    """
    return call("GET", "/playQueues/1", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_player_resources() -> str:
    """Get Client Resources.

    GET /player/resources
    """
    return call("GET", "/player/resources", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_player_timeline_poll() -> str:
    """Player Poll Timeline.

    GET /player/timeline/poll
    """
    return call("GET", "/player/timeline/poll", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_playlists(playlist_type: str | None = None, type: int | None = None) -> str:
    """List playlists.

    GET /playlists

    Args:
        playlist_type: Limit to a type of playlist
        type: Filter by playlist type. Use 42 for optimized/conversion items.
    """
    return call("GET", "/playlists", query={"playlistType": playlist_type, "type": type}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_prefs() -> str:
    """Get all preferences.

    GET /:/prefs
    """
    return call("GET", "/:/prefs", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_prefs_get(id: str | None = None) -> str:
    """Get a preferences.

    GET /:/prefs/get

    Args:
        id: The preference to fetch
    """
    return call("GET", "/:/prefs/get", query={"id": id}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_progress(key: str | None = None, time: int | None = None) -> str:
    """Get Progress.

    GET /:/progress

    Args:
        key: The metadata key of the item
        time: The current playback position in milliseconds
    """
    return call("GET", "/:/progress", query={"key": key, "time": time}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_resources() -> str:
    """Get Legacy Resources.

    GET /api/resources
    """
    return call("GET", "/api/resources", query=None, body=None, form=None, host='https://plex.tv/api')


@mcp.tool(annotations=_READ)
def list_resources_2(include_https: str | None = None, include_relay: str | None = None, include_ipv6: str | None = None) -> str:
    """Get Server Resources.

    GET /resources

    Args:
        include_https: Include Https entries in the results
        include_relay: Include Relay addresses in the results 
E.g: https://10-0-0-25.bbf8e10c7fa20447cacee74cd9914cde.plex.direct:32400
        include_ipv6: Include IPv6 entries in the results
    """
    return call("GET", "/resources", query={"includeHttps": include_https, "includeRelay": include_relay, "includeIPv6": include_ipv6}, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_root() -> str:
    """Get PMS info.

    GET /
    """
    return call("GET", "/", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_security_resources(source: str | None = None, refresh: str | None = None) -> str:
    """Get Source Connection Information.

    GET /security/resources

    Args:
        source: The source identifier with an included prefix.
        refresh: Force refresh
    """
    return call("GET", "/security/resources", query={"source": source, "refresh": refresh}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_server() -> str:
    """Get User Server Association.

    GET /server
    """
    return call("GET", "/server", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_server_access_tokens() -> str:
    """Get Server Access Tokens.

    GET /server/access_tokens
    """
    return call("GET", "/server/access_tokens", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_server_users_features() -> str:
    """Get Server User Features.

    GET /server/users/features
    """
    return call("GET", "/server/users/features", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_servers() -> str:
    """Get Local Servers.

    GET /servers
    """
    return call("GET", "/servers", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_services_browse(include_files: str | None = None) -> str:
    """Browse Filesystem.

    GET /services/browse

    Args:
        include_files: Include files in browse results
    """
    return call("GET", "/services/browse", query={"includeFiles": include_files}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_services_ultrablur_colors(url: str | None = None) -> str:
    """Get UltraBlur Colors.

    GET /services/ultrablur/colors

    Args:
        url: Url for image which requires color extraction. Can be relative PMS library path or absolute url.
    """
    return call("GET", "/services/ultrablur/colors", query={"url": url}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_services_ultrablur_image(top_left: str | None = None, top_right: str | None = None, bottom_right: str | None = None, bottom_left: str | None = None, width: int | None = None, height: int | None = None, noise: str | None = None) -> str:
    """Get UltraBlur Image.

    GET /services/ultrablur/image

    Args:
        top_left: The base color (hex) for the top left quadrant.
        top_right: The base color (hex) for the top right quadrant.
        bottom_right: The base color (hex) for the bottom right quadrant.
        bottom_left: The base color (hex) for the bottom left quadrant.
        width: Width in pixels for the image.
        height: Height in pixels for the image.
        noise: Whether to add noise to the ouput image. Noise can reduce color banding with the gradients. Image sizes with noise will be larger.
    """
    return call("GET", "/services/ultrablur/image", query={"topLeft": top_left, "topRight": top_right, "bottomRight": bottom_right, "bottomLeft": bottom_left, "width": width, "height": height, "noise": noise}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_statistics_bandwidth(timespan: int | None = None, account_id: int | None = None, device_id: int | None = None, lan: str | None = None) -> str:
    """Get Bandwidth Statistics.

    GET /statistics/bandwidth

    Args:
        timespan: Dashboard timespan (1-6)
        account_id: Filter by account ID
        device_id: Filter by device ID
        lan: Filter to LAN-only traffic
    """
    return call("GET", "/statistics/bandwidth", query={"timespan": timespan, "accountID": account_id, "deviceID": device_id, "lan": lan}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_statistics_resources() -> str:
    """Get Resource Statistics.

    GET /statistics/resources
    """
    return call("GET", "/statistics/resources", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_status_sessions() -> str:
    """List Sessions.

    GET /status/sessions
    """
    return call("GET", "/status/sessions", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_status_sessions_background() -> str:
    """Get background tasks.

    GET /status/sessions/background
    """
    return call("GET", "/status/sessions/background", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_status_sessions_history_all(account_id: int | None = None, viewed_at: int | None = None, library_section_id: int | None = None, metadata_item_id: int | None = None, sort: list | None = None, exclude_elements: str | None = None, exclude_fields: str | None = None, include_fields: str | None = None, include_elements: str | None = None, viewed_at_query: int | None = None, viewed_at_query_2: int | None = None, device_id: int | None = None) -> str:
    """List Playback History.

    GET /status/sessions/history/all

    Args:
        account_id: The account id to restrict view history
        viewed_at: The time period to restrict history (typically of the form `viewedAt>=12456789`)
        library_section_id: The library section id to restrict view history
        metadata_item_id: The metadata item to restrict view history (can provide the id for a show to see all of that show's view history).  Note this is translated to `metadata_items.id`, `parents.id`, or `grandparents.id` internally depending on the metadata type.
        sort: The field on which to sort.  Multiple orderings can be specified separated by `,` and the direction specified following a `:` (`desc` or `asc`; `asc` is assumed if not provided).  Note `metadataItemID` may not be used here.
        exclude_elements: Comma-separated list of elements to exclude from the response
        exclude_fields: Comma-separated list of fields to exclude from the response
        include_fields: Whitelist of fields to return
        include_elements: Whitelist of elements to include
        viewed_at_query: Greater-than filter for viewedAt timestamp
        viewed_at_query_2: Less-than filter for viewedAt timestamp
        device_id: Filter by device ID
    """
    return call("GET", "/status/sessions/history/all", query={"accountID": account_id, "viewedAt": viewed_at, "librarySectionID": library_section_id, "metadataItemID": metadata_item_id, "sort": sort, "excludeElements": exclude_elements, "excludeFields": exclude_fields, "includeFields": include_fields, "includeElements": include_elements, "viewedAt>": viewed_at_query, "viewedAt<": viewed_at_query_2, "deviceID": device_id}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_sync() -> str:
    """Get Sync Status.

    GET /sync
    """
    return call("GET", "/sync", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_sync_items() -> str:
    """Get Sync Items.

    GET /sync/items
    """
    return call("GET", "/sync/items", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_sync_queue() -> str:
    """Get Sync Queue.

    GET /sync/queue
    """
    return call("GET", "/sync/queue", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_sync_transcode_queue() -> str:
    """Get Sync Transcode Queue.

    GET /sync/transcodeQueue
    """
    return call("GET", "/sync/transcodeQueue", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_system_agents() -> str:
    """Get Metadata Agents.

    GET /system/agents
    """
    return call("GET", "/system/agents", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_system_settings() -> str:
    """Get System Settings.

    GET /system/settings
    """
    return call("GET", "/system/settings", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_system_updates() -> str:
    """Check for System Updates.

    GET /system/updates
    """
    return call("GET", "/system/updates", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_transcode_sessions() -> str:
    """Get Transcode Sessions.

    GET /transcode/sessions
    """
    return call("GET", "/transcode/sessions", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_updater_status() -> str:
    """Querying status of updates.

    GET /updater/status
    """
    return call("GET", "/updater/status", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_user() -> str:
    """Get Token Details.

    GET /user
    """
    return call("GET", "/user", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_users() -> str:
    """Get Legacy Users.

    GET /api/users/
    """
    return call("GET", "/api/users/", query=None, body=None, form=None, host='https://plex.tv/api')


@mcp.tool(annotations=_READ)
def list_users_2() -> str:
    """Get list of all connected users.

    GET /users
    """
    return call("GET", "/users", query=None, body=None, form=None, host='https://plex.tv/api')


@mcp.tool(annotations=_READ)
def list_users_account() -> str:
    """Get Account (XML).

    GET /users/account
    """
    return call("GET", "/users/account", query=None, body=None, form=None, host='https://plex.tv')


@mcp.tool(annotations=_READ)
def list_users_account_json() -> str:
    """Get Account (JSON).

    GET /users/account.json
    """
    return call("GET", "/users/account.json", query=None, body=None, form=None, host='https://plex.tv')


@mcp.tool(annotations=_READ)
def list_v2_user_webhooks() -> str:
    """User Webhooks.

    GET /api/v2/user/webhooks
    """
    return call("GET", "/api/v2/user/webhooks", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_webhooks() -> str:
    """Get Webhooks.

    GET /webhooks
    """
    return call("GET", "/webhooks", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_READ)
def list_websocket_notifications(filter: list | None = None) -> str:
    """Connect to WebSocket.

    GET /:/websocket/notifications

    Args:
        filter: By default, all events except logs are sent. A rich filtering mechanism is provided to allow clients to opt into or out of each event type using the `filters` parameter. For example:

- `filters=-log`: All event types except logs (the default).
- `filters=foo,bar`: Only the foo and bar event types.
- `filters=`: All events types.
- `filters=-foo,bar`: All event types except foo and bar.
    """
    return call("GET", "/:/websocket/notifications", query={"filter": filter}, body=None, form=None, host='server')


@mcp.tool(annotations=_READ)
def list_websockets_notifications() -> str:
    """Get WebSocket Notifications.

    GET /:/websockets/notifications
    """
    return call("GET", "/:/websockets/notifications", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def patch_livetv_dvrs_by_dvr_id(dvr_id: int) -> str:
    """Update DVR Settings.

    PATCH /livetv/dvrs/{dvrId}

    Args:
        dvr_id: The ID of the DVR.
    """
    return call("PATCH", f"/livetv/dvrs/{dvr_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_actions_remove_from_continue_watching(key: str | None = None) -> str:
    """Remove From Continue Watching.

    PUT /actions/removeFromContinueWatching

    Args:
        key: The metadata key of the item
    """
    return call("PUT", "/actions/removeFromContinueWatching", query={"key": key}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_home_users_by_user_id(user_id: int) -> str:
    """Update Home User.

    PUT /home/users/{userId}

    Args:
        user_id: The unique identifier of the user
    """
    return call("PUT", f"/home/users/{user_id}", query=None, body=None, form=None, host='https://plex.tv/api')


@mcp.tool(annotations=_WRITE)
def update_home_users_restricted_by_user_id(user_id: int) -> str:
    """Update Restricted User.

    PUT /home/users/restricted/{userId}

    Args:
        user_id: The unique identifier of the user
    """
    return call("PUT", f"/home/users/restricted/{user_id}", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_WRITE)
def update_hubs_sections_by_section_id_manage_by_identifier(section_id: int, identifier: str, promoted_to_recommended: str | None = None, promoted_to_own_home: str | None = None, promoted_to_shared_home: str | None = None) -> str:
    """Change hub visibility.

    PUT /hubs/sections/{sectionId}/manage/{identifier}

    Args:
        section_id: The section ID for the hubs to change
        identifier: The identifier of the hub to change
        promoted_to_recommended: Whether this hub should be displayed in recommended
        promoted_to_own_home: Whether this hub should be displayed in admin's home
        promoted_to_shared_home: Whether this hub should be displayed in shared user's home
    """
    return call("PUT", f"/hubs/sections/{section_id}/manage/{identifier}", query={"promotedToRecommended": promoted_to_recommended, "promotedToOwnHome": promoted_to_own_home, "promotedToSharedHome": promoted_to_shared_home}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_hubs_sections_by_section_id_manage_move(section_id: int, identifier: str | None = None, after: str | None = None) -> str:
    """Move Hub.

    PUT /hubs/sections/{sectionId}/manage/move

    Args:
        section_id: The section ID for the hubs to reorder
        identifier: The identifier of the hub to move
        after: The identifier of the hub to order this hub after (or empty/missing to put this hub first)
    """
    return call("PUT", f"/hubs/sections/{section_id}/manage/move", query={"identifier": identifier, "after": after}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_invites_requests_by_invite_id(invite_id: int, friend: str | None = None, home: str | None = None, server: str | None = None) -> str:
    """Accept an Invite.

    PUT /api/invites/requests/{inviteId}

    Args:
        invite_id: The pending invitation ID.
        friend: Whether the invitation includes a friend relationship.
        home: Whether the invitation includes Plex Home membership.
        server: Whether the invitation includes access to a shared server.
    """
    return call("PUT", f"/api/invites/requests/{invite_id}", query={"friend": friend, "home": home, "server": server}, body=None, form=None, host='https://plex.tv')


@mcp.tool(annotations=_WRITE)
def update_library_clean_bundles() -> str:
    """Clean bundles.

    PUT /library/clean/bundles
    """
    return call("PUT", "/library/clean/bundles", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_collections_by_collection_id_items(collection_id: int, uri: str | None = None) -> str:
    """Add items to a collection.

    PUT /library/collections/{collectionId}/items

    Args:
        collection_id: The collection id
        uri: The URI describing the items to add to this collection
    """
    return call("PUT", f"/library/collections/{collection_id}/items", query={"uri": uri}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_collections_by_collection_id_items_by_item_id(collection_id: int, item_id: int) -> str:
    """Update an item in a collection.

    PUT /library/collections/{collectionId}/items/{itemId}

    Args:
        collection_id: The collection id
        item_id: The item to delete
    """
    return call("PUT", f"/library/collections/{collection_id}/items/{item_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_collections_by_collection_id_items_by_item_id_move(collection_id: int, item_id: int, after: int | None = None) -> str:
    """Reorder an item in the collection.

    PUT /library/collections/{collectionId}/items/{itemId}/move

    Args:
        collection_id: The collection id
        item_id: The item to move
        after: The item to move this item after.  If not provided, this item will be moved to the beginning
    """
    return call("PUT", f"/library/collections/{collection_id}/items/{item_id}/move", query={"after": after}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids(ids: list, args: dict | None = None) -> str:
    """Edit a metadata item.

    PUT /library/metadata/{ids}

    Args:
        ids: Comma-separated list of IDs
        args: The new values for the metadata item
    """
    return call("PUT", f"/library/metadata/{ids}", query={"args": args}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_addetect(ids: str) -> str:
    """Ad-detect an item.

    PUT /library/metadata/{ids}/addetect

    Args:
        ids: Comma-separated list of IDs
    """
    return call("PUT", f"/library/metadata/{ids}/addetect", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_analyze(ids: str, thumb_offset: float | None = None, art_offset: float | None = None) -> str:
    """Analyze an item.

    PUT /library/metadata/{ids}/analyze

    Args:
        ids: Comma-separated list of IDs
        thumb_offset: Set the offset to be used for thumbnails
        art_offset: Set the offset to be used for artwork
    """
    return call("PUT", f"/library/metadata/{ids}/analyze", query={"thumbOffset": thumb_offset, "artOffset": art_offset}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_by_element(ids: str, element: str, url: str | None = None) -> str:
    """Set an item's artwork, theme, etc.

    PUT /library/metadata/{ids}/{element}

    Args:
        ids: Comma-separated list of IDs
        element: The type of artwork element (e.g., art, poster, thumb)
        url: The url of the new asset.
    """
    return call("PUT", f"/library/metadata/{ids}/{element}", query={"url": url}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_chapter_thumbs(ids: str, force: str | None = None) -> str:
    """Generate thumbs of chapters for an item.

    PUT /library/metadata/{ids}/chapterThumbs

    Args:
        ids: Comma-separated list of IDs
        force: Force the operation even if conditions are not met
    """
    return call("PUT", f"/library/metadata/{ids}/chapterThumbs", query={"force": force}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_credits(ids: str, force: str | None = None, manual: str | None = None) -> str:
    """Credit detect a metadata item.

    PUT /library/metadata/{ids}/credits

    Args:
        ids: Comma-separated list of IDs
        force: Force the operation even if conditions are not met
        manual: Whether to perform the operation manually
    """
    return call("PUT", f"/library/metadata/{ids}/credits", query={"force": force, "manual": manual}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_index(ids: str, force: str | None = None) -> str:
    """Start BIF generation of an item.

    PUT /library/metadata/{ids}/index

    Args:
        ids: Comma-separated list of IDs
        force: Force the operation even if conditions are not met
    """
    return call("PUT", f"/library/metadata/{ids}/index", query={"force": force}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_intro(ids: str, force: str | None = None, threshold: float | None = None) -> str:
    """Intro detect an item.

    PUT /library/metadata/{ids}/intro

    Args:
        ids: Comma-separated list of IDs
        force: Indicate whether detection should be re-run
        threshold: The threshold for determining if content is an intro or not
    """
    return call("PUT", f"/library/metadata/{ids}/intro", query={"force": force, "threshold": threshold}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_marker_by_marker(ids: str, marker: str, type: int | None = None, start_time_offset: int | None = None, end_time_offset: int | None = None, attributes: dict | None = None) -> str:
    """Edit a marker.

    PUT /library/metadata/{ids}/marker/{marker}

    Args:
        ids: Comma-separated list of IDs
        marker: The id of the marker to edit
        type: The type of marker to edit/create
        start_time_offset: The start time of the marker
        end_time_offset: The end time of the marker
        attributes: The attributes to assign to this marker
    """
    return call("PUT", f"/library/metadata/{ids}/marker/{marker}", query={"type": type, "startTimeOffset": start_time_offset, "endTimeOffset": end_time_offset, "attributes": attributes}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_match(ids: str, guid: str | None = None, name: str | None = None, year: int | None = None) -> str:
    """Match a metadata item.

    PUT /library/metadata/{ids}/match

    Args:
        ids: Comma-separated list of IDs
        guid: The guid
        name: The name
        year: The year to filter by
    """
    return call("PUT", f"/library/metadata/{ids}/match", query={"guid": guid, "name": name, "year": year}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_matches(ids: str, title: str | None = None, parent_title: str | None = None, agent: str | None = None, language: str | None = None, year: int | None = None, manual: str | None = None) -> str:
    """Get metadata matches for an item.

    PUT /library/metadata/{ids}/matches

    Args:
        ids: Comma-separated list of IDs
        title: The title to filter by
        parent_title: The parentTitle
        agent: The identifier of the metadata agent to use
        language: The language code to use
        year: The year to filter by
        manual: Whether to perform the operation manually
    """
    return call("PUT", f"/library/metadata/{ids}/matches", query={"title": title, "parentTitle": parent_title, "agent": agent, "language": language, "year": year, "manual": manual}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_merge(ids: str, ids_query: list | None = None) -> str:
    """Merge a metadata item.

    PUT /library/metadata/{ids}/merge

    Args:
        ids: Comma-separated list of IDs
        ids_query: Comma-separated list of item identifiers
    """
    return call("PUT", f"/library/metadata/{ids}/merge", query={"ids": ids_query}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_prefs(ids: str, args: dict | None = None) -> str:
    """Set metadata preferences.

    PUT /library/metadata/{ids}/prefs

    Args:
        ids: Comma-separated list of IDs
        args: The args
    """
    return call("PUT", f"/library/metadata/{ids}/prefs", query={"args": args}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_refresh(ids: str, agent: str | None = None, mark_updated: str | None = None, skip_refresh: str | None = None) -> str:
    """Refresh a metadata item.

    PUT /library/metadata/{ids}/refresh

    Args:
        ids: Comma-separated list of IDs
        agent: The identifier of the metadata agent to use
        mark_updated: The markUpdated
        skip_refresh: Skip synchronous refresh
    """
    return call("PUT", f"/library/metadata/{ids}/refresh", query={"agent": agent, "markUpdated": mark_updated, "skipRefresh": skip_refresh}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_split(ids: str) -> str:
    """Split a metadata item.

    PUT /library/metadata/{ids}/split

    Args:
        ids: Comma-separated list of IDs
    """
    return call("PUT", f"/library/metadata/{ids}/split", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_unmatch(ids: str) -> str:
    """Unmatch a metadata item.

    PUT /library/metadata/{ids}/unmatch

    Args:
        ids: Comma-separated list of IDs
    """
    return call("PUT", f"/library/metadata/{ids}/unmatch", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_metadata_by_ids_voice_activity(ids: str, force: str | None = None, manual: str | None = None) -> str:
    """Detect voice activity.

    PUT /library/metadata/{ids}/voiceActivity

    Args:
        ids: Comma-separated list of IDs
        force: Indicate whether detection should be re-run
        manual: Indicate whether detection is manually run
    """
    return call("PUT", f"/library/metadata/{ids}/voiceActivity", query={"force": force, "manual": manual}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_optimize(async_: str | None = None) -> str:
    """Optimize the Database.

    PUT /library/optimize

    Args:
        async_: If set, don't wait for completion but return an activity
    """
    return call("PUT", "/library/optimize", query={"async": async_}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_parts_by_part_id(part_id: int, audio_stream_id: int | None = None, subtitle_stream_id: int | None = None, all_parts: str | None = None) -> str:
    """Set stream selection.

    PUT /library/parts/{partId}

    Args:
        part_id: The id of the part to select streams on
        audio_stream_id: The id of the audio stream to select in this part
        subtitle_stream_id: The id of the subtitle stream to select in this part.  Specify 0 to select no subtitle
        all_parts: Perform the same for all parts of this media selecting similar streams in each
    """
    return call("PUT", f"/library/parts/{part_id}", query={"audioStreamID": audio_stream_id, "subtitleStreamID": subtitle_stream_id, "allParts": all_parts}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_sections_by_section_id(section_id: str, name: str | None = None, scanner: str | None = None, agent: str | None = None, metadata_agent_provider_group_id: str | None = None, language: str | None = None, locations: list | None = None, prefs: dict | None = None) -> str:
    """Edit a library section.

    PUT /library/sections/{sectionId}

    Args:
        section_id: The section identifier
        name: The name of the new section
        scanner: The scanner this section should use
        agent: The agent this section should use for metadata
        metadata_agent_provider_group_id: The agent group id for this section
        language: The language of this section
        locations: The locations on disk to add to this section
        prefs: The preferences for this section
    """
    return call("PUT", f"/library/sections/{section_id}", query={"name": name, "scanner": scanner, "agent": agent, "metadataAgentProviderGroupId": metadata_agent_provider_group_id, "language": language, "locations": locations, "prefs": prefs}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_sections_by_section_id_all(section_id: str, type: str | None = None, filters: str | None = None, field_value: str | None = None, field_locked: str | None = None, title_value: str | None = None, artist_title_value: str | None = None, artist_title_id: str | None = None, album_title_value: str | None = None, album_title_id: str | None = None, tagtype_idx_tag_tag: str | None = None, tagtype_idx_tagging_object: str | None = None, tagtype_tag_tag: str | None = None, tagtype_tag: str | None = None) -> str:
    """Set the fields of the filtered items.

    PUT /library/sections/{sectionId}/all

    Args:
        section_id: The id of the section
        type: The media type to filter by
        filters: The filters to apply to determine which items should be modified
        field_value: Set the specified field to a new value
        field_locked: Set the specified field to locked (or unlocked if set to 0)
        title_value: This field is treated specially by albums or artists and may be used for implicit reparenting.
        artist_title_value: Reparents set of Tracks or Albums - used with album.title.* in the case of tracks
        artist_title_id: Reparents set of Tracks or Albums - used with album.title.* in the case of tracks
        album_title_value: Reparents set of Tracks - Must be used in conjunction with artist.title.value or id
        album_title_id: Reparents set of Tracks - Must be used in conjunction with artist.title.value or id
        tagtype_idx_tag_tag: Creates tag and associates it with each item in the set. - [idx] links this and the next parameters together
        tagtype_idx_tagging_object: Here `object` may be text/thumb/art/theme - Optionally used in conjunction with tag.tag, to update association info across the set.
        tagtype_tag_tag: Remove comma separated tags from the set of items
        tagtype_tag: Remove associations of this type (e.g. genre) from the set of items
    """
    return call("PUT", f"/library/sections/{section_id}/all", query={"type": type, "filters": filters, "field.value": field_value, "field.locked": field_locked, "title.value": title_value, "artist.title.value": artist_title_value, "artist.title.id": artist_title_id, "album.title.value": album_title_value, "album.title.id": album_title_id, "tagtype[idx].tag.tag": tagtype_idx_tag_tag, "tagtype[idx].tagging.object": tagtype_idx_tagging_object, "tagtype[].tag.tag-": tagtype_tag_tag, "tagtype[].tag": tagtype_tag}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_sections_by_section_id_analyze(section_id: int) -> str:
    """Analyze a section.

    PUT /library/sections/{sectionId}/analyze

    Args:
        section_id: Section identifier
    """
    return call("PUT", f"/library/sections/{section_id}/analyze", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_sections_by_section_id_edit(section_id: int) -> str:
    """Edit Section.

    PUT /library/sections/{sectionId}/edit

    Args:
        section_id: The unique identifier of the library section
    """
    return call("PUT", f"/library/sections/{section_id}/edit", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_sections_by_section_id_empty_trash(section_id: int) -> str:
    """Empty section trash.

    PUT /library/sections/{sectionId}/emptyTrash

    Args:
        section_id: Section identifier
    """
    return call("PUT", f"/library/sections/{section_id}/emptyTrash", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_sections_by_section_id_move(section_id: int) -> str:
    """Move Section.

    PUT /library/sections/{sectionId}/move

    Args:
        section_id: The unique identifier of the library section
    """
    return call("PUT", f"/library/sections/{section_id}/move", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_sections_by_section_id_prefs(section_id: int, prefs: dict | None = None) -> str:
    """Set section prefs.

    PUT /library/sections/{sectionId}/prefs

    Args:
        section_id: Section identifier
        prefs: The preference key to retrieve or set
    """
    return call("PUT", f"/library/sections/{section_id}/prefs", query={"prefs": prefs}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_library_streams_by_stream_id_ext(stream_id: int, ext: str, offset: int | None = None) -> str:
    """Set a stream offset.

    PUT /library/streams/{streamId}.{ext}

    Args:
        stream_id: The id of the stream
        ext: This is not a part of this endpoint but documented here to satisfy OpenAPI
        offset: The offest in ms
    """
    return call("PUT", f"/library/streams/{stream_id}.{ext}", query={"offset": offset}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_livetv_dvrs_by_dvr_id(dvr_id: int) -> str:
    """Update DVR Settings.

    PUT /livetv/dvrs/{dvrId}

    Args:
        dvr_id: The ID of the DVR.
    """
    return call("PUT", f"/livetv/dvrs/{dvr_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_livetv_dvrs_by_dvr_id_devices_by_device_id(dvr_id: int, device_id: int) -> str:
    """Add a device to an existing DVR.

    PUT /livetv/dvrs/{dvrId}/devices/{deviceId}

    Args:
        dvr_id: The ID of the DVR.
        device_id: The ID of the device to add.
    """
    return call("PUT", f"/livetv/dvrs/{dvr_id}/devices/{device_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_livetv_dvrs_by_dvr_id_lineups(dvr_id: int, lineup: str | None = None) -> str:
    """Add a DVR Lineup.

    PUT /livetv/dvrs/{dvrId}/lineups

    Args:
        dvr_id: The ID of the DVR.
        lineup: The lineup to delete
    """
    return call("PUT", f"/livetv/dvrs/{dvr_id}/lineups", query={"lineup": lineup}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_livetv_dvrs_by_dvr_id_prefs(dvr_id: int, name: str | None = None, value: str | None = None) -> str:
    """Set DVR preferences.

    PUT /livetv/dvrs/{dvrId}/prefs

    Args:
        dvr_id: The ID of the DVR.
        name: Set the `name` preference to the provided value
        value: Preference value to set.
    """
    return call("PUT", f"/livetv/dvrs/{dvr_id}/prefs", query={"name": name, "value": value}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_log(level: int | None = None, message: str | None = None, source: str | None = None) -> str:
    """Logging a single-line message to the Plex Media Server log.

    PUT /log

    Args:
        level: An integer log level to write to the PMS log with.
  - 0: Error
  - 1: Warning
  - 2: Info
  - 3: Debug
  - 4: Verbose
        message: The text of the message to write to the log.
        source: A string indicating the source of the message.
    """
    return call("PUT", "/log", query={"level": level, "message": message, "source": source}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_media_grabbers_devices_by_device_id(device_id: int, enabled: str | None = None) -> str:
    """Enable or disable a device.

    PUT /media/grabbers/devices/{deviceId}

    Args:
        device_id: The ID of the device.
        enabled: Whether to enable the device
    """
    return call("PUT", f"/media/grabbers/devices/{device_id}", query={"enabled": enabled}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_media_grabbers_devices_by_device_id_channelmap(device_id: int, channel_mapping: dict | None = None, channel_mapping_by_key: dict | None = None, channels_enabled: list | None = None) -> str:
    """Set a device's channel mapping.

    PUT /media/grabbers/devices/{deviceId}/channelmap

    Args:
        device_id: The ID of the device.
        channel_mapping: The mapping of changes, passed as a map of device channel to lineup VCN.
        channel_mapping_by_key: The mapping of changes, passed as a map of device channel to lineup key.
        channels_enabled: The channels which are enabled.
    """
    return call("PUT", f"/media/grabbers/devices/{device_id}/channelmap", query={"channelMapping": channel_mapping, "channelMappingByKey": channel_mapping_by_key, "channelsEnabled": channels_enabled}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_media_grabbers_devices_by_device_id_prefs(device_id: int, name: str | None = None, value: str | None = None) -> str:
    """Set device preferences.

    PUT /media/grabbers/devices/{deviceId}/prefs

    Args:
        device_id: The ID of the device.
        name: The preference names and values.
        value: Preference value to set.
    """
    return call("PUT", f"/media/grabbers/devices/{device_id}/prefs", query={"name": name, "value": value}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_media_subscriptions_by_subscription_id(subscription_id: int, prefs: dict | None = None) -> str:
    """Edit a subscription.

    PUT /media/subscriptions/{subscriptionId}

    Args:
        subscription_id: The unique identifier of the subscription
        prefs: The preference key to retrieve or set
    """
    return call("PUT", f"/media/subscriptions/{subscription_id}", query={"prefs": prefs}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_media_subscriptions_by_subscription_id_move(subscription_id: int, after: int | None = None) -> str:
    """Re-order a subscription.

    PUT /media/subscriptions/{subscriptionId}/move

    Args:
        subscription_id: The unique identifier of the subscription
        after: The subscription to move this sub after.  If missing will insert at the beginning of the list
    """
    return call("PUT", f"/media/subscriptions/{subscription_id}/move", query={"after": after}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_myplex_refresh_reachability() -> str:
    """Refresh Reachability.

    PUT /myplex/refreshReachability
    """
    return call("PUT", "/myplex/refreshReachability", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_pins_link(body: dict) -> str:
    """Link OAuth PIN.

    PUT /pins/link

    Args:
        body: Request payload. Read the matching GET or the /schema endpoint first to see the fields this resource expects.
    """
    return call("PUT", "/pins/link", query=None, body=body, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_WRITE)
def update_play_queues_by_play_queue_id(play_queue_id: int, uri: str | None = None, playlist_id: str | None = None, next: str | None = None) -> str:
    """Add a generator or playlist to a play queue.

    PUT /playQueues/{playQueueId}

    Args:
        play_queue_id: The ID of the play queue.
        uri: The content URI for what we're adding to the queue.
        playlist_id: The ID of the playlist to add to the playQueue.
        next: Play this item next (defaults to 0 - queueing at the end of manually queued items).
    """
    return call("PUT", f"/playQueues/{play_queue_id}", query={"uri": uri, "playlistID": playlist_id, "next": next}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_play_queues_by_play_queue_id_items_by_play_queue_item_id_move(play_queue_id: int, play_queue_item_id: int, after: int | None = None) -> str:
    """Move an item in a play queue.

    PUT /playQueues/{playQueueId}/items/{playQueueItemId}/move

    Args:
        play_queue_id: The ID of the play queue.
        play_queue_item_id: The play queue item ID to delete.
        after: The play queue item ID to insert the new item after. If not present, moves to the beginning.
    """
    return call("PUT", f"/playQueues/{play_queue_id}/items/{play_queue_item_id}/move", query={"after": after}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_play_queues_by_play_queue_id_reset(play_queue_id: int) -> str:
    """Reset a play queue.

    PUT /playQueues/{playQueueId}/reset

    Args:
        play_queue_id: The ID of the play queue.
    """
    return call("PUT", f"/playQueues/{play_queue_id}/reset", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_play_queues_by_play_queue_id_shuffle(play_queue_id: int) -> str:
    """Shuffle a play queue.

    PUT /playQueues/{playQueueId}/shuffle

    Args:
        play_queue_id: The ID of the play queue.
    """
    return call("PUT", f"/playQueues/{play_queue_id}/shuffle", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_play_queues_by_play_queue_id_unshuffle(play_queue_id: int) -> str:
    """Unshuffle a play queue.

    PUT /playQueues/{playQueueId}/unshuffle

    Args:
        play_queue_id: The ID of the play queue.
    """
    return call("PUT", f"/playQueues/{play_queue_id}/unshuffle", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_playlists_by_playlist_id(playlist_id: int) -> str:
    """Editing a Playlist.

    PUT /playlists/{playlistId}

    Args:
        playlist_id: The ID of the playlist
    """
    return call("PUT", f"/playlists/{playlist_id}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_playlists_by_playlist_id_items(playlist_id: int, uri: str | None = None, play_queue_id: int | None = None) -> str:
    """Adding to  a Playlist.

    PUT /playlists/{playlistId}/items

    Args:
        playlist_id: The ID of the playlist
        uri: The content URI for the playlist.
        play_queue_id: The play queue to add to a playlist.
    """
    return call("PUT", f"/playlists/{playlist_id}/items", query={"uri": uri, "playQueueID": play_queue_id}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_playlists_by_playlist_id_items_by_generator_id(playlist_id: int, generator_id: int, item: dict | None = None) -> str:
    """Modify a Generator.

    PUT /playlists/{playlistId}/items/{generatorId}

    Args:
        playlist_id: The ID of the playlist
        generator_id: The generator item ID to modify.
        item: Note: OpenAPI cannot properly render this query parameter example ([See GHI](https://github.com/OAI/OpenAPI-Specification/issues/1706)).  It should be rendered as:

Item[type]=42&Item[title]=Jack-Jack Attack&Item[target]=&Item[targetTagID]=1&Item[locationID]=-1&Item[Location][uri]=library://82503060-0d68-4603-b594-8b071d54819e/item//library/metadata/146&Item[Policy][scope]=all&Item[Policy][value]=&Item[Policy][unwatched]=0
    """
    return call("PUT", f"/playlists/{playlist_id}/items/{generator_id}", query={"Item": item}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_playlists_by_playlist_id_items_by_generator_id_by_metadata_id_by_action(playlist_id: int, generator_id: int, metadata_id: int, action: str) -> str:
    """Reprocess a generator.

    PUT /playlists/{playlistId}/items/{generatorId}/{metadataId}/{action}

    Args:
        playlist_id: The ID of the playlist
        generator_id: The generator item ID to act on
        metadata_id: The metadata item ID to act on
        action: The action to perform for this item on this optimizer queue
    """
    return call("PUT", f"/playlists/{playlist_id}/items/{generator_id}/{metadata_id}/{action}", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_playlists_by_playlist_id_items_by_playlist_item_id_move(playlist_id: int, playlist_item_id: int, after: int | None = None) -> str:
    """Moving items in a playlist.

    PUT /playlists/{playlistId}/items/{playlistItemId}/move

    Args:
        playlist_id: The ID of the playlist
        playlist_item_id: The playlist item ID to move.
        after: The playlist item ID to insert the new item after.  If not provided, item is moved to beginning of playlist
    """
    return call("PUT", f"/playlists/{playlist_id}/items/{playlist_item_id}/move", query={"after": after}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_prefs(prefs: dict | None = None) -> str:
    """Set preferences.

    PUT /:/prefs

    Args:
        prefs: The preference key to retrieve or set
    """
    return call("PUT", "/:/prefs", query={"prefs": prefs}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_rate(identifier: str | None = None, key: str | None = None, rating: float | None = None, rated_at: int | None = None) -> str:
    """Rate an item.

    PUT /:/rate

    Args:
        identifier: The identifier of the media provider containing the media to rate.  Typically `com.plexapp.plugins.library`
        key: The key of the item to rate.  This is the `ratingKey` found in metadata items
        rating: The rating to give the item.
        rated_at: The time when the rating occurred.  If not present, interpreted as now.
    """
    return call("PUT", "/:/rate", query={"identifier": identifier, "key": key, "rating": rating, "ratedAt": rated_at}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_scrobble(identifier: str | None = None, key: str | None = None, uri: str | None = None) -> str:
    """Mark an item as played.

    PUT /:/scrobble

    Args:
        identifier: The identifier of the media provider containing the media to rate.  Typically `com.plexapp.plugins.library`
        key: The key of the item to rate.  This is the `ratingKey` found in metadata items
        uri: URI of the item to scrobble. Format is `library://<section-uuid>/item/<url-encoded-key>` or `plex://movie/<guid>` or `plex://episode/<guid>`.
    """
    return call("PUT", "/:/scrobble", query={"identifier": identifier, "key": key, "uri": uri}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_sharings_by_user_id(user_id: int) -> str:
    """Update Share.

    PUT /sharings/{userId}

    Args:
        user_id: The unique identifier of the user
    """
    return call("PUT", f"/sharings/{user_id}", query=None, body=None, form=None, host='https://plex.tv/api/v2')


@mcp.tool(annotations=_WRITE)
def update_sync_refresh_content() -> str:
    """Refresh Sync Content.

    PUT /sync/refreshContent
    """
    return call("PUT", "/sync/refreshContent", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_sync_refresh_synclists() -> str:
    """Refresh Sync Lists.

    PUT /sync/refreshSynclists
    """
    return call("PUT", "/sync/refreshSynclists", query=None, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_unscrobble(identifier: str | None = None, key: str | None = None, uri: str | None = None) -> str:
    """Mark an item as unplayed.

    PUT /:/unscrobble

    Args:
        identifier: The identifier of the media provider containing the media to rate.  Typically `com.plexapp.plugins.library`
        key: The key of the item to rate.  This is the `ratingKey` found in metadata items
        uri: URI of the item to scrobble. Format is `library://<section-uuid>/item/<url-encoded-key>` or `plex://movie/<guid>` or `plex://episode/<guid>`.
    """
    return call("PUT", "/:/unscrobble", query={"identifier": identifier, "key": key, "uri": uri}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_updater_apply(tonight: str | None = None, skip: str | None = None) -> str:
    """Applying updates.

    PUT /updater/apply

    Args:
        tonight: Indicate that you want the update to run during the next Butler execution. Omitting this or setting it to false indicates that the update should install immediately.
        skip: Indicate that the latest version should be marked as skipped. The <Release> entry for this version will have the `state` set to `skipped`.
    """
    return call("PUT", "/updater/apply", query={"tonight": tonight, "skip": skip}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_updater_check(download: str | None = None) -> str:
    """Checking for updates.

    PUT /updater/check

    Args:
        download: Indicate that you want to start download any updates found.
    """
    return call("PUT", "/updater/check", query={"download": download}, body=None, form=None, host='server')


@mcp.tool(annotations=_WRITE)
def update_user_view_state_sync() -> str:
    """Update View State Sync.

    PUT /user/view_state_sync
    """
    return call("PUT", "/user/view_state_sync", query=None, body=None, form=None, host='https://plex.tv/api/v2')
