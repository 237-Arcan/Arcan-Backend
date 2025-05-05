import os

# Structure avec description de chaque dossier
doc_map = {
    "app": "# ArcanApp\nContient l’architecture logique de l’application et les couches d’analyse.",
    "app/core": "# Core\nModules centraux de traitement : prédiction, orchestration et dashboard en live.",
    "app/meta_levels": "# Meta Levels\nNiveaux d'analyse avancés temporels et de répartition parallèle.",
    "app/meta_levels/time_warper": "# Time Warper\nGestion des anomalies temporelles, cycles cachés, récurrences narratives.",
    "app/meta_levels/data_weaver": "# Data Weaver\nModule de tissage des données : dispatch distribué, synchronisation parallèle.",
    "modules": "# Modules\nModules analytiques organisés par spécialisation (ArcanX, Shadow, Live).",
    "modules/arcanx": "# ArcanX\nModules ésotériques : gematria, astrologie, numérologie, kabbale, symbolique.",
    "modules/shadow": "# Shadow\nModules d’analyse comportementale, manipulation des cotes, signaux hybrides.",
    "modules/live": "# ArcanSentinel/Live\nVersion allégée en direct, adaptée aux pics et instabilités live.",
    "modes": "# Modes\nContient les scripts de lancement des trois modes : prédiction, live, statistique.",
}

def create_readme(path, content):
    full_path = os.path.join(path, "README.md")
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[✓] README créé : {full_path}")

def main():
    base_dir = os.getcwd()
    for rel_path, doc_content in doc_map.items():
        abs_path = os.path.join(base_dir, rel_path)
        if os.path.isdir(abs_path):
            create_readme(abs_path, doc_content)
        else:
            print(f"[!] Dossier manquant, ignoré : {abs_path}")

if __name__ == "__main__":
    main()
