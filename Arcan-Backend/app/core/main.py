from fastapi import APIRouter, HTTPException
from app.modules.arcan_archive_trigger import ArchiveTriggerSystem

router = APIRouter()
archive_trigger = ArchiveTriggerSystem()  # Instanciation unique

@router.post("/predict")
async def predict_handler(request_data: dict):
    try:
        # --- Étape 1 : Ton système de prédiction génère une prédiction ---
        prediction_result = ton_module_de_prediction(request_data)

        # --- Étape 2 : Déclenche l’incrémentation du compteur ---
        archive_trigger.handle_new_prediction(data=prediction_result)

        return {"prediction": prediction_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# api/arcanx.py
from app.core.arcan_loader import TriggerRule
from app.core.match_downloader import MatchDownloader

trigger = TriggerRule()
downloader = MatchDownloader()

def handle_new_prediction(data):
    trigger.increment_prediction()

    if trigger.should_trigger_download():
        print("Seuil atteint : téléchargement des archives")
        downloader.download_archives()

from modules.infrastructure.arcan_archive import archive_downloader

if arcanx.prediction_count >= 5:
    archive_downloader.trigger_archive_fetch()

count = increment_user_prediction(user_id)
if count == 5:
    from app.core.loader import download_archived_matches
    download_archived_matches(user_id)
