import os
import sys
import importlib

# === CONFIGURATION ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(BASE_DIR, "app")
CORE_DIR = os.path.join(APP_DIR, "core")
META_LEVELS_DIR = os.path.join(CORE_DIR, "meta_levels")

folders_required = [
    APP_DIR,
    CORE_DIR,
    META_LEVELS_DIR,
]

files_required = [
    os.path.join(CORE_DIR, "loader.py"),
    os.path.join(CORE_DIR, "module_manager.py"),
    os.path.join(META_LEVELS_DIR, "meta_loader.py"),
]

modules_to_import = [
    "app.core.loader",
    "app.core.module_manager",
    "app.core.meta_levels.meta_loader",
]

# === OUTILS ===
def create_file(path, content=""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"[AUTO] Fichier créé : {path}")

def ensure_init_files_recursively(folder):
    for root, dirs, files in os.walk(folder):
        init_file = os.path.join(root, "__init__.py")
        if not os.path.exists(init_file):
            create_file(init_file, "# Init file\n")

def clean_useless_files(base_folder):
    print("\n==> Nettoyage des fichiers inutiles...")
    deleted = []
    for root, dirs, files in os.walk(base_folder):
        for file in files:
            if file.endswith(".pyc") or file.endswith("~") or file.startswith("loader1"):
                os.remove(os.path.join(root, file))
                deleted.append(os.path.join(root, file))
    if deleted:
        print("[CLEAN] Fichiers supprimés :")
        for f in deleted:
            print(f" - {f}")
    else:
        print("[CLEAN] Aucun fichier inutile trouvé.")

def fix_sys_path():
    if BASE_DIR not in sys.path:
        sys.path.insert(0, BASE_DIR)

def import_test(modules):
    print("\n==> Test d'import des modules...")
    all_ok = True
    for module_path in modules:
        try:
            importlib.import_module(module_path)
            print(f"[OK] Module importé : {module_path}")
        except Exception as e:
            print(f"[ERREUR] Import impossible pour '{module_path}' : {e}")
            all_ok = False
    return all_ok

def summary(success):
    print("\n==> Résultat final :")
    if success:
        print("[SUCCÈS] Projet prêt pour pousser sur Github !")
    else:
        print("[ATTENTION] Certaines erreurs doivent être corrigées.")

# === LOGIQUE PRINCIPALE ===
def main():
    print("==> Vérification de la structure du projet...\n")
    
    fix_sys_path()

    # Créer les dossiers nécessaires
    for folder in folders_required:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"[AUTO] Dossier créé : {folder}")
    
    # Créer les fichiers nécessaires
    for file_path in files_required:
        if not os.path.exists(file_path):
            content = "# Initial file\n"
            create_file(file_path, content)
        else:
            print(f"[OK] Fichier trouvé : {file_path}")

    # Créer tous les __init__.py nécessaires
    ensure_init_files_recursively(APP_DIR)

    # Nettoyer les fichiers inutiles
    clean_useless_files(BASE_DIR)

    # Tester les imports
    success = import_test(modules_to_import)

    # Résumé
    summary(success)

if __name__ == "__main__":
    main()
