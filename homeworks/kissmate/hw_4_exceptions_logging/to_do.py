import logging
file_handler = logging.FileHandler('to_do.log')
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
my_list =[] 
#add task
def add_task():
    my_list.append(input("Enter a task: "))
#read tasks
def read_tasks():
    return my_list
#write tasks
def tasks_write(tasks):
    my_list.extend(tasks)
#view tasks
def view_tasks():
    for task in my_list:
        print(task)
#remove task
def remove_task():        
    my_list.remove(input("Enter a task to remove: "))
#menu
def display_menu():    
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
#assign user selection
def get_user_selection():
    if selection == "1":
        return add_task()
    elif selection == "2":
        return view_tasks()
    elif selection == "3":
        return remove_task()
    elif selection == "4":
        return exit 
#user inpunt/user mistake handling
while True:
    display_menu()
    break
selection = input("Select an option (1-4): ")
if selection not in ["1", "2", "3", "4"]:
    raise ValueError("Invalid menu selection.")
try:
    result = get_user_selection()  
except ValueError("Please enter a valid option."):
    print("Invalid input. Please enter a number.")
