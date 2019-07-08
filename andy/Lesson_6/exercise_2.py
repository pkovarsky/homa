"""
- Implement function which merge two files line by line into one new file.
  Empty lines should be skipped optionally (use default fn parameter).
  Retrieve source_file_path1, source_file_path2, target_file_path, skip_empty(default True).
"""
import os


def merge_func(first_text, second_text):
    first = open(first_text, 'r')
    second = open(second_text, 'r')
    first.seek(0)
    second.seek(0)
    first_lines = first.readlines()
    second_lines = second.readlines()
    new = open("merge_file", 'w+')
    i = 0
    while i < len(first_lines) or i < len(second_lines):
        print(i)
        if i < len(first_lines) and len(first_lines[i]) is not 1:
            try:
                new.writelines(first_lines[i])
            except IndexError:
                print("IndexError")
        if i < len(second_lines) and len(second_lines[i]) is not 1:
            try:
                new.writelines(second_lines[i])
            except IndexError:
                print("IndexError")
        i = i + 1
    new.seek(0)
    print(new.readlines())
    first.close()
    second.close()
    new.close()


TEXT1 = ["One", "Three", "Five", "Seven"]
TEXT2 = ["Two", "Four", "Six", "", "Eight"]
with open("first_text", 'w+') as FIRST_FILE:
    FIRST_FILE.writelines(map(lambda x: x + '\n', TEXT1))
    FIRST_FILE.close()
with open("second_text", 'w+') as SECOND_FILE:
    SECOND_FILE.writelines(map(lambda x: x + '\n', TEXT2))
    SECOND_FILE.close()

merge_func("first_text", "second_text")

print(os.path.dirname(os.path.abspath("first_text")))
print(os.path.dirname(os.path.abspath("second_text")))
print(os.path.dirname(os.path.abspath("merge_file")))
