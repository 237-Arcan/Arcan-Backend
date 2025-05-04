"""
Tests Unitaires pour IA-Arcan
"""

import pytest
from arcanapp.modules.ia_arcan_core import IAArcan


@pytest.fixture
def ia_arcan_instance():
    """
    Initialise une instance d'IA-Arcan pour les tests.
    """
    return IAArcan()


def test_receive_signals(ia_arcan_instance):
    """
    Vérifie que les signaux des modules sont correctement analysés.
    """
    context = {"competition": "league", "emotional_state": "high"}
    signals = ia_arcan_instance.receive_signals(context)
    assert "spirit_router" in signals
    assert "emotive_balance" in signals
    assert "arcan_code" in signals


def test_decide(ia_arcan_instance):
    """
    Vérifie la prise de décision en fonction des signaux.
    """
    context = {"competition": "league", "emotional_state": "high"}
    decision = ia_arcan_instance.decide(context)
    assert "prediction" in decision
    assert "confidence" in decision


def test_reboot_context(ia_arcan_instance):
    """
    Vérifie que le contexte est correctement réinitialisé.
    """
    ia_arcan_instance.predictions = [{"prediction": "test", "confidence": 0.9}]
    ia_arcan_instance.memory = {"short_term": ["data"]}
    ia_arcan_instance._reboot_context()
    assert ia_arcan_instance.predictions == []
    assert ia_arcan_instance.memory == {}
