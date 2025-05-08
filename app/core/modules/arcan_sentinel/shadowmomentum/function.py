class ShadowMomentumAnalyzer:
    """
    Analyse dynamique pour détecter les changements de momentum dans un match.
    """

    def __init__(self):
        self.momentum_score = 0

    def momentum_shift_tracker(self, match_data):
        """
        Détecte le point de bascule dans la dynamique d’un match.
        """
        if match_data['high_pressure_sequences'] > 5 and match_data['team_b_reacts']:
            return {"shift_detected": True, "team": match_data['dominated_team']}
        return {"shift_detected": False}

    def quiet_storm_signal(self, match_data):
        """
        Alerte sur une montée de pression invisible dans le match.
        """
        if match_data['possession_neutral'] > 60 and match_data['territorial_advantage'] > 70:
            return {"quiet_storm_detected": True, "team": match_data['pressing_team']}
        return {"quiet_storm_detected": False}

    def red_zone_phase(self, match_data):
        """
        Identifie les zones critiques où un événement décisif est probable.
        """
        if match_data['dangerous_free_kicks'] > 2 or match_data['near_goal_events'] > 3:
            return {"red_zone": True, "team": match_data['attacking_team']}
        return {"red_zone": False}
