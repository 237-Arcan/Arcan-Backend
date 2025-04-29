class Config(object):
    SECRET_KEY = "change-me"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False


import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis un fichier .env si présent
load_dotenv()

# Modes possibles
ENVIRONMENTS = ("development", "testing", "production")

class Config:
    """
    Configuration centrale de l'application ArcanApp
    """
    # Environnement actuel
    ENV = os.getenv("APP_ENV", "development")
    DEBUG = ENV == "development"

    # Dossiers principaux
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    LOGS_DIR = os.path.join(BASE_DIR, "logs")
    DATA_DIR = os.path.join(BASE_DIR, "data")
    MODELS_DIR = os.path.join(BASE_DIR, "models")
    TEMP_DIR = os.path.join(BASE_DIR, "tmp")

    # Paramètres API
    API_KEYS = {
        "flashscore": os.getenv("API_KEY_FLASHSCORE", ""),
        "sofascore": os.getenv("API_KEY_SOFASCORE", ""),
        "betfair": os.getenv("API_KEY_BETFAIR", ""),
        "astrologyapi": os.getenv("API_KEY_ASTROLOGY", ""),
    }

    # Paramètres généraux
    TIMEZONE = os.getenv("APP_TIMEZONE", "UTC")
    LANGUAGE = os.getenv("APP_LANGUAGE", "en")
    DEFAULT_RETRY_ATTEMPTS = int(os.getenv("DEFAULT_RETRY_ATTEMPTS", 3))

    # Sécurité
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

    # Options de debug avancées
    SHOW_SQL_QUERIES = bool(int(os.getenv("SHOW_SQL_QUERIES", 0)))
    ENABLE_PROFILING = bool(int(os.getenv("ENABLE_PROFILING", 0)))

# Exemple d'utilisation
if __name__ == "__main__":
    print("Current Environment:", Config.ENV)
    print("Debug mode:", Config.DEBUG)
    print("Flashscore API Key:", Config.API_KEYS['flashscore'])
    print("Base Directory:", Config.BASE_DIR)
