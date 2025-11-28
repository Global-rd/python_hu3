import threading
import time


def task1():
    print("Task 1 starting")
    time.sleep(3)
    print("Task 1 finished")

def task2():
    print("Task 2 starting")
    time.sleep(1)
    print("Task 2 finished")

thread_1 = threading.Thread(target=task1)
thread_2 = threading.Thread(target=task2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print("test")