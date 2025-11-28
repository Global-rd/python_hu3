import os
import logging
from pathlib import Path
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)
file_path = Path("homeworks") / "agocsbalazs"/ "hw_04_exceptions_logging"/"to_do.log"
file_path.parent.mkdir(parents=True, exist_ok=True)

if not os.path.exists(file_path):
    with open(file_path, 'w'):
       pass

#0. lépésben feladat lista beolvasása fájlból
#ne a rootba szemeteljen, ezt ki kellett keresni mert nem volt példa rá
base_dir = Path(__file__).resolve().parent
task_file = base_dir / "tasks.txt"
tasks = []  # feladatok listája

#--------------------------------------------------------------------------
#beolvassuk a feladatokat fájlból a globális tasks listába
def reading_task():
 
    global tasks

    if not task_file.exists():
        logger.info(f"Tasks file not found, starting with empty task list. ({task_file})")
        tasks = []
        return

    try:
        with task_file.open("r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]
    except OSError as e:
        logger.error(f"Failed to read tasks file ({task_file}, {e})")
        tasks = []
        return

   #üres sorok kiszűrése a listából
    tasks = []
    for line in lines:
        if line != "":
            tasks.append(line)


    if tasks:
        logger.info(f"Loaded {len(tasks)} tasks from file {task_file}")

    else:
        logger.info(f"Tasks file is empty, starting with empty list. {task_file}" )

#--------------------------------------------------------------------------
#feladatok mentése fájlba a tasks listából
def writing_task():

   #Save & Exit - Feladatok mentése fájlba és kilépés.

    try:
        with task_file.open("w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task + "\n")
    except OSError as e:
        logger.error(f"Failed to load {len(tasks)} tasks from file {task_file}")
        return

    logger.info(f"Saved {len(tasks)} tasks to file {str(task_file)}")

#--------------------------------------------------------------------------

def showing_task():
    
    #Feladatok megjelenítése a listából.
    
    if not tasks:
        print("Nincs egyetlen feladat sem.")
        logger.info("User tried to view tasks, but task list is empty.")
        return

    print("Feladatok:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")
    logger.info(f"Tasks listed. Count: {len(tasks)}")

#--------------------------------------------------------------------------

def deleting_task():
  
    #Egy feladat törlése a globális tasks listából.
   
    if not tasks:
        print("Nincs mit törölni, üres.")
        logger.info("User tried to delete task, but the list is empty.")
        return

    # Miből választhatunk?
    showing_task()

    # Melyiket töröljük?
    choice_del_task = input("Add meg a feladat sorszámát a törléshez: ").strip()

    try:
        index = int(choice_del_task)
    except ValueError:
        print("Nem számot adtál meg.")
        logger.warning(f"Invalid delete input (not an int): {choice_del_task}")
        return

    if index < 1 or index > len(tasks):
        print("Nincs ilyen sorszámú feladat.")
        logger.warning(f"Delete index out of range: {index}")
        return

    removed = tasks.pop(index - 1)
    print(f"Törölve: {removed}")
    logger.info(f"Task deleted at index {index}: {removed}")


#--------------------------------------------------------------------------

def adding_task():

    #Új feladat hozzáadása a listához.
    
    new_task = input("Add meg az új feladatot: ").strip()

    if not new_task:
        print("Üres feladatot nem működik")
        logger.warning("User tried to add an empty task.")
        return

    tasks.append(new_task)
    logger.info(f"New task added: {new_task}")
    print(f"Feladat hozzáadva: {new_task}")


 #--------------------------------------------------------------------------
 # Menü megjelenítése  

def display_menu():
    print ("""
1. Add Task
2. View Tasks
3. Remove Task
4. Save & Exit
""")

def controller():
    logger.info("Application started")
    logger.debug("Initializing controller function")

    reading_task()

    while True:
        display_menu()
        choice = input("Select a menu item (1-4): ")
        if choice == '1':
            adding_task()
        elif choice == '2':
            showing_task()
        elif choice == '3':
            deleting_task()
        elif choice == '4':
            writing_task()
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    controller()
    
