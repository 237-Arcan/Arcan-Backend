class ExplanatoryMode:
    def __init__(self):
        self.explanations = []

    def add_explanation(self, module_name, signals):
        """
        Ajoute une justification pour un module donné.
        """
        self.explanations.append({
            "module": module_name,
            "signals": signals
        })

    def get_explanations(self):
        """
        Retourne toutes les justifications collectées.
        """
        return self.explanations
