from arcan_engine.engine import ArcanEngine

class ArcanInterface:
    def __init__(self):
        self.engine = ArcanEngine()

    def get_prediction(self, full_context):
        self.engine.load_context(
            match_data=full_context["stats"],
            esoteric_data=full_context["esoteric"],
            odds_data=full_context["market"]
        )
        return self.engine.run_decision()
