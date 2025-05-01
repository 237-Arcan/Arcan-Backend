import os
import ast

PROJECT_ROOT = os.path.expanduser("~/arcan-backend")
EXCLUDED_MODULES = ["fastapi", "sklearn", "prophet", "pandas"]

def scan_file(path):
    with open(path, "r", encoding="utf-8") as file:
        try:
            tree = ast.parse(file.read(), filename=path)
        except SyntaxError:
            return []
    errors = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split('.')[0] not in EXCLUDED_MODULES:
                    try:
                        __import__(alias.name)
                    except ModuleNotFoundError as e:
                        errors.append((alias.name, path))
        elif isinstance(node, ast.ImportFrom):
            if node.module and node.module.split('.')[0] not in EXCLUDED_MODULES:
                try:
                    __import__(node.module)
                except ModuleNotFoundError as e:
                    errors.append((node.module, path))
    return errors

def fix_import_path(module_path):
    """ Essaie de corriger automatiquement les chemins basés sur la structure réelle """
    parts = module_path.split('.')
    current_path = PROJECT_ROOT
    for i, part in enumerate(parts):
        try_path = os.path.join(current_path, part)
        if os.path.isdir(try_path):
            current_path = try_path
        elif os.path.isfile(try_path + ".py"):
            return ".".join(parts[:i+1])
    return None

def process():
    print("Scan et correction en cours...\n")
    for root, dirs, files in os.walk(PROJECT_ROOT):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                issues = scan_file(filepath)
                if issues:
                    print(f"\n[{file}] : {len(issues)} erreur(s) d'import")
                    with open(filepath, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                    changed = False
                    for mod, _ in issues:
                        fixed = fix_import_path(mod)
                        if fixed and fixed != mod:
                            for i, line in enumerate(lines):
                                if mod in line:
                                    lines[i] = line.replace(mod, fixed)
                                    changed = True
                                    print(f" - Corrigé : {mod} -> {fixed}")
                    if changed:
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.writelines(lines)
                        print(" -> Fichier mis à jour.")
                    else:
                        print(" -> Pas de correction automatique trouvée.")
    print("\nTerminé.")

if __name__ == "__main__":
    process()
