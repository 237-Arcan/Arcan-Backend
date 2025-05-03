import os
import random

def pick_random_meta_dir(start_path):
    meta_dirs = []
    for root, dirs, files in os.walk(start_path):
        if 'meta.json' in files:
            meta_dirs.append(root)
    if meta_dirs:
        choice = random.choice(meta_dirs)
        print(f"Répertoire sélectionné : {choice}")
        with open(os.path.join(choice, "meta.json"), "r") as f:
            print(f.read())
    else:
        print("Aucun fichier meta.json trouvé.")

if __name__ == "__main__":
    pick_random_meta_dir(os.getcwd())
