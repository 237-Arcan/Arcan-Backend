#!/data/data/com.termux/files/usr/bin/bash

echo "[1/4] Vérification et mise à jour des modules ArcanApp..."

declare -A MODULES
MODULES=(
  ["arcanapp/modules/live/sentinel.py"]="Sentinel"
  ["arcanapp/modules/arcanx/analyzer.py"]="ArcanXAnalyzer"
  ["arcanapp/modules/shadow/odds_analyzer.py"]="ShadowOddsAnalyzer"
)

for path in "${!MODULES[@]}"; do
  class_name=${MODULES[$path]}
  if [ ! -f "$path" ]; then
    echo "[Création] $path (classe $class_name)"
    mkdir -p "$(dirname "$path")"
    echo -e "class $class_name:\n    def __init__(self):\n        print(\"[$class_name] Initialisation...\")\n\n    def run(self):\n        print(\"[$class_name] Analyse en cours...\")" > "$path"
  else
    if ! grep -q "class $class_name" "$path"; then
      echo "[Ajout] Classe $class_name manquante dans $path. Ajout..."
      echo -e "\n\nclass $class_name:\n    def __init__(self):\n        print(\"[$class_name] Initialisation...\")\n\n    def run(self):\n        print(\"[$class_name] Analyse en cours...\")" >> "$path"
    else
      echo "[OK] $class_name déjà présent dans $path"
    fi
  fi
done

echo "[2/4] Vérification des fichiers __init__.py..."
find arcanapp -type d | while read dir; do
  if [ ! -f "$dir/__init__.py" ]; then
    echo "[Ajout] $dir/__init__.py"
    touch "$dir/__init__.py"
  fi
done

echo "[3/4] Lancement test du mode live..."
python -m arcanapp.run_arcanapp --mode live

echo "[4/4] Vérification terminée."

