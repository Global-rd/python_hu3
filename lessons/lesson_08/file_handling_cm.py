import os
from pathlib import Path
print(os.getcwd())


file_path = Path("lessons") / "lesson_08" / "sample.txt" #relative path
file = open(file_path, "w")

#writing without context managers
try:
    file.write("This is a sample text")
finally:
    file.close()

#writing with context managers
with open(file_path, "w") as file:
    file.write("This is a sample text\n")


#append mode
with open(file_path, "a") as file:
    file.write("This is a sample text again\n")

#reading a file:

with open(file_path, "r") as file:
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line.strip())

print("---------------------")
#generator to read a file:

def read_file_line_by_line(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()


gen = read_file_line_by_line(file_path)
#print(next(gen))
#print(next(gen))

for line in read_file_line_by_line(file_path):
    print(line)