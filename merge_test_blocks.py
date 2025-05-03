# scripts/merge_test_blocks.py

import json
import os

INPUT_DIR = "data/raw/tests/"
OUTPUT_FILE = "data/processed/all_tests.json"

def load_json_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def merge_blocks():
    all_data = []
    for filename in sorted(os.listdir(INPUT_DIR)):
        if filename.endswith(".json"):
            full_path = os.path.join(INPUT_DIR, filename)
            try:
                block_data = load_json_file(full_path)
                if isinstance(block_data, list):
                    all_data.extend(block_data)
                else:
                    print(f"[WARNING] Format non-list dans {filename}")
            except Exception as e:
                print(f"[ERROR] Problème avec {filename} : {e}")
    
    print(f"[INFO] Total itérations fusionnées : {len(all_data)}")
    
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    merge_blocks()
