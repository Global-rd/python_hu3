# Files contex managers
import os
from pathlib import Path

print (os.getcwd())   

# file_path = "homeworks/petoimre/practices/sample.txt"                               # relative path always
file_path = Path("homeworks") / "petoimre" /"practices" / "sample.txt"
print(file_path)
file = open(file_path, "w")
#abs_path = "C:\PYTHON_LEARNING\python_hu3/homeworks/petoimre/practices/sample.txt"   # absolute path never

# writing without contex managers
try:
    file.write("This is a simple text")
finally:
    file.close()

# writing with contex managers
with open(file_path, "w") as file:
    file.write("This is a sample text111111111.\n")     # \n  = new line

# append mode
with open(file_path, "a") as file:
    file.write("This is a sample text1 append mode.\n")

# reading file to list
with open(file_path, "r") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line.strip())

# generate to read a file

def read_file_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

gen = read_file_line_by_line(file_path)
# print(next(gen()))
# print(next(gen()))
for line in read_file_line_by_line(file_path):
    print(line)
    




