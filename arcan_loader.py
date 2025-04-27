import importlib
import os
import pkgutil

def load_arcan_modules():
    print("[...] Chargement des modules Arcan en cours...")
    base_package = 'app.core.modules'

    package = importlib.import_module(base_package)

    for importer, modname, ispkg in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
        try:
            module = importlib.import_module(modname)

            if hasattr(module, 'init'):
                module.init()
                print(f"[✓] Module {modname} initialisé.")
            else:
                print(f"[!] Module {modname} n'a pas de fonction init(), ignoré.")
        except Exception as e:
            print(f"[✗] Erreur en important {modname}: {e}")

if __name__ == "__main__":
    load_arcan_modules()
