import json
from datetime import datetime
import os

DECISION_JOURNAL_PATH = "logs/decision_journal.json"

def log_decision(match_id, prediction, reasoning, modules_used, factors_detected, confidence_score):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "match_id": match_id,
        "prediction": prediction,
        "reasoning": reasoning,
        "modules_used": modules_used,
        "factors_detected": factors_detected,
        "confidence_score": confidence_score
    }
    if not os.path.exists(DECISION_JOURNAL_PATH):
        with open(DECISION_JOURNAL_PATH, "w") as f:
            json.dump([], f)
    with open(DECISION_JOURNAL_PATH, "r+") as f:
        data = json.load(f)
        data.append(entry)
        f.seek(0)
        json.dump(data, f, indent=2)
