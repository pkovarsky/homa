"""
- Implement function which copying only uniq lines from one file two other.
  Retrieve source_file_path, target_file_path, returns number of lines copied.
"""
import os

TEXT = ["Donetsk", "Kharkov", "Kiev", "Kharkov", "Donbass", "Lvov", "Kiev",
        "Lvov", "Dnepr", "Dnepr"]
with open("input_data", 'w+') as INPUT_FILE:
    INPUT_FILE.writelines(map(lambda x: x + '\n', TEXT))
    INPUT_FILE.seek(0)
    FILE_LINES = INPUT_FILE.readlines()
with open("unique_lines", 'w+') as UNIQUE_FILE:
    for i in FILE_LINES:
        UNIQUE_FILE.seek(0)
        UNIQUE_LINES = UNIQUE_FILE.readlines()
        if i not in UNIQUE_LINES:
            UNIQUE_FILE.writelines(i)
    UNIQUE_FILE.seek(0)
    print(UNIQUE_FILE.readlines())
    UNIQUE_FILE.seek(0)
    print("Number of lines copied: ", len(UNIQUE_FILE.readlines()))
    print("Source file path:", os.listdir())
    print("Target file path:", os.getcwd())
