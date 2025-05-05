from arcanapp.modes import prediction_mode, live_analysis_mode, statistic_mode
from arcanapp.core.logger import setup_logger

logger = setup_logger()

class Orchestrator:
    def run_prediction_mode(self):
        logger.info("Lancement du mode prédiction...")
        prediction_mode.start()

    def run_live_analysis_mode(self):
        logger.info("Lancement du mode analyse live...")
        live_analysis_mode.start()

    def run_statistic_mode(self):
        logger.info("Lancement du mode statistiques...")
        statistic_mode.start()
