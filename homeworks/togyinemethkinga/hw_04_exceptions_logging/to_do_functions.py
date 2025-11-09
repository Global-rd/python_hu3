import os
from pathlib import Path
import logging
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger('to_do_functions.log')

file_path = Path("homeworks") / "togyinemethkinga" / "hw_04_exceptions_logging" / "to_do_list.txt"


def task_reading(file_path = file_path):
    # Put the tasks in a list.
    try:
        with open(file_path, "r") as file:
            task_list = list(line.strip() for line in file)
            return task_list
    except FileNotFoundError as e:
        logger.error(f"FileNotFoundError error: {e}")


def task_writing(tasks):
    # Overwrite the list.
    try:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(f"{task}\n")
    except FileNotFoundError as e:
        logger.error(f"FileNotFoundError error: {e}")



def display_tasks():
    # Show the list 
    with open(file_path, "r") as file:
        lines = file.readlines()
    for i, line in enumerate(lines, 1):
        print(f"{i}. task: {line.strip()}")


def add_task(task):
    # Add task to the list.
    with open(file_path, "a") as file:
       file.write(f"{task}\n")


def remove_task():
    #Remove a task from the list.
    task_to_remove = input("Which task would you like to remove?")
    task_list = task_reading()
    if task_to_remove in task_list:
        task_list.remove(task_to_remove)
        new_list = task_list
        task_writing(new_list)
        # logger.info(f"{new_list} is the new list.")
    else:
        logger.info(f"{task_to_remove} is not on the list.")
       

def display_menu():
    # Choose a task.
    print("TASKS:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

