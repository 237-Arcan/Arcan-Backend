class TriggerEvent:
    """
    Classe représentant un événement déclencheur pour la création de modules.
    """

    def __init__(self, source: str, data: dict, module_affinity: str):
        self.source = source  # Exemple : 'CycleMirror', 'ShadowOdds'
        self.data = data      # Contexte brut ou transformé
        self.module_affinity = module_affinity  # Catégorie visée (ex: 'pattern_detector')
    
    def __repr__(self):
        return f"TriggerEvent(source={self.source}, module_affinity={self.module_affinity})"
