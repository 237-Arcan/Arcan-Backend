import pytest
from arcanapp.modules.shadow.eastern_gate import EasternGate

def test_eastern_gate_activation():
    module = EasternGate()
    match_context = {"region": "Asia"}
    module.activate(match_context)
    assert module.active is True

    match_context = {"region": "Europe"}
    module.activate(match_context)
    assert module.active is False

def test_eastern_gate_analysis():
    module = EasternGate()
    module.activate({"region": "Asia"})
    analysis = module.analyze_dynamics({"data": "mock_match_data"})
    assert analysis["energy_factor"] == "high"
    assert analysis["humidity_effect"] == "moderate"
    assert analysis["location_influence"] == "strong"
