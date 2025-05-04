"""
Tests pour l'intégration entre IA-Arcan et ArcanReflex.
"""

import pytest
from arcanapp.modules.integration_ia_reflex import evaluate_and_revise


def test_evaluate_and_revise():
    """
    Teste le processus d'évaluation et de révision.
    """
    sample_context = {
        "competition": "league",
        "events": [{"minute": 91, "type": "red_card"}],
        "reality": {"module1": "success", "module2": "failure"},
    }
    result = evaluate_and_revise(sample_context)

    assert "scores" in result
    assert "anomalies" in result
    assert "mismatches" in result
    assert len(result["anomalies"]) > 0
    assert len(result["mismatches"]) > 0
