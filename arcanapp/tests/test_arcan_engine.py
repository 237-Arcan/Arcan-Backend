"""
Tests Unitaires pour ArcanEngine
"""

import pytest
from arcanapp.engine.arcan_engine import ArcanEngine


@pytest.fixture
def arcan_engine_instance():
    """
    Initialise une instance d'ArcanEngine pour les tests.
    """
    return ArcanEngine()


def test_load_context(arcan_engine_instance):
    """
    Vérifie que le contexte est correctement chargé.
    """
    match_data = {"team_a": "Team A", "team_b": "Team B", "score": "2-1"}
    esoteric_data = {"lune": "scorpion", "mercure": "direct"}
    odds_data = {"team_a_odds": 1.5, "team_b_odds": 2.8}

    arcan_engine_instance.load_context(match_data, esoteric_data, odds_data)
    assert "stats" in arcan_engine_instance.current_context
    assert "astro" in arcan_engine_instance.current_context
    assert "odds" in arcan_engine_instance.current_context
    assert "temporal" in arcan_engine_instance.current_context


def test_run_decision(arcan_engine_instance, mocker):
    """
    Vérifie que la méthode run_decision retourne une décision valide.
    """
    match_data = {"team_a": "Team A", "team_b": "Team B", "score": "2-1"}
    esoteric_data = {"lune": "scorpion", "mercure": "direct"}
    odds_data = {"team_a_odds": 1.5, "team_b_odds": 2.8}

    mock_decision = {"action": "bet", "team": "Team A"}
    mocker.patch.object(arcan_engine_instance.ia_arcan, "decide", return_value=mock_decision)
    
    arcan_engine_instance.load_context(match_data, esoteric_data, odds_data)
    decision = arcan_engine_instance.run_decision()
    
    assert decision == mock_decision
    assert "action" in decision
    assert "team" in decision
