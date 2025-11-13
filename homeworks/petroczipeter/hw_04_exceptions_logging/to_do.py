import logging
import os
# A Logging beállítás
logger = logging.getLogger()
logger.setLevel(logging.INFO)
# Fájlba logolás
file_handler = logging.FileHandler('to_do.log', mode='a', encoding='utf-8')
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
# A feladatokat a memóriában tároljuk
tasks = []
# Definiálom a függvényeket
def read_tasks(filename="tasks.txt"):
    """Beolvassa a feladatokat a fájlból és feltölti a tasks listát."""
    global tasks
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                tasks = [line.strip() for line in f.readlines() if line.strip()]
            logger.info(f"{len(tasks)} feladat beolvasva a fájlból.")
        except Exception as e:
            logger.error(f"Hiba történt a fájl olvasásakor: {e}")
    else:
        logger.warning("A tasks.txt fájl nem található, üres lista lesz használva.")
        tasks = []
def write_tasks(filename="tasks.txt"):
    """Kiírja a feladatokat a fájlba (felülírja a korábbit)."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task + "\n")
        logger.info("Feladatok sikeresen mentve a fájlba.")
    except Exception as e:
        logger.error(f"Hiba történt a fájl írásakor: {e}")
def display_tasks():
    """Megjeleníti a feladatokat."""
    if not tasks:
        print("Nincs egyetlen feladat sem.")
    else:
        print("\n--- Feladatlista ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    print()
def add_task(task):
    """Új feladat hozzáadása a listához."""
    tasks.append(task)
    logger.info(f"Feladat hozzáadva: {task}")
def remove_task(index):
    """Feladat törlése index alapján."""
    try:
        removed = tasks.pop(index - 1)
        logger.info(f"Feladat törölve: {removed}")
    except IndexError:
        logger.warning("Érvénytelen sorszám, nincs ilyen feladat.")
def display_menu():
    """A menü megjelenítése."""
    print("\n--- To-Do List Menü ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
# Fő program#
def main():
    read_tasks()
    while True:
        display_menu()
        choice = input("Válassz egy opciót (1-4): ").strip()
        if choice not in ("1", "2", "3", "4"):
            print("Érvénytelen választás! Kérlek 1-4 között adj meg számot.\n")
            continue
        if choice == "1":
            task = input("Add meg az új feladatot: ").strip()
            if task:
                add_task(task)
            else:
                print("Üres feladat nem adható hozzá.")
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            display_tasks()
            try:
                index = int(input("Add meg a törlendő feladat sorszámát: "))
                remove_task(index)
                write_tasks() 
            except ValueError:
                print("Kérlek számot adj meg.")            
        elif choice == "4":
            write_tasks()
            print("Kilépés... A feladatok elmentve.")
            logger.info("Program bezárva, feladatok mentve.")
            break
if __name__ == "__main__":
    main()