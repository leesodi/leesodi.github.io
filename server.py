import os, sys
os.chdir('/Users/user/Desktop/maker')
sys.argv = ['server.py', '3000']
from http.server import HTTPServer, SimpleHTTPRequestHandler
httpd = HTTPServer(('', 3000), SimpleHTTPRequestHandler)
httpd.serve_forever()
