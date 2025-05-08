import pytest
from app.core.modules.arcan_shadow.crowdpressureindex.manager import CrowdPressureIndexManager

@pytest.fixture
def mock_event_data():
    return {
        "minute": 80,
        "crowd_volume": 75,
        "favored_team": "Team A",
        "players": [
            {"name": "Player 1", "errors": 4, "crowd_reaction": "negative"},
            {"name": "Player 2", "errors": 1, "crowd_reaction": "positive"}
        ],
        "type": "goal",
        "reaction_factor": 1.2
    }

def test_clutch_time_boost(mock_event_data):
    manager = CrowdPressureIndexManager()
    result = manager.analyzer.clutch_time_boost(mock_event_data)
    assert result["boost"] is True
    assert result["team"] == "Team A"

def test_nervous_shift(mock_event_data):
    manager = CrowdPressureIndexManager()
    result = manager.analyzer.nervous_shift(mock_event_data['players'])
    assert len(result) == 1
    assert result[0]["name"] == "Player 1"

def test_fan_surge(mock_event_data):
    manager = CrowdPressureIndexManager()
    result = manager.analyzer.fan_surge(mock_event_data)
    assert result["intensity"] > 0
