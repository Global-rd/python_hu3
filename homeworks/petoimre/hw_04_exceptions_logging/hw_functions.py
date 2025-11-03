


def file_open(file_path, m_list=[]):
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            m_list.append(line.strip())
            #print(f"line: {line}")
            #print(f"working: {working_list}")


def file_save(file_path, save_list=[]):
    with open(file_path, "w") as file:
        for element in save_list:
            file.write(element+"\n")     # \n  = new line

def display_menu():
    menu_list = ["Add Task", "View Tasks", "Remowe Task", "Exit"]
    for id, menu_item in enumerate(menu_list, 1):
        print(f"{id}. {menu_item}")            


def List_single_items(my_list=[]):
    return list(set(my_list))
"""
def add_task1111(task, my_list=[]):
    list_cnt = len(my_list)
    if list_cnt >= 1:
        for list_element in (my_list):
            if (task != list_element):
                my_list.append(task)
                print(f"{task} is succesfully added.")
                return my_list
            print(f"{task} is already exist on the list.")
            return my_list
    my_list.append(task)
    print(f"{task} is succesfully added.")
    return my_list  

"""

def add_task(task, my_list=[]):
    list_cnt = len(my_list)
    print(f"cnt: {list_cnt}")
    if list_cnt == 0:
        print(f"cnt==0, cnt:{list_cnt}")
        my_list.append(task)
        print(f"{task} is succesfully added.")
        return my_list
    print(f"cnt>0, cnt:{list_cnt}")
    for list_element in (my_list):
        if (task == list_element):
            print(f"{task} == {list_element}")
            print(f"{task} is already exist on the list.")
            return my_list
    my_list.append(task)
    print(f"{task} is succesfully added.")
    return my_list     
        
    

def wiew_tasks(my_list=[]):
    print("Tasks:")
    for id, list_element in enumerate(my_list, 1):
        print(f"{id} - {list_element}")

def remove_task(task, my_list=[]):
    for list_element in (my_list):
        if (task == list_element):
            my_list.remove(task)
            print(f"{task} is succesfully removed.")
            return my_list
        print(f"There is no {task} on the list.")
        return my_list  


def exit_prog():
    pass





#   user_info["favourite_meals"] = list(set(user_info["favourite_meals"]))