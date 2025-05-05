class AnomalicRadar:
    def scan(self, context):
        """
        Scanne le contexte pour détecter des signaux extra-normaux.

        :param context: Contexte actuel (ex. événements récents, données externes).
        :return: Fréquence des signaux anormaux détectés.
        """
        return {"frequency": 0.75}

import json


class AnomalicRadar:
    def __init__(self, config_path="config/anomalic_radar_config.json"):
        """
        Initialise le module avec une configuration par défaut ou personnalisée.
        """
        self.config = self._load_config(config_path)

    def _load_config(self, path):
        """
        Charge la configuration depuis un fichier JSON.
        """
        with open(path, "r") as config_file:
            return json.load(config_file)

    def scan(self, context):
        """
        Scanne le contexte pour détecter des signaux extra-normaux.

        :param context: Contexte actuel (ex. événements récents, données externes).
        :return: Fréquence des signaux anormaux détectés.
        """
        frequency_threshold = self.config["anomaly_detection"]["frequency_threshold"]

        # Exemple d'analyse basée sur la configuration
        detected_frequency = 0.75  # Exemple de valeur fixe pour démonstration
        if detected_frequency > frequency_threshold:
            return {"frequency": detected_frequency}
        return {"frequency": 0}
