from pathlib import Path
import logging
from logging_config import setup_logging
#import os
#print(os.getcwd())
file_path= Path("homeworks") / "almasilaszlo" / "hw_04_exceptions_logging" / "tasks.txt"
tasks=[]

#logger
setup_logging()
logger=logging.getLogger(__name__)


#Read  
def read_task():
    try:
        with open(file_path,"r") as file:
            lines=file.readlines()
            tasks=[line.strip() for line in lines]
            logger.info(f"Tasks read from file")
            return tasks
    except FileNotFoundError as e:
        print(f"File don't exsist! Please create a file first!")
        logger.error(f"The task.txt does not exsist")
        raise FileNotFoundError("The file does no texsist!")
    except Exception as e:
        print ("File reading error!")
        logger.error(f"File reading error!")

#Write
def write_task(tasks):
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(task+"\n")
            logger.info(f"The task has been saved!")

#View
def view_tasks(tasks):
    if not tasks:
        print(f"\nThe list is empty!")
    else:
        print(f"\nYou open tasks are:")
        print(tasks)

#Add
def add_tasks(tasks,new_task):
    if new_task in tasks:
        print(f"\n2The task {new_task} is alaready on the list! Nothing happened!")
        logger.warning(f"The task {new_task} is alaready on the list! Nothing happened!")
    else:
        tasks.append(new_task)
        print(f"The {new_task} task has been added to the list succesfully!")
        logger.info(f"The {new_task} task has been added to the list succesfully!")

#Remove
def remove_task(tasks, task_to_delete):
    if task_to_delete not in tasks:
        print(f"\nThe task {task_to_delete} is not on the list! Nothing happened!")
        logger.warning(f"The task {task_to_delete} is not on the list!")
    else:
        tasks.remove(task_to_delete)
        print(f"The task {task_to_delete} has been succesfully deleted from the list!")
        logger.info(f"he task {task_to_delete} has been succesfully deleted from the list!")

#display
def display_menu():
    print("\nWelcome to the task manager! What do you want???")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

#read_call
tasks=read_task()

#run main
def main():
        while True:
            display_menu()
            try:
                choice=int(input("What is you choice (1-4)?"))

                if choice==1:
                    new_task=input("Please provide a task you want to add:")
                    add_tasks(tasks,new_task)
                elif choice==2:
                    view_tasks(tasks)
                elif choice==3:
                    task_to_delete=input("What task wold you like to delete?:")
                    remove_task(tasks,task_to_delete)
                elif choice==4:
                    write_task(tasks)
                    break
                else:
                    print(f"Error! Please provide a number between 1-4!")
                    logger.error("Invalid choice!")
            except ValueError:
                print(f"Error! Please provide a NUMBER between 1-4!")
                logger.error("Invalid input!")
            
main()