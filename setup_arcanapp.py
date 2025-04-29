import os
import subprocess
import sys

def prompt_user():
    print("=== Initialisation du projet ArcanApp ===")
    project_name = input("Nom du projet (défaut: ArcanApp) : ") or "ArcanApp"
    debug_mode = input("Activer le mode DEBUG ? (o/n, défaut: o) : ") or "o"
    return project_name, debug_mode.lower() == 'o'

# Définir la structure de dossiers
folders = [
    "core",
    "modules",
    "services",
    "utils",
    "tests",
    "configs",
]

def generate_files(project_name, debug_active):
    files = {
        ".env": f"DEBUG={'True' if debug_active else 'False'}\nSECRET_KEY=your-secret-key\n",
        ".gitignore": ".env\n.secrets\n__pycache__/\n*.pyc\n",
        ".secrets": "# Stocke ici les vraies clés secrètes (ex: API keys)\n",
        "requirements.txt": "python-dotenv\ndynaconf\n",
        "configs/settings.toml": f"""[default]
debug = {str(debug_active).lower()}

[development]
debug = true

[production]
debug = false
""",
        "core/config.py": '''from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="ARCANAPP",
    settings_files=['configs/settings.toml', '.secrets'],
)
''',
        "core/logger.py": '''import logging

def get_logger(name=__name__):
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(name)s | %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    return logger
''',
        "main.py": f'''from core.config import settings
from core.logger import get_logger

logger = get_logger()

def main():
    logger.info("Bienvenue dans {project_name} !")
    logger.info(f"Mode debug actif: {{settings.debug}}")

if __name__ == "__main__":
    main()
''',
        "tests/test_base.py": '''def test_basic():
    assert 1 + 1 == 2
''',
        "README.md": f"# {project_name}\n\nProjet généré automatiquement.\n\n## Démarrage rapide\n```bash\npython main.py\n```\n\n## Structure\n- core/\n- modules/\n- services/\n- utils/\n- tests/\n- configs/\n",
    }
    return files

def create_folders():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Dossier créé : {folder}")

def create_files(files):
    for path, content in files.items():
        folder = os.path.dirname(path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)
        with open(path, 'w', encoding="utf-8") as f:
            f.write(content)
        print(f"Fichier créé : {path}")

def install_packages():
    print("Installation des packages nécessaires...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def main_script():
    project_name, debug_active = prompt_user()
    create_folders()
    files = generate_files(project_name, debug_active)
    create_files(files)
    install_packages()
    print("\n✅ Initialisation terminée !")
    print(f"Ton projet {project_name} est prêt à être codé !")

if __name__ == "__main__":
    main_script()
