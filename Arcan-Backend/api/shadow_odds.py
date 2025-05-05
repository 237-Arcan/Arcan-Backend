from flask import Blueprint, jsonify
from services.odds_fetcher import fetch_odds

shadow_odds = Blueprint("shadow_odds", __name__)

@shadow_odds.route("/api/shadow-odds", methods=["GET"])
def get_shadow_odds():
    data = fetch_odds()
    return jsonify(data)
