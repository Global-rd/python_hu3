import logging.config
from pathlib import Path

LOG_DIR = Path("logs")
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
            "level": "INFO",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
    return logging.getLogger()

def read_tasks(filename):
    try:
        with open(filename, "r") as file:
            return file.read().split(",")
    except:
        logger.info("Task file doesn't exist")
        return list()

def write_tasks(task_list, filename):
    task_str = ",".join(task_list)
    try:
        with open(filename, "w") as file:
            file.write(task_str)
    except Exception as e:
        logger.info(e)

def view_tasks(task_list):
    logger.info(f"These are your tasks: {task_list}")

def add_task(task_list, task):
    return task_list.append(task)

def delete_task(task_list, task):
    return task_list.remove(task)

def display_menu(filename, logger):
    task_list = read_tasks(filename)
    selection = None

    while selection != "4":
        try:
            selection = input("Choose from the following options:\n\t1. Add Task\n\t2. View Tasks\n\t3. Remove Task\n\t4. Exit\n")

            if int(selection) not in range(1,5):
                raise ValueError("Error: choose from the selected option with the numbers")

            if selection == "1":
                task = input("The task you want to add: ")
                add_task(task_list, task)
            elif selection == "2":
                view_tasks(task_list)
            elif selection == "3":
                task = input("The task you want to remove: ")
                delete_task(task_list, task)
        except Exception as e:
            logger.info(e)

    
    logger.info("Saving your file, goodbye!")
    write_tasks(task_list, filename)

filename = "tasks.txt"
logger = setup_logging()
display_menu(filename, logger)