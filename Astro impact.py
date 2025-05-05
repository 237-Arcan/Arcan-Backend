from typing import Dict, Any, Optional
import logging

class AstroImpact:
    def __init__(self):
        self.cosmic_conditions = {}
        self.last_influence: Optional[Dict[str, Any]] = None
        logging.basicConfig(level=logging.INFO)

    def set_cosmic_conditions(self, data: Dict[str, Any]) -> None:
        """Charge les conditions cosmiques du jour (ex: carte du ciel, aspects)."""
        if not isinstance(data, dict):
            raise ValueError("Les conditions cosmiques doivent être un dictionnaire.")
        self.cosmic_conditions = data
        logging.info("Conditions cosmiques chargées : %s", data)

    def evaluate_window(self, minute: int) -> None:
        """Évalue l'influence astrologique à une minute donnée."""
        if not self.cosmic_conditions:
            logging.warning("Aucune condition cosmique n'a été définie.")
            return

        influence = {
            "minute": minute,
            "planetary_hour": self._planetary_hour(minute),
            "sign_shift": self._check_sign_shift(minute),
            "aspects": self._detect_aspects(minute),
        }

        self.last_influence = influence
        logging.info("Influence évaluée pour la minute %d : %s", minute, influence)

    def _planetary_hour(self, minute: int) -> str:
        """Renvoie la planète gouvernante de l’heure."""
        planetary_hours = ["Saturn", "Jupiter", "Mars", "Sun", "Venus", "Mercury", "Moon"]
        planet = planetary_hours[(minute // 12) % 7]
        logging.debug("Planète gouvernante pour la minute %d : %s", minute, planet)
        return planet

    def _check_sign_shift(self, minute: int) -> Optional[str]:
        """Détecte si un changement de signe astrologique est programmé."""
        shifts = self.cosmic_conditions.get("sign_shifts", {})
        sign_shift = shifts.get(str(minute))
        if sign_shift:
            logging.debug("Changement de signe détecté à la minute %d : %s", minute, sign_shift)
        return sign_shift

    def _detect_aspects(self, minute: int) -> list:
        """Retourne une liste d’aspects majeurs détectés à cette minute."""
        aspects = self.cosmic_conditions.get("aspects", [])
        detected_aspects = [a for a in aspects if a.get("minute") == minute]
        logging.debug("Aspects détectés à la minute %d : %s", minute, detected_aspects)
        return detected_aspects
