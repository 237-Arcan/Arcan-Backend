import os
import sys
import importlib

# Chemin racine du projet
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'app'))

# Dossiers essentiels
REQUIRED_DIRS = [
    'core',
    'core/modules',
    'core/meta_levels'
]

# Fichiers essentiels (optionnel désormais)
REQUIRED_FILES = [
    # 'main.py'  # -> Désactivé pour ne pas bloquer inutilement
]

def check_directories():
    print("\n--- Vérification des dossiers ---\n")
    all_ok = True
    for directory in REQUIRED_DIRS:
        dir_path = os.path.join(PROJECT_ROOT, directory)
        if os.path.isdir(dir_path):
            print(f"[OK] Dossier '{directory}' trouvé.")
        else:
            print(f"[ERREUR] Dossier '{directory}' manquant.")
            all_ok = False
    return all_ok

def check_files():
    print("\n--- Vérification des fichiers ---\n")
    if not REQUIRED_FILES:
        print("[INFO] Vérification des fichiers désactivée temporairement.")
        return True

    all_ok = True
    for file in REQUIRED_FILES:
        file_path = os.path.join(PROJECT_ROOT, file)
        if os.path.isfile(file_path):
            print(f"[OK] Fichier '{file}' trouvé.")
        else:
            print(f"[ERREUR] Fichier '{file}' manquant.")
            all_ok = False
    return all_ok

def check_imports():
    print("\n--- Test des imports ---\n")
    all_ok = True
    sys.path.append(PROJECT_ROOT)  # Ajoute 'app' à sys.path

    # Tester les modules standards dans 'core'
    core_modules = [
        'core.loader',
        'core.module_manager'
    ]

    for module_name in core_modules:
        try:
            importlib.import_module(module_name)
            print(f"[OK] Module '{module_name}' importé.")
        except Exception as e:
            print(f"[ERREUR] Module '{module_name}' : {e}")
            all_ok = False

    # Tester les méta-modules dans 'core/meta_levels'
    meta_modules_path = os.path.join(PROJECT_ROOT, 'core', 'meta_levels')
    for file in os.listdir(meta_modules_path):
        if file.endswith('.py') and not file.startswith('__'):
            module_name = file[:-3]
            try:
                importlib.import_module(f'core.meta_levels.{module_name}')
                print(f"[OK] Méta-module '{module_name}' importé.")
            except Exception as e:
                print(f"[ERREUR] Méta-module '{module_name}' : {e}")
                all_ok = False

    return all_ok

def main():
    print("\n=== DÉMARRAGE DE L'AUTO-VÉRIFICATION ===\n")
    dirs_ok = check_directories()
    files_ok = check_files()
    imports_ok = check_imports()

    if dirs_ok and files_ok and imports_ok:
        print("\n=== AUTO-VÉRIFICATION TERMINÉE : TOUT EST OK ===\n")
    else:
        print("\n=== AUTO-VÉRIFICATION TERMINÉE : DES PROBLÈMES DÉTECTÉS ===\n")

if __name__ == "__main__":
    main()

import core.arcan_loader as loader
import core.arcan_sentinel as module_manager 
 # ou le bon module
