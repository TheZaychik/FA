import json
import socket
import logging
import hashlib
from datetime import datetime
import props
import threading

LOGIN = 'admin'
PASSWD = hashlib.sha256('1234'.encode()).hexdigest()
logging.basicConfig(filename='echo-server.log')
logger = logging.getLogger('echo-server')
logger.setLevel(logging.DEBUG)

sock = socket.socket()
sock.bind(('', props.PORT))
sock.listen(5)


def client_serve(conn, addr):
    creds = json.loads(conn.recv(1024).decode('UTF-8'))
    if creds['login'] == LOGIN and creds['passwd'] == PASSWD:
        logger.info(f' User {LOGIN} login on {datetime.now()}')
        conn.send(bytes('OK'.encode()))
    else:
        conn.close()
        sock.close()
        exit(0)

    while True:
        data = conn.recv(1024)
        text = data.decode('UTF-8') if data else None
        logger.info(f' Input {text} on {datetime.now()}')
        if text == 'exit' or not data:
            conn.send('CLOSE'.encode())
            conn.close()
            break
        else:
            conn.send(data.upper())


while True:
    conn, addr = sock.accept()
    print('accepted')
    t = threading.Thread(target=client_serve, args=[conn, addr])
    t.start()
    print('created')

sock.close()
