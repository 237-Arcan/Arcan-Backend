class CrowdPressureAnalyzer:
    """
    Analyse énergétique et comportementale du public en live.
    """

    def __init__(self):
        self.current_pressure = 0

    def clutch_time_boost(self, match_data):
        """
        Détecte les moments où la foule pousse une équipe à performer.
        """
        if match_data['minute'] >= 75 and match_data['crowd_volume'] > 70:
            return {"boost": True, "team": match_data['favored_team']}
        return {"boost": False}

    def nervous_shift(self, player_data):
        """
        Détecte les joueurs affectés par la pression.
        """
        nervous_players = [
            player for player in player_data
            if player['errors'] > 3 and player['crowd_reaction'] == "negative"
        ]
        return nervous_players

    def fan_surge(self, event_data):
        """
        Calcule l'intensité collective pendant des moments clés.
        """
        if event_data['type'] in ['goal', 'corner', 'penalty']:
            intensity = event_data['crowd_volume'] * event_data['reaction_factor']
            return {"intensity": intensity}
        return {"intensity": 0}
