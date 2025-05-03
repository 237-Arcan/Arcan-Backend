# test_imports.py
from app.core.loader import ArcanLoader
from app.core.module_manager import ModuleManager  # À créer

def test():
    print(ArcanLoader.load_config())
    
if __name__ == '__main__':
    test()

