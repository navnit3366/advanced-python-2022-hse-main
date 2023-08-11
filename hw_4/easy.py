import concurrent
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Process
from threading import Thread

NUMBER = 30000
ITERATIONS = 10


def fib_numbers(n):
    res = [1, 1]
    fib_num1 = fib_num2 = 1
    for i in range(2, n):
        fib_num3 = fib_num1 + fib_num2
        fib_num1 = fib_num2
        fib_num2 = fib_num3
        res.append(fib_num2)
    return res


def execute_sync_task():
    fst_timestamp = time.time()
    for _ in range(ITERATIONS):
        fib_numbers(NUMBER)
    snd_timestamp = time.time()
    return fst_timestamp, snd_timestamp


def execute_tasks(input_list):
    fst_timestamp = time.time()
    for el in input_list:
        el.start()
    for el in input_list:
        el.join()
    snd_timestamp = time.time()
    return fst_timestamp, snd_timestamp


if __name__ == '__main__':
    with open("artifacts/easy.txt", "w") as file:
        start, end = execute_sync_task()
        file.write("Synchronous: " + str(end - start) + " sec\n\n")
        threads = [Thread(target=fib_numbers, args=(NUMBER,)) for _ in range(ITERATIONS)]
        start, end = execute_tasks(threads)
        file.write("Threading: " + str(end - start) + " sec\n\n")
        processes = [Process(target=fib_numbers, args=(NUMBER,)) for _ in range(ITERATIONS)]
        start, end = execute_tasks(processes)
        file.write("Multiprocessing: " + str(end - start) + " sec\n\n")
