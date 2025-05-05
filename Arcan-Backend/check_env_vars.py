import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le .env
load_dotenv()

# Liste des variables obligatoires
required_vars = [
    "ARCAN_API_KEY",
    "DATABASE_URL",
    "SECRET_KEY"
]

def check_env_vars():
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("[!] Variables d'environnement manquantes :")
        for var in missing_vars:
            print(f"    - {var}")
    else:
        print("[✓] Toutes les variables d'environnement obligatoires sont présentes.")

if __name__ == "__main__":
    check_env_vars()
