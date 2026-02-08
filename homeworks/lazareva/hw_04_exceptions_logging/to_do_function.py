"""
Feladatkezelő alkalmazás - function-ok
  
- display_menu() - kiírja a választható menüpontokat
     1. Add Task
     2. View Tasks
     3. Remove Task 
     4. Exit
- read_tasks(file_path) - fájlból task-okat olvas ki > all_tasks
- exist_tasks(task_new, all_tasks) - ellenőrzi, hogy létezik-e a task a listában
     -  ha nem, és az "1. Add Task" menüpontban vagyunk,
        akkor hozzáadja a program az új feladatot a listához
     -  ha igen, és az "3. Remove Task" menüpontban vagyunk,
        akkor törli a program a feladatot a listából
- write_to_tasks(task_new, file_path) - fila végére felveszi az új taskot
     feltéve, hogy az exist_tasks() ellenőrzés eredmény False
- delete_from_tasks(task_old, all_tasks, file_path) - töröl a listából
     feltéve, hogy az exist_tasks() ellenőrzés eredmény True
- view_task(all_tasks) - egymás alá felsorolja a feladataokat
"""
import os
from pathlib import Path

from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

print(os.getcwd())

# -*- coding: utf-8 -*-

#kiír
def display_menu():
    print("------------------")
    print(f"Choose from menu")
    print("------------------")

    print(f"   1. Add Task") 
    print(f"   2. View Tasks") 
    print(f"   3. Remove Task") 
    print(f"   4. Exit")


#fájlból task-okat olvas ki > all_tasks
def read_tasks(file_path):
 
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
#           print(lines)
            all_tasks = []

            for line in lines:
                task_me = line.rstrip()
#                print(task_me)

                if task_me:
                    all_tasks.append(task_me)
#            logger.info("Reading tasks end")
            return(all_tasks)
    except FileNotFoundError as e:
        logger.error("File doesn't exists!")
        raise
    except Exception:
        logger.exception("Unexpected error while reading file")
        raise

#létezik már a task? > True/False
def exist_tasks(task_new, all_tasks):
    
    exist_file = False
    
    for task_old in all_tasks:
        if task_new == task_old: 
            print(f"Existing task! ({task_new})")
            exist_file = True               
    print(f"Checking task result: {task_new} {exist_file}")
    return exist_file

# file vegere ir
def write_to_tasks(task_new, file_path):

    try:
        with open(file_path, "a") as file:
            file.write(f"{task_new}\n")
        logger.info("Writing tasks end")
    except FileNotFoundError as e:
        logger.error("File doesn't exists!")
        raise
    except Exception:
        logger.exception("Unexpected error while writing file")
        raise
   

def delete_from_tasks(task_old, all_tasks, file_path):
    all_tasks.remove(task_old)
#    print(all_tasks)
    try:
        with open(file_path, "w") as file:
            for task in all_tasks:
                file.write(f"{task}\n")
        logger.info(f"Delete {task_old} task from list end")
    except FileNotFoundError as e:
        logger.error("File doesn't exists!")
        raise
    except Exception:
        logger.exception("Unexpected error while deleting from file")
        raise

def view_task(all_tasks):
    
    if all_tasks:
        for task in all_tasks:
            print(f"   {task}")
#        logger.info("View tasks end")
    else:
        logger.info("The task list is empty.")
    
    






