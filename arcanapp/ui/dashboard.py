
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Modules actifs simulés
active_modules = {
    "ShadowOdds": {"status": "active", "alerts": 3},
    "ChronoEcho": {"status": "active", "alerts": 1},
    "MomentumShift": {"status": "inactive", "alerts": 0}
}

@app.route("/")
def dashboard():
    Route principale pour afficher le tableau de bord.
    return render_template("dashboard.html", modules=active_modules)

@app.route("/alerts", methods=["GET"])
def get_alerts():
    API pour récupérer les alertes en cours.
    alerts = {
        "ShadowOdds": "Dérive de cotes détectée.",
        "ChronoEcho": "Motif historique détecté."
    }
    return jsonify(alerts)

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Modules actifs simulés
active_modules = {
    "ShadowOdds": {"status": "active", "alerts": 3},
    "ChronoEcho": {"status": "active", "alerts": 1},
    "MomentumShift": {"status": "inactive", "alerts": 0}
}

@app.route("/")
def dashboard():
    """
    Route principale pour afficher le tableau de bord.
    """
    return render_template("dashboard.html", modules=active_modules)

@app.route("/alerts", methods=["GET"])
def get_alerts():
    """
    API pour récupérer les alertes en cours.
    """
    alerts = {
        "ShadowOdds": "Dérive de cotes détectée.",
        "ChronoEcho": "Motif historique détecté."
    }
    return jsonify(alerts)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/explanations", methods=["GET"])
def get_explanations():
    """
    API pour fournir des explications sur les prédictions.
    """
    explanations = {
        "ShadowOdds": "Analyse comportementale des cotes détectée.",
        "ChronoEcho": "Cycle historique identifié pour l'équipe X."
    }
    return jsonify(explanations)
