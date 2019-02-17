from BaseHTTPServer import BaseHTTPRequestHandler
from parser import HttpRequest

from renderers import ACTIONS

SERIALIZER = 'swagger'

REQUESTS = []

def serialize(req):
    request = "{cmd} {path}".format(
        cmd=req.command,
        path=req.path
    )

    headers = "\n".join([": ".join((k,req.headers[k])) for k in req.headers])

    content_len = int(req.headers.getheader('content-length', 0))
    post_body = req.rfile.read(content_len)

    response = "\n".join((request, headers)) + "\n"

    if len(post_body) > 0:
        response += "\n" + post_body + "\n"

    return response


def render(requests):
    renderer = ACTIONS.get(SERIALIZER)

    return renderer(requests)


class DocHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text')
        self.end_headers()

        message = serialize(self)
        REQUESTS.append(HttpRequest(iter(message.split("\n"))))
        self.wfile.write(message)
        self.wfile.write("\n\n")
        self.wfile.write(render(REQUESTS))

    def do_POST(self):
        self.do_GET()

    def do_HEAD(self):
        self.do_GET()

    def do_PUT(self):
        self.do_GET()

    def do_OPTION(self):
        self.do_GET()
