import os
import shutil
import time

downloads_folder = os.path.expanduser("~/Downloads")
toDelete_folder = os.path.expanduser("~/Downloads/toDelete")
spaceSaving = 0


def check_file(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False


if not os.path.exists(toDelete_folder):
    os.makedirs(toDelete_folder)

for filename in os.listdir(downloads_folder):
    if check_file(os.path.join(toDelete_folder, filename)) is False:
        print(f"{filename} already exists in {toDelete_folder}")
        file_path = os.path.join(downloads_folder, filename)
        if os.path.isfile(file_path):
            if (time.time() - os.path.getmtime(file_path)) \
                    > (10 * 24 * 60 * 60):
                fileSize = os.path.getsize(file_path)
                spaceSaving += fileSize
                shutil.move(file_path, toDelete_folder)
                print(f"{filename} has been moved to {toDelete_folder}")

print(f"Total potential space saving: {spaceSaving}")
