# to_do_functions.py

import os
import logging

logger = logging.getLogger(__name__)


def read_tasks():
    """Read tasks from tasks.txt and return them as a list."""
    tasks = []
    if os.path.exists("tasks.txt"):
        try:
            with open("tasks.txt", "r", encoding="utf-8") as f:
                for line in f:
                    task = line.strip()
                    if task:
                        tasks.append(task)
            logger.info("Tasks successfully loaded.")
        except Exception as e:
            logger.error(f"Error while reading file: {e}")
    else:
        logger.info("tasks.txt does not exist, starting with an empty task list.")
    return tasks


def write_tasks(tasks):
    """Write the current list of tasks to tasks.txt."""
    try:
        with open("tasks.txt", "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task + "\n")
        logger.info("Tasks successfully saved.")
    except Exception as e:
        logger.error(f"Error while writing file: {e}")


def show_tasks(tasks):
    """Print all tasks to the console."""
    if tasks:
        print("\n--- Tasks ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks available.")
    logger.info("Task list displayed.")


def add_task(tasks, task):
    """Add a new task to the list."""
    tasks.append(task)
    logger.info(f"Task added: {task}")


def delete_task(tasks, task):
    """Remove a task from the list if it exists."""
    if task in tasks:
        tasks.remove(task)
        logger.info(f"Task removed: {task}")
    else:
        logger.warning(f"Task not found: {task}")


def display_menu():
    """Show available menu options."""
    print("\n--- Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
