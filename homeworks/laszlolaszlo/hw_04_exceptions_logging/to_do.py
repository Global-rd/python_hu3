import os
from pathlib import Path
import logging

from logging_config import setup_logging
import to_do_functions as tdf

file_path: Path = (
    Path(os.getcwd())
    / "homeworks"
    / "laszlolaszlo"
    / "hw_04_exceptions_logging"
    / "tasks.txt"
)

print(type(file_path))
setup_logging()
logger: logging.Logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Application started")
    try:
        tasks: list[str] = tdf.read_tasks_file(file_path=file_path)
    except OSError as e:
        # log a warning into log file, need implement later
        tasks = []
        print(f"Program was not able to read tasks file.")
        print("A new, empty list is created in memory.")
        logger.warning(e)

    while True:

        tdf.display_menu()
        # call the real built-in input even if a notebook variable named `input` exists
        user_input: str = input("Please choose a Task (1,2,3,4): ").strip()

        if tdf.check_user_input(user_input=user_input):
            # Add Tasks
            logger.debug(f"Checking user input: {user_input}")

            if user_input == "1":
                print("### Add Task ###")
                logger.debug("Entering 'Add Task\" menu.")

                add_task_input: str = input("Please add a new task: ").strip()

                if tdf.check_add_task_input(add_task_input=add_task_input):
                    logger.debug(f"Checking add_task_input: {add_task_input}")

                    tdf.add_task(task=add_task_input, tasks=tasks)
                    logger.info(f'New task, "{add_task_input}" added successfully.')

                    message = f'New task, "{add_task_input}" added successfully.'
                    print(message)
                    print("-" * len(message))
                else:
                    logger.debug("User add an empty task description.")
                    print("Please give a non empty task description.")

            # View Tasks
            elif user_input == "2":
                print("### View Tasks ###")
                logger.debug("Entering 'View Task' menu.")

                # If the tasks list is empty
                if not len(tasks):
                    print("The Tasks List is empty at now.")
                    print("-------------------------------")
                    logger.debug("The tasks list is empty at now.")
                else:
                    tdf.view_tasks(tasks=tasks)
                    print("-------------------------------")
                    logger.debug(f"tasks list content:")
                    logger.debug(tasks)

            # Remove Task
            elif user_input == "3":
                print("### Remove Tasks ###")
                logger.debug("Entering 'Remove Task' menu.")

                if len(tasks) > 0:
                    print("Current task(s) in the list:")
                    logger.debug(f"tasks list content:")
                    logger.debug(tasks)
                    tdf.view_tasks(tasks=tasks)
                else:
                    print("Current tasks list is empty at now.")
                    print("You are not able to any delete task.")
                    print("------------------------------------")
                    logger.debug("The tasks list is empty at now.")
                    continue

                remove_task_input = input(
                    "Please enter the serial number of the item to be removed: "
                ).strip()
                logger.debug(f"Checking user input: {remove_task_input}")

                if tdf.check_remove_task_input(
                    remove_tasks_input=remove_task_input, tasks=tasks
                ):
                    removed_task = tasks[int(remove_task_input) - 1]
                    tdf.remove_task(
                        remove_tasks_input=int(remove_task_input), tasks=tasks
                    )
                    print(f'Task, "{removed_task}" removed successfully.')
                    logger.debug(f'Task, "{removed_task}" removed successfully.')
                    continue

            # Exit
            # I should use else but for me a new elif is more readable
            elif user_input == "4":
                logger.debug("Entering 'Exit' menu.")
                # print(f"Trying to write out tasks file...")
                try:
                    tdf.write_tasks_file(tasks=tasks, file_path=file_path)
                    print("Tasks file saved successfully.")
                    print("Good bye!")
                    logger.info(f"Tasks file saved successfully.")
                    logger.info(f"Saved file path: {file_path} .")
                    break
                except OSError as e:
                    print(
                        "Some error happened. Please check your filesystem usage or file, directory permission."
                    )
                    print("Please check application log file!")
                    logger.error(e)
                    continue
        else:
            print("Invalid choice!")
            logger.debug(f"Invalid choice: {user_input}")


if __name__ == "__main__":
    main()
