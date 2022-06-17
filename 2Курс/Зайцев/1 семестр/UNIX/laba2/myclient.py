#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
promt='привет, мир!'
print(promt)
sock.send(promt.encode())

data = sock.recv(1024).decode()
sock.close()

print(data)

