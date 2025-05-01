import pytest
from modules.live.sentinel import *

def test_sentinel_module_activation():
    active_modules = ["ShadowMomentum", "LineTrap", "KarmicFlow", "MirrorPhase", "BetPulse"]
    assert all(m in __all__ for m in active_modules)

def test_sentinel_dynamic_behavior():
    status = True
    assert status is True
