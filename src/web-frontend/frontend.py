from http.server import SimpleHTTPRequestHandler, HTTPServer


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "app/index.html"
        elif self.path == "/style.css":
            self.path = "app/style.css"
        elif self.path == "/scan.js":
            self.path = "app/scan.js"
        return SimpleHTTPRequestHandler.do_GET(self)


def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ("", 8080)
    httpd = server_class(server_address, handler_class)
    print("Server started at http://localhost:8080")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
