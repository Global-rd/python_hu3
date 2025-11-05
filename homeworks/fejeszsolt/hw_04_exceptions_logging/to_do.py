import os
from pathlib import Path
from definitions import read_menu
from definitions import chekk_submenu
from definitions import add_task
from definitions import view_tasks
from definitions import remove_task
from definitions import write_task
from definitions import read_file
from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)


file_path = Path("homeworks") / "fejeszsolt" / "hw_04_exceptions_logging" / "to_do.txt" 

todo_list=[]

todo_list = read_file(file_path)

while True:
    read_menu()
    try:
        submenu=int(input("Vállasz menüpontot! A menüpont számát add meg 1-4ig szám formátumban!: "))
    except ValueError:
        logging.error("Hiba! Számot adj meg!")
        continue
    if chekk_submenu(submenu):
        if submenu==(1):
            newtask=str(input("Írdd be a teendőt, amit hozzá akarsz adni:" ))
            add_task(newtask, todo_list)
        elif submenu==(2):
            view_tasks(todo_list)
        elif submenu==(3):
            extask=str(input("Írdd be a teendőt, amit ki akarsz törölni:" ))
            remove_task(extask, todo_list)
        elif submenu==(4):
            write_task(todo_list, file_path)
            exit()