import time

heap_var = 1

def task1():
    stack_var = 2
    print(stack_var)
    print(heap_var)
    print("Task 1 starting")
    time.sleep(3)
    print("Task 1 finished")

def task2():
    stack_var = 2
    print(stack_var)
    print(heap_var)
    print("Task 2 starting")
    time.sleep(3)
    print("Task 2 finished")



#running on a single thread
task1()
task2()