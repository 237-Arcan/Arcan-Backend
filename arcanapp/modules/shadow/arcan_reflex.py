import datetime
import uuid
from typing import List, Dict


class ArcanReflex:
    def __init__(self):
        self.log = []

    def compare_prediction_vs_reality(self, prediction: Dict, reality: Dict) -> Dict:
        mismatch = {}
        for key in prediction:
            if prediction[key] != reality.get(key):
                mismatch[key] = (prediction[key], reality.get(key))
        return mismatch

    def detect_anomalies(self, events: List[Dict]) -> List[Dict]:
        anomalies = []
        for event in events:
            if event.get("minute") >= 90 or event.get("type") in ["red_card", "own_goal"]:
                anomalies.append(event)
        return anomalies

    def log_error(self, issue: str, details: Dict):
        timestamp = datetime.datetime.now().isoformat()
        log_entry = {
            "id": str(uuid.uuid4()),
            "time": timestamp,
            "issue": issue,
            "details": details,
        }
        self.log.append(log_entry)

    def get_reflex_report(self) -> List[Dict]:
        return self.log
