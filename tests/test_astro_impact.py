import unittest
from modules.astro_impact import AstroImpact

class TestAstroImpact(unittest.TestCase):
    def test_planetary_hour(self):
        """Teste la méthode pour déterminer l'heure planétaire."""
        astro = AstroImpact()
        astro.evaluate_window(15)
        self.assertIn("planetary_hour", astro.last_influence)
        self.assertIsInstance(astro.last_influence["planetary_hour"], str)

    def test_sign_shift(self):
        """Teste la détection des changements de signe astrologique."""
        astro = AstroImpact()
        astro.set_cosmic_conditions({
            "sign_shifts": {"60": "Moon in Leo"},
            "aspects": []
        })
        astro.evaluate_window(60)
        self.assertEqual(astro.last_influence["sign_shift"], "Moon in Leo")

    def test_aspect_detection(self):
        """Teste la détection des aspects planétaires."""
        astro = AstroImpact()
        astro.set_cosmic_conditions({
            "sign_shifts": {},
            "aspects": [{"minute": 75, "aspect": "Sun trine Neptune"}]
        })
        astro.evaluate_window(75)
        self.assertEqual(len(astro.last_influence["aspects"]), 1)

if __name__ == '__main__':
    unittest.main()
