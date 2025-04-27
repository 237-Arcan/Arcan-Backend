import importlib
import os

def discover_and_init_modules(base_path="app/core/modules"):
    print("[ARCAN INIT] Démarrage de l'initialisation des modules...")
    module_paths = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                rel_path = os.path.join(root, file).replace("/", ".").replace("\\", ".")
                module_name = rel_path.replace(".py", "")
                module_paths.append(module_name)

    for mod in module_paths:
        try:
            module = importlib.import_module(mod)
            if hasattr(module, "init"):
                module.init()
                print(f"[✓] {mod} initialisé avec succès.")
            else:
                print(f"[~] {mod} : aucune fonction init() détectée.")
        except Exception as e:
            print(f"[✗] Échec de l'initialisation de {mod} : {e}")

    print("[ARCAN INIT] Terminé.")

if __name__ == "__main__":
    discover_and_init_modules()
