from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

def read_tasks_from_file(filename):
    """Feladatok beolvasása fájlból"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            tasks = [line.strip() for line in file.readlines()]
            logger.info("Feladatok beolvasva a fájlból.")
            return tasks
    except FileNotFoundError:
        logger.warning("A fájl nem található, üres listával indul a program.")
        return []

def save_tasks_to_file(filename, tasks):
    """Feladatok mentése a fájlba"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        logger.info("Feladatok mentve a fájlba.")
    except Exception as e:
        logger.error(f"Hiba a fájlba íráskor: {e}")

def display_menu():
    print("\nVálassz egy opciót:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    try:
        task = input("Add meg az új feladatot: ")
        tasks.append(task)
        print(f'"{task}" hozzáadva a listához.')
        logger.info(f'Feladat hozzáadva: {task}')
    except Exception as e:
        print("Hiba történt a feladat hozzáadásakor.")
        logger.error(f'Hiba a feladat hozzáadásakor: {e}')

def view_tasks(tasks):
    if not tasks:
        print("\nNincs egyetlen feladat sem a listában.")
    else:
        print("\nFeladatok:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_tasks(tasks):
    view_tasks(tasks)
    if not tasks:
        logger.warning("Törlési kísérlet az üres listából.")
        return
    
    try:
        index = int(input("Add meg a törlendő feladat sorszámát: ")) - 1
        if index < 0 or index >= len(tasks):
            print("X Érvénytelen sorszám.")
            logger.warning(f"Érvénytelen sorszám: {index + 1}")
        else:
            removed = tasks.pop(index)
            print(f'"{removed}" törölve a listából.')
            logger.info(f'Feladat törölve: {removed}')
    except ValueError as e:
        print("X Hibás bevitel! Kérlek, számot adj meg.")
        logger.error(f'Hibás bevitel (nem szám): {e}')

# ---- Főprogram ----
FILENAME = "tasks.txt"
tasks = read_tasks_from_file(FILENAME)

while True:
    display_menu()
    choice = input("\nVálasztásod: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        remove_tasks(tasks)
    elif choice == "4":
        print("Kilépés... Viszlát!")
        logger.info("Program leállt a felhasználó kérésére.")
        save_tasks_to_file(FILENAME, tasks)
        break
    else:
        print("X Érvénytelen opció! Próbáld újra.")
        logger.warning(f"Érvénytelen menüválasztás: {choice}")

    