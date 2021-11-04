import socket
import threading

print('Введите хост')
# host = input()
host = 'localhost'
open_ports = []


def thread_scan1():
    with socket.socket() as sock:
        for port in range(0, 32768):
            res = sock.connect_ex((host, port))
            if res == 0:
                open_ports.append(port)


def thread_scan2():
    with socket.socket() as sock:
        for port in range(32768, 65536):
            res = sock.connect_ex((host, port))
            if res == 0:
                open_ports.append(port)


p1 = threading.Thread(target=thread_scan1(), name="t1", args=["1"])
p2 = threading.Thread(target=thread_scan2(), name="t2", args=["2"])
p1.start()
p2.start()
p1.join()
p2.join()

open_ports.sort()
for op in open_ports:
    print(f'Порт {op} открыт')
