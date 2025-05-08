class LateGoalPredictor:
    """
    Module généré automatiquement pour détecter des patterns spécifiques.
    """

    def __init__(self):
        self.trigger_condition = "data['minute'] > 80 and data['momentum'] < 0"

    def scan(self, data):
        """
        Scanne les données pour détecter le pattern défini.
        """
        if eval(self.trigger_condition):
            return "Possible late equalizer"
        return None
