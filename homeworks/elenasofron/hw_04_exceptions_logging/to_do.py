tasks = []
#tasks = ["to eat", "to sleep", "to drink"]

def read_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:                
                    tasks.append(line)

    except FileNotFoundError:
        print("The task file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return tasks

def write_tasks(tasks, filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task + "\n")

    except FileNotFoundError:
        print("Error: The file path does not exist.")

    except PermissionError:
        print("Error: Cannot write to the file (permission denied).")

    except Exception as e:
        print(f"Unexpected error while writing tasks: {e}")    

def show_tasks():
    if not tasks:
        print("No tasks in the list")
    else:
        print("To-Do List:")
        for idx, task in enumerate(tasks, start=0):
            print(f"{idx+1}: {tasks[idx]}")
            

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")
    return tasks

def remove_task():
    task_to_remove = input("Enter the task to remove: ")

    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        print(f"Task '{task_to_remove}' removed.")
    else:
        print("Task not found in the list.")
    return tasks

def display_menu():
    print("What do you want to do? Please select the number: ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def get_user_response():
    if response == "1":
        return add_task()
    elif response == "2":
        return show_tasks()
    elif response == "3":
        return remove_task()
    elif response == "4":
        print ("Exit")
        #break

while True:
    display_menu()
    response = input("Select one option (1-4):")
    if response not in ["1", "2", "3", "4"]:
        print("Give a valid number (between 1 and 4)")
    elif response == "1":
        add_task()
    elif response == "2":
        show_tasks()
    elif response == "3":
        remove_task()
    elif response == "4":
        print("Exiting the program. Good bye")
        break