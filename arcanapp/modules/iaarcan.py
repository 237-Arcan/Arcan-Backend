import json
from pathlib import Path
from typing import Dict, List


class IAArcan:
    def __init__(self, config_path: str = "./ia_arcan/config.json"):
        self.modules = {}
        self.memory = {
            "short_term": [],
            "mid_term": [],
            "long_term": [],
        }
        self.active_context = {}
        self.load_config(config_path)

    def load_config(self, path):
        with open(path, "r") as f:
            config = json.load(f)
            self.modules = config.get("modules", {})
            self.interfaces = config.get("interfaces", {})

    def update_memory(self, data: Dict, term: str):
        if term in self.memory:
            self.memory[term].append(data)

    def evaluate_modules(self, context: Dict):
        evaluated = {}
        self.active_context.update(context)  # Mémorisation dynamique du dernier contexte
        for name, module in self.modules.items():
            if context.get("competition") in module.get("contexts", []):
                score = self.score_module(name, context)
                evaluated[name] = score
        return evaluated

    def score_module(self, name: str, context: Dict) -> float:
        perf = context.get("performance", {}).get(name, 1.0)
        climate = 0.5 if context.get("climate") == "rainy" else 1.0
        return perf * climate

    def anticipate(self, current_signals: Dict):
        activated = []
        for name, module in self.modules.items():
            if module.get("dormant") and module.get("trigger") in current_signals:
                activated.append(name)
        if activated:
            self.active_context["triggered_modules"] = activated  # Journalisation des modules déclenchés
        return activated
