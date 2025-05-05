import json
from .modules
import NeuroArcan, AnomalicRadar, KarmicSensor

class ArcanReflex:
    def __init__(self, config_path="config/arcan_reflex_config.json"):
        self.modules = {}
        self.load_config(config_path)

    def load_config(self, path):
        with open(path, "r") as config_file:
            config = json.load(config_file)
            self.modules = {
                "neuro_arcan": NeuroArcan(config["neuro_arcan"]),
                "anomalic_radar": AnomalicRadar(config["anomalic_radar"]),
                "karmic_sensor": KarmicSensor(config["karmic_sensor"])
            }
