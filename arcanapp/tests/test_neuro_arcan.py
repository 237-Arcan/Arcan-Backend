"""
Tests Unitaires pour NeuroArcan
"""

import pytest
from arcanapp.modules.neuro_arcan import NeuroArcan


@pytest.fixture
def neuro_arcan_instance():
    """
    Initialise une instance de NeuroArcan pour les tests.
    """
    return NeuroArcan()


def test_simulate(neuro_arcan_instance):
    """
    Vérifie la simulation des scénarios.
    """
    history = [{"prediction": "Win", "confidence": 70}]
    context = {"match_type": "friendly"}
    result = neuro_arcan_instance.simulate(history, context)

    assert "best_scenario" in result
    assert "prediction" in result["best_scenario"]
    assert "confidence" in result["best_scenario"]
    assert result["best_scenario"]["confidence"] == 68  # Vérifie le comportement par défaut
