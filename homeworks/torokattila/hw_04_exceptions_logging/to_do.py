import os
from pathlib import Path

from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

file_path = Path("homeworks") / "torokattila" / "hw_04_exceptions_logging" / "tasks.txt"

# Functions declaration
# Beolvassa a tasks.txt fájlból a TASK információkat.
def read_tasks(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tasks = [line.strip() for line in file if line.strip()]
        logger.info("Tasks successfully read from file.")
        return tasks
    except FileNotFoundError:
        logger.warning(f"File not found: {file_path}. Starting with empty task list.")
        return []
    except Exception as e:
        logger.exception(f"Error reading from file: {e}")
        return []
# Kiírja a task.txt fájlba a TASK információkat a programból való kilépéskor
def write_tasks(task_list, file_path):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            for task in task_list:
                file.write(task + "\n")
        logger.info("Tasks successfully written to file.")
    except Exception as e:
        logger.exception(f"Error writing to file: {e}")

def display_tasks(task_list):
    print("-----------")
    print("Tasks list:")
    print("-----------")
    for task in task_list:
        print(task)
    
def add_task(task_list, name:str):
    task = name
    task_list.append(task)
    logging.info("Task added")    

def remove_task(task_list, name:str):
    for task in task_list:
        if task == name:
            task_list.remove(task)
            logging.info("Task deleted")
            return
    
def display_menu():
    print ("M E N U")
    print("-----------")
    print ("1 - Add a new task")
    print ("2 - View tasks")
    print ("3 - Remove a task")
    print ("4 - Exit")

def main():
    logger.info("Application started")
    task_list = []
    # Ha létezik a tasks.txt akkor beolvassuk soronként és beírjuk a task_list-be.        
    if file_path.exists():
        read_tasks(file_path)

    while True:
        display_menu()
        try:
            answare = int(input ("Choose an option: "))
            
            if answare == 4:
                write_tasks(task_list,file_path)
                break
            if answare == 3:
                task_name_to_delete = input("Which task should I delete? ")
                remove_task(task_list,task_name_to_delete)
            if answare == 2:
                display_tasks(task_list)
            if answare == 1:
                task_name_to_add = input("What is name the new task ? ")
                add_task(task_list,task_name_to_add)
                
        except ValueError as e:            
            logger.exception(f"An error occured: {e}")                        
    logger.info("Application quit")

main()
