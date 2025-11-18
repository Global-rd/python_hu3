def read_tasks():
    tasks = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:                # skip empty lines
                    tasks.append(line)

    except FileNotFoundError:
        print("The task file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

    return tasks

def write_tasks():
    try:
        existing_tasks = read_tasks()
    except FileNotFoundError:
        existing_tasks = []
    with open(file_path, 'a') as f:
        for task in tasks:
            f.write(task + '\n')
    global my_list
    my_list = read_tasks()

def show_tasks():
    my_list = read_tasks()
    if not my_list:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for idx, task in enumerate(my_list, start=1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter a new task: ")
    write_tasks(task):
    logger.info(f"Task '{task}' added to the list.")

def remove_task():
    task_to_remove = input("Enter the task to remove: ")
    my_list = read_tasks()
    if task_to_remove in my_list:
        my_list.remove(task_to_remove)
        with open(file_path, 'w') as f:
            for task in my_list:
                f.write(task + '\n')
    else:
        print("Task not found in the list.")

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
        print("Give a valid number")
    elif get_user_response()