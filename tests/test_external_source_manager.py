import unittest
from app.core.utils.external_source_manager import ExternalSourceManager

class TestExternalSourceManager(unittest.TestCase):
    def setUp(self):
        self.manager = ExternalSourceManager()

    def test_fetch_from_api(self):
        response = self.manager.fetch_from_api("https://jsonplaceholder.typicode.com/todos/1")
        self.assertIsNotNone(response)
        self.assertIn("title", response)

    def test_redis_integration(self):
        self.manager.store_in_redis("test_key", "test_value", expiry=10)
        value = self.manager.fetch_from_redis("test_key")
        self.assertEqual(value.decode(), "test_value")

    def test_websocket_listen(self):
        # Simule un test pour WebSocket (nécessite un serveur WebSocket pour être pleinement testé)
        self.assertTrue(callable(self.manager.listen_to_websocket))

if __name__ == "__main__":
    unittest.main()