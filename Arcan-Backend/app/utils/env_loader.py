import os
from dotenv import load_dotenv

def load_environment():
    dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..", ".env")
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        print("[✓] Variables d'environnement chargées depuis .env")
    else:
        print("[!] Fichier .env introuvable")


import os

def load_environment():
    # Charger les variables d'environnement nécessaires
    os.environ["FLASK_APP"] = "flask_app.py"
    os.environ["FLASK_ENV"] = "development"
    print("Environnement chargé")
