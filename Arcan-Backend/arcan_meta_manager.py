import os
import json
import re
from datetime import datetime

def generate_meta_for_folder(folder_path):
    meta = {
        "folder": os.path.basename(folder_path),
        "path": folder_path,
        "created": datetime.now().isoformat(),
        "files": [],
        "subfolders": []
    }

    for entry in os.listdir(folder_path):
        full_path = os.path.join(folder_path, entry)
        if os.path.isfile(full_path):
            meta["files"].append(entry)
        elif os.path.isdir(full_path):
            meta["subfolders"].append(entry)

    return meta

def scan_and_create_meta(start_path):
    for root, dirs, files in os.walk(start_path):
        if 'meta.json' not in files:
            meta = generate_meta_for_folder(root)
            meta_path = os.path.join(root, 'meta.json')
            with open(meta_path, 'w') as f:
                json.dump(meta, f, indent=4)
            print(f"meta.json créé pour : {root}")
        else:
            print(f"meta.json déjà présent : {root}")

if __name__ == "__main__":
    base_path = os.getcwd()  # ou mets le chemin absolu de arcan-backend si tu préfères
    scan_and_create_meta(base_path)
