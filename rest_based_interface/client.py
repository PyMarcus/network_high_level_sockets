from RestBased import PathDispacher


_hello_resp = '''\
        <html>
        <head>
        <title>Hello ,{name}</title>
        </head>
        <body>
        <h1>Hello, {name}!</h1>
        </body>
        </html>'''

def hello(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    resp = _hello_resp.format(name=params.get('name'))
    yield resp.encode('utf-8')


if __name__ == '__main__':
    dispatcher = PathDispacher()
    dispatcher.register('GET', '/hello', hello)
    dispatcher.server()
