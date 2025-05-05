# Loader or Manager initial
import os
import requests

ARCHIVE_URL = "https://raw.githubusercontent.com/ton-org/arcan-matches/main/data"

def download_archived_matches(user_id):
    archive_folder = f"./user_data/{user_id}/archives/"
    os.makedirs(archive_folder, exist_ok=True)

    # Liste d’archives ciblées (à personnaliser selon modules)
    files = ["historic_jleague.json", "classic_uefa.csv", "cycle_patterns.json"]

    for f in files:
        url = f"{ARCHIVE_URL}/{f}"
        response = requests.get(url)
        if response.status_code == 200:
            with open(os.path.join(archive_folder, f), "wb") as out_file:
                out_file.write(response.content)
        else:
            print(f"[WARN] Archive {f} not found.")
