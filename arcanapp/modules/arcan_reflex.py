from .modules import NeuroArcan, AnomalicRadar, KarmicSensor


class ArcanReflex:
    def __init__(self):
        self.modules = {
            "neuro_arcan": NeuroArcan(),
            "anomalic_radar": AnomalicRadar(),
            "karmic_sensor": KarmicSensor()
        }

    def evaluate(self, past_predictions, new_prediction, context):
        """
        Évalue la situation et prend des décisions adaptatives basées sur les anomalies, le karma et les alternatives.
        """
        anomalies = self.modules["anomalic_radar"].scan(context)
        karma = self.modules["karmic_sensor"].measure(context)
        alternatives = self.modules["neuro_arcan"].simulate(past_predictions, context)

        if anomalies["frequency"] > 0.7 or karma["load"] > 0.8:
            return {
                "action": "adjust",
                "suggestion": alternatives["best_scenario"]
            }

        if len(past_predictions) >= 5 and self._is_incoherent(past_predictions[-3:], new_prediction):
            return {"action": "reboot"}

        return {"action": "ok"}

    def _is_incoherent(self, recent_preds, current_pred):
        """
        Vérifie si les prédictions récentes et actuelles sont incohérentes.
        """
        scores = [pred["confidence"] for pred in recent_preds]
        return max(scores) - min(scores) > 50
