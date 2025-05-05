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
                        metadata_list.append(data)
                except Exception as e:
                    print(f"Erreur lors du chargement de {json_path} : {e}")
    return metadata_list

# Exemple d'utilisation
if __name__ == '__main__':
    all_metadata = load_all_module_metadata()
    print(json.dumps(all_metadata, indent=2, ensure_ascii=False))
