import requests
n = 3



if n == 1:
    json={"token": ""}
    url = requests.post("http://localhost:8000/start-bot", json=json)
if n == 2:
    json={"user_id": 1073383604576591974, "guild_id": 1077968892535775262, "channel_id": 1100148368996573265}
    url = requests.post("http://localhost:8000/join-voice", json=json)
if n == 3:
    url = requests.post("http://localhost:8000/play-music")


print(url.text)
