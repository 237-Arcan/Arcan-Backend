class YouthImpactAnalyzer:
    def __init__(self):
        self.youth_threshold_age = 23  # Exemple : joueurs de moins de 23 ans.

    def analyze_impact(self, players_data):
        """
        Analyse l'impact des jeunes joueurs.
        """
        young_players = [
            player for player in players_data
            if player.get("age") <= self.youth_threshold_age
        ]
        return {
            "young_players_count": len(young_players),
            "impact_scores": [
                {"player": player["name"], "impact": self.calculate_impact(player)}
                for player in young_players
            ]
        }

    def calculate_impact(self, player):
        """
        Calcule un score d'impact basé sur les statistiques du joueur.
        """
        return player.get("goals", 0) * 2 + player.get("assists", 0)
