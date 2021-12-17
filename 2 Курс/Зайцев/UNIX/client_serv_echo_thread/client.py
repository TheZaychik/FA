import socket
import hashlib
import json
import props
sock = socket.socket()

print('Введите хост и порт через пробел')
host, port = input().split(' ')
# host, port = 'localhost', props.PORT

print('Введите логин и пароль через пробел')
login, passwd = input().split(' ')
creds = {'login': login, 'passwd': hashlib.sha256(passwd.encode()).hexdigest()}

# creds = {'login': 'admin', 'passwd': hashlib.sha256('1234'.encode()).hexdigest()}
sock.connect((host, int(port)))
sock.send(bytes(json.dumps(creds).encode()))
status = sock.recv(1024)
if status.decode('UTF-8') == 'OK':
    print('Добро пожаловать,', login)
    while True:
        sock.send(bytes(input().encode()))
        data = sock.recv(1024)
        print(str(data))
        if data.decode('UTF-8') == 'CLOSE':
            break
sock.close()
