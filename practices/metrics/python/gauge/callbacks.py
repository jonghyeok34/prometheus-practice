import http.server
import time
from prometheus_client import start_http_server, Gauge

TIME = Gauge('time_seconds', 'The current time')
TIME.set_function(lambda: time.time())


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        TIME
        self.wfile.write(b"Hello World")


if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('localhost', 8001), MyHandler)
    server.serve_forever()
