from logging_config import setup_logging
from pathlib import Path
import logging
import os

setup_logging()
logger = logging.getLogger(__name__)

TASKS_FILE = Path("homeworks") / "pappildiko" / "hw_04_exceptions_logging"/"tasks.txt"


def read_tasks() -> list[str]:
    """Reads the tasks from a file. Returns an empty list if the file doesn't exist."""
    
    tasks = []

    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r", encoding="utf-8") as file:
                tasks = [line.strip() for line in file.readlines() if line.strip()]
            logger.info("Tasks loaded successfully.")
        except Exception as e:
            logger.exception(f"Error reading file: {e}")
    else:
        logger.warning("No existing tasks file found. Starting with an empty list.")
    return tasks



def write_tasks(tasks: list[str]) -> None:
    """Writes tasks to the file (overwrites the existing one)"""
    try:
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(task + "\n")
        logger.info("Tasks successfully saved to file.")
    except Exception as e:
        logger.exception(f"Error writing file: {e}")


def display_tasks(tasks: list[str]) -> None:
    """Displays tasks on the console."""
    if not tasks:
        print("No tasks available.")
        logger.info("Displayed empty task list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print()
        logger.info("Tasks displayed successfully.")



def add_task(tasks: list[str], new_task: str) -> None:
    """Adds new task to current list"""
    tasks.append(new_task)
    logger.info(f"Task added: '{new_task}'")



def remove_task(tasks: list[str], index: int) -> None:
    """Removes a task by index (1-based). Handles invalid or negative input safely."""
    if index < 1 or index > len(tasks):
        print("Invalid task number. Please enter a number between 1 and", len(tasks))
        logger.warning(f"Invalid task number entered for removal: {index}")
        return

    removed = tasks.pop(index - 1)
    print(f"Removed task: '{removed}'")
    logger.info(f"Task removed: '{removed}'")


def display_menu() -> None:
    """Displays menu options"""
    print("\nPlease select an option from the menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")



def main():
    tasks = read_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            logger.warning(f"Invalid menu input: {choice}")
            continue

        if choice == "1":
            new_task = input("Enter the new task: ").strip()
            if new_task:
                add_task(tasks, new_task)
            else:
                print("Task cannot be empty.")
                logger.warning("Attempted to add an empty task.")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            if not tasks:
                continue
            try:
                num = int(input("Enter the number of the task to remove: "))
                remove_task(tasks, num)
            except ValueError:
                print("Please enter a valid number.")
                logger.warning("Invalid number entered for removal.")

        elif choice == "4":
            write_tasks(tasks)
            print("Exiting program. Goodbye!")
            logger.info("Program exited and tasks saved.")
            break


if __name__ == "__main__":
    main()
