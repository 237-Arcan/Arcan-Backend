from .functions import CrowdPressureAnalyzer

class CrowdPressureIndexManager:
    """
    Gère le module CrowdPressureIndex.
    """

    def __init__(self):
        self.analyzer = CrowdPressureAnalyzer()

    def process_live_event(self, event_data):
        """
        Traite un événement live.
        """
        results = {
            "clutch_time": self.analyzer.clutch_time_boost(event_data),
            "nervous_shift": self.analyzer.nervous_shift(event_data.get('players', [])),
            "fan_surge": self.analyzer.fan_surge(event_data),
        }
        return results

    def should_activate(self, match_data):
        """
        Détermine si le module doit être activé automatiquement.
        """
        return (
            match_data['is_home_game'] and
            match_data['importance'] == "high" and
            match_data['crowd_volume'] > 60
        )
