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
    serv = TCPServer(('', 21000), EchoHandler)
    serv.serve_forever()
