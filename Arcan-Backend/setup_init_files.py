import os

# Liste des dossiers où on doit mettre un __init__.py
folders = [
    "arcanapp",
    "arcanapp/core",
    "arcanapp/modules",
    "arcanapp/modules/arcanx",
    "arcanapp/modules/shadow",
    "arcanapp/modules/live",
]

def create_init_files(base_path="."):
    for folder in folders:
        full_path = os.path.join(base_path, folder)
        os.makedirs(full_path, exist_ok=True)
        init_file = os.path.join(full_path, "__init__.py")
        if not os.path.exists(init_file):
            with open(init_file, "w") as f:
                pass  # fichier vide
            print(f"Créé : {init_file}")
        else:
            print(f"Déjà existant : {init_file}")

if __name__ == "__main__":
    create_init_files()
