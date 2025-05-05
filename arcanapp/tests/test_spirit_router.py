"""
Tests Unitaires pour SpiritRouter
"""

import pytest
from arcanapp.modules.spirit_router import SpiritRouter


@pytest.fixture
def spirit_router_instance():
    """
    Initialise une instance de SpiritRouter pour les tests.
    """
    return SpiritRouter(config_path="config/spirit_router_config.json")


def test_load_config(spirit_router_instance):
    """
    Vérifie si la configuration est correctement chargée.
    """
    assert "astrological_impact" in spirit_router_instance.config
    assert "default_sync_score" in spirit_router_instance.config


def test_analyze(spirit_router_instance):
    """
    Vérifie l'analyse du contexte astrologique.
    """
    context = {"lune": "scorpion", "mercure": "retrograde"}
    result = spirit_router_instance.analyze(context)
    assert "sync_score" in result
    assert result["sync_score"] > 42  # Doit augmenter en fonction de la configuration
