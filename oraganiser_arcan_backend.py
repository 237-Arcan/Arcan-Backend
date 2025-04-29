import os

# Définir les dossiers principaux
folders = [
    "api/routes",
    "arcan_core/arcanx",
    "arcan_core/shadowodds",
    "arcan_core/modules",
    "arcan_core/utils",
    "config",
    "tests"
]

# Définir les fichiers principaux à créer
files = {
    "api/main.py": "# Point d'entrée FastAPI ou Flask\n",
    "api/routes/arcanx_routes.py": "# Routes pour ArcanX\n",
    "api/routes/shadowodds_routes.py": "# Routes pour ShadowOdds\n",
    "arcan_core/__init__.py": "",
    "arcan_core/arcanx/__init__.py": "",
    "arcan_core/arcanx/moteur_arcanx.py": "# Moteur de traitement ArcanX\n",
    "arcan_core/shadowodds/__init__.py": "",
    "arcan_core/shadowodds/moteur_shadowodds.py": "# Moteur de traitement ShadowOdds\n",
    "arcan_core/modules/chrono_echo.py": "# Module ChronoEcho\n",
    "arcan_core/modules/cycle_mirror.py": "# Module CycleMirror\n",
    "arcan_core/utils/helpers.py": "# Fonctions utilitaires\n",
    "arcan_core/utils/validations.py": "# Fonctions de validation\n",
    "config/settings.py": "# Configuration des variables d'environnement\n",
    "config/database.py": "# Connexion et gestion de la base de données\n",
    "config/loader.py": "# Chargement des configurations\n",
    "tests/test_arcanx.py": "# Test pour moteur ArcanX\n",
    "tests/test_shadowodds.py": "# Test pour moteur ShadowOdds\n",
    ".gitignore": "# Ignorer les fichiers .env, __pycache__, etc.\n.env\n__pycache__/\n*.pyc\n",
    "README.md": "# Documentation de Arcan-Backend\n",
    "requirements.txt": "# Dépendances du projet\n"
}

def create_structure(base_path="."):
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"✅ Dossier créé : {folder_path}")

    for file_path, content in files.items():
        full_path = os.path.join(base_path, file_path)
        dir_path = os.path.dirname(full_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)
        print(f"✅ Fichier créé : {full_path}")

if __name__ == "__main__":
    create_structure()
    print("\n✅ Structure de Arcan-Backend organisée avec succès !")
