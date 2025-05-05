# app/core/status_manager.py

module_status = {
    "ChronoEcho": "active",
    "ShadowOdds": "active",
    "CrowdPressureIndex": "active",
    "CaptainSwitch": "sleep",
    "MomentumShift": "sleep",
    "YouthImpactAnalyzer": "inactive",
    "LateSurgeDetector": "sleep",
    "SetPieceThreatEvaluator": "inactive",
    "FanSentimentMonitor": "inactive",
    "KarmicFlow": "active",
    "MirrorPhase": "active",
    "BetPulse": "active",
    "LineTrap": "active",
    "ShadowMomentum": "active"
}

def get_status(module_name: str) -> str:
    return module_status.get(module_name, "inactive")

def set_status(module_name: str, status: str):
    if status not in ["active", "sleep", "inactive"]:
        raise ValueError("Status must be 'active', 'sleep', or 'inactive'")
    module_status[module_name] = status

def get_all_statuses() -> dict:
    return module_status.copy()

def activate_module(module_name: str):
    set_status(module_name, "active")

def sleep_module(module_name: str):
    set_status(module_name, "sleep")

def deactivate_module(module_name: str):
    set_status(module_name, "inactive")
