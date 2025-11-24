import logging
from pathlib import Path

logger = logging.getLogger(__name__)


FILE_NAME = Path("homeworks") /"lassuistvanisu"/ "hw_04_exceptions_logging" / "sample.txt"
to_do = []

#def feladat olvasás
def task_read():
    global to_do
    try:
        with open(FILE_NAME, "r") as file:
            to_do = [line.strip() for line in file.readlines()]
        logging.info("Tasks read from the file.")
    except FileNotFoundError:
        logging.warning(f"The {FILE_NAME} not found!.")
        to_do = []
    except Exception as e:
        logging.error(f"Error reading file: {e}")
        to_do = []

        
#def feladatok megjelenítés
def task_show():
    for t, task in enumerate(to_do, 1):
        print(f"{t}. {task}")    
    
#def feladat hozzáadás
def task_add():
    print("/"*42)
    print("TASK ADD")
    print("/"*42)
    
    task_datas = input("New task: ")
    to_do.append(task_datas)
    logging.info(f"Feladat hozzáadva: {task_datas}")


#def feladat törlés
def task_del():
    if not to_do:
        print("The list is empty, there is nothing to delete.")
        return
    try:
        task_show()
        task_delete = int(input("Enter the serial number of the task you want to delete: "))
        if 1 <= task_delete <= len(to_do):
            removed_task = to_do.pop(task_delete - 1)
            print(f"Removed: {removed_task}")
        else:
            print("Invalid number of task!")
    except ValueError:
        print("Please enter a number!")
    print()    

#def feladat írés
def task_write(to_do):
    try:
        with open(FILE_NAME, "w",) as file:
            for task in to_do:
                file.write(task + "\n")
        logging.info("Tasks saved successfully.")
    except Exception as e:
        logging.error(f"Error writing file: {e}")


def display_menu():
    print("\n" + "="*42)
    print("TODO LIST MENU")
    print("="*42)
    items = ["1 - Add task",
             "2 - View tasks", 
             "3 - Delete task", 
             "4 - Exit"]
    for item in items:
        print(item)
    print("="*42)
    