import pytest
from arcanapp.modules.ui.explanatory_mode import ExplanatoryMode

def test_logging_explanations():
    module = ExplanatoryMode()
    module.log_explanation("ArcanX", "Analyzed the numerology of the match.")
    module.log_explanation("ShadowOdds", "Detected odds manipulation.")
    assert module.explanations["ArcanX"] == "Analyzed the numerology of the match."
    assert module.explanations["ShadowOdds"] == "Detected odds manipulation."

def test_generate_report():
    module = ExplanatoryMode()
    module.log_explanation("ArcanX", "Analyzed the numerology of the match.")
    report = module.generate_report()
    assert "ArcanX" in report
    assert report["ArcanX"] == "Analyzed the numerology of the match."
