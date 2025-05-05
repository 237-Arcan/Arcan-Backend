import pytest
from arcanapp.modules.shadow.eastern_gate import EasternGate
from arcanapp.modules.shadow.youth_impact_analyzer import YouthImpactAnalyzer
from arcanapp.modules.supervision.d_grid_sync import DGridSync

def test_interaction_between_eastern_gate_and_d_grid_sync():
    eastern_gate = EasternGate()
    d_grid_sync = DGridSync()

    # Activation de EasternGate
    eastern_gate.activate({"region": "Asia"})
    assert eastern_gate.active is True

    # Synchronisation avec D-GridSync
    d_grid_sync.synchronize(["EasternGate"])
    assert "EasternGate" in d_grid_sync.synced_modules

def test_combination_of_modules():
    youth_analyzer = YouthImpactAnalyzer()
    grid_sync = DGridSync()

    # Activation de YouthImpactAnalyzer
    youth_analyzer.activate([{"name": "Player1", "age": 20}])
    assert youth_analyzer.active is True

    # Synchronisation avec D-GridSync
    grid_sync.synchronize(["YouthImpactAnalyzer"])
    assert "YouthImpactAnalyzer" in grid_sync.synced_modules
