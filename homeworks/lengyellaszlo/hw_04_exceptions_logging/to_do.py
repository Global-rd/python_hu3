from pathlib import Path
import logging
from logging_config import setup_logging
#import os
#print(os.getcwd())

# logger meghívás
setup_logging()
logger = logging.getLogger(__name__)

# beolvasás/hibakezelés
def read_tasks():
    file_path = Path(__file__).parent / "tasks.txt"

    if not file_path.exists():
        try:
            with open(file_path, "w") as file:
                pass
            logger.info("tasks.txt fájl létrehozva, mert nem létezett.")
        except Exception as e:
            logger.error(f"Hiba történt a fájl létrehozása során: {e}")

    try:
        with open(file_path, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        logger.info(f"{len(tasks)} feladat beolvasva a fájlból.")
    except Exception as e:
        logger.error(f"Hiba történt a fájl beolvasása során: {e}")
        tasks = []

    return tasks


# hozzáadás
def add_task(tasks, new_task):
    if new_task in tasks:
        logger.warning(f'A feladat már létezik: "{new_task}"')
        print(f'Hiba: a(z) "{new_task}" feladat már szerepel a listában.')
    else:
        tasks.append(new_task)
        logger.info(f'Új feladat hozzáadva: "{new_task}"')
        print(f'"{new_task}" hozzáadva a listához.')


# megjelenítés
def display_tasks(tasks):
    if not tasks:
        logger.info("Nincs egyetlen feladatod sem.")
        print("Nincs egyetlen feladatod sem.")
    else:
        print(f"{len(tasks)} feladatod van:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        logger.info(f"{len(tasks)} feladat megjelenítve a konzolon.")


# törlés
def remove_task(tasks, task_to_remove):
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        logger.info(f'Feladat törölve: "{task_to_remove}"')
        print(f'"{task_to_remove}" törölve a listából.')
    else:
        logger.warning(f'Nem található a listában: "{task_to_remove}"')
        print(f'Hiba: "{task_to_remove}" nem található a listában.')


# kiírás/mentés
def write_tasks(tasks):
    file_path = Path(__file__).parent / "tasks.txt"
    try:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        logger.info(f"{len(tasks)} feladat elmentve a fájlba.")
    except Exception as e:
        logger.error(f"Hiba történt a fájl írása során: {e}")


# menü
def display_menu():
    print("\nVálassz egy opciót:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


# beolvas
tasks = read_tasks()

# program
while True:
    display_menu()
    try:
        choice = int(input("Add meg a választásod (1-4): "))

        if choice == 1:
            new_task = input("Add meg az új feladatot: ")
            add_task(tasks, new_task)

        elif choice == 2:
            display_tasks(tasks)

        elif choice == 3:
            task_to_remove = input("Add meg a törlendő feladatot: ")
            remove_task(tasks, task_to_remove)
            

        elif choice == 4:
            logger.info("Program leállítva a felhasználó által.")
            print("Kilépés a programból...")
            write_tasks(tasks)
            break

        else:
            logger.warning(f'Érvénytelen választás: {choice}')
            print("Hiba: csak 1 és 4 közötti számot adhatsz meg!")

    except ValueError:
        logger.error("Érvénytelen bemenet: nem egész számot adott meg a felhasználó.")
        print("Hiba: csak egész számot adhatsz meg (1-4)!")
