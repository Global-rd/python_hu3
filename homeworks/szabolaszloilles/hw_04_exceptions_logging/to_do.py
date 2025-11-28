from to_do_functions import (
    display_menu,
    read_tasks,
    write_tasks,
    show_tasks,
    add_task,
    delete_task
)

from logging_config import setup_logging

# Setup logging
setup_logging()

def main():
    tasks = read_tasks()

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter the new task: ").strip()
            if task:
                add_task(tasks, task)
            else:
                print("Cannot add empty task.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            task = input("Enter the task to remove (exact match): ").strip()
            if task:
                delete_task(tasks, task)
            else:
                print("No task entered for deletion.")
        elif choice == "4":
            write_tasks(tasks)
            print("Exiting... Tasks saved.")
            break
        else:
            print("Invalid option! Only 1, 2, 3, or 4 is allowed.")

if __name__ == "__main__":
    main()
