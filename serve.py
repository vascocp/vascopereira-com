import http.server, socketserver, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("127.0.0.1", 3456), handler) as httpd:
    httpd.serve_forever()
