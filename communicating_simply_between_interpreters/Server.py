import time
from multiprocessing.connection import Listener
import traceback


def echo_client(conn):
    try:
        while True:
            print(conn)
            message = conn.recv()
            print(message)
            conn.send(message)
    except EOFError as e:
        print(f"Connection closed {e}")


def echo_server(addr, authkey: bytes):
    server = Listener(addr, authkey=authkey)
    while True:
        try:
            client = server.accept()
            echo_client(client)
        except Exception:
            traceback.print_exc()


if __name__ == '__main__':
    echo_server(('', 23000), authkey=b'peekaboo')
