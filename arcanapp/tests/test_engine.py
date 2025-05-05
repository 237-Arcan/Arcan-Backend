import pytest
from arcan_engine.engine import ArcanEngine

@pytest.fixture
def fake_context():
    return {
        "stats": {
            "teams": ["TeamA", "TeamB"],
            "match_time": "2025-05-04T18:00"
        },
        "astro": {
            "planetary_alignment": "Mars-Saturn",
            "karma_node": "Scorpio"
        },
        "odds": {
            "initial": 1.70,
            "final": 1.90,
            "volume": "heavy"
        }
    }

def test_decision_output(fake_context):
    engine = ArcanEngine()
    engine.load_context(**fake_context)
    decision = engine.run_decision()
    assert "prediction" in decision
    assert "activated_modules" in decision
