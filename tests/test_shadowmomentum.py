import pytest
from app.core.modules.arcan_sentinel.shadowmomentum.manager import ShadowMomentumManager

@pytest.fixture
def mock_match_data():
    return {
        "high_pressure_sequences": 6,
        "team_b_reacts": True,
        "dominated_team": "Team A",
        "possession_neutral": 65,
        "territorial_advantage": 72,
        "pressing_team": "Team B",
        "dangerous_free_kicks": 3,
        "near_goal_events": 4,
        "attacking_team": "Team A",
        "importance": "high",
        "live_mode": True
    }

def test_momentum_shift_tracker(mock_match_data):
    manager = ShadowMomentumManager()
    result = manager.analyzer.momentum_shift_tracker(mock_match_data)
    assert result["shift_detected"] is True
    assert result["team"] == "Team A"

def test_quiet_storm_signal(mock_match_data):
    manager = ShadowMomentumManager()
    result = manager.analyzer.quiet_storm_signal(mock_match_data)
    assert result["quiet_storm_detected"] is True
    assert result["team"] == "Team B"

def test_red_zone_phase(mock_match_data):
    manager = ShadowMomentumManager()
    result = manager.analyzer.red_zone_phase(mock_match_data)
    assert result["red_zone"] is True
    assert result["team"] == "Team A"
