import os
from pathlib import Path

BASE_DIR = Path.cwd()
CRITICAL_MODULES = {
    "modules/live/sentinel": "ArcanSentinel",
    "modules/shadow/odds_analyzer": "ShadowOdds",
    "modules/meta/chrono_echo": "ChronoEcho"
}

UNIT_TESTS_DIR = BASE_DIR / "tests" / "unit"
INIT_TEMPLATE = '''"""
Module initialisé : {modname}
"""

__all__ = []  # À enrichir selon les composants du module
'''

def ensure_dir_and_init_py(module_path: Path):
    module_path.mkdir(parents=True, exist_ok=True)
    init_file = module_path / "__init__.py"
    if not init_file.exists() or init_file.stat().st_size == 0:
        with open(init_file, "w") as f:
            f.write(INIT_TEMPLATE.format(modname=module_path.name))

def generate_unit_test(module_path: Path, module_alias: str):
    import_path = str(module_path).replace("/", ".").replace(".py", "")
    test_filename = f"test_{module_path.name}.py"
    test_path = UNIT_TESTS_DIR / test_filename
    UNIT_TESTS_DIR.mkdir(parents=True, exist_ok=True)
    if not test_path.exists():
        with open(test_path, "w") as f:
            f.write(f'''import pytest
from {import_path} import *

def test_{module_alias.lower()}_core_behavior():
    # Placeholder test – à remplacer par des assertions réelles
    assert True

def test_{module_alias.lower()}_robustness():
    try:
        result = True  # À remplacer par appel de fonction critique
        assert result is not None
    except Exception as e:
        pytest.fail(f"{module_alias} crash détecté : " + str(e))
''')

def setup_test_environment():
    for rel_path, alias in CRITICAL_MODULES.items():
        module_path = BASE_DIR / rel_path
        ensure_dir_and_init_py(module_path)
        generate_unit_test(module_path, alias)

def main():
    setup_test_environment()
    print("[✔] Tous les modules, dossiers et tests critiques ont été générés avec succès.")

if __name__ == "__main__":
    main()
