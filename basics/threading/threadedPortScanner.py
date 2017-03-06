import threading
from queue import Queue
import socket

print_lock = threading.Lock()
target = 'pythonprogramming.net'


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('Port', port, 'is open!')

        con.close()
    except:
        pass


def threader():
    while True:
        port = q.get()
        portscan(port)
        q.task_done()


q = Queue()

for worker in range(100):
    t = threading.Thread(target=threader)
    # dies when main thread dies
    t.daemon = True
    t.start()


for port in range(1, 10000):
    q.put(port)


# main thread waits until all tasks in queue finishes
q.join()

print('End...')
