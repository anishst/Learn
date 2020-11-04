# https://pymotw.com/2/multiprocessing/basics.html
import multiprocessing
import time

import multiprocessing
import time
import sys

def daemon():
    print('Starting:', multiprocessing.current_process().name)
    time.sleep(2)
    print('Exiting :', multiprocessing.current_process().name)

def non_daemon():
    print('Starting:', multiprocessing.current_process().name)
    print('Exiting :', multiprocessing.current_process().name)

if __name__ == '__main__':
    start = time.perf_counter()

    d = multiprocessing.Process(name='process_video', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='process_audio', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
    # script will wait until processes are finished before moving on
    d.join()
    n.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')