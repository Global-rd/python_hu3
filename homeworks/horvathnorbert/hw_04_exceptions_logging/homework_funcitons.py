import os
from datetime import datetime

def clear_line():
    print("\033[2K", end="")

def cursor_move_to(x, y):
    print(f"\033[{y};{x}H", end="")

def menu_draw(menu_items,menu_item):
        
    if menu_item != None:
        menu_item -= 1
    
    if menu_item == None:
        cursor_move_to(1, 1)
        print(f"------MAIN MENU------")
        for k, v in menu_items.items():
            print(f"   {k}. {v}")
        print(f"---------------------")
    else:
        cursor_move_to(1, 1)
        print(f"------MAIN MENU------")
        for k, v in menu_items.items():
            if menu_item == k-1:
                print(f" ▷ {k}. {v}")
            else:
                print(f"   {k}. {v}")
        print(f"---------------------")

def add_task(tasks,task_description):
    if not tasks:
        last_key = 1
        tasks[last_key] = task_description
    else:
        last_key = list(tasks.keys())[-1]
        tasks[last_key + 1] = task_description
        # return tasks

def read_task(tasks):
    if tasks:
        print("-----------------TASKS------------------")
        for k, v in tasks.items():
            print(f"{k}. {v}")
    else:
        print("There no tasks!")

def remove_task(task_to_delete,tasks):
    del tasks[task_to_delete]


        
        
        
    
    


    
    
        
           







        

    








