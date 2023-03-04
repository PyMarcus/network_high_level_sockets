import cgi
from typing import List, Callable
from wsgiref.simple_server import make_server


def not_found_404(environ, start_response) -> List[bytes]:
    start_response('404 not found', [('content-type', 'text/plain')])
    return [b'Not found']


class PathDispacher:
    def __init__(self) -> None:
        self.pathmap = {}

    def __call__(self, environ, start_response, *args, **kwargs):
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'], environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = {key: params.getvalue(key) for key in params}
        handler = self.pathmap.get((method, path), not_found_404)
        return handler(environ, start_response)

    def register(self, method, path, function) -> Callable:
        self.pathmap[method.lower(), path] = function
        return function

    def server(self) -> None:
        httpd = make_server('', 8080, self)
        print("Serving on port 8080")
        httpd.serve_forever()
