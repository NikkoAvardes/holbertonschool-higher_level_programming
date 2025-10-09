#!/usr/bin/python3
"""Simple HTTP server exposing a few GET endpoints.

Provides a minimal HTTP server using http.server.BaseHTTPRequestHandler
with routes: /, /data, /info, /status and a 404 fallback.
"""

import http.server
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """HTTP request handler exposing a few simple GET routes.

    The handler implements do_GET to respond to a fixed set of paths:
    - /       : plain text greeting
    - /data   : JSON user data
    - /info   : JSON info about the API
    - /status : plain text 'Ok'
    Other paths return 404.
    """

    def do_GET(self):
        """Handle GET requests for predefined routes.

        The method checks the request path and writes the appropriate
        headers and body for each supported endpoint.
        """
        if self.path == '/':
            # Root endpoint: return plain text greeting.
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            # Data endpoint: return JSON payload with user data.
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server",
            }
            self.wfile.write(json.dumps(info).encode())
        elif self.path == '/status':
            # Status endpoint: return plain text status OK.
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            # Unknown endpoint: respond with 404.
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(
    server_class=http.server.HTTPServer,
    handler_class=SimpleHTTPRequestHandler,
):
    """ Create and start the HTTP server on port 8000."""
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    # Execute run when the script is run directly.
    run()
