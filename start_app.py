# start_app.py

import time
import sys
import subprocess
from app import create_app

def run_dev():
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)

def run_prod():
    from waitress import serve
    app = create_app("production")
    serve(app, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_dev()


import subprocess
import time
import os
from app import create_app

def free_port(port):
    try:
        # Vérifie si le port est occupé
        output = subprocess.check_output(f"lsof -t -i:{port}", shell=True).decode().strip()
        if output:
            print(f"Port {port} occupé, tentative de libération...")
            subprocess.run(f"kill -9 {output}", shell=True)
            time.sleep(1)
            print(f"Port {port} libéré.")
    except subprocess.CalledProcessError:
        # Aucun processus trouvé sur ce port
        pass

def run_dev():
    free_port(5000)  # Avant de démarrer, libère le port 5000 si besoin
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)

def run_prod():
    from waitress import serve
    app = create_app("production")
    serve(app, host="0.0.0.0", port=5000)


from app import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

import sys
import os

# Ajouter le répertoire racine au PYTHONPATH
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)


# Dans flask_app.py ou autres
from app.core.loader import ArcanLoader
print(ArcanLoader.load_config())  # Test
