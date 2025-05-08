from arcanforge.module_generator import ModuleGenerator

# Définir la logique du module
logic = {
    "condition": "data['minute'] > 80 and data['momentum'] < 0",
    "reaction": "'Possible late equalizer'",
    "origin": "ShadowOdds",
    "dependencies": ["match_state", "volume_fluctuations"]
}

# Générer le module
generator = ModuleGenerator()
generator.generate_module("LateGoalPredictor", "pattern_detector", logic)
