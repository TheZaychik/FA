#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
try:
    conn, addr = sock.accept()
except KeyboardInterrupt as k:
    print(k)
    print("Stop program")
    exit()

print('connection established:', addr)

while True:

    try:
        data = conn.recv(1024).decode("utf8")
    except ConnectionResetError as e:
        print(e)
        print("lost connection from client")
        exit()
    except KeyboardInterrupt as k:
        print(k)
        print("Stop program")
        print("lost connection from client")
        exit()

    if not data:
        break

    conn.send(data.upper().encode())

conn.close()

