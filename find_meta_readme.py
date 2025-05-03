import os

base_path = "app/core/modules"
targets = ["meta.json", "README.md"]

found_files = []

for root, dirs, files in os.walk(base_path):
    for file in files:
        if file in targets:
            rel_path = os.path.join(root, file)
            found_files.append(rel_path)

print("Fichiers trouvés :\n")
for path in found_files:
    print(path)
