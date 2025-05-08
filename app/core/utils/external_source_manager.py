import requests
import redis
from websocket import create_connection

class ExternalSourceManager:
    """
    Gère les interactions avec des sources externes (API, bases de données, WebSockets).
    """

    def __init__(self):
        self.redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

    def fetch_from_api(self, url, params=None):
        """
        Effectue un appel API GET et retourne les données.
        :param url: URL de l'API.
        :param params: Paramètres de la requête.
        :return: Réponse JSON de l'API.
        """
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de l'appel API : {e}")
            return None

    def listen_to_websocket(self, ws_url):
        """
        Écoute un flux WebSocket.
        :param ws_url: URL du WebSocket.
        :return: Messages reçus en temps réel.
        """
        try:
            ws = create_connection(ws_url)
            while True:
                message = ws.recv()
                yield message
        except Exception as e:
            print(f"Erreur WebSocket : {e}")

    def fetch_from_redis(self, key):
        """
        Récupère une valeur depuis Redis.
        :param key: Clé Redis.
        :return: Valeur stockée.
        """
        try:
            return self.redis_client.get(key)
        except redis.RedisError as e:
            print(f"Erreur Redis : {e}")
            return None

    def store_in_redis(self, key, value, expiry=None):
        """
        Stocke une valeur dans Redis.
        :param key: Clé Redis.
        :param value: Valeur à stocker.
        :param expiry: Durée d'expiration en secondes.
        """
        try:
            self.redis_client.set(key, value, ex=expiry)
        except redis.RedisError as e:
            print(f"Erreur Redis : {e}")