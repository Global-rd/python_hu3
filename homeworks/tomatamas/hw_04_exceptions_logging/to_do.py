import os
import logging
from pathlib import Path
from logging_config import setup_logging

file_path = Path("homeworks") / "tomatamas" / "hw_04_exceptions_logging" / "tasks.txt"

setup_logging()
logger = logging.getLogger(__name__)

"""
---- FÜGGVÉNYEK ----
"""
#Feladatok beolvasása fileból ÉS kezdő task lista létrehozása
def read_file():
    try:
        with open(file_path, "r") as file:
            tasks = []
            lines = file.readlines()
            for line in lines:
                tasks.append(line.strip())
        logger.info(f"Tasks loaded")
        return tasks
    except FileNotFoundError:
        logger.error(f"'{file_path}' not found, starting with an empty list.")
        return [] 
    except Exception as e:
        logger.error(f"Unexpected error while loading file: {e}")
        return []

#Feladatok írása fileba
def write_file(tasks):
    try:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        logger.info("Tasks saved successfully.")
    except Exception as e:
        logger.error(f"Failed to save tasks to file: {e}")

#Feladatok megjelenítése
def view_tasks(tasks_list):
    print("*CURRENT TASKS:")
    if tasks_list:
        for i, task in enumerate(tasks_list, 1):
            print(f"{i} - {task}")
    else:
        print("Tasks list is currently empty!")
    return tasks_list

#Feladat hozzáadása
def append_task(tasks_list):
    task = input("Task to add:").strip()
    tasks_list.append(task)
    return tasks_list

#Feladat törlése
def remove_task(tasks_list):
    task = input("Task to remove:").strip()
    if task in tasks_list:
        tasks_list.remove(task)
        logger.info(f"Task '{task}' removed.")
    else:
        logger.warning(f"Task '{task}' not found.")

#Display menu
def display_menu():
    print("---")
    print("Choose an option, with numbers 1,2,3,4")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove tasks")
    print("4. Exit")
    print("---")

"""
---- PROGRAM ----
"""
#File beolvasása
tasks = read_file()

while True:
    display_menu()
    choice = int(input("Choose an option: ").strip())

    if choice == 1:
        append_task(tasks)
    elif choice == 2:
        view_tasks(tasks)
    elif choice == 3:
        remove_task(tasks)
    elif choice == 4:
        write_file(tasks)
        print("Exiting program...")
        break
    else:
        print("Invalid input!")