# ARCHITECTURE.md

## Vue d'ensemble

Ce fichier décrit l’architecture fonctionnelle du backend ArcanShadow / ArcanX, structuré pour être extensible, modulaire et optimisé pour le traitement hybride (statistiques + ésotérisme + comportement des cotes).

---

## 1. Structure des dossiers

### `api/`
- Contient les **routes d'entrée** de l'API.
- Fait le lien entre les requêtes HTTP (ou websocket) et les appels aux modules ou aux niveaux méta.
- Endpoints clés :
  - `/arcanx/launch`
  - `/shadowodds/scan`
  - `/live/activate`
  - `/modules/status`

### `app/`
- **Cœur du système**, organise les appels métiers, les modules, les chargements dynamiques, et les niveaux logiques.
- Sous-dossiers principaux :
  
#### `app/core/modules/`
- Contient **tous les modules d’analyse**, regroupés par familles :
  - `arcan_shadow/` : modules statistiques + ésotériques.
  - `arcan_sentinel/` : modules live optimisés.
  - `meta_modules/` : modules spéciaux (ArcanForge, ArcanSentinel, etc.).
  
#### `app/core/manager.py`
- Gère la **sélection, l’activation et l'exécution dynamique** des modules en fonction du contexte.

#### `app/core/loader.py`
- Permet le **chargement dynamique** des modules selon les requêtes API ou les appels internes.

#### `app/levels/`
- Contient la **logique des niveaux d’intelligence** : ArcanX (stat/stat+ésotérisme), ArcanShadow (stat+ésotérisme+cotes), ArcanSentinel (live).

---

## 2. Schéma de traitement typique (exemple : appel à ArcanShadow)

```text
[API Request]
    |
    v
[/api/arcan_shadow/launch]
    |
    v
[app/core/manager.py]
    |
    v
[app/core/loader.py] ----> Charge les modules nécessaires :
    |                           - ShadowOdds
    |                           - ChronoEcho
    |                           - ClutchTimeScanner
    |                           - etc.
    v
[Exécution des modules]
    |
    v
[Résultat consolidé (json)]
    |
    v
[Réponse à l’API]
