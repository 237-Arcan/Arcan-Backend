import os
import shutil

# Répertoires et fichiers attendus
base_path = os.getcwd()
src_path = os.path.join(base_path, 'app', 'core')
dest_path = os.path.join(base_path, 'modules', 'infrastructure', 'arcan_archive')
matches_path = os.path.join(base_path, 'data', 'matches')

files_to_move = ['meta.json', 'README.md', 'archive_downloader.py']

# Création des dossiers si manquants
os.makedirs(dest_path, exist_ok=True)
os.makedirs(matches_path, exist_ok=True)

# Déplacement des fichiers
for filename in files_to_move:
    src_file = os.path.join(src_path, filename)
    dest_file = os.path.join(dest_path, filename)
    if os.path.exists(src_file):
        shutil.move(src_file, dest_file)
        print(f"✔ Déplacé : {filename}")
    else:
        print(f"✖ Fichier introuvable : {filename}")

# Vérification finale
print("\nStructure corrigée. Tu peux relancer le test :")
print("  python test_arcan_download.py")
