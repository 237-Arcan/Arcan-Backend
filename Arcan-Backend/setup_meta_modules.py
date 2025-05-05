import os

# Base path où seront stockés les méta-modules
BASE_META_PATH = "app/core/meta_levels"

# Liste des méta-modules à créer
META_MODULES = [
    "d_gridsync",
    "arcanreflex",
    "soulweaver",
    "mindpulse",
    "dynacore",
    "timeline_stitcher"
]

def create_meta_module_structure():
    """Crée la structure de base pour les méta-niveaux d'ArcanShadow."""
    if not os.path.exists(BASE_META_PATH):
        os.makedirs(BASE_META_PATH)
        print(f"[OK] Dossier '{BASE_META_PATH}' créé.")
    else:
        print(f"[INFO] Dossier '{BASE_META_PATH}' existe déjà.")

    for module in META_MODULES:
        module_path = os.path.join(BASE_META_PATH, module)
        init_file = os.path.join(module_path, "__init__.py")
        if not os.path.exists(module_path):
            os.makedirs(module_path)
            print(f"[OK] Module méta '{module}' créé.")
        if not os.path.exists(init_file):
            with open(init_file, "w") as f:
                f.write(f"# Initialisation du module méta {module}\n")
                f.write(f"class {module.capitalize().replace('_', '')}:\n")
                f.write("    def __init__(self):\n")
                f.write("        self.ready = False\n\n")
                f.write("    def initialize(self):\n")
                f.write(f"        print('[META] {module} initialisé.')\n")
                f.write("        self.ready = True\n")
            print(f"[OK] __init__.py pour '{module}' créé.")

def create_meta_loader():
    """Crée un fichier pour charger dynamiquement tous les méta-modules."""
    loader_path = os.path.join(BASE_META_PATH, "meta_loader.py")
    with open(loader_path, "w") as f:
        f.write("# Loader dynamique des méta-modules ArcanShadow\n\n")
        for module in META_MODULES:
            f.write(f"from .{module} import {module.capitalize().replace('_', '')}\n")
        f.write("\n\n")
        f.write("class MetaManager:\n")
        f.write("    def __init__(self):\n")
        for module in META_MODULES:
            class_name = module.capitalize().replace("_", "")
            f.write(f"        self.{module} = {class_name}()\n")
        f.write("\n")
        f.write("    def initialize_all(self):\n")
        for module in META_MODULES:
            f.write(f"        self.{module}.initialize()\n")
        f.write("\n")
        f.write("    def status(self):\n")
        f.write("        status_list = {}\n")
        for module in META_MODULES:
            f.write(f"        status_list['{module}'] = self.{module}.ready\n")
        f.write("        return status_list\n")

    print(f"[OK] meta_loader.py créé pour gérer tous les méta-modules.")

def main():
    create_meta_module_structure()
    create_meta_loader()
    print("\n[FINI] Tous les méta-modules et le meta_loader sont prêts.")

if __name__ == "__main__":
    main()
