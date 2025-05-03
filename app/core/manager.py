from app.core.status_manager import get_status
from app.modules import (
    chrono_echo,
    shadow_odds,
    crowd_pressure_index,
    captain_switch,
    momentum_shift,
    youth_impact_analyzer,
    late_surge_detector,
    set_piece_threat_evaluator,
    fan_sentiment_monitor,
    karmic_flow,
    mirror_phase,
    bet_pulse,
    line_trap,
    shadow_momentum,
)

def run_all_modules(context):
    if get_status("ChronoEcho") == "active":
        chrono_echo.run(context)

    if get_status("ShadowOdds") == "active":
        shadow_odds.run(context)

    if get_status("CrowdPressureIndex") == "active":
        crowd_pressure_index.run(context)

    if get_status("CaptainSwitch") == "active":
        captain_switch.run(context)

    if get_status("MomentumShift") == "active":
        momentum_shift.run(context)

    if get_status("YouthImpactAnalyzer") == "active":
        youth_impact_analyzer.run(context)

    if get_status("LateSurgeDetector") == "active":
        late_surge_detector.run(context)

    if get_status("SetPieceThreatEvaluator") == "active":
        set_piece_threat_evaluator.run(context)

    if get_status("FanSentimentMonitor") == "active":
        fan_sentiment_monitor.run(context)

    if get_status("KarmicFlow") == "active":
        karmic_flow.run(context)

    if get_status("MirrorPhase") == "active":
        mirror_phase.run(context)

    if get_status("BetPulse") == "active":
        bet_pulse.run(context)

    if get_status("LineTrap") == "active":
        line_trap.run(context)

    if get_status("ShadowMomentum") == "active":
        shadow_momentum.run(context)
