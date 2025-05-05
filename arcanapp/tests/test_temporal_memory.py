"""
Tests Unitaires pour TemporalMemory
"""

import pytest
from arcanapp.modules.temporal.memory import TemporalMemory


@pytest.fixture
def temporal_memory_instance():
    """
    Initialise une instance de TemporalMemory pour les tests.
    """
    return TemporalMemory(max_history=5)


def test_initialization(temporal_memory_instance):
    """
    Vérifie que l'instance de TemporalMemory est correctement initialisée.
    """
    assert temporal_memory_instance.max_history == 5
    assert isinstance(temporal_memory_instance.history, list)
    assert len(temporal_memory_instance.history) == 0


def test_extract(temporal_memory_instance):
    """
    Vérifie que les données temporelles sont correctement extraites.
    """
    match_data = {"team_a_score": 3, "team_b_score": 2, "time_elapsed": 75}
    temporal_data = temporal_memory_instance.extract(match_data)
    
    assert "team_a_last_score" in temporal_data
    assert "team_b_last_score" in temporal_data
    assert "time_elapsed" in temporal_data
    assert temporal_data["team_a_last_score"] == 3
    assert temporal_data["team_b_last_score"] == 2
    assert temporal_data["time_elapsed"] == 75


def test_extract_empty_data(temporal_memory_instance):
    """
    Vérifie que l'extraction retourne un dictionnaire vide si les données sont absentes.
    """
    temporal_data = temporal_memory_instance.extract({})
    assert temporal_data == {}


def test_update(temporal_memory_instance):
    """
    Vérifie que la mémoire est correctement mise à jour.
    """
    context = {"stats": {"team_a": "Team A", "team_b": "Team B"}, "odds": {}}
    decision = {"action": "bet", "team": "Team A"}

    temporal_memory_instance.update(context, decision)
    
    assert len(temporal_memory_instance.history) == 1
    assert temporal_memory_instance.history[0]["context"] == context
    assert temporal_memory_instance.history[0]["decision"] == decision


def test_update_with_max_history(temporal_memory_instance):
    """
    Vérifie que la mémoire respecte la limite maximale d'historique.
    """
    for i in range(6):  # Insère 6 éléments dans un historique de taille max 5
        temporal_memory_instance.update({"stats": {"match": i}}, {"decision": f"decision_{i}"})
    
    assert len(temporal_memory_instance.history) == 5
    assert temporal_memory_instance.history[0]["context"]["stats"]["match"] == 1  # Le plus ancien est supprimé
    assert temporal_memory_instance.history[-1]["decision"] == "decision_5"  # Le plus récent est conservé


def test_get_history(temporal_memory_instance):
    """
    Vérifie que l'historique complet est retourné.
    """
    context = {"stats": {"team_a": "Team A"}}
    decision = {"action": "pass"}

    temporal_memory_instance.update(context, decision)
    history = temporal_memory_instance.get_history()
    
    assert len(history) == 1
    assert history[0]["context"] == context
    assert history[0]["decision"] == decision
