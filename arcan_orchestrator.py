#!/usr/bin/env python3
# arcan_orchestrator.py - Système central de gestion Arcan-Backend

import importlib
import inspect
import json
import logging
from pathlib import Path
import sys
from typing import Dict, List
import yaml

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/arcan_backend.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('ArcanOrchestrator')

class ArcanBackend:
    """Classe principale gérant l'orchestration de tous les modules"""
    
    def __init__(self, config_path: str = 'config/settings.yaml'):
        self.root_dir = Path(__file__).parent.resolve()
        self.config = self._load_config(config_path)
        self.modules: Dict[str, object] = {}
        self._init_core()
        self._init_modules()

    def _load_config(self, config_path: str) -> dict:
        try:
            with open(config_path) as f:
                return yaml.safe_load(f)
        except Exception as e:
            logger.error(f"Erreur chargement config: {e}")
            raise

    def _init_core(self):
        core_modules = [
            'app.core.orchestrator',
            'app.core.predictive_engine',
            'app.core.realtime_dashboard',
            'app.core.module_manager'
        ]
        for module_path in core_modules:
            try:
                module = importlib.import_module(module_path)
                class_name = module_path.split('.')[-1].title().replace('_', '')
                self.modules[class_name] = getattr(module, class_name)()
                logger.info(f"Module core {class_name} chargé")
            except Exception as e:
                logger.error(f"Erreur chargement {module_path}: {e}")

    def _init_modules(self):
        modules_dir = self.root_dir / 'app' / 'modules'
        for module_type in ['arcanx', 'shadow', 'live', 'meta']:
            module_path = modules_dir / module_type
            if not module_path.exists():
                continue
            for module_file in module_path.glob('**/*.py'):
                if module_file.name.startswith('_') or not self._should_load_module(module_file):
                    continue
                try:
                    module_name = f"app.modules.{module_type}.{module_file.stem}"
                    module = importlib.import_module(module_name)
                    for name, obj in inspect.getmembers(module):
                        if inspect.isclass(obj) and name.endswith('Analyzer'):
                            self.modules[name] = obj(self.config)
                            logger.info(f"Module {name} chargé depuis {module_file}")
                except Exception as e:
                    logger.error(f"Erreur chargement {module_file}: {e}")

    def _should_load_module(self, module_file: Path) -> bool:
        meta_file = module_file.parent / 'meta.json'
        if not meta_file.exists():
            return True
        try:
            with open(meta_file) as f:
                meta = json.load(f)
                return meta.get('enabled', True)
        except Exception:
            return True

    def run_pipeline(self, mode: str = 'full'):
        try:
            orchestrator = self.modules.get('Orchestrator')
            data = {}
            if mode in ['full', 'stats']:
                data.update(self._load_stats_data())
            if mode in ['full', 'live']:
                data.update(self._load_live_data())

            results = {}
            for name, module in self.modules.items():
                if hasattr(module, 'analyze'):
                    results[name] = module.analyze(data)

            if 'DGridSync' in self.modules:
                final_output = self.modules['DGridSync'].sync(results)
            else:
                final_output = results

            self._generate_output(final_output, mode)
            return final_output
        except Exception as e:
            logger.error(f"Erreur pipeline: {e}")
            raise

    def _load_stats_data(self) -> dict:
        data_service = self.modules.get('DataService')
        if data_service:
            return data_service.get_stats()
        return {}

    def _load_live_data(self) -> dict:
        live_service = self.modules.get('LiveService')
        if live_service:
            return live_service.get_live_data()
        return {}

    def _generate_output(self, results: dict, mode: str):
        output_dir = self.root_dir / 'output'
        output_dir.mkdir(exist_ok=True)
        with open(output_dir / f'results_{mode}.json', 'w') as f:
            json.dump(results, f, indent=2)
        if 'RealtimeDashboard' in self.modules:
            self.modules['RealtimeDashboard'].update(results)

if __name__ == '__main__':
    try:
        logger.info("Démarrage Arcan-Backend")
        arcan = ArcanBackend()
        modes = {'1': 'full', '2': 'stats', '3': 'live'}
        print("Sélectionnez un mode:")
        for key, value in modes.items():
            print(f"{key}. {value}")
        choice = input("Votre choix: ")
        selected_mode = modes.get(choice, 'full')
        results = arcan.run_pipeline(selected_mode)
        logger.info("Pipeline terminé. Résultats sauvegardés.")
    except Exception as e:
        logger.critical(f"Erreur critique: {e}")
        sys.exit(1)

