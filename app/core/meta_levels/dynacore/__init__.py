# Initialisation du module méta dynacore
class Dynacore:
    def __init__(self):
        self.ready = False

    def initialize(self):
        print('[META] dynacore initialisé.')
        self.ready = True
