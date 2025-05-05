# app/__init__.py

from flask import Flask
from .routes_test import test_blueprint

def create_app(config_name="development"):
    app = Flask(__name__)

    # Configuration basique
    app.config['SECRET_KEY'] = 'arcan-secret-key'

    # Routes de test
    app.register_blueprint(test_blueprint, url_prefix='/api/test')

    print("Application lancée.")

    return app

from notifications.notify_manager import send_push_notification, send_email, check_odds_alert
