import os
import sys
import importlib
import shutil

# Configuration de base
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(BASE_DIR, "app", "core")
META_LEVELS_DIR = os.path.join(APP_DIR, "meta_levels")

files_required = [
    os.path.join(APP_DIR, "loader.py"),
    os.path.join(APP_DIR, "module_manager.py"),
    os.path.join(META_LEVELS_DIR, "meta_loader.py"),
]

folders_required = [
    APP_DIR,
    META_LEVELS_DIR
]

# Fonctions utilitaires
def create_file(path, content=""):
    with open(path, "w") as f:
        f.write(content)
    print(f"[AUTO] Fichier créé : {path}")

def ensure_init_files(directory):
    init_path = os.path.join(directory, "__init__.py")
    if not os.path.exists(init_path):
        create_file(init_path)

def clean_useless_files(base_folder):
    print("\n==> Nettoyage des fichiers inutiles...")
    deleted = []
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith(".pyc") or file.startswith("loader1") or file.endswith("~"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                deleted.append(file_path)
    if deleted:
        print("[CLEAN] Fichiers supprimés :")
        for d in deleted:
            print(f" - {d}")
    else:
        print("[CLEAN] Aucun fichier inutile trouvé.")

def import_test(module_path):
    try:
        importlib.import_module(module_path)
        print(f"[OK] Module importé : {module_path}")
    except Exception as e:
        print(f"[ERREUR] Import impossible pour '{module_path}' : {e}")

def fix_sys_path():
    if BASE_DIR not in sys.path:
        sys.path.insert(0, BASE_DIR)

def main():
    print("==> Vérification de la structure du projet...\n")
    all_ok = True

    # Corriger sys.path
    fix_sys_path()

    # Vérification / création des dossiers nécessaires
    for folder in folders_required:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"[AUTO] Dossier créé : {folder}")

    # Vérification / création des fichiers nécessaires
    for file_path in files_required:
        if not os.path.exists(file_path):
            if file_path.endswith("meta_loader.py"):
                content = "# Meta loader initial\n"
            else:
                content = "# Loader or Manager initial\n"
            create_file(file_path, content)
            all_ok = False
        else:
            print(f"[OK] Fichier trouvé : {file_path}")

    # Vérification des __init__.py
    ensure_init_files(APP_DIR)
    ensure_init_files(META_LEVELS_DIR)

    # Nettoyage des fichiers inutiles
    clean_useless_files(BASE_DIR)

    # Test d'import
    modules = [
        "core.loader",
        "core.module_manager",
        "core.meta_levels.meta_loader"
    ]

    for module in modules:
        import_test(module)

    print("\n==> Résultat final :")
    if all_ok:
        print("[SUCCÈS] Projet prêt pour pousser sur Github !")
    else:
        print("[ATTENTION] Des corrections ont été faites automatiquement. Revérifie si besoin.")

if __name__ == "__main__":
    main()
