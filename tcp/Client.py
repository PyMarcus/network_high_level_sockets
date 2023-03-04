from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


def client() -> None:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 22000))
    for n in range(10):
        s.send(b"Test")
        print(s.recv(8192).decode())


if __name__ == '__main__':
    for n in range(10):
        t = Thread(target=client)
        t.start()
