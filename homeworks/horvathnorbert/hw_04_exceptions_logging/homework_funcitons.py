import os
from datetime import datetime
from pathlib import Path
import logging
from logging_config import setup_logging

current_dir = Path(__file__).resolve().parent
file_path = current_dir / "tasks.txt"

setup_logging()
logger = logging.getLogger(__name__)

def clear_line():
    print("\033[2K", end="")

def cursor_move_to(x, y):
    print(f"\033[{y};{x}H", end="")

def menu_draw(menu_items,menu_item):
        
    if menu_item != None:
        menu_item -= 1
    
    if menu_item == None:
        cursor_move_to(1, 1)
        print(f"------MAIN MENU------")
        for k, v in menu_items.items():
            print(f"   {k}. {v}")
        print(f"---------------------")
    else:
        cursor_move_to(1, 1)
        print(f"------MAIN MENU------")
        for k, v in menu_items.items():
            if menu_item == k-1:
                print(f" ▷ {k}. {v}")
            else:
                print(f"   {k}. {v}")
        print(f"---------------------")

def add_task(tasks,task_description):
    if not tasks:
        last_key = 1
        tasks[last_key] = task_description
    else:
        last_key = list(tasks.keys())[-1]
        tasks[last_key + 1] = task_description
        # return tasks

def read_task(tasks):
    if tasks:
        print("-----------------TASKS------------------")
        for k, v in tasks.items():
            print(f"{k}. {v}")
    else:
        print("There are no tasks!")

def remove_task(task_to_delete,tasks):
    del tasks[task_to_delete]


def load_tasks(tasks):
    try:
        with open (file_path, "r") as file:
            for i, line in enumerate(file, start=1):
                tasks[i] = line.strip()
        logger.debug(f"{file} File opened, tasks loaded.")
    except:
        with open (file_path, "w") as file:
            logger.debug(f"{file} not exist, {file} created.")

def close_file(tasks):
    with open(file_path, "w") as file:
        for k, v in tasks.items():
            file.write(f"{v}\n")
        


        
        
        
    
    


    
    
        
           







        

    








