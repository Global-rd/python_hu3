import logging

# Set up logging to both console and file
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("task_manager.log"),
        logging.StreamHandler()
    ]
)

TASK_FILE = "tasks.txt"
tasks = []

# Read tasks from file
def read_tasks():
    global tasks
    try:
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        logging.info("Tasks successfully loaded from file.")
    except FileNotFoundError:
        logging.warning("Task file not found. A new file will be created.")
        tasks = []
    except Exception as e:
        logging.error(f"Error while reading file: {e}")

# Write tasks to file
def write_tasks():
    try:
        with open(TASK_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        logging.info("Tasks successfully saved to file.")
    except Exception as e:
        logging.error(f"Error while writing to file: {e}")

# Display all tasks
def display_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    logging.info("Tasks displayed.")

# Add a new task
def add_task(task):
    tasks.append(task)
    logging.info(f"Task added: {task}")

# Remove a task by index
def remove_task(index):
    try:
        removed = tasks.pop(index - 1)
        logging.info(f"Task removed: {removed}")
    except IndexError:
        logging.warning("Invalid index. No task removed.")

# Show menu options
def display_menu():
    print("\n--- Task Manager Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

# Main program loop
def main():
    read_tasks()
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            task = input("Enter the new task: ").strip()
            if task:
                add_task(task)
            else:
                print("Empty task cannot be added.")
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            display_tasks()
            try:
                index = int(input("Enter the task number to remove: "))
                remove_task(index)
            except ValueError:
                print("Invalid number format.")
        elif choice == "4":
            write_tasks()
            print("Exit. Tasks saved.")
            break
        else:
            print("Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()