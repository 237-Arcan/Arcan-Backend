#!/bin/bash
#
# bundle_arcan_backend.sh
# Crée une archive zip du projet Arcan-Backend compatible Windows/Mac/Android
#

ARCHIVE="arcan-backend-$(date +%Y%m%d_%H%M%S).zip"

echo "📦 Création de l’archive $ARCHIVE …"

# Commande zip
zip -r "$ARCHIVE" \
    Makefile \
    requirements.txt \
    arcan_loader.py \
    check_env.py \
    check_env_vars.py \
    check_project.py \
    create_module_init.py \
    diagnostic_port.py \
    fix_backend.sh \
    flask_app.py \
    generate_modules.py \
    init_arcan.py \
    security_check.py \
    start_app.py \
    wsgi.py \
    mkdir \
    logs/app.log \
    app

echo "✅ Archive ZIP créée : $ARCHIVE"
