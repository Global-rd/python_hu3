from concurrent.futures import ThreadPoolExecutor
import time

def task(name, duration):
    print(f"Task {name} starting...")
    time.sleep(duration)
    print(f"Task {name} finished...")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(task, "A", 3)
    executor.submit(task, "B", 2)
    executor.submit(task, "C", 1)
    executor.submit(task, "D", 2)
    executor.submit(task, "E", 1)
    executor.submit(task, "F", 3)
    executor.submit(task, "G", 1)



