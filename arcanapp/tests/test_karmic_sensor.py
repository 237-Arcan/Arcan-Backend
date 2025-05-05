import pytest
from arcanapp.modules.karmic_sensor
 import KarmicSensor


@pytest.fixture
def karmic_sensor_instance():
    """
    Initialise une instance de KarmicSensor pour les tests.
    """
    return KarmicSensor()


def test_measure(karmic_sensor_instance):
    """
    Vérifie que le module mesure correctement la charge karmique.
    """
    context = {"team_1": "Team A", "team_2": "Team B"}
    result = karmic_sensor_instance.measure(context)
    assert "load" in result
    assert 0 <= result["load"] <= 1
