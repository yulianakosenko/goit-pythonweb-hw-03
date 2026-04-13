import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from datetime import datetime
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

BASE_DIR = Path()
STORAGE_FILE = BASE_DIR / "storage" / "data.json"

env = Environment(loader=FileSystemLoader("templates"))


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.render("index.html")

        elif self.path == "/message":
            self.render("message.html")

        elif self.path == "/read":
            self.show_messages()

        elif self.path.startswith("/static/"):
            self.serve_static()

        else:
            self.error_page()

    def do_POST(self):
        if self.path == "/message":
            length = int(self.headers["Content-Length"])
            body = self.rfile.read(length).decode()
            data = parse_qs(body)

            message = {
                "username": data.get("username", [""])[0],
                "message": data.get("message", [""])[0],
            }

            self.save_message(message)

            self.send_response(302)
            self.send_header("Location", "/")
            self.end_headers()

    # ---------- helpers ----------

    def render(self, template_name, context=None):
        template = env.get_template(template_name)
        html = template.render(context or {})

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

    def show_messages(self):
        if STORAGE_FILE.exists():
            with open(STORAGE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {}

        self.render("read.html", {"messages": data})

    def save_message(self, message):
        STORAGE_FILE.parent.mkdir(exist_ok=True)

        if STORAGE_FILE.exists():
            with open(STORAGE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = {}

        data[str(datetime.now())] = message

        with open(STORAGE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def serve_static(self):
        file_path = Path(__file__).parent / self.path.lstrip("/")

        if file_path.exists() and file_path.is_file():
            self.send_response(200)

            if file_path.suffix == ".css":
                self.send_header("Content-type", "text/css")
            elif file_path.suffix == ".png":
                self.send_header("Content-type", "image/png")

            self.end_headers()

            with open(file_path, "rb") as f:
                self.wfile.write(f.read())
        else:
            self.error_page()

    def error_page(self):
        template = env.get_template("error.html")
        html = template.render()

        self.send_response(404)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 3000), MyHandler)
    print("Server running on http://localhost:3000")
    server.serve_forever()