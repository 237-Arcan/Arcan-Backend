from modules.shadow_odds import ShadowOddsEngine
from modules.cycle_mirror import CycleMirror
from modules.astro_impact import AstroImpact
from modules.tarot_bridge import TarotBridge
from modules.arcan_reflex import ArcanReflex
from typing import Dict, Any

class Orchestrator:
    def __init__(self):
        self.minute = 0
        self.shadow_odds = ShadowOddsEngine()
        self.cycle_mirror = CycleMirror()
        self.astro_impact = AstroImpact()
        self.tarot_bridge = TarotBridge()
        self.reflex = ArcanReflex()

    def load_context(self, context_data: Dict[str, Any]) -> None:
        """Initialise les modules avec les données du match (pré-match, ésotériques, etc.)."""
        self.shadow_odds.load_market_data(context_data.get('odds', {}))
        self.astro_impact.set_cosmic_conditions(context_data.get('cosmic', {}))
        self.cycle_mirror.load_history(context_data.get('history', []))
        self.tarot_bridge.prepare_draw(context_data.get('tarot', {}))

    def step_minute(self, match_state: Dict[str, Any]) -> Dict[str, Any]:
        """Fait progresser la simulation minute par minute en activant les modules."""
        self.minute += 1
        print(f"\n--- Minute {self.minute} ---")

        self.shadow_odds.observe(match_state)
        karmic_events = self.cycle_mirror.scan(match_state)
        self.astro_impact.evaluate_window(self.minute)
        self.tarot_bridge.evaluate_draw(self.minute)

        corrections = self.reflex.evaluate(match_state, karmic_events)

        return {
            "minute": self.minute,
            "shadow_odds": getattr(self.shadow_odds, 'last_signal', None),
            "astro": getattr(self.astro_impact, 'last_influence', None),
            "tarot": getattr(self.tarot_bridge, 'last_draw', None),
            "cycle": karmic_events,
            "corrections": corrections
        }

    def reset(self) -> None:
        """Réinitialise l'état de l'orchestrateur."""
        self.__init__()
