#!/usr/bin/env python3
"""Simple HTTP server exposing a few GET endpoints."""

import http.server
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # Handle HTTP GET requests for predefined routes.
    def do_GET(self):
        # Root endpoint: return plain text greeting.
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        # Data endpoint: return JSON payload with user data.
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        # Info endpoint: return JSON with version and description.
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self.wfile.write(json.dumps(info).encode())
        # Status endpoint: return plain text status OK.
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Ok")
        # Unknown endpoint: respond with 404.
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(
    server_class=http.server.HTTPServer,
    handler_class=SimpleHTTPRequestHandler,
):
    # Create and start the HTTP server on port 8000.
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    # Execute run when the script is run directly.
    run()
