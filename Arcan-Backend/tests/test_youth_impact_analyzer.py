import pytest
from arcanapp.modules.shadow.youth_impact_analyzer import YouthImpactAnalyzer

def test_youth_impact_activation():
    module = YouthImpactAnalyzer()
    player_data = [{"name": "Player1", "age": 19}, {"name": "Player2", "age": 25}]
    module.activate(player_data)
    assert module.active is True

    player_data = [{"name": "Player3", "age": 30}]
    module.activate(player_data)
    assert module.active is False

def test_youth_impact_analysis():
    module = YouthImpactAnalyzer()
    module.activate([{"name": "Player1", "age": 19}])
    analysis = module.analyze_performance({"data": "mock_match_data"})
    assert analysis["young_player_impact"] == "high"
    assert analysis["decisive_actions"] == 2
