#!/bin/bash

# Étape 1 : Création de l'arborescence si elle n'existe pas
mkdir -p data/results
mkdir -p data/leagues

echo "[✓] Arborescence des dossiers créée."

# Étape 2 : Vérifie la présence des fichiers requis
declare -a required_files=(
  "data/results/actual_results.csv"
  "data/results/results.parquet"
  "data/leagues/english-premier-league.csv"
  "data/leagues/spanish-la-liga.csv"
  "data/leagues/italian-serie-a.csv"
  "data/leagues/german-bundesliga.csv"
  "data/leagues/french-ligue-1.csv"
)

all_present=true

for file in "${required_files[@]}"; do
  if [ ! -f "$file" ]; then
    echo "[!] Fichier manquant : $file"
    all_present=false
  fi
done

if [ "$all_present" = false ]; then
  echo "Erreur : Un ou plusieurs fichiers de jeux de données sont manquants."
  exit 1
fi

# Étape 3 : Ajout et commit dans Git
git add data/
git commit -m "Ajout des jeux de données recommandés pour ArcanApp"
git push origin main  # remplace 'main' si ta branche est 'master'

echo "[✓] Fichiers poussés sur GitHub avec succès."
