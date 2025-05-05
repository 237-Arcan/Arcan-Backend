"""
ShadowOdds – Analyse du comportement des cotes et des volumes.

Fonctionnalités :
- Détection de line traps (favori surmisé sans chute de cote)
- Intégration avec Pinnacle, Betfair Exchange, Oddspedia
- Alerte sur anomalies de marché

Sous-modules :
- ShadowOdds+
"""
__all__ = ["detect_line_trap", "monitor_odds_volume", "ShadowOddsPlus"]
