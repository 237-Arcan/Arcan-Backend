from flask import Flask
from app.routes.shadow_odds import shadow_odds_bp
from app.routes.match_sim import match_sim_bp

app = Flask(__name__)

# Configuration des Blueprints
app.register_blueprint(shadow_odds_bp, url_prefix='/shadow-odds')
app.register_blueprint(match_sim_bp, url_prefix='/match-sim')

@app.route('/')
def home():
    return "ArcanBackend - Pack A+B Actif"

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
