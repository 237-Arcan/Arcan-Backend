"""
Extension du système de journaux pour IA-Arcan et ArcanReflex.
"""

import logging
from logging.handlers import RotatingFileHandler


def setup_logger(name, log_file="logs/arcan_backend.log", level=logging.INFO):
    """
    Configure un logger avec rotation de fichiers.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Gestionnaire de rotation
    handler = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=5)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    # Ajout du gestionnaire
    if not logger.hasHandlers():
        logger.addHandler(handler)

    return logger
