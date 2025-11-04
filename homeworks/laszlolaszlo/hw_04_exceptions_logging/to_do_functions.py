import os


def create_tasks_file(file_path) -> bool:
    """Create tasks file if it does not exists."""
    if not os.path.exists(path=file_path):
        with open(file=file_path, mode="w", encoding="utf-8"):
            return True
    return False


def read_tasks_file(file_path) -> list[str]:
    """Read task file from filesystem and return it as a Python list and create it if it does not exist."""

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
