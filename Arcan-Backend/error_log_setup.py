import logging
import os
from logging.handlers import RotatingFileHandler

# Configuration des logs
def setup_logging(log_file='logs/app.log', log_level=logging.DEBUG):
    """
    Configure les logs pour l'application.
    Crée un fichier de log rotatif et définit le niveau de log.
    """
    # Créer le dossier 'logs' si ce n'est pas déjà fait
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Configurer le format de log
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    # Définir le gestionnaire de log rotatif
    log_handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)  # 10MB par fichier, 5 backups
    log_handler.setLevel(log_level)
    
    # Créer le formateur de log
    formatter = logging.Formatter(log_format)
    log_handler.setFormatter(formatter)
    
    # Configurer le logger
    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.addHandler(log_handler)
    
    # Ajouter un handler pour afficher dans la console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Afficher uniquement les infos et au-dessus dans la console
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logger.info("Logging system initialized successfully.")

# Exemple d'utilisation de l'initialisation des logs
if __name__ == "__main__":
    setup_logging()
    logging.debug("This is a debug message")
    logging.info("Application started")
    logging.warning("This is a warning")
    logging.error("An error occurred")
    logging.critical("Critical error encountered")

