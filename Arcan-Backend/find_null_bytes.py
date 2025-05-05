import os

def find_null_bytes_in_files(directory):
    # Liste tous les fichiers dans le répertoire donné
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            try:
                with open(file_path, 'rb') as f:
                    # Lire le fichier en mode binaire
                    content = f.read()
                    # Vérifier si des octets nuls sont présents
                    if b'\x00' in content:
                        print(f"Fichier avec octets nuls trouvé : {file_path}")
            except Exception as e:
                print(f"Erreur lors de l'ouverture du fichier {file_path}: {e}")

# Remplacer '/data/user/0/ru.iiec.pydroid3/files/accomp_files/arcan-backend' par le chemin de ton répertoire
find_null_bytes_in_files('/data/user/0/ru.iiec.pydroid3/files/accomp_files/arcan-backend')
