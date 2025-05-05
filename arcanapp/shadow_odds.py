import json
import logging
from typing import Dict, Any

class ShadowOddsEngine:
    def __init__(self):
        self.market_data = {}
        self.last_signal = None
        self.threshold = 0.75  # Pourcentage de mises suspectes
        logging.basicConfig(level=logging.INFO)

    def load_market_data(self, data: Dict[str, Any]) -> None:
        """Charge les données initiales de marché (cotes, mises, etc.)."""
        if not isinstance(data, dict):
            logging.error("Les données de marché doivent être un dictionnaire.")
            return
        self.market_data = data
        logging.info("Données de marché chargées : %s", data)

    def observe(self, match_state: Dict[str, Any]) -> None:
        """Observe l'évolution des cotes et détecte les pièges à parieurs."""
        odds_a = match_state.get("odds", {}).get("team_a")
        bets_a = match_state.get("bets", {}).get("team_a")

        if not odds_a or not bets_a:
            logging.info("Données insuffisantes pour l'observation : %s", match_state)
            return

        if bets_a >= self.threshold and odds_a >= self.market_data.get("team_a", 1.0):
            self.last_signal = {
                "alert": True,
                "type": "LineTrap",
                "description": "Cote stable ou en hausse malgré forte mise publique"
            }
        else:
            self.last_signal = {
                "alert": False,
                "type": "Stable",
                "description": "Pas de comportement suspect"
            }

        logging.info("Signal généré : %s", self.last_signal)
