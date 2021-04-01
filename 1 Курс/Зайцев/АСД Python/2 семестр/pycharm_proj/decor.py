headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}


def decorator_function(func):
    def wrapper():
        print('Функция обертка!')
        func()
        print('Конец декоратора!')

    return wrapper


@decorator_function
def hello_world():
    print('Hello World!')


def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        returned = func(*args, **kwargs)
        end = time.time()
        print(f'Врремя выполнения : [{end - start}] секнуд')
        return returned

    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url, headers=headers)
    print(webpage.status_code)
    return webpage.text


def benchmark1(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] Remained time {}'.format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


@benchmark1(iters=10)
def fetch_webpage1(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


if __name__ == '__main__':
    print(fetch_webpage1("https://google.com"))
