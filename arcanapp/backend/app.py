from flask import Flask, jsonify
from modules.shadow.shadow_odds import ShadowOdds
from modules.meta.chrono_echo import ChronoEcho

app = Flask(__name__)

# Initialiser les modules
shadow_odds = ShadowOdds()
chrono_echo = ChronoEcho()

@app.route("/api/shadow-odds", methods=["GET"])
def get_shadow_odds():
    """
    Route pour récupérer les données de ShadowOdds.
    """
    data = shadow_odds.analyze_odds()  # Exemple d'appel à une méthode du module
    return jsonify(data)

@app.route("/api/chrono-echo", methods=["GET"])
def get_chrono_echo():
    """
    Route pour récupérer les données de ChronoEcho.
    """
    data = chrono_echo.get_historical_patterns()  # Exemple d'appel à une méthode du module
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
