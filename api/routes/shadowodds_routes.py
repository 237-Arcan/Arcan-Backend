# Routes pour ShadowOdds

from flask import Blueprint, request, jsonify
from arcan_core.shadowodds.shadowodds_service import ShadowOddsService

shadowodds_bp = Blueprint('shadowodds', __name__)
shadowodds_service = ShadowOddsService()

@shadowodds_bp.route('/analyze', methods=['POST'])
def analyze_odds():
    """Analyse des cotes et des mises."""
    odds_data = request.json.get('odds_data')
    if not odds_data:
        return jsonify({"error": "Données manquantes"}), 400

    result = shadowodds_service.analyze_odds_behavior(odds_data)
    return jsonify(result)
