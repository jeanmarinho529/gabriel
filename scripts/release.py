import os
import shutil

def new_release(current_folder: str, ignore: list = [], new_folder: str = "release"):
    # current_folder = os.path.dirname(os.path.abspath(__file__))
    destination = os.path.join(current_folder, new_folder)

    os.makedirs(destination, exist_ok=True)

    script_name = os.path.basename(__file__)

    for item in os.listdir(current_folder):
        if item == new_folder or item == script_name:
            continue

        if item in ignore:
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

def delete_files(path: str, file_folder: str, delete_files: list):
    for file in delete_files:
        file_path = path + "/" + file_folder + "/" + file
        if os.path.exists(file_path):
            os.remove(file_path)