import os

API_DOC = """# ArcanApp – Documentation des API & Fichiers Clés

## 1. Fichiers Critiques

### predictive_engine.py
- **Rôle :** Cœur du moteur prédictif d’ArcanApp.
- **Fonctionnalités :**
  - Prédictions basées sur l’analyse ésotérique, statistique et comportementale.
  - Interface avec les modules ArcanX, Shadow, Live.
- **Responsabilités principales :**
  - Centralisation de la logique de score.
  - Gestion des modules ArcanX + ShadowOdds.
  - Chargement des modèles si XGBoost activé.

---

### realtime_dashboard.py
- **Rôle :** Affichage et mise à jour en temps réel des signaux prédictifs.
- **Fonctionnalités :**
  - Vue live de l’analyse ArcanSentinel.
  - Monitoring des modules : CrowdPressureIndex, MomentumShift, FanSentimentMonitor, etc.
- **Responsabilités principales :**
  - Rafraîchissement dynamique.
  - Connexion à l’API interne via WebSocket ou HTTP polling.

---

## 2. APIs Exposées (Endpoints internes à venir)

> Tous les endpoints REST seront placés dans `/api/v1/` via `FastAPI` ou `Flask` selon ton choix final.

| Endpoint                      | Méthode | Description |
|------------------------------|---------|-------------|
| `/api/v1/predict`            | POST    | Lance une prédiction complète sur match fourni. |
| `/api/v1/live-feed`          | GET     | Renvoie les signaux live en temps réel (sentinel, odds, etc.). |
| `/api/v1/modules/status`     | GET     | Statut d’activation des modules. |
| `/api/v1/init-arcan`         | POST    | Initialise ArcanApp avec les bons paramètres. |

---

## 3. Dépendances Clés

| Module            | Utilité principale                                  |
|-------------------|-----------------------------------------------------|
| `numpy` / `pandas`| Traitement des données pré-match.                   |
| `scikit-learn`    | Modélisation statistique de base.                   |
| `xgboost`         | Modèle prédictif avancé utilisé par ArcanX.         |
| `requests`        | Requête des API de données externes (Flashscore).   |
| `websockets`      | Communication temps réel avec les modules live.     |
| `astropy`         | Calculs astrologiques ésotériques (module ArcanX).  |

---

## 4. Notes
- Une API publique REST sera couplée avec une version CLI.
- Un **fichier `.env`** est requis pour stocker les clés API (datasources externes).
- Tous les modules critiques sont instanciés dynamiquement via `orchestrator.py`.

"""

def generate_api_doc():
    with open("API_OVERVIEW.md", "w", encoding="utf-8") as f:
        f.write(API_DOC)
    print("[✓] Documentation API générée : API_OVERVIEW.md")

if __name__ == "__main__":
    generate_api_doc()
