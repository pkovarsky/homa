"""
- Implement get_dir_info function which return directory info (files info, etc.)
  Retrieve dir_path.
  Return dir info object (any data type). (files and their sizes)
"""
import os
import genericpath


def get_dir_info():
    currentdir = os.getcwd()
    print("Retrieve dir_path: ", currentdir)
    dirobject = os.listdir(currentdir)
    print("Objects at current dir:", dirobject)
    for i in dirobject:
        print("File name: ", i)
        print("Byte size: ", genericpath.getsize(i))


get_dir_info()
