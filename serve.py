import os, http.server, socketserver
PORT = int(os.environ.get('PORT', 8080))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
Handler = http.server.SimpleHTTPRequestHandler
Handler.log_message = lambda *a: None
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}", flush=True)
    httpd.serve_forever()
