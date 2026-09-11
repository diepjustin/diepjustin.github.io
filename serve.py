"""Tiny static server for previewing the homepage (mimics GitHub Pages).

Serves the repository root at http://127.0.0.1:8765/ — though the homepage
fetches nothing, so opening index.html directly works just as well.

    python3 serve.py            # port 8765
    python3 serve.py 8778       # any other port

Computes the root from __file__ because os.getcwd() is not always permitted in
the preview sandbox. Every data project that used to live in this repo and
need this server (ne-contracts, ne-ice, and so on) has since split into its own
repo; each keeps its own local preview setup now.
"""

import functools
import http.server
import os
import socketserver
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args), flush=True)


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    handler = functools.partial(Handler, directory=ROOT)
    with socketserver.TCPServer(("127.0.0.1", PORT), handler) as httpd:
        print(f"serving {ROOT} at http://127.0.0.1:{PORT}/", flush=True)
        httpd.serve_forever()
