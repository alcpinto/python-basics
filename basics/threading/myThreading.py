import threading
from queue import Queue
import time

print_lock = threading.Lock()


def exampleJob(task):
    time.sleep(0.5)

    with print_lock:
        print(threading.current_thread().name, task)


def threader():
    while True:
        w = q.get()
        exampleJob(w)
        q.task_done()


q = Queue()

for worker in range(10):
    t = threading.Thread(target=threader)
    t.daemon = True # dies when main thread dies
    t.start()


start = time.time()


for task in range(20):
    q.put(task)


q.join() # main thread waits until all tasks in queue finishes

print('Entire time took:', time.time()-start)
