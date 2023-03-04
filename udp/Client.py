import threading
from socket import AF_INET, SOCK_DGRAM, socket


def client() -> None:
    s = socket(AF_INET, SOCK_DGRAM)
    s.sendto(b"OK", ('localhost', 22000))
    print(s.recvfrom(8192))


if __name__ == '__main__':
    for n in range(100000):
        t = threading.Thread(target=client)
        t.start()
