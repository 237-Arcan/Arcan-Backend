import unittest
from modules.tarot_bridge import TarotBridge

class TestTarotBridge(unittest.TestCase):
    def setUp(self):
        # Initialisation de l'objet TarotBridge
        self.tb = TarotBridge()
        # Vérification que la méthode prepare_draw existe et est appelée correctement
        if hasattr(self.tb, 'prepare_draw') and callable(getattr(self.tb, 'prepare_draw')):
            self.tb.prepare_draw({
                "major_arcana": [
                    {"card": "The Fool", "minute": 10},
                    {"card": "The Tower", "minute": 60}
                ]
            })
        else:
            raise AttributeError("La méthode 'prepare_draw' est introuvable dans la classe TarotBridge.")

    def test_draw_trigger(self):
        # Vérification que la méthode evaluate_draw existe
        if hasattr(self.tb, 'evaluate_draw') and callable(getattr(self.tb, 'evaluate_draw')):
            self.tb.evaluate_draw(10)
            # Vérification que l'attribut last_draw existe
            self.assertTrue(hasattr(self.tb, 'last_draw'), "L'attribut 'last_draw' est introuvable dans la classe TarotBridge.")
            self.assertIsNotNone(self.tb.last_draw, "Aucun tirage n'a été effectué.")
            self.assertEqual(self.tb.last_draw["card"], "The Fool", "La carte tirée ne correspond pas à 'The Fool'.")
        else:
            raise AttributeError("La méthode 'evaluate_draw' est introuvable dans la classe TarotBridge.")

    def test_no_draw(self):
        # Vérification que la méthode evaluate_draw existe
        if hasattr(self.tb, 'evaluate_draw') and callable(getattr(self.tb, 'evaluate_draw')):
            self.tb.evaluate_draw(20)
            # Vérification que l'attribut last_draw existe
            self.assertTrue(hasattr(self.tb, 'last_draw'), "L'attribut 'last_draw' est introuvable dans la classe TarotBridge.")
            self.assertIsNone(self.tb.last_draw, "Un tirage a été effectué alors qu'il ne devrait pas.")
        else:
            raise AttributeError("La méthode 'evaluate_draw' est introuvable dans la classe TarotBridge.")

if __name__ == '__main__':
    unittest.main()
