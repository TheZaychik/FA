import json
import socket
import props

sock = socket.socket()
host, port = 'localhost', props.PORT
sock.connect((host, int(port)))

request = {'Town': 'Samara'}
sock.send(bytes(json.dumps(request).encode()))
response = json.loads(sock.recv(1024).decode('UTF-8'))
print(response)
sock.close()
