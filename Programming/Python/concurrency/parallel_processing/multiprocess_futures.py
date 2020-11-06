#  need python 3.2 or above; better way for paralle
import concurrent.futures
import multiprocessing
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

if __name__ == '__main__':
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        # use map function
        results = executor.map(do_something, secs)
        # loop over results
        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')