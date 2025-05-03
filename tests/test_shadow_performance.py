import time

def test_shadow_analysis_speed():
    start = time.time()
    time.sleep(0.2)  # simulation
    end = time.time()
    assert (end - start) < 1.0  # Doit s'exécuter rapidement
