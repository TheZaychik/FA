from random import randint
import time


def time_test(func):
    def wrapper(list):
        t1 = time.time()
        func(list)
        t2 = time.time()
        print(t2 - t1)

    return wrapper


@time_test
def bubble_sort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


@time_test
def cocktail_sort(a):
    up = range(len(a) - 1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if a[i] > a[i + 1]:
                    a[i], a[i + 1] = a[i + 1], a[i]
                    swapped = True
            if not swapped:
                return a


n1 = 10
n2 = 10
d1 = []
d2 = []
for i in range(n1):
    d1.append(randint(1, 99))
for i in range(n2):
    d2.append(randint(1, 99))

bubble_sort(d1)
cocktail_sort(d2)


