import json
import csv

# Load data from recents.json
with open('recents.json', 'r', encoding='utf-8') as f:
    events = json.load(f)

# Map to store unique players
player_map = {}

# Write events.csv
with open('events.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=[
        "Id", "Label", "type", "date", "season", "formats",
        "medium", "location", "coverage", "logo", "teamsize", "NodeType"
    ])
    writer.writeheader()
    for event in events:
        writer.writerow({
            "Id": event.get("id", ""),
            "Label": event.get("name", ""),
            "type": event.get("type", ""),
            "date": event.get("date", ""),
            "season": event.get("season", ""),
            "formats": ";".join(event.get("formats", [])),
            "medium": event.get("medium", ""),
            "location": event.get("location", ""),
            "coverage": event.get("coverage", ""),
            "teamsize": event.get("teamsize", 1),
            "NodeType": "Event"
        })

# Write edges.csv
with open('edges.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["Source", "Target", "relation", "money", "team"])
    writer.writeheader()
    for event in events:
        for player in event.get("top", []):
            pid = player.get("id")
            if not pid:
                continue
            money = int(player.get("money", 0))
            team = player.get("team", "")
            player_map[pid] = {
                "player_id": pid,
                "name": player.get("name", ""),
                "team": team,
                "money": max(money, player_map.get(pid, {}).get("money", 0))
            }
            writer.writerow({
                "Source": pid,
                "Target": event.get("id", ""),
                "relation": "TopFinish",
                "money": money,
                "team": team              
            })

# Write players.csv
with open('players.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["player_id", "name", "team", "money", "NodeType"])
    writer.writeheader()
    for player in player_map.values():
        writer.writerow({
            "player_id": player["player_id"],
            "name": player["name"],
            "team": player["team"],
            "money": player["money"],
            "NodeType": "Player"
        })
