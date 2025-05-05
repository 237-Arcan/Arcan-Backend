# Exemple d'initialisation
memory = TemporalMemory(max_history=50)

# Extraction de données temporelles
match_data = {"team_a_score": 2, "team_b_score": 1, "time_elapsed": 90}
temporal_data = memory.extract(match_data)
print(temporal_data)  # {'team_a_last_score': 2, 'team_b_last_score': 1, 'time_elapsed': 90}

# Mise à jour de la mémoire
context = {"stats": match_data, "astro": {}, "odds": {}}
decision = {"action": "bet", "team": "Team A"}
memory.update(context, decision)

# Récupération de l'historique
history = memory.get_history()
print(history)

