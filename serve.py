"""Tiny static server for previewing any page in this repo (mimics GitHub Pages).

Serves the repository root, so every project loads at the path it has on
GitHub Pages: http://127.0.0.1:8765/ne-contracts/, /ne-ice/, /salary-search/,
and so on. Pages that fetch data with a relative URL need this; opening the
file directly does not work for them.

    python3 serve.py            # port 8765
    python3 serve.py 8778       # any other port

Computes the root from __file__ because os.getcwd() is not always permitted in
the preview sandbox. Replaces the identical copies that lived in
ne-contracts/scripts/serve_site.py and ne-ice/serve.py.
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
