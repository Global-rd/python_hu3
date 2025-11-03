"""
1. Elindul a program
2. Beolvassa a tasks.txt-ből a feladatokat
    - Ha nincs még tasks.txt, nem adunk hibát, létrehozom
    - Ha nem üres a taskst.txt beolvassuk azt egy tasks list-be
3. Megjelenik a Menü a terminálon, az opciók közül lehet választani
4. Felhasználó választ, megtörténik a kiválasztott feladat elvégzése
    - Ha üres a tasks list, akkor a View Tasks opciónál kiírjuk, hogy még nincs rögzített feladat
3-4 ismétlődik, amíg a Menüből nem az Exit kerül kiválasztásra
Exit kiválasztás után, a feladatok kiíródnak a tasks.txt file-ba, felülírva a tartalmát.
"""

import os
from pathlib import Path

file_path = (
    Path(os.getcwd())
    / "homeworks"
    / "laszlolaszlo"
    / "hw_04_exceptions_logging"
    / "tasks.txt"
)


def create_tasks_file(file_path) -> bool:
    """Create tasks file if it does not exists."""
    if not os.path.exists(path=file_path):
        with open(file=file_path, mode="w", encoding="utf-8"):
            return True
    return False


def read_tasks_file(file_path) -> list[str]:
    """Read task file from filesystem and return it as a Python list and create it if does not exists."""

    if not os.path.exists(path=file_path):
        create_tasks_file(file_path=file_path)

    with open(file=file_path, mode="r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file]
        return tasks


def write_tasks_file(tasks, file_path) -> None:
    """Write tasks from memory into task file"""
    with open(file=file_path, mode="w", encoding="utf-8") as file:
        formatted_tasks = "\n".join(tasks)
        file.write(formatted_tasks)


def view_tasks(tasks: list[str]) -> None:
    # Use list comprehension and ennumarate to display tasks with index+1 for human eyes
    # Index start from zero in lists.
    # [print(f"{i+1}: {x}") for i, x in enumerate(tasks)]

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def remove_task(remove_tasks_input: int, tasks: list[str]) -> None:
    """Remove the specified task"""
    tasks.pop(remove_tasks_input - 1)


def add_task(task, tasks: list[str]) -> None:
    """Append a task into the tasks list"""
    if len(task) != 0:
        tasks.append(task)
        return


def display_menu() -> None:
    print("########")
    print("# MENU #")
    print("########")
    print("Choose a Task:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def check_user_input(user_input: str) -> bool:
    """Check user input. Return True if valid or False when invalid."""
    VALID_INPUTS: list[str] = ["1", "2", "3", "4"]
    if user_input in VALID_INPUTS:
        # Log validation result
        return True
    # Raise error, log error
    return False


def check_remove_task_input(remove_tasks_input: str, tasks: list[str]) -> bool:
    """Check user input about Tasks list index. Return True if valid or False when invalid."""
    if not remove_tasks_input.isdigit():
        print("Please add a numeric value.")
        return False
    maximum_index: int = len(tasks)
    if 0 < int(remove_tasks_input) <= maximum_index:
        return True
    else:
        print(f"Your choice {remove_tasks_input} is not in the list.")
        print(f"Please give a valid choice: 1 - {maximum_index}")
        return False


def check_add_task_input(add_task_input: str) -> bool:
    """Check if users Add Task input is valid"""
    if add_task_input:
        return True
    return False


def main() -> None:

    try:
        tasks: list[str] = read_tasks_file(file_path=file_path)
    except OSError:
        # log a warning into log file, need implement later
        tasks = []
        print(f"Program was not able to read tasks file.")
        print("A new, empty list is created in memory.")

    while True:

        display_menu()
        # call the real built-in input even if a notebook variable named `input` exists
        user_input: str = input("Please choose a Task (1,2,3,4): ").strip()

        if check_user_input(user_input=user_input):
            # Add Tasks
            if user_input == "1":
                print("### Add Tasks ###")
                add_task_input: str = input("Please add a new task: ").strip()
                if check_add_task_input(add_task_input=add_task_input):
                    add_task(task=add_task_input, tasks=tasks)
                    print(f'New task, "{add_task_input}" added succesfully.')
                    add_task_input_length = len(add_task_input)
                    # Print as many - as new task and the other part of the message length.
                    # Little be ugly solution, not so Pythonic.
                    print((add_task_input_length + 31) * "-")
                else:
                    print("Please give a non empty task description.")

            # View Tasks
            elif user_input == "2":
                print("### View Tasks ###")

                # If the tasks list is empty
                if not len(tasks):
                    print("The Tasks List is empty at now.")
                    print("-------------------------------")
                else:
                    view_tasks(tasks=tasks)
                    print("-------------------------------")

            # Remove Task
            elif user_input == "3":
                print("### Remove Tasks ###")

                if len(tasks) > 0:
                    print("Current task(s) in the list:")
                    view_tasks(tasks=tasks)
                else:
                    print("Current tasks list is empty at now.")
                    print("You are not able to any delete task.")
                    print("------------------------------------")
                    continue
                remove_task_input = input(
                    "Please enter the serial number of the item to be removed: "
                ).strip()
                if check_remove_task_input(
                    remove_tasks_input=remove_task_input, tasks=tasks
                ):
                    removed_task = tasks[int(remove_task_input) - 1]
                    remove_task(remove_tasks_input=int(remove_task_input), tasks=tasks)
                    print(f'Task, "{removed_task}" removed succesfully.')
                    continue

            # Exit
            # I should use else but for me a new elif is more readable
            elif user_input == "4":
                # print(f"Trying to write out tasks file...")
                try:
                    write_tasks_file(tasks=tasks, file_path=file_path)
                    print("Tasks file saved succesfully.")
                    print("Good bye!")
                    break
                except OSError as e:
                    # log e into log file
                    # need implement

                    print(
                        f"Some error happened. Please check your filesystem usage or file, directory permission."
                    )
                    continue
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
