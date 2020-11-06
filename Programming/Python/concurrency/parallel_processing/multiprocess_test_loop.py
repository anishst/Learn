# https://pymotw.com/2/multiprocessing/basics.html
import multiprocessing
import time

import multiprocessing
import time
import sys

def do_something(seconds):
    print('Starting:', multiprocessing.current_process().name)
    print(f"sleeping for {seconds} seconds...")
    time.sleep(seconds)
    print('Exiting :', multiprocessing.current_process().name)

if __name__ == '__main__':
    start = time.perf_counter()

    processes = []
    for _ in range(5):
        p = multiprocessing.Process(name='do_something', target=do_something, args=[1.5])
        p.start()
        processes.append(p)
    # wait for processes to complete
    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')