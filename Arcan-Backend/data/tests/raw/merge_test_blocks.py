import os
import json
from glob import glob

OUTPUT_FILE = 'data/merged_tests.json'

def merge_blocks():
    # Recherche récursive de tous les fichiers test_block_*.json dans le dossier data/
    json_files = glob('data/**/test_block_*.json', recursive=True)

    if not json_files:
        print("Aucun fichier test_block_*.json trouvé.")
        return

    merged_data = []

    for file_path in sorted(json_files):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                if isinstance(data, list):
                    merged_data.extend(data)
                else:
                    merged_data.append(data)
        except Exception as e:
            print(f"Erreur de lecture {file_path} : {e}")

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, 'w') as out_file:
        json.dump(merged_data, out_file, indent=2)

    print(f"Fusion terminée. {len(merged_data)} entrées sauvegardées dans {OUTPUT_FILE}")

if __name__ == "__main__":
    merge_blocks()
