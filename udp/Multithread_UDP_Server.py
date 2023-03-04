import time
from socketserver import ThreadingUDPServer, BaseRequestHandler


class TimeHandler(BaseRequestHandler):
    def handle(self) -> None:
        print(f"Connection from {self.client_address}")
        message, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('utf-8'), self.client_address)


if __name__ == '__main__':
    serv = ThreadingUDPServer(('', 22000), TimeHandler)
    serv.serve_forever()
