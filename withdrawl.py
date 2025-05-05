import os

def concatenate_files(directory, output_file):
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f"\n\n--- {file_path} ---\n\n")
                        outfile.write(infile.read())
                except Exception as e:
                    print(f"Impossible de lire {file_path}: {e}")

# Utilisation
concatenate_files('  /storage/emulated/0/Download/arcanbackend', 'Arcan-Backend.txt')
