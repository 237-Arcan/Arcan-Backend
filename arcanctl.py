import json
from pathlib import Path

# Définir le modèle de métadonnées par défaut
DEFAULT_META = {
    "name": "",
    "description": "",
    "type": "core",  # ou "live", "passive", etc.
    "compatible_with": [],
    "author": "Unknown",
    "version": "1.0",
    "enabled": True,
    "meta_levels": {
        "level_1": {
            "description": "Fonctions de base : activation/désactivation, compatibilité."
        },
        "level_2": {
            "description": "Chargement dynamique, gestion des dépendances."
        },
        "level_3": {
            "description": "Interaction avec le noyau ArcanShadow, synchronisation live."
        },
        "level_4": {
            "description": "Auto-diagnostic, adaptation aux signaux extérieurs (ex : énergie du match, public, météo)."
        },
        "level_5": {
            "description": "Connexion aux modules ésotériques et aux données métaphysiques, activation des patterns profonds."
        }
    }
}

def generate_meta_json(module_dir: Path):
    meta_file = module_dir / "meta.json"
    if not meta_file.exists():
        DEFAULT_META["name"] = module_dir.name
        with open(meta_file, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_META, f, indent=4)
        print(f"[+] meta.json créé pour {module_dir.name}")
    else:
        print(f"[-] meta.json déjà présent pour {module_dir.name}")

def initialize_module_meta():
    modules_path = Path("modules")
    if not modules_path.exists():
        print("Le dossier 'modules' est introuvable.")
        return

    for module_dir in modules_path.iterdir():
        if module_dir.is_dir():
            generate_meta_json(module_dir)
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == "init-meta":
        initialize_module_meta()


import os
import json
import argparse

BASE_PATH = "app/core/modules"

DEFAULT_META = {
    "name": "",
    "description": "",
    "version": "0.1.0",
    "author": "ArcanForge",
    "meta_levels": [],
    "status": "draft"
}

def init_meta(module_name):
    module_path = os.path.join(BASE_PATH, module_name.lower())
    if not os.path.exists(module_path):
        print(f"Module '{module_name}' introuvable dans {BASE_PATH}.")
        return

    meta_path = os.path.join(module_path, "meta.json")
    if os.path.exists(meta_path):
        print(f"meta.json existe déjà pour '{module_name}' à {meta_path}.")
        return

    meta_data = DEFAULT_META.copy()
    meta_data["name"] = module_name
    os.makedirs(module_path, exist_ok=True)

    with open(meta_path, "w") as f:
        json.dump(meta_data, f, indent=4)
    print(f"meta.json généré à : {meta_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ArcanCTL")
    parser.add_argument("command", help="Commande à exécuter")
    parser.add_argument("module", nargs="?", help="Nom du module (ex: ChronoEcho)")
    args = parser.parse_args()

    if args.command == "init-meta" and args.module:
        init_meta(args.module)
    else:
        print("Usage : python arcanctl.py init-meta NomModule")


import os
import sys
import argparse
import json

# Fonction pour retrouver automatiquement le chemin du module
def find_module_path(module_name):
    base_dir = os.path.join("app", "core", "modules")
    for root, dirs, files in os.walk(base_dir):
        if module_name.lower() in [d.lower() for d in dirs]:
            for d in dirs:
                if d.lower() == module_name.lower():
                    return os.path.join(root, d)
    return None

# Fonction pour initialiser ou afficher le meta.json d’un module
def init_meta(module_name):
    module_path = find_module_path(module_name)
    if not module_path:
        print(f"Module '{module_name}' introuvable dans app/core/modules.")
        sys.exit(1)

    meta_path = os.path.join(module_path, "meta.json")

    if os.path.exists(meta_path):
        print(f"Fichier meta.json déjà présent pour {module_name} :")
        with open(meta_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
            print(json.dumps(meta, indent=4, ensure_ascii=False))
    else:
        default_meta = {
            "name": module_name,
            "version": "1.0",
            "description": f"Module {module_name} - description par défaut.",
            "author": "AutoGen",
            "active": True,
            "dependencies": []
        }
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(default_meta, f, indent=4, ensure_ascii=False)
        print(f"Fichier meta.json généré pour {module_name} dans {meta_path}.")

# Configuration des arguments CLI
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="Commande à exécuter (ex: init-meta)")
    parser.add_argument("module", nargs="?", help="Nom du module concerné")

    args = parser.parse_args()

    if args.command == "init-meta":
        if not args.module:
            print("Erreur : vous devez spécifier le nom du module.")
            sys.exit(1)
        init_meta(args.module)
    else:
        print(f"Commande inconnue : {args.command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
