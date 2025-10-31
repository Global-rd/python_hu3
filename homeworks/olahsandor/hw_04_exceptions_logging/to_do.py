import logging
import os

#Fájlok elérési útjai - a mappába tettem őket, ahol a to_do.py is van
tasks_file = "task.txt"
log_file = "app.log" 

# Logolás, az óráról
file_handler = logging.FileHandler(log_file)
stream_handler = logging.StreamHandler()
formatter_file = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
formatter_cons = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter_file)
stream_handler.setFormatter(formatter_cons)
file_handler.setLevel(logging.ERROR)
stream_handler.setLevel(logging.INFO)
logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


#Feladatok olvasása:
def load_tasks_from_file():
    try:
        with open(tasks_file, "r") as file:
# Beolvassuk a sorokat, eltávolítjuk a whitespace-t
            tasks_list = []
            lines = file.readlines()
            for line in lines:
                task = line.strip() 
                if task: 
                    tasks_list.append(task)
        logger.info(f"Tasks loaded: {len(tasks_list)} items.")
        return tasks_list
    except FileNotFoundError:
        logger.error(f"Task file '{tasks_file}' not found. Starting with an empty list.")
# Üres lista visszaadása
        return [] 
    except Exception as e:
        logger.error(f"An unexpected error occurred during file loading: {e}")
        return []

#Feladatok Írása:
def save_tasks_to_file(tasks_list):
    try:
        with open(tasks_file, "w") as file:
# Felülírjuk a fájlt a memóriábanmal
            file.writelines(f"{task}\n" for task in tasks_list)
        logger.info(f"Tasks saved successfully: {len(tasks_list)} items.")
    except Exception as e:
        logger.error(f"Failed to save tasks to file: {e}")


# Feladat megjelenítése
def view_tasks(tasks_list):
    print("\n--- View Tasks (Current List) ---")
    if tasks_list:
        for i, task in enumerate(tasks_list, 1):
            print(f"{i}. {task}")
    else:
        logger.info("The task list is empty.")
    
# Mivel ez a függvény nem módosítja a listát, az eredeti listával tér vissza
    return tasks_list


#Feladat Hozzáadása
def add_task(tasks_list, task_to_add):
    task = task_to_add.strip()
    if task:
        tasks_list.append(task)
        print(f"'{task}' added to list (in memory).")
    else:
        logger.info("The task to add cannot be empty.")
# A frissített lista visszaadása
    return tasks_list 

#Feladat Törlése
def remove_task(tasks_list, task_to_remove):
    task = task_to_remove.strip()

    try:
        tasks_list.remove(task)
        print(f"'{task}' deleted from memory.")
    except ValueError:
        # Akkor dobódik, ha az elem nincs a listában
        logger.error(f"There is no such task: '{task}'!")
# A frissített lista visszaadása
    return tasks_list 


#Menü
def display_menu():
    print("\n--- Task Manager Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit (Save & Exit)")
    
    while True:
        try:
            chosen_str = input("Choose please (1-4): ")
            
            if not chosen_str:
                logger.info("The selection must be between 1 and 4!")
                continue
                
            chosen = int(chosen_str)
            
            if chosen in range(1, 5):
                return chosen
            else:
                logger.info("The selection must be between 1 and 4!")
        except ValueError:
            logger.info("Invalid input. Please enter a number (1-4).")


#fő Program
def main():
    
# 1. A fájlból való olvasás automatikusan megtörténik a program indulásakor
    tasks_list = load_tasks_from_file() 
    logger.info("Program RUN started.")

    while True:
        chosen = display_menu() 
        
        if chosen == 1:
            task = input("What is the task to add?: ").strip()
# A függvény frissíti a listát, és a visszatérési értékkel frissítjük a tasks_list-et
            tasks_list = add_task(tasks_list, task) 
        
        elif chosen == 2:
            tasks_list = view_tasks(tasks_list) 
        
        elif chosen == 3:
            task = input("What is the task to remove?: ").strip()
# A függvény frissíti a listát, és a visszatérési értékkel frissítjük a lokális tasks_list-et
            tasks_list = remove_task(tasks_list, task) 
        
        elif chosen == 4:
# 2. Fájlba írás csak a program befejezésekor
            save_tasks_to_file(tasks_list) 
            logger.info("Program RUN completed. Exiting.")
            break

if __name__ == "__main__":
    main()