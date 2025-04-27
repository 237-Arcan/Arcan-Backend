#!/bin/bash

echo "=== Arcan-Backend Correctif Général (Termux Compatible) ==="

# 1. Stopper tout processus Flask en cours
echo "[1/6] Vérification des processus en cours..."
FLASK_PID=$(lsof -t -i:5000)

if [ ! -z "$FLASK_PID" ]; then
    echo "Processus Flask détecté (PID $FLASK_PID), arrêt..."
    kill -9 $FLASK_PID
else
    echo "Aucun processus Flask détecté sur le port 5000."
fi

# 2. Nettoyer les fichiers pyc et cache
echo "[2/6] Nettoyage des fichiers temporaires..."
find . -name "*.pyc" -delete
find . -name "__pycache__" -type d -exec rm -r {} +

# 3. Vérification des dépendances Python
echo "[3/6] Vérification des dépendances..."
if [ -f requirements.txt ]; then
    echo "Installation des dépendances sans mise à jour de pip..."
    pip install --no-cache-dir -r requirements.txt
else
    echo "Fichier requirements.txt introuvable, dépendances non vérifiées."
fi

# 4. Vérification de l'existence de start_app.py
echo "[4/6] Vérification de start_app.py..."
if [ -f start_app.py ]; then
    echo "start_app.py trouvé."
else
    echo "start_app.py manquant ! Correction impossible sans lui."
    exit 1
fi

# 5. Vérification du Makefile
echo "[5/6] Vérification du Makefile..."
if [ -f Makefile ]; then
    echo "Makefile trouvé."
else
    echo "Attention : Makefile manquant. Impossible de lancer avec 'make run-dev'."
fi

# 6. Lancement de l'application
echo "[6/6] Tentative de relancer l'application..."
python start_app.py

echo "=== Correctif terminé ==="

