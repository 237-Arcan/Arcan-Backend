class SimulationMode:
    def __init__(self, modules):
        self.modules = modules

    def run_simulation(self, historical_matches):
        """
        Exécute une simulation sur des matchs historiques.
        """
        results = []
        for match in historical_matches:
            match_result = {}
            for module_name, module in self.modules.items():
                if hasattr(module, "analyze"):
                    match_result[module_name] = module.analyze(match)
            results.append(match_result)
        return results
