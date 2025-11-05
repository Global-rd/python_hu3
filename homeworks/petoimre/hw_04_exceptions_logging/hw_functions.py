

def file_open(file_path, m_list=[]):
    '''
    Open the file and the content go to the m_list.
    '''
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            m_list.append(line.strip())


def file_save(file_path, m_list=[]):
    '''
    Write the m_list content to the list, each below.
    '''
    with open(file_path, "w") as file:
        for element in m_list:
            file.write(element+"\n")                                             # \n  = new line


def display_menu():
    """
    Print the menu_list to the consol.
    """
    menu_list = ["Add Task", "View Tasks", "Remowe Task", "Exit"]
    for id, menu_item in enumerate(menu_list, 1):
        print(f"{id}. {menu_item}")            


def add_task(task, my_list=[]):
    '''
    Add the task string to the m_list.
    '''
    list_cnt = len(my_list)
    if list_cnt == 0:
        my_list.append(task)
        print(f"{task} is succesfully added.")
        return
    for list_element in (my_list):
        if (task == list_element):
            print(f"{task} is already exist on the list.")
            return
    my_list.append(task)
    print(f"{task} is succesfully added.")    
            

def wiew_tasks(my_list=[]):
    '''
    Print the my_list to the consol, with enumerate.
    '''
    list_cnt = len(my_list)
    if list_cnt == 0:
        print("The list is empty")
    print("Tasks:")
    for id, list_element in enumerate(my_list, 1):
        print(f"{id} - {list_element}")


def remove_task(task, my_list=[]):
    '''
    Remove the task from the my_list, if it exist in.
    '''
    for list_element in (my_list):
        if (task == list_element):
            my_list.remove(task)
            print(f"{task} is succesfully removed.")
            return
    print(f"There is no {task} on the list.")  

