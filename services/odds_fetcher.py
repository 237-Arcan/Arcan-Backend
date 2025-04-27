import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ODDS_API_KEY")
BASE_URL = "https://api.the-odds-api.com/v4/sports/soccer_epl/odds"

def fetch_odds(region="uk", market="h2h"):
    params = {
        "apiKey": API_KEY,
        "regions": region,
        "markets": market,
        "oddsFormat": "decimal"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}
