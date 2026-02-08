"""
Feladatkezelő alkalmazás
  
  1. Add Task - feladat hozzáadása a listához
  2. View Tasks - feladatok felsorolás
  3. Remove Task - feladat törlése a listából  
  4. Exit

  A program folyamatosan kérdez, amíg a "4. Exit" menüvel ki nem lépünk. 
"""
import os
from pathlib import Path

from logging_config import setup_logging
import logging

import to_do_function as todo

setup_logging()
logger = logging.getLogger(__name__)

# -*- coding: utf-8 -*-

#print(os.getcwd())

file_path = Path("homeworks") / "lazareva" / "hw_04_exceptions_logging" / "to_do_me.txt" #relative path

def main():

    task_menu = 0

    while task_menu == 0:

        todo.display_menu() #lista a választáshoz
        input_menu = input("Choose from menu: ")

#        print(input_menu)

        if input_menu.isnumeric() and int(input_menu) > 0 and int(input_menu) <= 4:
            task_menu = int(input_menu)
            all_tasks = todo.read_tasks(file_path) #file-ból listába kerül
        else:
            print("Invalid answer. It must be a positive odd integer less or equal 4")
            task_menu = 0

        # 1. Add Task 
        if task_menu == 1:
            print("")
            print("1. Add Task")
            
            task_new = input("    Please, add task name: ")
            print(task_new)
            exist_task = todo.exist_tasks(task_new, all_tasks)

            if exist_task == False:
                todo.write_to_tasks(task_new, file_path)
            task_menu = 0

        # 2. View Tasks
        elif task_menu == 2:
            print("")
            print("2.  View Tasks")
        
            todo.view_task(all_tasks)

            exit_ok = input("Press a karater, then enter to continue: ")

            if exit_ok:
                task_menu = 0                   

        # 3. Remove Task
        elif task_menu == 3:
            print("")
            print("3. Remove Task")

            todo.view_task(all_tasks)
            task_old = input("   Please, add task name: ")

            #Is exists the task?
            exist_task = todo.exist_tasks(task_old, all_tasks)
            
            #If exist > remove task
            if exist_task:
                todo.delete_from_tasks(task_old, all_tasks, file_path)

            task_menu = 0
        
        # 4. Exit
        elif task_menu == 4:
            print("")
            print("4. Exit")

            input_que = True

            while input_que:

                input_que = False
                exit_ok = input("   Are you sure exit (y/n): ")

                if exit_ok == 'y':
                    task_menu = -1  #kilep                  
                elif exit_ok == 'n':
                    task_menu = 0   #ujra
                else:
                    print("   Invalid answer. Correct answer: yes=y, no=n")
                    input_que = True  #ujra kerdez

if __name__ == "__main__":
    main()
