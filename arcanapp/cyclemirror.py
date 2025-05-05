from typing import List, Dict, Any
import difflib
import logging

class CycleMirror:
    def __init__(self):
        self.history = []
        self.last_cycles = []
        logging.basicConfig(level=logging.INFO)

    def load_history(self, data: List[Dict[str, Any]]) -> None:
        """Charge un historique d’événements passés pertinents."""
        if not isinstance(data, list):
            logging.error("L'historique doit être une liste de dictionnaires.")
            return
        self.history = data
        logging.info("Historique chargé avec %d événements.", len(data))

    def scan(self, match_state: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Analyse la situation actuelle et recherche des échos cycliques."""
        team_a = match_state.get("team_a")
        team_b = match_state.get("team_b")
        score = match_state.get("score")

        if not team_a or not team_b or not score:
            logging.warning("Données incomplètes dans match_state : %s", match_state)
            return []

        potential_matches = []
        for event in self.history:
            if self._is_cycle_match(team_a, team_b, event):
                potential_matches.append({
                    "echo": event,
                    "score_similarity": self._score_similarity(score, event.get("score"))
                })

        self.last_cycles = potential_matches
        logging.info("Scan terminé : %d correspondances trouvées.", len(potential_matches))
        return potential_matches

    def _is_cycle_match(self, team_a: str, team_b: str, event: Dict[str, Any]) -> bool:
        """Détecte les cycles d’opposition inversée ou répétée."""
        teams_match = (
            (team_a == event.get("team_a") and team_b == event.get("team_b")) or
            (team_b == event.get("team_a") and team_a == event.get("team_b"))
        )
        return teams_match

    def _score_similarity(self, current_score: str, past_score: str) -> float:
        """Évalue la similarité narrative des scores (simplement ici avec ratio)."""
        if not current_score or not past_score:
            return 0.0
        similarity = difflib.SequenceMatcher(None, current_score, past_score).ratio()
        logging.debug("Similarité entre scores '%s' et '%s' : %.2f", current_score, past_score, similarity)
        return similarity
