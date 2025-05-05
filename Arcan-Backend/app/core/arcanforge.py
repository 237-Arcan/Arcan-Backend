import os
import json

MODULES_DIR = os.path.join(os.path.dirname(__file__), 'modules')

def load_all_module_metadata():
    metadata_list = []
    for root, _, files in os.walk(MODULES_DIR):
        for file in files:
            if file == 'meta.json':
                json_path = os.path.join(root, file)
                try:
                    with open(json_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        data["module_path"] = os.path.relpath(root, MODULES_DIR)
                        metadata_list.append(data)
                except Exception as e:
                    print(f"Erreur lors du chargement de {json_path} : {e}")
    return metadata_list

def print_arcanforge_metadata():
    metadata = load_all_module_metadata()
    forge_data = [m for m in metadata if "arcan_forge" in m.get("module_path", "")]
    if not forge_data:
        print("Aucun meta.json trouvé pour arcan_forge.")
        return

    print("=== ArcanForge Modules ===")
    for module in forge_data:
        print(f"Nom : {module.get('name', 'N/A')}")
        print(f"Version : {module.get('version', 'N/A')}")
        print(f"Auteur : {module.get('author', 'N/A')}")
        print(f"Description : {module.get('description', 'N/A')}")
        print(f"Path : {module.get('module_path', 'N/A')}")
        print("-" * 40)

if __name__ == "__main__":
    print_arcanforge_metadata()
