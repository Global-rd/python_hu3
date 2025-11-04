import logging
import os
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
    with open(file_path, 'w') as f:
        pass
with open(file_path, 'r') as f:
    my_list = [line.strip() for line in f.readlines()]
#add task
def add_task():
    my_list.append(input("Enter a task: "))
    return my_list
#read tasks
def read_tasks():
    return my_list
#write tasks
def tasks_write(tasks):
    my_list.extend(tasks)
    with open(file_path, 'a') as f:
        for task in tasks:
            f.write(task + '\n')
#view tasks
def view_tasks():
    for task in my_list:
        print(task)
#remove task
def remove_task():        
    task_to_remove = input("Enter a task to remove: ")
    if task_to_remove in my_list:
        my_list.remove(task_to_remove)
        with open(file_path, 'w') as f:
            for task in my_list:
                f.write(task + '\n')
    else:
        logger.warning(f"Task '{task_to_remove}' not found in the list.")
