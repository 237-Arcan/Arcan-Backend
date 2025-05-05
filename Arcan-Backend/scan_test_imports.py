import os
import ast
import importlib.util

ROOT_DIR = os.path.expanduser("~/arcan-backend")
error_report = []

def is_test_file(filename):
    return filename.startswith("test_") and filename.endswith(".py")

def scan_imports_in_file(filepath):
    rel_path = os.path.relpath(filepath, ROOT_DIR)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError as e:
        error_report.append((rel_path, "EncodingError", str(e)))
        return

    try:
        tree = ast.parse(content, filename=filepath)
    except SyntaxError as e:
        error_report.append((rel_path, "SyntaxError", str(e)))
        return

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                check_import(alias.name, rel_path)
        elif isinstance(node, ast.ImportFrom):
            mod = node.module
            if mod:
                check_import(mod, rel_path)

def check_import(module_name, rel_path):
    try:
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            raise ModuleNotFoundError
    except ModuleNotFoundError:
        error_report.append((rel_path, "ModuleNotFoundError", module_name))

def main():
    for dirpath, _, filenames in os.walk(ROOT_DIR):
        for filename in filenames:
            if is_test_file(filename) or "tests" in dirpath:
                full_path = os.path.join(dirpath, filename)
                scan_imports_in_file(full_path)

    if not error_report:
        print("Aucun problème d'import détecté dans les tests.")
    else:
        print("Problèmes détectés :\n")
        for filepath, err_type, detail in error_report:
            print(f"[{err_type}] dans {filepath} -> {detail}")

if __name__ == "__main__":
    main()
