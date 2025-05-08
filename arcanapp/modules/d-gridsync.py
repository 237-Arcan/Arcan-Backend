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

from app.core.utils.external_source_manager import ExternalSourceManager

class DGridSync:
    def __init__(self):
        self.sync_history = []
        self.source_manager = ExternalSourceManager()

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
        return module.get("performance", 0) > 0.8

    def listen_for_updates(self, ws_url):
        """
        Écoute un flux WebSocket en temps réel pour des mises à jour.
        :param ws_url: URL WebSocket.
        """
        print("[D-GridSync] Début de l'écoute des mises à jour en temps réel...")
        for message in self.source_manager.listen_to_websocket(ws_url):
            print(f"Mise à jour reçue : {message}")
            # Traitez les messages reçus ici