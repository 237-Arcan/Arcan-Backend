from flask import Blueprint
from app.core.shadow_odds_engine import calculate_odds

shadow_odds_bp = Blueprint('shadow_odds', __name__)

@shadow_odds_bp.route('/predict')
def predict():
    return calculate_odds()
