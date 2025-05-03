# app/core/match_downloader.py
import os
import requests

class MatchDownloader:
    def __init__(self, github_repo="arcan-datasets/match-archives", target_dir="data/matches"):
        self.repo = github_repo
        self.target_dir = target_dir
        self.api_url = f"https://api.github.com/repos/{self.repo}/contents"

    def download_archives(self):
        os.makedirs(self.target_dir, exist_ok=True)
        files = self._list_files()
        for file in files:
            self._download_file(file)

    def _list_files(self):
        res = requests.get(self.api_url)
        if res.status_code == 200:
            return [f["download_url"] for f in res.json() if f["name"].endswith(".json")]
        else:
            return []

    def _download_file(self, url):
        local_filename = os.path.join(self.target_dir, os.path.basename(url))
        with requests.get(url, stream=True) as r:
            with open(local_filename, 'wb') as f:
                f.write(r.content)
