# ShadowOdds Module

## Description
ShadowOdds est un module dédié à la **détection comportementale des cotes** et des **volumes de mises**. Son objectif principal est de repérer les anomalies entre les volumes de mises et les mouvements de cotes, permettant ainsi d'identifier les matchs pouvant être manipulés par les bookmakers.

---

## Fonction principale
> **Détection des anomalies dans les cotes et les volumes de mises.**

ShadowOdds analyse les données en provenance de diverses sources pour détecter des comportements suspects, tels que :
- Des cotes qui augmentent malgré une majorité de paris sur une équipe.
- Des déséquilibres importants entre l'argent placé et le mouvement des cotes.

---

## Principe fondateur
> *“Si la majorité parie sur une équipe et que sa cote reste stable ou augmente, méfie-toi.”*

---

## Fonctionnalités clés
- **Line Trap Scanner** : détecte les cotes "piège".
- **Volume Divergence Detector** : identifie les déséquilibres entre l'argent placé et le mouvement des lignes.
- **Bookie Resistance Sensor** : mesure la résistance des bookmakers face au flux des mises.

---

## Sources analysées
ShadowOdds s’appuie sur les données provenant des sources suivantes :
- [OddsPortal](https://www.oddsportal.com)
- [Betfair Exchange](https://www.betfair.com/exchange)
- [Pinnacle](https://www.pinnacle.com)
- [Oddspedia](https://www.oddspedia.com)

*Des intégrations supplémentaires sont possibles via API ou web scraping.*

---

## Niveau de confiance
- **Élevé en pré-match** : Les analyses effectuées avant le début des matchs sont robustes et fiables.
- **Critique en live** : Les analyses en direct sont particulièrement efficaces lorsqu'elles sont combinées avec d'autres modules comme `CrowdPressureIndex` et `MomentumTracker`.

---

## Couplages recommandés
Pour des performances optimales, ShadowOdds peut être utilisé avec :
1. **ArcanX** : Pour appliquer des filtres ésotériques.
2. **Eastern Gate** : Pour les matchs asiatiques.
3. **ChronoEcho** : Pour analyser les contextes historiques répétitifs.

---

## Intégration et Utilisation

### Installation
Assurez-vous que le module est activé par défaut dans votre instance d'ArcanShadow ou d'ArcanShadow-live.

### Exemple d'utilisation
Une fonction principale est définie dans `app/core/modules/arcan_shadow/shadowodds.py` :
```python
def shadow_odds_function():
    return "Shadow Odds Fonctionnement réussi!"
```

---

## Tests
Les tests unitaires pour ShadowOdds sont disponibles dans le fichier suivant :
- [`tests/test_shadowodds.py`](../../../../tests/test_shadowodds.py)

Pour exécuter les tests :
```bash
pytest tests/test_shadowodds.py
```

---

## Contributions
Pour proposer des améliorations ou signaler un problème, veuillez créer une issue ou une pull request dans le dépôt principal.

---

© 2025 ArcanShadow
