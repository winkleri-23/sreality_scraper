import http.server
import socketserver
from http import HTTPStatus

        

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world')


with socketserver.TCPServer(('', 8080), HttpRequestHandler) as server:
    print('Server started on port 8080...')
    server.serve_forever()