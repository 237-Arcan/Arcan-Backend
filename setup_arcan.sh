#!/bin/bash

echo "===== Initialisation de ArcanBackend ====="

# Création de l'environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installation des dépendances de requirements.txt
pip install -r requirements.txt

# Fichier .env si absent
if [ ! -f .env ]; then
  echo "ODDS_API_KEY=ta_clé_api_oddsapi_ici" > .env
  echo "[.env créé]"
fi

echo "===== Setup terminé ====="
echo "Lance maintenant :"
echo "  source venv/bin/activate"
echo "  export FLASK_APP=flask_app.py"
echo "  flask run"
