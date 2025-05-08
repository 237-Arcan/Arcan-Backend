from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI(
    title="ArcanApp API",
    description="Documentation des modules internes ArcanX, ShadowOdds, Sentinel, etc.",
    version="1.0.0",
    contact={
        "name": "ArcanX Project",
        "email": "support@arcanx.ai"
    }
)

# Exemple de route prédictive
@app.post("/api/v1/predict")
async def predict(match: dict):
    """
    Lancer une prédiction ArcanX complète (statistiques, ésotérisme, ShadowOdds).
    """
    # Remplacer avec le vrai appel au moteur de prédiction
    return {"prediction": "2-1", "confidence": 0.78}

# Statut des modules
@app.get("/api/v1/modules/status")
async def module_status():
    """
    Retourne l'état des modules critiques en cours.
    """
    return {
        "ArcanX": "active",
        "ShadowOdds": "active",
        "ChronoEcho": "loaded",
        "Sentinel": "ready"
    }

# Exemple de gestion d'erreur
@app.exception_handler(Exception)
async def custom_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": str(exc)})

# Lancer avec : uvicorn main_api:app --reload

@app.get("/api/v1/top-betting-patterns")
async def top_betting_patterns():
    """
    Retourne les formules de mise les plus fréquentes.
    """
    try:
        betting_data = pd.read_csv("data/player_bets.csv")  # Charger les données de mise des joueurs
        patterns_analyzer = PlayerBettingPatterns(betting_data)
        top_patterns = patterns_analyzer.extract_common_patterns()
        return {"top_betting_patterns": top_patterns}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/api/v1/player-betting-patterns/{player_id}")
async def player_betting_patterns(player_id: str):
    """
    Retourne les formules de mise spécifiques à un joueur.
    """
    try:
        betting_data = pd.read_csv("data/player_bets.csv")
        patterns_analyzer = PlayerBettingPatterns(betting_data)
        player_patterns = patterns_analyzer.player_specific_patterns(player_id)
        return {"player_betting_patterns": player_patterns}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
