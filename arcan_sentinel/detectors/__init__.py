from typing import Dict, Any, Optional
import statistics

class BaseDetector:
    """
    Classe de base pour tous les détecteurs spécialisés.
    """

    def __init__(self):
        self.last_state = {}

    def detect(self, deltas: Dict[str, Any], context: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Méthode à implémenter dans les sous-classes.
        """
        raise NotImplementedError("Must be implemented in subclass")


class LineTrapDetector(BaseDetector):
    """
    Détecteur de pièges sur les lignes de cotes.
    """

    def detect(self, deltas, context):
        odds = context.get("odds", {})
        volumes = context.get("volumes", {})
        if not odds or not volumes:
            return None

        favourite = min(odds, key=odds.get)
        if volumes.get(favourite, 0) > 0.75 and odds[favourite] >= self.last_state.get("odds_fav", 0):
            self.last_state["odds_fav"] = odds[favourite]
            return {
                "type": "line_trap",
                "team": favourite,
                "odds": odds[favourite],
                "volume": volumes[favourite],
            }
        self.last_state["odds_fav"] = odds.get(favourite, 0)
        return None


class RhythmBreakDetector(BaseDetector):
    """
    Détecteur de ruptures de rythme basées sur les événements récents.
    """

    def detect(self, deltas, context):
        events = context.get("events", [])
        current_minute = context.get("minute", 0)
        last_events = [e for e in events if e.get("minute", 0) >= current_minute - 5]
        if len(last_events) >= 3:
            return {
                "type": "rhythm_break",
                "recent_events": last_events,
            }
        return None


class StatAnomalyDetector(BaseDetector):
    """
    Détecteur d'anomalies statistiques (e.g., tirs élevés avec faible xG).
    """

    def detect(self, deltas, context):
        stats = context.get("live_stats", {})
        if not stats:
            return None

        shots = stats.get("shots", 0)
        xg = stats.get("xG", 0)
        if shots > 10 and xg < 0.5:
            return {
                "type": "anomaly",
                "detail": "High shot count with low xG",
                "stats": stats,
            }
        return None


class NarrativeLoopDetector(BaseDetector):
    """
    Détecteur de boucles narratives basées sur l'historique des matchs.
    """

    def detect(self, deltas, context):
        history = context.get("historical", [])
        current_score = context.get("score", "0-0")
        current_match = context.get("match_id")
        for match in history:
            if match.get("match_id") != current_match and match.get("score") == current_score:
                return {
                    "type": "narrative_loop",
                    "match_reference": match,
                }
        return None


class EgregoreSurgeScanner(BaseDetector):
    """
    Scanner des réactions collectives basées sur le volume sonore de la foule.
    """

    def detect(self, deltas, context):
        crowd = context.get("crowd_reaction", {})
        if crowd.get("volume_db", 0) > 95 and crowd.get("chant", False):
            return {
                "type": "egregore_surge",
                "intensity": crowd["volume_db"],
                "chant": True,
            }
        return None


class MomentumCollapseSensor(BaseDetector):
    """
    Détecteur d'effondrements de momentum.
    """

    def detect(self, deltas, context):
        momentum = context.get("momentum", [])
        if len(momentum) < 3:
            return None

        if all(m < 0 for m in momentum[-3:]):
            std_dev = statistics.stdev(momentum[-5:]) if len(momentum) >= 5 else 0
            return {
                "type": "momentum_collapse",
                "values": momentum[-5:],
                "volatility": std_dev,
            }
        return None


# Registre des détecteurs
DETECTORS_REGISTRY = [
    LineTrapDetector(),
    RhythmBreakDetector(),
    StatAnomalyDetector(),
    NarrativeLoopDetector(),
    EgregoreSurgeScanner(),
    MomentumCollapseSensor(),
]
