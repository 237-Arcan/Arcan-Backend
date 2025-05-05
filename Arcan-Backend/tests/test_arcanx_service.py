import unittest
from arcan_core.arcanx.arcanx_service import ArcanXService

class TestArcanXService(unittest.TestCase):
    def setUp(self):
        self.service = ArcanXService()

    def test_run_analysis_exists(self):
        """Vérifie que la méthode run_analysis existe"""
        self.assertTrue(callable(getattr(self.service, "run_analysis", None)))

    def test_run_analysis_behavior(self):
        """Test comportement par défaut de run_analysis"""
        result = self.service.run_analysis(data={})
        self.assertIsNone(result)  # Par défaut, la méthode retourne None

if __name__ == '__main__':
    unittest.main()
