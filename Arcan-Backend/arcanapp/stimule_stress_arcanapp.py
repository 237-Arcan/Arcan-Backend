import time
import random
import threading
from datetime import datetime, timedelta

# === Simulation d'Anomalies Temporelles (Time Warper) ===
def simulate_time_anomalies():
    print("[TimeWarper] Simulation d'anomalies temporelles en cours...")
    base_time = datetime.now()
    
    for i in range(10):
        offset = random.choice([-60, -30, 0, 15, 120])  # secondes
        fake_time = base_time + timedelta(seconds=offset)
        print(f"[TimeWarper] Cycle {i+1}: temps simulé = {fake_time.strftime('%H:%M:%S')}")
        time.sleep(random.uniform(0.3, 0.7))

# === Simulation de Pics de Données en Temps Réel (Data Weaver) ===
def simulate_data_spikes():
    print("[DataWeaver] Simulation de pics de données...")
    for i in range(10):
        data_volume = random.randint(500, 10000)  # paquets simulés
        is_spike = data_volume > 8000
        print(f"[DataWeaver] Tick {i+1}: volume = {data_volume} unités {'[PIC]' if is_spike else ''}")
        time.sleep(random.uniform(0.2, 0.5))

# === Lancement parallèle des simulations ===
if __name__ == "__main__":
    print("=== Lancement de la simulation de résilience ArcanApp ===")

    t1 = threading.Thread(target=simulate_time_anomalies)
    t2 = threading.Thread(target=simulate_data_spikes)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("=== Simulation terminée. Vérifiez les logs des modules TimeWarper et DataWeaver ===")
