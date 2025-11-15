

import logging
import logging.config
from pathlib import Path

LOG_DIR = Path("homeworks") / "horvolgyinegalkatalin" / "hw_04_exceptions_logging"
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
            "encoding":"utf-8"
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
def read_file(to_do_txt_path: Path):
    strip_lines = []
    try:
        with open(to_do_txt_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                strip_lines.append(line.strip())
    except FileNotFoundError:
        logger.error(f"A feladatfájl nem található: {to_do_txt_path}")
        # új üres fájlt hozunk létre
        to_do_txt_path.touch()
    except Exception as e:
        logger.exception("Váratlan hiba a fájl olvasása közben.")
        raise
    return strip_lines

def write_file(to_do_txt_path:Path,write_list:list): #feltételezem, hogy ugyanazzal a fileal dolgozunk és nem egy másik értékkel
    with open(to_do_txt_path, 'w', encoding="utf-8") as file:
        for elem in write_list:
            file.write(elem+"\n")


def view_tasks(task_list):
    for task in task_list:
        print(task)

def add_tasks(task_list,input_task):
    task_list.append(input_task)

def del_task(task_list,input_task):
    try:
        task_list.remove(input_task)
    except ValueError:
        print("Nincs mit törölni")    
def display_menu(menu):
    for menu_pontok in menu:
       print(menu_pontok)

setup_logging()
logger=logging.getLogger(__name__)

menu=["1. Add Task:","2.View Tasks:", "3. Remove Tasks:", "4. Exit"]

def main():

    file_path = Path("homeworks") / "horvolgyinegalkatalin" / "hw_04_exceptions_logging" / "to_do.txt" #relative path

    task_list=read_file(file_path)
    logger.info("beolvastam az eddigi feladatokat a fájlból")
    display_menu(menu)

    while True:
        try:
            menu_mumber=int(input("Válassz a menüpontok közül 1-4-ig:"))

        except ValueError:
            logger.error("Csak számot adhatsz meg!")
            continue    
        if 1<= menu_mumber <=4:
                
            if menu_mumber==1:
                logger.debug("hozzáadom az ój feladatot a listához")
                task=input("Add meg a feladatot:")
                add_tasks(task_list,task)
                    
            elif menu_mumber==2:
                logger.debug("most kiírom a listát a képernyőre")
                view_tasks(task_list)

            elif menu_mumber==3:
                task=input("Add meg a feladatot:")
                del_task(task_list,task)
                logger.debug("kitörlődött a törölni való")

            elif menu_mumber==4:
                logger.debug("Most fogom a fájlba kiírni visszaírni a to_do listát az 4 menüpont választása miatt")
                write_file(file_path,task_list)
                break

        else:
            logger.warning("csak 1-4-ig adhatsz meg számokat!")
    

if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)
    main()

