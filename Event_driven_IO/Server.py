import select
from AbstractServer import EventHandler
import socket
import time


def event_loop(handlers):
    while True:
        wants = [h for h in handlers if h.wants_to_receive()]
        sends = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants, sends, [])
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()


class UDPServer(EventHandler):
    def __init__(self, addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(addr)

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True

