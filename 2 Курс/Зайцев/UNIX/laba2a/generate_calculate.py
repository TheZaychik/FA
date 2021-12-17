import multiprocessing
import sys
import threading
import time
import os

import matrix_dot

queue = multiprocessing.Queue()
is_working = multiprocessing.Event()


def parallel_gen(size):
    while is_working.is_set():
        queue.put(matrix_dot.random_fill(size, size))


def parallel_calc():
    while is_working.is_set():
        if queue.qsize() > 1:
            m1 = queue.get()
            m2 = queue.get()
            matrix_dot.parallel_calc(m1, m2, matrix_dot.write_locking)


def parallel():
    with multiprocessing.Pool() as pool:
        while is_working.is_set():
            a = queue.get()
            b = queue.get()
            n = matrix_dot.SIZE
            args = [(a, b, (i, j), matrix_dot.write_locking) for i in range(n) for j in range(n)]
            pool.starmap(matrix_dot.single_dot, args)

    pool.join()


def console():
    while is_working.is_set():
        cmd = input(">>> ")
        if cmd.lower() == "exit":
            is_working.clear()
            os._exit(0)


if __name__ == '__main__':
    is_working.set()
    threading.Thread(target=parallel_gen, args=(matrix_dot.SIZE,)).start()
    threading.Thread(target=parallel_calc).start()
    console()
