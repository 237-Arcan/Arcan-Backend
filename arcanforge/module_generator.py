import os
import json

class ModuleGenerator:
    """
    Classe pour générer dynamiquement des modules à partir de templates.
    """

    def __init__(self):
        self.templates = {
            "pattern_detector": "templates/pattern_detector.py.tpl",
            "karmic_predictor": "templates/karmic_predictor.py.tpl",
        }

    def generate_module(self, module_name: str, type_: str, logic: dict):
        """
        Génère un module Python et une fiche JSON associée.
        """
        if type_ not in self.templates:
            raise ValueError(f"Type de module inconnu : {type_}")

        # Charger le template Python
        template_path = self.templates[type_]
        with open(template_path, "r") as tpl_file:
            template_code = tpl_file.read()

        # Remplir le template avec les paramètres de logique
        filled_code = template_code.format(
            module_name=module_name,
            condition=logic["condition"],
            reaction=logic["reaction"]
        )

        # Sauvegarder le fichier .py
        module_file = f"generated/{module_name}.py"
        os.makedirs("generated", exist_ok=True)
        with open(module_file, "w") as mod_file:
            mod_file.write(filled_code)
        print(f"Module généré : {module_file}")

        # Générer le fichier JSON
        metadata = {
            "name": module_name,
            "origin": logic.get("origin", "Unknown"),
            "logic": logic,
            "dependencies": logic.get("dependencies", [])
        }
        json_file = f"generated/{module_name}.json"
        with open(json_file, "w") as json_out:
            json.dump(metadata, json_out, indent=4)
        print(f"Fiche JSON générée : {json_file}")

        return module_file, json_file
