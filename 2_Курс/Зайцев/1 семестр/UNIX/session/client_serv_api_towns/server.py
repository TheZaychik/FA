import json
import socket
import props

api = {
    'Moscow': '+15C',
    'Samara': '+10C',
    'Vologda': '+18C',
}

sock = socket.socket()
sock.bind(('', props.PORT))
sock.listen(1)
conn, addr = sock.accept()

data = conn.recv(1024)
request = json.loads(data.decode('UTF-8'))
response = api[request['Town']]
conn.send(json.dumps(response).encode())
sock.close()
