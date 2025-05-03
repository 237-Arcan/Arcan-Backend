#!/bin/bash

set -e

PROJECT_ROOT=~/arcan-backend
BACKUP_ROOT=~/arcan-backend-backup
LOGFILE=$PROJECT_ROOT/migration.log

echo "### MIGRATION ARCAN BACKEND ###"
echo "Sauvegarde du projet initial vers $BACKUP_ROOT..."
cp -r "$PROJECT_ROOT" "$BACKUP_ROOT"

echo "Création de la nouvelle structure..."
mkdir -p $PROJECT_ROOT/{api/routes,app/config,app/core,app/meta_levels,modules,scripts,tests}

echo "Déplacement des modules analytiques dans modules/"
for mod in arcan_shadow arcan_sentinel captainswitch mirrorphase shadowmomentum betpulse karmicflow \
            clutchtimescanner momentumshifttracker setpiecethreatevaluator fansentimentmonitor \
            late_surgedetector youthimpactanalyzer chronoecho arcanbrain arcanforge; do
    if [ -d "$PROJECT_ROOT/$mod" ]; then
        mv "$PROJECT_ROOT/$mod" "$PROJECT_ROOT/modules/"
        echo "Déplacé : $mod -> modules/" >> "$LOGFILE"
    fi
done

echo "Déplacement des composants du cœur applicatif dans app/core/"
for core_file in arcan_loader.py predictive_engine.py shadow_odds_engine.py realtime_dashboard.py; do
    if [ -f "$PROJECT_ROOT/$core_file" ]; then
        mv "$PROJECT_ROOT/$core_file" "$PROJECT_ROOT/app/core/"
        echo "Déplacé : $core_file -> app/core/" >> "$LOGFILE"
    fi
done

echo "Déplacement des scripts annexes dans scripts/"
for script in *.sh; do
    if [ -f "$PROJECT_ROOT/$script" ]; then
        mv "$PROJECT_ROOT/$script" "$PROJECT_ROOT/scripts/"
        echo "Déplacé : $script -> scripts/" >> "$LOGFILE"
    fi
done

echo "Déplacement des tests dans tests/"
find "$PROJECT_ROOT" -name "test_*.py" -exec mv {} "$PROJECT_ROOT/tests/" \;

echo "Nettoyage terminé."
echo "Un fichier migration.log a été généré à la racine pour suivre les déplacements."

echo "### MIGRATION TERMINÉE AVEC SUCCÈS ###"
