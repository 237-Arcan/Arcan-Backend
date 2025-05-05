from typing import Dict, Any, Optional, List
import logging

class TarotBridge:
    def __init__(self):
        self.draw_data: Dict[str, Any] = {}
        self.last_draw: Optional[Dict[str, Any]] = None
        logging.basicConfig(level=logging.INFO)

    def prepare_draw(self, tarot_info: Dict[str, Any]) -> None:
        """
        Reçoit les cartes tirées avant le match.
        Exemple :
        {
            "major_arcana": [
                {"card": "The Tower", "minute": 60},
                {"card": "The Star", "minute": 75}
            ]
        }
        """
        if not isinstance(tarot_info, dict) or "major_arcana" not in tarot_info:
            raise ValueError("Les données du tirage doivent inclure une clé 'major_arcana'.")
        self.draw_data = tarot_info
        logging.info("Cartes de tarot chargées : %s", tarot_info)

    def evaluate_draw(self, minute: int) -> None:
        """Active une carte si elle est liée à la minute actuelle."""
        draws: List[Dict[str, Any]] = self.draw_data.get("major_arcana", [])
        relevant = [d for d in draws if d.get("minute") == minute]

        self.last_draw = relevant[0] if relevant else None
        if self.last_draw:
            logging.info("Carte activée à la minute %d : %s", minute, self.last_draw)
        else:
            logging.debug("Aucune carte activée à la minute %d.", minute)
