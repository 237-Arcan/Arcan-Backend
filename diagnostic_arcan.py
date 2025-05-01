import os
import ast
import traceback

ROOT_DIR = os.path.expanduser("~/arcan-backend")
EXCLUDE_DIRS = {"__pycache__", ".git", ".venv", "venv", "env"}

def is_valid_py_file(file):
    return file.endswith(".py") and "__pycache__" not in file

def clean_pycache():
    print("Suppression des dossiers __pycache__...")
    for root, dirs, files in os.walk(ROOT_DIR):
        for d in dirs:
            if d == "__pycache__":
                path = os.path.join(root, d)
                print(f" - Supprimé : {path}")
                os.system(f"rm -rf '{path}'")

def scan_file(filepath):
    issues = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=filepath)
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                if node.module and node.level == 0:
                    try:
                        __import__(node.module)
                    except ModuleNotFoundError:
                        issues.append(f"[ModuleNotFoundError] {node.module}")
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    try:
                        __import__(alias.name)
                    except ModuleNotFoundError:
                        issues.append(f"[ModuleNotFoundError] {alias.name}")
    except SyntaxError as e:
        issues.append(f"[SyntaxError] ligne {e.lineno} : {e.msg}")
    except UnicodeDecodeError as e:
        issues.append(f"[EncodingError] : {e}")
    return issues

def main():
    clean_pycache()
    print("\nScan en cours...")
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for file in files:
            if is_valid_py_file(file):
                path = os.path.join(root, file)
                issues = scan_file(path)
                if issues:
                    print(f"\nFichier : {path}")
                    for issue in issues:
                        print(" ", issue)

if __name__ == "__main__":
    main()
