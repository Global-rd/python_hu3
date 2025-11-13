"""Hozz létre egy új mappát a neveddel ellátott mappán belül 
“hw_04_exceptions_logging” néven. A következő feladatokhoz tartozó 
.py fi le-okat ide mentsd el.
Feladat:
Hozz létre egy to_do.py nevű fi le-t, és kódold le a következő feladat 
megoldását:
Készíts egy Feladatkezelő alkalmazást!
● Definiálj 5 függvényt a következőkre: 
feladatok olvasása, 
feladatok írása, 
feladatok megjelenítése,
egy feladat hozzáadása, 
egy feladat törlése

● Legyen egy display_menu() function-öd is, ami kiprinteli a lehetséges 
opciókat:
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Folyamatosan kérj be inputot a felhasználótól hogy ezek közül a menüpontok
közül mit szeretne csinálni, és hívd meg a válaszhoz megfelelő függvényt.
A felhasználó inputja 1,2,3 vagy 4 kell, hogy legyen, ellenőrizd! Ha az 1-es
vagy 3-as opciót választja, mindkét esetben paramétert kell átadnod a
megfelelő függvénynek. “Exit”-re lépjen ki a programból.
Használj hibakezelést a file-ba való íráskor és olvasáskor, illetve használd
a logging module-t. Egyszerre logolj a konzolra és egy .log file-ba. A .txt
file legyen része a pull request-nek. Tipp: A program futása során a
feladatokat memóriában (egy listában) tartsd nyilván (itt adj hozzá vagy
törölj elemeket a function hívásoknál).
A file-ból való olvasás automatikusan történjen meg a program indulásakor.
A fájlba írás csak a program befejezésekor (“Exit” opció választásakor) történjen meg,
ekkor a program írja felül a korábbi feladatlistát a módosított
tartalommal (nem kell minden Add Task vagy Remove Task opciónál módosítani a
file-t)."""

#imports

import hw_04_functions as fun
from pathlib import Path
from logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

# main line
def main():

    # init

    list_of_menu = ["Add Task","View Tasks","Remove Task","Exit"]
    file_path = Path("homeworks") / "rederkonstantin" / "hw_04_exceptions_logging" / "task_file.txt" #relative path
    to_do_list = list()

    # read todo activities from file to variable(list)
    to_do_list = fun.read_tasks(file_path)

    # print current tasks to display for start
    print("")
    fun.view_tasks(to_do_list)
    
    # start of main cycle
    while True:

        print("")
        fun.display_menu(list_of_menu)
        print("")

        chose = int(input("What would you like to do? (1-4)"))
        try:
            fun.chosen_check(chose)
        except ValueError as e:
            logger.exception(f"ValueError: {e}")
            continue

        if chose == 1:
            print("Menu 1 has choosen.")
            try:
                fun.add_task(to_do_list)
            except ValueError as e:
                logger.exception(f"ValueError: {e}")

        elif chose == 2:
            try:
                fun.view_tasks(to_do_list)
            except ValueError as e:
                logger.exception(f"ValueError: {e}")

        elif chose == 3:
            try:
                fun.remove_task(to_do_list)
            except ValueError as e:
                logger.exception(f"ValueError: {e}")

        elif chose == 4:
            try:
                fun.exit(file_path, to_do_list)
            except ValueError as e:
                logger.exception(f"ValueError: {e}")
            
            break

main()