import threading
from functools import reduce

results = []


def calculate(file):
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


N = 3
for i in range(1, N + 1):
    threading.Thread(target=calculate, args=[f'dats/in_{i}.dat']).run()
print(results)
with open('output.dat', 'w') as f:
    f.write(str(reduce(lambda x, y: x + y, results)))
