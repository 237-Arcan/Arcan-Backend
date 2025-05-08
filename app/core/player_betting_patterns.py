import pandas as pd

class PlayerBettingPatterns:
    """
    Analyse les comportements et formules de mise des joueurs.
    """

    def __init__(self, betting_data: pd.DataFrame):
        """
        Initialise avec les données de mise des joueurs.
        :param betting_data: DataFrame contenant les colonnes ["player_id", "match_id", "bet_type", "bet_value", "outcome"]
        """
        self.betting_data = betting_data

    def extract_common_patterns(self, top_n=5):
        """
        Identifie les formules de mise les plus fréquentes.
        :param top_n: Nombre de formules les plus fréquentes à extraire.
        :return: Liste des formules les plus utilisées.
        """
        patterns = self.betting_data.groupby(["bet_type", "bet_value"]).size().sort_values(ascending=False).head(top_n)
        return patterns.to_dict()

    def player_specific_patterns(self, player_id):
        """
        Analyse les formules spécifiques à un joueur.
        :param player_id: Identifiant du joueur.
        :return: Liste des formules les plus utilisées par ce joueur.
        """
        player_data = self.betting_data[self.betting_data["player_id"] == player_id]
        patterns = player_data.groupby(["bet_type", "bet_value"]).size().sort_values(ascending=False)
        return patterns.to_dict()