import logging

FILENAME = "tasks.txt"
logging.basicConfig(filename="task_manager.log",
                    level=logging.INFO,
                    format="%(levelname)s: %(message)s")



def read_tasks(filename):
    tasks = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line != "":
                    tasks.append(line)

        msg = "Olvasva: " + str(len(tasks)) + " feladat"
        print(msg)
        logging.info(msg)
    except FileNotFoundError:
        print("Nincs fájl, üres lista.")
        logging.info("Nincs fájl, üres lista.")
    except Exception as e:
        print("Olvasási hiba:", e)
        logging.error("Olvasási hiba: " + str(e))
    return tasks



def write_tasks(filename, tasks):
    try:
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task + "\n")

        msg = "Mentve: " + str(len(tasks)) + " feladat"
        print(msg)
        logging.info(msg)
    except Exception as e:
        print("Írási hiba:", e)
        logging.error("Írási hiba: " + str(e))




def view_tasks(tasks):
    if len(tasks) == 0:
        print("Nincs feladat.")
        return
    i = 0
    while i < len(tasks):
        print(str(i + 1) + ". " + tasks[i])
        i = i + 1



def add_task(tasks, text):
    text = text.strip()
    if text == "":
        print("Üres nem lehet.")
        return
    tasks.append(text)
    print("Hozzáadva.")
    logging.info("Hozzáadva: " + text)



def remove_task(tasks, index):
    if index < 1 or index > len(tasks):
        print("Érvénytelen sorszám.")
        return
    removed = tasks.pop(index - 1)
    print("Törölve.")
    logging.info("Törölve: " + removed)



def display_menu():
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")



def main():
    tasks = read_tasks(FILENAME)

    while True:
        display_menu()
        choice = input("Opció: ").strip()

        if choice == "1":
            txt = input("Feladat: ")
            add_task(tasks, txt)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            if len(tasks) == 0:
                print("Nincs mit törölni.")
            else:
                view_tasks(tasks)
                s = input("Sorszám: ").strip()
                if s.isdigit():
                    remove_task(tasks, int(s))
                else:
                    print("Szám kell.")

        elif choice == "4":
            write_tasks(FILENAME, tasks)
            print("Viszlát!")
            break

        else:
            print("Csak 1-4.")

if __name__ == "__main__":
    main()

