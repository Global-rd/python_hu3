#imports
from pathlib import Path
from logging_config import setup_logging
import logging


setup_logging()
logger = logging.getLogger(__name__)

"""collection of used functions"""

def display_menu(list_of_menu):
    """This function print a parts of list with order number.
    Imput must be a list.

    Imput:
    ["a", "b", "c"]

    result:
    1. a
    2. b
    3. c
    """
    print("Menu:")
    for order,task in enumerate(list_of_menu):
        print(f"{order+1}:",task.strip())


def read_tasks(file_path):                  # feladatok ovlasása file-ból
    """Read information from file ( .txt ), and return with a list.
        Function using 'with'. 
    """
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            return lines
    except Exception as e:
        logger.exception(f"Something problem happened: {e}")


def write_tasks(file_path, list):           # feladatok írása file-ba
    """Write information to file ( .txt ) from a list.
    """
    try:
        with open(file_path, "w") as file:
            file.write(list)
    except Exception as e: 
        logger.exception(f"Something unexpected happened: {e}")

def view_tasks(to_do_list):                 # feladatok megjelenítése
    """ Print list on consol with order number.
        input: list
        output: list on consol
    """
    print("")
    print("Current task list:")
    for n, line in enumerate(to_do_list):
        print(f"{n+1}. ",line.strip())


def add_task(to_do_list):                             # egy feladat hozzáadása
    """Import information from terminal and append to current list.
        attributum: list
        in: (any)
    """
    if type(to_do_list) != list:
        raise ValueError("Attributum must be type list!")

    new_task = input("Please input your new task: ")
    to_do_list.append(new_task)
    

def remove_task(to_do_list):                         # egy feladat törlése
    """ Remove element from list according to order of element.
        attributes: list
        in: (int)
    """
    number_of_element = int(input("Please give number of element what you would like to remove from your list: "))-1
    removed_task = to_do_list.pop(number_of_element)
    print(f"I have removed '{removed_task}' from todo list.")


def exit(file_path, to_do_list):
    """ Stop running main cycle and save 'to_do_list' to file on 'file_path'.
        attributes: path of file (str)
                    list of items (list)
    """
    with open(file_path, "w") as file:
        for item in to_do_list:
            file.write(item.strip() + "\n")
    print("List has been saved.")

def chosen_check(chose):
    """ Checks input of attribute. If it is not 1, 2, 3, 4, makes ValueError
        attribute: (any) :)
    """
    if chose not in [1,2,3,4]:
        raise ValueError("You must use numbers (int) from 1 to 4!")
    