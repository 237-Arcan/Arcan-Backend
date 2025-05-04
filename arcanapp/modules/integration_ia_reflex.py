# Intégration entre IA-A
from arcanapp.modules.iaarcan import IAArcan
from app.core.meta_levels.arcanreflex import ArcanReflex
from app.core.logger import setup_logger

# Initialisation des modules
ia_arcan = IAArcan()
arcan_reflex = ArcanReflex()
logger = setup_logger("IntegrationLogger")


def evaluate_and_revise(context):
    """
    Évalue les modules via IA-Arcan et applique des révisions via ArcanReflex.
    """
    logger.info("Début de l'évaluation des modules.")
    evaluated_scores = ia_arcan.evaluate_modules(context)
    logger.info(f"Scores évalués : {evaluated_scores}")

    # Révision des prédictions par ArcanReflex
    anomalies = arcan_reflex.detect_anomalies(context.get("events", []))
    logger.info(f"Anomalies détectées : {anomalies}")

    # Comparaison avec la réalité
    prediction = evaluated_scores
    reality = context.get("reality", {})
    mismatches = arcan_reflex.compare_prediction_vs_reality(prediction, reality)
    logger.info(f"Incohérences détectées : {mismatches}")

    return {"scores": evaluated_scores, "anomalies": anomalies, "mismatches": mismatches}


if __name__ == "__main__":
    # Exemple de contexte
    sample_context = {
        "competition": "league",
        "events": [{"minute": 91, "type": "red_card"}],
        "reality": {"module1": "success", "module2": "failure"},
    }
    result = evaluate_and_revise(sample_context)
    print(result)
