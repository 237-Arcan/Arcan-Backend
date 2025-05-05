#!/data/data/com.termux/files/usr/bin/bash

cd ~/arcan-backend

echo "[1/5] Création des dossiers manquants..."
mkdir -p arcanapp/core arcanapp/modules/arcanx arcanapp/modules/shadow arcanapp/modules/live

echo "[2/5] Création des fichiers __init__.py..."
touch arcanapp/__init__.py
touch arcanapp/core/__init__.py
touch arcanapp/modules/__init__.py
touch arcanapp/modules/arcanx/__init__.py
touch arcanapp/modules/shadow/__init__.py
touch arcanapp/modules/live/__init__.py

echo "[3/5] Déplacement de logger.py dans core/..."
if [ -f arcanapp/logger.py ]; then
  mv arcanapp/logger.py arcanapp/core/logger.py
fi

echo "[4/5] Ajout de __init__.py s'ils sont vides (import module Python)..."
for file in $(find arcanapp -type f -name '__init__.py'); do
  if [ ! -s "$file" ]; then
    echo "# Package init" > "$file"
  fi
done

echo "[5/5] Lancement du module ArcanApp..."
python -m arcanapp.run_arcanapp --mode live
