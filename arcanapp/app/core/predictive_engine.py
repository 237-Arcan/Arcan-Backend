from modules.arcanx.analyzer import ArcanXAnalyzer
from meta_levels.time_warper.time_analysis import TimeCyclePredictor

class PredictiveEngine:
    def __init__(self):
        self.arcanx = ArcanXAnalyzer()
        self.cycle_predictor = TimeCyclePredictor()

    def run_prediction(self, match_data):
        stats_prediction = self.arcanx.analyze(match_data)
        cycle_prediction = self.cycle_predictor.predict_cycles(match_data)
        return {
            "ArcanX": stats_prediction,
            "ChronoEcho": cycle_prediction
        }
