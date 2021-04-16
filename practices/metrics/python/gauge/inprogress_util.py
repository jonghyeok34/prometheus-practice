import http.server
from prometheus_client import start_http_server, Gauge

INPROGRESS = Gauge('hello_worlds_inprogress', 'Number of Hello Worlds in progress.')
LAST = Gauge('hello_worlds_last_time_seconds', 'The last time a Hello World was served.')


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        INPROGRESS.inc()
        self.send_response(200)
        self.end_headers()
        LAST.set_to_current_time()
        self.wfile.write(b"Hello World")


if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('localhost', 8001), MyHandler)
    server.serve_forever()
