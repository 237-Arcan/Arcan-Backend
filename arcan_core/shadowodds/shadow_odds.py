# Suggestions pour le module ShadowOdds

# Créer une fonction d'entrée principale pour exécuter une analyse complète.

from arcan_core.shadowodds.shadowodds_service import ShadowOddsService

def shadow_odds_function(odds_data):
    """
    Fonction principale pour exécuter une analyse complète des cotes et des mises.
    """
    service = ShadowOddsService()
    analysis_result = service.analyze_odds_behavior(odds_data)
    return analysis_result
