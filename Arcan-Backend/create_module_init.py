import os

MODULE_DIR = "app/core/modules"

BASIC_TEMPLATE = '''def init():
    print("{mod} prêt.")

def analyse(match_data=None):
    print("Analyse de {mod} en cours...")
'''

def create_init_files():
    for dirpath, _, _ in os.walk(MODULE_DIR):
        if dirpath.endswith("__pycache__"): continue

        init_path = os.path.join(dirpath, "__init__.py")
        modname = dirpath.replace("/", ".").replace("app.core.modules.", "")

        if not os.path.exists(init_path):
            with open(init_path, "w") as f:
                f.write(BASIC_TEMPLATE.format(mod=modname))
            print(f"[✓] Fichier __init__.py généré pour : {modname}")

if __name__ == "__main__":
    create_init_files()

