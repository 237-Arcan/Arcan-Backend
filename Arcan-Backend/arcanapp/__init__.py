"""
ArcanApp – Point central de l'application ArcanShadow.

Ce répertoire contient les modules principaux et les fonctionnalités
nécessaires pour l'exécution de l'application ArcanShadow, un moteur
hybride de prédictions pour les paris sportifs.

Modules inclus :
- `modules` : Contient les modules analytiques comme ArcanX, ShadowOdds, ChronoEcho, etc.
- `documentation` : Fournit les fichiers de documentation pour les interactions et les tests.
- `tests` : Contient les tests unitaires et d'intégration pour valider le comportement des modules.
- `core` : Gère les composants centraux comme ArcanBrain et ArcanForge.

Initialisation :
Ce fichier initialise les composants critiques et fournit une vue d'ensemble
des modules disponibles pour faciliter l'intégration et les tests.

Auteur : ArcanForge Team
Version : 1.0.0
"""

# Import des modules principaux
from .modules import shadow, live, supervision, ui
from .core import arcanbrain, arcanforge

__all__ = [
    "shadow",
    "live",
    "supervision",
    "ui",
    "arcanbrain",
    "arcanforge"
]

# Exemple de test d'initialisation
def initialize_app():
    """
    Initialise les composants critiques de l'application.
    """
    print("[ArcanApp] Initialisation des modules principaux...")
    arcanbrain.init()
    arcanforge.init()
