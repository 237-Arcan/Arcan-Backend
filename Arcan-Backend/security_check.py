# security_check.py

import os
import sys

def detect_app_run_files():
    """Cherche dans tous les fichiers .py un app.run() qui pourrait poser problème."""
    root_dir = "."
    found_files = []

    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".py"):
                filepath = os.path.join(foldername, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                        if "app.run(" in content and "start_app.py" not in filepath:
                            found_files.append(filepath)
                except Exception as e:
                    print(f"Erreur en lisant {filepath}: {e}")

    return found_files

if __name__ == "__main__":
    files = detect_app_run_files()
    if files:
        print("\033[91m" + "!!! ATTENTION !!!" + "\033[0m")
        print("Les fichiers suivants contiennent un app.run() qui peut bloquer le serveur :")
        for f in files:
            print(f" -> {f}")
        print("\nCorrige cela avant de relancer l'application.")
        sys.exit(1)
    else:
        print("\033[92m" + "Sécurité OK : aucun app.run() parasite détecté." + "\033[0m")


import sys
import os

# Vérifier les fichiers contenant app.run()
def check_security():
    problematic_files = []
    for filename in ["flask_app.py", "security_check.py", "start_app.py"]:
        with open(filename, "r") as f:
            if "app.run()" in f.read():
                problematic_files.append(filename)
    return problematic_files

def main():
    print("!!! ATTENTION !!!")
    problematic_files = check_security()
    if problematic_files:
        print("Les fichiers suivants contiennent un app.run() qui peut bloquer le serveur :")
        for file in problematic_files:
            print(f" -> {file}")
        sys.exit(1)
    else:
        print("Pas de problème détecté avec les fichiers app.run()")

if __name__ == "__main__":
    main()
