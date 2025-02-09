#!/usr/bin/env python3

try:
    import os
    from http.server import BaseHTTPRequestHandler, HTTPServer
except Exception as e:
    print(f'[ERROR] {e}')

COLOR = os.environ.get('COLOR', 'no color!')
print(f'COLOR is {COLOR}')

PORT = int(os.environ.get('PORT', '8080'))
print(f'PORT is {PORT}')

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/ping':
            self.send_response(200)
            self.end_headers()
            return
        header = self.headers.get('statuscode-header')
        if header is not None:
            if header == '200':
                self.send_response(200)
            if header == '500':
                self.send_response(500)
            if header == '503':
                self.send_response(503)
        else:
            self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(COLOR, 'utf8'))

print('starting server...')
httpd = HTTPServer(('', PORT), Handler)
print('running server...')
httpd.serve_forever()
