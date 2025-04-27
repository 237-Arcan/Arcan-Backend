import os

# Liste des modules principaux et sous-modules
modules = {
    "arcan_shadow": [
        "ShadowOdds", "CollapseDetector", "ClutchTimeScanner", "CrowdPressureIndex",
        "LateSurgeDetector", "YouthImpactAnalyzer", "MomentumShiftTracker",
        "SetPieceThreatEvaluator", "FanSentimentMonitor", "CycleMirror", "ChronoEcho",
        "EasternGate", "CaptainSwitch", "MomentumShift"
    ],
    "arcan_sentinel": ["ShadowMomentum", "LineTrap", "KarmicFlow", "MirrorPhase", "BetPulse"],
    "arcan_forge": [],
    "arcan_brain": [],
    "arcan_x": [],
}

base_path = "app/core/modules"

def create_module_structure():
    for module, submods in modules.items():
        main_dir = os.path.join(base_path, module)
        os.makedirs(main_dir, exist_ok=True)
        with open(os.path.join(main_dir, "__init__.py"), "w") as f:
            f.write("def init():\n    print('Initialisation de {}')\n".format(module))

        for sub in submods:
            sub_dir = os.path.join(main_dir, sub.lower())
            os.makedirs(sub_dir, exist_ok=True)
            with open(os.path.join(sub_dir, "__init__.py"), "w") as f:
                f.write("def init():\n    print('Initialisation du module {}')\n".format(sub))

    print("[✓] Arborescence des modules Arcan générée avec succès.")

if __name__ == "__main__":
    create_module_structure()
