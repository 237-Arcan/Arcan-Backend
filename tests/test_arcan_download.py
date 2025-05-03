import os

def check_file_structure():
    base_path = os.getcwd()
    expected_paths = [
        "modules/infrastructure/arcan_archive/meta.json",
        "modules/infrastructure/arcan_archive/README.md",
        "modules/infrastructure/arcan_archive/archive_downloader.py",
        "data/matches/"
    ]
    
    all_ok = True
    print("== Vérification de l'arborescence arcan_archive ==")
    for path in expected_paths:
        full_path = os.path.join(base_path, path)
        if os.path.exists(full_path):
            print(f"  ✔ Présent : {path}")
        else:
            print(f"  ✖ Manquant : {path}")
            all_ok = False
    
    return all_ok

def check_dependencies():
    try:
        import requests
        print("  ✔ Dépendance 'requests' installée")
        return True
    except ImportError:
        print("  ✖ Dépendance manquante : 'requests'")
        return False

if __name__ == "__main__":
    structure_ok = check_file_structure()
    deps_ok = check_dependencies()

    if structure_ok and deps_ok:
        print("\n>>> Tout est prêt pour utiliser arcan_archive.")
    else:
        print("\n>>> Corrige les éléments manquants avant d'activer le module.")
