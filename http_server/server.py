import http.server
import socketserver

class HttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')

with socketserver.TCPServer(('', 8080), HttpRequestHandler) as server:
    print('Server started on port 8080...')
    server.serve_forever()