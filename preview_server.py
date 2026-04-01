import os, http.server, socketserver
os.chdir('/Users/user/Desktop/leesodi.github.io-main')
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', 8080), handler) as httpd:
    httpd.serve_forever()
