import os
import shutil

# Imported for convenience
from collections import namedtuple

# Main function, so this can act like a script
if __name__ == '__main__':
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))  # Root directory

    file_change_times_dest = []  # List of files from destination folder
    file_change_times_src = []  # List of files from source folder

    # Nameed tuple to ease writing code
    FileInformation = namedtuple('FileInformation', ['file_path', 'file_name', 'last_modified'])

    # Loop through files in destination folder to collect information
    for dirpath, dirs, files in os.walk(os.path.join(ROOT_DIR, 'dest')):
        for file in files:
            # getting file path
            file_path = os.path.join(dirpath, file)
            # getting file change info and casting it to FileInformation type
            file_change_times_dest.append(FileInformation(file_path, file, os.stat(file_path).st_mtime))

    # Loop through source folder, same logic
    for dirpath, dirs, files in os.walk(os.path.join(ROOT_DIR, 'src')):
        for file in files:
            file_path = os.path.join(dirpath, file)
            file_change_times_src.append(FileInformation(file_path, file,os.stat(file_path).st_mtime))

    # Comparing the two, using Zip to combine the two lists into a tuple
    for file_comp in zip(file_change_times_dest, file_change_times_src):

        # Settings variables for 0 and 1 to make writing code easier
        _DEST = 0
        _SRC = 1

        # File comparison, to see if file name is the same, since we want to update
        if file_comp[_SRC].file_name == file_comp[_DEST].file_name:
            # If the last modified is greater for source, then we copy
            if file_comp[_SRC].last_modified > file_comp[_DEST].last_modified:
                shutil.copy(file_comp[_SRC].file_path, file_comp[_DEST].file_path)
                print("File moved")  # Just for checking