import pytest
from arcanapp.modules.shadow.eastern_gate import EasternGate
from arcanapp.modules.live.sentinel import Sentinel

def test_eastern_gate_activation():
    module = EasternGate()
    match_context = {"region": "Asia"}
    module.activate(match_context)
    assert module.active is True

def test_sentinel_module_activation():
    sentinel = Sentinel()
    active_modules = ["ShadowMomentum", "LineTrap", "KarmicFlow", "MirrorPhase", "BetPulse"]
    for module in active_modules:
        assert module in sentinel.__all__

def test_interaction_shadow_and_chrono():
    # Simule une interaction entre ShadowOdds et ChronoEcho
    shadow_output = {"alert": True}
    chrono_output = {"repeat_pattern": "score_mirror"}
    assert shadow_output["alert"] and chrono_output["repeat_pattern"] == "score_mirror"
