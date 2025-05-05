from typing import Dict, Any, List, Optional, TypedDict

class MatchState(TypedDict):
    domination: bool
    goals_scored: int
    minute: int

class KarmicEvent(TypedDict):
    type: str
    intensity: int
    event: str

class ArcanReflex:
    def __init__(self):
        self.correction_log: List[Dict[str, Any]] = []

    def evaluate(self, match_state: MatchState, karmic_events: Optional[List[KarmicEvent]] = None) -> List[Dict[str, Any]]:
        """
        Analyse l’état du match + modules pour déclencher des réflexes adaptatifs.
        Exemples de corrections :
        - Si domination mais pas de but → alerte 'Blocage énergétique'
        - Si karmic_events très récurrents → alerte 'Répétition active'
        """
        corrections = []

        # Vérification de domination sans but
        if match_state["domination"] and match_state["goals_scored"] == 0:
            corrections.append({
                "type": "blockage",
                "label": "Blocage énergétique détecté",
                "minute": match_state["minute"]
            })

        # Vérification des événements karmiques
        if karmic_events:
            corrections.extend([
                {
                    "type": "karmic_loop",
                    "label": f"Répétition karmique détectée : {event['event']}",
                    "minute": match_state["minute"]
                }
                for event in karmic_events
                if event["type"] == "repeat" and event.get("intensity", 0) >= 2
            ])

        # Historique des corrections
        self.correction_log.extend(corrections)
        return corrections
