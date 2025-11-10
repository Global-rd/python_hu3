from to_do_functions import *

display_menu()

while True:
    try:
        choice = int(input("Which task would you like to do?")) 
        if choice in [1,2,3,4]:
            break
        else:
            print("Please give the number of the task between 1 and 4.")
    except ValueError:
        print("Please give the number of the task.")

if choice == 1:
    new_task = input("What task would you like to add?")
    add_task(new_task)

elif choice == 2:
    display_tasks()

elif choice == 3:
    remove_task()

else :
    exit()