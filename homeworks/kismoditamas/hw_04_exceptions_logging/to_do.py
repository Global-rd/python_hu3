from logging_config import setup_logging
import logging
from pathlib import Path

setup_logging()
logger = logging.getLogger(__name__)


file_path = Path("homeworks") / "kismoditamas" /  "hw_04_exceptions_logging" / "tasks.txt" 

def import_tasks(tasks):
    '''Import tasks from file'''    
    try:
        with open(file_path, "r") as file:
            for line in file.readlines():
                add_task(tasks, line.strip())
        print(f"The tasks have been imported from the file ({file_path})")
        logger.info(f"The tasks have been imported from the file ({file_path})")
    except FileNotFoundError as e:
        print(f"No file found to import ({file_path})")
        logger.debug(f"No file found to import ({file_path})")
    except Exception:
        logger.exception(f"Unexpected err while reading tasks file ({file_path})")
        raise

def write_tasks(tasks):
    '''Writing tasks to file'''
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(f"{task}\n")
        logger.info(f"The tasks have been written to file ({file_path})")
    except OSError as e:
        logger.error(f"Write to ({file_path}) failed: {e}")
        raise
    except Exception:        
        logger.exception(f"Unexpected error while writing tasks file ({file_path})" )    
        raise

def view_tasks(tasks):
    '''Print to consol the tasks lists items'''
    print("Task list items:" )
    for id, task in enumerate(tasks,1):          
        print (f"{id}. {task}")
    logger.debug("Tasks listed")

def add_task(tasks, task_name):
    '''Add a item to tasks list'''
    tasks.append(task_name)
    print (f"'{task_name}' task added to tasklist.")
    logger.debug(f"Task added ({task_name})")

def remove_task(tasks, task_index):
    '''Remove a item from tasks list'''
    task_name = tasks.pop(task_index)
    print (f"'{task_name}' task removed from tasklist.")    
    logger.debug(f"Task removed ({task_name})")

def display_menu(tasks):
    '''Displaying options for the user (Add task, View task, Remove task, Exit)'''        
    while True:
        try:
            print("____________________________________________________________________________________")
            result = int( input("Choose from the options [ 1. Add task - 2. View task - 3. Remove task - 4. Exit ]: "))
            if result==1:
                task_name = input("Enter the name of the task: ")                            
                logger.debug(f"Correct user action (Option: {result}, Task name: {task_name})")                
                return (result, task_name)         
            elif result == 3:
                while True:
                    try:
                        task_index = int(input("Enter the index of the task: "))
                        if task_index > 0 and task_index <= len(tasks):                            
                            logger.debug(f"Correct user action (Task index: {task_index})")                
                            return (result, task_index-1)         
                        print(f"Enter a number between 1 and {len(tasks)}")                                
                    except ValueError as e:
                        print(f"Enter a number between 1 and {len(tasks)}")
                
            elif result==2 or result == 4:
                logger.debug(f"Correct user action (Option: {result})")                                
                return (result, None)
            else:
                print ("Please give me a number between 1 and 4.")
                logger.debug(f"Incorrect user action (Input: {result})")          
        except ValueError as e:            
            print ("Please give me a number between 1 and 4.")  
            logger.debug(f"Incorrect user action (Input: {result})")          
    
def main():
    logger.info("Application started")    
    tasks = []
    try:    
        import_tasks(tasks)
    except Exception:
        logger.debug(f"Import failed ({file_path})")

    while True:
        result, task_name = display_menu(tasks)
        if result ==1:
            add_task(tasks,task_name)
        elif result==2:
            view_tasks(tasks)
        elif result==3:
            remove_task(tasks, task_name)
        elif result==4:
            try:
                write_tasks(tasks)          
                logger.info("Application treminated")
            except Exception:
                logger.exception(f"Save failed ({file_path})")    
            break

if __name__=="__main__":
    main()
