"""
Tests Unitaires pour EmotiveBalance
"""

import pytest
from arcanapp.modules.emotive_balance import EmotiveBalance


@pytest.fixture
def emotive_balance_instance():
    """
    Initialise une instance d'EmotiveBalance pour les tests.
    """
    return EmotiveBalance(config_path="config/emotive_balance_config.json")


def test_load_config(emotive_balance_instance):
    """
    Vérifie si la configuration est correctement chargée.
    """
    assert "emotional_events" in emotive_balance_instance.config
    assert "default_emotional_weight" in emotive_balance_instance.config


def test_analyze(emotive_balance_instance):
    """
    Vérifie l'analyse du contexte émotionnel.
    """
    context = {"finale": True, "derby": True}
    result = emotive_balance_instance.analyze(context)
    assert "emotional_weight" in result
    assert result["emotional_weight"] > 55  # Doit augmenter en fonction de la configuration
