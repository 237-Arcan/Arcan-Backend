#Interface Utilisateur – ArcanShadow

# Ce fichier gère les routes pour afficher l'interface utilisateur.

from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Simuler des données pour les graphiques
def generate_mock_data():
    return [{"label": f"Match {i+1}", "value": random.randint(1, 100)} for i in range(10)]

@app.route("/")
def dashboard():

#    Route principale pour afficher le tableau de bord synthétique.
    data = generate_mock_data()
    return render_template("dashboard.html", data=data)

@app.route("/mode-simulation")
def mode_simulation():
  
    "Route pour afficher le mode simulation."

    return render_template("simulation.html")

@app.route("/api/data")
def api_data():
    API pour fournir des données de graphique.
   
    return jsonify(generate_mock_data())

if __name__ == "__main__":
    app.run(debug=True)
