import unittest
from app.core.modules.arcan_shadow.chronoecho import ChronoEcho

class TestChronoEcho(unittest.TestCase):
    def setUp(self):
        self.module = ChronoEcho()

    def test_prediction_output(self):
        context = {"match_id": "FRA-L1-2022-PSG-OM", "historical_data": [...]}
        result = self.module.on_prediction_request(context)
        self.assertIn("score", result)
        self.assertGreaterEqual(len(result["score"]), 1)

if __name__ == "__main__":
    unittest.main()
