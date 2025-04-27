import os

def create_or_update_env():
    dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..", ".env")

    # Vérifie si le fichier .env existe
    if not os.path.exists(dotenv_path):
        print("[!] Fichier .env introuvable, création d'un nouveau fichier...")
        
        # Crée un nouveau fichier .env et ajoute des variables d'environnement de base
        with open(dotenv_path, "w") as f:
            f.write("# Fichier .env pour ArcanApp\n")
            f.write("ARCAN_API_KEY=your_api_key\n")
            f.write("DATABASE_URL=your_database_url\n")
            f.write("DEBUG=True\n")
            f.write("SECRET_KEY=your_secret_key\n")
            print("[✓] Fichier .env créé avec des variables d'exemple.")
    else:
        print("[✓] Fichier .env trouvé.")
    
    return dotenv_path

from app.utils.env_loader import load_environment

# Charger l'environnement
load_environment()

# Vérification rapide des variables essentielles
print("\n=== Vérification des variables d'environnement ===")
for key in ["SECRET_KEY", "DATABASE_URL", "ARCAN_API_KEY"]:
    value = os.getenv(key)
    if value:
        print(f"[✓] {key} = {value}")
    else:
        print(f"[✗] {key} est introuvable ou vide.")
# Appelle la fonction pour créer ou mettre à jour le fichier .env
dotenv_path = create_or_update_env()

# Charge les variables d'environnement depuis le fichier .env
from dotenv import load_dotenv
load_dotenv(dotenv_path)

