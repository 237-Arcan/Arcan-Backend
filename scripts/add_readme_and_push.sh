#!/bin/bash

echo "==> Création des fichiers README.md..."

mkdir -p data/results
mkdir -p data/leagues

echo "# Dossier data" > data/README.md
echo "# Dossier results" > data/results/README.md
echo "# Dossier leagues" > data/leagues/README.md

echo "[✓] Fichiers README.md créés."

echo "==> Ajout des fichiers à Git..."
git add data/README.md data/results/README.md data/leagues/README.md

echo "==> Commit des changements..."
git commit -m "Ajout des fichiers README.md pour visualisation des dossiers sur GitHub"

echo "==> Push vers le dépôt distant..."
git push origin main

echo "[✓] Terminé. Les dossiers devraient maintenant apparaître dans GitHub."
