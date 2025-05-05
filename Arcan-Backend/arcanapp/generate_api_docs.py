import os

api_doc = """
# Documentation API & Composants Critiques - ArcanApp

## 1. API Exposées (Endpoints prévus)

| Méthode | Endpoint                    | Description                                             |
|--------:|-----------------------------|---------------------------------------------------------|
| GET     | /predict                    | Lancer une prédiction ArcanX ou ArcanShadow.           |
| GET     | /live/analyze               | Démarre l’analyse live avec ArcanSentinel.             |
| POST    | /feedback                   | Envoie un retour d’analyse pour apprentissage.         |
| GET     | /dashboard/status           | Affiche les métriques en temps réel du backend.        |

---

## 2. Dépendances Spécifiques

- **pandas**, **numpy** : Manipulation de données statistiques.
- **scikit-learn**, **xgboost** : Prédictions & modèles ML.
- **sympy**, **pytz**, **ephem** : Calculs ésotériques & temporels.
- **uvicorn**, **fastapi** : Framework API backend ultra-léger.
- **aiohttp**, **websockets** : Comms temps réel live/dashboard.
- **pyyaml**, **requests**, **orjson** : Configuration rapide, I/O.
- **matplotlib**, **plotly** (optionnel) : Visualisations internes.

---

## 3. Fichiers Critiques

### `app/core/predictive_engine.py`
Responsable de :
- Chargement et orchestration des modèles hybrides.
- Fusion ArcanX (ésotérisme) + ShadowOdds (comportement).
- Renvoie un dictionnaire structuré avec les insights par module.

Entrées :
```json
{
  "match_id": 123,
  "date": "2025-05-01",
  "teams": ["Team A", "Team B"]
}
