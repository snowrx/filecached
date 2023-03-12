import os
import socket
import hashlib
from functools import cache

PORT = 32356
NAME = 'default'
BUF = 0x100000

path = os.curdir + os.sep + NAME
if not os.path.isdir(path):
    os.makedirs(path)
os.chdir(path)
print(os.getcwd())


@cache
def hash(key: str):
    return hashlib.sha3_512(key.encode()).hexdigest()


def read(key: str):
    if key == '_':
        e = os.listdir()
        if len(e) == 0:
            return 'db is empty'
        l = []
        for i in e:
            with open(i) as f:
                l.append(f.read())
        l.sort()
        return '\n'.join(l)
    if key:
        hk = hash(key)
        if not os.path.isfile(hk):
            return 'key not found'
        with open(hk) as f:
            return f.read()
    return 'key is empty'


def write(key: str, value: str):
    if not key:
        return 'key is empty'
    hk = hash(key)
    if not value:
        if not os.path.isfile(hk):
            return 'key not found'
        os.remove(hk)
        return key
    with open(hk, 'w') as f:
        f.write('='.join([key, value]))
    return key


def processor(command: str):
    c = command.split('=', 1)
    l = []
    for i in c:
        l.append(i.strip())
    if len(l) == 2:
        return write(l[0], l[1])
    return read(l[0])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('', PORT))
    sock.listen(1)
    while sock:
        try:
            client, addr = sock.accept()
            while client:
                data = client.recv(BUF)
                if not data:
                    client.sendall('empty data received'.encode())
                else:
                    command = data.decode()
                    p = processor(command)
                    client.sendall(p.encode())
            client.close()
        except Exception as e:
            print(e)
