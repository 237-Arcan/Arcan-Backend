import os

def check_project_structure():
    print("Vérification de la structure du projet Arcan...")

    expected_files = [
        'arcan_loader.py',
        'flask_app.py',
        'app/utils/env_loader.py',
        'app/routes.py'
    ]

    expected_dirs = [
        'app/core/modules'
    ]

    all_ok = True

    # Vérification des fichiers
    for filepath in expected_files:
        if not os.path.isfile(filepath):
            print(f"[✗] Fichier manquant : {filepath}")
            all_ok = False
        else:
            print(f"[✓] Fichier trouvé : {filepath}")

    # Vérification des dossiers
    for dirpath in expected_dirs:
        if not os.path.isdir(dirpath):
            print(f"[✗] Dossier manquant : {dirpath}")
            all_ok = False
        else:
            print(f"[✓] Dossier trouvé : {dirpath}")

    # Vérification du contenu de arcan_loader.py
    if os.path.isfile('arcan_loader.py'):
        with open('arcan_loader.py', 'r', encoding='utf-8') as f:
            content = f.read()
            if 'def load_arcan_modules()' in content:
                print("[✓] Fonction 'load_arcan_modules()' trouvée dans arcan_loader.py")
            else:
                print("[✗] Fonction 'load_arcan_modules()' ABSENTE dans arcan_loader.py")
                all_ok = False

    if all_ok:
        print("\n[✔] Structure OK. Tu peux lancer ton serveur Flask avec : python3 flask_app.py")
    else:
        print("\n[!] Corrige les erreurs ci-dessus avant de lancer Flask.")

if __name__ == "__main__":
    check_project_structure()
