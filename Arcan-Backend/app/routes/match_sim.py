from flask import Blueprint

match_sim_bp = Blueprint('match_sim', __name__)

@match_sim_bp.route('/simulate')
def simulate():
    return "Simulation en cours..."
