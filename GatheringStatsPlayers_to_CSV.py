import json
import csv

# Load data from GatheringStats_players.json
with open('GatheringStats_players.json', 'r', encoding='utf-8') as f:
    players = json.load(f)

# Write WCPlayers.csv
with open('WCPlayers.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=[
        "Id", "name", "money", "nationality", "teams"
    ])
    writer.writeheader()
    for player_id, info in players.items():
        writer.writerow({
            "Id": player_id,
            "name": info.get("name", "empty"),  # Most don't have a name field
            "money": info.get("money", "0"),  # Most don't have a money field
            "nationality": info.get("nationality", info.get("flag", "empty")),  # Use 'flag' if 'nationality' missing
            "teams": info.get("teams", "empty")  # Most don't have a teams field
        })


