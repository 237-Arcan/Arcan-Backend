from .functions import ShadowMomentumAnalyzer

class ShadowMomentumManager:
    """
    Gère le module ShadowMomentum et ses analyses.
    """

    def __init__(self):
        self.analyzer = ShadowMomentumAnalyzer()

    def process_live_event(self, event_data):
        """
        Traite un événement en live.
        """
        results = {
            "momentum_shift": self.analyzer.momentum_shift_tracker(event_data),
            "quiet_storm": self.analyzer.quiet_storm_signal(event_data),
            "red_zone": self.analyzer.red_zone_phase(event_data),
        }
        return results

    def should_activate(self, match_data):
        """
        Détermine si le module doit être activé automatiquement.
        """
        return match_data['importance'] == "high" and match_data['live_mode']
