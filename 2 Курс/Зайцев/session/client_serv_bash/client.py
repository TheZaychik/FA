import socket
import props

sock = socket.socket()
host, port = 'localhost', props.PORT
sock.connect((host, int(port)))

while True:
    cmd = input()
    if cmd == 'EXIT':
        break
    sock.send(bytes(cmd.encode()))
    data = sock.recv(1024).decode('UTF-8')
    print(data)
sock.close()
