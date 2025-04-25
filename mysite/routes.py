from flask import Blueprint, jsonify
from .controllers.arcan_shadow import example_analysis

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({"message": "Bienvenue sur Arcan-Backend!"})

@main.route("/arcan/analyze")
def analyze():
    result = example_analysis()
    return jsonify(result)
