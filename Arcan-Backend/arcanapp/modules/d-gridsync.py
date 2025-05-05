class DGridSync:
    def __init__(self):
        self.sync_history = []

    def synchronize(self, modules, patterns):
        """
        Synchronise les modules et les patterns en fonction des résultats passés.
        """
        sync_result = {
            "modules": [module for module in modules if self.should_activate(module)],
            "patterns": patterns,
        }
        self.sync_history.append(sync_result)
        print("[D-GridSync] Synchronisation effectuée.")
        return sync_result

    def should_activate(self, module):
        """
        Détermine si un module doit être activé en fonction des performances passées.
        """
        # Exemple de logique d'activation basée sur l'historique.
        return module.get("performance", 0) > 0.8
