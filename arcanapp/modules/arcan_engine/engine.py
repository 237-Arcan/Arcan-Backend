from ia_arcan.core import IAArcan
from modules.temporal.memory import TemporalMemory

class ArcanEngine:
    def __init__(self):
        self.ia_arcan = IAArcan()
        self.memory = TemporalMemory()
        self.current_context = {}

    def load_context(self, match_data, esoteric_data, odds_data):
        self.current_context = {
            "stats": match_data,
            "astro": esoteric_data,
            "odds": odds_data,
            "temporal": self.memory.extract(match_data)
        }

    def run_decision(self):
        decision = self.ia_arcan.decide(self.current_context)
        self.memory.update(self.current_context, decision)
        return decision
