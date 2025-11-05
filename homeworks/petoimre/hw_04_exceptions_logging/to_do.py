import os
from pathlib import Path
import hw_functions as hw_fc
from logging_config import setup_logging
import logging


setup_logging()
logger = logging.getLogger(__name__)
logger.info("Application started.")

txt_file_name = "hw_tasks.txt"
file_path = Path("homeworks") / "petoimre" / "hw_04_exceptions_logging" / txt_file_name
working_list = []


if os.path.exists(file_path):
    try:
        hw_fc.file_open(file_path, working_list)
    except FileNotFoundError as e:                                                       # no sense
        logger.exception(f"{txt_file_name} not found. System message: {e}")
    
# file_path = ""                                                                         #  make file error to try logging

while True:
    print("------------------------------------")
    print("Type one of them below items number.")
    hw_fc.display_menu()
    user_list_nun_input = input("INPUT:").strip()
    if user_list_nun_input == "1":
        user_task_input = input("Give me the adding task: ")
        hw_fc.add_task(user_task_input, working_list)
    elif user_list_nun_input == "2":
        hw_fc.wiew_tasks(working_list)
    elif user_list_nun_input == "3":
        user_task_input = input("Give me the removing task: ")
        hw_fc.remove_task(user_task_input, working_list)
    elif user_list_nun_input == "4":
        try:
            hw_fc.file_save(file_path, working_list)
            logger.info("Application exit.")
            break
        except FileNotFoundError as e:
            logger.exception(f"{txt_file_name} not found. System message: {e}")
            break
    else:  
        print("You have to type 1-4 numbers!")

