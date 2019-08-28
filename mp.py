import multiprocessing as mp
import time

THREADS=10

def f(x):
    print("Starting...." + str(x))
    time.sleep(5)
    print("Finishing...."+ str(x))

processes = [None] * THREADS
print(processes)

def add_to_processes(args):
    while True:
        for idx, process in enumerate(processes):
            if process is None or not process.is_alive():
                p = mp.Process(target=f, args=args)
                processes[idx] = p
                p.start()
                return

for i in range(0, 30):
    add_to_processes((i,))
