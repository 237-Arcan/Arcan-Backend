import os
import sys

# Correction automatique du sys.path pour qu'on trouve app/
current_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(current_dir, 'app')

if app_dir not in sys.path:
    sys.path.insert(0, app_dir)

# Maintenant, on peut importer sans erreurs
# -------------------------------------------

def check_file_exists(filepath):
    if os.path.isfile(filepath):
        print(f"[OK] Fichier trouvé : {filepath}")
        return True
    else:
        print(f"[ERREUR] Fichier manquant : {filepath}")
        return False

def check_module_import(module_name):
    try:
        __import__(module_name)
        print(f"[OK] Module importé : {module_name}")
        return True
    except ImportError as e:
        print(f"[ERREUR] Import impossible pour '{module_name}' : {e}")
        return False

def main():
    print("==> Vérification de la structure du projet...\n")
    
    all_ok = True
    
    # Liste des fichiers attendus
    expected_files = [
        os.path.join(app_dir, 'core', 'loader1.py'),
        os.path.join(app_dir, 'core', 'module_manager.py'),
        os.path.join(app_dir, 'core', 'meta_levels', 'meta_loader.py')
    ]
    
    # Vérifier que les fichiers existent
    for filepath in expected_files:
        if not check_file_exists(filepath):
            all_ok = False
    
    # Liste des modules à importer
    expected_modules = [
        'core.loader1',
        'core.module_manager',
        'core.meta_levels.meta_loader'
    ]
    
    # Vérifier que les modules s'importent bien
    for module_name in expected_modules:
        if not check_module_import(module_name):
            all_ok = False
    
    print("\n==> Résultat final :")
    if all_ok:
        print("[SUCCÈS] Tout est prêt pour pousser vers Github !")
    else:
        print("[ATTENTION] Corrige les erreurs avant de pousser.")

if __name__ == "__main__":
    main()

