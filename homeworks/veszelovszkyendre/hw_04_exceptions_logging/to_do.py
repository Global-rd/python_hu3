import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("todo.log", mode="a", encoding="utf-8")
    ]
)
logger = logging.getLogger(__name__)

TASK_FILE = "tasks.txt"
tasks = []


def read_tasks():
    try:
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r", encoding="utf-8") as f:
                tasks.extend([line.strip() for line in f if line.strip()])
            logger.info(f"{len(tasks)} feladat beolvasva.")
        else:
            logger.warning(f"{TASK_FILE} nem található, üres lista indul.")
    except Exception as e:
        logger.error(f"Hiba olvasáskor: {e}")


def write_tasks():
    try:
        with open(TASK_FILE, "w", encoding="utf-8") as f:
            f.writelines(f"{task}\n" for task in tasks)
        logger.info("Feladatok elmentve.")
    except Exception as e:
        logger.error(f"Hiba íráskor: {e}")


def view_tasks():
    if not tasks:
        print("Nincs feladat.")
    else:
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")


def add_task():
    task = input("Add meg a feladatot: ").strip()
    if task:
        tasks.append(task)
        logger.info(f"Hozzáadva: {task}")
    else:
        print("Üres feladat nem adható hozzá.")


def remove_task():
    view_tasks()
    try:
        idx = int(input("Törlendő sorszám: "))
        removed = tasks.pop(idx - 1)
        logger.info(f"Törölve: {removed}")
    except (ValueError, IndexError):
        print("Hibás sorszám.")
        logger.warning("Hibás sorszámot adott meg a felhasználó.")


def display_menu():
    print("\n--- Menü ---")
    print("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit")


def main():
    read_tasks()

    # Menü opciók dictionary-ben
    options = {
        "1": add_task,
        "2": view_tasks,
        "3": remove_task,
        "4": None
    }

    while True:
        display_menu()
        choice = input("Válassz (1-4): ").strip()

        if choice not in options:
            print("Érvénytelen választás!")
            continue

        if choice == "4":
            write_tasks()
            print("Kilépés... Feladatok elmentve.")
            break

        # Dictionary-ből hívjuk a megfelelő függvényt
        try:
            options[choice]()
        except Exception as e:
            logger.error(f"Hiba a menüpont futtatása közben: {e}")


if __name__ == "__main__":
    main()
