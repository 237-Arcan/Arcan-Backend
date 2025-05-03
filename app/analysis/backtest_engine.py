# app/analysis/backtest_engine.py

import json
import os
from collections import defaultdict
import statistics

DATA_FILE = "data/processed/all_tests.json"

def load_all_tests():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def compute_module_stats(data):
    modules_scores = defaultdict(list)
    durations = defaultdict(list)
    
    for item in data:
        scores = item.get("modules_scores", {})
        for module, module_data in scores.items():
            success = module_data.get("success", False)
            confidence = module_data.get("confidence", 0)
            runtime = module_data.get("runtime", 0)
            modules_scores[module].append((success, confidence))
            durations[module].append(runtime)
    
    for module in modules_scores:
        values = modules_scores[module]
        success_rate = sum(1 for s, _ in values if s) / len(values) * 100
        avg_conf = statistics.mean(c for _, c in values)
        avg_runtime = statistics.mean(durations[module])
        std_runtime = statistics.stdev(durations[module]) if len(durations[module]) > 1 else 0
        print(f"[{module}] Précision : {success_rate:.2f}%, Confiance : {avg_conf:.2f}, Durée : {avg_runtime:.3f}s (σ={std_runtime:.3f})")

if __name__ == "__main__":
    data = load_all_tests()
    compute_module_stats(data)
