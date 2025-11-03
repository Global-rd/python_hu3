import os
from pathlib import Path
import hw_functions as hw_fc

file_path = Path("homeworks") / "petoimre" / "hw_04_exceptions_logging" / "hw_tasks.txt"
working_list = []

if os.path.exists(file_path):
    hw_fc.file_open(file_path, working_list)

print(f"working_list_start: {working_list}")

while True:
    print("")
    print("Type one of them below items number.")
    hw_fc.display_menu()
    user_list_nun_input = input(" :").strip()
    if user_list_nun_input == "1":
        user_task_input = input("Give me the task: ")
        working_list = hw_fc.add_task(user_task_input, working_list)
        print(f"working_list_1: {working_list}")
    elif user_list_nun_input == "2":
        hw_fc.wiew_tasks(working_list)
        print(f"working_list_2: {working_list}")
    elif user_list_nun_input == "3":
        user_task_input = input("Give me the task: ")
        working_list = hw_fc.remove_task(user_task_input, working_list)
        print(f"working_list_3: {working_list}")
    elif user_list_nun_input == "4":
        hw_fc.file_save(file_path, working_list)
        break
    else:  
        print("You have to type 1-4 numbers!")





 

"""

while True:
    answer = input("Do you want to be a professional python developer (yes/no)")
    if answer in ["yes", "no"]:
        break


if os.path.exists(file_path):
    hw_fc.file_open(file_path, working_list)
    print("Létezik")
else:    
    print("Nem létezik")


print(f"Range előtt: {working_list}")    





#range
for i in range(0,5):
    working_list.append(str(i))

working_list = hw_fc.List_single_items(working_list)    

hw_fc.file_save(file_path, working_list)

print(f"Range után: {working_list}")   

"""