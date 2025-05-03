#!/bin/bash

echo "[*] Création de l’arborescence de dossiers..."

# Liste des dossiers à créer
folders=(
  "data"
  "data/results"
  "data/leagues"
)

# Création des dossiers
for folder in "${folders[@]}"; do
  mkdir -p "$folder"
  echo "[✓] Dossier créé : $folder"
done

# Liste des fichiers attendus (pour info uniquement)
expected_files=(
  "data/results/actual_results.csv"
  "data/results/results.parquet"
  "data/leagues/english-premier-league.csv"
  "data/leagues/spanish-la-liga.csv"
  "data/leagues/italian-serie-a.csv"
  "data/leagues/german-bundesliga.csv"
  "data/leagues/french-ligue-1.csv"
)

echo ""
echo "[!] Vérification des fichiers (informations seulement) :"

missing=false
for file in "${expected_files[@]}"; do
  if [ ! -f "$file" ]; then
    echo "  [!] Fichier manquant (à créer plus tard) : $file"
    missing=true
  fi
done

echo ""
echo "[✓] Arborescence prête. Les fichiers manquants seront ajoutés manuellement."
exit 0


# Ajoute ce bloc à la fin de ton script push_datasets_to_github.sh

# Ajouter des fichiers .gitkeep pour que les dossiers vides soient suivis par Git
for folder in "${folders[@]}"; do
  touch "$folder/.gitkeep"
  echo "[+] .gitkeep ajouté à : $folder"
done
