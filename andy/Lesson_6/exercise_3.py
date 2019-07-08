"""
- Implement copy function which copying files into new location.
  Retrieve source_file_path, target_file_path.
  built in module for coping files should be used
"""


def copy_func(file_path, new_file_path):
    with open(file_path, 'rb') as file:
        with open(new_file_path, 'wb') as newfile:
            newfile.write(file.read())


TEXT1 = ["One", "Three", "Five", "Seven"]
with open("first_text", 'w+') as FIRST_FILE:
    FIRST_FILE.writelines(map(lambda x: x + '\n', TEXT1))
    FIRST_FILE.close()
copy_func("first_text", "newwww")
