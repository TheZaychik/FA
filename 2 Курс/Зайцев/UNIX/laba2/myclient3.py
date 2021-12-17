#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
try:
    sock.connect(('localhost', 9090))
except ConnectionRefusedError as c:
    print(c)
    print("В соединении отказано")
    exit()

try:
    promt=input("Введите данные:")
except KeyboardInterrupt as k:
    print(k)
    print("Stop program")
    exit()

try:
    result=sock.send(promt.encode())
    if not result:
        raise Exception("нет данных!")
except Exception as e:
    print(e)
    exit()

try:
    data = sock.recv(1024).decode("utf8")
    if (len(data)==0):
        raise Exception("нет данных или потеря связи!")
except ConnectionResetError as e:
    print(e)
    print("lost connection from server")
    sock.close()
    exit()
except Exception as s:
    print(s)
    sock.close()
    exit()



sock.close()

print(data)
print(len(data))
