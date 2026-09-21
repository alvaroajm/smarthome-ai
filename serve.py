#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
serve.py — servidor local para pré-visualizar o site gerado em dist/.

Uso:
    python3 serve.py            # http://localhost:8000
    python3 serve.py 8080       # outra porta
    python3 serve.py --watch    # regera o site a cada requisição
"""
from __future__ import annotations

import http.server
import socketserver
import subprocess
import sys
import webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
WATCH = "--watch" in sys.argv
PORT = next((int(a) for a in sys.argv[1:] if a.isdigit()), 8000)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIST), **kwargs)

    def do_GET(self):  # noqa: N802
        if WATCH:
            subprocess.run([sys.executable, str(ROOT / "build.py")],
                           capture_output=True, check=False)
        super().do_GET()

    def send_error(self, code, message=None, explain=None):  # noqa: N802
        if code == 404 and (DIST / "404.html").exists():
            self.error_message_format = (DIST / "404.html").read_text(encoding="utf-8")
        super().send_error(code, message, explain)

    def log_message(self, fmt, *args):  # noqa: N802
        sys.stderr.write(f"  {self.address_string()} · {fmt % args}\n")


def main() -> None:
    if not DIST.exists():
        subprocess.run([sys.executable, str(ROOT / "build.py")], check=True)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"\n🌐  SmartHome-AI em {url}   (Ctrl+C para parar)\n")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋  Encerrado.\n")


if __name__ == "__main__":
    main()
