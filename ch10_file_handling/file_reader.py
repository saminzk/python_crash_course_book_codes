import os
print(os.getcwd())
file_path ="./python_works/text_files/pi_digits.txt"
with open(file_path) as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())
    lines = file_object.readlines()


for line in lines:
    print(line.rstrip())