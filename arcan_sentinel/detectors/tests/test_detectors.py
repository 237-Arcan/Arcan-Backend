import unittest
from arcan_sentinel.detectors import (
    LineTrapDetector,
    RhythmBreakDetector,
    StatAnomalyDetector,
    NarrativeLoopDetector,
    EgregoreSurgeScanner,
    MomentumCollapseSensor,
)


class TestDetectors(unittest.TestCase):
    def setUp(self):
        """
        Initialisation des détecteurs avant chaque test.
        """
        self.line_trap_detector = LineTrapDetector()
        self.rhythm_break_detector = RhythmBreakDetector()
        self.stat_anomaly_detector = StatAnomalyDetector()
        self.narrative_loop_detector = NarrativeLoopDetector()
        self.egregore_surge_scanner = EgregoreSurgeScanner()
        self.momentum_collapse_sensor = MomentumCollapseSensor()

    def test_line_trap_detector(self):
        context = {
            "odds": {"team_a": 1.5, "team_b": 2.5},
            "volumes": {"team_a": 0.8, "team_b": 0.4},
        }
        deltas = {}
        result = self.line_trap_detector.detect(deltas, context)
        self.assertIsNotNone(result)
        self.assertEqual(result["type"], "line_trap")
        self.assertEqual(result["team"], "team_a")

    def test_rhythm_break_detector(self):
        context = {
            "events": [
                {"minute": 10, "type": "foul"},
                {"minute": 11, "type": "goal"},
                {"minute": 12, "type": "corner"},
            ],
            "minute": 15,
        }
        deltas = {}
        result = self.rhythm_break_detector.detect(deltas, context)
        self.assertIsNotNone(result)
        self.assertEqual(result["type"], "rhythm_break")
        self.assertEqual(len(result["recent_events"]), 3)

    def test_stat_anomaly_detector(self):
        context = {
            "live_stats": {
                "shots": 12,
                "xG": 0.4,
            }
        }
        deltas = {}
        result = self.stat_anomaly_detector.detect(deltas, context)
        self.assertIsNotNone(result)
        self.assertEqual(result["type"], "anomaly")
        self.assertIn("High shot count with low xG", result["detail"])

    def test_narrative_loop_detector(self):
        context = {
            "historical": [
                {"match_id": "001", "score": "1-1"},
                {"match_id": "002", "score": "2-2"},
            ],
            "score": "1-1",
            "match_id": "003",
        }
        deltas = {}
        result = self.narrative_loop_detector.detect(deltas, context)
        self.assertIsNotNone(result)
        self.assertEqual(result["type"], "narrative_loop")
        self.assertEqual(result["match_reference"]["match_id"], "001")

    def test_egregore_surge_scanner(self):
        context = {
            "crowd_reaction": {
                "volume_db": 98,
                "chant": True,
            }
        }
        deltas = {}
        result = self.egregore_surge_scanner.detect(deltas, context)
        self.assertIsNotNone(result)
        self.assertEqual(result["type"], "egregore_surge")
        self.assertTrue(result["chant"])

    def test_momentum_collapse_sensor(self):
        context = {
            "momentum": [-0.5, -0.6, -0.7, -0.8, -0.9],
        }
        deltas = {}
        result = self.momentum_collapse_sensor.detect(deltas, context)
        self.assertIsNotNone(result)
        self.assertEqual(result["type"], "momentum_collapse")
        self.assertGreater(result["volatility"], 0)


if __name__ == "__main__":
    unittest.main()
