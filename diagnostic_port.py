# diagnostic_port.py

import subprocess

def check_port(port=5000):
    print(f"--- Diagnostic du port {port} ---\n")
    
    try:
        # Liste des processus utilisant ce port
        result = subprocess.run(f"lsof -i :{port}", shell=True, text=True, capture_output=True)
        if result.stdout:
            print("Processus détectés sur le port :")
            print(result.stdout)
        else:
            print("Aucun processus n'utilise ce port.")
        
        # Vérification si le port est vraiment occupé
        check = subprocess.run(f"ss -ltnp | grep :{port}", shell=True, text=True, capture_output=True)
        if check.stdout:
            print("\nDétail supplémentaire avec ss :")
            print(check.stdout)
        else:
            print("\nPas de connexion active détectée sur ce port.")

    except Exception as e:
        print(f"Erreur lors du diagnostic : {e}")

if __name__ == "__main__":
    check_port()
