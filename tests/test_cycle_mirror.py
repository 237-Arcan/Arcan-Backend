import unittest
from modules.cycle_mirror import CycleMirror

class TestCycleMirror(unittest.TestCase):
    def setUp(self):
        """Initialise l'objet CycleMirror et charge un historique."""
        self.mirror = CycleMirror()
        self.mirror.load_history([
            {"team_a": "TeamX", "team_b": "TeamY", "score": "1-1"},
            {"team_a": "TeamY", "team_b": "TeamX", "score": "2-2"}
        ])

    def test_detect_cycles(self):
        """Teste la détection des cycles avec une correspondance."""
        match_state = {"team_a": "TeamX", "team_b": "TeamY", "score": "1-1"}
        echoes = self.mirror.scan(match_state)

        self.assertGreater(len(echoes), 0, "Aucun cycle détecté.")
        for echo in echoes:
            self.assertIn("score_similarity", echo)
            self.assertGreaterEqual(echo["score_similarity"], 0.5)

    def test_no_cycles_detected(self):
        """Teste le cas où aucun cycle n'est détecté."""
        match_state = {"team_a": "TeamA", "team_b": "TeamB", "score": "0-0"}
        echoes = self.mirror.scan(match_state)

        self.assertEqual(len(echoes), 0, "Des cycles ont été détectés alors qu'il ne devrait pas y en avoir.")

    def test_empty_history(self):
        """Teste la détection avec un historique vide."""
        self.mirror.load_history([])
        match_state = {"team_a": "TeamX", "team_b": "TeamY", "score": "1-1"}
        echoes = self.mirror.scan(match_state)

        self.assertEqual(len(echoes), 0, "Des cycles ont été détectés avec un historique vide.")

if __name__ == '__main__':
    unittest.main()
