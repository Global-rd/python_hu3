import logging
import os
from logging_config import setup_logging
setup_logging()
logger = logging.getLogger(__name__) 
logger = logging.getLogger('to_do.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('to_do.log')
stream_handler = logging.StreamHandler()
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
file_path = "homeworks/kissmate/hw_4_exceptions_logging/to_do_list.txt"
if not os.path.exists(file_path):
    with open(file_path, 'w'):
        pass
#add task
def add_task():
    task = input("Enter a new task: ")
    tasks_write([task])
    logger.info(f"Task '{task}' added to the list.")
#read tasks
def read_tasks():
    with open(file_path, 'r') as f:
        tasks = f.readlines()
    return [task.strip() for task in tasks]
#write tasks
def tasks_write(tasks):
    with open(file_path, 'a') as f:
        for task in tasks:
            f.write(task + '\n')
    global my_list
    my_list = read_tasks()
#view tasks
def view_tasks():
    my_list = read_tasks()
    if not my_list:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(my_list, start=1):
            print(f"{idx}. {task}")
#remove task
def remove_task():        
    task_to_remove = input("Enter the task to remove: ")
    my_list = read_tasks()
    if task_to_remove in my_list:
        my_list.remove(task_to_remove)
        with open(file_path, 'w') as f:
            for task in my_list:
                f.write(task + '\n')
        logger.info(f"Task '{task_to_remove}' removed from the list.")
    else:
        print("Task not found in the list.")
#menu
def display_menu():    
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
#assign user selection
def get_user_selection():
    if selection == "1":
        return add_task()
    elif selection == "2":
        return view_tasks()
    elif selection == "3":
        return remove_task() 
#user inpunt/user mistake handling
while True:
    display_menu()
    selection = input("Select an option (1-4): ")
    if selection not in ["1", "2", "3", "4"]:
        raise ValueError("Invalid menu selection.")
    try:
       result = get_user_selection()  
    except ValueError("Please enter a valid option."):
        print("Invalid input. Please enter a number.")
    if selection == "4":
        print("Exiting the program.")
        break