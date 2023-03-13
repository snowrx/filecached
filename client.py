import socket

BUF = 0x100000

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(('127.0.0.1', 32356))
        while sock:
            command = input('> ')
            if command:
                sock.sendall(command.encode())
                data = sock.recv(BUF)
                print(data.decode())
except Exception as e:
    print(e)
