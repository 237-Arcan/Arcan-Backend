from flask import Flask, jsonify
from app.utils.env_loader import load_environment
from app.modules.module1 import module1_function
from app.modules.module2 import module2_function

# Chargement de l'environnement
load_environment()

# Création de l'application Flask
app = Flask(__name__)

# Définition des routes
@app.route('/')
def hello():
    return jsonify(message="ArcanApp is running successfully")

@app.route('/module1')
def module1():
    result = module1_function()
    return jsonify(result=result)

@app.route('/module2')
def module2():
    result = module2_function()
    return jsonify(result=result)

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
from mysite import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
