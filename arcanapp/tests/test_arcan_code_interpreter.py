"""
Tests Unitaires pour ArcanCodeInterpreter
"""

import pytest
from arcanapp.modules.arcan_code_interpreter import ArcanCodeInterpreter


@pytest.fixture
def arcan_code_interpreter_instance():
    """
    Initialise une instance d'ArcanCodeInterpreter pour les tests.
    """
    return ArcanCodeInterpreter(config_path="config/arcan_code_interpreter_config.json")


def test_load_config(arcan_code_interpreter_instance):
    """
    Vérifie si la configuration est correctement chargée.
    """
    assert "patterns" in arcan_code_interpreter_instance.config
    assert "default_decoded_pattern" in arcan_code_interpreter_instance.config


def test_analyze(arcan_code_interpreter_instance):
    """
    Vérifie l'analyse des motifs et cycles.
    """
    context = {"mirror_date": "2025-05-05"}
    result = arcan_code_interpreter_instance.analyze(context)
    assert "decoded_pattern" in result
    assert "pattern miroir détecté" in result["decoded_pattern"]  # Doit détecter un pattern miroir
