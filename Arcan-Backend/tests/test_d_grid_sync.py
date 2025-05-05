import pytest
from arcanapp.modules.supervision.d_grid_sync import DGridSync

def test_d_grid_sync_synchronization():
    module = DGridSync()
    active_modules = ["ArcanX", "ChronoEcho"]
    module.synchronize(active_modules)
    assert module.synced_modules == active_modules

def test_d_grid_sync_optimization():
    module = DGridSync()
    history_data = {"past_activations": ["ArcanX", "ShadowOdds"]}
    recommendations = module.optimize_activations(history_data)
    assert "recommended_activations" in recommendations
    assert recommendations["recommended_activations"] == ["ArcanX", "ChronoEcho"]
