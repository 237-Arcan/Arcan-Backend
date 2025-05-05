class ChronoEcho:
    def __init__(self):
        self.patterns = [
            {"team": "Team A", "pattern": "3 consecutive wins"},
            {"team": "Team B", "pattern": "Loss after 2 wins"}
        ]

    def get_historical_patterns(self):
        """
        Récupère les motifs historiques détectés.
        """
        return self.patterns
