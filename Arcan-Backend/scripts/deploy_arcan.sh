#!/bin/bash
# Script de déploiement pour Arcan-Backend

echo "=== Initialisation Arcan-Backend ==="

# Vérification Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 est requis mais non trouvé"
    exit 1
fi

# Installation des dépendances
pip install -r requirements.txt

# Création des dossiers nécessaires
mkdir -p logs output data/{raw,processed}

# Vérification de la structure
python3 -c "from arcan_loader import verify_structure; verify_structure()"

# Lancement des tests
pytest tests/ -v

# Lancement en mode debug ou production
if [ "$1" == "--production" ]; then
    gunicorn -w 4 -b :5000 arcan_orchestrator:app
else
    python3 arcan_orchestrator.py
fi
