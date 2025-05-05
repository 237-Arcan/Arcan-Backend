"""
ArcanEngine – Moteur Principal d'Analyse et de Décision

Ce module centralise l'intégration de l'IA Arcan et la mémoire temporelle pour
prendre des décisions basées sur le contexte.
"""

from ia_arcan.core import IAArcan
from modules.temporal.memory import TemporalMemory


class ArcanEngine:
    def __init__(self):
        """
        Initialise le moteur Arcan avec les composants IA et mémoire temporelle.
        """
        self.ia_arcan = IAArcan()
        self.memory = TemporalMemory()
        self.current_context = {}

    def load_context(self, match_data, esoteric_data, odds_data):
        """
        Charge le contexte actuel basé sur les données du match, ésotériques et probabilistes.

        :param match_data: Données statistiques du match.
        :param esoteric_data: Données astrologiques ou ésotériques.
        :param odds_data: Données sur les probabilités ou cotes.
        """
        self.current_context = {
            "stats": match_data,
            "astro": esoteric_data,
            "odds": odds_data,
            "temporal": self.memory.extract(match_data)
        }

    def run_decision(self):
        """
        Exécute la logique de décision basée sur le contexte actuel.

        :return: Décision calculée par l'IA.
        """
        decision = self.ia_arcan.decide(self.current_context)
        self.memory.update(self.current_context, decision)
        return decision
