import logging
import logging.config
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

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
        logger.warning("Törlési kísérlet az üres listából")
        return #ha üres a lista kilépünk
    
    try:
        index = int(input("Add meg a törlendő feladat sorszámát: ")) - 1
        if index < 0 or index >= len(tasks):
            print("X Érvénytelen sorszám")
            logger.warning(f"Érvénytelen sorszám: {index + 1}")
        else:
            removed = tasks.pop(index)
            print(f'"{removed}" törölve a listából.')
            logger.info(f'Feladat törölve: {removed}')
    except ValueError as e:
            print("X Hibás bevitel! Kérlek, számot adj meg.")
            logger.error(f'Hibás bevitel (nem szám): {e}')
tasks = []

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
        break
    else:
        print("X Érvénytelen opció! Próbáld újra.")
        logger.warning(f"Érvénytelen menüválasztás: {choice}")

    