from .modules import SpiritRouter, EmotiveBalance, ArcanCodeInterpreter
from arcan_reflex.core import ArcanReflex


class IAArcan:
    def __init__(self):
        self.modules = {
            "spirit_router": SpiritRouter(),
            "emotive_balance": EmotiveBalance(),
            "arcan_code": ArcanCodeInterpreter()
        }
        self.memory = {}
        self.reflex = ArcanReflex()
        self.predictions = []

    def receive_signals(self, context):
        """
        Analyse les signaux des modules actifs en fonction du contexte fourni.
        """
        results = {}
        for name, module in self.modules.items():
            results[name] = module.analyze(context)
        return results

    def decide(self, context):
        """
        Prend une décision basée sur les signaux reçus et l'évaluation réflexive.
        """
        signals = self.receive_signals(context)
        decision = self._synthesize(signals)
        reflex_output = self.reflex.evaluate(self.predictions, decision, context)

        if reflex_output["action"] == "adjust":
            decision = reflex_output["suggestion"]
        elif reflex_output["action"] == "reboot":
            self._reboot_context()
            decision = self.decide(context)

        self.predictions.append(decision)
        return decision

    def _synthesize(self, signals):
        """
        Fusionne les signaux des modules pour générer une prédiction et une confiance.
        """
        score = 0
        score += signals["emotive_balance"]["emotional_weight"]
        score += signals["spirit_router"]["sync_score"]
        return {"prediction": signals["arcan_code"]["decoded_pattern"], "confidence": score}

    def _reboot_context(self):
        """
        Réinitialise le contexte, y compris les prédictions et la mémoire.
        """
        self.predictions = []
        self.memory.clear()
