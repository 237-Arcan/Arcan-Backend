import json
from pathlib import Path

def load_all_module_metadata(base_path="./app/core/modules"):
    modules = {}
    for json_file in Path(base_path).rglob("meta.json"):
        try:
            with open(json_file, "r") as f:
                data = json.load(f)
                module_name = json_file.parent.name
                modules[module_name] = data
        except Exception as e:
            print(f"Erreur dans {json_file}: {e}")
    return modules

