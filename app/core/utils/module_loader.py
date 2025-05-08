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

import json
from pathlib import Path
from app.core.utils.external_source_manager import ExternalSourceManager

def load_all_module_metadata(base_path="./app/core/modules", api_url=None):
    """
    Charge les métadonnées des modules depuis des fichiers locaux ou une API externe.
    :param base_path: Chemin des fichiers locaux.
    :param api_url: URL de l'API externe (optionnelle).
    :return: Dictionnaire des métadonnées des modules.
    """
    modules = {}
    source_manager = ExternalSourceManager()

    # Chargement depuis des fichiers locaux
    for json_file in Path(base_path).rglob("meta.json"):
        try:
            with open(json_file, "r") as f:
                data = json.load(f)
                module_name = json_file.parent.name
                modules[module_name] = data
        except Exception as e:
            print(f"Erreur dans {json_file}: {e}")

    # Chargement depuis l'API externe si disponible et si aucun fichier local n'est trouvé
    if api_url and not modules:
        print("[INFO] Aucun fichier local trouvé. Requête à l'API externe...")
        api_data = source_manager.fetch_from_api(api_url)
        if api_data:
            modules.update(api_data)

    return modules
