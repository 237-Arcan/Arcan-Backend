import unittest
from modules.arcan_reflex import ArcanReflex

class TestArcanReflex(unittest.TestCase):
    def setUp(self):
        # Initialisation d'une instance d'ArcanReflex pour chaque test
        self.ar = ArcanReflex()

    def test_blockage_detection(self):
        """
        Vérifie que le système détecte correctement un blocage énergétique
        lorsque la domination est vraie et qu'aucun but n'est marqué.
        """
        result = self.ar.evaluate({"domination": True, "goals_scored": 0, "minute": 15})
        self.assertEqual(len(result), 1, "Le nombre de corrections détectées devrait être 1.")
        self.assertEqual(result[0]["type"], "blockage", "Le type de correction devrait être 'blockage'.")
        self.assertEqual(result[0]["minute"], 15, "La minute de la correction devrait être 15.")

    def test_karmic_loop(self):
        """
        Vérifie que le système détecte correctement une répétition karmique
        lorsque l'intensité d'un événement récurrent est suffisante.
        """
        karmic_events = [{"type": "repeat", "event": "But 32e", "intensity": 2}]
        result = self.ar.evaluate({"minute": 32}, karmic_events=karmic_events)
        self.assertEqual(len(result), 1, "Le nombre de corrections détectées devrait être 1.")
        self.assertEqual(result[0]["type"], "karmic_loop", "Le type de correction devrait être 'karmic_loop'.")
        self.assertIn("Répétition karmique", result[0]["label"], "Le label devrait mentionner 'Répétition karmique'.")
        self.assertEqual(result[0]["minute"], 32, "La minute de la correction devrait être 32.")

    def test_no_trigger(self):
        """
        Vérifie qu'aucune correction n'est déclenchée lorsque les conditions
        pour un blocage ou une répétition karmique ne sont pas remplies.
        """
        result = self.ar.evaluate({"domination": False, "goals_scored": 1})
        self.assertEqual(result, [], "Aucune correction ne devrait être détectée.")

    def test_empty_karmic_events(self):
        """
        Vérifie le comportement du système avec une liste vide d'événements karmiques.
        """
        result = self.ar.evaluate({"minute": 45}, karmic_events=[])
        self.assertEqual(result, [], "Aucune correction ne devrait être détectée avec des karmic_events vides.")

    def test_missing_keys(self):
        """
        Vérifie que le système gère correctement les entrées incomplètes.
        """
        with self.assertRaises(KeyError, msg="Une KeyError devrait être levée si une clé essentielle est manquante."):
            self.ar.evaluate({"goals_scored": 0})  # Clé 'domination' manquante

if __name__ == "__main__":
    unittest.main()
