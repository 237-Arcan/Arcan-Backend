# Initialisation du module méta arcanreflex
class Arcanreflex:
    def __init__(self):
        self.ready = False

    def initialize(self):
        print('[META] arcanreflex initialisé.')
        self.ready = True

from app.core.logger import setup_logger

logger = setup_logger("ArcanReflexLogger")

def detect_anomalies(self, events: List[Dict]) -> List[Dict]:
    logger.info(f"Détection des anomalies dans les événements : {events}")
    anomalies = []
    for event in events:
        if event.get("minute") >= 90 or event.get("type") in ["red_card", "own_goal"]:
            anomalies.append(event)
            logger.warning(f"Anomalie détectée : {event}")
    return anomalies
