class ArcanBrain:
    def __init__(self):
        self.modules = {}

    def register_module(self, name, module):
        self.modules[name] = module
        print(f"[ArcanBrain] Module {name} enregistré.")

    def execute(self, context):
        results = {}
        for name, module in self.modules.items():
            if hasattr(module, "analyze"):
                results[name] = module.analyze(context)
        return results
