import os
import requests

# === 1. Déclencheur de téléchargement basé sur le nombre de prédictions ===
class TriggerRule:
    def __init__(self, threshold=5):
        self.prediction_count = 0
        self.threshold = threshold

    def increment_prediction(self):
        self.prediction_count += 1
        print(f"[TriggerRule] Prédiction #{self.prediction_count}")
        return self.prediction_count

    def should_trigger_download(self):
        return self.prediction_count >= self.threshold

# === 2. Téléchargeur des archives depuis GitHub ===
class MatchDownloader:
    def __init__(self, github_repo="arcan-datasets/match-archives", target_dir="data/matches"):
        self.repo = github_repo
        self.target_dir = target_dir
        self.api_url = f"https://api.github.com/repos/{self.repo}/contents"

    def download_archives(self):
        os.makedirs(self.target_dir, exist_ok=True)
        files = self._list_files()
        if not files:
            print("[MatchDownloader] Aucune archive détectée.")
        for file_url in files:
            self._download_file(file_url)

    def _list_files(self):
        print("[MatchDownloader] Récupération de la liste des fichiers...")
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()
            return [f["download_url"] for f in response.json() if f["name"].endswith(".json")]
        except Exception as e:
            print(f"[MatchDownloader] Erreur lors de la récupération : {e}")
            return []

    def _download_file(self, url):
        filename = os.path.join(self.target_dir, os.path.basename(url))
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"[MatchDownloader] Téléchargé : {filename}")
        except Exception as e:
            print(f"[MatchDownloader] Échec du téléchargement de {url} : {e}")

# === 3. Intégration générale ===
class ArchiveTriggerSystem:
    def __init__(self):
        self.trigger = TriggerRule()
        self.downloader = MatchDownloader()

    def handle_new_prediction(self, data=None):
        self.trigger.increment_prediction()
        if self.trigger.should_trigger_download():
            print("[ArchiveTriggerSystem] Seuil atteint : téléchargement des archives lancé.")
            self.downloader.download_archives()
        else:
            print("[ArchiveTriggerSystem] Seuil non atteint.")

# === 4. Exemple d'utilisation ===
if __name__ == "__main__":
    system = ArchiveTriggerSystem()

    # Simule 6 prédictions consécutives
    for i in range(6):
        print(f"\n--- Simulation de prédiction {i + 1} ---")
        system.handle_new_prediction()
