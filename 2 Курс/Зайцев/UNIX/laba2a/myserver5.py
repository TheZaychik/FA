#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
port = input("введите порт:")
if port == '':
    port = 9090
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', int(port)))

while True:
    print("слушаем порт", int(port))
    sock.listen(1)
    
    try:
        conn, addr = sock.accept()
    except KeyboardInterrupt as k:
        print(k)
        print("Stop program")
        exit()

    print('connection established:', addr[1])

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
            print("Конец связи")
            break
        
        if "sstop" in data:
           break
        conn.send(data.upper().encode())
    
    if "sstop" in data:
        break

conn.close()

