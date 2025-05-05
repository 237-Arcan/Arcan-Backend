"""
Tests Unitaires pour AnomalicRadar
"""

import pytest
from arcanapp.modules.anomalic_radar import AnomalicRadar


@pytest.fixture
def anomalic_radar_instance():
    """
    Initialise une instance d'AnomalicRadar pour les tests.
    """
    return AnomalicRadar()


def test_scan(anomalic_radar_instance):
    """
    Vérifie la détection des anomalies dans le contexte.
    """
    context = {"recent_events": ["unexpected_pattern", "high_activity"]}
    result = anomalic_radar_instance.scan(context)
    assert "frequency" in result
    assert 0 <= result["frequency"] <= 1  # La fréquence doit être entre 0 et 1

