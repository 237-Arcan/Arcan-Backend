from ia_arcan.reflex import ArcanReflex

def test_reflex_triggered_on_incoherence():
    reflex = ArcanReflex()
    reflex_input = {
        "current_prediction": "win",
        "actual_result": "loss",
        "coherence_score": 0.3
    }
    reflex.analyze(reflex_input)
    assert reflex.last_alert == "ReflexPulse" or reflex.last_alert == "ResetSuggestion"
