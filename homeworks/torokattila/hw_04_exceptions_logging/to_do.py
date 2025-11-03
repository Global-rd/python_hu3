# Functions declaration
def read_task():
    pass
def write_task():
    pass
def display_task(task_list):
    print("Tasks list:")
    for task in task_list:
        print(task)
    

def add_task(task_list, name:str):
    task = name
    task_list.append(task)

def remove_task(task_list, name:str):
    for task in task_list:
        if task == name:
            task_list.remove(task)
            return

def display_menu():
    pass

def main():
    task_list = []
    add_task(task_list, "Ebéd")
    add_task(task_list, "Uzsi")
    add_task(task_list, "Vacsora")
    #add_task(task_list, "Ebéd")
    remove_task(task_list, "Ebéd")
    
    display_task(task_list)

main()
