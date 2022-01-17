import multiprocessing
from functools import reduce


def calculate(file, results):
    with open(file, 'r') as f:
        lines = f.readlines()
        operation = int(lines[0])
        numbers = [float(x) for x in lines[1].split(' ')]
    if operation == 1:
        results.append(reduce(lambda x, y: x + y, numbers))
    elif operation == 2:
        results.append(reduce(lambda x, y: x * y, numbers))
    elif operation == 3:
        results.append(reduce(lambda x, y: x ** 2 + y ** 2, numbers))
    else:
        print(f'Error while processing {file}')


if __name__ == '__main__':
    N = 3
    manager = multiprocessing.Manager()
    return_list = manager.list()
    jobs = []
    for i in range(1, N + 1):
        p = multiprocessing.Process(target=calculate, args=(f'dats/in_{i}.dat', return_list))
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
    print(return_list)
    with open('output.dat', 'w') as f:
        f.write(str(reduce(lambda x, y: x + y, return_list)))
