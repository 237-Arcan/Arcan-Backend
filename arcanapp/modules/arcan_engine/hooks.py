from arcan_engine.engine import ArcanEngine

class ArcanHooks:
    def __init__(self):
        self.engine = ArcanEngine()
        self.live_mode = False

    def on_pre_match(self, data):
        self.engine.load_context(
            match_data=data["stats"],
            esoteric_data=data["astro"],
            odds_data=data["odds"]
        )
        return self.engine.run_decision()

    def on_live_update(self, data):
        self.live_mode = True
        self.engine.load_context(
            match_data=data["live_stats"],
            esoteric_data=data["astro_signals"],
            odds_data=data["live_odds"]
        )
        return self.engine.run_decision()
