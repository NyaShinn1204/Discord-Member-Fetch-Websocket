import websocket,json

token=""
server_id=""
channel_id=""

def get_members(token,server,channel):
    ws = websocket.WebSocket()
    ws.connect("wss://gateway.discord.gg/?v=10&encoding=json")
    users = []
    while True:
        response = json.loads(ws.recv())
        if response["t"] is None:
            ws.send(json.dumps({"op": 2, "d": {"token": token, "capabilities": 16381, "properties": {"os": "Android", "browser": "Discord Android", "device": "Android", "system_locale": "ja-JP", "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36", "browser_version": "122.0.0.0", "os_version": "", "referrer": "", "referring_domain": "", "referrer_current": "", "referring_domain_current": "", "release_channel": "stable", "client_build_number": 263582, "client_event_source": None}, "presence": {"status": "invisible", "since": 0, "activities": [], "afk": False}, "compress": False, "client_state": {"guild_versions": {}, "highest_last_message_id": "0", "read_state_version": 0, "user_guild_settings_version": -1, "private_channels_version": "0", "api_code_version": 0}}}))
        elif response["t"] == "READY_SUPPLEMENTAL":
            ws.send(json.dumps({"op": 14, "d": {"guild_id": server, "typing": True, "activities": True, "threads": True, "channels": {channel: [[0, 99], [100, 199], [200, 299]]}}}))
        elif response["t"] == "GUILD_MEMBER_LIST_UPDATE":
            for _ in response["d"]["ops"]:
                for i in _["items"]:
                    if "member" in i:
                        users.append(i["member"]["user"]["id"])
            ws.close()
            return users

print(get_members(token,server_id,channel_id))
