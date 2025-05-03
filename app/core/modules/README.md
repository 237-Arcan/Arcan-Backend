# Module ``

Ce module fait partie de l'infrastructure **ArcanX / ArcanShadow**.

- Type : statistical
- Compatible avec : shadow

## Fonctions attendues
- `on_prediction_request(context)`
- `on_live_event(event)`

# ArcanArchive

**Type** : Infrastructure / Téléchargement automatique  
**Statut** : Actif  
**Version** : 1.0.0  
**Déclencheur** : À partir de la 5e prédiction ArcanX  
**Créateur** : ArcanForge

---

## Description

`ArcanArchive` est un module infrastructurel destiné à enrichir la base de données de l'écosystème ArcanX. Il agit comme un **déclencheur automatique** qui télécharge les **archives de matchs historiques** dès que **5 prédictions** ont été réalisées dans le système.

Cela permet :

- L'entraînement futur de modèles internes (ChronoEcho, CycleMirror, KarmicFlow+).
- L’enrichissement du système ArcanBrain avec des cas archivés.
- L’exploitation par des modules esotérico-analytiques (gematria, répétitions, patterns karmiques, etc.).

---

## Fonctionnement

1. **Suivi du nombre de prédictions ArcanX** réalisées par l'utilisateur ou le système.
2. Une fois la 5e prédiction atteinte, un **appel API GitHub** est effectué.
3. Les **fichiers `.json`** de matchs archivés sont **téléchargés localement** dans `data/matches/`.

---

## Format attendu des archives

Chaque fichier JSON représente un match historique, avec au minimum les champs suivants :

```json
{
  "match_id": "FRA-L1-2022-PSG-OM",
  "date": "2022-04-17",
  "teams": ["PSG", "Marseille"],
  "score": "2-1",
  "goals": [
    {"minute": 12, "team": "PSG", "scorer": "Mbappé"},
    {"minute": 36, "team": "OM", "scorer": "Payet"},
    {"minute": 74, "team": "PSG", "scorer": "Messi"}
  ],
  "astrology": {...},
  "esoteric_keys": ["22", "Saturne", "Chokmah", "Lion", "Miroir"]
}
