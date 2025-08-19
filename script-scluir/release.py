import os
import shutil

IGNORE = [
    "dev",
    "scripts",
    "excluir",
    ".git",
    ".gitkeep",
    "Makefile",
    "bootstrap.css", 
]

new_folder = "release"

current_folder = os.path.dirname(os.path.abspath(__file__))
destination = os.path.join(current_folder, new_folder)

os.makedirs(destination, exist_ok=True)

script_name = os.path.basename(__file__)

for item in os.listdir(current_folder):
    if item == new_folder or item == script_name:
        continue

    if item in IGNORE:
        continue

    source_path = os.path.join(current_folder, item)
    destination_path = os.path.join(destination, item)

    if os.path.isfile(source_path):
        shutil.copy2(source_path, destination_path)
        print(f"File copied: {item}")
    elif os.path.isdir(source_path):
        shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
        print(f"Folder copied: {item}")

print("\n✅ Copy completed!")
