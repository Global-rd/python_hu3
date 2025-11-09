
import logging
from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


def file_open(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        logger.warning(f"File not found: {file_path}")
        return []
    except Exception as e:
        logger.exception(f"Unexpected error while opening file: {e}")
        return []

      
def file_save(file_path, m_list=None):
    """
    Write the m_list content to the list, each below.
    """
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        #Path(file_path).parent.mkdir(parents=True, exist_ok=True) #ezzel biztosítjuk hogy a parent mappa létezik

        with open(file_path, "w", encoding="utf-8") as file:
            for element in m_list:
                file.write(element + "\n")

        logger.info(f"File successfully saved: {file_path} ({len(m_list)} tasks)")
    
    except PermissionError:
        logger.exception(f"Permission denied when writing to {file_path}")
        print("Error: insufficient permissions to save file.")

    except FileNotFoundError:
        logger.exception(f"Invalid path: {file_path}")
        print("Error: the given path is invalid.")

    except Exception as e:
        logger.exception(f"Unexpected error saving file: {e}")
        print("An unexpected error occurred while saving tasks.")


def display_menu():
    """
    Print the menu_list to the consol.
    """
    menu_list = ["Add Task", "View Tasks", "Remowe Task", "Exit"]
    for id, menu_item in enumerate(menu_list, 1):
        print(f"{id}. {menu_item}")            


def add_task(task, my_list=None):
    '''
    Add the task string to the m_list.
    '''        
    list_cnt = len(my_list)
    if list_cnt == 0:
        my_list.append(task)
        print(f"{task} is succesfully added.")
        return my_list
    for list_element in (my_list):
        if (task == list_element):
            print(f"{task} is already exist on the list.")
            return my_list
    my_list.append(task)
    print(f"{task} is succesfully added.")
    return my_list   


def wiew_tasks(my_list=None):
    '''
    Print the my_list to the consol, with enumerate.
    ''' 
    list_cnt = len(my_list)
    if list_cnt == 0:
        print("The list is empty")
    print("Tasks:")
    for id, list_element in enumerate(my_list, 1):
        print(f"{id} - {list_element}")


def remove_task(task, my_list=None):
    '''
    Remove the task from the my_list, if it exist in.
    '''
    for list_element in (my_list):
        if (task == list_element):
            my_list.remove(task)
            print(f"{task} is succesfully removed.")
            return my_list
    print(f"There is no {task} on the list.") 
    return my_list 

