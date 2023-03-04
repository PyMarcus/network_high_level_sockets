from socketserver import BaseRequestHandler, TCPServer


class EchoHandler(BaseRequestHandler):
    def handle(self) -> None:
        print(f"Got connection from {self.client_address}")
        while True:
            message = self.request.recv(8192)
            if not message:
                break
            print(f"Received: {message.decode()}")
            self.request.send(message)


if __name__ == '__main__':
    from threading import Thread
    NWORKERS = 16
    serv = TCPServer(('', 22000), EchoHandler)
    # TCPServer.allow_reuse_address = True
    for n in range(NWORKERS):
        t = Thread(target=serv.serve_forever)
        t.daemon = True
        t.start()
    serv.serve_forever()
