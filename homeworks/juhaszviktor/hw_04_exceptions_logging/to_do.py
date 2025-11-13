import os
import logging
import logging.config
from pathlib import Path

base_dir = Path(__file__).parent  # a futó fájl mappája
file_name = "tasks.txt"
file_path = base_dir / file_name

tasks = []  # itt tartjuk a feladatokat a memóriában

LOG_DIR_NAME = "logs"
LOG_DIR = base_dir / LOG_DIR_NAME
LOG_DIR.mkdir(exist_ok=True)

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {
            "format": "%(levelname)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "INFO",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "app.log",
            "maxBytes": 10_000_000,
            "backupCount": 5,
            "formatter": "default",
            "level": "DEBUG",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)

def display_menu(): 
    print ("1) Add Task")
    print ("2) View Task")
    print ("3) Remove Task")
    print ("4) Exit")

def load_task():
    with open(file_path, "r", encoding="utf-8") as f:
        tasks[:] = [line.strip() for line in f if line.strip()]

def save_task():
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(tasks))
    print("Feladatok elmentve.")

def add_task():
    task = input("Írd be az új feladatot: ").strip()
    if task:
        tasks.append(task)
        print("Hozzáadva.")
    else:
        print("Üres feladatot nem veszek fel.")

def view_tasks():
    if not tasks:
        print("Nincs egyetlen feladat sem.")
        return
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")

def remove_task():
    if not tasks:
        print("Nincs mit törölni.")
        return
    view_tasks()
    try:
        idx = int(input("Melyik sorszámot töröljem? ")) - 1
        removed = tasks.pop(idx)
        print(f"Törölve: {removed}")
    except (ValueError, IndexError):
        print("Érvénytelen sorszám.")

def main():
    setup_logging()
    logger = logging.getLogger()    

    logger.info("Elindult a program")
    #logger.warning("Warning message")
    #logger.error("Error message")
    #logger.critical("Critical message")

    load_task()
    display_menu()

    while True:    
        choice = input ("Válassz egy funkciót (1-4): ").strip()
        logger.info(f"Választásod: {choice}")    
        if choice == "4":
            save_task()
            break    
        elif choice == "1":            
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        else:            
            print ("Érvénytelen választ adtál. A lehetséges válaszok: 1,2,3,4 !")
            display_menu()
main()


