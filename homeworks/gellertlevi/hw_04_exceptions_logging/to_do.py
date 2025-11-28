import os   # Operating system modul beszedése
import logging # loggoló modul beszedése

#from pathlib import Path # Path modul beszedése
#print(os.getcwd())

logger = logging.getLogger(__name__) #  Logging beállítás 
logger.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') # Log formátum

console_handler = logging.StreamHandler() # Konzolra 
console_handler.setFormatter(formatter)


file_handler = logging.FileHandler('todo.log') # File-ba 
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

"""Tasks to choose from"""
def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

#display_menu()


FILENAME= "Task.txt"

def view_tasks():
    tasks = []
    try:
        if os.path.exists(FILENAME):
            with open(FILENAME, "r") as file:
                tasks = [line.strip() for line in file.readlines()]
                logger.info("Open existing Task.txt file .")    
        else:
            with open(FILENAME, "w") as file:
              logger.info("Creating new Task.txt file")        
       
    except Exception as e:
            logger.error(f"File handling error: {e}")
    return tasks
                  
def    write_tasks(tasks)  :
    try:
        with open(FILENAME, "w") as file:
            for task in tasks:
                file.write(task + "\n") # feladat hozzáadása soronként "\n"
        logger.info("Task added.")
    except Exception as e:
        logger.error(f"Task writing error: {e}")



def add_task(task):
    
    tasks = view_tasks()
    tasks.append(task)
    write_tasks(tasks)
    logger.info(f"Task added: {task}")
    print(f'"{task}" Task added to list.\n')   


def remove_task(index):
    
    tasks = view_tasks()
    try:
        removed = tasks.pop(index - 1)
        write_tasks(tasks)
        logger.info(f"Task removed: {removed}")
        print(f'"{removed}" removed from list.\n')
    except IndexError:
        logger.warning("Invalid task number to delete.")
        print("Provide correct task number to delete .\n")    

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            tasks = view_tasks()
            if not tasks:
                print("\nNo tasks available.\n")
            else:
                print("\n--- Tasks ---")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                print("--------------\n")
        elif choice == '3':
            index = int(input("Enter the task number to remove: "))
            remove_task(index)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")
if __name__ == "__main__":
    main()

         
