from datetime import datetime
import os
import homework_funcitons as hf
import logging
from pathlib import Path

menu_items = {1: "Add Task",
              2: "View Tasks",
              3: "Remove Task",
              4: "Exit"}

menu_choice = None
task_description = None
task_to_delete = None
tasks = {}
current_dir = Path(__file__).resolve().parent
file_path = current_dir / "tasks.txt"

file_handler = logging.FileHandler(current_dir / "logs.txt")
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
stream_handler.setLevel(logging.ERROR)
logger = logging.getLogger()
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

logger.debug("Application started")

os.system('cls' if os.name == 'nt' else 'clear')

try:
  with open (file_path, "r") as file:
    for i, line in enumerate(file, start=1):
      tasks[i] = line.strip()
    logger.debug(f"{file} File opened, tasks loaded.")
except:
  with open (file_path, "w") as file:
     pass
  logger.debug(f"{file} not exist, {file} created.")

hf.menu_draw(menu_items,menu_choice)

while True:
    hf.cursor_move_to(1, 7)
    hf.clear_line()
    
    try:
      menu_choice = int(input("Pls choose from the menu!: "))
      if menu_choice < 1 or menu_choice > 4:
        raise ValueError()
    except Exception as e:
      logger.error(f"{e} Not acceptable value for 'menu_choice'")
      
    
    if menu_choice == 4:
      os.system('cls' if os.name == 'nt' else 'clear')
      hf.menu_draw(menu_items,menu_choice)
      break
    elif menu_choice == 3:
      hf.menu_draw(menu_items,menu_choice)
      hf.cursor_move_to(1,7)
      logger.debug("User entered 'Remove Task' menu.")
      task_to_delete = int(input("Which task number would you like to delete: ?"))
      if task_to_delete in tasks:
        hf.remove_task(task_to_delete,tasks)
        logger.debug(f"User deleted the {task_to_delete}. task.")
        os.system('cls' if os.name == 'nt' else 'clear')
      else:
        logger.error("User trying to delete a task what not exist.")
        os.system('cls' if os.name == 'nt' else 'clear')

    elif menu_choice == 2:
        hf.menu_draw(menu_items,menu_choice) 
        hf.cursor_move_to(1, 9)
        logger.debug("User entered 'View Tasks' menu.")
        hf.read_task(tasks)
                

    elif menu_choice == 1:
        hf.menu_draw(menu_items,menu_choice)
        hf.cursor_move_to(1, 7)
        logger.debug("User entered 'Add Task' menu.")
        hf.clear_line()
                
        task_description = str(input("Pls Describe your task!: "))
        if len(task_description) == 0 or len(task_description) > 40:
          logger.error("User trying to add a task what to long or to short.")
          hf.cursor_move_to(1, 7)
        else:
          hf.add_task(tasks,task_description)
          logger.debug(f"User added a task. {task_description}")
          

        
    hf.menu_draw(menu_items,None)

with open(file_path, "w") as file:
  for k, v in tasks.items():
    file.write(f"{v}\n")
  
logger.debug("Application terminated")
