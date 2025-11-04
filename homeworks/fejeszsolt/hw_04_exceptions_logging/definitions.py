import logging
import os

def read_menu():
    print (
    """
       1. Add Task
       2. View Tasks
       3. Remove Task
       4. Exit
       """
       )
    logging.info("menü kijelezve")

def chekk_submenu(submenu):
    if not isinstance(submenu, int):
        logging.warning(f"HIBÁS TÍPUS: A bemenet ('{submenu}') nem szám, számot adj meg.")
        return False 
    if submenu not in [1, 2, 3, 4]:
        logging.warning(f"HIBÁS ÉRTÉK: 1,2,3,4 közül válassz!")
        return False 
    return True

def read_file(file_path):
    """file olvasása
lista készítése"""
    try:
        with open(file_path, "r") as file:
            todo_list = [line.strip() for line in file]
    except Exception as e:
        logging.error(f"Hiba: nincs ilyen fájl, vagy nincs hozzá jogosúltságod {e}.")
    logging.info("sikeres beolvasás")
    if not todo_list:
            logging.warning("A fájl sikeresen beolvasva, de még üres.")
    return todo_list


def view_tasks(todo_list):
    """lista printelése"""
    for line in todo_list:
        print(line)
    if not todo_list:
        logging.info("A lista még üres")
    logging.info("Lista megjelenítése befejeződött")


def add_task(newtask, todo_list):
    """új feladat hozzáadása a listához"""
    todo_list.append(newtask)
    logging.info("a feladat sikeresen hozzáadva")
    return todo_list
    


def remove_task(extask, todo_list):
    """feladat törlése"""
    try:
        todo_list.remove(extask)
        logging.info(f"Sikeresen törölted: '{extask}'")
    except ValueError:
        logging.warning(f"HIBA: Az '{extask}' feladat nincs alistában, nézdd meg ne e írtál el valamit.")
    return todo_list


def write_task(todo_list, file_path):
    """Feladatok kiírása, miután a fájlt teljesen kiürítettük"""
    with open(file_path, "w") as file:
        for line in todo_list:
            file.write(line + "\n")
    logging.info("a fájl írása sikeresen megtörtént.")