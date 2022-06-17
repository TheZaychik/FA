#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('привет, мир!'.encode())


try:
    data = sock.recv(1024).decode("utf8")
except ConnectionResetError as e:
    print(e)
    print("lost connection from server")
    exit()

sock.close()

print(data)

