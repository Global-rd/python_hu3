from logging_config import setup_logging
import logging
from to_do import display_menu, task_add, task_show, task_read, task_del,task_write, to_do

setup_logging()
logger = logging.getLogger(__name__)


def main():
    logger.info("Application started")
    logger.debug("Debug info here")
    task_read()

    while True:
        
        try:
            display_menu()
            valasz = int(input("Please select the menu number(1,2,3,4): "))
        except ValueError:
            print("Please enter a valid number!")
            continue
        except ZeroDivisionError as e:
            logger.exception(f"An error occured: {e}")

        if valasz == 1:
            task_add()
        elif valasz == 2:
            task_show()
        elif valasz == 3:
            task_del()
        elif valasz == 4:
            logger.info("Exit, save tasks...")
            print(to_do)
            task_write(to_do)
            print("Bye!")
            break
        else:
            print("Invalid selection, please select a number between 1 and 4!")
    

if __name__ == "__main__":
    main()